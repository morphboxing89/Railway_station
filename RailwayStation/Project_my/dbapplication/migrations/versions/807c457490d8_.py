"""empty message

Revision ID: 807c457490d8
Revises: 
Create Date: 2024-09-16 02:31:47.832411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '807c457490d8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('train',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('direction', sa.String(length=20), nullable=False),
    sa.Column('times', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('train')
    # ### end Alembic commands ###
