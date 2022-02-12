from rdkit import Chem as Chem, DataStructs as DataStructs
from rdkit.Chem import AllChem as AllChem, Draw as Draw, SDWriter as SDWriter, rdchem as rdchem
from rdkit.Chem.Scaffolds import MurckoScaffold as MurckoScaffold
from typing import Any

log: Any
pandasVersion: Any
defPandasRendering: Any
defPandasRepr: Any
highlightSubstructures: bool
molRepresentation: str
molSize: Any

def getAdjustmentAttr(): ...
def patchPandasrepr(self, **kwargs): ...
def patchPandasHTMLrepr(self, **kwargs): ...
def is_molecule_image(s): ...

class RenderMoleculeAdjustment:
    inner_adjustment: Any
    def __init__(self, inner_adjustment) -> None: ...
    def len(self, text): ...
    def justify(self, texts, max_len, mode: str = ...): ...
    def adjoin(self, space, *lists, **kwargs): ...

def PrintAsBase64PNGString(x, renderer: Any | None = ...): ...
def PrintDefaultMolRep(x): ...
def RenderImagesInAllDataFrames(images: bool = ...) -> None: ...
def AddMoleculeColumnToFrame(frame, smilesCol: str = ..., molCol: str = ..., includeFingerprints: bool = ...): ...
def ChangeMoleculeRendering(frame: Any | None = ..., renderer: str = ...) -> None: ...
def LoadSDF(filename, idName: str = ..., molColName: str = ..., includeFingerprints: bool = ..., isomericSmiles: bool = ..., smilesName: Any | None = ..., embedProps: bool = ..., removeHs: bool = ..., strictParsing: bool = ...): ...
def WriteSDF(df, out, molColName: str = ..., idName: Any | None = ..., properties: Any | None = ..., allNumeric: bool = ...) -> None: ...
def RemoveSaltsFromFrame(frame, molCol: str = ...): ...
def SaveSMILESFromFrame(frame, outFile, molCol: str = ..., NamesCol: str = ..., isomericSmiles: bool = ...) -> None: ...
def SaveXlsxFromFrame(frame, outFile, molCol: str = ..., size=...) -> None: ...
def FrameToGridImage(frame, column: str = ..., legendsCol: Any | None = ..., **kwargs): ...
def AddMurckoToFrame(frame, molCol: str = ..., MurckoCol: str = ..., Generic: bool = ...): ...
def AlignMol(mol, scaffold): ...
def AlignToScaffold(frame, molCol: str = ..., scaffoldCol: str = ...): ...
def RGroupDecompositionToFrame(groups, mols, include_core: bool = ..., redraw_sidechains: bool = ...): ...
def InstallPandasTools() -> None: ...
def UninstallPandasTools() -> None: ...