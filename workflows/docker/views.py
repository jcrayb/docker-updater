from flask import Blueprint, request, url_for
from utils import verify_user, ContainerHandler
import requests

docker = Blueprint('docker', __name__, url_prefix='/docker')

@docker.route('/healthcheck')
def healthcheck():
    return {'status':'healthy'}

@docker.route('/pull', methods=['POST'])
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
    
    container_handler = ContainerHandler()
    data = requests.post(f"{container_handler.protocol}{container_handler.host}:{container_handler.port}/pull?image={image}&restart={restart}")
    return {'status':'Test succesful'}