import React from 'react';
import ReactDOM from 'react-dom';
import Navbar from '../Navbar/Navbar';
import SearchForm from '../SearchForm/SearchForm';
import Home from '../Home/Home';
import {BrowserRouter, Route, Switch } from 'react-router-dom'
import Cookies from 'js-cookie';

class App extends React.Component{
    render(){
        return (
            <BrowserRouter>
                <div>
                    <Navbar />
                    <Switch>
                        <Route path='/ui/' exact component={Home} />
                        <Route path='/ui/searchreddit' component={SearchForm} />
                    </Switch>
                </div>
            </BrowserRouter>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'))