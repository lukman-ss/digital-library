from app import app,db
from flask import render_template,request,url_for,redirect,Flask,session
from app.model.buku import Buku
from app.model.member import Member
from app.model.pinjam import Pinjam

@app.route('/', methods=['GET','POST'])
def login():
    if 'email' in session:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email == 'admin@gmail.com' and password == 'pass':
            session['email']=email
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('email')
    return redirect(url_for('login'))


@app.route('/dashbords')
def dashboard():
    titles = "DASHBOARD"
    judul = "Dashboard"
    if 'email' in session:
        jumlahMember = Member.query.filter(Member.id).count()
        jumlahBuku = Buku.query.filter(Buku.id).count()
        jumlahPinjam = Pinjam.query.filter(Pinjam.id).count()
        return render_template('dashboards.html',judul=judul,titles=titles,jumlahBuku=jumlahBuku,jumlahMember=jumlahMember,jumlahPinjam=jumlahPinjam)
    else:
        return redirect(url_for("login"))

# BUKU

@app.route('/daftarbuku')
def daftarBuku():
    titles = "DAFTAR BUKU"
    judul = "Daftar Buku"
    subjudul = "Daftar Buku | DIGITAL LIBRARY STMIK JAYAKARTA"
    buttontambah = "Tambah Data Buku"
    if 'email' in session:
        listBuku = Buku.query.all()
        return render_template('daftarbuku-main.html',judul=judul, subjudul=subjudul,titles=titles,buttontambah=buttontambah,listBuku=enumerate(listBuku))
    else:
        return redirect(url_for("login"))

@app.route('/daftarbuku/tambahbuku', methods=['POST', 'GET'])
def tambahBuku():
    titles = "DAFTAR BUKU - Tambah Buku"
    judul = "Tambah Buku"
    subjudul = "Tambah Buku | DIGITAL LIBRARY STMIK JAYAKARTA"
    if request.method == 'POST':
        judulbuku = request.form['judulbuku']
        pengarang = request.form['pengarang']
        penerbit = request.form['penerbit']
        tahunterbit = request.form['tahunterbit']
        kategori = request.form['kategori']
        try:
            dataBuku=Buku(judulbuku=judulbuku,pengarang=pengarang,penerbit=penerbit,tahunterbit=tahunterbit,kategori=kategori)
            db.session.add(dataBuku)
            db.session.commit()
        except Exception as e:
            print(e)
    if 'email' in session:

        return render_template('daftarbuku-tambah.html',judul=judul, subjudul=subjudul,titles=titles)
    else:
        return redirect(url_for("login"))

# MEMBER

@app.route('/daftarmember')
def daftarMember():
    titles = "DAFTAR MEMBER"
    judul = "Daftar Member"
    subjudul = "Daftar Member | DIGITAL LIBRARY STMIK JAYAKARTA"
    buttontambah = "Tambah Data Member"
    if 'email' in session:
        listMember = Member.query.all()
        return render_template('daftarmember-main.html',judul=judul, subjudul=subjudul,titles=titles,buttontambah=buttontambah,listMember=enumerate(listMember))
    else:
        return redirect(url_for("login"))

@app.route('/daftarmember/tambahmember',methods=['POST','GET'])
def tambahMember():
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
            db.session.add(dataMember)
            db.session.commit()
        except Exception as e:
            print(e)

    if 'email' in session:
        return render_template('daftarmember-tambah.html',judul=judul, subjudul=subjudul,titles=titles)
    else:
        return redirect(url_for("login"))

@app.route('/daftarbuku/ubahbuku/<int:id>',methods=['POST','GET'])
def ubahDaftarBuku(id):
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
                db.session.commit()
            except Exception as e:
                print(e)
            return redirect(url_for('daftarBuku'))
        listBuku = Buku.query.filter_by(id=id).first()
        return render_template('daftarbuku-ubah.html',judul=judul, subjudul=subjudul,titles=titles,buttontambah=buttontambah,listBuku=listBuku)
    else:
        return redirect(url_for("login"))

