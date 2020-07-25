import React from 'react';
import {Link} from 'react-router-dom';
import SubmissionsList from './SubmissionsList';
import CommentsList from './CommentsList';

class Data extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            active: 'posts'
        }
        this.displayPosts = this.displayPosts.bind(this);
        this.displayConvos = this.displayConvos.bind(this);
    }

    displayPosts(e) {
        if (this.state.active !== 'posts') {
            this.setState({ active: 'posts' });
            e.preventDefault(); 
        }
        
    }
    
    displayConvos(e) {
        if (this.state.active !== 'convos') {
            this.setState({ active: 'convos' });
            e.preventDefault();
        }
        
    }

    render() {
        if (this.state.active === 'posts') {
            return (
                <div>
                    <div className="container">
                        <div className="row align-items-center">
                            <div className="col-2 offset-sm-5 align-self-center text-center">
                                <h1>all posts</h1>
                            </div>
                            <div className="col-2 offset-sm-3 align-self-center text-center">
                                <button type="button" className="btn btn-outline-info" onClick={this.displayConvos}>all convos</button>
                            </div>
                        </div>
                    </div>
                    <SubmissionsList />
                </div>
            )
        } else if (this.state.active === 'convos') {
            return (
                <div>
                    <div className="container">
                        <div className="row align-items-center">
                            <div className="col-2 align-self-center text-center">
                                <button type="button" className="btn btn-outline-info" onClick={this.displayPosts}>all posts</button>
                            </div>
                            <div className="col-2 offset-sm-3 align-self-center text-center">
                                <h1>all convos</h1>
                            </div>
                        </div>
                    </div>
                    <CommentsList />
                </div>
            )
        }
    }
}

export default Data;