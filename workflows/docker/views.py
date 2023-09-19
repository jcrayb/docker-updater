from flask import Blueprint, request, url_for
from utils import verify_user, ContainerHandler, cwd
import requests


docker = Blueprint('docker', __name__, url_prefix='/docker')

container_handler = ContainerHandler()

@docker.route('/healthcheck')
def healthcheck():
    return {'status':'healthy'}

@docker.route('/pull', methods=['GET'])
def post_pull():
    try:
        image = request.args['image']
    except KeyError:
        return {'content':'', 'status':'ERR', 'error':'Image name not provided.'}
    
    try:
        restart = request.args['restart']
    except KeyError:
        restart = False
    
    try:
        auth_key = request.args['auth_key']
    except KeyError:
        return {'content':'', 'status':'ERR', 'error':'Authentication key not provided.'}
    
    if not verify_user(auth_key):
        return {'content':'', 'status':'ERR', 'error':'Authentication failed.'}
    
    
    data = requests.post(f"{container_handler.protocol}{container_handler.host}:{container_handler.port}/pull?image={image}&restart={restart}&auth_key={auth_key}").json()
    return data

@docker.route('/restart', methods=['GET'])
def post_restart():
    try:
        image = request.args['image']
    except KeyError:
        return {'content':'', 'status':'ERR', 'error':'Image name not provided.'}
    
    try:
        auth_key = request.args['auth_key']
    except KeyError:
        return {'content':'', 'status':'ERR', 'error':'Authentication key not provided.'}
    
    if not verify_user(auth_key):
        return {'content':'', 'status':'ERR', 'error':'Authentication failed.'}
    
    data = requests.post(f"{container_handler.protocol}{container_handler.host}:{container_handler.port}/restart?image={image}&auth_key={auth_key}").json()
    print(f"{container_handler.protocol}{container_handler.host}:{container_handler.port}/restart?image={image}&auth_key={auth_key}")
    return data