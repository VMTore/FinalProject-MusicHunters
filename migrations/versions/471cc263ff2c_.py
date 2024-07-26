"""empty message

Revision ID: 471cc263ff2c
Revises: 5d52175cb027
Create Date: 2024-07-25 17:19:33.216092

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '471cc263ff2c'
down_revision = '5d52175cb027'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.alter_column('genere',
               existing_type=postgresql.ENUM('pop', 'fiestas', 'rock', 'clasic', 'reggaeton', 'rap', 'trap', 'indie', name='generetype'),
               type_=sa.String(length=120),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.alter_column('genere',
               existing_type=sa.String(length=120),
               type_=postgresql.ENUM('pop', 'fiestas', 'rock', 'clasic', 'reggaeton', 'rap', 'trap', 'indie', name='generetype'),
               existing_nullable=False)

    # ### end Alembic commands ###