from flask import Flask

#create new flask app instance
app = Flask(__name__)

#create flask route
@app.route('/')
def hello_world():
    return 'Hello world'
app.run()