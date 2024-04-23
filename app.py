import json 
from flask import Flask, render_template
from file import filehandle
app = Flask(__name__)

@app.route("/")
def hello_world():
    
    data =json.loads( filehandle())
    #print(data)
    data = data["lol"]["data"]
    
    return render_template("index.html", res =data, name= "lol" )


@app.route("/lol/<int:marks>")
def lol(marks):
    return render_template("lol.html",mark = marks)


if __name__ == "__main__":
    app.run(debug=True)
