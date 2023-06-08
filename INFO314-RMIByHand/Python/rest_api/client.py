import requests
import sys
import time


headers = {
	'Content-Type': 'application/json',
}


if __name__ == "__main__":
	try:
		# Get the hostname from the first argument of the command line
		hostname = sys.argv[1]
		# Get the port from the second argument of the command line
		port = sys.argv[2]

		# subtract(12, 6) = 6
		result = requests.request('POST', f'http://{hostname}:{port}/calculator', headers=headers, json={'operation': 'subtract', 'operands': [12, 6]})
		json_data = result.json()
		print(json_data)
		assert json_data['result'] == 6

		time.sleep(2)

		# multiply(3, 4) = 12
		result = requests.request('POST', f'http://{hostname}:{port}/calculator', headers=headers, json={'operation': 'multiply', 'operands': [3, 4]})
		json_data = result.json()
		print(json_data)
		assert json_data['result'] == 12

		time.sleep(2)

		# divide(10, 5) = 2
		result = requests.request('POST', f'http://{hostname}:{port}/calculator', headers=headers, json={'operation': 'divide', 'operands': [10, 5]})
		json_data = result.json()
		print(json_data)
		assert json_data['result'] == 2

		time.sleep(2)

		# modulo(10, 5) = 0
		result = requests.request('POST', f'http://{hostname}:{port}/calculator', headers=headers, json={'operation': 'modulo', 'operands': [10, 5]})
		json_data = result.json()
		print(json_data)
		assert json_data['result'] == 0

		time.sleep(2)

		# add(0) = 0
		result = requests.request('POST', f'http://{hostname}:{port}/calculator', headers=headers, json={'operation': 'add', 'operands': [0]})
		json_data = result.json()
		print(json_data)
		assert json_data['result'] == 0

		time.sleep(2)

		# add(1, 2, 3, 4, 5) = 15
		result = requests.request('POST', f'http://{hostname}:{port}/calculator', headers=headers, json={'operation': 'add', 'operands': [1, 2, 3, 4, 5]})
		json_data = result.json()
		print(json_data)
		assert json_data['result'] == 15

		time.sleep(2)

		# multiply(1, 2, 3, 4, 5) = 120
		result = requests.request('POST', f'http://{hostname}:{port}/calculator', headers=headers, json={'operation': 'multiply', 'operands': [1, 2, 3, 4, 5]})
		json_data = result.json()
		print(json_data)
		assert json_data['result'] == 120

		time.sleep(2)

		# Add two very large numbers such that it triggers a stack overflow
		result = requests.request('POST', f'http://{hostname}:{port}/calculator', headers=headers, json={'operation': 'add', 'operands': [-2 * sys.maxsize, 2 * sys.maxsize]})
		json_data = result.json()
		print(json_data)
		assert json_data['error'] == 'Operand too large or too small'

		time.sleep(2)

		# Multiply two very large numbers and trigger an overflow
		result = requests.request('POST', f'http://{hostname}:{port}/calculator', headers=headers, json={'operation': 'multiply', 'operands': [-2 * sys.maxsize, 2 * sys.maxsize]})
		json_data = result.json()
		print(json_data)
		assert json_data['error'] == 'Operand too large or too small'

		# Two string parameters for subtraction
		result = requests.request('POST', f'http://{hostname}:{port}/calculator', headers=headers, json={'operation': 'subtract', 'operands': ['a', 'b']})
		json_data = result.json()
		print(json_data)
		assert result.status_code == 400

		time.sleep(2)

		# Divide by zero
		result = requests.request('POST', f'http://{hostname}:{port}/calculator', headers=headers, json={'operation': 'divide', 'operands': [1, 0]})
		json_data = result.json()
		print(json_data)
		assert json_data['error'] == 'divide by zero'

	except Exception as e:
		print(f'Exception: {str(e)}')
