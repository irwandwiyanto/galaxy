"""
Migration script to add a 'subindex' column to the run table.
"""
from __future__ import print_function

from sqlalchemy import Column, MetaData, Table

from galaxy.model.custom_types import TrimmedString

metadata = MetaData()


def upgrade(migrate_engine):
    metadata.bind = migrate_engine
    print(__doc__)
    metadata.reflect()
    try:
        Run_table = Table( "run", metadata, autoload=True )
        c = Column( "subindex", TrimmedString( 255 ), index=True )
        c.create( Run_table, index_name="ix_run_subindex")
        assert c is Run_table.c.subindex
    except Exception as e:
        print("Adding the subindex column to the run table failed: ", str( e ))


def downgrade(migrate_engine):
    metadata.bind = migrate_engine
    metadata.reflect()
    try:
        Run_table = Table( "run", metadata, autoload=True )
        Run_table.c.subindex.drop()
    except Exception as e:
        print("Dropping the subindex column from run table failed: ", str( e ))
