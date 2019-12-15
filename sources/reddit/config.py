import os
import praw
from praw import Reddit


class RedditConnector:
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_SECRET")
    instance = os.getenv("REDDIT_APPLICATION")
    _reddit_instance = None

    def __init__(self):
        self._authenticate()

    def _authenticate(self):
        self._reddit_instance = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.instance
        )

    def get_reddit_connector(self) -> Reddit:
        return self._reddit_instance
