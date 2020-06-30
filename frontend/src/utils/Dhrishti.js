import Cookies from 'js-cookie';
import {React, useState} from 'react';

const Dhrishti = {
    async searchReddit(subreddit, order, limit) {
        // const [loading, setLoading] = useState(false);
        const csrfToken = Cookies.get('csrftoken');
        const url = `http://127.0.0.1:8000/dhrishti/search`;
        console.log(`received csrf token: ${csrfToken}`);
        console.log(`retrieving the ${order} ${limit} submissions from /r/${subreddit}`);
        let result = await fetch(
            url,
            {
                method: 'POST',
                cache: "no-cache",
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({subreddit: subreddit, order: order, limit: limit})
            }
        );
        // setLoading(true);
        if (result.ok) {
            console.log('successfully retrieved data from reddit.');
            // setLoading(false);
            return false;
        } else {
            throw new Error('Something went wrong with the praw? yh... lets blame praw')
        }
    }
}

export default Dhrishti;