from rdkit import Chem as Chem
from rdkit.Chem import AllChem as AllChem
from typing import Any

murckoTransforms: Any

def MakeScaffoldGeneric(mol): ...

murckoPatts: Any
murckoQ: Any
aromaticNTransform: Any

def GetScaffoldForMol(mol): ...
def MurckoScaffoldSmiles(smiles: Any | None = ..., mol: Any | None = ..., includeChirality: bool = ...): ...
def MurckoScaffoldSmilesFromSmiles(smiles, includeChirality: bool = ...): ...
