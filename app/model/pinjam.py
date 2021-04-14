from app import db
from datetime import datetime
from app.model.buku import Buku
from app.model.member import Member

class Pinjam(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    idbuku = db.Column(db.BigInteger,db.ForeignKey(Buku.id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    idmember = db.Column(db.BigInteger, db.ForeignKey(Member.id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    tanggalpinjam = db.Column(db.DateTime)
    tanggalkembali = db.Column(db.DateTime)

    def __repr__(self):
        return '<Pinjam {}>'.format(self.id)