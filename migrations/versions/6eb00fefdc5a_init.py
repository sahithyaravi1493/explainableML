"""'init'

Revision ID: 6eb00fefdc5a
Revises: 13c614f69d01
Create Date: 2020-09-03 14:24:48.838638

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6eb00fefdc5a'
down_revision = '13c614f69d01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('time_elapsed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dataset', sa.String(length=64), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('time', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_time_elapsed_dataset'), 'time_elapsed', ['dataset'], unique=False)
    op.create_index(op.f('ix_time_elapsed_time'), 'time_elapsed', ['time'], unique=False)
    op.create_index(op.f('ix_time_elapsed_user_id'), 'time_elapsed', ['user_id'], unique=False)
    op.drop_table('davidson_dataset_train')
    op.drop_index('ix_davidson_dataset_cluster_index', table_name='davidson_dataset_cluster')
    op.drop_table('davidson_dataset_cluster')
    op.drop_table('davidson_dataset_test')
    op.drop_table('davidson_dataset_noshap')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('davidson_dataset_noshap',
    sa.Column('index', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True),
    sa.Column('level_0', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True),
    sa.Column('label', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True),
    sa.Column('text', mysql.TEXT(), nullable=True),
    sa.Column('cluster_id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True),
    sa.Column('round', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('davidson_dataset_test',
    sa.Column('index', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True),
    sa.Column('label', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True),
    sa.Column('text', mysql.TEXT(), nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('davidson_dataset_cluster',
    sa.Column('index', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True),
    sa.Column('text', mysql.TEXT(), nullable=True),
    sa.Column('cluster_id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True),
    sa.Column('centroid', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('positive', mysql.TEXT(), nullable=True),
    sa.Column('negative', mysql.TEXT(), nullable=True),
    sa.Column('keywords', mysql.TEXT(), nullable=True),
    sa.Column('truth', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('round', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True),
    sa.CheckConstraint('(`centroid` in (0,1))', name='davidson_dataset_cluster_chk_1'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_davidson_dataset_cluster_index', 'davidson_dataset_cluster', ['index'], unique=False)
    op.create_table('davidson_dataset_train',
    sa.Column('index', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True),
    sa.Column('label', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True),
    sa.Column('text', mysql.TEXT(), nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_index(op.f('ix_time_elapsed_user_id'), table_name='time_elapsed')
    op.drop_index(op.f('ix_time_elapsed_time'), table_name='time_elapsed')
    op.drop_index(op.f('ix_time_elapsed_dataset'), table_name='time_elapsed')
    op.drop_table('time_elapsed')
    # ### end Alembic commands ###
