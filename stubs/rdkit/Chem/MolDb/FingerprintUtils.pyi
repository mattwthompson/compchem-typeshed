from rdkit import Chem as Chem, DataStructs as DataStructs
from typing import Any

similarityMethods: Any
supportedSimilarityMethods: Any

class LayeredOptions:
    loadLayerFlags: int
    searchLayerFlags: int
    minPath: int
    maxPath: int
    fpSize: int
    wordSize: int
    nWords: Any
    @staticmethod
    def GetFingerprint(mol, query: bool = ...): ...
    @staticmethod
    def GetWords(mol, query: bool = ...): ...
    @staticmethod
    def GetQueryText(mol, query: bool = ...): ...

def BuildSigFactory(options: Any | None = ..., fdefFile: Any | None = ..., bins=..., skipFeats=...): ...
def BuildAtomPairFP(mol): ...
def BuildTorsionsFP(mol): ...
def BuildRDKitFP(mol): ...
def BuildPharm2DFP(mol): ...
def BuildMorganFP(mol): ...
def BuildAvalonFP(mol, smiles: Any | None = ...): ...
def DepickleFP(pkl, similarityMethod): ...
