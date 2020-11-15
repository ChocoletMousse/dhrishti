from google.cloud import language_v1
from google.cloud.firestore import SERVER_TIMESTAMP
from nlp.thresholds import sentiment_score, sentiment_magnitude
from sinks.database import FirestoreReddit, BigQueryReddit
from praw.models import Comment
from utils import fields, schema
import logging
from datetime import datetime


class SentimentAnalyser:
    def __init__(self):
        self._client = language_v1.LanguageServiceClient()
        self._langauge = "en"
        self._type = language_v1.Document.Type.PLAIN_TEXT
        self.firestore = FirestoreReddit()
        self.bq = BigQueryReddit()

    def analyse_submissions(self, submissions: list):
        """Go through each document in a collection and analyse the sentiment."""
        for submission in submissions:
            sentiment_annotations = self.perform_sentiment_analysis(submission.title)
            self.firestore.update_documents(
                self.firestore.subreddit_ref,
                submission.id,
                self.format_sentiment(sentiment_annotations),
            )
        logging.info(
            "performed sentiment analysis on %d documents" % (len(submissions))
        )

    def analyse_comments(self, comments: list):
        """Go through each document in a collection and analyse the sentiment."""
        for comment in comments:
            sentiment_annotations = self.perform_sentiment_analysis(comment.body)
            formatted_firestore = self.format_sentiment(sentiment_annotations)

            annotations = self.perform_entity_sentiment_analysis(comment.body)
            formatted_bigquery = self.format_entities(annotations.entities, comment)
            formatted_bigquery[fields.COMMENT_SENTIMENT] = formatted_firestore.get(
                fields.SENTIMENT_SCORE
            )
            formatted_bigquery[fields.COMMENT_MAGNITUDE] = formatted_firestore.get(
                fields.SENTIMENT_MAGNITUDE
            )

            self.firestore.update_documents(
                self.firestore.comments_ref, comment.id, formatted_firestore
            )
            self.bq.write_to_table([formatted_bigquery])

        logging.info("performed sentiment analysis on %d documents" % (len(comments)))

    def analyse_responses(self, responses: list):
        """Go through each document in a collection and analyse the sentiment."""
        for response in responses:
            sentiment_annotations = self.perform_sentiment_analysis(response.body)
            self.firestore.update_documents(
                self.firestore.responses_ref,
                response.id,
                self.format_sentiment(sentiment_annotations),
            )
        logging.info("performed sentiment analysis on %d documents" % (len(responses)))

    # def analyse_entities_sentiment(self, comments: list):
    #     for comment in comments:
    #         annotations = self.perform_entity_sentiment_analysis(comment.body)
    #         formatted = self.format_entities(annotations.entities, comment)
    #         self.bq.write_to_table(formatted)
    #     logging.info(
    #         "performed sentiment analysis on entities in %d documents" % (len(comments))
    #     )

    def perform_sentiment_analysis(self, target_attr: str) -> list:
        doc = language_v1.Document(content=target_attr, type_=self._type, language=self._langauge)
        annotations = self._client.analyze_sentiment(
            request={"document": doc, "encoding_type": language_v1.EncodingType.UTF8}
        )
        return annotations

    def perform_entity_analysis(self, target_attr: str) -> list:
        doc = language_v1.Document(content=target_attr, type_=self._type, language=self._langauge)
        annotations = self._client.analyze_entities(
            request={"document": doc, "encoding_type": language_v1.EncodingType.UTF8}
        )
        return annotations

    def perform_entity_sentiment_analysis(self, target_attr: str) -> list:
        doc = language_v1.Document(content=target_attr, type_=self._type, language=self._langauge)
        annotations = self._client.analyze_entity_sentiment(
            request={"document": doc, "encoding_type": language_v1.EncodingType.UTF8}
        )
        return annotations

    def format_sentiment(self, annotations: dict) -> dict:
        """Returns a dict containing sentiment analysis values."""
        negative_flag = False
        negative_count = 0
        parameters = {
            fields.SENTIMENT_SCORE: round(annotations.document_sentiment.score, 4),
            fields.SENTIMENT_MAGNITUDE: round(
                annotations.document_sentiment.magnitude, 4
            ),
        }
        for sentence in annotations.sentences:
            if sentiment_score(sentence) and sentiment_magnitude(sentence):
                negative_flag = True
                negative_count += 1
        parameters[fields.NEGATIVE_FLAG] = negative_flag
        parameters[fields.NEGATIVE_SENTENCES_COUNT] = negative_count
        parameters[fields.SCORE_TIMESTAMP] = SERVER_TIMESTAMP
        return parameters

    def format_entities(self, entities: list, comment: Comment) -> dict:
        """Returns a dict containing entity analysis values."""
        cleaned_entities = [schema.reddit_entity_schema(entity) for entity in entities]
        parameters = {"subreddit": comment.subreddit.name}
        parameters[fields.SUBREDDIT_NAME] = comment.subreddit.display_name
        parameters[fields.COMMENT_ID] = comment.id
        parameters[fields.SUBREDDIT_ID] = comment.subreddit.id
        parameters[fields.SCORE] = comment.score
        parameters[fields.ENTITIES] = cleaned_entities
        parameters[fields.LANDING_TIMESTAMP] = str(datetime.now())
        parameters[fields.CREATED_TIMESTAMP] = str(
            datetime.utcfromtimestamp(int(comment.created_utc))
        )
        return parameters
