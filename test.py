import requests

data = requests.post('https://workflows.jcrayb.com/docker/pull?image=file_sharing&restart=True&auth_key=9c65bfac2feecb04b8c8cb5c78766381')

print(data.json())
