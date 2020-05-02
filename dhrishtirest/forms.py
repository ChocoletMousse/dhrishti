from django import forms


class SearchForm(forms.Form):

    SUBMISSIONS_ORDER = [
        ('latest', 'latest'),
        ('top', 'top')
    ]

    subreddit = forms.CharField(
        label='subreddit',
        max_length=40
    )

    submissions_limit = forms.IntegerField(
        label='submissions per subreddit',
        max_value=30,
        min_value=1
    )

    comments_limit = forms.IntegerField(
        label='comments per submission',
        max_value=30,
        min_value=1
    )

    responses_limit = forms.IntegerField(
        label='responses per comment',
        max_value=30,
        min_value=1
    )

    order = forms.ChoiceField(
        label='order',
        choices=SUBMISSIONS_ORDER
    )
