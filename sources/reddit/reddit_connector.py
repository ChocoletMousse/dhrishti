import os
from sinks.database import Database
from sinks import schema
from praw import Reddit


class RedditConnector(Database):
    """Class for retrieving Reddit data."""

    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_SECRET")
    instance = os.getenv("REDDIT_APPLICATION")

    def __init__(self):
        super().__init__()
        self._authenticate()

    def _authenticate(self):
        self._reddit_instance = Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.instance
        )

    def fetch_top_rated_posts(self, subreddit_name: str, limit: int):
        """Write the retrieved subreddit submissions to Firestore."""
        subreddit_obj = self._reddit_instance.subreddit(subreddit_name)
        submissions = subreddit_obj.top(limit=limit)
        for submission in submissions:
            item = schema.reddit_submission_schema(submission)
            self.write_to_firestore(subreddit_name, submission.id, item)
