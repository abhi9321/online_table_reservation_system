"""empty message

Revision ID: bc0c636794ea
Revises: fc56e448a5d8
Create Date: 2020-04-14 09:53:22.161841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc0c636794ea'
down_revision = 'fc56e448a5d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reservation', 'check_in')
    op.drop_index('ix_user_email', table_name='user')
    op.drop_column('user', 'password_hash')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.VARCHAR(length=120), nullable=True))
    op.add_column('user', sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True))
    op.create_index('ix_user_email', 'user', ['email'], unique=1)
    op.add_column('reservation', sa.Column('check_in', sa.DATETIME(), nullable=True))
    # ### end Alembic commands ###