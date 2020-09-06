import React from 'react';
import axios from 'axios';
import Submission from './Submission';

class SubmissionsList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [],
            postsInDB: true,
            viewPosts: true,
        }
    }

    async componentDidMount() {
        if (this.state.viewPosts) {
            if (this.state.data.length == 0) {
                const url = 'http://127.0.0.1:8000/dhrishti/data/submissions';
                let response = await axios.get(url);
                if (response.status == 200) {
                    if (!response.data.length > 0) {
                        this.setState({ postsInDB: false });
                    }
                    this.setState({ data: response.data });
                }
            }
        }
    }

    render() {
        if (this.state.data.length == 0 && this.state.postsInDB) {
            return (
                <div className="d-flex justify-content-center align-items-center">
                    <div className="spinner-border text-danger" role="status">
                        <span className="sr-only">Loading...</span>
                    </div>
                </div>
            )
        } else if (!this.state.postsInDB) {
            return (
                <div className="col-md-auto">
                    <div className="alert alert-info" role="alert">
                        Currently no posts in the database. Try searching for a topic!
                        </div>
                </div>
            )
        } else {
            return (
                <div className="container">
                    <div className="row">
                        {this.state.data.map(submission => {
                            return <Submission key={submission.name} submission={submission} />;
                        })}
                    </div>
                </div>
            )
        }
    }
}

export default SubmissionsList;