from rdkit import Chem as Chem
from rdkit.Chem import AllChem as AllChem, Crippen as Crippen
from rdkit.Chem.ChemUtils.AlignDepict import AlignDepict as AlignDepict
from typing import Any

logger: Any

def Usage() -> None: ...

nDumped: int

def Explode(template, sidechains, outF, autoNames: bool = ..., do3D: bool = ..., useTethers: bool = ...) -> None: ...
def MoveDummyNeighborsToBeginning(mol, useAll: bool = ...): ...
def ConstructSidechains(suppl, sma: Any | None = ..., replace: bool = ..., useAll: bool = ...): ...
