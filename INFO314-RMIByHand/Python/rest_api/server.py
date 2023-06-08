from flask import Flask, jsonify, request
import sys

"""
# The payload format:
#   {
#       "operation": "add",     # Either "add", "subtract", "multiply", "divide", "modulo", or "answer"
#       "operands": [1, 2],     # Either empty or full of numbers
#	    "error": "Invalid operation,
#		"value": 3
#   }
#
#
"""


app = Flask(__name__)


@app.route('/calculator', methods=['POST'])
def calculator_route():
	try:
		if request.method != 'POST':
			return jsonify({'error': 'Invalid request method'}), 400
		if request.headers.get('Content-Type') != 'application/json':
			return jsonify({'error': 'Invalid content type'}), 400
		json_data = request.get_json()
		if 'operation' not in json_data:
			return jsonify({'error': 'Missing operation'}), 400
		if 'operands' not in json_data:
			return jsonify({'error': 'Missing operands'}), 400
		operation = json_data['operation']
		operation = str(operation).lower()
		operands = json_data['operands']
		if operation not in ['add', 'subtract', 'multiply', 'divide', 'modulo', 'answer']:
			return jsonify({'error': 'Invalid operation'}), 400

		# Check if all operands are numbers
		for operand in operands:
			if not isinstance(operand, (int, float)):
				return jsonify({'error': f'{str(operand)} is not a valid argument type'}), 400
			elif operand < -1 * sys.maxsize or operand > sys.maxsize:
				return jsonify({'error': 'Operand too large or too small'}), 400

		# Add
		if operation == 'add':
			if len(operands) == 0:
				return jsonify({'result': 0}), 200
			if len(operands) == 1:
				return jsonify({'result': operands[0]}), 200
			result = operands[0]
			for i in range(1, len(operands)):
				result += operands[i]
			return jsonify({'result': result}), 200

		elif operation == 'subtract':
			if len(operands) == 2:
				# Subtract the second operand from the first
				return jsonify({'result': operands[0] - operands[1]}), 200
			else:
				return jsonify({'error': 'Invalid number of operands for subtraction'}), 400

		elif operation == 'multiply':
			if len(operands) == 0:
				return jsonify({'result': 1}), 200
			elif len(operands) == 1:
				return jsonify({'result': operands[0]}), 200
			result = operands[0]
			for i in range(1, len(operands)):
				result *= operands[i]
			return jsonify({'result': result}), 200

		elif operation == 'divide':
			if operands[1] == 0:
				return jsonify({'error': 'divide by zero'}), 400
			if len(operands) == 2:
				# Divide the first operand by the second
				return jsonify({'result': operands[0] / operands[1]}), 200
			else:
				return jsonify({'error': 'Invalid number of operands for division'}), 400

		elif operation == 'modulo':
			if operands[1] == 0:
				return jsonify({'error': 'divide by zero'}), 400
			if len(operands) == 2:
				# Divide the first operand by the second
				return jsonify({'result': operands[0] % operands[1]}), 200
			else:
				return jsonify({'error': 'Invalid number of operands for modulo'}), 400
		else:
			return jsonify({'error': 'Illegal argument type'}), 400
	except Exception as e:
		return jsonify({'error': str(e)}), 500


# Error handler
@app.errorhandler(404)
def route_not_found(_):
	return jsonify({'error': 'Endpoint not found'}), 404


if __name__ == "__main__":
	app.run(threaded=True, processes=True, debug=False)
