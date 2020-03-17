from google.cloud import firestore
import logging


class Database():

    def __init__(self):
        self.db = firestore.Client()

    def write_doc_to_firestore(self, collection, document, item):
        """Write an object to Firestore."""
        logging.info(f"saving {document} to collection {collection}")
        self.db.collection(collection).document(document).set(item)

    def update_doc_from_firestore(self, collection, document, parameters: dict):
        """Fetch an document from a collection in a Firestore."""
        self.db.collection(collection).document(document).update(parameters)

    def get_docs_from_firestore(self, collection, limit: int) -> list:
        """Retrieves the specified number of documents from a given collection."""
        documents = self.db.collection(collection).limit(limit).stream()
        return documents

    def clear_collection(self, collection):
        """Clear all documents in a collection."""
        logging.info(f"Removing all documents in collection {collection}.")
        docs = self.db.collection(collection).stream()
        for doc in docs:
            doc.reference.delete()
        logging.info(f"Collection {collection} cleared.")
