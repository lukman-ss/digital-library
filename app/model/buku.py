from app import db
from datetime import datetime

class Buku(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    judulbuku = db.Column(db.String(100), nullable=False)
    pengarang = db.Column(db.String(100), nullable=False)
    penerbit = db.Column(db.String(100), nullable=False)
    tahunterbit = db.Column(db.String(100), nullable=False)
    kategori = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Buku {}>'.format(self.id)