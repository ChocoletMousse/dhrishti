import React from 'react';

class SearchForm extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            subreddit: '',
            order: 'top',
            limit: 0
        };
        this.handleSubredditChange = this.handleSubredditChange.bind(this);
        this.handleOrderChange = this.handleOrderChange.bind(this);
        this.handleLimitChange = this.handleLimitChange.bind(this);
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

    render(){
        return(
            <div className="SearchForm">
                <form>
                    <div class="form-group col-md-6">
                        <label>Subreddit</label>
                        <input type="text" class="form-control" id="subreddit" placeholder="e.g. Coronavirus" 
                            onChange={this.handleSubredditChange} />
                        <div class="col-auto my-1">
                            <label class="mr-sm-2" for="inlineFormCustomSelect">Order</label>
                            <select class="custom-select mr-sm-2" id="inlineFormCustomSelect" onSelect={this.handleOrderChange}>
                                <option selected>Choose...</option>
                                <option value="top">top</option>
                                <option value="latest">latest</option>
                                <option value="controversial">controversial</option>
                            </select>
                        </div>
                        <div class="col-auto my-1">
                            <label class="mr-sm-2">Limit</label>
                            <select class="custom-select mr-sm-2" id="inlineFormCustomSelect" onSelect={this.handleLimitChange}>
                                <option selected>Choose...</option>
                                <option value="5">5</option>
                                <option value="10">10</option>
                                <option value="15">15</option>
                            </select>
                        </div>
                        <br />
                        <button type="submit" class="btn btn-primary">Submit</button>
                    </div>
                </form>
            </div>
        )
    }
}

export default SearchForm;