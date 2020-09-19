from utils import constants


def sentiment_score(entity) -> bool:
    return entity.sentiment.score < constants.MIN_SENTIMENT_SCORE


def sentiment_magnitude(entity) -> bool:
    return entity.sentiment.magnitude > constants.MIN_SENTIMENT_MAGNITUDE


def salience_score(entity) -> bool:
    return entity.salience > constants.MIN_SALIENCE_SCORE
