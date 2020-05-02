from flask import Flask, render_template,request, redirect, url_for, make_response

import sqlite3
import hashlib
import datetime
import uuid

#import models.User

app=Flask(__name__)#MODEL
#db.create_all()
  
@app.route("/index", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        user_name = request.form.get("email")
        user_password = request.form.get("password")

        # create a User object
        #user = User(name=user_name, email=user_email)

        # save the user object into a database
        #db.add(user)
        #db.commit()

        print(user_name)
        print(user_password)

        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
