from praw.models import Submission, Comment
from google.cloud.firestore import SERVER_TIMESTAMP
from google.cloud.language_v1 import enums


def reddit_submission_schema(submission: Submission, subreddit: str) -> dict:
    """Submission document structure for storage"""
    return {
        "name": submission.name,
        "type": "submission",
        "subreddit": subreddit,
        "title": submission.title,
        "score": submission.score,
        "upvote_ratio": submission.upvote_ratio,
        "num_comments": submission.num_comments,
        "url": submission.url,
        "created_utc": submission.created_utc,
        "landing_timestamp": SERVER_TIMESTAMP
    }


def reddit_comment_schema(comment: Comment, submission_id: str) -> dict:
    return {
        "comment": comment.body,
        "type": "comment",
        "submission_id": submission_id,
        "score": comment.score,
        "parent_id": comment.parent_id,
        "created_utc": comment.created_utc,
        "landing_timestamp": SERVER_TIMESTAMP
    }


def reddit_response_schema(response: Comment, comment_id) -> dict:
    return {
        "comment": response.body,
        "type": "response",
        "comment_id": comment_id,
        "score": response.score,
        "parent_id": response.parent_id,
        "created_utc": response.created_utc,
        "landing_timestamp": SERVER_TIMESTAMP
    }


def reddit_entity_schema(entity: list) -> dict:
    return {
        "entity_name": entity.name,
        "entity_type": enums.Entity.Type(entity.type).name,
        "salience": entity.salience,
        "mentions_count": len(entity.mentions)
    }
