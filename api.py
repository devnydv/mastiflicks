import json
import requests
from dotenv import load_dotenv
import os
load_dotenv()
db = os.getenv("db")


response = requests.get(db)
data = response.json()

def filehandle():
    jdata = json.dumps(data, indent=4)
    return jdata