import json
import os
import subprocess
from utils import from_root

config = json.load(open(from_root("config/config.json"), 'r'))
docker_dir = config['docker_dir']

def pull_image(image):
    if not image in config['images']:
        return {'content':'', 'status':'ERR', 'error':'Image not allowed'}
    
    image_dir = config['images'][image]
    dir_ = os.path.join(docker_dir, image_dir)

    command = f'cd {dir_}; docker compose pull'

    run = subprocess.run(command, capture_output=True, shell=True)
    return {"content":image, 'status':'OK', 'error': 'None'}

def restart_container(image):
    if not image in config['images']:
        return {'content':'', 'status':'ERR', 'error':'Image not allowed'}
    

    image_dir = config['images'][image]
    dir_ = os.path.join(docker_dir, image_dir)

    command = f'cd {dir_}; docker compose down; docker compose up -d'

    run = subprocess.run(command, capture_output=True, shell=True)
    return {"content":image, 'status':'OK', 'error': 'None'}
