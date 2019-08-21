import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo   
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html',
    cuisines=mongo.db.cuisines.find())

@app.route('/get_recipes')
def get_recipes():
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

@app.route('/get_cuisines')
def get_cuisines():
    return render_template('cuisines.html',
    cuisines=mongo.db.cuisines.find())

@app.route('/edit_cuisine/<cuisine_id>')
def edit_cuisine(cuisine_id):
    return render_template('editcuisine.html',
    cuisines=mongo.db.cuisines.find_one({'_id': ObjectId(cuisine_id)}))
    
@app.route('/update_cuisine/<cuisine_id>', methods=['POST'])
def update_cuisine(cuisine_id):
    mongo.db.cuisines.update(
        {'_id': ObjectId(cuisine_id)},
        {'cuisine_name': request.form.get('cuisine_name')})
    return redirect(url_for('get_cuisines'))

@app.route('/delete_cuisine/<cuisine_id>')
def delete_cuisine(cuisine_id):
    mongo.db.cuisines.remove({'_id': ObjectId(cuisine_id)}),
    return redirect(url_for('get_cuisines'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)