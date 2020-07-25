from django.urls import path
from dhrishtirest import views

urlpatterns = [
    path("search", views.load_subreddit_posts, name="load-reddit-submissions"),
    path("data/submissions", views.get_submission_data, name="get-submission-data"),
    path("data/comments/<str:submission_id>/<int:limit>", views.load_comments, name="load-submission-comments"),
    path("data/comments", views.get_comments_data, name="view-saved-comments")
]
