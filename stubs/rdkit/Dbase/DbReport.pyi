from rdkit import Chem as Chem
from rdkit.Chem import rdDepictor as rdDepictor
from rdkit.Chem.Draw import DrawUtils as DrawUtils
from rdkit.Chem.Draw.MolDrawing import DrawingOptions as DrawingOptions, MolDrawing as MolDrawing
from rdkit.Dbase import DbInfo as DbInfo
from rdkit.Dbase.DbConnection import DbConnect as DbConnect
from rdkit.Reports.PDFReport import PDFReport as PDFReport, ReportUtils as ReportUtils
from rdkit.utils import cactvs as cactvs
from typing import Any

GetReportlabTable: Any
QuickReport: Any
hasCDX: int

class CDXImageTransformer:
    smiCol: Any
    tempHandler: Any
    width: Any
    verbose: Any
    def __init__(self, smiCol, width: int = ..., verbose: int = ..., tempHandler: Any | None = ...) -> None: ...
    def __call__(self, arg): ...

class CactvsImageTransformer:
    smiCol: Any
    tempHandler: Any
    width: Any
    verbose: Any
    def __init__(self, smiCol, width: float = ..., verbose: int = ..., tempHandler: Any | None = ...) -> None: ...
    def __call__(self, arg): ...

class ReportLabImageTransformer:
    smiCol: Any
    width: Any
    verbose: Any
    def __init__(self, smiCol, width: float = ..., verbose: int = ..., tempHandler: Any | None = ...) -> None: ...
    def __call__(self, arg): ...

class RDImageTransformer:
    smiCol: Any
    tempHandler: Any
    width: Any
    verbose: Any
    def __init__(self, smiCol, width: float = ..., verbose: int = ..., tempHandler: Any | None = ...) -> None: ...
    def __call__(self, arg): ...
