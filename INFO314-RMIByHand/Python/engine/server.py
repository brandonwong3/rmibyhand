from flask import Flask, request
from lxml import etree


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

		if method_name == 'add':
			i4_method_parameters = xml_request.xpath('//params/param/value/i4')
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

		method_parameters = xml_request.xpath('//params/param/value')
		# Do the calculations

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
	pass
