from rdkit import Chem as Chem, RDConfig as RDConfig
from rdkit.Chem import rdMolDescriptors as rdMolDescriptors
from rdkit.Chem.rdMolDescriptors import GetAtomPairFingerprint as GetAtomPairFingerprint, GetTopologicalTorsionFingerprint as GetTopologicalTorsionFingerprint
from typing import Any

numPathBits: Any
numFpBits: Any
fpLen: Any

def AssignPattyTypes(mol, defns: Any | None = ...): ...

typMap: Any

def GetBPFingerprint(mol, fpfn=...): ...
def GetBTFingerprint(mol, fpfn=...): ...
