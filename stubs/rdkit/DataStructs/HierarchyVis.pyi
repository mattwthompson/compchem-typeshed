from typing import Any

class VisOpts:
    circRad: int
    minCircRad: int
    maxCircRad: int
    circColor: Any
    terminalEmptyColor: Any
    terminalOnColor: Any
    terminalOffColor: Any
    outlineColor: Any
    lineColor: Any
    lineWidth: int
    horizOffset: int
    vertOffset: int
    topMargin: int
    labelFont: Any
    highlightColor: Any
    highlightWidth: int

visOpts: Any

def GetMinCanvasSize(adjList, levelList): ...
def DrawHierarchy(adjList, levelList, canvas, entryColors: Any | None = ..., bitIds: Any | None = ..., minLevel: int = ..., maxLevel: float = ...): ...
