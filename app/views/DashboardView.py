from app import app,db
from flask import render_template,request,url_for,redirect,Flask,session
from app.model.buku import Buku
from app.model.member import Member
from app.model.pinjam import Pinjam

def dashboards():
    titles = "DASHBOARD"
    judul = "Dashboard"
    if 'email' in session:
        jumlahMember = Member.query.filter(Member.id).count()
        jumlahBuku = Buku.query.filter(Buku.id).count()
        jumlahPinjam = Pinjam.query.filter(Pinjam.id).count()
        return render_template('dashboards.html',judul=judul,titles=titles,jumlahBuku=jumlahBuku,jumlahMember=jumlahMember,jumlahPinjam=jumlahPinjam)
    else:
        return redirect(url_for("login"))