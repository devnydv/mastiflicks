from bson import json_util
import math
import datetime
from mastiflics.db import catedata, catsize, readone, oneid, update, submit
from flask import render_template, request , send_from_directory
from mastiflics import app
from datetime import datetime


@app.route("/", methods = ["GET", "POST"])
def formongo():
    if request.method == "GET":
        start = 0
        end = 12 #not riquired
        
        data = catedata(start, "all")
        cate = request.args.get("category")
        
        
        if cate == None:
            tota_page = catsize("all")
        
            return render_template("index.html", dbdata = data, cate = cate, pages= tota_page)
           
        else:
            tota_page = catsize(cate)
            data = catedata(start, cate )
            return render_template("index.html" , cate = cate, dbdata = data )
        
    elif request.method == "POST":
        cate = request.args.get("category")
        page = request.args.get("page", 0 ,type=int)
        page = page +1
        start = 12*page - 12
        end = 12*page
        
         
        tota_page =  catsize(cate)
        print(cate)
        tota_page = tota_page / 12
        tota_page = math.ceil(tota_page)
        if tota_page >= page:
            
            data = catedata(start, cate )
            return render_template('rhtml.html', dbdata = data, cate= cate)
        else:
            return "No More news"

@app.route("/read")
def read():
    id = request.args.get("id")

    # send 9 items for the recomandation section of read route
    otherpost = []
    if int(id) > 11:
        newid = int(id) 
        data = catedata(0, "all")
        filtered_items = [item for item in data if item['id'] != id]
        otherpost.append(filtered_items)
        
    else:
        otherpost = []

    post =readone(id)
    return render_template("read.html", ids = id, dbdata= post, alldata= otherpost)

@app.route("/newdb", methods = ["GET", "POST"])
def newdb():
    if request.method == "GET":
        lastid = oneid()
        for x in lastid:
            idlast = int(x["id"]) +1
        
        timer = datetime.now()
        timedata = f'{timer.strftime("%A")}, {timer.day} {timer.strftime("%b")}, {timer.strftime("%Y")}'
        return render_template("db.html", tm = timedata, lid= idlast)
    
    elif request.method == "POST":
        reqst = request.args.get("reqst")

        if reqst == "fetch":
            print("fetch")
            id = request.args.get("id") 
            
            post = readone(id)
            post = json_util.dumps(post)
            return post
        
        if reqst== "update":
            data = request.get_json()  # Get JSON data from the request
            id = data['data']['id']
            
            update(data["data"], id)
            

        if reqst == "create":
            data = request.get_json()
            submit(data["data"])
            
        return render_template("db.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.root_path, 'robots.txt')




# Custom Jinja filter to format the date
@app.template_filter('format_date')
def format_date(value):
    try:
        # Convert the string to a datetime object
        date_obj = datetime.strptime(value, '%A, %d %b, %Y')
        # Format it to 'YYYY-MM-DD'
        return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        return value