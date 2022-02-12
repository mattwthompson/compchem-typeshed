from rdkit import Chem as Chem, RDConfig as RDConfig
from rdkit.Avalon import pyAvalonTools as pyAvalonTools
from rdkit.Chem.MolKey import InchiInfo as InchiInfo
from typing import Any, NamedTuple

class MolIdentifierException(Exception): ...
class BadMoleculeException(Exception): ...

MOL_KEY_VERSION: str
ERROR_DICT: Any
INCHI_COMPUTATION_ERROR: Any
RDKIT_CONVERSION_ERROR: Any
INCHI_READWRITE_ERROR: Any
NULL_MOL: Any
BAD_SET: Any
GET_STEREO_RE: Any
NULL_SMILES_RE: Any
PATTERN_NULL_MOL: str
CHIRAL_POS: int
T_NULL_MOL: Any
stereo_code_dict: Any

def initStruchk(configDir: Any | None = ..., logFile: Any | None = ...) -> None: ...
def CheckCTAB(ctab, isSmiles: bool = ...): ...

class InchiResult(NamedTuple):
    error: Any
    inchi: Any
    fixed_ctab: Any

def GetInchiForCTAB(ctab): ...
def ErrorBitsToText(err): ...

class MolKeyResult(NamedTuple):
    mol_key: Any
    error: Any
    inchi: Any
    fixed_ctab: Any
    stereo_code: Any
    stereo_comment: Any

def GetKeyForCTAB(ctab, stereo_info: Any | None = ..., stereo_comment: Any | None = ..., logger: Any | None = ...): ...
