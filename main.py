from flask import Flask, request, jsonify, render_template
from utils import get_stock_stats

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/api/v1/stats", methods=["GET"])
def stock_stats():
    symbol = request.args.get("symbol", "").upper()
    if not symbol:
        return jsonify({"error": "Symbol parameter is required"}), 400

    try:
        result = get_stock_stats(symbol)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
