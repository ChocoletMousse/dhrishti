from utils import constants


def sentiment_score(entity) -> bool:
    if entity.sentiment.score < constants.MIN_SENTIMENT_SCORE:
        return True
    return False


def sentiment_magnitude(entity) -> bool:
    if entity.sentiment.magnitude > constants.MIN_SENTIMENT_MAGNITUDE:
        return True
    return False


def salience_score(entity) -> bool:
    if entity.salience > constants.MIN_SALIENCE_SCORE:
        return True
    return False
