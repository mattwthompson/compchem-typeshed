from rdkit.Dbase import DbInfo as DbInfo, DbModule as DbModule, DbUtils as DbUtils
from typing import Any

class DbError(RuntimeError): ...

class DbConnect:
    dbName: Any
    tableName: Any
    user: Any
    password: Any
    cn: Any
    cursor: Any
    def __init__(self, dbName: str = ..., tableName: str = ..., user: str = ..., password: str = ...) -> None: ...
    def GetTableNames(self, includeViews: int = ...): ...
    def GetColumnNames(self, table: str = ..., join: str = ..., what: str = ..., where: str = ..., **kwargs): ...
    def GetColumnNamesAndTypes(self, table: str = ..., join: str = ..., what: str = ..., where: str = ..., **kwargs): ...
    def GetColumns(self, fields, table: str = ..., join: str = ..., **kwargs): ...
    def GetData(self, table: Any | None = ..., fields: str = ..., where: str = ..., removeDups: int = ..., join: str = ..., transform: Any | None = ..., randomAccess: int = ..., **kwargs): ...
    def GetDataCount(self, table: Any | None = ..., where: str = ..., join: str = ..., **kwargs): ...
    def GetCursor(self): ...
    def KillCursor(self) -> None: ...
    def AddTable(self, tableName, colString) -> None: ...
    def InsertData(self, tableName, vals) -> None: ...
    def InsertColumnData(self, tableName, columnName, value, where) -> None: ...
    def AddColumn(self, tableName, colName, colType) -> None: ...
    def Commit(self) -> None: ...