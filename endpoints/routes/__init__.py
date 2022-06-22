from flask import Flask
from .account import account

app = Flask(__name__)
app.register_blueprint(account)