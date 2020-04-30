from google.cloud import language
from google.cloud.language import types, enums
from google.cloud.firestore import SERVER_TIMESTAMP
from nlp.thresholds import sentiment_score, sentiment_magnitude
from sinks.database import FirestoreReddit
from utils import fields
import logging


class SentimentAnalyser(FirestoreReddit):

    def __init__(self):
        super().__init__()
        self._client = language.LanguageServiceClient()

    def analyse_submissions(self, submissions: list) -> list:
        """Go through each document in a collection and analyse the sentiment."""
        for submission in submissions:
            annotations = self.perform_analysis(submission.title)
            self.update_documents(
                self.subreddit_ref,
                submission.id,
                self.flag_negative_entities(annotations)
            )
        logging.info("performed sentiment analysis on %d documents" % (len(submissions)))

    def analyse_comments(self, comments: list) -> list:
        """Go through each document in a collection and analyse the sentiment."""
        for comment in comments:
            annotations = self.perform_analysis(comment.body)
            self.update_documents(
                self.comments_ref,
                comment.id,
                self.flag_negative_entities(annotations)
            )
        logging.info("performed sentiment analysis on %d documents" % (len(comments)))

    def perform_analysis(self, target_attr: str) -> list:
        doc = types.Document(type=enums.Document.Type.PLAIN_TEXT, content=target_attr)
        annotations = self._client.analyze_sentiment(document=doc)
        return annotations

    def flag_negative_entities(self, annotations: dict) -> dict:
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

# ========================================================================================== #
#                                   TO BE REPLACED                                           #
# ========================================================================================== #

    def analyse_text(self, collection: str, documents: list, target_attr: str) -> list:
        """Go through each document in a collection and analyse the sentiment."""
        sentences_analysis = []
        for doc in documents:
            id = doc.id
            annotations = self.perform_analysis(doc.to_dict(), target_attr)
            self.update_documents(
                target_attr,
                collection,
                id,
                self.flag_negative_entities(annotations)
            )
            sentences_analysis.append(annotations.sentences)
        logging.info("performed sentiment analysis on %d documents" % (len(sentences_analysis)))
        return sentences_analysis

    def perform_analysis_old(self, document: dict, target_attr: str) -> list:
        doc = types.Document(type=enums.Document.Type.PLAIN_TEXT, content=document.get(target_attr))
        annotations = self._client.analyze_sentiment(document=doc)
        return annotations
