import sys
import requests
import time
from lxml import etree


headers = {
	'Content-Type': 'text/xml',
}


if __name__ == "__main__":
	try:
		args = sys.argv
		if len(args) != 3:
			print("Usage: python client.py <connection_type> <hostname> <port>")
			sys.exit(1)
		hostname = args[1]
		port = int(args[2])
		print("Running client...")

		# Testing

		# subtract(12, 6) = 6
		xml_request_payload = etree.Element('methodCall')
		method_name = etree.SubElement(xml_request_payload, 'methodName')
		method_name.text = 'subtract'
		params = etree.SubElement(xml_request_payload, 'params')
		param1 = etree.SubElement(params, 'param')
		value1 = etree.SubElement(param1, 'value')
		int1 = etree.SubElement(value1, 'i4')
		int1.text = '12'
		param2 = etree.SubElement(params, 'param')
		value2 = etree.SubElement(param2, 'value')
		int2 = etree.SubElement(value2, 'i4')
		int2.text = '6'
		xml_request_payload = etree.tostring(xml_request_payload, pretty_print=True)
		print(xml_request_payload)
		response = requests.post(f'http://{hostname}:{port}', data=xml_request_payload, headers=headers)
		print(response.text)
		# Now parse the XML response and check if the result is correct
		xml_response_payload = etree.fromstring(response.text)
		result = xml_response_payload.xpath('//methodResponse/params/param/value/i4/text()')[0]
		print(f"Result: {result}")
		assert result == '6'

		time.sleep(2)

		# multiply(3, 4) = 12
		xml_request_payload = etree.Element('methodCall')
		method_name = etree.SubElement(xml_request_payload, 'methodName')
		method_name.text = 'multiply'
		params = etree.SubElement(xml_request_payload, 'params')
		param1 = etree.SubElement(params, 'param')
		value1 = etree.SubElement(param1, 'value')
		int1 = etree.SubElement(value1, 'i4')
		int1.text = '3'
		param2 = etree.SubElement(params, 'param')
		value2 = etree.SubElement(param2, 'value')
		int2 = etree.SubElement(value2, 'i4')
		int2.text = '4'
		xml_request_payload = etree.tostring(xml_request_payload, pretty_print=True)
		print(xml_request_payload)
		response = requests.post(f'http://{hostname}:{port}', data=xml_request_payload, headers=headers)
		print(response.text)
		# Now parse the XML response and check if the result is correct
		xml_response_payload = etree.fromstring(response.text)
		result = xml_response_payload.xpath('//methodResponse/params/param/value/i4/text()')[0]
		print(f"Result: {result}")
		assert result == '12'

		time.sleep(2)

		# divide(10, 5) = 2
		xml_request_payload = etree.Element('methodCall')
		method_name = etree.SubElement(xml_request_payload, 'methodName')
		method_name.text = 'divide'
		params = etree.SubElement(xml_request_payload, 'params')
		param1 = etree.SubElement(params, 'param')
		value1 = etree.SubElement(param1, 'value')
		int1 = etree.SubElement(value1, 'i4')
		int1.text = '10'
		param2 = etree.SubElement(params, 'param')
		value2 = etree.SubElement(param2, 'value')
		int2 = etree.SubElement(value2, 'i4')
		int2.text = '5'
		xml_request_payload = etree.tostring(xml_request_payload, pretty_print=True)
		print(xml_request_payload)
		response = requests.post(f'http://{hostname}:{port}', data=xml_request_payload, headers=headers)
		print(response.text)
		# Now parse the XML response and check if the result is correct
		xml_response_payload = etree.fromstring(response.text)
		result = xml_response_payload.xpath('//methodResponse/params/param/value/i4/text()')[0]
		print(f"Result: {result}")
		assert result == '2'

		time.sleep(2)

		# modulo(10, 5) = 0
		xml_request_payload = etree.Element('methodCall')
		method_name = etree.SubElement(xml_request_payload, 'methodName')
		method_name.text = 'modulo'
		params = etree.SubElement(xml_request_payload, 'params')
		param1 = etree.SubElement(params, 'param')
		value1 = etree.SubElement(param1, 'value')
		int1 = etree.SubElement(value1, 'i4')
		int1.text = '10'
		param2 = etree.SubElement(params, 'param')
		value2 = etree.SubElement(param2, 'value')
		int2 = etree.SubElement(value2, 'i4')
		int2.text = '5'
		xml_request_payload = etree.tostring(xml_request_payload, pretty_print=True)
		print(xml_request_payload)
		response = requests.post(f'http://{hostname}:{port}', data=xml_request_payload, headers=headers)
		print(response.text)
		# Now parse the XML response and check if the result is correct
		xml_response_payload = etree.fromstring(response.text)
		result = xml_response_payload.xpath('//methodResponse/params/param/value/i4/text()')[0]
		print(f"Result: {result}")
		assert result == '0'

		time.sleep(2)

		# add(0) = 0
		xml_request_payload = etree.Element('methodCall')
		method_name = etree.SubElement(xml_request_payload, 'methodName')
		method_name.text = 'add'
		params = etree.SubElement(xml_request_payload, 'params')
		param1 = etree.SubElement(params, 'param')
		value1 = etree.SubElement(param1, 'value')
		int1 = etree.SubElement(value1, 'i4')
		int1.text = '0'
		xml_request_payload = etree.tostring(xml_request_payload, pretty_print=True)
		print(xml_request_payload)
		response = requests.post(f'http://{hostname}:{port}', data=xml_request_payload, headers=headers)
		print(response.text)
		# Now parse the XML response and check if the result is correct
		xml_response_payload = etree.fromstring(response.text)
		result = xml_response_payload.xpath('//methodResponse/params/param/value/i4/text()')[0]
		print(f"Result: {result}")
		assert result == '0'

		time.sleep(2)

		# add(1, 2, 3, 4, 5) = 15
		xml_request_payload = etree.Element('methodCall')
		method_name = etree.SubElement(xml_request_payload, 'methodName')
		method_name.text = 'add'
		params = etree.SubElement(xml_request_payload, 'params')
		param1 = etree.SubElement(params, 'param')
		value1 = etree.SubElement(param1, 'value')
		int1 = etree.SubElement(value1, 'i4')
		int1.text = '1'
		param2 = etree.SubElement(params, 'param')
		value2 = etree.SubElement(param2, 'value')
		int2 = etree.SubElement(value2, 'i4')
		int2.text = '2'
		param3 = etree.SubElement(params, 'param')
		value3 = etree.SubElement(param3, 'value')
		int3 = etree.SubElement(value3, 'i4')
		int3.text = '3'
		param4 = etree.SubElement(params, 'param')
		value4 = etree.SubElement(param4, 'value')
		int4 = etree.SubElement(value4, 'i4')
		int4.text = '4'
		param5 = etree.SubElement(params, 'param')
		value5 = etree.SubElement(param5, 'value')
		int5 = etree.SubElement(value5, 'i4')
		int5.text = '5'
		xml_request_payload = etree.tostring(xml_request_payload, pretty_print=True)
		print(xml_request_payload)
		response = requests.post(f'http://{hostname}:{port}', data=xml_request_payload, headers=headers)
		print(response.text)
		# Now parse the XML response and check if the result is correct
		xml_response_payload = etree.fromstring(response.text)
		result = xml_response_payload.xpath('//methodResponse/params/param/value/i4/text()')[0]
		print(f"Result: {result}")
		assert result == '15'

		time.sleep(2)

		# multiply(1, 2, 3, 4, 5) = 120
		xml_request_payload = etree.Element('methodCall')
		method_name = etree.SubElement(xml_request_payload, 'methodName')
		method_name.text = 'multiply'
		params = etree.SubElement(xml_request_payload, 'params')
		param1 = etree.SubElement(params, 'param')
		value1 = etree.SubElement(param1, 'value')
		int1 = etree.SubElement(value1, 'i4')
		int1.text = '1'
		param2 = etree.SubElement(params, 'param')
		value2 = etree.SubElement(param2, 'value')
		int2 = etree.SubElement(value2, 'i4')
		int2.text = '2'
		param3 = etree.SubElement(params, 'param')
		value3 = etree.SubElement(param3, 'value')
		int3 = etree.SubElement(value3, 'i4')
		int3.text = '3'
		param4 = etree.SubElement(params, 'param')
		value4 = etree.SubElement(param4, 'value')
		int4 = etree.SubElement(value4, 'i4')
		int4.text = '4'
		param5 = etree.SubElement(params, 'param')
		value5 = etree.SubElement(param5, 'value')
		int5 = etree.SubElement(value5, 'i4')
		int5.text = '5'
		xml_request_payload = etree.tostring(xml_request_payload, pretty_print=True)
		print(xml_request_payload)
		response = requests.post(f'http://{hostname}:{port}', data=xml_request_payload, headers=headers)
		print(response.text)
		# Now parse the XML response and check if the result is correct
		xml_response_payload = etree.fromstring(response.text)
		result = xml_response_payload.xpath('//methodResponse/params/param/value/i4/text()')[0]
		print(f"Result: {result}")
		assert result == '120'

		time.sleep(2)

		# Testing error handling

		# Add two very large numbers such that it triggers an overflow
		xml_request_payload = etree.Element('methodCall')
		method_name = etree.SubElement(xml_request_payload, 'methodName')
		method_name.text = 'add'
		params = etree.SubElement(xml_request_payload, 'params')
		param1 = etree.SubElement(params, 'param')
		value1 = etree.SubElement(param1, 'value')
		int1 = etree.SubElement(value1, 'i4')
		int1.text = str(sys.maxsize * 2)
		param2 = etree.SubElement(params, 'param')
		value2 = etree.SubElement(param2, 'value')
		int2 = etree.SubElement(value2, 'i4')
		int2.text = str(sys.maxsize * 2)
		xml_request_payload = etree.tostring(xml_request_payload, pretty_print=True)
		print(xml_request_payload)
		response = requests.post(f'http://{hostname}:{port}', data=xml_request_payload, headers=headers)
		print(response.text)
		# Now parse the XML response and check if the result is correct
		xml_response_payload = etree.fromstring(response.text)
		fault_code = xml_response_payload.xpath('//methodResponse/fault/value/struct/member/name/text()')[0]
		fault_string = xml_response_payload.xpath('//methodResponse/fault/value/struct/member/value/string/text()')[0]
		print(f"Fault code: {fault_code}")
		print(f"Fault string: {fault_string}")

		time.sleep(2)

		# Test that multiplying two very large numbers triggers an overflow
		xml_request_payload = etree.Element('methodCall')
		method_name = etree.SubElement(xml_request_payload, 'methodName')
		method_name.text = 'multiply'
		params = etree.SubElement(xml_request_payload, 'params')
		param1 = etree.SubElement(params, 'param')
		value1 = etree.SubElement(param1, 'value')
		int1 = etree.SubElement(value1, 'i4')
		int1.text = str(sys.maxsize * 2)
		param2 = etree.SubElement(params, 'param')
		value2 = etree.SubElement(param2, 'value')
		int2 = etree.SubElement(value2, 'i4')
		int2.text = str(sys.maxsize * 2)
		xml_request_payload = etree.tostring(xml_request_payload, pretty_print=True)
		print(xml_request_payload)
		response = requests.post(f'http://{hostname}:{port}', data=xml_request_payload, headers=headers)
		print(response.text)
		# Now parse the XML response and check if the result is correct
		xml_response_payload = etree.fromstring(response.text)
		fault_code = xml_response_payload.xpath('//methodResponse/fault/value/struct/member/name/text()')[0]
		fault_string = xml_response_payload.xpath('//methodResponse/fault/value/struct/member/value/string/text()')[0]
		print(f"Fault code: {fault_code}")
		print(f"Fault string: {fault_string}")

		time.sleep(2)

		# Test that subtraction taking two string parameters should trigger illegal argument fault
		xml_request_payload = etree.Element('methodCall')
		method_name = etree.SubElement(xml_request_payload, 'methodName')
		method_name.text = 'subtract'
		params = etree.SubElement(xml_request_payload, 'params')
		param1 = etree.SubElement(params, 'param')
		value1 = etree.SubElement(param1, 'value')
		string1 = etree.SubElement(value1, 'string')
		string1.text = '1'
		param2 = etree.SubElement(params, 'param')
		value2 = etree.SubElement(param2, 'value')
		string2 = etree.SubElement(value2, 'string')
		string2.text = '2'
		xml_request_payload = etree.tostring(xml_request_payload, pretty_print=True)
		print(xml_request_payload)
		response = requests.post(f'http://{hostname}:{port}', data=xml_request_payload, headers=headers)
		print(response.text)
		# Now parse the XML response and check if the result is correct
		xml_response_payload = etree.fromstring(response.text)
		fault_code = xml_response_payload.xpath('//methodResponse/fault/value/struct/member/name/text()')[0]
		fault_string = xml_response_payload.xpath('//methodResponse/fault/value/struct/member/value/string/text()')[0]
		print(f"Fault code: {fault_code}")
		print(f"Fault string: {fault_string}")

		time.sleep(2)

		# Test division by zero
		xml_request_payload = etree.Element('methodCall')
		method_name = etree.SubElement(xml_request_payload, 'methodName')
		method_name.text = 'divide'
		params = etree.SubElement(xml_request_payload, 'params')
		param1 = etree.SubElement(params, 'param')
		value1 = etree.SubElement(param1, 'value')
		int1 = etree.SubElement(value1, 'i4')
		int1.text = '1'
		param2 = etree.SubElement(params, 'param')
		value2 = etree.SubElement(param2, 'value')
		int2 = etree.SubElement(value2, 'i4')
		int2.text = '0'
		xml_request_payload = etree.tostring(xml_request_payload, pretty_print=True)
		print(xml_request_payload)
		response = requests.post(f'http://{hostname}:{port}', data=xml_request_payload, headers=headers)
		print(response.text)
		# Now parse the XML response and check if the result is correct
		xml_response_payload = etree.fromstring(response.text)
		fault_code = xml_response_payload.xpath('//methodResponse/fault/value/struct/member/name/text()')[0]
		fault_string = xml_response_payload.xpath('//methodResponse/fault/value/struct/member/value/string/text()')[0]
		print(f"Fault code: {fault_code}")
		print(f"Fault string: {fault_string}")
		


	except KeyboardInterrupt:
		print("Keyboard interrupt detected. Exiting...")
		sys.exit(0)
	except Exception as e:
		print(str(e))
		sys.exit(1)
