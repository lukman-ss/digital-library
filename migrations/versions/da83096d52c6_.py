"""empty message

Revision ID: da83096d52c6
Revises: 80e4a165261b
Create Date: 2021-04-13 11:10:24.505985

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'da83096d52c6'
down_revision = '80e4a165261b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('member', 'tanggallahir',
               existing_type=mysql.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('member', 'tanggallahir',
               existing_type=mysql.DATETIME(),
               nullable=False)
    # ### end Alembic commands ###
