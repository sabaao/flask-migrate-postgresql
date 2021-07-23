"""empty message

Revision ID: 29c9ec063e2c
Revises: 0360d2e4d958
Create Date: 2021-07-24 02:10:13.351454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29c9ec063e2c'
down_revision = '0360d2e4d958'
branch_labels = None
depends_on = None


def upgrade():
    accounts_table = sa.table('user',
        sa.column('name', sa.String),
        sa.column('email', sa.String)
    )

    op.bulk_insert(accounts_table,
        [
            {'name':'John Smith',
                    'email':'abc'},
            {'name':'Ed Williams',
                    'email':'abc'},
            {'name':'Wendy Jones',
                    'email':'abc'},
        ]
    )


def downgrade():
    pass
