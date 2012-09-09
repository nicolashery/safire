from flask import Blueprint, render_template

# Test some relative package imports
from .helpers import helper_msg

safire_blueprint = Blueprint('safire', __name__, 
                                static_folder='static',
                                template_folder='templates')

@safire_blueprint.route('/')
def index():
    return render_template('safire.html')
