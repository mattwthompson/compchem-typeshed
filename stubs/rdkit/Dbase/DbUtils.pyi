from rdkit.Dbase import DbInfo as DbInfo, DbModule as DbModule
from rdkit.Dbase.DbResultSet import DbResultSet as DbResultSet, RandomAccessDbResultSet as RandomAccessDbResultSet
from typing import Any

def GetColumns(dBase, table, fieldString, user: str = ..., password: str = ..., join: str = ..., cn: Any | None = ...): ...
def GetData(dBase, table, fieldString: str = ..., whereString: str = ..., user: str = ..., password: str = ..., removeDups: int = ..., join: str = ..., forceList: int = ..., transform: Any | None = ..., randomAccess: int = ..., extras: Any | None = ..., cn: Any | None = ...): ...
def DatabaseToText(dBase, table, fields: str = ..., join: str = ..., where: str = ..., user: str = ..., password: str = ..., delim: str = ..., cn: Any | None = ...): ...
def TypeFinder(data, nRows, nCols, nullMarker: Any | None = ...): ...
def GetTypeStrings(colHeadings, colTypes, keyCol: Any | None = ...): ...
def TextFileToDatabase(dBase, table, inF, delim: str = ..., user: str = ..., password: str = ..., maxColLabelLen: int = ..., keyCol: Any | None = ..., nullMarker: Any | None = ...) -> None: ...
def DatabaseToDatabase(fromDb, fromTbl, toDb, toTbl, fields: str = ..., join: str = ..., where: str = ..., user: str = ..., password: str = ..., keyCol: Any | None = ..., nullMarker: str = ...) -> None: ...
