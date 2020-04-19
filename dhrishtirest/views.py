from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from dhrishtirest.forms import SearchForm
from sources.reddit.reddit_connector import RedditConnector
from nlp.sentiment import SentimentAnalyser


reddit_connector = RedditConnector()
sentiment = SentimentAnalyser()


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


@require_http_methods(["POST"])
def load_subreddit_top(request):
    if not request.POST:
        return HttpResponse('there is no endpoint for a GET request.')
    form = SearchForm(request.POST)
    if form.is_valid():
        subreddit = form.cleaned_data['subreddit']
        limit = form.cleaned_data['limit']
        order = form.cleaned_data['order']
        if order == 'top':
            reddit_connector.fetch_top_posts(subreddit, limit)
            return HttpResponse("Gathered the top %d results from /r/%s" % (limit, subreddit))
        if order == 'latest':
            reddit_connector.fetch_latest_posts(subreddit, limit)
            return HttpResponse("Gathered data from the latest %d results from /r/%s" % (limit, subreddit))

# @require_http_methods(["POST"])
# def load_subreddit_latest(request):
#     subreddit = request.POST['subreddit']
#     limit = request.POST['limit']
#     reddit_connector.fetch_latest_posts(subreddit, limit)
#     return HttpResponse("Gathered data from the latest %d results from /r/%s" % (limit, subreddit))


@require_http_methods(["GET"])
def view_submission_data(request, subreddit: str, limit: int):
    documents = reddit_connector.get_submissions(subreddit, limit)
    context = {
        'subreddit': subreddit,
        'documents': documents
    }
    return render(request, "dhrishtirest/subreddits.html", context)


@require_http_methods(["GET"])
def analyse_text(request, subreddit: str, limit: int):
    documents = reddit_connector.get_submissions(subreddit, limit)
    sentences_analysis = sentiment.analyse_text(subreddit, documents, "title")
    context = {
        'sentences_analysis': sentences_analysis
    }
    return render(request, "dhrishtirest/analysis.html", context)


@require_http_methods(["GET"])
def load_comments(request, submission_id: str, limit: int):
    reddit_connector.fetch_best_comments(submission_id, limit)
    return HttpResponse("fetched comments.")


@require_http_methods(["GET"])
def view_comments_data(request, submission_id: str, limit: int):
    documents = reddit_connector.get_comments(submission_id, limit)
    context = {
        'submission_id': submission_id,
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
