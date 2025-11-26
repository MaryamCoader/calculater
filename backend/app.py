from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})

@app.route('/api/calc', methods=['POST'])
def calculate():
    data = request.get_json()
    if not data:
        return jsonify({"result": None, "error": "Invalid JSON"}), 400

    op = data.get('op')
    a = data.get('a')
    b = data.get('b')

    if not all([op, a is not None, b is not None]):
        return jsonify({"result": None, "error": "Missing 'op', 'a', or 'b' parameters"}), 400

    try:
        a = float(a)
        b = float(b)
    except (ValueError, TypeError):
        return jsonify({"result": None, "error": "Parameters 'a' and 'b' must be numbers"}), 400

    result = None
    error = None

    if op == 'add':
        result = a + b
    elif op == 'subtract':
        result = a - b
    elif op == 'multiply':
        result = a * b
    elif op == 'divide':
        if b == 0:
            error = "Division by zero is not allowed"
        else:
            result = a / b
    elif op == 'modulo':
        if b == 0:
            error = "Modulo by zero is not allowed"
        else:
            result = a % b
    elif op == 'power':
        result = a ** b
    else:
        error = f"Unsupported operation: {op}"

    if error:
        return jsonify({"result": None, "error": error}), 400
    else:
        # Check if result is an integer to avoid .0 for whole numbers
        if result == int(result):
            result = int(result)
        return jsonify({"result": result, "error": None})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
