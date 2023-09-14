from flask import Flask, json, request, jsonify
from dotenv import load_dotenv
import os
import re

import instaloader as igldr
import pandas as pd
import numpy as np

app = Flask(__name__)

ipconfig = ""

@app.route('/flask', methods=['GET'])
def index():
    return "Flask server"

if __name__ == "__main__":
    app.run(ipaddress=ipconfig,port=5000, debug=True)


