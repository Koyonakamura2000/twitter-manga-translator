import json

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)


class MangaFeed:
    # api = Tweepy api object, term = search term (default "漫画")
    def __init__(self, api):
        # want list of recent tweets by artists that Manga Translator Bot follows
        self.api = api
        self.id = self.api.me()._json["id_str"]
        self.listId = "1334734045880623105"  # static listId - manually change if I make a new list
        self.tweets = self.__get_tweets()

    # gets tweets from the "manga" list, filtering out posts with less than 3 images

    def __get_tweets(self):
        tweetObjs = self.api.list_timeline(list_id=self.listId, count=100)
        filteredTweets = []
        rank = 1
        for tweetObj in tweetObjs:
            tweet = tweetObj._json
            if "media" in tweet["entities"]:
                if len(tweet["extended_entities"]["media"]) >= 3:
                    # print(pretty(tweet))
                    # print("----------")
                    # print("----------")
                    # print("----------")
                    tweetInfo = {}
                    tweetInfo["rank"] = rank
                    tweetInfo["url"] = tweet["extended_entities"]["media"][0]["expanded_url"][:-8]
                    tweetInfo["post_id"] = tweet["id_str"]
                    if len(tweet["entities"]["user_mentions"]) > 0:
                        tweetInfo["handle"] = tweet["entities"]["user_mentions"][0]["screen_name"]
                    else:
                        tweetInfo["handle"] = tweet["user"]["screen_name"]
                    tweetInfo["num_images"] = len(tweet["extended_entities"]["media"])
                    tweetInfo["embed_html"] = \
                        self.api.get_oembed(url=tweetInfo["url"], maxwidth=500, align="center")["html"]
                    # if necessary, tweetInfo["user"]["id_str"] gives user id
                    filteredTweets.append(tweetInfo)
                    rank = rank + 1
        return filteredTweets
