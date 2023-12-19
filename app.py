# app.py
from assignment import get_combinations, get_probabilities, undoom_dice
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return app.send_static_file('dicee.html')

die_A = [1, 2, 3, 4, 5, 6]
die_B = [1, 2, 3, 4, 5, 6]

@app.route('/api/roll-distribution', methods=['GET'])
def roll_distribution():
    combinations = get_combinations(die_A, die_B)
    probabilities = get_probabilities(combinations)
    return jsonify({
        'combinations': combinations,
        'probabilities': probabilities
    })

@app.route('/api/undoom-dice', methods=['POST', 'OPTIONS'])
def undoom_dice_endpoint():
    if request.method == 'OPTIONS':
        # Respond to the preflight request
        response = make_response()
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response

    data = request.get_json()
    new_die_A, new_die_B = undoom_dice(data['die_A'], data['die_B'])
    return jsonify({
        'new_die_A': new_die_A,
        'new_die_B': new_die_B
    })


if __name__ == '__main__':
    app.run(debug=True, port=8080)
