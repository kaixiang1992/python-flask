"""empty message

Revision ID: 32c05d436e2a
Revises: 
Create Date: 2020-03-01 21:09:29.348850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32c05d436e2a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('create_time', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
