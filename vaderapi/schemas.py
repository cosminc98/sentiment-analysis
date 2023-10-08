from pydantic import BaseModel, Field, ConfigDict


class SentimentPredictInput(BaseModel):
    text: str = Field(min_length=1, max_length=256)


class SentimentPredictOutput(BaseModel):
    sentiment: str
    score: float


class HealthCheckOutput(BaseModel):
    status: str
    timestamp: str


class MetadataOutput(BaseModel):
    model_version: str
    model_type: str
    model_training_date: str

    # ignore warnings about the protected "model_" namespace
    model_config = ConfigDict(protected_namespaces=())
