from flask import Flask,render_template, jsonify, request, url_for
import random
import json
import pymongo
from pymongo import MongoClient
# import json
from bson import json_util
from flask import Markup
value = Markup('First line.<br>Second line.<br>')
cluster = MongoClient('mongodb+srv://praveena:praveena@cluster0.vhted.mongodb.net/registration?retryWrites=true&w=majority')

db = cluster["praveena"]
col = db["registration"]

app  = Flask(__name__)
PORT = 3000

@app.route("/", methods=["GET","POST"])
def startpy():

    return render_template("index.html") 



@app.route("/submit", methods=["GET","POST"])
def submit():
    name = request.form.get("feature")
    line  = request.form.get("line")

    col.insert_one({ "Name": name , "line": line })
    for x in col.find():
        
       

        val=x['Name']
        val2=x['line'] 
    result = {
        'Name' : val ,
        'line' : val2
    }  
    # {{ org.backgroundInfo | replace(‘\n’, ‘<br>’) }} 

    # return json.dumps(result) 
    return render_template('result.html', result = result)
    

@app.route("/file", methods=["GET"])
def file():
    response=[]
    for main in col.find():
        value = main['Name']
        value2 = main['line']
        
        main = {
             'Name' : value ,
             'line' : value2
        }  
        response.append(main)
        print(response)

        
    # return json.dumps(response) 
    return render_template('main.html', main = response)

@app.route("/find/<username>", methods=["GET"])
def find(username):
    db = cluster["praveena"]
    col = db["registration"]
   
    mydata=[]
    myquery = { "Name": username }

    for mydoc in col.find(myquery):
        mydata.append(mydoc)


    print(mydata)
    return render_template('find.html', data=mydata)

    # name =  mydoc['name']
    # desc,

    # for x in mydoc:
    #   print(x)


    # data={
    #     'name' : mydoc['name'],
    #     'description' : mydoc['description']
    # }

    
  




    


if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port = PORT)
