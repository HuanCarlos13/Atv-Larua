
from flask import Flask
from service import Service
import json

app = Flask(__name__)

@app.route("/")
def endpoint():
    return "hello, world"