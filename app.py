from flask import Flask,request,render_template,redirect
from flaskext.mysql import MySQL
import mysql.connector
app=Flask(__name__)

cnx = mysql.connector.connect(user='root', database='test')
cursor = cnx.cursor()

def getdate():
    import datetime
    return datetime.datetime.now()

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/dashboard',methods=['POST'])
def Authentication():
    username=request.form['name']
    password=request.form['password']
    cursor = cnx.cursor()

    select_stmt = "SELECT * FROM user WHERE username = %(emp_no)s and password=%(pass)s"
    cursor.execute(select_stmt, {'emp_no': username,'pass':password})
    data=cursor.fetchone()
    if data is None:
        return render_template('error.html')
    else:
        return render_template('dashboard.html')



@app.route('/registered',methods=['POST'])
def Insertion():
    username=request.form['name']
    email=request.form['email']
    password=request.form['password']
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO user (username,email,password) "
        "VALUES (%s, %s, %s)"
    )
    data =(username,email,password)
    cursor.execute(insert_stmt, data)
    cnx.commit()
    f = open("hello.txt", "a")
    f.write("[ " + str(getdate()) + " ] : " + username + " created a account with email:"+email+"\n")
    return render_template('registered.html')

@app.route("/logout",methods=['GET','POST'])
def logout():
    return redirect('/')

@app.route("/home")
def backed():
    return redirect('/')
@app.route("/error")
def error():
    return redirect('/')


app.run(debug=True)
