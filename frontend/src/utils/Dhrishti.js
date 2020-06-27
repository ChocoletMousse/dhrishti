import Cookies from 'js-cookie'

const csrfToken = Cookies.get('csrftoken');

const Dhrishti = {
    async searchReddit(subreddit, order, limit) {
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
        if (result.ok) {
            let jsonResponse = await result.json();
            console.log(`received ${jsonResponse}`);
            return jsonResponse;
        }
    }
}

export default Dhrishti;