from google.cloud import language
from google.cloud.language import types, enums
from google.cloud.firestore import SERVER_TIMESTAMP
from nlp.thresholds import sentiment_score, sentiment_magnitude
from sinks.database import FirestoreReddit
from utils import fields, schema
import logging


class SentimentAnalyser(FirestoreReddit):

    def __init__(self):
        super().__init__()
        self._client = language.LanguageServiceClient()

    def analyse_submissions(self, submissions: list):
        """Go through each document in a collection and analyse the sentiment."""
        for submission in submissions:
            annotations = self.perform_sentiment_analysis(submission.title)
            self.update_documents(
                self.subreddit_ref,
                submission.id,
                self.format_sentiment(annotations)
            )
        logging.info("performed sentiment analysis on %d documents" % (len(submissions)))

    def analyse_comments(self, comments: list):
        """Go through each document in a collection and analyse the sentiment."""
        for comment in comments:
            annotations = self.perform_sentiment_analysis(comment.body)
            self.update_documents(
                self.comments_ref,
                comment.id,
                self.format_sentiment(annotations)
            )
        logging.info("performed sentiment analysis on %d documents" % (len(comments)))

    def analyse_responses(self, responses: list):
        """Go through each document in a collection and analyse the sentiment."""
        for response in responses:
            annotations = self.perform_sentiment_analysis(response.body)
            self.update_documents(
                self.responses_ref,
                response.id,
                self.format_sentiment(annotations)
            )
        logging.info("performed sentiment analysis on %d documents" % (len(responses)))

    def analyse_entities(self, comments: list):
        """Go through each document in a collection and analyse the sentiment."""
        for comment in comments:
            annotations = self.perform_entity_analysis(comment.body)
            subreddit_name = comment.subreddit.display_name
            self.write_entities(
                comment.id,
                self.format_entities(annotations.entities, subreddit_name)
            )
        logging.info("performed sentiment analysis on %d documents" % (len(comments)))

    def perform_sentiment_analysis(self, target_attr: str) -> list:
        doc = types.Document(type=enums.Document.Type.PLAIN_TEXT, content=target_attr)
        annotations = self._client.analyze_sentiment(document=doc)
        return annotations

    def perform_entity_analysis(self, target_attr: str) -> list:
        doc = types.Document(type=enums.Document.Type.PLAIN_TEXT, content=target_attr)
        annotations = self._client.analyze_entities(document=doc)
        return annotations

    def format_sentiment(self, annotations: dict) -> dict:
        """Returns a dict containing sentiment analysis values."""
        negative_flag = False
        negative_count = 0
        parameters = {
            fields.SENTIMENT_SCORE: round(annotations.document_sentiment.score, 4),
            fields.SENTIMENT_MAGNITUDE: round(annotations.document_sentiment.magnitude, 4)
        }
        for sentence in annotations.sentences:
            if sentiment_score(sentence) and sentiment_magnitude(sentence):
                negative_flag = True
                negative_count += 1
        parameters[fields.NEGATIVE_FLAG] = negative_flag
        parameters[fields.NEGATIVE_SENTENCES_COUNT] = negative_count
        parameters[fields.SCORE_TIMESTAMP] = SERVER_TIMESTAMP
        return parameters

    def format_entities(self, entities: list, subreddit: str) -> dict:
        """Returns a dict containing entity analysis values."""
        parameters = {"subreddit": subreddit}
        cleaned_entities = [schema.reddit_entity_schema(entity) for entity in entities]
        parameters["entities"] = cleaned_entities
        return parameters

# ========================================================================================== #
#                                   TO BE REPLACED                                           #
# ========================================================================================== #

    def analyse_text(self, collection: str, documents: list, target_attr: str) -> list:
        """Go through each document in a collection and analyse the sentiment."""
        sentences_analysis = []
        for doc in documents:
            id = doc.id
            annotations = self.perform_sentiment_analysis(doc.to_dict(), target_attr)
            self.update_documents(
                target_attr,
                collection,
                id,
                self.format_sentiment(annotations)
            )
            sentences_analysis.append(annotations.sentences)
        logging.info("performed sentiment analysis on %d documents" % (len(sentences_analysis)))
        return sentences_analysis

    def perform_sentiment_analysis_old(self, document: dict, target_attr: str) -> list:
        doc = types.Document(type=enums.Document.Type.PLAIN_TEXT, content=document.get(target_attr))
        annotations = self._client.analyze_sentiment(document=doc)
        return annotations
