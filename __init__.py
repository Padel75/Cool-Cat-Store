from flask import Flask, render_template
import os
from exceptions import errors_bp
from routes import login_bp, signup_bp, signout_bp
from database import Database

database = Database()
database.init_db()

app = Flask(__name__)
#set a key for session(logged in user)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersekrit")

app.register_blueprint(errors_bp)
app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(signout_bp)
print(app.url_map)

@app.route("/")
def main():
    return render_template('login.html')

if __name__ == "__main__":
    app.run()
