from google.cloud import language
from google.cloud.language import types, enums


class SentimentAnalyser():

    def __init__(self):
        self._client = language.LanguageServiceClient()

    def analyse_titles(self, documents: list):
        """Go through each document in a collection and analyse the sentiment."""
        outputs = []
        for doc in documents:
            title = doc.get("title")
            document = types.Document(
                 type=enums.Document.Type.PLAIN_TEXT,
                 content=title
            )
            annotation = self._client.analyze_sentiment(document=document)
            self.display_annotation(title, annotation)
            outputs.append(annotation)
        return outputs

    def display_annotation(self, title: str, annotation):
        """Print the output of the sentiment analysis"""
        print(f"""
            {title} =>
            sentiment: {annotation.document_sentiment.score},
            magnitude: {annotation.document_sentiment.magnitude}
        """)
