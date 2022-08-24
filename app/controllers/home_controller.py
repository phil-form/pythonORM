from app import app
from flask import render_template, redirect, jsonify


@app.route('/', methods=['GET'])
def index():
    return jsonify({'error': 'invalid credentials'}), 500
