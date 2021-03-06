from rdkit.Chem.Draw.rdMolDraw2D import *
from rdkit import Chem as Chem, RDConfig as RDConfig, rdBase as rdBase
from rdkit.Chem import rdDepictor as rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D as rdMolDraw2D
from rdkit.Chem.Draw.MolDrawing import DrawingOptions as DrawingOptions, MolDrawing as MolDrawing
from typing import Any, NamedTuple

def MolDraw2DFromQPainter(qpainter, width: int = ..., height: int = ..., panelWidth: int = ..., panelHeight: int = ...): ...
def MolToImage(mol, size=..., kekulize: bool = ..., wedgeBonds: bool = ..., fitImage: bool = ..., options: Any | None = ..., canvas: Any | None = ..., **kwargs): ...
def MolToFile(mol, filename, size=..., kekulize: bool = ..., wedgeBonds: bool = ..., imageType: Any | None = ..., fitImage: bool = ..., options: Any | None = ..., **kwargs) -> None: ...
def MolToImageFile(mol, filename, size=..., kekulize: bool = ..., wedgeBonds: bool = ..., **kwargs) -> None: ...
def ShowMol(mol, size=..., kekulize: bool = ..., wedgeBonds: bool = ..., title: str = ..., stayInFront: bool = ..., **kwargs) -> None: ...
def MolToMPL(mol, size=..., kekulize: bool = ..., wedgeBonds: bool = ..., imageType: Any | None = ..., fitImage: bool = ..., options: Any | None = ..., **kwargs): ...
def calcAtomGaussians(mol, a: float = ..., step: float = ..., weights: Any | None = ...): ...
def MolsToImage(mols, subImgSize=..., legends: Any | None = ..., **kwargs): ...
def MolsToGridImage(mols, molsPerRow: int = ..., subImgSize=..., legends: Any | None = ..., highlightAtomLists: Any | None = ..., highlightBondLists: Any | None = ..., useSVG: bool = ..., returnPNG: bool = ..., **kwargs): ...
def ReactionToImage(rxn, subImgSize=..., useSVG: bool = ..., drawOptions: Any | None = ..., returnPNG: bool = ..., **kwargs): ...
def MolToQPixmap(mol, size=..., kekulize: bool = ..., wedgeBonds: bool = ..., fitImage: bool = ..., options: Any | None = ..., **kwargs): ...
def DrawMorganBit(mol, bitId, bitInfo, whichExample: int = ..., **kwargs): ...
def DrawMorganBits(tpls, **kwargs): ...

class FingerprintEnv(NamedTuple):
    submol: Any
    highlightAtoms: Any
    atomColors: Any
    highlightBonds: Any
    bondColors: Any
    highlightRadii: Any

def DrawMorganEnvs(envs, molsPerRow: int = ..., subImgSize=..., baseRad: float = ..., useSVG: bool = ..., aromaticColor=..., ringColor=..., centerColor=..., extraColor=..., legends: Any | None = ..., drawOptions: Any | None = ..., **kwargs): ...
def DrawMorganEnv(mol, atomId, radius, molSize=..., baseRad: float = ..., useSVG: bool = ..., aromaticColor=..., ringColor=..., centerColor=..., extraColor=..., drawOptions: Any | None = ..., **kwargs): ...
def DrawRDKitBits(tpls, **kwargs): ...
def DrawRDKitBit(mol, bitId, bitInfo, whichExample: int = ..., **kwargs): ...
def DrawRDKitEnvs(envs, molsPerRow: int = ..., subImgSize=..., baseRad: float = ..., useSVG: bool = ..., aromaticColor=..., extraColor=..., nonAromaticColor: Any | None = ..., legends: Any | None = ..., drawOptions: Any | None = ..., **kwargs): ...
def DrawRDKitEnv(mol, bondPath, molSize=..., baseRad: float = ..., useSVG: bool = ..., aromaticColor=..., extraColor=..., nonAromaticColor: Any | None = ..., drawOptions: Any | None = ..., **kwargs): ...
def SetComicMode(opts) -> None: ...
