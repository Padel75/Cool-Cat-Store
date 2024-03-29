from flask import Blueprint, render_template, request

login_bp = Blueprint("login", __name__, template_folder="templates")
signup_bp = Blueprint("signup", __name__)
signout_bp = Blueprint("signout", __name__)
sell_bp = Blueprint("sell", __name__)
add_to_cart_bp = Blueprint("add_to_cart", __name__)
get_user_infos_bp = Blueprint("get_user_infos", __name__)
products_bp = Blueprint("products", __name__)
seller_products_bp = Blueprint("seller_products", __name__)
get_cart_bp = Blueprint("get_cart", __name__)
get_public_seller_bp = Blueprint("get_public_seller", __name__)
add_payment_system_bp = Blueprint("add_payment_system", __name__)
get_payment_systems_bp = Blueprint("get_payment_systems", __name__)
pay_bp = Blueprint("pay", __name__)
get_invoices_bp = Blueprint("get_invoices", __name__)

from api.routes import (
    login,
    signup,
    signout,
    sell,
    add_to_cart,
    get_cart,
    products,
    seller_products,
    get_user_infos,
    get_public_seller,
    add_payment_system,
    get_payment_systems,
    pay,
    get_invoices,
)