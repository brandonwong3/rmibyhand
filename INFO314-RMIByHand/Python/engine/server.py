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
		pass
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
