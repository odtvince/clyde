from flask import Flask, request
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)

class Pong(restful.Resource):
    def post(self):
       hail = request.get_json()
       hail['hail']['status'] = 'received_by_taxi'
       return hail

api.add_resource(Pong, '/hail/')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
