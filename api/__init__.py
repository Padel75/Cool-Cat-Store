from flask import Flask, render_template
import os
from exceptions import errors_bp
from api.routes import login_bp, signup_bp, signout_bp, sell_bp, add_to_cart_bp
from infrastructure.database.database import Database

Database.init_db()

app = Flask(__name__)
#set a key for session(logged in user)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersekrit")

app.register_blueprint(errors_bp)
app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(signout_bp)
app.register_blueprint(sell_bp)
app.register_blueprint(add_to_cart_bp)
print(app.url_map)

@app.route("/")
def main():
    return render_template('login.html')

if __name__ == "__main__":
    app.run()
