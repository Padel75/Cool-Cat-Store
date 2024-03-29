from flask import Flask, render_template
from api.token_manager import TokenManager
from exceptions import errors_bp
from flask_cors import CORS
from api.routes import (
    login_bp,
    signup_bp,
    signout_bp,
    sell_bp,
    add_to_cart_bp,
    get_user_infos_bp,
    products_bp,
    seller_products_bp,
    get_cart_bp,
    get_public_seller_bp,
    add_payment_system_bp,
    get_payment_systems_bp,
    pay_bp,
    get_invoices_bp,
)
from infrastructure.database.database import Database
from db_loader import DbLoader


Database.init_db()
db_loader = DbLoader()
db_loader.loadDb()

app: Flask = Flask(__name__)
token_manager: TokenManager = TokenManager(app)
app.config["TOKEN_MANAGER"] = token_manager
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

app.register_blueprint(errors_bp)
app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(signout_bp)
app.register_blueprint(sell_bp)
app.register_blueprint(add_to_cart_bp)
app.register_blueprint(get_user_infos_bp)
app.register_blueprint(products_bp)
app.register_blueprint(seller_products_bp)
app.register_blueprint(get_cart_bp)
app.register_blueprint(get_public_seller_bp)
app.register_blueprint(add_payment_system_bp)
app.register_blueprint(get_payment_systems_bp)
app.register_blueprint(pay_bp)
app.register_blueprint(get_invoices_bp)
print(app.url_map)


@app.route("/")
def main() -> str:
    return render_template("login.html")


if __name__ == "__main__":
    app.run(ssl_context=("certificates/cert.pem", "certificates/key.pem"))
