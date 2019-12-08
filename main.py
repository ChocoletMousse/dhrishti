from sources.reddit import RedditConnector


def main():
    reddit_connector = RedditConnector()
    reddit = reddit_connector.get_reddit_connector()
    subreddit = reddit.subreddit('python').hot(limit=10)

    for submission in subreddit:
        print(f"title: {submission.title}")


if __name__ == "__main__":
    main()
