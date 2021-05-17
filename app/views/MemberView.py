from app import app,db
from flask import render_template,request,url_for,redirect,Flask,session
from app.model.member import Member

def daftarMembers():
    titles = "DAFTAR MEMBER"
    judul = "Daftar Member"
    subjudul = "Daftar Member | DIGITAL LIBRARY STMIK JAYAKARTA"
    buttontambah = "Tambah Data Member"
    if 'email' in session:
        listMember = Member.query.all() #Query Menampilkan Semua data di tabel Member
        return render_template('daftarmember-main.html',judul=judul, subjudul=subjudul,titles=titles,buttontambah=buttontambah,listMember=enumerate(listMember))
    else:
        return redirect(url_for("login"))

def tambahMembers():
    titles = "DAFTAR Member - Tambah Buku"
    judul = "Tambah Member"
    subjudul = "Tambah Member | DIGITAL LIBRARY STMIK JAYAKARTA"
    if request.method == 'POST':
        tipe = request.form['tipe']
        nama = request.form['nama']
        tempatlahir = request.form['tempatlahir']
        tanggallahir = request.form['tanggallahir']
        jeniskelamin = request.form['jeniskelamin']
        email = request.form['email']
        alamat = request.form['alamat']
        pekerjaan = request.form['pekerjaan']
        try:
            dataMember = Member(tipe=tipe,nama=nama,tempatlahir=tempatlahir,tanggallahir=tanggallahir,jeniskelamin=jeniskelamin,email=email,alamat=alamat,pekerjaan=pekerjaan)
            db.session.add(dataMember) # Insert data member
            db.session.commit()
        except Exception as e:
            print(e)
        return redirect(url_for('daftarMember'))
    if 'email' in session:
        return render_template('daftarmember-tambah.html',judul=judul, subjudul=subjudul,titles=titles)
    else:
        return redirect(url_for("login"))

def ubahDaftarMembers(id):
    titles = "UBAH DAFTAR Member"
    judul = "Ubah Daftar Member"
    subjudul = "Ubah Daftar Member | DIGITAL LIBRARY STMIK JAYAKARTA"
    buttontambah = "Tambah Data Member"
    if 'email' in session:
        if request.method == 'POST':
            tipe = request.form['tipe']
            nama = request.form['nama']
            tempatlahir = request.form['tempatlahir']
            tanggallahir = request.form['tanggallahir']
            jeniskelamin = request.form['jeniskelamin']
            email = request.form['email']
            alamat = request.form['alamat']
            pekerjaan = request.form['pekerjaan']
            try:
                ubahDataMember = Member.query.filter_by(id=id).first()
                ubahDataMember.tipe = tipe
                ubahDataMember.nama = nama
                ubahDataMember.tempatlahir = tempatlahir
                ubahDataMember.tanggallahir = tanggallahir
                ubahDataMember.jeniskelamin = jeniskelamin
                ubahDataMember.email = email
                ubahDataMember.alamat = alamat
                ubahDataMember.pekerjaan = pekerjaan
                db.session.commit() # Update Data Member
            except Exception as e:
                print(e)
            return redirect(url_for('daftarMember'))
        listMember = Member.query.filter_by(id=id).first()
        return render_template('daftarmember-ubah.html',judul=judul, subjudul=subjudul,titles=titles,buttontambah=buttontambah,listMember=listMember)
    else:
        return redirect(url_for("login"))

def hapusMembers(id):
    if 'email' in session:
        try:
            dataMember = Member.query.filter_by(id=id).first()
            db.session.delete(dataMember) # Hapus data Member
            db.session.commit()
        except Exception as e:
            print(e)
        return redirect(url_for('daftarMember'))
        return render_template('daftarmember-main.html')
    else:
        return redirect(url_for("login"))