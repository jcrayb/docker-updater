import json
import os

cwd = os.getcwd()

def from_root(path):
    return os.path.join(cwd, path)

class ContainerHandler():
    def __init__(self) -> None:
        json_data = json.load(open('config/container_handler.json', 'r'))
        self.protocol = json_data['protocol']
        self.host = json_data['host']
        self.port = json_data['port']

def verify_user(key):
    if key == open(from_root('config/key'), 'r').read():
        return True
    return False

