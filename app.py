from flask import Flask, render_template, flash, redirect, url_for, request
from pymongo import MongoClient
from flask_pymongo import PyMongo
from decouple import config

app = Flask(__name__)
app.secret_key = "caircocoders-ednalan-2020"
app.config['MONGO_URI'] = config('MONGO_URI') 
mongo = PyMongo(app)
dbenter = mongo.db.registration

@app.route('/')
def index():
    return render_template('upload.html')
 
@app.route('/upload', methods=['POST'])
def upload():
    info={
        "username"  : request.form['txtusername'],
        "inputEmail": request.form['inputEmail'],
        "comment"   : request.form['txtcomment']
         }
    print(info)
    dbenter.insert_one(info)
    flash('Successfully uploaded ' ' to the database!')
    return redirect('/')



if __name__ == '__main__':
    app.run(port=5500,debug=True)

      