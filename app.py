# app.py
from script import coffee_bot
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/order', methods=['POST'])
def order_coffee():
    data = request.get_json()

    # Extract information from the request
    cup_size = data.get('cup_size')
    drink_type = data.get('drink_type')
    cup_type = data.get('cup_type')

    # Call the coffee_bot function
    result = coffee_bot(cup_size, drink_type, cup_type)

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
