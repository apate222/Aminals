# FLASK Tutorial 1 -- We show the bare bones code to get an app up and running

# imports
import os                 # os is used to get environment variables IP & PORT
from flask import Flask   # Flask is the web app that we will customize
from flask import render_template
from flask import request
from flask import redirect, url_for
#from database import db
#from models import Note as Note
#from models import User as User

app = Flask(__name__)     # create an app

a_user = {'name': 'Casey', 'email':'cwill399@uncc.edu'}
questions = {1: {'title': 'First Note', 'text': 'This is my first note', 'date': '10-1-2020'},
             2: {'title': 'Second Note', 'text': 'This is my second note', 'date': '10-2-2020'},
             3: {'title': 'Third Note', 'text': 'This is my third note', 'date': '10-3-2020'}
             }

# @app.route is a decorator. It gives the function "index" special powers.
# In this case it makes it so anyone going to "your-url/" makes this function
# get called. What it returns is what is shown as the web page

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', user = a_user)

@app.route('/questions')
def get_questions():
    return render_template('questions.html', questions=questions, user=a_user)

@app.route('/question/<q_id>')
def get_question(q_id):
    return render_template('question.html', question=questions[int(q_id)], user=a_user)

@app.route('/questions/new', methods=['GET', 'POST'])
def new_question():
    return render_template('new.html')




app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)

# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000

# Note that we are running with "debug=True", so if you make changes and save it
# the server will automatically update. This is great for development but is a
# security risk for production.