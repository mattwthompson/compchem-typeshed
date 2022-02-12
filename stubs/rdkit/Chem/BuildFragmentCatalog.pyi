from rdkit import RDConfig as RDConfig
from rdkit.Chem import FragmentCatalog as FragmentCatalog
from rdkit.Dbase.DbConnection import DbConnect as DbConnect
from rdkit.ML import InfoTheory as InfoTheory
from typing import Any

def message(msg, dest=...) -> None: ...
def BuildCatalog(suppl, maxPts: int = ..., groupFileName: Any | None = ..., minPath: int = ..., maxPath: int = ..., reportFreq: int = ...): ...
def ScoreMolecules(suppl, catalog, maxPts: int = ..., actName: str = ..., acts: Any | None = ..., nActs: int = ..., reportFreq: int = ...): ...
def ScoreFromLists(bitLists, suppl, catalog, maxPts: int = ..., actName: str = ..., acts: Any | None = ..., nActs: int = ..., reportFreq: int = ...): ...
def CalcGains(suppl, catalog, topN: int = ..., actName: str = ..., acts: Any | None = ..., nActs: int = ..., reportFreq: int = ..., biasList: Any | None = ..., collectFps: int = ...): ...
def CalcGainsFromFps(suppl, fps, topN: int = ..., actName: str = ..., acts: Any | None = ..., nActs: int = ..., reportFreq: int = ..., biasList: Any | None = ...): ...
def OutputGainsData(outF, gains, cat, nActs: int = ...) -> None: ...
def ProcessGainsData(inF, delim: str = ..., idCol: int = ..., gainCol: int = ...): ...
def ShowDetails(catalog, gains, nToDo: int = ..., outF=..., idCol: int = ..., gainCol: int = ..., outDelim: str = ...) -> None: ...
def SupplierFromDetails(details): ...
def Usage() -> None: ...

class RunDetails:
    numMols: int
    doBuild: int
    doSigs: int
    doScore: int
    doGains: int
    doDetails: int
    catalogName: Any
    onBitsName: Any
    scoresName: Any
    gainsName: Any
    dbName: str
    tableName: Any
    detailsName: Any
    inFileName: Any
    fpName: Any
    minPath: int
    maxPath: int
    smiCol: int
    actCol: int
    nameCol: int
    hasTitle: int
    nActs: int
    nBits: int
    delim: str
    biasList: Any
    topN: int

def ParseArgs(details) -> None: ...
