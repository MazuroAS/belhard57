"""empty message

Revision ID: 41c8c9253c68
Revises: 
Create Date: 2022-07-29 21:24:36.196460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41c8c9253c68'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.SmallInteger(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=24), nullable=False),
    sa.Column('parent_id', sa.SmallInteger(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['categories.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=24), nullable=False),
    sa.Column('hashed_password', sa.Text(), nullable=False),
    sa.Column('is_blocked', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('articles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.SmallInteger(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), nullable=False),
    sa.Column('body', sa.VARCHAR(length=1024), nullable=False),
    sa.Column('date_created', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_articles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['articles.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='NO ACTION'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_articles')
    op.drop_table('articles')
    op.drop_table('users')
    op.drop_table('categories')
    # ### end Alembic commands ###
