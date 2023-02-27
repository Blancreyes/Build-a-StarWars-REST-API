"""empty message

Revision ID: 4b76c17efb2a
Revises: 914493763ea6
Create Date: 2023-02-27 09:38:39.499879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b76c17efb2a'
down_revision = '914493763ea6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.alter_column('planets_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('character_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.alter_column('character_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('planets_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
