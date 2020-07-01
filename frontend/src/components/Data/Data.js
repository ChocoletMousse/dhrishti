import React from 'react';
import axios from 'axios';
import Submission from '../Data/Submission';

class Data extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: []
        }
    }

    async componentDidMount() {
        if (this.state.data.length == 0) {
            const url = 'http://127.0.0.1:8000/dhrishti/data';
            let response = await axios.get(url);
            if (response.status == 200) {
                this.setState({data: response.data})
            }
        }
    }

    render() {
        if (this.state.data.length == 0) {
            return (
                <div className="d-flex justify-content-center">
                    <div className="spinner-border text-danger" role="status">
                        <span className="sr-only">Loading...</span>
                    </div>
                </div>
            ) 
        } else {
            return (
                <div>
                    {this.state.data.map(submission => {
                        return <Submission key={submission.name} submission={submission} />;
                    })}
                </div>
            )
        }
    }
}

export default Data;