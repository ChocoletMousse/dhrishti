from google.cloud import language
from google.cloud.language import types, enums
from logging import log


class SentimentAnalyser():

    def __init__(self):
        self._client = language.LanguageServiceClient()

    def analyse_titles(self, documents: list):
        """Go through each document in a collection and analyse the sentiment."""
        docs_analysis = []
        for doc in documents:
            title = doc.get("title")
            document = types.Document(
                 type=enums.Document.Type.PLAIN_TEXT,
                 content=title
            )
            response = self._client.analyze_entity_sentiment(document=document)
            docs_analysis.append(response.entities)
        self.display_annotation(docs_analysis)
        log.info("performed analysis on %d documents" % (len(docs_analysis)))
        return docs_analysis
