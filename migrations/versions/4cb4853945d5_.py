"""empty message

Revision ID: 4cb4853945d5
Revises: bc0c636794ea
Create Date: 2020-04-14 09:56:23.966905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cb4853945d5'
down_revision = 'bc0c636794ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('address', sa.String(length=225), nullable=True),
    sa.Column('amount_per_person', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_restaurant_name'), 'restaurant', ['name'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('phone_number', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_name'), 'user', ['name'], unique=False)
    op.create_index(op.f('ix_user_phone_number'), 'user', ['phone_number'], unique=True)
    op.create_table('menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dish', sa.String(length=64), nullable=True),
    sa.Column('cost', sa.String(length=120), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_menu_cost'), 'menu', ['cost'], unique=True)
    op.create_index(op.f('ix_menu_dish'), 'menu', ['dish'], unique=True)
    op.create_table('table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reservation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=True),
    sa.Column('table_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('num_guests', sa.Integer(), nullable=True),
    sa.Column('reservation_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.ForeignKeyConstraint(['table_id'], ['table.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reservation_num_guests'), 'reservation', ['num_guests'], unique=False)
    op.create_index(op.f('ix_reservation_reservation_time'), 'reservation', ['reservation_time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_reservation_reservation_time'), table_name='reservation')
    op.drop_index(op.f('ix_reservation_num_guests'), table_name='reservation')
    op.drop_table('reservation')
    op.drop_table('table')
    op.drop_index(op.f('ix_menu_dish'), table_name='menu')
    op.drop_index(op.f('ix_menu_cost'), table_name='menu')
    op.drop_table('menu')
    op.drop_index(op.f('ix_user_phone_number'), table_name='user')
    op.drop_index(op.f('ix_user_name'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_restaurant_name'), table_name='restaurant')
    op.drop_table('restaurant')
    # ### end Alembic commands ###