from praw.models import Submission


def reddit_submission_schema(submission: Submission) -> dict:
    """Submission document structure for storage"""
    return {
        "id": submission.id,
        "name": submission.name,
        "score": submission.score,
        "upvote_ratio": submission.upvote_ratio,
        "num_comments": submission.num_comments,
        "url": submission.url
    }
