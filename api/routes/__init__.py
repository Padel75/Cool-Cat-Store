from flask import Blueprint, render_template, request

login_bp = Blueprint('login', __name__, template_folder='templates')
signup_bp = Blueprint('signup', __name__)
signout_bp = Blueprint('signout', __name__)
sell_bp = Blueprint('sell', __name__)

from . import login
from . import signup
from . import signout
from . import sell