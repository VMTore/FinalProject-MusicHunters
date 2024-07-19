"""empty message

Revision ID: 90db6051a51f
Revises: 40b7ba70c382
Create Date: 2024-07-19 15:48:50.108497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90db6051a51f'
down_revision = '40b7ba70c382'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('precio_tickets', schema=None) as batch_op:
        batch_op.drop_column('url')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('precio_tickets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('url', sa.VARCHAR(length=250), autoincrement=False, nullable=False))

    # ### end Alembic commands ###