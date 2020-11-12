import React, {useEffect, useState} from 'react'

const Insights = () => {

    const [subreddit, setSubreddit] = useState('');

    return (
        <div>
            <div className="container">
                <div className="row align-items-center">
                    <div className="col-2 offset-sm-5 align-self-center text-center">
                        <h1>Insights</h1>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Insights;