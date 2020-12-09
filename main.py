from flask import Flask, redirect
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


count: int = 0


class Get(Resource):
    def get(self):
        global count
        ret = count
        count += 1
        return {'count': ret}, 200


class Reset(Resource):
    def get(self):
        global count
        count = 0
        return {'status': 'ok'}, 200


class Home(Resource):
    def get(self):
        return {'resources': ['GET /get', 'GET /reset']}, 200


api.add_resource(Get, '/get')
api.add_resource(Reset, '/reset')
api.add_resource(Home, '/')


if __name__ == '__main__':
    app.run()

