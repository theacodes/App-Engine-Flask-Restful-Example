from flask import Flask
from flask.ext import restful


app = Flask(__name__)
api = restful.Api(app)


class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')


# @app.route('/')
# def hello():
#     """Return a friendly HTTP greeting."""
#     return 'Hello World!'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
