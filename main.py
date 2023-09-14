from flask import Flask, json, request, jsonify
from dotenv import load_dotenv
import os
import re

app = Flask(__name__)

ipconfig = "127.0.0.1"

@app.route('/flask', methods=['GET'])
def index():
    return "Flask server"

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000, debug=True)



