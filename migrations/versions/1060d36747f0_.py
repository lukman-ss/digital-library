"""empty message

Revision ID: 1060d36747f0
Revises: 9f25c18478ce
Create Date: 2021-05-10 13:51:52.016680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1060d36747f0'
down_revision = '9f25c18478ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('buku', sa.Column('pdf', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('buku', 'pdf')
    # ### end Alembic commands ###
