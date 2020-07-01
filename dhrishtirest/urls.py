from django.urls import path
from dhrishtirest import views

urlpatterns = [
    # path("", views.index, name="index"),
    # path("search-reddit", views.search, name="search-reddit"),
    path("search", views.load_subreddit_posts, name="load-reddit-submissions"),
    # path("insights", views.get_dhrishti_data, name="get-insights"),
    path("data", views.get_submission_data, name="get-data"),
    # path("view/submissions/<str:subreddit>/<int:limit>", views.view_submission_data, name="view-saved-submissions"),
    # path("analyse/submissions/<str:subreddit>/<int:limit>", views.analyse_text, name="analyse-submission-titles"),
    # path("comments/<str:submission_id>/<int:limit>", views.load_comments, name="load-submission-comments"),
    # path("view/comments/<str:submission_id>/<int:limit>", views.view_comments_data, name="view-saved-comments"),
    # path("analyse/comments/<str:submission_id>/<int:limit>", views.analyse_comments, name="analyse-sentiment-comments"),
    # path("replies/<str:submission_id>/<int:limit>", views.load_replies, name="load-comment-replies"),
]
