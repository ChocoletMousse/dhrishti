from praw.models import Submission, Comment
from datetime import datetime


def reddit_submission_schema(submission: Submission, subreddit_id: str) -> dict:
    """Submission document structure for storage"""
    return {
        "name": submission.name,
        "type": "submission",
        "subreddit_id": subreddit_id,
        "title": submission.title,
        "score": submission.score,
        "upvote_ratio": submission.upvote_ratio,
        "num_comments": submission.num_comments,
        "url": submission.url,
        "landing_timestamp": datetime.now().isoformat()
    }


def reddit_comment_schema(comment: Comment, submission_id: str) -> dict:
    return {
        "comment": comment.body,
        "type": "comment",
        "submission_id": submission_id,
        "score": comment.score,
        "parent_id": comment.parent_id,
        "created_utc": comment.created_utc,
        "replies": [],
        "landing_timestamp": datetime.now().isoformat()
    }


def reddit_reply_schema(reply: Comment) -> dict:
    return {
        "id": reply.id,
        "type": "response",
        "comment": reply.body,
        "score": reply.score,
        "created_utc": reply.created_utc,
        "landing_timestamp": datetime.now().isoformat(),
        "replies": []
    }
