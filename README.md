# Relic / Monument / Landmark Classifier for Dinara

![Discover Nusantara Cover](logo/dinara_cover.png)

Bangkit 2022 Capstone Project Classifier for Dinara 

## Deploying
1. Create new Google Cloud project
2. Install Cloud Run API && Cloud Build API
3. Install and init Google Cloud SDK
4. Run commands below
```plaintext
gcloud builds submit --tag gcr.io/relic-classifier/index
gcloud run deploy --image gcr.io/relic-classifier/index --platform managed
```

## Usage 
Usage is really straight up, after deploying model with steps above we simply
send a file using HTTP POST with 'imagefile' and the images itself as key value
pair and the deployed model sends back a JSON response containing the predicted image.

```py
import requests

resp = requests.post("https://getprediction-qyqf4nfema-et.a.run.app", files={'imagefile': open('./test/example_images/candi-borobudur.jpg', 'rb')})

print(resp.json())
```

or you can just use it locally by running 'main.py' and flask will run a local
server instead

```py
import requests

resp = requests.post("https://getprediction-qyqf4nfema-et.a.run.app", files={'imagefile': open('./test/example_images/candi-borobudur.jpg', 'rb')})

print(resp.json())
```