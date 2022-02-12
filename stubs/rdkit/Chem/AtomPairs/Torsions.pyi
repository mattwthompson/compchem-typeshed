from rdkit.Chem import rdMolDescriptors as rdMolDescriptors
from rdkit.Chem.AtomPairs import Utils as Utils
from rdkit.Chem.rdMolDescriptors import GetHashedTopologicalTorsionFingerprint as GetHashedTopologicalTorsionFingerprint, GetTopologicalTorsionFingerprint as GetTopologicalTorsionFingerprint
from typing import Any

GetTopologicalTorsionFingerprintAsIntVect: Any

def pyScorePath(mol, path, size, atomCodes: Any | None = ...): ...
def ExplainPathScore(score, size: int = ...): ...
def GetTopologicalTorsionFingerprintAsIds(mol, targetSize: int = ...): ...
