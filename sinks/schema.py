from praw.models import Submission
from datetime import datetime


def reddit_submission_schema(submission: Submission) -> dict:
    """Submission document structure for storage"""
    return {
        "name": submission.name,
        "title": submission.title,
        "score": submission.score,
        "upvote_ratio": submission.upvote_ratio,
        "num_comments": submission.num_comments,
        "url": submission.url,
        "landing_timestamp": datetime.now().isoformat()
    }
