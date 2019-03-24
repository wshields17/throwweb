"""empty message

Revision ID: 01c773797b25
Revises: 
Create Date: 2019-03-17 19:37:47.971801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01c773797b25'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meetdata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('meetdate', sa.String(), nullable=True),
    sa.Column('spresult', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('outdoormeetdata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('datemeet', sa.String(), nullable=True),
    sa.Column('spresult', sa.Float(), nullable=True),
    sa.Column('discresult', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('throwers',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('Gradyear', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('throwers')
    op.drop_table('outdoormeetdata')
    op.drop_table('meetdata')
    # ### end Alembic commands ###
