from typing import Any

class SkeletonPoint:
    location: Any
    shapeMoments: Any
    shapeDirs: Any
    molFeatures: Any
    featmapFeatures: Any
    fracVol: float
    def __init__(self, *args, **kwargs) -> None: ...

class ShapeWithSkeleton:
    grid: Any
    skelPts: Any
    def __init__(self, *args, **kwargs) -> None: ...

class SubshapeShape:
    shapes: Any
    featMap: Any
    keyFeat: Any
    def __init__(self, *args, **kwargs) -> None: ...

def DisplaySubshapeSkeleton(viewer, shape, name, color=..., colorByOrder: bool = ...) -> None: ...
def DisplaySubshape(viewer, shape, name, showSkelPts: bool = ..., color=...) -> None: ...
