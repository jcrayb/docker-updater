import requests

data = requests.post('http://localhost:8080/docker/pull?image=test&restart=True&auth_key=44c2afcf84ae1456e1d90110958b3a38')

print(data.json())
