from typing import Any

class Trainer: ...

class BackProp(Trainer):
    oldDeltaW: Any
    def StepUpdate(self, example, net, resVect: Any | None = ...): ...
    def TrainOnLine(self, examples, net, maxIts: int = ..., errTol: float = ..., useAvgErr: int = ..., silent: int = ...) -> None: ...
    speed: Any
    momentum: Any
    def __init__(self, speed: float = ..., momentum: float = ...) -> None: ...
