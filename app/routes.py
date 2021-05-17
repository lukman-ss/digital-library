from app import app,db
from flask import render_template,request,url_for,redirect,Flask,session
from app.model.buku import Buku
from app.model.member import Member
from app.model.pinjam import Pinjam
from app.model.admin import Admin
from werkzeug.utils import secure_filename
import os
from os.path import join, dirname, realpath
from app.views import LoginView, DashboardView,BukuView, MemberView, PinjamView, AdminView

#----------------------------------Login, Logout dan Dashboard----------------------------------

@app.route('/', methods=['GET','POST'])
def login():
    return LoginView.logins() #methods logins dari LoginView

@app.route('/logout')
def logout():
    return LoginView.logouts() #methods logout dari LoginView


@app.route('/dashbords')
def dashboard():
    titles = "DASHBOARD"
    judul = "Dashboard"
    if 'email' in session:
        # Menghitung jumlah id member dalam tabel member
        jumlahMember = Member.query.filter(Member.id).count() 
        # Menghitung jumlah id Buku dalam tabel buku
        jumlahBuku = Buku.query.filter(Buku.id).count()
        # Menghitung jumlah id Pinjam dalam tabel Pinjam
        jumlahPinjam = Pinjam.query.filter(Pinjam.id).count()
        # Menghitung jumlah id Admin dalam tabel Admin
        jumlahAdmin = Admin.query.filter(Admin.id).count()
        return render_template('dashboards.html',judul=judul,titles=titles,jumlahBuku=jumlahBuku,jumlahMember=jumlahMember,jumlahPinjam=jumlahPinjam,jumlahAdmin=jumlahAdmin)
    else:
        return redirect(url_for("login"))

#----------------------------------BUKU----------------------------------

# @app.route('/downloads/<pdf>')
# def download(pdf):
#    return BukuView.downloads(pdf)

@app.route('/daftarbuku')
def daftarBuku():
    return BukuView.daftarBukus() #Method daftarBukus dalam view BukuView

@app.route('/daftarbuku/tambahbuku', methods=['POST', 'GET'])
def tambahBuku():
    return BukuView.tambahBukus() #Method tambahBukus dalam view BukuView

@app.route('/daftarbuku/ubahbuku/<int:id>',methods=['POST','GET'])
def ubahDaftarBuku(id):
    return BukuView.ubahDaftarBukus(id) #Method ubahDaftarBukus dalam view BukuView

@app.route('/daftarbuku/hapusbuku/<int:id>',methods=['POST','GET'])
def hapusBuku(id):
    return BukuView.hapusBukus(id) #Method hapusBukus dalam view BukuView

#----------------------------------MEMBER----------------------------------

@app.route('/daftarmember')
def daftarMember():
    return MemberView.daftarMembers() #Method daftarMembers dalam view MemberView

@app.route('/daftarmember/tambahmember',methods=['POST','GET'])
def tambahMember():
    return MemberView.tambahMembers() #Method tambahMembers dalam view MemberView

@app.route('/daftarbuku/ubahmember/<int:id>',methods=['POST','GET'])
def ubahDaftarMember(id):
    return MemberView.ubahDaftarMembers(id) #Method ubahDaftarMembers dalam view MemberView

@app.route('/daftarbuku/hapusmember/<int:id>',methods=['POST','GET'])
def hapusMember(id):
    return MemberView.hapusMembers(id) #Method hapusMembers dalam view MemberView

#----------------------------------Pinjam----------------------------------

@app.route('/daftarpinjam')
def daftarPinjam():
    return PinjamView.daftarPinjams() #Method daftarPinjams dalam view PinjamView

@app.route('/daftarpinjam/tambahpinjam', methods=['POST', 'GET'])
def tambahPinjam():
    return PinjamView.tambahPinjam() #Method tambahPinjam dalam view PinjamView

#----------------------------------ADMIN----------------------------------

@app.route('/daftaradmin')
def daftarAdmin():
    return AdminView.daftarAdmins() #Method daftarAdmins dalam view AdminView

@app.route('/daftaradmin/tambahadmin', methods=['POST', 'GET'])
def tambahAdmin():
    return AdminView.tambahAdmins() #Method tambahAdmins dalam view AdminView

@app.route('/daftaradmin/ubahadmin/<int:id>', methods=['POST','GET'])
def ubahAdmin(id):
    return AdminView.ubahAdmins(id) #Method ubahAdmin dalam view AdminView

@app.route('/daftaradmin/hapusadmin/<int:id>')
def hapusAdmin(id):
    return AdminView.hapusAdmins(id) #Method hapusAdmin dalam view AdminView