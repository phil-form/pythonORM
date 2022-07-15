"""20220713_1020

Revision ID: 21e3720a1569
Revises: e1c76c2e70ed
Create Date: 2022-07-13 10:20:54.337689

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '21e3720a1569'
down_revision = 'e1c76c2e70ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('createdate', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updatedate', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deletedate', sa.DateTime(timezone=True), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('itemid', sa.Integer(), nullable=False),
    sa.Column('itemname', sa.String(length=50), nullable=False),
    sa.Column('itemdescription', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('itemid')
    )
    op.create_table('baskets',
    sa.Column('createdate', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updatedate', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deletedate', sa.DateTime(timezone=True), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('basketid', sa.Integer(), nullable=False),
    sa.Column('basketclosed', sa.Boolean(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['users.userid'], ),
    sa.PrimaryKeyConstraint('basketid')
    )
    op.create_table('user_roles',
    sa.Column('createdate', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updatedate', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deletedate', sa.DateTime(timezone=True), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('roleid', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['roleid'], ['users.userid'], ),
    sa.ForeignKeyConstraint(['userid'], ['roles.roleid'], ),
    sa.PrimaryKeyConstraint('roleid', 'userid')
    )
    op.create_table('baskets_items',
    sa.Column('createdate', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updatedate', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deletedate', sa.DateTime(timezone=True), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('itemid', sa.Integer(), nullable=False),
    sa.Column('basketid', sa.Integer(), nullable=False),
    sa.Column('itemquantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['basketid'], ['baskets.basketid'], ),
    sa.ForeignKeyConstraint(['itemid'], ['items.itemid'], ),
    sa.PrimaryKeyConstraint('itemid', 'basketid')
    )
    op.drop_table('userroles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userroles',
    sa.Column('createdate', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('updatedate', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('deletedate', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('roleid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('userid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['roleid'], ['users.userid'], name='userroles_roleid_fkey'),
    sa.ForeignKeyConstraint(['userid'], ['roles.roleid'], name='userroles_userid_fkey'),
    sa.PrimaryKeyConstraint('roleid', 'userid', name='userroles_pkey')
    )
    op.drop_table('baskets_items')
    op.drop_table('user_roles')
    op.drop_table('baskets')
    op.drop_table('items')
    # ### end Alembic commands ###