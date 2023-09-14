from flask import Flask, request
import json
import os
import subprocess

app = Flask(__name__)

def pull_and_restart(image):
    config = json.load(open("config/config.json", 'r'))
    if not image in config['images']:
        return {'content':'', 'status':'ERR', 'error':'Image not allowed'}
    
    main_dir = config['main_dir']
    image_dir = config['images'][image]
    dir_ = os.path.join(main_dir, image_dir)

    command = f'cd {dir_}; docker compose pull; docker compose down; docker compose up -d'

    run = subprocess.run(command, capture_output=True, shell=True)
    return {"content":image, 'status':'OK', 'error': 'None'}


@app.route('/ping', methods=['POST'])
def ping():
    image = request.data.decode('utf-8').split('=')[-1]
    data = pull_and_restart(image)
    return data

@app.route('/healthcheck')
def healthcheck():
    return {'status':'healthy'}

if __name__ == '__main__':
    if not os.path.exists('config'):
        os.mkdir('config')
    app.run(host="0.0.0.0", port = '8080')