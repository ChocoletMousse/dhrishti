from django.urls import path
from dhrishtirest import views

urlpatterns = [
    path("", views.index, name="index"),
    path("top/<str:subreddit>/<int:limit>", views.load_subreddit_top, name="load-subreddit-top"),
    path("latest/<str:subreddit>/<int:limit>", views.load_subreddit_latest, name="load-subreddit-latest"),
    path("<str:subreddit>/<int:limit>", views.view_subreddit_data, name="saved-submissions"),
    path("analyse/submission/<str:subreddit>/<int:limit>", views.analyse_text, name="analyse-sentiment-titles"),
    path("comments/<str:submission_id>", views.load_comments, name="load-submission-comments"),
    path("<str:submission_id>/<int:limit>", views.view_comments_data, name="saved-comments"),
    path("analyse/comments/<str:submission_id>/<int:limit>", views.analyse_comments, name="analyse-sentiment-comments")
]
