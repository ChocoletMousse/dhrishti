from google.cloud import firestore, exceptions
import logging


class Database():

    def __init__(self):
        self.db = firestore.Client()

    def write_to_firestore(self, collection, document, item):
        """Write an object to Firestore."""
        logging.info(f"saving {document} to collection {collection}")
        self.db.collection(collection).document(document).set(item)

    def retrieve_doc_from_firestore(self, collection, document):
        """Fetch an document from a collection in a Firestore."""
        try:
            return self.db.collection(collection).document(document).get()
        except exceptions.NotFound:
            logging.info(f"{document} in {collection} was not found in Firestore.")

    def retrieve_docs_from_firestore(self, collection, limit: int):
        """Retrieves the specified number of documents from a given collection."""
        docs = self.db.collection(collection).limit(limit).stream()
        for doc in docs:
            logging.info(f"{doc.to_dict()}")

    def clear_collection(self, collection):
        """Clear all documents in a collection."""
        logging.info(f"Removing all documents in collection {collection}.")
        docs = self.db.collection(collection).stream()
        for doc in docs:
            doc.reference.delete()
        logging.info(f"Collection {collection} cleared.")
