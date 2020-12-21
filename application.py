from flask import Flask, redirect, render_template, request, session
# from flask_session import Session

app = Flask(__name__)
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

@app.route('/')
def index():
    # if "todos" not in session:
    #     session["todos"] = []
    return render_template('index.html')