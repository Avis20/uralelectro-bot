import pytest

from alembic.config import Config
from alembic.script import Script, ScriptDirectory
from alembic.command import downgrade, upgrade


def get_revisions():
    config = Config("alembic.ini")
    revisions_dir = ScriptDirectory.from_config(config)

    revisions = list(revisions_dir.walk_revisions('base', 'heads'))
    revisions.reverse()
    return revisions


@pytest.mark.parametrize('revision', get_revisions())
def test_migrations_stairway(alembic_config, revision: Script, single_use_database):
    upgrade(alembic_config, revision.revision)
    downgrade(alembic_config, str(revision.down_revision or '-1'))
    upgrade(alembic_config, revision.revision)
