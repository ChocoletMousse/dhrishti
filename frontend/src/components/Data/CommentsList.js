import React from 'react';
import axios from 'axios';
import Comment from './Comment';

class CommentsList extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            data: [],
            commentsInDB: true,
            viewComments: true,
        }
    }

    async componentDidMount() {
        if (this.state.viewComments) {
            if (this.state.data.length == 0) {
                const url = '/dhrishti/data/comments';
                let response = await axios.get(url);
                if (response.status == 200) {
                    if (!response.data.length > 0) {
                        this.setState({ commentsInDB: false });
                    }
                    this.setState({ data: response.data });
                }
            }
        }
    }

    render() {
        if (this.state.data.length == 0 && this.state.commentsInDB) {
            return (
                <div className="d-flex justify-content-center align-items-center">
                    <div className="spinner-border text-info" role="status">
                        <span className="sr-only">Loading...</span>
                    </div>
                </div>
            )
        } else if (!this.state.commentsInDB) {
            return (
                <div className="col-md-auto">
                    <div className="alert alert-info" role="alert">
                        Currently no convos in the database. Try loading convos from the posts!
                        </div>
                </div>
            )
        } else {
            return (
                <div className="container">
                    <div className="row">
                        {this.state.data.map(comment => {
                            return <Comment key={comment.id} comment={comment} />;
                        })}
                    </div>
                </div>
            )
        }
    }
}

export default CommentsList;