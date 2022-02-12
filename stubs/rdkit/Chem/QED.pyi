from rdkit import Chem as Chem
from rdkit.Chem import Crippen as Crippen, MolSurf as MolSurf
from rdkit.Chem.ChemUtils.DescriptorUtilities import setDescriptorVersion as setDescriptorVersion
from typing import Any, NamedTuple

class QEDproperties(NamedTuple):
    MW: Any
    ALOGP: Any
    HBA: Any
    HBD: Any
    PSA: Any
    ROTB: Any
    AROM: Any
    ALERTS: Any

class ADSparameter(NamedTuple):
    A: Any
    B: Any
    C: Any
    D: Any
    E: Any
    F: Any
    DMAX: Any
WEIGHT_MAX: Any
WEIGHT_MEAN: Any
WEIGHT_NONE: Any
AliphaticRings: Any
AcceptorSmarts: Any
Acceptors: Any
StructuralAlertSmarts: Any
StructuralAlerts: Any
adsParameters: Any

def ads(x, adsParameter): ...
def properties(mol): ...
def qed(mol, w=..., qedProperties: Any | None = ...): ...
def weights_max(mol): ...
def weights_mean(mol): ...
def weights_none(mol): ...
def default(mol): ...
