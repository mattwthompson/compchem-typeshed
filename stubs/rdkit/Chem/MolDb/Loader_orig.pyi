from rdkit import Chem as Chem
from rdkit.Chem import AllChem as AllChem, Crippen as Crippen, Descriptors as Descriptors, Lipinski as Lipinski
from rdkit.Dbase import DbModule as DbModule
from rdkit.Dbase.DbConnection import DbConnect as DbConnect
from typing import Any

logger: Any

def ProcessMol(mol, typeConversions, globalProps, nDone, nameProp: str = ..., nameCol: str = ..., redraw: bool = ..., keepHs: bool = ..., skipProps: bool = ..., addComputedProps: bool = ..., skipSmiles: bool = ..., uniqNames: Any | None = ..., namesSeen: Any | None = ...): ...
def ConvertRows(rows, globalProps, defaultVal, skipSmiles) -> None: ...
def LoadDb(suppl, dbName, nameProp: str = ..., nameCol: str = ..., silent: bool = ..., redraw: bool = ..., errorsTo: Any | None = ..., keepHs: bool = ..., defaultVal: str = ..., skipProps: bool = ..., regName: str = ..., skipSmiles: bool = ..., maxRowsCached: int = ..., uniqNames: bool = ..., addComputedProps: bool = ..., lazySupplier: bool = ..., startAnew: bool = ...) -> None: ...
