"""empty message

Revision ID: ad2a42b22780
Revises: 7b74a5ea08d2
Create Date: 2020-04-14 07:53:13.100154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad2a42b22780'
down_revision = '7b74a5ea08d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone_number', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_user_phone_number'), 'user', ['phone_number'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_phone_number'), table_name='user')
    op.drop_column('user', 'phone_number')
    # ### end Alembic commands ###
