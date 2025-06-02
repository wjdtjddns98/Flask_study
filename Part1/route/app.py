from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
@app.route('/about')
def abou123t():
    return "About Page"

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User : {username}'

if __name__ == '__main__':
    app.run()
