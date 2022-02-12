from rdkit.sping.pid import *
from rdkit.sping.PDF import pdfmetrics as pdfmetrics
from typing import Any

class PyartCanvas(Canvas):
    filename: Any
    def __init__(self, size=..., name: str = ...) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    def clear(self) -> None: ...
    def flush(self) -> None: ...
    def save(self, file: Any | None = ..., format: Any | None = ...) -> None: ...
    def stringWidth(self, s, font: Any | None = ...): ...
    def fontAscent(self, font: Any | None = ...): ...
    def fontDescent(self, font: Any | None = ...): ...
    def drawLine(self, x1, y1, x2, y2, color: Any | None = ..., width: Any | None = ...) -> None: ...
    def drawString(self, s, x, y, font: Any | None = ..., color: Any | None = ..., angle: int = ...) -> None: ...
    def drawPolygon(self, pointlist, edgeColor: Any | None = ..., edgeWidth: Any | None = ..., fillColor: Any | None = ..., closed: int = ...) -> None: ...
