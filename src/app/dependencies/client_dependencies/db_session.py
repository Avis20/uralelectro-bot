from typing import Annotated
from fastapi import Depends

from app.connectors.pg_database import MasterSessionMaker, SQLAlchemyDatabaseConnector, SlaveSessionMaker
from app.settings import Settings


settings = Settings()
database_dep = SQLAlchemyDatabaseConnector(settings)
MasterSessionMakerDep = Annotated[MasterSessionMaker, Depends(database_dep.get_master_session_maker)]
SlaveSessionMakerDep = Annotated[SlaveSessionMaker, Depends(database_dep.get_slave_session_maker)]
