from qt import *
from typing import Any

class ChemdrawPanel(QWidget):
    cdx: Any
    offset: int
    label: Any
    def __init__(self, parent: Any | None = ..., name: str = ..., readOnly: int = ..., size=...) -> None: ...
    def pullData(self, fmt: str = ...): ...
    def setData(self, data, fmt: str = ...): ...
    def resizeEvent(self, evt) -> None: ...
    def __del__(self) -> None: ...
