import logging
from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .schemas import (
    HealthCheckOutput,
    MetadataOutput,
    SentimentPredictInput,
    SentimentPredictOutput,
)
from .sentiment_analysis import predict_sentiment

app = FastAPI()
logger = logging.getLogger(__name__)


@app.get("/")
def get_root_redirect_docs():
    return RedirectResponse(url="/docs")


@app.post("/predict")
def post_sentiment_analysis(
    predict_input: SentimentPredictInput,
) -> SentimentPredictOutput:
    """
    Predict the positive/negative/netural sentiment of a given text along with
    a confidence score.

    Args:
        predict_input (SentimentPredictInput): The prediction input object
            which contains the "text" string field on which sentiment analysis
            is performed.

    Returns:
        SentimentPredictOutput: The sentiment and confidence score.
    """
    sentiment_type, score = predict_sentiment(predict_input.text)
    logger.info(
        'Predicted "%s" with a confidence of "%f" for "%s".',
        sentiment_type.value,
        score,
        predict_input.text,
    )
    return SentimentPredictOutput(sentiment=sentiment_type.value, score=score)


@app.get("/health")
def get_health_check() -> HealthCheckOutput:
    """
    Simple health check to verify that the API Server is running.

    Returns:
        HealthCheckOutput: Object describing the API Server status.
    """
    status = "up"
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    logger.info('The API status is "%s" (%s).', status, timestamp)
    return HealthCheckOutput(status=status, timestamp=timestamp)


@app.get("/metadata")
def get_metadata() -> MetadataOutput:
    """
    Describes the model used. The information is based on this commit, which
    is the first commit in the VADER project where the lexicon file matches
    the one from NLTK:
    https://github.com/cjhutto/vaderSentiment/commit/fb3a8a5d899a8e71cd4872110c28f0d8783bdd4a#diff-60f61ab7a8d1910d86d9fda2261620314edcae5894d5aaa236b821c7256badd7

    Returns:
        MetadataOutput: Object describing the model version, type and training
        date.
    """
    return MetadataOutput(
        model_version="0.5.0",
        model_type="VADER Sentiment Analysis",
        model_training_date="2014-11-17",
    )
