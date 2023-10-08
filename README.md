```bash
uvicorn vaderapi.main:app --log-config=log_conf.yaml

# predict the sentiment
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"text": "This movie is amazing!"}'

# health check
curl -X 'GET' \
  'http://127.0.0.1:8000/health' \
  -H 'accept: application/json'

# metadata
curl -X 'GET' \
  'http://127.0.0.1:8000/metadata' \
  -H 'accept: application/json'
```