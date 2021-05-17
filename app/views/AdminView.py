from app import app,db
from flask import render_template,request,url_for,redirect,Flask,session
from werkzeug.utils import secure_filename
import os
from os.path import join, dirname, realpath
from app.model.admin import Admin

def daftarAdmins():
    titles = "DAFTAR ADMIN"
    judul = "Daftar Admin"
    subjudul = "Daftar Admin | DIGITAL LIBRARY STMIK JAYAKARTA"
    buttontambah = "Tambah Data Admin"
    if 'email' in session:
        listAdmin = Admin.query.all() # SELECT semua row admin
        return render_template('daftaradmin-main.html',judul=judul, subjudul=subjudul,titles=titles,buttontambah=buttontambah, listAdmin=enumerate(listAdmin))
    else:
        return redirect(url_for("login"))

def tambahAdmins():
    titles = "DAFTAR ADMIN - Tambah Admin"
    judul = "Tambah Admin"
    subjudul = "Tambah Admin | DIGITAL LIBRARY STMIK JAYAKARTA"

    if 'email' in session:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            nama = request.form['nama']
            file = request.files['file']
            if 'file' not in request.files:
                return render_template('daftaradmin-tambah.html')

            if file.filename == '':
                return render_template('daftaradmin-tambah.html')
            try:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'] , filename))
                dataAdmin=Admin(username=username,password=password,nama=nama,file=filename)
                db.session.add(dataAdmin) # INSERT row admin
                db.session.commit()
            except Exception as e:
                print(e)
            return redirect(url_for('daftarAdmin'))
        return render_template('daftaradmin-tambah.html',judul=judul, subjudul=subjudul,titles=titles)
    else:
        return redirect(url_for("login"))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION

ALLOWED_EXTENSION = set(['png', 'jpeg', 'jpg','pdf'])
app.config['UPLOAD_FOLDER'] = 'C:/Users/envy/Downloads/belajar flask/digital-library/digital-library/app/static/uploads'

def ubahAdmins(id):
    titles = "UBAH ADMIN"
    judul = "Ubah Data Admin"
    subjudul = "Ubah Data Admin | DIGITAL LIBRARY STMIK JAYAKARTA"
    buttontambah = "Tambah Data Member"
    if 'email' in session:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            nama = request.form['nama']
            file = request.files['file']
            if 'file' not in request.files:
                return render_template('daftaradmin-tambah.html')

            if file.filename == '':
                return render_template('daftaradmin-tambah.html')
            try:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'] , filename))
                ubahDataAdmin = Admin.query.filter_by(id=id).first()
                ubahDataAdmin.username = username
                ubahDataAdmin.password = password
                ubahDataAdmin.nama = nama
                ubahDataAdmin.file = filename
                db.session.commit() # Update by id row admin
            except Exception as e:
                print(e)
            return redirect(url_for('daftarAdmin'))
        listAdmin = Admin.query.filter_by(id=id).first()
        return render_template('daftaradmin-ubah.html',judul=judul, subjudul=subjudul,titles=titles,buttontambah=buttontambah,listAdmin=listAdmin)
    else:
        return redirect(url_for("login"))

def hapusAdmins(id):
    if 'email' in session:
        try:
            dataAdmin = Admin.query.filter_by(id=id).first()
            db.session.delete(dataAdmin) # DELETE by id
            db.session.commit()
        except Exception as e:
            print(e)
        return redirect(url_for('daftarAdmin'))
        return render_template('daftarmember-main.html')
    else:
        return redirect(url_for("login"))