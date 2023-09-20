from workflows.docker.views import docker

from flask import Flask

app = Flask(__name__)
app.register_blueprint(docker)

@app.route('/healthcheck')
def healthcheck():
    return {'status':'healthy'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)