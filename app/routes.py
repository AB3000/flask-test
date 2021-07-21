from app import app
from flask import request

# @app.route('/')
# @app.route('/index')
# def index():
#     return "Hello, World!"

@app.route('/', methods=['GET', 'POST'])
def post_route():
    if request.method == 'POST':

        data = request.get_json()

        print('Data Received: "{data}"'.format(data=data))
        return "Request Processed.\n"

# app.run()