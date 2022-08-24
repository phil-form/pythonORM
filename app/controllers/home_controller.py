from app import app
from flask import render_template, redirect, jsonify


@app.route('/', methods=['GET'])
def index():
    # return render_template('home/home.html')
    return jsonify({'error': 'WRONG URL'}), 500
