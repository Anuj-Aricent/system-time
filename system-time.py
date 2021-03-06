import sys
import time

from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class SystemTime(Resource):
    def get(self):
        return { 'time' : time.strftime("%b %d %Y %H:%M:%S") }


api.add_resource(SystemTime, '/time')


if __name__ == '__main__':
    if(len(sys.argv) > 1):
        run_port = sys.argv[1]
    else:
        run_port = 10002
    app.run(host='0.0.0.0',port=int(run_port), debug=True)
