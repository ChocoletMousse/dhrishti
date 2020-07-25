import {React, useState} from 'react';

const Comment = (props) => {
    const [dislpayMore, setDisplayMore] = useState(false);
    if (!dislpayMore) {
        return (
            <div className="col-sm-4">
                <div className="shadow-sm p-3 mb-5 bg-white rounded">
                    <div className="card">
                        <div className="card-body">
                            <div className="row justify-content-between">
                                <div className="col-8">
                                    <p className="card-text"><i><a href={`www.reddit.com${props.submission.permalink}`}>/r/{props.submission.subreddit}</a></i></p>
                                </div>
                                <div className="col-sm-2">
                                    <svg onClick={() => setDisplayMore(true)} width="1em" height="1em" viewBox="0 0 16 16" className="bi bi-chevron-double-right text-danger" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                        <path fillRule="evenodd" d="M3.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L9.293 8 3.646 2.354a.5.5 0 0 1 0-.708z" />
                                        <path fillRule="evenodd" d="M7.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L13.293 8 7.646 2.354a.5.5 0 0 1 0-.708z" />
                                    </svg>
                                </div>
                            </div>
                            <h5 className="card-title">{props.submission.title}</h5>
                            <div className="row justify-content-between">
                                <div className="col-sm-2">
                                    <a href={props.submission.url}>
                                        <svg width="1em" height="1em" viewBox="0 0 16 16" className="bi bi-arrow-bar-right" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                            <path fillRule="evenodd" d="M10.146 4.646a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L12.793 8l-2.647-2.646a.5.5 0 0 1 0-.708z" />
                                            <path fillRule="evenodd" d="M6 8a.5.5 0 0 1 .5-.5H13a.5.5 0 0 1 0 1H6.5A.5.5 0 0 1 6 8zm-2.5 6a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 1 0v11a.5.5 0 0 1-.5.5z" />
                                        </svg>
                                    </a>
                                </div>
                                <div className="col-sm-2">
                                    <Link to="">
                                        <svg width="1em" height="1em" viewBox="0 0 16 16" className="bi bi-chat-right-dots" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                            <path fillRule="evenodd" d="M2 1h12a1 1 0 0 1 1 1v11.586l-2-2A2 2 0 0 0 11.586 11H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1zm12-1a2 2 0 0 1 2 2v12.793a.5.5 0 0 1-.854.353l-2.853-2.853a1 1 0 0 0-.707-.293H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12z" />
                                            <path d="M5 6a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm4 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm4 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0z" />
                                        </svg>
                                    </Link>
                                </div>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    } else {
        return (
            <div className="col-sm-4">
                <div className="shadow-sm p-3 mb-5 bg-white rounded">
                    <div className="card">
                        <div className="card-body">
                            <div className="row justify-content-between">
                                <div className="col-8">
                                    <p className="card-text"><i><a href={`www.reddit.com${props.submission.permalink}`}>/r/{props.submission.subreddit}</a></i></p>
                                </div>
                                <div className="col-sm-2">
                                    <svg onClick={() => setDisplayMore(false)} width="1em" height="1em" viewBox="0 0 16 16" className="bi bi-chevron-double-right text-danger" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                        <path fillRule="evenodd" d="M3.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L9.293 8 3.646 2.354a.5.5 0 0 1 0-.708z" />
                                        <path fillRule="evenodd" d="M7.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L13.293 8 7.646 2.354a.5.5 0 0 1 0-.708z" />
                                    </svg>
                                </div>
                            </div>
                            <h6 className="card-subtitle mb-2 text-muted">{props.submission.negative_flag}</h6>
                            <p className="card-text">Sentiment score: {props.submission.sentiment_score}</p>
                            <p className="card-text">Sentiment magnitude: {props.submission.sentiment_magnitude}</p>
                            <p className="card-text">Comments: {props.submission.num_comments}</p>
                        </div>
                    </div>
                </div>
            </div>
        )
    }

}

export default Comment;