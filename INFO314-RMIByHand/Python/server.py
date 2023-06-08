from flask import Flask, request
from lxml import etree
import sys


app = Flask(__name__)


@app.route('/RPC', methods=['POST'])
def rpc_route():
	if request.method != 'POST':
		xml_response = etree.Element('methodResponse')
		fault = etree.SubElement(xml_response, 'fault')
		value = etree.SubElement(fault, 'value')
		struct = etree.SubElement(value, 'struct')
		member = etree.SubElement(struct, 'member')
		name = etree.SubElement(member, 'name')
		name.text = 'faultCode'
		value = etree.SubElement(member, 'value')
		value.text = '405'
		member = etree.SubElement(struct, 'member')
		name = etree.SubElement(member, 'name')
		name.text = 'faultString'
		value = etree.SubElement(member, 'value')
		value.text = 'Method Not Supported'
		return etree.tostring(xml_response, pretty_print=True), 405, {'Content-Type': 'text/xml'}
	try:
		# Parse the XML
		xml_request = etree.fromstring(request.data)
		# Get the method name
		method_name = xml_request.xpath('//methodName')[0].text
		method_name = str(method_name).lower()
		if method_name not in ['add', 'subtract', 'multiply', 'divide', 'modulo']:
			# Create a method not supported XML response
			xml_response = etree.Element('methodResponse')
			fault = etree.SubElement(xml_response, 'fault')
			value = etree.SubElement(fault, 'value')
			struct = etree.SubElement(value, 'struct')
			member = etree.SubElement(struct, 'member')
			name = etree.SubElement(member, 'name')
			name.text = 'faultCode'
			value = etree.SubElement(member, 'value')
			value.text = '3'
			member = etree.SubElement(struct, 'member')
			name = etree.SubElement(member, 'name')
			name.text = 'faultString'
			value = etree.SubElement(member, 'value')
			value.text = 'illegal argument type'
			return etree.tostring(xml_response, pretty_print=True), 500, {'Content-Type': 'text/xml'}
		# Get the method parameters. They should all be i4 types
		i4_method_parameters = xml_request.xpath('//params/param/value/i4')

		# Check if any of the parameters are less than -sys.maxsize or greater than sys.maxsize
		# If so, then trigger an overflow
		for i4_method_parameter in i4_method_parameters:
			if int(i4_method_parameter.text) < -1 * sys.maxsize or int(i4_method_parameter.text) > sys.maxsize:
				# Create an overflow XML response
				xml_response = etree.Element('methodResponse')
				fault = etree.SubElement(xml_response, 'fault')
				value = etree.SubElement(fault, 'value')
				struct = etree.SubElement(value, 'struct')
				member = etree.SubElement(struct, 'member')
				name = etree.SubElement(member, 'name')
				name.text = 'faultCode'
				value = etree.SubElement(member, 'value')
				value.text = '1'
				member = etree.SubElement(struct, 'member')
				name = etree.SubElement(member, 'name')
				name.text = 'faultString'
				value = etree.SubElement(member, 'value')
				value.text = 'overflow'
				return etree.tostring(xml_response, pretty_print=True), 500, {'Content-Type': 'text/xml'}

		# Check if all parameters are numbers
		for i4_method_parameter in i4_method_parameters:
			if not i4_method_parameter.text.isdigit():
				# Create an illegal argument type XML response
				xml_response = etree.Element('methodResponse')
				fault = etree.SubElement(xml_response, 'fault')
				value = etree.SubElement(fault, 'value')
				struct = etree.SubElement(value, 'struct')
				member = etree.SubElement(struct, 'member')
				name = etree.SubElement(member, 'name')
				name.text = 'faultCode'
				value = etree.SubElement(member, 'value')
				value.text = '3'
				member = etree.SubElement(struct, 'member')
				name = etree.SubElement(member, 'name')
				name.text = 'faultString'
				value = etree.SubElement(member, 'value')
				value.text = 'illegal argument type'
				return etree.tostring(xml_response, pretty_print=True), 500, {'Content-Type': 'text/xml'}

		if method_name == 'add':
			# If there are zero parameters, then return 0
			if len(i4_method_parameters) == 0:
				# Create XML to return just 0
				xml_response = etree.Element('methodResponse')
				params = etree.SubElement(xml_response, 'params')
				param = etree.SubElement(params, 'param')
				value = etree.SubElement(param, 'value')
				i4 = etree.SubElement(value, 'i4')
				i4.text = '0'
				return etree.tostring(xml_response, pretty_print=True), 200, {'Content-Type': 'text/xml'}
			if len(i4_method_parameters) == 1:
				# Return the parameter
				xml_response = etree.Element('methodResponse')
				params = etree.SubElement(xml_response, 'params')
				param = etree.SubElement(params, 'param')
				value = etree.SubElement(param, 'value')
				i4 = etree.SubElement(value, 'i4')
				i4.text = i4_method_parameters[0].text
				return etree.tostring(xml_response, pretty_print=True), 200, {'Content-Type': 'text/xml'}
			else:
				# Sum the parameters
				total_sum = 0
				for i4_method_parameter in i4_method_parameters:
					total_sum += int(i4_method_parameter.text)
				# Create the XML response
				xml_response = etree.Element('methodResponse')
				params = etree.SubElement(xml_response, 'params')
				param = etree.SubElement(params, 'param')
				value = etree.SubElement(param, 'value')
				i4 = etree.SubElement(value, 'i4')
				i4.text = str(total_sum)
				return etree.tostring(xml_response, pretty_print=True), 200, {'Content-Type': 'text/xml'}

		elif method_name == "subtract":
			# If there are zero parameters, then return 0
			if len(i4_method_parameters) == 0:
				# Create XML to return just 0
				xml_response = etree.Element('methodResponse')
				params = etree.SubElement(xml_response, 'params')
				param = etree.SubElement(params, 'param')
				value = etree.SubElement(param, 'value')
				i4 = etree.SubElement(value, 'i4')
				i4.text = '0'
				return etree.tostring(xml_response, pretty_print=True), 200, {'Content-Type': 'text/xml'}
			# If there is just one parameter, then return the parameter
			if len(i4_method_parameters) == 1:
				xml_response = etree.Element('methodResponse')
				params = etree.SubElement(xml_response, 'params')
				param = etree.SubElement(params, 'param')
				value = etree.SubElement(param, 'value')
				i4 = etree.SubElement(value, 'i4')
				i4.text = i4_method_parameters[0].text
				return etree.tostring(xml_response, pretty_print=True), 200, {'Content-Type': 'text/xml'}
			# If there are two parameters, then subtract the second from the first
			if len(i4_method_parameters) == 2:
				xml_response = etree.Element('methodResponse')
				params = etree.SubElement(xml_response, 'params')
				param = etree.SubElement(params, 'param')
				value = etree.SubElement(param, 'value')
				i4 = etree.SubElement(value, 'i4')
				i4.text = str(int(i4_method_parameters[0].text) - int(i4_method_parameters[1].text))
				return etree.tostring(xml_response, pretty_print=True), 200, {'Content-Type': 'text/xml'}
			# For more than two parameters, return an error
			else:
				xml_response = etree.Element('methodResponse')
				fault = etree.SubElement(xml_response, 'fault')
				value = etree.SubElement(fault, 'value')
				struct = etree.SubElement(value, 'struct')
				member = etree.SubElement(struct, 'member')
				name = etree.SubElement(member, 'name')
				name.text = 'faultCode'
				value = etree.SubElement(member, 'value')
				value.text = '3'
				member = etree.SubElement(struct, 'member')
				name = etree.SubElement(member, 'name')
				name.text = 'faultString'
				value = etree.SubElement(member, 'value')
				value.text = 'illegal argument type'
				return etree.tostring(xml_response, pretty_print=True), 500, {'Content-Type': 'text/xml'}

		elif method_name == 'multiply':
			if len(i4_method_parameters) == 0:
				# Create XML to return just 1
				xml_response = etree.Element('methodResponse')
				params = etree.SubElement(xml_response, 'params')
				param = etree.SubElement(params, 'param')
				value = etree.SubElement(param, 'value')
				i4 = etree.SubElement(value, 'i4')
				i4.text = '1'
				return etree.tostring(xml_response, pretty_print=True), 200, {'Content-Type': 'text/xml'}
			elif len(i4_method_parameters) == 1:
				# Return the original value
				xml_response = etree.Element('methodResponse')
				params = etree.SubElement(xml_response, 'params')
				param = etree.SubElement(params, 'param')
				value = etree.SubElement(param, 'value')
				i4 = etree.SubElement(value, 'i4')
				i4.text = i4_method_parameters[0].text
				return etree.tostring(xml_response, pretty_print=True), 200, {'Content-Type': 'text/xml'}
			else:
				# Multiply the parameters
				total_product = 1
				for i4_method_parameter in i4_method_parameters:
					total_product *= int(i4_method_parameter.text)
				# Create the XML response
				xml_response = etree.Element('methodResponse')
				params = etree.SubElement(xml_response, 'params')
				param = etree.SubElement(params, 'param')
				value = etree.SubElement(param, 'value')
				i4 = etree.SubElement(value, 'i4')
				i4.text = str(total_product)
				return etree.tostring(xml_response, pretty_print=True), 200, {'Content-Type': 'text/xml'}

		elif method_name == 'divide':
			if len(i4_method_parameters) != 2:
				# Return an error with invalid number of parameters
				xml_response = etree.Element('methodResponse')
				fault = etree.SubElement(xml_response, 'fault')
				value = etree.SubElement(fault, 'value')
				struct = etree.SubElement(value, 'struct')
				member = etree.SubElement(struct, 'member')
				name = etree.SubElement(member, 'name')
				name.text = 'faultCode'
				value = etree.SubElement(member, 'value')
				value.text = '3'
				member = etree.SubElement(struct, 'member')
				name = etree.SubElement(member, 'name')
				name.text = 'faultString'
				value = etree.SubElement(member, 'value')
				value.text = 'Invalid number of parameters'
				return etree.tostring(xml_response, pretty_print=True), 500, {'Content-Type': 'text/xml'}
			elif int(i4_method_parameters[1].text) == 0:
				# Return a faultCode of 1 and a faultString of "divide by zero"
				xml_response = etree.Element('methodResponse')
				fault = etree.SubElement(xml_response, 'fault')
				value = etree.SubElement(fault, 'value')
				struct = etree.SubElement(value, 'struct')
				member = etree.SubElement(struct, 'member')
				name = etree.SubElement(member, 'name')
				name.text = 'faultCode'
				value = etree.SubElement(member, 'value')
				value.text = '1'
				member = etree.SubElement(struct, 'member')
				name = etree.SubElement(member, 'name')
				name.text = 'faultString'
				value = etree.SubElement(member, 'value')
				value.text = 'divide by zero'
				return etree.tostring(xml_response, pretty_print=True), 500, {'Content-Type': 'text/xml'}
			else:
				# Divide the first parameter by the second parameter
				quotient = int(i4_method_parameters[0].text) / int(i4_method_parameters[1].text)
				# Create the XML response
				xml_response = etree.Element('methodResponse')
				params = etree.SubElement(xml_response, 'params')
				param = etree.SubElement(params, 'param')
				value = etree.SubElement(param, 'value')
				i4 = etree.SubElement(value, 'i4')
				i4.text = str(quotient)
				return etree.tostring(xml_response, pretty_print=True), 200, {'Content-Type': 'text/xml'}

		elif method_name == 'modulo':
			# Optionally, I put this in—even though it was not in the specification—because it is a common error handler.
			if len(i4_method_parameters) != 2:
				# Return an error with invalid number of parameters
				xml_response = etree.Element('methodResponse')
				fault = etree.SubElement(xml_response, 'fault')
				value = etree.SubElement(fault, 'value')
				struct = etree.SubElement(value, 'struct')
				member = etree.SubElement(struct, 'member')
				name = etree.SubElement(member, 'name')
				name.text = 'faultCode'
				value = etree.SubElement(member, 'value')
				value.text = '3'
				member = etree.SubElement(struct, 'member')
				name = etree.SubElement(member, 'name')
				name.text = 'faultString'
				value = etree.SubElement(member, 'value')
				value.text = 'Invalid number of parameters'
				return etree.tostring(xml_response, pretty_print=True), 500, {'Content-Type': 'text/xml'}
			elif int(i4_method_parameters[1].text) == 0:
				# Return a faultCode of 1 and a faultString of "divide by zero"
				xml_response = etree.Element('methodResponse')
				fault = etree.SubElement(xml_response, 'fault')
				value = etree.SubElement(fault, 'value')
				struct = etree.SubElement(value, 'struct')
				member = etree.SubElement(struct, 'member')
				name = etree.SubElement(member, 'name')
				name.text = 'faultCode'
				value = etree.SubElement(member, 'value')
				value.text = '1'
				member = etree.SubElement(struct, 'member')
				name = etree.SubElement(member, 'name')
				name.text = 'faultString'
				value = etree.SubElement(member, 'value')
				value.text = 'divide by zero'
				return etree.tostring(xml_response, pretty_print=True), 500, {'Content-Type': 'text/xml'}
			else:
				# Perform the modulo operation and return the value
				modulo = int(i4_method_parameters[0].text) % int(i4_method_parameters[1].text)
				# Create the XML response
				xml_response = etree.Element('methodResponse')
				params = etree.SubElement(xml_response, 'params')
				param = etree.SubElement(params, 'param')
				value = etree.SubElement(param, 'value')
				i4 = etree.SubElement(value, 'i4')
				i4.text = str(modulo)
				return etree.tostring(xml_response, pretty_print=True), 200, {'Content-Type': 'text/xml'}

		else:
			# No method name was found, so return an error
			xml_response = etree.Element('methodResponse')
			fault = etree.SubElement(xml_response, 'fault')
			value = etree.SubElement(fault, 'value')
			struct = etree.SubElement(value, 'struct')
			member = etree.SubElement(struct, 'member')
			name = etree.SubElement(member, 'name')
			name.text = 'faultCode'
			value = etree.SubElement(member, 'value')
			value.text = '2'
			member = etree.SubElement(struct, 'member')
			name = etree.SubElement(member, 'name')
			name.text = 'faultString'
			value = etree.SubElement(member, 'value')
			value.text = 'Method not found'
			return etree.tostring(xml_response, pretty_print=True), 500, {'Content-Type': 'text/xml'}

	except Exception as e:
		xml_response = etree.Element('methodResponse')
		fault = etree.SubElement(xml_response, 'fault')
		value = etree.SubElement(fault, 'value')
		struct = etree.SubElement(value, 'struct')
		member = etree.SubElement(struct, 'member')
		name = etree.SubElement(member, 'name')
		name.text = 'faultCode'
		value = etree.SubElement(member, 'value')
		value.text = '500'
		member = etree.SubElement(struct, 'member')
		name = etree.SubElement(member, 'name')
		name.text = 'faultString'
		value = etree.SubElement(member, 'value')
		value.text = str(e)
		return etree.tostring(xml_response, pretty_print=True), 500, {'Content-Type': 'text/xml'}


# Define a catchall 404 route
@app.errorhandler(404)
def route_not_found(_):
	xml_response = etree.Element('methodResponse')
	fault = etree.SubElement(xml_response, 'fault')
	value = etree.SubElement(fault, 'value')
	struct = etree.SubElement(value, 'struct')
	member = etree.SubElement(struct, 'member')
	name = etree.SubElement(member, 'name')
	name.text = 'faultCode'
	value = etree.SubElement(member, 'value')
	value.text = '404'
	member = etree.SubElement(struct, 'member')
	name = etree.SubElement(member, 'name')
	name.text = 'faultString'
	value = etree.SubElement(member, 'value')
	value.text = 'URL Not Supported'
	return etree.tostring(xml_response, pretty_print=True), 404, {'Content-Type': 'text/xml'}


def run_main():
	app.run(port=8080)


if __name__ == "__main__":
	print("Starting the backend server on port 8080...")
	run_main()
