from django.urls import path
from dhrishtirest import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:subreddit>/top/<int:limit>", views.load_subreddit_top, name="load-subreddit-top"),
    path("<str:subreddit>/latest/<int:limit>", views.load_subreddit_latest, name="load-subreddit-latest"),
    path("<str:subreddit>/<int:limit>", views.view_subreddit_data, name="get-subreddit-top"),
    path("<str:subreddit>/analyse/<int:limit>", views.analyse_sentiment, name="analyse-sentiment-top"),
    path("<str:submission_id>/comments", views.load_comments, name="load-submission-comments")
]
