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

- use gunicorn in django container before deploying to kubernetes
- address error:
```
{
  "textPayload": "ERROR:django.security.DisallowedHost:Invalid HTTP_HOST header: '35.235.79.222'. You may need to add '35.235.79.222' to ALLOWED_HOSTS.\n",
  "insertId": "td99jk05k55qcpb2z",
  "resource": {
    "type": "k8s_container",
    "labels": {
      "location": "us-west2-b",
      "project_id": "arcane-boulder-263622",
      "container_name": "dhrishti-backend",
      "cluster_name": "dhrishti-cluster",
      "pod_name": "dhrishti-9955b7797-q48lr",
      "namespace_name": "default"
    }
  },
  "timestamp": "2020-11-01T20:34:34.788117889Z",
  "severity": "ERROR",
  "labels": {
    "k8s-pod/app": "django-pod",
    "k8s-pod/pod-template-hash": "9955b7797"
  },
  "logName": "projects/arcane-boulder-263622/logs/stderr",
  "receiveTimestamp": "2020-11-01T20:34:41.323608716Z"
}
```
