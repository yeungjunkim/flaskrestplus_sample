from flask import Flask
from flask_restplus import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app, version='1.0', title='Sample API', description='A sample API')

name_space = api.namespace('main/aaa/', description='Main APIs')

@api.doc(params={'idtest':'An ID'})
class HelloWorld(Resource):
    def get(self,idtest):
        return {'hello': 'world test'+idtest}
    def post(self,idtest):
        return {'hello': 'world test'+idtest}


api.add_resource(HelloWorld, '/hello/<idtest>')



"""
for obj in dir(HelloWorld) : 
   print(obj)
"""

if __name__ == '__main__':
    app.run(debug=True)
