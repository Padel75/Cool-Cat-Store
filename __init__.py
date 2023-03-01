from flask import Flask, render_template
from routes import login_bp, signup_bp, signout_bp
from database import init_db

init_db()

app = Flask(__name__)
app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(signout_bp)
print(app.url_map)

@app.route("/")
def main():
    return render_template('login.html')

if __name__ == "__main__":
    app.run()
