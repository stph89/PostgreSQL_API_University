"""init db

Revision ID: f0242b4866bf
Revises: d4867f3a4c0a
Create Date: 2022-10-29 22:58:18.864392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0242b4866bf'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profesor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('apedillo_1', sa.String(), nullable=True),
    sa.Column('apedillo_2', sa.String(), nullable=True),
    sa.Column('edad', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_profesor_apedillo_1'), 'profesor', ['apedillo_1'], unique=False)
    op.create_index(op.f('ix_profesor_apedillo_2'), 'profesor', ['apedillo_2'], unique=False)
    op.create_index(op.f('ix_profesor_edad'), 'profesor', ['edad'], unique=False)
    op.create_index(op.f('ix_profesor_email'), 'profesor', ['email'], unique=True)
    op.create_index(op.f('ix_profesor_id'), 'profesor', ['id'], unique=False)
    op.create_index(op.f('ix_profesor_nombre'), 'profesor', ['nombre'], unique=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_index(op.f('ix_profesor_nombre'), table_name='profesor')
    op.drop_index(op.f('ix_profesor_id'), table_name='profesor')
    op.drop_index(op.f('ix_profesor_email'), table_name='profesor')
    op.drop_index(op.f('ix_profesor_edad'), table_name='profesor')
    op.drop_index(op.f('ix_profesor_apedillo_2'), table_name='profesor')
    op.drop_index(op.f('ix_profesor_apedillo_1'), table_name='profesor')
    op.drop_table('profesor')
    # ### end Alembic commands ###