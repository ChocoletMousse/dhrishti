from google.cloud import firestore
from google.cloud.firestore import Query
import logging
import json


class FirestoreReddit():

    def __init__(self):
        self.db = firestore.Client()
        self.subreddit_ref = "subreddits"
        self.comments_ref = "comments"
        self.responses_ref = "responses"
        self.entities_ref = "entities"

    def update_documents(self, collection: str, document_id: str, parameters: dict):
        """Fetch a document from firestore based on the domain."""
        logging.info(f"updating {document_id} from collection {collection}")
        self.db.collection(collection).document(document_id).update(parameters)

    def write_submission(self, submission_id: str, item: dict):
        """Write a submission from a subreddit."""
        logging.info(f"saving submission {submission_id}.")
        self.db.collection(self.subreddit_ref).document(submission_id).set(item)

    def get_submissions(self, limit: int = 10) -> list:
        """Retrieves the specified number of submissions from a given subreddit."""
        logging.info(f"getting {limit} submissions")
        documents = self.db.collection(self.subreddit_ref) \
            .order_by('landing_timestamp', direction=Query.DESCENDING).limit(limit).stream()
        dict_docs = [doc.to_dict() for doc in documents]
        return json.dumps(dict_docs, default=str)

    def get_submissions_by_subreddit(self, subreddit: str) -> list:
        """Retrieves the specified number of submissions from a given subreddit."""
        logging.info(f"getting submissions from subreddit {subreddit}")
        documents = self.db.collection(self.subreddit_ref).where("subreddit", "==", subreddit).stream()
        return documents

    def write_comment(self, document_id: str, item: dict):
        """Write the comment from a submission."""
        logging.info(f"saving comment {document_id}.")
        self.db.collection(self.comments_ref).document(document_id).set(item)

    def get_comments(self, limit: int = 5) -> list:
        """Retrieves the specified number of comments from all comments."""
        logging.info(f"getting {limit} comments")
        documents = self.db.collection(self.comments_ref) \
            .order_by('landing_timestamp', direction=Query.DESCENDING).limit(limit).stream()
        dict_comments = [comment.to_dict() for comment in documents]
        return json.dumps(dict_comments, default=str)

    def get_comments_by_submission(self, submission_id: str) -> list:
        """Retrieves the specified number of comments from a given submission."""
        logging.info(f"getting comments from submission {submission_id}")
        documents = self.db.collection(self.comments_ref).where("submission_id", "==", submission_id).stream()
        return documents

    def write_responses(self, response_id: str, item: dict):
        """Save the response on a comment."""
        logging.info(f"saving response {response_id}.")
        self.db.collection(self.responses_ref).document(response_id).set(item)

    def get_responses(self, limit: int = 5) -> list:
        """Retrieves the specified number of comments from a given submission."""
        logging.info(f"getting {limit} comments")
        documents = self.db.collection(self.responses_ref) \
            .order_by('landing_timestamp', direction=Query.DESCENDING).limit(limit).stream()
        return documents

    def get_responses_by_comments(self, comment_id: str) -> list:
        """Retrieves the specified number of comments from a given submission."""
        logging.info(f"getting responses to comment {comment_id}")
        documents = self.db.collection(self.responses_ref).where("comment_id", "==", comment_id).stream()
        return documents

    def write_entities(self, comment_id: str, item: dict):
        """Writes the output of entity analysis on comments."""
        logging.info(f"saving entities for comment {comment_id}.")
        self.db.collection(self.entities_ref).document(comment_id).set(item)
