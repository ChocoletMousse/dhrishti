import os
from sinks.database import FirestoreReddit
from utils import constants, schema
from praw import Reddit
import logging


class RedditConnector(FirestoreReddit):
    """Class for retrieving Reddit data."""

    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_SECRET")
    instance = os.getenv("REDDIT_APPLICATION")

    def __init__(self):
        super().__init__()
        self._authenticate()

    def _authenticate(self):
        logging.info("reddit connector: authenticating reddit connector")
        self.reddit_instance = Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.instance
        )

    def fetch_top_posts(self, subreddit_name: str, limit: int):
        """Write the retrieved subreddit submissions to FirestoreReddit."""
        logging.info(f"reddit connector: retreiving top {limit} posts from /r/{subreddit_name}")
        subreddit_obj = self.reddit_instance.subreddit(subreddit_name)
        submissions = subreddit_obj.top(limit=limit)
        for submission in submissions:
            item = schema.reddit_submission_schema(submission)
            self.write_submission(subreddit_name, submission.id, item)

    def fetch_latest_posts(self, subreddit_name: str, limit: int):
        """Write the retrieved subreddit submissions to FirestoreReddit."""
        logging.info(f"reddit connector: retreiving latest {limit} posts from /r/{subreddit_name}")
        subreddit_obj = self.reddit_instance.subreddit(subreddit_name)
        submissions = subreddit_obj.new(limit=limit)
        for submission in submissions:
            item = schema.reddit_submission_schema(submission)
            self.write_submission(subreddit_name, submission.id, item)

    def fetch_best_comments(self, submission_id: str):
        """Write the first level comments on a submission to FirestoreReddit."""
        logging.info(f"reddit connector: fetching comments for subreddit id {submission_id}")
        submission_obj = self.reddit_instance.submission(submission_id)
        comment_count = 0
        for comment in submission_obj.comments:
            if comment_count == constants.MAX_COMMENTS:
                break
            if len(comment.body) > constants.MAX_COMMENT_LENGTH:
                continue
            item = schema.reddit_comment_schema(comment)
            self.write_comment(submission_id, comment.id, item)
            comment_count += 1
