from sources.reddit.reddit_connector import RedditConnector


def main():
    reddit_connector = RedditConnector()
    reddit_connector.write_top_rated_posts("python", 5)


if __name__ == "__main__":
    main()
