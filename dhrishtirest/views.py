from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from dhrishtirest.forms import SearchForm
from sources.reddit.reddit_connector import RedditConnector
from nlp.sentiment import SentimentAnalyser


reddit_connector = RedditConnector()
sentiment = SentimentAnalyser()
# TODO create a way navigate between submissions and comments


# Create your views here.
def index(request):
    return render(request, "dhrishtirest/index.html")


@require_http_methods(['GET'])
def search(request):
    search_form = SearchForm()
    context = {
        'search_form': search_form
    }
    return render(request, "dhrishtirest/search-reddit.html", context)


# TODO replace both responses with html page.
# TODO automatically retrieve comments and responses.
@require_http_methods(["POST"])
def load_subreddit_posts(request):
    if not request.POST:
        return HttpResponse('there is no endpoint for a GET request.')
    form = SearchForm(request.POST)
    if form.is_valid():
        subreddit = form.cleaned_data['subreddit']
        sub_limit = form.cleaned_data['submissions_limit']
        comments_limit = form.cleaned_data['comments_limit']
        responses_limit = form.cleaned_data['responses_limit']
        order = form.cleaned_data['order']
        if order == 'top':
            submissions = reddit_connector.fetch_top_posts(subreddit, sub_limit)
        if order == 'latest':
            submissions = reddit_connector.fetch_latest_posts(subreddit, sub_limit)
        sentiment.analyse_submissions(submissions)
        comments = reddit_connector.fetch_comments(submissions, comments_limit)
        sentiment.analyse_comments(comments)
        responses = reddit_connector.fetch_responses(comments, responses_limit)
        sentiment.analyse_responses(responses)
        all_comments = comments + responses
        sentiment.analyse_entities(all_comments)
        return HttpResponse("Gathered the top results from /r/%s" % (subreddit))


@require_http_methods(["GET"])
def get_dhrishti_data(request):
    return HttpResponse('still needs work lmao')


@require_http_methods(["GET"])
def get_submission_data(request, limit: int = 10):
    documents = reddit_connector.get_submissions(limit)
    context = {
        'documents': documents
    }
    return render(request, "dhrishtirest/subreddits.html", context)


@require_http_methods(["GET"])
def analyse_text(request, subreddit: str, limit: int):
    documents = reddit_connector.get_submissions(limit)
    sentences_analysis = sentiment.analyse_text(subreddit, documents, "title")
    context = {
        'sentences_analysis': sentences_analysis
    }
    return render(request, "dhrishtirest/analysis.html", context)

# ========================================================================================== #
#                                   TO BE REPLACED                                           #
# ========================================================================================== #


@require_http_methods(["GET"])
def load_comments(request, submission_id: str, limit: int):
    reddit_connector.fetch_best_comments(submission_id, limit)
    return HttpResponse("fetched comments.")


@require_http_methods(["GET"])
def get_comments_data(request, limit: int):
    documents = reddit_connector.get_comments(limit)
    context = {
        'documents': documents
    }
    return render(request, "dhrishtirest/comments.html", context)


@require_http_methods(["GET"])
def analyse_comments(request, submission_id: str, limit: int):
    documents = reddit_connector.get_comments(submission_id, limit)
    sentences_analysis = sentiment.analyse_text(submission_id, documents, "comment")
    context = {
        'sentences_analysis': sentences_analysis
    }
    return render(request, "dhrishtirest/analysis.html", context)


@require_http_methods(["GET"])
def load_replies(request, submission_id: str, limit: int):
    replies = reddit_connector.fetch_best_responses(submission_id, limit)
    return HttpResponse("fetched replies %s" % (str(replies)))
