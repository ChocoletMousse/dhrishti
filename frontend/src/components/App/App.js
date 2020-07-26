import React from 'react';
import ReactDOM from 'react-dom';
import Navbar from '../Navbar/Navbar';
import SearchForm from '../SearchForm/SearchForm';
import Home from '../Home/Home';
import Data from '../Data/Data';
import {BrowserRouter, Route, Switch } from 'react-router-dom'

class App extends React.Component{
    render(){
        return (
            <BrowserRouter>
                <div>
                    <Navbar />
                    <Switch>
                        <Route path='/ui/' exact component={Home} />
                        <Route path='/ui/searchreddit' component={SearchForm} />
                        <Route path='/ui/data' exact component={Data} />
                        {/* <Route path='/ui/data/convos/:id' component={CommentsList} /> */}
                    </Switch>
                </div>
            </BrowserRouter>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'))