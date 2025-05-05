from flask import Flask, render_template, jsonify
import json
from pathlib import Path

app = Flask(__name__)

def load_json(file_path):
    try:
        with open(file_path) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

@app.route("/")
def index():
    report = load_json("../reports/latest_report.json")
    suggestions = load_json("../reports/suggestions.json")
    return render_template("dashboard.html", report=report, suggestions=suggestions)

@app.route("/api/report")
def report_api():
    return jsonify(load_json("../reports/latest_report.json"))

@app.route("/api/suggestions")
def suggestions_api():
    return jsonify(load_json("../reports/suggestions.json"))

if __name__ == "__main__":
    app.run(debug=True)
