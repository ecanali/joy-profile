import os
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc


app = Flask(__name__)

UPLOAD_FOLDER = './static/gallery'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Create database models
class Gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200), nullable=False)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gallery', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        title = request.form['title']
        # Push to upload folder
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        # Push to database
        new_file = Gallery(title=title, image=os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        try:
            db.session.add(new_file)
            db.session.commit()
            return redirect('/gallery')
        except:
            return "There was an error adding the file..."
    else:
        files = Gallery.query.order_by(desc(Gallery.id)).all()
        return render_template('gallery.html', files=files)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        # Push to database
        new_email = Contact(email=email)
        try:
            db.session.add(new_email)
            db.session.commit()
            return redirect('/contact')
        except:
            return "There was an error adding the email..."
    else:
        return render_template('contact.html')