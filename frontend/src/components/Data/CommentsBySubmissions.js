import React, {useEffect, useState} from 'react';
import Comment from './Comment';
import axios from 'axios';
import {Link} from 'react-router-dom';

const CommentsBySubmission = ({ match }) => {
    const [commentData, setCommentData] = useState([]);

    useEffect(() => {
        loadComments();
    }, [])

    let loadComments = async () => {
        console.log(`loading new comments with: ${match.params}`);
        const url = `http://127.0.0.1:8000/dhrishti/data/comments/${match.params.submissionId}`;
        let response = await axios.get(url);
        if (response.status == 200) {
            if (!response.data.length > 0) {
                console.log(`No comments found for submission ${match.params.submissionId}. Try loading comments first.`);
            }
            console.log(`received the following: ${response.data}`)
            setCommentData(response.data);
        }
        else {
            throw new Error(`Error trying to load comments for submission ${match.params.submissionId}.`);
        }
    }

// TODO get this to display.
    return (
        <div>
            <div className="container">
                <div className="row align-items-center">
                    <div className="col-2 align-self-center text-center">
                        <Link to="/ui/data">
                            <button type="button" className="btn btn-outline-danger">all posts</button>
                        </Link>
                    </div>
                    <div className="col-2 offset-sm-3 align-self-center text-center">
                        <h1>{match.params.submissionId}</h1>
                    </div>
                </div>
            </div>
            <div className="container">
                <div className="row">
                    {commentData.map(comment => {
                        return <Comment key={comment.id} comment={comment} />;
                    })}
                </div>
            </div>
        </div>
    )
}

export default CommentsBySubmission;