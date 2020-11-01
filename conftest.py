import pytest
from unittest.mock import Mock, MagicMock
from sources.reddit.reddit_connector import RedditConnector
from sinks.database import BigQueryReddit
from google.cloud.firestore import SERVER_TIMESTAMP
from django.test import Client
import datetime


@pytest.fixture(scope="function")
def big_query_reddit():
    bq = BigQueryReddit()
    return bq


@pytest.fixture(scope="function")
def django_client():
    return Client()


@pytest.fixture(scope="function")
@pytest.mark.usefixtures("subreddit")
def reddit():
    mock_reddit = MagicMock()
    return mock_reddit


@pytest.fixture(scope="function")
@pytest.mark.usefixture("reddit_submission_data")
def subreddit():
    mock_subreddit = MagicMock()
    mock_subreddit.top.return_value = reddit_submission_data()
    mock_subreddit.new.return_value = reddit_submission_data()
    mock_subreddit.controversial.return_value = reddit_submission_data()
    return mock_subreddit


@pytest.fixture(scope="function")
@pytest.mark.usefixtures("reddit", "subreddit")
def reddit_connector(reddit, subreddit):
    reddit_connector = RedditConnector()
    reddit_connector.write_submission = Mock()
    reddit_connector._reddit_instance = reddit
    reddit_connector._reddit_instance.subreddit.return_value = subreddit
    return reddit_connector


def reddit_submission_data():
    mock_submission_1 = MagicMock()
    mock_submission_2 = MagicMock()
    return [mock_submission_1, mock_submission_2]


@pytest.fixture(scope="function")
def sentiment_entity_sample():
    return [
        {
            "comment_id": "test_id",
            "entities": [
                {
                    "entity_name": "entity.name",
                    "entity_type": "enums.Entity.Type(entity.type).name",
                    "salience": 1.44,
                    "entity_sentiment_score": 1.44,
                    "entity_sentiment_magnitude": 1.44,
                    "mentions_count": 1,
                },
                {
                    "entity_name": "entity.name2",
                    "entity_type": "enums.Entity.Type(entity.type).name2",
                    "salience": 1.45,
                    "entity_sentiment_score": 1.45,
                    "entity_sentiment_magnitude": 1.45,
                    "mentions_count": 2,
                },
            ],
            "score": 2,
            "subreddit": "abcd",
            "subreddit_name": "test_subreddit",
            "landing_timestamp": str(datetime.datetime.now()),
        }
    ]
