from rdkit.Chem.FeatMaps.FeatMapPoint import FeatMapPoint as FeatMapPoint
from typing import Any

class FeatMapScoreMode:
    All: int
    Closest: int
    Best: int

class FeatDirScoreMode:
    Ignore: int
    DotFullRange: int
    DotPosRange: int

class FeatMapParams:
    radius: float
    width: float
    class FeatProfile:
        Gaussian: int
        Triangle: int
        Box: int
    featProfile: Any

class FeatMap:
    dirScoreMode: Any
    scoreMode: Any
    params: Any
    def __init__(self, params: Any | None = ..., feats: Any | None = ..., weights: Any | None = ...) -> None: ...
    def AddFeature(self, feat, weight: Any | None = ...) -> None: ...
    def AddFeatPoint(self, featPt) -> None: ...
    def GetFeatures(self): ...
    def GetNumFeatures(self): ...
    def GetFeature(self, i): ...
    def DropFeature(self, i) -> None: ...
    def GetFeatFeatScore(self, feat1, feat2, typeMatch: bool = ...): ...
    def ScoreFeats(self, featsToScore, mapScoreVect=..., featsScoreVect=..., featsToFeatMapIdx=...): ...
