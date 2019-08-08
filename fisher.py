

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

@app.route('/hello')
def hello():
    return 'Hello, TerrySH'


app.run(host='0.0.0.0',debug=app.config['DEBUG'], port=81)