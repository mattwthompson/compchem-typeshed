from .utils import memoized_property as memoized_property
from rdkit import Chem as Chem
from rdkit.Chem import AllChem as AllChem
from typing import Any

log: Any

class Normalization:
    name: Any
    transform_str: Any
    def __init__(self, name, transform) -> None: ...
    def transform(self): ...

NORMALIZATIONS: Any
MAX_RESTARTS: int

class Normalizer:
    normalizations: Any
    max_restarts: Any
    def __init__(self, normalizations=..., max_restarts=...) -> None: ...
    def __call__(self, mol): ...
    def normalize(self, mol): ...
