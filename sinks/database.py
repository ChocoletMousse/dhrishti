from google.cloud import firestore
import logging


class FirestoreReddit():

    def __init__(self):
        self.db = firestore.Client()
        self.subreddit_ref = "subreddits"
        self.title = "title"
        self.comments_ref = "comments"
        self.attribute_map = {
            "title": "subreddits",
            "comment": "comments"
        }

    def write_submission(self, subreddit: str, document_id: str, item: dict):
        """write a submission."""
        logging.info(f"saving {document_id} to collection {subreddit}")
        subreddit_ref = self.db.collection(self.subreddit_ref).document(self.title)
        subreddit_ref.collection(subreddit).document(document_id).set(item)

    def update_documents(self, domain: str, collection: str, document_id: str, parameters: dict):
        """Fetch a submission from a subreddit."""
        subreddit_ref = self.db.collection(self.attribute_map[domain]).document(self.title)
        subreddit_ref.collection(collection).document(document_id).update(parameters)

    def get_submissions(self, subreddit: str, limit: int) -> list:
        """Retrieves the specified number of submissions from a given subreddit."""
        subreddit_ref = self.db.collection(self.subreddit_ref).document(self.title)
        documents = subreddit_ref.collection(subreddit).limit(limit).stream()
        return documents

    def clear_collection(self, collection):
        """Clear all documents in a collection."""
        logging.info(f"Removing all documents in collection {collection}.")
        docs = self.db.collection(collection).stream()
        for doc in docs:
            doc.reference.delete()
        logging.info(f"Collection {collection} cleared.")

    def write_comment(self, submission_id: str, document_id: str, item: dict):
        """Save the comment from a submission."""
        logging.info(f"writing {document_id} to collection {submission_id}")
        comments_ref = self.db.collection(self.comments_ref).document(self.title)
        comments_ref.collection(submission_id).document(document_id).set(item)

    def get_comments(self, submission_id: str, limit: int) -> list:
        """Retrieves the specified number of submissions from a given subreddit."""
        subreddit_ref = self.db.collection(self.comments_ref).document(self.title)
        documents = subreddit_ref.collection(submission_id).limit(limit).stream()
        return documents
