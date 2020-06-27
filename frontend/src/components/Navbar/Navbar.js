import React from 'react';
import {Link} from 'react-router-dom';

function Navbar () {
    
    return (
        <div>
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <Link to="/ui/">
                    <a className="navbar-brand">dhrishti</a>
                </Link>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                    <ul className="navbar-nav">
                        <Link to="/ui/searchreddit" className="nav-link">
                            <li className="nav-item">Search</li>
                        </Link>
                        <Link to="/ui/insights" className="nav-link">
                            <li className="nav-item">Insights</li>
                        </Link>
                        <Link to="/ui/data" className="nav-link">
                            <li className="nav-item">Data</li>
                        </Link>
                    </ul>
                </div>
            </nav>
        </div>
    )
}

export default Navbar;