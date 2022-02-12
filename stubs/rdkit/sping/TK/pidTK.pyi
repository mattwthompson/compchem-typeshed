import Tkinter
import rdkit.sping.PIL
from typing import Any

tk = Tkinter
__date__: str

class FontManager:
    master: Any
    font_cache: Any
    def __init__(self, master) -> None: ...
    def stringWidth(self, s, font): ...
    def fontHeight(self, font): ...
    def fontAscent(self, font): ...
    def fontDescent(self, font): ...
    def getTkFontString(self, font): ...
    def getTkFontName(self, font): ...
    def piddleToTkFont(self, font): ...

class TKCanvas(tk.Canvas, rdkit.sping.pid.Canvas):
    def __init__(self, size=..., name: str = ..., master: Any | None = ..., scrollingViewPortSize: Any | None = ..., **kw) -> None: ...
    def isInteractive(self): ...
    def onOver(self, event) -> None: ...
    def onClick(self, event) -> None: ...
    def onKey(self, event) -> None: ...
    def flush(self) -> None: ...
    def clear(self) -> None: ...
    def drawLine(self, x1, y1, x2, y2, color: Any | None = ..., width: Any | None = ...) -> None: ...
    def stringWidth(self, s, font: Any | None = ...): ...
    def fontAscent(self, font: Any | None = ...): ...
    def fontDescent(self, font: Any | None = ...): ...
    def drawString(self, s, x, y, font: Any | None = ..., color: Any | None = ..., angle: Any | None = ...) -> None: ...
    def drawRect(self, x1, y1, x2, y2, edgeColor: Any | None = ..., edgeWidth: Any | None = ..., fillColor: Any | None = ...) -> None: ...
    def drawEllipse(self, x1, y1, x2, y2, edgeColor: Any | None = ..., edgeWidth: Any | None = ..., fillColor: Any | None = ...) -> None: ...
    def drawArc(self, x1, y1, x2, y2, startAng: int = ..., extent: int = ..., edgeColor: Any | None = ..., edgeWidth: Any | None = ..., fillColor: Any | None = ...) -> None: ...
    def drawPolygon(self, pointlist, edgeColor: Any | None = ..., edgeWidth: Any | None = ..., fillColor: Any | None = ..., closed: int = ...) -> None: ...
    def drawImage(self, image, x1, y1, x2: Any | None = ..., y2: Any | None = ...) -> None: ...

class TKCanvasPIL(rdkit.sping.PIL.PILCanvas):
    def __init__(self, size=..., name: str = ..., master: Any | None = ..., **kw) -> None: ...
    def flush(self) -> None: ...
    def getTKCanvas(self): ...
