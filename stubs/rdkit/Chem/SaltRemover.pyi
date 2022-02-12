from rdkit import Chem as Chem, RDConfig as RDConfig
from rdkit.Chem.rdmolfiles import SDMolSupplier as SDMolSupplier, SmilesMolSupplier as SmilesMolSupplier
from typing import Any

class InputFormat:
    SMARTS: str
    MOL: str
    SMILES: str

class SaltRemover:
    defnFilename: Any
    defnData: Any
    salts: Any
    defnFormat: Any
    def __init__(self, defnFilename: Any | None = ..., defnData: Any | None = ..., defnFormat=...) -> None: ...
    def StripMol(self, mol, dontRemoveEverything: bool = ..., sanitize: bool = ...): ...
    def StripMolWithDeleted(self, mol, dontRemoveEverything: bool = ...): ...
    def __call__(self, mol, dontRemoveEverything: bool = ...): ...
