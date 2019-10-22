import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo   
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

# Home Page - Index
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html',
    cuisines=mongo.db.cuisines.find())
    
# Create Cuisine Page - Short Form
@app.route('/create_cuisine')
def create_cuisine():
    return render_template('create_cuisine.html',
    cuisines=mongo.db.cuisines.find())

# Inserts New Cuisine To Site & Redirects Back To Cuisine Homepage
@app.route('/insert_cuisine', methods=['POST'])
def insert_cuisine():
    cuisines = mongo.db.cuisines
    cuisines.insert_one(request.form.to_dict())
    return redirect(url_for('edit_cuisine_homepage'))

# Edit Cuisine Homepage - Shows Collection For User Choice
@app.route('/edit_cuisine_homepage')
def edit_cuisine_homepage():
    return render_template('edit_cuisine_homepage.html',
    cuisines=mongo.db.cuisines.find())

# Edit Cuisine Page, Cuisine Title Altered Here
@app.route('/edit_cuisine/<cuisine_id>')
def edit_cuisine(cuisine_id):
    return render_template('edit_cuisine.html',
    cuisines=mongo.db.cuisines.find_one({'_id': ObjectId(cuisine_id)}))
    
# Confirms Cuisine Change & Redirects Back To Cuisine Homepage
@app.route('/update_cuisine/<cuisine_id>', methods=['POST'])
def update_cuisine(cuisine_id):
    mongo.db.cuisines.update(
        {'_id': ObjectId(cuisine_id)},
        {'cuisine_name': request.form.get('cuisine_name')})
    return redirect(url_for('edit_cuisine_homepage'))

# Confirms Cuisine Deletion & Redirects Back To Cuisine Homepage
@app.route('/delete_cuisine/<cuisine_id>')
def delete_cuisine(cuisine_id):
    mongo.db.cuisines.remove({'_id': ObjectId(cuisine_id)}),
    return redirect(url_for('edit_cuisine_homepage'))

# Displays Correct Recipe In Relation To Cuisine Chosen
@app.route('/recipe_display/<cuisine_id>')
def recipe_display(cuisine_id):
    return render_template('recipe_display.html',
    recipes=mongo.db.recipes.find(),
    difficulties=mongo.db.difficulties.find(),
    serves=mongo.db.serves.find(),
    cuisines=mongo.db.cuisines.find_one({'_id': ObjectId(cuisine_id)}))

# Displays Cuisines So Users Can Narrow Recipe Search Efficiently
@app.route('/get_recipes_step_one')
def get_recipes_step_one():
    return render_template('get_recipes_step_one.html',
    cuisines=mongo.db.cuisines.find())

# Displays Recipes With Edit & Delete Buttons For User
@app.route('/get_recipes_step_two/<cuisine_id>')
def get_recipes_step_two(cuisine_id):
    return render_template('get_recipes_step_two.html',
    recipes=mongo.db.recipes.find(),
    cuisines=mongo.db.cuisines.find_one({'_id': ObjectId(cuisine_id)}))
    
# Confirms Cuisine Deletion & Redirects Back To Recipe Step One
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)}),
    return redirect(url_for('get_recipes_step_one'))

#SPACE FOR RECIPE EDIT 

# Allows User To Fill Form Creating New Recipe
@app.route('/create_recipe')
def create_recipe():
    return render_template('create_recipe.html',
    recipes=mongo.db.recipes.find(),
    cuisines=mongo.db.cuisines.find(),
    difficulties=mongo.db.difficulties.find(),
    serves=mongo.db.serves.find()) 

# This Allows The Form To Update Theh Database
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('create_recipe'))

# This Offers A User A Form With Dynamically Loaded Content To Edit
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cuisine = mongo.db.cuisines.find()
    difficulties = mongo.db.difficulties.find()
    serves = mongo.db.serves.find()
    return render_template('edit_recipe.html', recipe=recipes,
    cuisines=cuisine, difficulties=difficulties, serves=serves)
    
# Confirms Recipe Change & Redirects Back To Get Recipe Step Two
@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    print(request.form.get('dish_difficulty'))    
    recipes.update({'_id': ObjectId(recipe_id)},
        {
            'cuisine_name':request.form.get('cuisine_name'),
            'dish_name':request.form.get('dish_name'),
            'dish_difficulty':request.form.get('dish_difficulty'),
            'serves':request.form.get('serves'),
            'ingredient_1':request.form.get('ingredient_1'),
            'ingredient_2':request.form.get('ingredient_2'),
            'ingredient_3':request.form.get('ingredient_3'),
            'ingredient_4':request.form.get('ingredient_4'),
            'ingredient_5':request.form.get('ingredient_5'),
            'ingredient_6':request.form.get('ingredient_6'),
            'ingredient_7':request.form.get('ingredient_7'),
            'ingredient_8':request.form.get('ingredient_8'),
            'ingredient_9':request.form.get('ingredient_9'),
            'step_1':request.form.get('step_1'),
            'step_2':request.form.get('step_2'),
            'step_3':request.form.get('step_3'),
            'step_4':request.form.get('step_4'), 
            'step_5':request.form.get('step_5')

        })
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)