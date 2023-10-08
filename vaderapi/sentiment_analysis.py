import logging
import math
from dataclasses import dataclass
from enum import Enum
from typing import Tuple

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

logger = logging.getLogger(__name__)
logger.info("Downloading the VADER lexicon...")
nltk.download("vader_lexicon")
logger.info("Initializing the sentiment analyzer...")
sid = SentimentIntensityAnalyzer()


@dataclass
class VaderSentimentScores:
    neg: float
    neu: float
    pos: float
    compound: float


class SentimentType(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"


def predict_sentiment(text: str) -> Tuple[SentimentType, float]:
    """Predict the sentiment of a given text.

    Args:
        text (str): The input text.

    Returns:
        Tuple[SentimentType, float]: A tuple of the predicted sentiment type
        and its associated confidence score.
    """
    logger.info('Predicting sentiment of "%s".', text)
    scores = VaderSentimentScores(**sid.polarity_scores(text))
    max_score = max(scores.neu, scores.pos, scores.neg)
    if math.isclose(max_score, scores.neu):
        return (SentimentType.NEUTRAL, max_score)
    elif math.isclose(max_score, scores.pos):
        return (SentimentType.POSITIVE, max_score)
    else:
        return (SentimentType.NEGATIVE, max_score)
