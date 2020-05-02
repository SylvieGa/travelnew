import hashlib
import uuid

from flask import Flask, render_template, request, redirect, url_for, make_response
from models import User, db

app = Flask(__name__)
db.create_all()  # create new tables in database


@app.route("/")  # CONTROLLER
def index():
    session_token = request.cookies.get("session_token")

    if session_token:
        # get user from the database based on email address
        user = db.query(User).filter_by(session_token=session_token).first()

    else:
        user = None

    return render_template("index.html", user=user)


@app.route("/index", methods=["GET", "POST"])
def login():
     if request.method == "GET":

        return render_template("index.html")

    elif request.method == "POST":

        user_name = request.form.get("email")

        user_password = request.form.get("password")

    # save user into database
    db.add(user)
    db.commit()

    if hashed_password != user.password:
        return "Wrong Password. Try Again."
    elif hashed_password == user.password:
        session_token = str(uuid.uuid4())

        user.session_token = session_token
        db.add(user)
        db.commit()

        response = make_response(redirect(url_for('profile')))
        response.set_cookie("session_token", session_token, httponly=True, samesite='Strict')

       return response



if __name__ == '__main__':
    app.run(debug=True)
    
