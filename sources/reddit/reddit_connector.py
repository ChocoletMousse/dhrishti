import os
from sinks.database import FirestoreReddit
from utils import constants, schema
from praw import Reddit
from praw.models import Comment
import logging


class RedditConnector(FirestoreReddit):
    """Class for retrieving Reddit data."""

    def __init__(self):
        super().__init__()
        self._authenticate()

    def _authenticate(self):
        logging.info("reddit connector: authenticating reddit connector")
        self._reddit_instance = Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_SECRET"),
            user_agent=os.getenv("REDDIT_APPLICATION"),
        )

    def incorrect_comment_length(self, comment: Comment) -> bool:
        too_long = len(comment.body) > constants.MAX_COMMENT_LENGTH
        too_short = len(comment.body) < constants.MIN_COMMENT_LENGTH
        return too_long or too_short

    def fetch_posts(self, subreddit_name: str, order: str, limit: int) -> list:
        """Write the retrieved subreddit submissions to FirestoreReddit."""
        logging.info(
            f"reddit connector: retreiving {order} {limit} posts from /r/{subreddit_name}"
        )
        subreddit_obj = self._reddit_instance.subreddit(subreddit_name)
        if order == "top":
            submissions = subreddit_obj.top(limit=limit)
        elif order == "latest":
            submissions = subreddit_obj.new(limit=limit)
        elif order == "controversial":
            submissions = subreddit_obj.controversial(limit=limit)
        submission_list = []
        for submission in submissions:
            item = schema.reddit_submission_schema(submission, subreddit_name)
            self.write_submission(submission.id, item)
            submission_list.append(submission)
        return submission_list

    def fetch_comments_for_submissions(self, submissions: list, limit: int = 2) -> list:
        """Write the first level comments on a submission to FirestoreReddit."""
        logging.info(f"reddit connector: fetching comments.")
        comments = []
        for submission in submissions:
            comment_count = 0
            submission.comment_sort = "best"
            submission.comments.replace_more(limit=10)
            for comment in submission.comments:
                if comment_count == limit:
                    break
                if self.incorrect_comment_length(comment):
                    continue
                item = schema.reddit_comment_schema(comment, submission.id)
                self.write_comment(comment.id, item)
                comment_count += 1
                comments.append(comment)
        return comments

    def fetch_comments(self, submission_id: str, limit: int = 2) -> list:
        """Write the first level comments on a submission to FirestoreReddit."""
        logging.info(f"reddit connector: fetching comments.")
        comments = []
        submission = self._reddit_instance.submission(submission_id)
        comment_count = 0
        submission.comment_sort = "best"
        submission.comments.replace_more(limit=10)
        for comment in submission.comments:
            if comment_count == limit:
                break
            if self.incorrect_comment_length(comment):
                continue
            item = schema.reddit_comment_schema(comment, submission.id)
            self.write_comment(comment.id, item)
            comment_count += 1
            comments.append(comment)
        return comments

    def fetch_responses(self, comments: list, limit: int = 2) -> list:
        """Write the first level comments on a submission to FirestoreReddit."""
        logging.info(f"reddit connector: fetching responses.")
        responses = []
        for comment in comments:
            response_count = 0
            comment.refresh()
            comment.replies.replace_more(limit=10)
            for response in comment.replies:
                if response_count == limit:
                    break
                if self.incorrect_comment_length(response):
                    continue
                item = schema.reddit_response_schema(response, comment.id)
                self.write_responses(response.id, item)
                response_count += 1
                responses.append(response)
        return responses
