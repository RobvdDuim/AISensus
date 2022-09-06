# Define the URL where Label Studio is accessible and the API key for your user account
LABEL_STUDIO_URL = 'http://localhost:8082'
API_KEY = 'c56ac339688280463139ee2cf4c94d6df1aeec5e'

# Import the SDK and the client module
from datetime import datetime
from label_studio_sdk import Client

# Connect to the Label Studio API and check the connection
ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
ls.check_connection()

from label_studio_sdk import users as User

Piet = User.User(id= 1, username= 'Piet_Project1', first_name = 'Piet', last_name = 'Pietersma', email= 'Piet_Project1@gmail.com',last_activity= datetime.today(), initials = 'P', phone='XX', client = ls, active_organization = 1)
Piet = User.User(id= 1, username= 'Piet_Project1', first_name = 'Piet', last_name = 'Pietersma', email= 'Piet_Project1@gmail.com',last_activity= datetime.today(), initials = 'P', phone='XX', client = ls, active_organization = 1)
