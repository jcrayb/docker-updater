import os

cwd = os.getcwd()

def from_root(path):
    return os.path.join(cwd, path)

def verify_user(key):
    if str(key) == str(open(from_root('config/key'), 'r').read().replace('\n', '')):
        return True
    return False