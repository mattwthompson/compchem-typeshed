from collections.abc import Generator
from rdkit import Chem as Chem, Geometry as Geometry, RDLogger as RDLogger
from rdkit.Chem.Subshape import SubshapeObjects as SubshapeObjects
from rdkit.Numerics import Alignment as Alignment
from typing import Any

logger: Any

class SubshapeAlignment:
    transform: Any
    triangleSSD: Any
    targetTri: Any
    queryTri: Any
    alignedConfId: int
    dirMatch: float
    shapeDist: float

class SubshapeDistanceMetric:
    TANIMOTO: int
    PROTRUDE: int

def GetShapeShapeDistance(s1, s2, distMetric): ...
def ClusterAlignments(mol, alignments, builder, neighborTol: float = ..., distMetric=..., tempConfId: int = ...): ...
def TransformMol(mol, tform, confId: int = ..., newConfId: int = ...) -> None: ...

class SubshapeAligner:
    triangleRMSTol: float
    distMetric: Any
    shapeDistTol: float
    numFeatThresh: int
    dirThresh: float
    edgeTol: float
    coarseGridToleranceMult: float
    medGridToleranceMult: float
    def GetTriangleMatches(self, target, query) -> Generator[Any, None, None]: ...
    def PruneMatchesUsingFeatures(self, target, query, alignments, pruneStats: Any | None = ...) -> None: ...
    def PruneMatchesUsingDirection(self, target, query, alignments, pruneStats: Any | None = ...) -> None: ...
    def PruneMatchesUsingShape(self, targetMol, target, queryMol, query, builder, alignments, tgtConf: int = ..., queryConf: int = ..., pruneStats: Any | None = ...) -> None: ...
    def GetSubshapeAlignments(self, targetMol, target, queryMol, query, builder, tgtConf: int = ..., queryConf: int = ..., pruneStats: Any | None = ...): ...
    def __call__(self, targetMol, target, queryMol, query, builder, tgtConf: int = ..., queryConf: int = ..., pruneStats: Any | None = ...) -> Generator[Any, None, None]: ...
