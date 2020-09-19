from unittest.mock import patch, MagicMock, Mock
# from unittest import TestCase
import pytest

from sources.reddit.reddit_connector import RedditConnector


class TestRedditConnector():

    @pytest.mark.usefixtures("reddit_connector", "subreddit")
    def test_fetch_posts(self, reddit_connector: RedditConnector, subreddit):
        test_top = reddit_connector.fetch_posts('test', 'top', 2)

        reddit_connector._reddit_instance.subreddit.call_count == 1
        reddit_connector.write_submission.call_count == 2
        subreddit.top.assert_called_once()
        subreddit.new.assert_not_called()
        subreddit.controversial.assert_not_called()
        assert len(test_top) == 2

        test_new = reddit_connector.fetch_posts('test', 'latest', 2)

        reddit_connector._reddit_instance.subreddit.call_count == 2
        subreddit.new.assert_called_once()
        subreddit.controversial.assert_not_called()
        reddit_connector.write_submission.call_count == 4
        assert len(test_new) == 2

        test_controversial = reddit_connector.fetch_posts('test', 'controversial', 2)

        reddit_connector._reddit_instance.subreddit.call_count == 3
        subreddit.controversial.assert_called_once()
        reddit_connector.write_submission.call_count == 6
        assert len(test_controversial) == 2

    
    @pytest.mark.usefixtures()

