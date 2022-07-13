from app import app
from flask import render_template, redirect


@app.route('/', methods=['GET'])
def index():
    return render_template('home/home.html')
