import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://root:zgadnij88w@myfirstcluster-gg70b.mongodb.net/task_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)


#@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    _tasks = mongo.db.tasks.find()
    task_list = [task for task in _tasks]
    return render_template("tasks.html", tasks = task_list)


@app.route('/add_task')
def add_task():
    _categories = mongo.db.categories.find()
    category_list = [category for category in _categories]
    return render_template('addtask.html', categories = category_list)

@app.route('insert_task', methods = ['POST'])
def insert_task():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)



