from google.cloud import language
from google.cloud.language import types, enums
from sinks.database import Database
from nlp.thresholds import sentiment_score, sentiment_magnitude
import logging


class SentimentAnalyser(Database):

    def __init__(self):
        super().__init__()
        self._client = language.LanguageServiceClient()

    def analyse_titles(self, collection: str, documents: list) -> list:
        """Go through each document in a collection and analyse the sentiment."""
        document_entities_analysis = []
        for doc in documents:
            id = doc.id
            doc_dict = doc.to_dict()
            title = doc_dict.get("title")
            document = types.Document(type=enums.Document.Type.PLAIN_TEXT, content=title)
            response = self._client.analyze_entity_sentiment(document=document)
            self.update_doc_from_firestore(
                collection,
                id,
                "negative_sentiment",
                self.identify_negative_entities(response.entities)
            )
            document_entities_analysis.append(response.entities)
        logging.info("performed sentiment analysis on %d documents" % (len(document_entities_analysis)))
        return document_entities_analysis

    def display_annotation(self, title: str, annotation):
        """Print the output of the sentiment analysis"""
        print(f"""
            {title} =>
            sentiment: {annotation.document_sentiment.score},
            magnitude: {annotation.document_sentiment.magnitude}
        """)

    def identify_negative_entities(self, entities: list) -> bool:
        negative_entity_flag = False
        negative_entity_count = 0
        for entity in entities:
            if sentiment_score(entity) and sentiment_magnitude(entity):
                negative_entity_flag = True
                negative_entity_count += 1
        return negative_entity_flag
