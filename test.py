import json
import os
import subprocess

image = 'dev'

config = json.load(open("config/test.json", 'r'))
main_dir = config['main_dir']
image_dir = config['images'][image]
dir_ = os.path.join(main_dir, image_dir)

command = f'cd {dir_}; docker compose pull; docker compose down; docker compose up -d'

run = subprocess.run(command, capture_output=True, shell=True)
print(run)