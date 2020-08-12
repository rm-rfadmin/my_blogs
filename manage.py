from flask import Flask, Blueprint

app = Flask(__name__)

auth_bp = Blueprint('auth', __name__)
app.register_blueprint(auth_bp, url_prfix='/auth')


app.route('/')
def test():
    return 'hello_world222113'

if __name__ == "__main__":
    app.run()