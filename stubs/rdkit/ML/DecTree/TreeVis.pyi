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
    labelFont: Any
    highlightColor: Any
    highlightWidth: int

visOpts: Any

def CalcTreeNodeSizes(node) -> None: ...
def SetNodeScales(node) -> None: ...
def DrawTreeNode(node, loc, canvas, nRes: int = ..., scaleLeaves: bool = ..., showPurity: bool = ...) -> None: ...
def CalcTreeWidth(tree): ...
def DrawTree(tree, canvas, nRes: int = ..., scaleLeaves: bool = ..., allowShrink: bool = ..., showPurity: bool = ...) -> None: ...
def ResetTree(tree) -> None: ...
