# Manga Translator Project. Check out the project on https://twitmanga-translator.wl.r.appspot.com/
# You can find the Twitter replies by visiting https://twitter.com/MangaTranslator
# If you would like to test the website, please be aware that the reply will be actually sent to the Twitter artist.
# Explanation of files:
# - main.py: Flask app that displays a feed of tweets when the website is loaded. When a user clicks on "Reply with
#     Translation", Manga Translator Bot will reply to the tweet on the right with the text in the textbox.
# - mangafeed.py: Contains the class MangaFeed, which searches for relevant manga tweets and creates a tweets object to
#     be used to load the webpage.
# - secret.py: contains tweepy API keys for Manga Translator Bot.
# - __init__.py: empty file that is needed in order to smoothly import python files from the same directory (i.e.
#     mangafeed, secret) without giving warnings.


from flask import Flask, render_template, request
import tweepy
import json
import secret
from mangafeed import MangaFeed


def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)


app = Flask(__name__)
auth = tweepy.OAuthHandler(secret.consumer_key, secret.consumer_key_secret)
auth.set_access_token(secret.access_token, secret.access_token_secret)
api = tweepy.API(auth)


@app.route("/")
def load_home():
    recent_tweets = api.user_timeline()
    recent_replies = []
    for tweet in recent_tweets:
        if tweet._json["text"][0:1] == "@":
            recent_replies.append(tweet._json["id_str"])
    recent_replies_embed = []
    for tweet in recent_replies:
        recent_replies_embed.append(api.get_oembed(id=tweet, maxwidth=600, align="center")["html"])
    return render_template("home.html", tweets=recent_replies_embed)


@app.route("/login", methods=["POST"])
def log_in():
    password = request.form.get("password")
    if password == secret.password:
        feed = MangaFeed(api)
        tweets = feed.tweets  # dictionary with "url", "post_id", "handle", "num_images", "embed_html", "rank"
        return render_template("feedtemplate.html", tweets=tweets)
    else:
        return render_template("failed_login.html")

# def load_feed():
#     feed = MangaFeed(api)
#     tweets = feed.tweets  # dictionary with "url", "post_id", "handle", "num_images", "embed_html", "rank"
#     return render_template("feedtemplate.html", tweets=tweets)


@app.route("/send_reply")
def send_reply():
    user_handle = request.args.get("handle")
    text = request.args.get("translation")
    post_id = request.args.get("post_id")
    tweet_json = api.get_status(id=post_id)._json
    # print(pretty(tweet_json))
    if not tweet_json["retweeted"]:
        tweet_reply(user_handle, post_id, text)
        return render_template("confirmation.html", user_handle=user_handle, text=text)
    else:
        return render_template("confirmation.html", user_handle=user_handle,
                               text="You already translated for this tweet.")


def tweet_reply(user_handle, post_id, text):
    text_thread_header = "@" + user_handle + \
                         " すみません、勝手ながらあなたの漫画が気に入ったのでセリフを英語に翻訳させていただきました！＊完全手動です。\n" \
                         "I translated your manga to English! Here's the english translation below: "
    text_thread = []
    text_length = len(text)
    num_tweets = text_length // 240
    if text_length % 240 > 0:
        num_tweets = num_tweets + 1
    for n in range(num_tweets):
        if len(text) >= 240:
            test_text_split = text[0:240]
            text_thread.append(test_text_split)
            text = text[240:]
        else:
            text_thread.append(text)
    api.retweet(id=post_id)  # used to check whether I already translated a post
    bot_tweet = api.update_status(status=text_thread_header, in_reply_to_status_id=post_id)
    for text in text_thread:
        bot_tweet = api.update_status(status=text, in_reply_to_status_id=bot_tweet._json["id"])


if __name__ == "__main__":
    app.run(host="localhost", port=8080)
