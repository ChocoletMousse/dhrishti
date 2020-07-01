import React from 'react';

const Submission = (props) => {
    console.log('hello');
    return(
        <div className="card">
            <div className="card-body">
            <h5 className="card-title">{props.submission.title}</h5>
            <p className="card-text"><i>/r/{props.submission.subreddit}</i></p>
            <h6 className="card-subtitle mb-2 text-muted">{props.submission.negative_flag}</h6>
            <p className="card-text">Sentiment score: {props.submission.sentiment_score}</p>
            <p className="card-text">Sentiment magnitude: {props.submission.sentiment_magnitude}</p>
            <p className="card-text">Comments: {props.submission.num_comments}</p>
            <a href={props.submission.url} className="card-link">{props.submission.url}</a>
            </div>
        </div>
    )
}

export default Submission;