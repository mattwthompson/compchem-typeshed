from typing import Any

class CanvasBase:
    def addCanvasLine(self, p1, p2, color=..., color2: Any | None = ..., **kwargs) -> None: ...
    def addCanvasText(self, text, pos, font, color=..., **kwargs) -> None: ...
    def addCanvasPolygon(self, ps, color=..., **kwargs) -> None: ...
    def addCanvasDashedWedge(self, p1, p2, p3, dash=..., color=..., color2: Any | None = ..., **kwargs) -> None: ...
    def flush(self) -> None: ...