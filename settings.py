from dotenv import load_dotenv, find_dotenv
import os


class Setup:
    def __init__(self):
        self.load_settings()
        self.client_id = os.getenv("REDDIT_CLIENT_ID")
        self.client_secret = os.getenv("REDDIT_SECRET")

    def load_settings(self):
        load_dotenv(find_dotenv())
