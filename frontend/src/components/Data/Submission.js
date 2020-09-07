import React, { useState, useEffect } from 'react';
import {Link} from 'react-router-dom';
import axios from 'axios';
import Dhrishti from '../../utils/Dhrishti';

const Submission = (props) => {
    const [displayMore, setDisplayMore] = useState(false);
    const [commentsInDb, setCommentsInDb] = useState(false);
    const [loading, setLoading] = useState(false);
    const [fetchingComments, setFetchingComments] = useState(false);

    const loadCommentsForSubmission = async () => {
        setLoading(true);
        console.log('checking comments data for submission ' + props.submission.id);
        const url = `http://127.0.0.1:8000/dhrishti/data/comments/${props.submission.id}`;
        let response = await axios.get(url);
        if (response.status == 200) {
            if (!response.data.length > 0) {
                setFetchingComments(true);
                console.debug(`no comments saved for submission ${props.submission.id} in db`);
            } else {
                console.debug(`comments available for submission ${props.submission.id} in db`);
                setCommentsInDb(true);
                setLoading(false);
            }
        }
    }

    useEffect(() => {
        let loadComments = async () => {
            if (fetchingComments) {
                let successfulLoad = await Dhrishti.loadCommentsForSubmission(props.submission.id)
                    .catch(error => console.log(error));
                if (successfulLoad) {
                    console.log('finished comments load.', successfulLoad);
                    setLoading(false);
                    setCommentsInDb(successfulLoad);
                    setFetchingComments(false);
                }
            }
        }
        loadComments();
    }, [fetchingComments])
    
    const commentsInDbIcon = () => {
        if (loading) {
            return (
                <div className="col-sm-2">
                    <div className="spinner-grow spinner-grow-sm text-danger" role="status">
                        <span className="sr-only">Loading...</span>
                    </div>
                </div>
            )
        } else if (!loading && commentsInDb) {
            return (
                <div className="col-sm-2">
                    <Link to={`data/convos/${props.submission.id}`}>
                        <svg width="1em" height="1em" viewBox="0 0 16 16" className="bi bi-diagram-3" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                            <path fillRule="evenodd" d="M0 11.5A1.5 1.5 0 0 1 1.5 10h1A1.5 1.5 0 0 1 4 11.5v1A1.5 1.5 0 0 1 2.5 14h-1A1.5 1.5 0 0 1 0 12.5v-1zm1.5-.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1zm4.5.5A1.5 1.5 0 0 1 7.5 10h1a1.5 1.5 0 0 1 1.5 1.5v1A1.5 1.5 0 0 1 8.5 14h-1A1.5 1.5 0 0 1 6 12.5v-1zm1.5-.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1zm4.5.5a1.5 1.5 0 0 1 1.5-1.5h1a1.5 1.5 0 0 1 1.5 1.5v1a1.5 1.5 0 0 1-1.5 1.5h-1a1.5 1.5 0 0 1-1.5-1.5v-1zm1.5-.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1zM6 3.5A1.5 1.5 0 0 1 7.5 2h1A1.5 1.5 0 0 1 10 3.5v1A1.5 1.5 0 0 1 8.5 6h-1A1.5 1.5 0 0 1 6 4.5v-1zM7.5 3a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1z" />
                            <path fillRule="evenodd" d="M8 5a.5.5 0 0 1 .5.5V7H14a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-1 0V8h-5v.5a.5.5 0 0 1-1 0V8h-5v.5a.5.5 0 0 1-1 0v-1A.5.5 0 0 1 2 7h5.5V5.5A.5.5 0 0 1 8 5z" />
                        </svg>
                    </Link>
                </div>
            )
        } else if (!loading && !commentsInDb) {
            return (
                <div className="col-sm-2">
                    <Link>
                        <svg onClick={loadCommentsForSubmission} width="1em" height="1em" viewBox="0 0 16 16" className="bi bi-search" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                            <path fillRule="evenodd" d="M10.442 10.442a1 1 0 0 1 1.415 0l3.85 3.85a1 1 0 0 1-1.414 1.415l-3.85-3.85a1 1 0 0 1 0-1.415z" />
                            <path fillRule="evenodd" d="M6.5 12a5.5 5.5 0 1 0 0-11 5.5 5.5 0 0 0 0 11zM13 6.5a6.5 6.5 0 1 1-13 0 6.5 6.5 0 0 1 13 0z" />
                        </svg>
                    </Link>
                </div>
            )
        }
    }

    if (!displayMore) {
        return (
            <div className="col-sm-4">
                <div className="shadow-sm p-3 mb-5 bg-white rounded">
                    <div className="card">
                        <div className="card-body">
                            <div className="row justify-content-between">
                                <div className="col-8">
                                    <p className="card-text"><i><a href={`https://www.reddit.com${props.submission.permalink}`}>/r/{props.submission.subreddit}</a></i></p>
                                </div>
                                <div className="col-sm-2">
                                    <Link>
                                        <svg onClick={() => setDisplayMore(true)} width="1em" height="1em" viewBox="0 0 16 16" className="bi bi-chevron-double-right text-danger" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                            <path fillRule="evenodd" d="M3.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L9.293 8 3.646 2.354a.5.5 0 0 1 0-.708z" />
                                            <path fillRule="evenodd" d="M7.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L13.293 8 7.646 2.354a.5.5 0 0 1 0-.708z" />
                                        </svg>
                                    </Link>
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
                                    <p className="card-text"><i><a href={`https://www.reddit.com${props.submission.permalink}`}>/r/{props.submission.subreddit}</a></i></p>
                                </div>
                                <div className="col-sm-2">
                                    <Link>
                                        <svg onClick={() => setDisplayMore(false)} width="1em" height="1em" viewBox="0 0 16 16" className="bi bi-chevron-double-right text-danger" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                            <path fillRule="evenodd" d="M3.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L9.293 8 3.646 2.354a.5.5 0 0 1 0-.708z" />
                                            <path fillRule="evenodd" d="M7.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L13.293 8 7.646 2.354a.5.5 0 0 1 0-.708z" />
                                        </svg>
                                    </Link>
                                </div>
                            </div>
                            <h6 className="card-subtitle mb-2 text-muted">{props.submission.negative_flag}</h6>
                            <p className="card-text">Sentiment score: {props.submission.sentiment_score}</p>
                            <p className="card-text">Sentiment magnitude: {props.submission.sentiment_magnitude}</p>
                            <p className="card-text">Comments: {props.submission.num_comments}</p>
                            <div className="row justify-content-between">
                                <div className="col-sm-2">
                                    <Link>
                                        <svg width="1em" height="1em" viewBox="0 0 16 16" className="bi bi-chat-right-quote" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                            <path fillRule="evenodd" d="M2 1h12a1 1 0 0 1 1 1v11.586l-2-2A2 2 0 0 0 11.586 11H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1zm12-1a2 2 0 0 1 2 2v12.793a.5.5 0 0 1-.854.353l-2.853-2.853a1 1 0 0 0-.707-.293H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12z" />
                                            <path fillRule="evenodd" d="M7.066 4.76A1.665 1.665 0 0 0 4 5.668a1.667 1.667 0 0 0 2.561 1.406c-.131.389-.375.804-.777 1.22a.417.417 0 1 0 .6.58c1.486-1.54 1.293-3.214.682-4.112zm4 0A1.665 1.665 0 0 0 8 5.668a1.667 1.667 0 0 0 2.561 1.406c-.131.389-.375.804-.777 1.22a.417.417 0 1 0 .6.58c1.486-1.54 1.293-3.214.682-4.112z" />
                                        </svg>
                                    </Link>
                                </div>
                                <div>
                                    {commentsInDbIcon()}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default Submission;