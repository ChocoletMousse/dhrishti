import os
import praw
from sinks.database import Database
from sinks import schema
from praw import Reddit


class RedditConnector(Database):
    """Self-contained methods for Reddit data"""
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_SECRET")
    instance = os.getenv("REDDIT_APPLICATION")

    def __init__(self):
        super().__init__()
        self._authenticate()

    def _authenticate(self):
        self._reddit_instance = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.instance
        )

    def get_reddit_connector(self) -> Reddit:
        return self._reddit_instance

    def write_top_rated_posts(self, subreddit_name: str, limit: int) -> Reddit:
        """Write the retrieved submissions for the subreddit provided to firestore database"""
        self.collection = subreddit_name
        subreddit = self._reddit_instance.subreddit(subreddit_name)
        submissions = subreddit.top(limit=limit)
        for submission in submissions:
            self.document = submission.title
            self.write_to_firestore(schema.reddit_submission_schema(submission))
