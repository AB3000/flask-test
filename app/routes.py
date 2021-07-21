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

app.run()

# from flask import render_template
# from app import app
# from app.forms import LoginForm

# # @app.route('/')
# # @app.route('/index')
# # def index():
# #     return "Hello, World!"

# @app.route('/login')
# def login():
#     form = LoginForm()
#     #form = form line passes form object (right) to the template (left)
#     return render_template('templates/login.html', title='Sign In', form=form)

