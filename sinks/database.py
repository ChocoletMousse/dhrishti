from google.cloud import firestore
import logging


class Database():

    def __init__(self):
        self.db = firestore.Client()

    def write_to_firestore(self, item):
        logging.info(f"saving {self.document} to collection {self.collection}")
        self.db.collection(self.collection).document(self.document).set(item)
