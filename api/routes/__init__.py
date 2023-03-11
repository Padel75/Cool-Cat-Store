from flask import Blueprint, render_template, request
from . import login, signup, signout, sell, add_to_cart, get_user_infos

login_bp = Blueprint("login", __name__, template_folder="templates")
signup_bp = Blueprint("signup", __name__)
signout_bp = Blueprint("signout", __name__)
sell_bp = Blueprint("sell", __name__)
add_to_cart_bp = Blueprint("add_to_cart", __name__)
get_user_infos_bp = Blueprint("get_user_infos", __name__)
