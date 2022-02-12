from rdkit import Chem as Chem, Geometry as Geometry, RDConfig as RDConfig, rdBase as rdBase
from rdkit.Chem import rdMolDescriptors as rdMolDescriptors, rdchem as rdchem
from typing import Any

def CalculateTorsionLists(mol, maxDev: str = ..., symmRadius: int = ..., ignoreColinearBonds: bool = ...): ...
def CalculateTorsionAngles(mol, tors_list, tors_list_rings, confId: int = ...): ...
def CalculateTorsionWeights(mol, aid1: int = ..., aid2: int = ..., ignoreColinearBonds: bool = ...): ...
def CalculateTFD(torsions1, torsions2, weights: Any | None = ...): ...
def GetTFDBetweenConformers(mol, confIds1, confIds2, useWeights: bool = ..., maxDev: str = ..., symmRadius: int = ..., ignoreColinearBonds: bool = ...): ...
def GetTFDBetweenMolecules(mol1, mol2, confId1: int = ..., confId2: int = ..., useWeights: bool = ..., maxDev: str = ..., symmRadius: int = ..., ignoreColinearBonds: bool = ...): ...
def GetTFDMatrix(mol, useWeights: bool = ..., maxDev: str = ..., symmRadius: int = ..., ignoreColinearBonds: bool = ...): ...