from rdkit import Geometry as Geometry, RDConfig as RDConfig
from typing import Any

logger: Any
BEGIN: int
END: int
TRIANGLE_FAN: int
COLOR: int
VERTEX: int
NORMAL: int
SPHERE: int
CYLINDER: int
ALPHA: int

def ShowArrow(viewer, tail, head, radius, color, label, transparency: int = ..., includeArrowhead: bool = ...) -> None: ...
def ShowMolFeats(mol, factory, viewer, radius: float = ..., confId: int = ..., showOnly: bool = ..., name: str = ..., transparency: float = ..., colors: Any | None = ..., excludeTypes=..., useFeatDirs: bool = ..., featLabel: Any | None = ..., dirLabel: Any | None = ..., includeArrowheads: bool = ..., writeFeats: bool = ..., showMol: bool = ..., featMapFile: bool = ...) -> None: ...

parser: Any
