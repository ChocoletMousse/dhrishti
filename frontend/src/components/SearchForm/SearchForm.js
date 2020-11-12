import React from 'react';
import Dhrishti from '../../utils/Dhrishti';
// import {Link} from 'react-router-dom';

class SearchForm extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            subreddit: '',
            order: 'top',
            limit: 0,
            loading: false
        };
        this.handleSubredditChange = this.handleSubredditChange.bind(this);
        this.handleOrderChange = this.handleOrderChange.bind(this);
        this.handleLimitChange = this.handleLimitChange.bind(this);
        this.handleSearch = this.handleSearch.bind(this);
    }

    handleSubredditChange(e) {
        this.setState({subreddit: e.target.value});
    }

    handleOrderChange(e) {
        this.setState({order: e.target.value});
    }

    handleLimitChange(e) {
        this.setState({limit: e.target.value});
    }

    handleSearch(e) {
        e.preventDefault();
        this.setState({loading: true});
        console.debug('handling form to search reddit');
        Dhrishti.searchReddit(
            this.state.subreddit,
            this.state.order,
            parseInt(this.state.limit)
        ).then(success => {
            this.setState({loading: !success})
        }).catch(error => console.log(error));
    }

    render(){
        return(
            <div className="container">
                <div className="col-md-6">
                    <div className="SearchForm">
                        <form onSubmit={this.handleSearch}>
                            <div className="form-group col-md-6">
                                <label>Subreddit</label>
                                <input type="text" className="form-control" id="subreddit" placeholder="e.g. Coronavirus"
                                    onChange={this.handleSubredditChange} />
                                <div className="col-auto my-1">
                                    <label className="mr-sm-2" htmlFor="inlineFormCustomSelect">Order</label>
                                    <select className="custom-select mr-sm-2" id="inlineFormCustomSelect" onChange={this.handleOrderChange}>
                                        <option defaultValue={"top"}>Choose...</option>
                                        <option value="top">top</option>
                                        <option value="latest">latest</option>
                                        <option value="controversial">controversial</option>
                                    </select>
                                </div>
                                <div className="col-auto my-1">
                                    <label className="mr-sm-2">Limit</label>
                                    <select className="custom-select mr-sm-2" id="inlineFormCustomSelect" onChange={this.handleLimitChange}>
                                        <option defaultValue={"5"}>Choose...</option>
                                        <option value="2">2</option>
                                        <option value="5">5</option>
                                        <option value="10">10</option>
                                        <option value="15">15</option>
                                    </select>
                                </div>
                                <br />
                                {
                                    this.state.loading
                                        ? (
                                            <button className="btn btn-primary" type="submit" disabled>
                                                <span className="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>
                                    Loading...
                                            </button>
                                        )
                                        : (
                                            <button className="btn btn-primary" type="submit" onSubmit={this.handleSearch}>Submit</button>
                                        )
                                }
                            </div>
                        </form>
                    </div>
                </div>
            </div>

        )
    }
}

export default SearchForm;