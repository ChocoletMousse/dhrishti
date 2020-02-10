from django.shortcuts import render
from django.http import HttpResponse
from sources.reddit.reddit_connector import RedditConnector


reddit_connector = RedditConnector()


# Create your views here.
def index(request):
    return HttpResponse("This is the dhrishti index.")


def load_subreddit_top(request, subreddit, limit):
    reddit_connector.fetch_top_rated_posts(subreddit, limit)
    return HttpResponse("Gathering data from the top %d results from /r/%s" % (limit, subreddit))


def view_subreddit_top(request, subreddit, limit):
    reddit_connector.retrieve_docs_from_firestore(subreddit, limit)
    return HttpResponse("Retrieving the top %d posts from /r/%s" % (limit, subreddit))