# @app.route('/daftarbuku/ubahbuku',methods=['POST','GET'])
# def updatedDaftarBuku():
#     if request.method == 'POST':
#         id = request.form['id']
#         judulbuku = request.form['judulbuku']
#         pengarang = request.form['pengarang']
#         penerbit = request.form['penerbit']
#         tahunterbit = request.form['tahunterbit']
#         kategori = request.form['kategori']
#         try:
#             ubahDataBuku = Buku.query.filter_by(id=id).first()
#             ubahDataBuku.judulbuku = judulbuku
#             ubahDataBuku.pengarang = pengarang
#             ubahDataBuku.penerbit = penerbit
#             ubahDataBuku.tahunterbit = tahunterbit
#             ubahDataBuku.kategori = kategori
#             db.session.commit()
#         except Exception as e:
#             print(e)
#         return redirect(url_for('daftarBuku'))

@app.route('/daftarbuku/hapusbuku/<int:id>',methods=['POST','GET'])
def hapusBuku(id):
    if 'email' in session:
        try:
            dataBuku = Buku.query.filter_by(id=id).first()
            db.session.delete(dataBuku)
            db.session.commit()
        except Exception as e:
            print(e)
        return redirect(url_for('daftarBuku'))
        return render_template('daftarmember-main.html')
    else:
        return redirect(url_for("login"))

@app.route('/daftarbuku/ubahmember/<int:id>',methods=['POST','GET'])
def ubahDaftarMember(id):
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
                db.session.commit()
            except Exception as e:
                print(e)
            return redirect(url_for('daftarMember'))
        listMember = Member.query.filter_by(id=id).first()
        return render_template('daftarmember-ubah.html',judul=judul, subjudul=subjudul,titles=titles,buttontambah=buttontambah,listMember=listMember)
    else:
        return redirect(url_for("login"))

@app.route('/daftarbuku/hapusmember/<int:id>',methods=['POST','GET'])
def hapusMember(id):
    if 'email' in session:
        try:
            dataMember = Member.query.filter_by(id=id).first()
            db.session.delete(dataMember)
            db.session.commit()
        except Exception as e:
            print(e)
        return redirect(url_for('daftarMember'))
        return render_template('daftarmember-main.html')
    else:
        return redirect(url_for("login"))

@app.route('/daftarpinjam')
def daftarPinjam():
    titles = "DAFTAR Peminjaman Buku"
    judul = "Daftar Peminjaman Buku"
    subjudul = "Daftar Peminjaman Buku | DIGITAL LIBRARY STMIK JAYAKARTA"
    buttontambah = "Tambah Data Peminjaman"
    if 'email' in session:
        listBuku = Buku.query.all()
        listMember = Member.query.all()
        listPinjam = Pinjam.query.all()
        return render_template('daftarpeminjaman-main.html',judul=judul, subjudul=subjudul,titles=titles,buttontambah=buttontambah,listPinjam=enumerate(listPinjam),listBuku=enumerate(listBuku), listMember=enumerate(listMember))
    else:
        return redirect(url_for("login"))

@app.route('/daftarpinjam/tambahpinjam', methods=['POST', 'GET'])
def tambahPinjam():
    titles = "DAFTAR BUKU - Tambah Buku"
    judul = "Tambah Buku"
    subjudul = "Tambah Buku | DIGITAL LIBRARY STMIK JAYAKARTA"
    if request.method == 'POST':
        idbuku = request.form['idbuku']
        idmember = request.form['idmember']
        tanggalpinjam = request.form['tanggalpinjam']
        tanggalkembali = request.form['tanggalkembali']
        try:
            dataPinjam=Pinjam(idbuku=idbuku,idmember=idmember,tanggalpinjam=tanggalpinjam,tanggalkembali=tanggalkembali)
            db.session.add(dataPinjam)
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