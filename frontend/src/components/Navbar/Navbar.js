import React from 'react';
import {Link} from 'react-router-dom';

function Navbar () {
    
    return (
        <div>
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <Link to="/">
                    <a class="navbar-brand">dhrishti</a>
                </Link>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <Link to="/searchreddit" class="nav-link">
                            <li class="nav-item">Search</li>
                        </Link>
                        <Link to="/insights" class="nav-link">
                            <li class="nav-item">Insights</li>
                        </Link>
                        <Link to="/data" class="nav-link">
                            <li class="nav-item">Data</li>
                        </Link>
                    </ul>
                </div>
            </nav>
        </div>
    )
}

export default Navbar;