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

    limit = forms.IntegerField(
        label='limit',
        max_value=30,
        min_value=5
    )

    order = forms.ChoiceField(
        label='order',
        choices=SUBMISSIONS_ORDER
    )
