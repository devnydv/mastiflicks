import os
import time
import json
import requests
from dotenv import load_dotenv
import os 

load_dotenv()
db = os.getenv("db")
    

response = requests.get(db)
data = response.json()

def filehandle():
    file_path = "./fbdata.json"
    if os.path.exists(file_path):
        file_creation_time = os.path.getctime(file_path)
        current_time = time.time()
        if current_time - file_creation_time <= 6:  # 600 seconds = 10 minutes
            f = open("fbdata.json", "r")
            
            return f.read()
        else:
            os.remove("fbdata.json")
            #ref = db.reference('/lol/')
            
            json_string = json.dumps(data, indent=4)
            #print(data)
            f = open("fbdata.json", "w")
            f.write(json_string)
            f.close()
            
            f = open("fbdata.json", "r")
            return f.read()
    else:
        print("File does not exist")