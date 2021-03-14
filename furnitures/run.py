
from flask import Flask
from flask_restful import Api 
from flask_cors import CORS
from src.api import Channels, Nodes, Products, Skus
from src.models import Database

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Channels,'/channels')
api.add_resource(Nodes,'/nodes/<string:channel>')
api.add_resource(Products,'/products/<string:node>')
api.add_resource(Skus,'/skus/<string:product>','/skus/<string:product>/<string:id>')

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    debug = True
    
    app.run(host,port,debug)
