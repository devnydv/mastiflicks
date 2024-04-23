import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
db = os.getenv("db")

response = requests.get(db)
data = response.json()
json_string = json.dumps(data, indent=4)
def filehandle():
    return json_string
