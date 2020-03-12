from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from sources.reddit.reddit_connector import RedditConnector
from nlp.sentiment import SentimentAnalyser
import json


reddit_connector = RedditConnector()
sentiment = SentimentAnalyser()


# Create your views here.
def index(request):
    return render(request, "dhrishtirest/index.html")


@require_http_methods(["GET"])
def load_subreddit_top(request, subreddit, limit):
    reddit_connector.fetch_top_posts(subreddit, limit)
    return HttpResponse("Gathered data from the top %d results from /r/%s" % (limit, subreddit))


@require_http_methods(["GET"])
def load_subreddit_latest(request, subreddit, limit):
    reddit_connector.fetch_latest_posts(subreddit, limit)
    return HttpResponse("Gathered data from the latest %d results from /r/%s" % (limit, subreddit))


@require_http_methods(["GET"])
def view_subreddit_top(request, subreddit, limit):
    documents = reddit_connector.get_docs_from_firestore(subreddit, limit)
    return HttpResponse("<html><head><body>%s</body></head></html>" % (json.dumps(documents)))


@require_http_methods(["GET"])
def analyse_sentiment(request, subreddit, limit):
    documents = reddit_connector.get_docs_from_firestore(subreddit, limit)
    sentences_analysis = sentiment.analyse_titles(subreddit, documents)
    context = {
        "sentences_analysis": sentences_analysis
    }
    return render(request, "dhrishtirest/analysis.html", context)
