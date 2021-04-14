from app import db
from datetime import datetime

class Member(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    tipe = db.Column(db.String(100), nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    tempatlahir = db.Column(db.String(100), nullable=False)
    tanggallahir = db.Column(db.DateTime)
    jeniskelamin = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.String(100), nullable=False)
    pekerjaan = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Member {}>'.format(self.judulbuku)