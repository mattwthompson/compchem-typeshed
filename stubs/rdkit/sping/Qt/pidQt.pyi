from qt import *
from qtcanvas import *
from math import *
from rdkit.sping import pid as pid
from typing import Any

class QCanvasRotText(QCanvasText):
    def __init__(self, txt, canvas, angle: int = ...) -> None: ...
    def draw(self, qP) -> None: ...

class QtCanvas(pid.Canvas):
    size: Any
    objs: Any
    nObjs: int
    def __init__(self, destCanvas, size=..., name: str = ...) -> None: ...
    def clear(self) -> None: ...
    def flush(self) -> None: ...
    def save(self, file: Any | None = ..., format: Any | None = ...) -> None: ...
    def drawLine(self, x1, y1, x2, y2, color: Any | None = ..., width: Any | None = ..., dash: Any | None = ..., **kwargs) -> None: ...
    def drawPolygon(self, pointlist, edgeColor: Any | None = ..., edgeWidth: Any | None = ..., fillColor=..., closed: int = ..., dash: Any | None = ..., **kwargs) -> None: ...
    def drawString(self, s, x, y, font: Any | None = ..., color: Any | None = ..., angle: int = ..., **kwargs) -> None: ...
    def drawImage(self, image, x1, y1, x2: Any | None = ..., y2: Any | None = ..., **kwargs) -> None: ...
    def stringWidth(self, s, font: Any | None = ...): ...
    def fontAscent(self, font: Any | None = ...): ...
    def fontDescent(self, font: Any | None = ...): ...

def test(canvas): ...
def dashtest(canvas): ...
