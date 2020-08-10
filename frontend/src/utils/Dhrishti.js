import Cookies from 'js-cookie';
import {React, useState} from 'react';
import axios from 'axios';

const csrfToken = Cookies.get('csrftoken');

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

const Dhrishti = {
    async searchReddit(subreddit, order, limit) {
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
        if (result.ok) {
            console.log('successfully retrieved submission data from reddit.');
            return true;
        } else {
            throw new Error('Something went wrong with the praw? yh... lets blame praw')
        }
    },
    async loadCommentsForSubmission(id) {
        console.log(`received csrf token: ${csrfToken}`);
        console.log('loading comments now for submission: ' + id);
        const url = 'http://127.0.0.1:8000/dhrishti/search/comments';
        response = await axios.post(
            url,
            {submissionId: id},
            {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            }
        );
        if (response.ok) {
            console.log('successfully retrieved comment data from reddit.');
            return true;
        } else {
            throw new Error('Something went wrong with the praw? yh... lets blame praw');
        }
    }
}

export default Dhrishti;