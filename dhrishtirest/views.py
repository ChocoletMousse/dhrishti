from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from sources.reddit.reddit_connector import RedditConnector
from nlp.sentiment import SentimentAnalyser
import json
import logging

reddit_connector = RedditConnector()
sentiment = SentimentAnalyser()


@require_http_methods(["POST"])
def load_analyse_subreddit_posts(request):
    if request.method == "POST":
        json_form = request.body.decode('utf-8')
        form = json.loads(json_form)
        logging.info(f"received the following data: {form}")
        submissions = reddit_connector.fetch_posts(form['subreddit'], form['order'], form['limit'])
        sentiment.analyse_submissions(submissions)
        return HttpResponse("Gathered the %s results from /r/%s" % (form['order'], form['subreddit']))
    else:
        return HttpResponse(f"Cannot use a {request.method} method for this endpoint.")


@require_http_methods(["GET"])
def get_submission_data(request):
    logging.info(f"received {request.method} request for reddit submissions data")
    documents = reddit_connector.get_submissions()
    return HttpResponse(documents)


@require_http_methods(["POST"])
def load_analyse_comments(request):
    if request.method == 'POST':
        json_body = request.body.decode('utf-8')
        json_submission = json.loads(json_body)
        logging.info(f"received the following data {json_submission}")
        submission_id = json_submission['submissionId']
        comments = reddit_connector.fetch_comments(submission_id, 5)
        sentiment.analyse_comments(comments)
        sentiment.analyse_entities_sentiment(comments)
        return HttpResponse("fetched comments.")
    else:
        return HttpResponse(f"Cannot use a {request.method} method for this endpoint.")


@require_http_methods(["GET"])
def get_comments_data(request):
    logging.info(f"received {request.method} request for reddit comments data")
    # hard coded to return 5 comments only
    documents = reddit_connector.get_comments()
    return HttpResponse(documents)


@require_http_methods(["GET"])
def get_comments_by_submission(request, submission_id: str):
    logging.info(f"received {request.method} request for reddit comments data")
    documents = reddit_connector.get_comments_by_submission(submission_id)
    return HttpResponse(documents)


# NOTE DEPRECATED
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
