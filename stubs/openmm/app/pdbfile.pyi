from typing import Any

class PDBFile:
    topology: Any
    positions: Any
    def __init__(self, file, extraParticleIdentifier: str = ...) -> None: ...
    def getTopology(self): ...
    def getNumFrames(self): ...
    def getPositions(self, asNumpy: bool = ..., frame: int = ...): ...
    @staticmethod
    def writeFile(topology, positions, file=..., keepIds: bool = ..., extraParticleIdentifier: str = ...) -> None: ...
    @staticmethod
    def writeHeader(topology, file=...) -> None: ...
    @staticmethod
    def writeModel(topology, positions, file=..., modelIndex: Any | None = ..., keepIds: bool = ..., extraParticleIdentifier: str = ...) -> None: ...
    @staticmethod
    def writeFooter(topology, file=...) -> None: ...