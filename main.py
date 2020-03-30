from flask import Flask, render_template,request, redirect, url_for, make_response

import sqlite3
import hashlib
import datetime
import uuid

#import models.User

app=Flask(__name__)#MODEL
#db.create_all()

@app.route("/", methods=["GET"])#CONTROLLER
def index():
    
 #SQLite3 DB-Connection

    conn = sqlite3.connect("user.db", check_same_thread=False)

    #SQLite3 DB-Cursor

    curs = conn.cursor()

    email = request.form.get("email")
    password = request.form.get("password")

     # Session_Token abfragen

    session_token = str(request.cookies.get("session_token"))

    #curs.execute("CREATE TABLE IF NOT EXISTS user(firstname, Id, lastname, city, password);")
    #curs.execute("INSERT INTO user(firstname, Id, lastname, city, password) VALUES ('Matt', '5', 'Schmidt', 'Cologne', 'PW2020');")
    #conn.commit()



    #curs.execute("SELECT * FROM user")

    #curs.execute("CREATE TABLE IF NOT EXISTS payments(PaymentId integer primary key autoincrement, firstname, lastname, city, adress);")
    #curs.execute("INSERT INTO payments(firstname, lastname, city, adress) VALUES ('Mat', 'Schmidt', 'Cologne', 'Auf der Domplatte');")
    #conn.commit()


    #curs.pretty_print("SELECT * FROM Payments;")

    #curs.execute("CREATE TABLE IF NOT EXISTS products_in_shop(prodductId, productname, in_stock, price);")
    #curs.execute("INSERT INTO products_in_shop(prodductId, productname, in_stock, price) VALUES ('1', 'Notizbuch', '4', '12');")
    #conn.commit()

    curs.execute("CREATE TABLE IF NOT EXISTS login(email, password);")
    curs.execute("""
            INSERT INTO login (email, password)
            VALUES (?, ?)
            """, 
            (email, password))
    conn.commit()
    print(email)
    print(password)

 #SQLite3 DB-Cursor schließen

    curs.close()

    #SQLite3 DB-Connection schließen

    conn.close()
    return render_template("index.html")#VIEW
    
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