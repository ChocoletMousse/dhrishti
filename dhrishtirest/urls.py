from django.urls import path
from dhrishtirest import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:subreddit>/<int:limit>", views.load_subreddit_top, name="load-subreddit-top"),
]
