from . import ClusterUtils as ClusterUtils
from rdkit.piddle import piddle as piddle
from rdkit.sping import pid as pid
from typing import Any

piddle = pid

class VisOpts:
    xOffset: int
    yOffset: int
    lineColor: Any
    hideColor: Any
    terminalColors: Any
    lineWidth: int
    hideWidth: float
    nodeRad: int
    nodeColor: Any
    highlightColor: Any
    highlightRad: int

class ClusterRenderer:
    canvas: Any
    size: Any
    ptColors: Any
    lineWidth: Any
    showIndices: Any
    showNodes: Any
    stopAtCentroids: Any
    logScale: Any
    tooClose: Any
    def __init__(self, canvas, size, ptColors=..., lineWidth: Any | None = ..., showIndices: int = ..., showNodes: int = ..., stopAtCentroids: int = ..., logScale: int = ..., tooClose: int = ...) -> None: ...
    ySpace: Any
    def DrawTree(self, cluster, minHeight: float = ...) -> None: ...

def DrawClusterTree(cluster, canvas, size, ptColors=..., lineWidth: Any | None = ..., showIndices: int = ..., showNodes: int = ..., stopAtCentroids: int = ..., logScale: int = ..., tooClose: int = ...) -> None: ...
def ClusterToPDF(cluster, fileName, size=..., ptColors=..., lineWidth: Any | None = ..., showIndices: int = ..., stopAtCentroids: int = ..., logScale: int = ...): ...
def ClusterToSVG(cluster, fileName, size=..., ptColors=..., lineWidth: Any | None = ..., showIndices: int = ..., stopAtCentroids: int = ..., logScale: int = ...): ...
def ClusterToImg(cluster, fileName, size=..., ptColors=..., lineWidth: Any | None = ..., showIndices: int = ..., stopAtCentroids: int = ..., logScale: int = ...): ...
