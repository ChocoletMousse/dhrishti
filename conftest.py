import pytest
from unittest.mock import Mock, MagicMock
from sources.reddit.reddit_connector import RedditConnector
from django.test import Client


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
    return [
        mock_submission_1,
        mock_submission_2
    ]
