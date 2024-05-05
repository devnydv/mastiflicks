import json
from flask import Flask, render_template, request
from api import filehandle
import requests

app = Flask(__name__)
data =json.loads( filehandle())
#print(data)
data = data["data"]
reverseddata = data
reverseddata.reverse()
#@app.route("/")
#def index():
    #return render_template("index.html" ,dbdata= data)

@app.route("/")
def fil():
    
    cate = request.args.get("category")
    if cate == None:       
        return render_template("index.html" ,dbdata = reverseddata, cate = cate)
    else:
        
        movies = [item for item in data if item["cat"] == cate]
        return render_template("index.html" , cate = cate, dbdata = movies )


@app.route("/read")
def read():
    id = request.args.get("id")
    #print(data)
    #id = int(id)
    post = [item for item in reverseddata if item["id"] == id]
    return render_template("read.html", ids = id, dbdata= post)
@app.route("/newdb")
def newdb():
    return render_template("newdb.html")
    
#if __name__ == "__main__":
   #app.run(debug=True)
