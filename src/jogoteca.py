from flask import Flask   # pip install  flask==2.0.2

app = Flask(__name__)

@app.route('/inicio')
def ola():
    return '<p>ola mundo</p>'

app.run()