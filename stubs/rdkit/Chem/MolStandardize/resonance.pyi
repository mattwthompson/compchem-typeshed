from rdkit import Chem as Chem
from typing import Any

log: Any
MAX_STRUCTURES: int

class ResonanceEnumerator:
    kekule_all: Any
    allow_incomplete_octets: Any
    unconstrained_cations: Any
    unconstrained_anions: Any
    allow_charge_separation: Any
    max_structures: Any
    def __init__(self, kekule_all: bool = ..., allow_incomplete_octets: bool = ..., unconstrained_cations: bool = ..., unconstrained_anions: bool = ..., allow_charge_separation: bool = ..., max_structures=...) -> None: ...
    def __call__(self, mol): ...
    def enumerate(self, mol): ...

def enumerate_resonance_smiles(smiles): ...
