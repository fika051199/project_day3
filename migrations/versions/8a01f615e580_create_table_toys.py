"""create table toys

Revision ID: 8a01f615e580
Revises: b1fdf53da16b
Create Date: 2020-08-03 01:05:26.278160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a01f615e580'
down_revision = 'b1fdf53da16b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('toys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.Text(), nullable=True),
    sa.Column('puppy_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['puppy_id'], ['puppies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('toys')
    # ### end Alembic commands ###
