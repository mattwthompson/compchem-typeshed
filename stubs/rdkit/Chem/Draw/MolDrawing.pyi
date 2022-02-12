from rdkit import Chem as Chem
from typing import Any

def cmp(t1, t2): ...

periodicTable: Any

class Font:
    face: Any
    size: Any
    weight: Any
    name: Any
    def __init__(self, face: Any | None = ..., size: Any | None = ..., name: Any | None = ..., weight: Any | None = ...) -> None: ...

class DrawingOptions:
    dotsPerAngstrom: int
    useFraction: float
    atomLabelFontFace: str
    atomLabelFontSize: int
    atomLabelMinFontSize: int
    atomLabelDeuteriumTritium: bool
    bondLineWidth: float
    dblBondOffset: float
    dblBondLengthFrac: float
    defaultColor: Any
    selectColor: Any
    bgColor: Any
    colorBonds: bool
    noCarbonSymbols: bool
    includeAtomNumbers: bool
    atomNumberOffset: int
    radicalSymbol: str
    dash: Any
    wedgeDashedBonds: bool
    showUnknownDoubleBonds: bool
    coordScale: float
    elemDict: Any

class MolDrawing:
    canvas: Any
    canvasSize: Any
    drawingOptions: Any
    atomPs: Any
    boundingBoxes: Any
    def __init__(self, canvas: Any | None = ..., drawingOptions: Any | None = ...) -> None: ...
    def transformPoint(self, pos): ...
    molTrans: Any
    currAtomLabelFontSize: Any
    drawingTrans: Any
    def scaleAndCenter(self, mol, conf, coordCenter: bool = ..., canvasSize: Any | None = ..., ignoreHs: bool = ...) -> None: ...
    currDotsPerAngstrom: Any
    activeMol: Any
    bondRings: Any
    def AddMol(self, mol, centerIt: bool = ..., molTrans: Any | None = ..., drawingTrans: Any | None = ..., highlightAtoms=..., confId: int = ..., flagCloseContactsDist: int = ..., highlightMap: Any | None = ..., ignoreHs: bool = ..., highlightBonds=..., **kwargs) -> None: ...
