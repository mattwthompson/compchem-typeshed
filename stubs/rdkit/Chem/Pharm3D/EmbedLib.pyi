from collections.abc import Generator
from rdkit import Chem as Chem
from rdkit.Chem import ChemicalFeatures as ChemicalFeatures, ChemicalForceFields as ChemicalForceFields
from rdkit.Chem.Pharm3D import ExcludedVolume as ExcludedVolume
from rdkit.ML.Data import Stats as Stats
from typing import Any

logger: Any
defaultFeatLength: float

def GetAtomHeavyNeighbors(atom): ...
def ReplaceGroup(match, bounds, slop: float = ..., useDirs: bool = ..., dirLength=...): ...
def EmbedMol(mol, bm, atomMatch: Any | None = ..., weight: float = ..., randomSeed: int = ..., excludedVolumes: Any | None = ...) -> None: ...
def AddExcludedVolumes(bm, excludedVolumes, smoothIt: bool = ...): ...
def UpdatePharmacophoreBounds(bm, atomMatch, pcophore, useDirs: bool = ..., dirLength=..., mol: Any | None = ...): ...
def EmbedPharmacophore(mol, atomMatch, pcophore, randomSeed: int = ..., count: int = ..., smoothFirst: bool = ..., silent: bool = ..., bounds: Any | None = ..., excludedVolumes: Any | None = ..., targetNumber: int = ..., useDirs: bool = ...): ...
def isNaN(v): ...
def OptimizeMol(mol, bm, atomMatches: Any | None = ..., excludedVolumes: Any | None = ..., forceConstant: float = ..., maxPasses: int = ..., verbose: bool = ...): ...
def EmbedOne(mol, name, match, pcophore, count: int = ..., silent: int = ..., **kwargs): ...
def MatchPharmacophoreToMol(mol, featFactory, pcophore): ...
def MatchFeatsToMol(mol, featFactory, features): ...
def CombiEnum(sequence) -> Generator[Any, None, None]: ...
def DownsampleBoundsMatrix(bm, indices, maxThresh: float = ...): ...
def CoarseScreenPharmacophore(atomMatch, bounds, pcophore, verbose: bool = ...): ...
def Check2DBounds(atomMatch, mol, pcophore): ...
def ConstrainedEnum(matches, mol, pcophore, bounds, use2DLimits: bool = ..., index: int = ..., soFar=...) -> Generator[Any, None, None]: ...
def MatchPharmacophore(matches, bounds, pcophore, useDownsampling: bool = ..., use2DLimits: bool = ..., mol: Any | None = ..., excludedVolumes: Any | None = ..., useDirs: bool = ...): ...
def GetAllPharmacophoreMatches(matches, bounds, pcophore, useDownsampling: int = ..., progressCallback: Any | None = ..., use2DLimits: bool = ..., mol: Any | None = ..., verbose: bool = ...): ...
def ComputeChiralVolume(mol, centerIdx, confId: int = ...): ...
