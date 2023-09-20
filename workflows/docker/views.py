from flask import Blueprint, request, url_for
from utils import verify_user, ContainerHandler, cwd
from container_manager import restart_container, pull_image


docker = Blueprint('docker', __name__, url_prefix='/docker')

container_handler = ContainerHandler()

@docker.route('/healthcheck')
def healthcheck():
    return {'status':'healthy'}

@docker.route('/pull', methods=['POST'])
def post_pull():
    try:
        auth_key = request.args['auth_key']
    except KeyError:
        return {'content':'', 'status':'ERR', 'error':'Authentication key not provided.'}
    
    if not verify_user(auth_key):
        return {'content':auth_key, 'status':'ERR', 'error':'Authentication failed.'}
    
    try:
        image = request.args['image']
    except KeyError:
        return {'content':'', 'status':'ERR', 'error':'Image name not provided.'}
    
    try:
        restart = request.args['restart']
    except KeyError:
        restart = False
    
    
    data = {}
    
    data['pull'] = pull_image(image)
    if restart:
        data['restart'] = restart_container(image)
    return data

@docker.route('/restart', methods=['POST'])
def post_restart():
    try:
        auth_key = request.args['auth_key']
    except KeyError:
        return {'content':'', 'status':'ERR', 'error':'Authentication key not provided.'}
    
    if not verify_user(auth_key):
        return {'content':auth_key, 'status':'ERR', 'error':'Authentication failed.'}
    
    try:
        image = request.args['image']
    except KeyError:
        return {'content':'', 'status':'ERR', 'error':'Image name not provided.'}
    
    data = {}

    data['restart'] = restart_container(image)
    return data