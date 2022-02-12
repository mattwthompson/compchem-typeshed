from rdkit.Chem.Draw.canvasbase import CanvasBase as CanvasBase
from typing import Any

have_cairocffi: bool
have_pango: bool
ffi: Any
defaultLibs: Any
envVar: Any
envVarSet: bool
libName: Any
libPath: Any
importError: bool
scriptPattern: Any

class Canvas(CanvasBase):
    image: Any
    imageType: Any
    ctx: Any
    size: Any
    surface: Any
    fileName: Any
    def __init__(self, image: Any | None = ..., size: Any | None = ..., ctx: Any | None = ..., imageType: Any | None = ..., fileName: Any | None = ...) -> None: ...
    def flush(self): ...
    def addCanvasLine(self, p1, p2, color=..., color2: Any | None = ..., **kwargs) -> None: ...
    def addCanvasText(self, text, pos, font, color=..., **kwargs): ...
    def addCanvasPolygon(self, ps, color=..., fill: bool = ..., stroke: bool = ..., **kwargs) -> None: ...
    def addCanvasDashedWedge(self, p1, p2, p3, dash=..., color=..., color2: Any | None = ..., **kwargs) -> None: ...
    def addCircle(self, center, radius, color=..., fill: bool = ..., stroke: bool = ..., alpha: float = ..., **kwargs) -> None: ...
