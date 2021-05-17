from app import app,db
from flask import render_template,request,url_for,redirect,Flask,session
from app.model.buku import Buku
from app.model.member import Member
from app.model.pinjam import Pinjam

def daftarPinjams():
    titles = "DAFTAR Peminjaman Buku"
    judul = "Daftar Peminjaman Buku"
    subjudul = "Daftar Peminjaman Buku | DIGITAL LIBRARY STMIK JAYAKARTA"
    buttontambah = "Tambah Data Peminjaman"
    if 'email' in session:
        listBuku = Buku.query.all() # SELECT data Buku
        listMember = Member.query.all() # SELECT data Member
        listPinjam = Pinjam.query.all() # SELECT data Pinjam
        return render_template('daftarpeminjaman-main.html',judul=judul, subjudul=subjudul,titles=titles,buttontambah=buttontambah,listPinjam=enumerate(listPinjam),listBuku=enumerate(listBuku), listMember=enumerate(listMember))
    else:
        return redirect(url_for("login"))

def tambahPinjam():
    titles = "Peminjaman Buku - Tambah Buku"
    judul = "Tambah List Peminjaman"
    subjudul = "Tambah Pinjam | DIGITAL LIBRARY STMIK JAYAKARTA"
    if request.method == 'POST':
        idbuku = request.form['idbuku']
        idmember = request.form['idmember']
        tanggalpinjam = request.form['tanggalpinjam']
        tanggalkembali = request.form['tanggalkembali']
        try:
            dataPinjam=Pinjam(idbuku=idbuku,idmember=idmember,tanggalpinjam=tanggalpinjam,tanggalkembali=tanggalkembali)
            db.session.add(dataPinjam) # INSERT data Pinjam
            db.session.commit()
        except Exception as e:
            print(e)
        return redirect(url_for('daftarPinjam'))
    if 'email' in session:
        listBukus = Buku.query.all() 
        listMembers = Member.query.all()
        return render_template('daftarpeminjaman-tambah.html',judul=judul, subjudul=subjudul,titles=titles, listBukus=listBukus, listMembers=listMembers)
    else:
        return redirect(url_for("login"))