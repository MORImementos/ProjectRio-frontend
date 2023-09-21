"""empty message

Revision ID: e5873923ddbe
Revises: 5e820ba37623
Create Date: 2023-04-06 19:26:41.911642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5873923ddbe'
down_revision = '5e820ba37623'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('character', 'name',
               existing_type=sa.VARCHAR(length=16),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.alter_column('character', 'name_lowercase',
               existing_type=sa.VARCHAR(length=16),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.alter_column('character', 'starting_addr',
               existing_type=sa.VARCHAR(length=16),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.alter_column('community', 'name',
               existing_type=sa.VARCHAR(length=32),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.alter_column('community', 'name_lowercase',
               existing_type=sa.VARCHAR(length=32),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.alter_column('community', 'comm_type',
               existing_type=sa.VARCHAR(length=16),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.alter_column('community', 'desc',
               existing_type=sa.VARCHAR(length=300),
               type_=sa.String(length=64000),
               existing_nullable=True)
    op.alter_column('gecko_code_tag', 'gecko_code_desc',
               existing_type=sa.TEXT(),
               type_=sa.String(length=64000),
               existing_nullable=True)
    op.alter_column('tag', 'name',
               existing_type=sa.VARCHAR(length=32),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.alter_column('tag', 'name_lowercase',
               existing_type=sa.VARCHAR(length=32),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.alter_column('tag', 'tag_type',
               existing_type=sa.VARCHAR(length=16),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.alter_column('tag', 'desc',
               existing_type=sa.VARCHAR(length=300),
               type_=sa.String(length=64000),
               existing_nullable=True)
    op.alter_column('tag_set', 'name',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.alter_column('tag_set', 'name_lowercase',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.alter_column('tag_set', 'type',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.alter_column('user_group', 'name',
               existing_type=sa.VARCHAR(length=32),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.alter_column('user_group', 'name_lowercase',
               existing_type=sa.VARCHAR(length=32),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.alter_column('user_group', 'desc',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=64000),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_group', 'desc',
               existing_type=sa.String(length=64000),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)
    op.alter_column('user_group', 'name_lowercase',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=32),
               existing_nullable=True)
    op.alter_column('user_group', 'name',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=32),
               existing_nullable=True)
    op.alter_column('tag_set', 'type',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=120),
               existing_nullable=True)
    op.alter_column('tag_set', 'name_lowercase',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=120),
               existing_nullable=True)
    op.alter_column('tag_set', 'name',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=120),
               existing_nullable=True)
    op.alter_column('tag', 'desc',
               existing_type=sa.String(length=64000),
               type_=sa.VARCHAR(length=300),
               existing_nullable=True)
    op.alter_column('tag', 'tag_type',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=16),
               existing_nullable=True)
    op.alter_column('tag', 'name_lowercase',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=32),
               existing_nullable=True)
    op.alter_column('tag', 'name',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=32),
               existing_nullable=True)
    op.alter_column('gecko_code_tag', 'gecko_code_desc',
               existing_type=sa.String(length=64000),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.alter_column('community', 'desc',
               existing_type=sa.String(length=64000),
               type_=sa.VARCHAR(length=300),
               existing_nullable=True)
    op.alter_column('community', 'comm_type',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=16),
               existing_nullable=True)
    op.alter_column('community', 'name_lowercase',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=32),
               existing_nullable=True)
    op.alter_column('community', 'name',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=32),
               existing_nullable=True)
    op.alter_column('character', 'starting_addr',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=16),
               existing_nullable=True)
    op.alter_column('character', 'name_lowercase',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=16),
               existing_nullable=True)
    op.alter_column('character', 'name',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=16),
               existing_nullable=True)
    # ### end Alembic commands ###
