from flask import Flask
from flask_restplus import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app, version='1.0', title='Sample API', description='A sample API')

name_space = api.namespace('main/aaa/', description='Main APIs')



id_parser = api.parser()
id_parser.add_argument('accessKey', type=str, help='accessKey')
id_parser.add_argument('function', type=str, help='write your function name')
id_parser.add_argument('id', type=str, help='test id')
id_parser.add_argument('password', type=str, help='test password')

@api.doc(params={'function':'executing function name'})
@api.doc(parser=id_parser)
class HelloWorld(Resource):
    def get(self, function):
        return {'hello': 'world test id = ['+reqparse.request.args.get('id') + ']' + reqparse.request.args.get('password') + function}
    def post(self, function):
        print(reqparse.request.args.get('function'))
        return {'hello': 'world test id = ['+reqparse.request.args.get('id') + ']' + reqparse.request.args.get('password') + function}

api.add_resource(HelloWorld, '/modelergateway/uuid12313231/<function>')



"""
for obj in dir(HelloWorld) : 
   print(obj)
"""

if __name__ == '__main__':
    app.run(debug=True)
