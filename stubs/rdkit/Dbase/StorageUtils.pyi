from rdkit import RDConfig as RDConfig
from rdkit.Dbase import DbModule as DbModule
from typing import Any

def ValidateRDId(ID): ...
def RDIdToInt(ID, validate: int = ...): ...
def IndexToRDId(idx, leadText: str = ...): ...
def GetNextId(conn, table, idColName: str = ...): ...
def GetNextRDId(conn, table, idColName: str = ..., leadText: str = ...): ...
def RegisterItem(conn, table, value, columnName, data: Any | None = ..., id: str = ..., idColName: str = ..., leadText: str = ...): ...
def RegisterItems(conn, table, values, columnName, rows, startId: str = ..., idColName: str = ..., leadText: str = ...): ...

__test__: Any