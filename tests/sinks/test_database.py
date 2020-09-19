import pytest
from unittest.mock import patch
from sinks.database import BigQueryReddit


class TestBigQueryReddit():

    @patch("google.cloud.bigquery.Client.create_table")
    @pytest.mark.usefixtures("big_query_reddit")
    def test_create_reddit_table(self, create_table_patch, big_query_reddit: BigQueryReddit):
        big_query_reddit.create_reddit_table()
        create_table_patch.assert_called_once()

    @pytest.mark.usefixtures("big_query_reddit", "sentiment_entity_sample")
    def test_add_rows(self, big_query_reddit: BigQueryReddit, sentiment_entity_sample: dict):
        big_query_reddit.write_to_table(sentiment_entity_sample)
