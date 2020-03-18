from flask import Flask
from flask_restful import Api, Resource, marshal_with, fields

app = Flask(__name__)
api = Api(app)


class User(object):
    def __init__(self, username, age, school):
        self.username = username
        self.age = age
        self.school = school


user = User(username='zhiliao', age=18, school="牛津大学")


class HomePageView(Resource):
    response_field = {
        "username": fields.String,
        "age": fields.Integer,
        "school": fields.String
    }

    @marshal_with(response_field)
    def get(self):
        return user


api.add_resource(HomePageView, '/', endpoint="index")

if __name__ == '__main__':
    app.run(debug=True)
