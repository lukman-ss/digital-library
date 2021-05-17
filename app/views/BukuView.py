from app import app,db
from flask import render_template,request,url_for,redirect,Flask,session, send_file
from app.model.buku import Buku
from werkzeug.utils import secure_filename
import os
import flask

ALLOWED_EXTENSION = set(['png', 'jpeg', 'jpg','pdf'])
app.config['UPLOAD_FOLDER'] = 'C:/Users/envy/Downloads/belajar flask/digital-library/digital-library/app/static/uploads'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION

def daftarBukus():
    titles = "DAFTAR BUKU"
    judul = "Daftar Buku"
    subjudul = "Daftar Buku | DIGITAL LIBRARY STMIK JAYAKARTA"
    buttontambah = "Tambah Data Buku"
    if 'email' in session:
        listBuku = Buku.query.all() # SELECT semua row BUKU
        return render_template('daftarbuku-main.html',judul=judul, subjudul=subjudul,titles=titles,buttontambah=buttontambah,listBuku=enumerate(listBuku))
    else:
        return redirect(url_for("login"))

# def downloads(pdf):
#     try:
#         filename = f"{pdf}.pdf"
#         return flask.send_from_directory(app.config['UPLOAD_FOLDER'], filename=filename)

def tambahBukus():
    titles = "DAFTAR BUKU - Tambah Buku"
    judul = "Tambah Buku"
    subjudul = "Tambah Buku | DIGITAL LIBRARY STMIK JAYAKARTA"
    if request.method == 'POST':
        judulbuku = request.form['judulbuku']
        pengarang = request.form['pengarang']
        penerbit = request.form['penerbit']
        tahunterbit = request.form['tahunterbit']
        kategori = request.form['kategori']
        pdf = request.files['pdf']
        if 'pdf' not in request.files:
            return render_template('daftarbuku-tambah.html')

        if pdf.filename == '':
            return render_template('daftarbuku-tambah.html')
        try:
            if pdf and allowed_file(pdf.filename):
                filename = secure_filename(pdf.filename)
                pdf.save(os.path.join(app.config['UPLOAD_FOLDER'] , filename))
            dataBuku=Buku(judulbuku=judulbuku,pengarang=pengarang,penerbit=penerbit,tahunterbit=tahunterbit,kategori=kategori, pdf=pdf)
            db.session.add(dataBuku) #INSERT Data buku
            db.session.commit()
        except Exception as e:
            print(e)
        return redirect(url_for('daftarBuku'))
    if 'email' in session:

        return render_template('daftarbuku-tambah.html',judul=judul, subjudul=subjudul,titles=titles)
    else:
        return redirect(url_for("login"))

def ubahDaftarBukus(id):
    titles = "UBAH DAFTAR Buku"
    judul = "Ubah Daftar Buku"
    subjudul = "Ubah Daftar Buku | DIGITAL LIBRARY STMIK JAYAKARTA"
    buttontambah = "Tambah Data Buku"
    if 'email' in session:
        if request.method == 'POST':
            id = request.form['id']
            judulbuku = request.form['judulbuku']
            pengarang = request.form['pengarang']
            penerbit = request.form['penerbit']
            tahunterbit = request.form['tahunterbit']
            kategori = request.form['kategori']
            try:
                ubahDataBuku = Buku.query.filter_by(id=id).first()
                ubahDataBuku.judulbuku = judulbuku
                ubahDataBuku.pengarang = pengarang
                ubahDataBuku.penerbit = penerbit
                ubahDataBuku.tahunterbit = tahunterbit
                ubahDataBuku.kategori = kategori
                db.session.commit() # Update Data Buku
            except Exception as e:
                print(e)
            return redirect(url_for('daftarBuku'))
        listBuku = Buku.query.filter_by(id=id).first()
        return render_template('daftarbuku-ubah.html',judul=judul, subjudul=subjudul,titles=titles,buttontambah=buttontambah,listBuku=listBuku)
    else:
        return redirect(url_for("login"))

def hapusBukus(id):
    if 'email' in session:
        try:
            dataBuku = Buku.query.filter_by(id=id).first()
            db.session.delete(dataBuku) #Hapus Data BUku
            db.session.commit()
        except Exception as e:
            print(e)
        return redirect(url_for('daftarBuku'))
        return render_template('daftarmember-main.html')
    else:
        return redirect(url_for("login"))