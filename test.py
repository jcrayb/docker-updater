import requests

data = requests.post('https://workflows.jcrayb.com/docker/pull?image=file_sharing&restart=True&auth_key=44c2afcf84ae1456e1d90110958b3a38')

print(data.json())
