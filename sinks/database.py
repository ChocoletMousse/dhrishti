from google.cloud import firestore
from google.cloud.firestore import Query
import logging


class FirestoreReddit():

    def __init__(self):
        self.db = firestore.Client()
        self.subreddit_ref = "subreddits"
        self.comments_ref = "comments"

    def write_submission(self, subreddit: str, document_id: str, item: dict):
        """write a submission."""
        logging.info(f"saving submission {document_id} to collection {subreddit}")
        self.db.collection(self.subreddit_ref).document(document_id).set(item)

    def update_documents(self, collection: str, document_id: str, parameters: dict):
        """Fetch a document from firestore based on the domain."""
        logging.info(f"updating {document_id} from collection {collection}")
        self.db.collection(collection).document(document_id).update(parameters)

    def get_submissions(self, limit: int = 10) -> list:
        """Retrieves the specified number of submissions from a given subreddit."""
        logging.info(f"getting {limit} submissions")
        documents = self.db.collection(self.subreddit_ref) \
            .order_by('landing_timestamp', direction=Query.DESCENDING).limit(limit).stream()
        return documents

    def get_submissions_by_subreddit(self, subreddit: str) -> list:
        """Retrieves the specified number of submissions from a given subreddit."""
        logging.info(f"getting submissions from subreddit {subreddit}")
        documents = self.db.collection(self.subreddit_ref).where("subreddit", "==", subreddit).stream()
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
        logging.info(f"saving comment {document_id} to collection {submission_id}")
        self.db.collection(self.comments_ref).document(document_id).set(item)

    def get_comments(self, submission_id: str, limit: int) -> list:
        """Retrieves the specified number of comments from a given submission."""
        logging.info(f"getting {limit} comments")
        documents = self.db.collection(self.comments_ref) \
            .order_by('landing_timestamp', direction=Query.DESCENDING).limit(limit).stream()
        return documents

    def get_comments_by_submission(self, submission_id: str) -> list:
        """Retrieves the specified number of comments from a given submission."""
        logging.info(f"getting comments from submission {submission_id}")
        documents = self.db.collection(self.comments_ref).where("submission", "==", submission_id).stream()
        return documents
