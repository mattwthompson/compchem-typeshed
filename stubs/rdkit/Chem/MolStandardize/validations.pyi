from .errors import StopValidateError as StopValidateError
from .fragment import REMOVE_FRAGMENTS as REMOVE_FRAGMENTS
from rdkit import Chem as Chem
from typing import Any

class Validation:
    log: Any
    def __init__(self, log) -> None: ...
    def __call__(self, mol) -> None: ...
    def run(self, mol) -> None: ...

class SmartsValidation(Validation):
    level: Any
    message: str
    entire_fragment: bool
    def __init__(self, log) -> None: ...
    @property
    def smarts(self) -> None: ...
    def run(self, mol) -> None: ...

class IsNoneValidation(Validation):
    def run(self, mol) -> None: ...

class NoAtomValidation(Validation):
    def run(self, mol) -> None: ...

class DichloroethaneValidation(SmartsValidation):
    level: Any
    smarts: str
    entire_fragment: bool
    message: str

class FragmentValidation(Validation):
    fragments: Any
    def run(self, mol) -> None: ...

class NeutralValidation(Validation):
    def run(self, mol) -> None: ...

class IsotopeValidation(Validation):
    def run(self, mol) -> None: ...

VALIDATIONS: Any
