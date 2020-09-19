from praw.models import Submission, Comment
from google.cloud.firestore import SERVER_TIMESTAMP
from google.cloud.language_v1 import enums
from google.cloud.bigquery import SchemaField


def reddit_submission_schema(submission: Submission, subreddit: str) -> dict:
    """Submission document structure for storage"""
    return {
        "id": submission.id,
        "name": submission.name,
        "type": "submission",
        "subreddit": subreddit,
        "permalink": submission.permalink,
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
        "id": comment.id,
        "comment": comment.body,
        "type": "comment",
        "submission_id": submission_id,
        "permalink": comment.permalink,
        "score": comment.score,
        "parent_id": comment.parent_id,
        "subreddit_name": comment.subreddit.display_name,
        "created_utc": comment.created_utc,
        "landing_timestamp": SERVER_TIMESTAMP
    }


def reddit_response_schema(response: Comment, comment_id) -> dict:
    return {
        "id": response.id,
        "comment": response.body,
        "type": "response",
        "comment_id": comment_id,
        "permalink": response.permalink,
        "score": response.score,
        "parent_id": response.parent_id,
        "subreddit_name": response.subreddit.display_name,
        "created_utc": response.created_utc,
        "landing_timestamp": SERVER_TIMESTAMP
    }


def reddit_entity_schema(entity) -> dict:
    return {
        "entity_name": entity.name,
        "entity_type": enums.Entity.Type(entity.type).name,
        "salience": entity.salience,
        "entity_sentiment_score": entity.sentiment.score,
        "entity_sentiment_magnitude": entity.sentiment.magnitude,
        "mentions_count": len(entity.mentions)
    }


def reddit_bq_schema() -> list:
    return [
        SchemaField("comment_id", "STRING", mode="NULLABLE"),
        SchemaField("entities", "RECORD", mode="REPEATED", fields=[
            SchemaField("entity_name", "STRING", mode="NULLABLE"),
            SchemaField("entity_type", "STRING", mode="NULLABLE"),
            SchemaField("salience", "FLOAT", mode="NULLABLE"),
            SchemaField("entity_sentiment_score", "FLOAT", mode="NULLABLE"),
            SchemaField("entity_sentiment_magnitude", "FLOAT", mode="NULLABLE"),
            SchemaField("mentions_count", "INTEGER", mode="NULLABLE"),
        ]),
        SchemaField("score", "INTEGER", mode="NULLABLE"),
        SchemaField("subreddit", "STRING", mode="NULLABLE"),
        SchemaField("subreddit_name", "STRING", mode="NULLABLE"),
        SchemaField("landing_timestamp", "TIMESTAMP", mode="NULLABLE"),
        SchemaField("comment_sentiment", "FLOAT", mode="NULLABLE"),
        SchemaField("comment_magnitude", "FLOAT", mode="NULLABLE"),
        SchemaField("created_timestamp", "TIMESTAMP", mode="NULLABLE"),
    ]
