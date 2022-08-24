from app import app
from flask import jsonify, redirect, render_template


@app.route("/", methods=["GET"])
def index():
    return jsonify({"error": "invalid credentials"}), 500
