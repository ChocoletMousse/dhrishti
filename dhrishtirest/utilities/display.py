def display_annotations(self, title: str, annotations):
    """Print the output of the sentiment analysis"""
    for sentence in annotations.sentences:
        print(f"""
            {"=-" * 10}
            {sentence.text.content} =>
            sentiment: {sentence.sentiment.score},
            magnitude: {annotations.sentiment.magnitude}
        """)