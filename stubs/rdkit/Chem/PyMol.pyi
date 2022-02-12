from rdkit import Chem as Chem
from typing import Any

class MolViewer:
    server: Any
    def __init__(self, host: Any | None = ..., port: int = ..., force: int = ..., **kwargs) -> None: ...
    def InitializePyMol(self) -> None: ...
    def DeleteAll(self) -> None: ...
    def DeleteAllExcept(self, excludes) -> None: ...
    def LoadFile(self, filename, name, showOnly: bool = ...): ...
    def ShowMol(self, mol, name: str = ..., showOnly: bool = ..., highlightFeatures=..., molB: str = ..., confId: int = ..., zoom: bool = ..., forcePDB: bool = ..., showSticks: bool = ...): ...
    def GetSelectedAtoms(self, whichSelection: Any | None = ...): ...
    def SelectAtoms(self, itemId, atomIndices, selName: str = ...) -> None: ...
    def HighlightAtoms(self, indices, where, extraHighlight: bool = ...) -> None: ...
    def SetDisplayStyle(self, obj, style: str = ...) -> None: ...
    def SelectProteinNeighborhood(self, aroundObj, inObj, distance: float = ..., name: str = ..., showSurface: bool = ...) -> None: ...
    def AddPharmacophore(self, locs, colors, label, sphereRad: float = ...) -> None: ...
    def SetDisplayUpdate(self, val) -> None: ...
    def GetAtomCoords(self, sels): ...
    def HideAll(self) -> None: ...
    def HideObject(self, objName) -> None: ...
    def DisplayObject(self, objName) -> None: ...
    def Redraw(self) -> None: ...
    def Zoom(self, objName) -> None: ...
    def DisplayHBonds(self, objName, molName, proteinName, molSelText: str = ..., proteinSelText: str = ...) -> None: ...
    def DisplayCollisions(self, objName, molName, proteinName, distCutoff: float = ..., color: str = ..., molSelText: str = ..., proteinSelText: str = ...) -> None: ...
    def SaveFile(self, filename) -> None: ...
    def GetPNG(self, h: Any | None = ..., w: Any | None = ..., preDelay: int = ...): ...