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
        sentences_analysis = []
        for doc in documents:
            id = doc.id
            doc_dict = doc.to_dict()
            title = doc_dict.get("title")
            document = types.Document(type=enums.Document.Type.PLAIN_TEXT, content=title)
            annotations = self._client.analyze_sentiment(document=document)
            self.update_doc_from_firestore(
                collection,
                id,
                "negative_sentiment",
                self.identify_negative_entities(annotations.sentences)
            )
            sentences_analysis.append(annotations.sentences)
        logging.info("performed sentiment analysis on %d documents" % (len(sentences_analysis)))
        return sentences_analysis

    def display_annotations(self, title: str, annotations):
        """Print the output of the sentiment analysis"""
        for sentence in annotations.sentences:
            print(f"""
                {"=-" * 10}
                {sentence.text.content} =>
                sentiment: {sentence.sentiment.score},
                magnitude: {annotations.sentiment.magnitude}
            """)

    def identify_negative_entities(self, sentences: list) -> bool:
        negative_entity_flag = False
        for sentence in sentences:
            if sentiment_score(sentence) and sentiment_magnitude(sentence):
                negative_entity_flag = True
        return negative_entity_flag
