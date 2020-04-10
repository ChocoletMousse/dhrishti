# dhrishti

## _user journey_:
1) User is interested in a certain topic does a shallow dive via dashboard to find any actionable insights.
2) User decides to use this service to get objective results to validate their insights, as well as getting additional information to be displayed on the dashboard.
3) If the information yielded is relevant, user can take action via the company's policy.

## _process_:

1) Create a restful service that makes calls to the social media api based on incoming requests containing search parameters (e.g. subreddit, user).

2) User makes a request.

3) Results of the query are stored in a database:
    
    * The raw stored results will be available for display on a dashboard.
4) The raw data will be passed into a machine learning algorithm. The output will also be stored in the database, available for viewing on the dashboard.
5) The output of the algorithm will suggest any particular threads which are worth delving into. The user can choose to dig into these threads or not.
    * If yes, the algorithm will search for comments 

## _todo_:

- Map of all the possible searches to their expected results.
- Decide what algorithms to use
- Decide what database to use
- Decide how to write to database

## _log_:
- [x] create a view from the index to fetch results from reddit
- [x] give a score to a title based
- [x] determine a threshold which determines whether there should be further delving
- [ ] delve into CommentForests and retrieve significant threads
- [ ] Run analysis on comments and identify key words and phrases
- [ ] create links to traverse between different html pages

