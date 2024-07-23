import requests

req = requests.post(url='http://127.0.0.1:5000/delete_fruit', json={'_id':'65eef2baaa9f82813288f19b'})
print(req.json())