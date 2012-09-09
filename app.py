# This app is just to test the blueprint package
import os
from flask import Flask

from safire.blueprint import safire_blueprint

application = app = Flask(__name__)

# Must use a url prefix or else serving blueprint's static files won't work
app.register_blueprint(safire_blueprint, url_prefix='/safire')

app.debug = False

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)