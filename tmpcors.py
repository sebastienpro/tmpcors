import json

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=["POST"])
def post_data():
    file = open("/tmp/collage.txt", "a")
    file.write(str(request.data)+'\n')
    file.close()
    return request.data


if __name__ == '__main__':
    app.run()
