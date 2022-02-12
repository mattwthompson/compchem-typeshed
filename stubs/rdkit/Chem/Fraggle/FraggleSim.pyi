from rdkit import Chem as Chem, DataStructs as DataStructs
from rdkit.Chem import rdqueries as rdqueries
from typing import Any

rdkitFpParams: Any
FTYPE_ACYCLIC: str
FTYPE_CYCLIC: str
FTYPE_CYCLIC_ACYCLIC: str
ACYC_SMARTS: Any
CYC_SMARTS: Any
cSma1: Any
cSma2: Any
dummyAtomQuery: Any

def delete_bonds(mol, bonds, ftype, hac): ...
def select_fragments(fragments, ftype, hac): ...
def isValidRingCut(mol): ...
def generate_fraggle_fragmentation(mol, verbose: bool = ...): ...
def atomContrib(subs, mol, tverskyThresh: float = ...): ...

modified_query_fps: Any

def compute_fraggle_similarity_for_subs(inMol, qMol, qSmi, qSubs, tverskyThresh: float = ...): ...
def GetFraggleSimilarity(queryMol, refMol, tverskyThresh: float = ...): ...
