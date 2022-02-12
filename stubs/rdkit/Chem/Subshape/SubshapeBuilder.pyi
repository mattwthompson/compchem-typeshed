from rdkit import Chem as Chem, Geometry as Geometry
from rdkit.Chem import AllChem as AllChem
from rdkit.Chem.Subshape import BuilderUtils as BuilderUtils, SubshapeObjects as SubshapeObjects
from typing import Any

class SubshapeCombineOperations:
    UNION: int
    SUM: int
    INTERSECT: int

class SubshapeBuilder:
    gridDims: Any
    gridSpacing: float
    winRad: float
    nbrCount: int
    terminalPtRadScale: float
    fraction: float
    stepSize: float
    featFactory: Any
    def SampleSubshape(self, subshape1, newSpacing): ...
    def GenerateSubshapeShape(self, cmpd, confId: int = ..., addSkeleton: bool = ..., **kwargs): ...
    def __call__(self, cmpd, **kwargs): ...
    def GenerateSubshapeSkeleton(self, shape, conf: Any | None = ..., terminalPtsOnly: bool = ..., skelFromConf: bool = ...) -> None: ...
    def CombineSubshapes(self, subshape1, subshape2, operation=...): ...
