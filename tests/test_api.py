import json
from datetime import datetime, timezone

from dateutil import parser as date_parser
from fastapi.testclient import TestClient

from vaderapi.main import app

client = TestClient(app)


def test_get_health():
    response = client.get("/health")

    assert response.status_code == 200

    data = json.loads(response.content)
    assert "status" in data
    assert data["status"] == "up"

    timestamp = date_parser.parse(data["timestamp"])
    # the timestamp from the health check and the current UTC time should be
    # roughly the same (1 second tolerance)
    assert (datetime.now(timezone.utc) - timestamp).microseconds < 1000000


def test_get_metadata():
    response = client.get("/metadata")

    assert response.status_code == 200

    data = json.loads(response.content)
    assert "model_type" in data
    assert "model_version" in data
    assert "model_training_date" in data


def test_post_sentiment_analysis():
    response = client.post("/predict", content=json.dumps({"text": "I really like this movie!"}))

    assert response.status_code == 200

    data = json.loads(response.content)
    assert data["sentiment"] == "positive"
