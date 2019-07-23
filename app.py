import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo   
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def hello():
    return render_template('recipes.html', recipes=mongo.db.recipes.find())
    
@app.route('/add_cuisine')
def add_cuisine():
    return render_template('addcuisine.html',
    cuisines=mongo.db.cuisines.find())

@app.route('/insert_cuisine', methods=['POST'])
def insert_cuisine():
    cuisines = mongo.db.cuisines
    cuisines.insert_one(request.form.to_dict())
    return redirect(url_for('add_cuisine'))

@app.route('/edit_cuisine')
def edit_cuisine():
    return render_template('editcuisine.html',
    cuisines=mongo.db.cuisines.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)