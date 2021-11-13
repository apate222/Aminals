# FLASK Tutorial 1 -- We show the bare bones code to get an app up and running

# imports
import os                 # os is used to get environment variables IP & PORT
from flask import Flask   # Flask is the web app that we will customize
from flask import render_template
from flask import request
from flask import redirect, url_for
from database import db
from models import Question as Question
from models import User as User

app = Flask(__name__)     # create an app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_note_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
#  Bind SQLAlchemy db object to this Flask app
db.init_app(app)
with app.app_context():
    db.create_all()

# @app.route is a decorator. It gives the function "index" special powers.
# In this case it makes it so anyone going to "your-url/" makes this function
# get called. What it returns is what is shown as the web page

@app.route('/')
@app.route('/index')
def index():
    a_user = db.session.query(User).filter_by(email='test@uncc.edu')

    return render_template('index.html', user = a_user)

@app.route('/questions')
def get_questions():
    a_user = db.session.query(User).filter_by(email='test@uncc.edu')
    my_questions = db.session.query(Question).all()

    return render_template('question.html', question=my_questions, user=a_user)

@app.route('/question/<q_id>')
def get_question(q_id):
    a_user = db.session.query(User).filter_by(email='test@uncc.edu')
    my_question = db.session.query(Question).filter_by(id=q_id).one()

    return render_template('question.html', question=my_question, user=a_user)

@app.route('/questions/new', methods=['GET', 'POST'])
def new_question():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['noteText']

        from datetime import date
        today = date.today()

        today = today.strftime("%m-%d-%Y")
        new_record = Question(title, text, today)
        db.session.add(new_record)
        db.session.commit()
        return redirect(url_for('get_questions'))
    else:
        a_user = db.session.query(User).filter_by(email='test@uncc.edu')
        return render_template('new.html', user = a_user)




app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)

# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000

# Note that we are running with "debug=True", so if you make changes and save it
# the server will automatically update. This is great for development but is a
# security risk for production.