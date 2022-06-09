### 1. Setup Google Cloud 
- Create new project
- Activate Cloud Run API and Cloud Build API

### 2. Install and init Google Cloud SDK
- https://cloud.google.com/sdk/docs/install

### 3. Dockerfile, requirements.txt, .dockerignore
- https://cloud.google.com/run/docs/quickstarts/build-and-deploy#containerizing

### 4. Cloud build & deploy
```
gcloud builds submit --tag gcr.io/relic-classifier/index
gcloud run deploy --image gcr.io/relic-classifier/index --platform managed
```

### Test
- Test the code with `test.py`