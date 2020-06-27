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
            results: []
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
        console.log('handling form to search reddit');
        let results = Dhrishti.searchReddit(
            this.state.subreddit,
            this.state.order,
            parseInt(this.state.limit)
        );
        return results;
    }

    render(){
        return(
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
                                <option value="5">5</option>
                                <option value="10">10</option>
                                <option value="15">15</option>
                            </select>
                        </div>
                        <br />
                        <button className="btn btn-primary" type="submit" onSubmit={this.handleSearch}>Submit</button>
                    </div>
                </form>
            </div>

        )
    }
}

export default SearchForm;