import requests

data = requests.post('http://docker.jcrayb.com/ping', data={'image':'monitoring'}, headers={'Content-Type':'application/json'})

print(data.json())
