import sys
from logging.config import fileConfig
from pathlib import Path

from alembic import context

project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from database import Base, engine
import models

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def include_object(object_, name, type_, reflected, compare_to):
    if type_ == "table":
        if getattr(object_, "schema", None) == "auth":
            return False
        if name == "spatial_ref_sys":
            return False
    return True

def run_migrations_offline():
    context.configure(
        include_object=include_object,
        url=engine.url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
        include_schemas=False,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    with engine.connect() as connection:
        context.configure(
            include_object=include_object,
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            include_schemas=False,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()