from .utils import memoized_property as memoized_property
from rdkit import Chem as Chem
from rdkit.Chem import rdMolDescriptors as rdMolDescriptors
from typing import Any

log: Any

class FragmentPattern:
    name: Any
    smarts_str: Any
    def __init__(self, name, smarts) -> None: ...
    def smarts(self): ...

REMOVE_FRAGMENTS: Any
LEAVE_LAST: bool
PREFER_ORGANIC: bool

def is_organic(fragment): ...

class FragmentRemover:
    fragments: Any
    leave_last: Any
    def __init__(self, fragments=..., leave_last=...) -> None: ...
    def __call__(self, mol): ...
    def remove(self, mol): ...

class LargestFragmentChooser:
    prefer_organic: Any
    def __init__(self, prefer_organic=...) -> None: ...
    def __call__(self, mol): ...
    def choose(self, mol): ...
