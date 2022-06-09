import requests

resp = requests.post("http://127.0.0.1:5000/", files={'imagefile': open('./test/example_images/candi-borobudur.jpg', 'rb')})
# resp = requests.post("https://getprediction-qyqf4nfema-et.a.run.app", files={'imagefile': open('./test/example_images/candi-borobudur.jpg', 'rb')})


print(resp.json())