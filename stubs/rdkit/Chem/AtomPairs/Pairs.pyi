from rdkit import DataStructs as DataStructs
from rdkit.Chem import rdMolDescriptors as rdMolDescriptors
from rdkit.Chem.AtomPairs import Utils as Utils
from rdkit.Chem.rdMolDescriptors import GetAtomPairFingerprint as GetAtomPairFingerprint, GetHashedAtomPairFingerprint as GetHashedAtomPairFingerprint
from typing import Any

GetAtomPairFingerprintAsIntVect: Any
numPathBits: Any
numFpBits: Any
fpLen: Any

def pyScorePair(at1, at2, dist, atomCodes: Any | None = ..., includeChirality: bool = ...): ...
def ExplainPairScore(score, includeChirality: bool = ...): ...
def GetAtomPairFingerprintAsBitVect(mol): ...
