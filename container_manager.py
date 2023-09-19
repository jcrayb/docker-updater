from flask import Flask, request
import json
import os
import subprocess

app = Flask(__name__)

config = json.load(open("config/config.json", 'r'))
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

@app.route('/pull', methods=['POST'])
def post_pull():
    data = {}
    image = request.args['image']
    data['pull'] = pull_image(image)
    if request.args['restart'] == 'True':
        data['restart'] = restart_container(image)
    return data

@app.route('/restart', methods=['POST'])
def post_restart():
    data = {}
    image = request.args['image']
    data['restart'] = restart_container(image)
    return data

@app.route('/healthcheck')
def healthcheck():
    return {'status':'healthy'}

if __name__ == '__main__':
    if not os.path.exists('config'):
        os.mkdir('config')
    app.run(host="0.0.0.0", port = '7000', debug=True)