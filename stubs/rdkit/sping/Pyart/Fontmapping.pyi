from typing import Any

DefaultFace: str
PidLegalFonts: Any
Roman: str
Bold: str
Italic: str
BoldItalic: str
MapPid2PyartFontName: Any

def getPyartName(pidfont): ...
getPdfName = getPyartName
