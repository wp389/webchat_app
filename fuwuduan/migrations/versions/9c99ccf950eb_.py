"""empty message

Revision ID: 9c99ccf950eb
Revises: 95f573fea691
Create Date: 2018-06-03 15:43:38.800127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c99ccf950eb'
down_revision = '95f573fea691'
branch_labels = None
depends_on = None
def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
   # op.create_foreign_key(None, 'goodguiges', 'goodatters', ['atter'], ['id'])
    op.add_column('goods', sa.Column('pic_url', sa.String(), nullable=True))
    #op.create_foreign_key(None, 'goods', 'classtags', ['classtag'], ['id'])
    #op.drop_column('goods', 'is_you')
    # ### end Alembic commands ###
def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goods', sa.Column('is_you', sa.BOOLEAN(), nullable=True))
    op.drop_constraint(None, 'goods', type_='foreignkey')
    op.drop_column('goods', 'pic_url')
    op.drop_constraint(None, 'goodguiges', type_='foreignkey')
    # ### end Alembic commands ###
