from flask import render_template,request,url_for,redirect,Flask,session
from app.model.admin import Admin
from sqlalchemy.sql import *
from sqlalchemy import funcfilter



def logins():
    if 'email' in session: # session saat login by email
            return redirect(url_for('dashboard'))
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        emailstring = Admin.query.filter_by(username=email).first()
        passwordstring = Admin.query.filter_by(password=password).first()
        msg = 'email atau password salah'
        try:
            if email == emailstring.username and password == passwordstring.password:
                session['email']=email
                return redirect(url_for('dashboard'))
            # else:
            #     return render_template('login.html', msg)
            # elif emailstring.username != email:
            # elif email != emailstring.username and password != passwordstring.password:
                # return 'username atau password salah'
            # else:
            #     return redirect(url_for('login'))
        except:
            return render_template('login.html',msg=msg)
    return render_template('login.html')

def logouts():
    session.pop('email') #session logout
    return redirect(url_for('login'))

