from django import forms


class SearchForm(forms.Form):

    subreddit = forms.CharField(
        label='subreddit',
        max_length=40
    )

    limit = forms.IntegerField(
        label='limit',
        max_value=30,
        min_value=5
    )
