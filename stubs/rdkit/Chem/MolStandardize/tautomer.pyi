from .utils import memoized_property as memoized_property, pairwise as pairwise
from rdkit import Chem as Chem
from rdkit.Chem.rdchem import BondDir as BondDir, BondStereo as BondStereo, BondType as BondType
from typing import Any

log: Any

class TautomerTransform:
    BONDMAP: Any
    CHARGEMAP: Any
    name: Any
    tautomer_str: Any
    bonds: Any
    charges: Any
    def __init__(self, name, smarts, bonds=..., charges=..., radicals=...) -> None: ...
    def tautomer(self): ...

class TautomerScore:
    name: Any
    smarts_str: Any
    score: Any
    def __init__(self, name, smarts, score) -> None: ...
    def smarts(self): ...

TAUTOMER_TRANSFORMS: Any
TAUTOMER_SCORES: Any
MAX_TAUTOMERS: int

class TautomerCanonicalizer:
    transforms: Any
    scores: Any
    max_tautomers: Any
    def __init__(self, transforms=..., scores=..., max_tautomers=...) -> None: ...
    def __call__(self, mol): ...
    def canonicalize(self, mol): ...

class TautomerEnumerator:
    transforms: Any
    max_tautomers: Any
    def __init__(self, transforms=..., max_tautomers=...) -> None: ...
    def __call__(self, mol): ...
    def enumerate(self, mol): ...
