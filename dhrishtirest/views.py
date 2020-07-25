from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from sources.reddit.reddit_connector import RedditConnector
from nlp.sentiment import SentimentAnalyser
import json
import logging

reddit_connector = RedditConnector()
sentiment = SentimentAnalyser()
# TODO create a way navigate between submissions and comments


# Create your views here.
@require_http_methods(["POST"])
def load_subreddit_posts(request):
    if request.method == "POST":
        jsonForm = request.body.decode('utf-8')
        form = json.loads(jsonForm)
        logging.info(f"received the following data: {form}")
        subreddit = form['subreddit']
        sub_limit = form['limit']
        order = form['order']

        submissions = reddit_connector.fetch_posts(subreddit, order, sub_limit)
        sentiment.analyse_submissions(submissions)
        # comments = reddit_connector.fetch_comments(submissions)
        # sentiment.analyse_comments(comments)
        # responses = reddit_connector.fetch_responses(comments)
        # sentiment.analyse_responses(responses)

        return HttpResponse("Gathered the %s results from /r/%s" % (order, subreddit))
    else:
        return HttpResponse(f"Cannot use a {request.method} method for this endpoint.")


@require_http_methods(["GET"])
def get_submission_data(request):
    logging.info(f"received {request.method} request for reddit submissions data")
    documents = reddit_connector.get_submissions()
    return HttpResponse(documents)


# @require_http_methods(["GET"])
# def analyse_text(request, subreddit: str, limit: int):
#     documents = reddit_connector.get_submissions(limit)
#     sentences_analysis = sentiment.analyse_text(subreddit, documents, "title")
#     context = {
#         'sentences_analysis': sentences_analysis
#     }
#     return render(request, "dhrishtirest/analysis.html", context)


@require_http_methods(["GET"])
def load_comments(request, submission_id: str):
    comments = reddit_connector.fetch_comments(submission_id, 5)
    sentiment.analyse_comments(comments)
    return HttpResponse("fetched comments.")


@require_http_methods(["GET"])
def get_comments_data(request, limit: int):
    documents = reddit_connector.get_comments(limit)
    context = {
        'documents': documents
    }
    return render(request, "dhrishtirest/comments.html", context)


# @require_http_methods(["GET"])
# def analyse_comments(request, submission_id: str, limit: int):
#     documents = reddit_connector.get_comments(submission_id, limit)
#     sentences_analysis = sentiment.analyse_text(submission_id, documents, "comment")
#     context = {
#         'sentences_analysis': sentences_analysis
#     }
#     return render(request, "dhrishtirest/analysis.html", context)


@require_http_methods(["GET"])
def load_replies(request, submission_id: str, limit: int):
    replies = reddit_connector.fetch_best_responses(submission_id, limit)
    return HttpResponse("fetched replies %s" % (str(replies)))
