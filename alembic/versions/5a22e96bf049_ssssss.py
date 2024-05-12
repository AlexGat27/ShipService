"""ssssss

Revision ID: 5a22e96bf049
Revises: 2c0b57536597
Create Date: 2024-05-13 01:04:46.329641

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a22e96bf049'
down_revision: Union[str, None] = '2c0b57536597'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dangers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('security_indicators',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ship_systems',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ships',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('equipments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('ship_system_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ship_system_id'], ['ship_systems.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ship_and_systems',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ship_id', sa.Integer(), nullable=True),
    sa.Column('ship_system_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ship_id'], ['ships.id'], ),
    sa.ForeignKeyConstraint(['ship_system_id'], ['ship_systems.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('system_and_indicators',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ship_system_id', sa.Integer(), nullable=True),
    sa.Column('security_indicator_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['security_indicator_id'], ['security_indicators.id'], ),
    sa.ForeignKeyConstraint(['ship_system_id'], ['ship_systems.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('protections',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('equipment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['equipment_id'], ['equipments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vulnerabilities',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('equipment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['equipment_id'], ['equipments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('danger_for_system_ship_system_id_fkey', 'danger_for_system', type_='foreignkey')
    op.drop_constraint('danger_for_system_danger_id_fkey', 'danger_for_system', type_='foreignkey')
    op.drop_constraint('protection_equipment_id_fkey', 'protection', type_='foreignkey')
    op.drop_table('security_indicator')
    op.drop_table('vulnerability')
    op.drop_table('equipment')
    op.drop_table('protection')
    op.drop_table('ship_system')
    op.drop_table('ship')
    op.drop_table('danger')
    op.create_foreign_key(None, 'danger_for_system', 'dangers', ['danger_id'], ['id'])
    op.create_foreign_key(None, 'danger_for_system', 'ship_systems', ['ship_system_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'danger_for_system', type_='foreignkey')
    op.drop_constraint(None, 'danger_for_system', type_='foreignkey')
    op.create_foreign_key('danger_for_system_danger_id_fkey', 'danger_for_system', 'danger', ['danger_id'], ['id'])
    op.create_foreign_key('danger_for_system_ship_system_id_fkey', 'danger_for_system', 'ship_system', ['ship_system_id'], ['id'])
    op.create_table('danger',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='danger_pkey')
    )
    op.create_table('ship',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('ship_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='ship_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('ship_system',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('ship_system_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('ship_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['ship_id'], ['ship.id'], name='ship_system_ship_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='ship_system_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('protection',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('equipment_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['equipment_id'], ['equipment.id'], name='protection_equipment_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='protection_pkey')
    )
    op.create_table('equipment',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('equipment_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('ship_system_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['ship_system_id'], ['ship_system.id'], name='equipment_ship_system_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='equipment_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('vulnerability',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('equipment_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['equipment_id'], ['equipment.id'], name='vulnerability_equipment_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='vulnerability_pkey')
    )
    op.create_table('security_indicator',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('ship_system_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['ship_system_id'], ['ship_system.id'], name='security_indicator_ship_system_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='security_indicator_pkey')
    )
    op.drop_table('vulnerabilities')
    op.drop_table('protections')
    op.drop_table('system_and_indicators')
    op.drop_table('ship_and_systems')
    op.drop_table('equipments')
    op.drop_table('ships')
    op.drop_table('ship_systems')
    op.drop_table('security_indicators')
    op.drop_table('dangers')
    # ### end Alembic commands ###