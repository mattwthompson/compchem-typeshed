from typing import Any

class MCSResult:
    numAtoms: Any
    numBonds: Any
    smarts: Any
    completed: Any
    def __init__(self, obj) -> None: ...
    def __nonzero__(self): ...

def FindMCS(mols, minNumAtoms: int = ..., maximize=..., atomCompare=..., bondCompare=..., matchValences=..., ringMatchesRingOnly: bool = ..., completeRingsOnly: bool = ..., timeout=..., threshold: Any | None = ...): ...
