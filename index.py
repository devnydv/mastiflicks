import json
import math
from flask import Flask, render_template, request
from api import filehandle


app = Flask(__name__)
data =json.loads( filehandle())
#print(data)
data = data["data"]
reverseddata = data
reverseddata.reverse()
postlen = len(reverseddata)

#@app.route("/")
#def index():
    #return render_template("index.html" ,dbdata= data)

@app.route("/")
def fil():
    page = request.args.get("page", 0 ,type=int)
    page = page +1
    start = 21*page - 21
    end = 21*page
    tota_page = postlen  / 21
    tota_page = math.ceil(tota_page)
    print(tota_page)
    cate = request.args.get("category")
    if cate == None:
        return render_template("index.html",dbdata = reverseddata[start: end], cate = cate, pages= tota_page)
    else:
        movies = [item for item in data if item["cat"] == cate]
        return render_template("index.html" , cate = cate, dbdata = movies )


@app.route("/read")
def read():
    id = request.args.get("id")
    #print(data)
    #id = int(id)
# send 9 items for the recomandation section of read route
    otherpost = []
    if int(id) > 9:
        newid = int(id) 
        lowid= newid -9
        for x in range(lowid, newid):
            otherpost.append([item for item in reverseddata if item["id"] == str(x)])
        
    else:
        otherpost = []

    # post contains a single post that is the main post
    post = [item for item in reverseddata if item["id"] == id]
    return render_template("read.html", ids = id, dbdata= post, alldata= otherpost)

@app.route("/newdb")
def newdb():
    return render_template("newdb.html")

if __name__ == "__main__":
    app.run(debug=True)
