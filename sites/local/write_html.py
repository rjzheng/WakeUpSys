import os
import webbrowser
import time

class Write_html():
	def __init__(self, username, password):
		self.username = username
		self.password = password

		input_value = {
		'username': self.username,
		'password': self.password
		}

		action = 'http://localhost:8000/maps/'
		method = 'post'

		input_field = '<input type="hidden" name="{0}" value="{1}" />'

		html_contents = """
		<html>
		<body onload="document.traffic_form.submit()">
			<form name="traffic_form" action = "{0}" method="{1}">
				{2}
			</form>
		</body>
		</html>
		"""

		input_fields = ""

		for key, value in input_value.items():
			input_fields += input_field.format(key, value)

		with open('temp_html.html', "w") as file:
			file.write(html_contents.format(action, method, input_fields))
			file.close()
			webbrowser.open(os.path.abspath(file.name))
			time.sleep(1)
	    	os.remove(os.path.abspath(file.name))

