"""empty message

Revision ID: 72695e838965
Revises: 
Create Date: 2020-03-07 17:37:14.481873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72695e838965'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('psd', sa.String(length=30), nullable=False),
    sa.Column('money', sa.Float(), nullable=True),
    sa.Column('create_time', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
