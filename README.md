[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=3747208&assignment_repo_type=AssignmentRepo)
# Homework 7 - Flask with User Input and APIs
Due: 7 December, 9am

We can be flexible out this deadline; we're suggesting the 7th as a good milestone toward having a strong project.

What to hand in: 
- A link to your GitHub repository, including all of your code, including any images, HTML templates, CSS, and app.yaml files we need to run your program.
- You can use Canvas as a backup turn in, but if so, please zip all the files rather than turning them in separately -- especially because folders matter!
- If you get your code running on Google Cloud, we'd love a link to it there too!

Even if you are working with a partner on your project, this is an individual assignment. You are, as always, encouraged to collaborate - but you should write your own code and be able to explain all code in your assignment in your own words.

# The assignment
This assignment is a bit different. You goal is to write a Flask App that
1. Accesses an API (not the sunrise/sunset API or the National Weather Service API) to retrieve results.
2. Accept user input that affects what it searches for and/or what results it shows.

This is written to be as flexible as possible, so that you can use any of the following as a starting point:
- HW6 (in which case, the most basic version of the app will search Flickr for a tag and display some images.) 
- Your HW5 Part 2
- Some other API, if your project idea has changed since HW5 Part 2

and get it running in Flask. 

We encourage you to explore a bit more. Are there unique searches you can build in your app that are hard to do in the interface of the site whose API you use? Something fun related to your interests?

We also encourage you to get your app running on Google's servers (this is useful practice if you want to run your project on Google Cloud), but this is not required. Still, this is a good time to connect with us in office hours work out any challenges you are having with deploying an app to Google's servers - as we mentioned in class, there are a bunch of small, idiosyncratic things that can go awry with getting their tools set up and configured.

# Tips
1. If you use your HW6 as a starting point, if your code calls  `flickr.photos.getInfo` on the Flickr API for many photos, Google will almost certainly kill your app for taking too long to run. Try to do searches that either avoid calling that method for each photo, or focus on only on a few photos.
2. We followed all of the steps required for this homework in labs, including the Live Data lab in S12, the Flask Lab in S14, the Google Cloud lab in S15, and the Flask & Forms lab in S16. You can use those slides (and corresponding code) as a guide for working with your API!