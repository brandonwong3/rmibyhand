from lxml import etree      # Using lxml for XML parsing


class Calculator:
	def __init__(self):
		self.operation = None
		self.first_number = None
		self.second_number = None
		self.result = None

	@staticmethod
	def create_from_xml(input_xml):
		root = etree.Element('root')

	def calculate(self):
		pass

	def to_xml(self):
		# Convert the class data to XML to send to the server
		pass
