from django.urls import path
from dhrishtirest import views

urlpatterns = [
    path("search", views.load_analyse_subreddit_posts, name="load-reddit-submissions"),
    path("data/submissions", views.get_submission_data, name="get-submission-data"),
    path(
        "search/comments", views.load_analyse_comments, name="load-submission-comments"
    ),
    path("data/comments", views.get_comments_data, name="get-comments-data"),
    path(
        "data/comments/<str:submission_id>",
        views.get_comments_by_submission,
        name="get-comments-data-for-submission",
    ),
]
