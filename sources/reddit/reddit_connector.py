import os
from sinks.database import FirestoreReddit
from utils import constants, schema
from praw import Reddit
from praw.models import Comment
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
        self._reddit_instance = Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.instance
        )

    def incorrect_comment_length(self, comment: Comment) -> bool:
        too_long = len(comment.body) > constants.MAX_COMMENT_LENGTH
        too_short = len(comment.body) > constants.MIN_COMMENT_LENGTH
        return too_long or too_short

    def fetch_top_posts(self, subreddit_name: str, limit: int):
        """Write the retrieved subreddit submissions to FirestoreReddit."""
        logging.info(f"reddit connector: retreiving top {limit} posts from /r/{subreddit_name}")
        subreddit_obj = self._reddit_instance.subreddit(subreddit_name)
        submissions = subreddit_obj.top(limit=limit)
        for submission in submissions:
            item = schema.reddit_submission_schema(submission)
            self.write_submission(subreddit_name, submission.id, item)

    def fetch_latest_posts(self, subreddit_name: str, limit: int):
        """Write the retrieved subreddit submissions to FirestoreReddit."""
        logging.info(f"reddit connector: retreiving latest {limit} posts from /r/{subreddit_name}")
        subreddit_obj = self._reddit_instance.subreddit(subreddit_name)
        submissions = subreddit_obj.new(limit=limit)
        for submission in submissions:
            item = schema.reddit_submission_schema(submission)
            self.write_submission(subreddit_name, submission.id, item)

    def fetch_best_comments(self, submission_id: str, limit: int):
        """Write the first level comments on a submission to FirestoreReddit."""
        logging.info(f"reddit connector: fetching comments for subreddit id {submission_id}")
        submission_obj = self._reddit_instance.submission(submission_id)
        comment_count = 0
        submission_obj.comment_sort = 'best'
        submission_obj.comments.replace_more(limit=5)
        for comment in submission_obj.comments:
            if comment_count == limit:
                break
            if self.incorrect_comment_length(comment):
                continue
            item = schema.reddit_comment_schema(comment)
            self.write_comment(submission_id, comment.id, item)
            comment_count += 1

    # def fetch_replies(self, submission_id: str, comment_id: str):
    #     comment_obj = self._reddit_instance.comment(comment_id)
    #     replies = comment.replies()
    #     replies.replace_more()
