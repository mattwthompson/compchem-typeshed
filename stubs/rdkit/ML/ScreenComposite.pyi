from rdkit import DataStructs as DataStructs
from rdkit.Dbase import DbModule as DbModule
from rdkit.Dbase.DbConnection import DbConnect as DbConnect
from rdkit.ML import CompositeRun as CompositeRun
from rdkit.ML.Data import DataUtils as DataUtils, SplitData as SplitData
from typing import Any

hasPil: int

def message(msg, noRet: int = ...) -> None: ...
def error(msg) -> None: ...
def CalcEnrichment(mat, tgt: int = ...): ...
def CollectResults(indices, dataSet, composite, callback: Any | None = ..., appendExamples: int = ..., errorEstimate: int = ...): ...
def DetailedScreen(indices, data, composite, threshold: int = ..., screenResults: Any | None = ..., goodVotes: Any | None = ..., badVotes: Any | None = ..., noVotes: Any | None = ..., callback: Any | None = ..., appendExamples: int = ..., errorEstimate: int = ...) -> None: ...
def ShowVoteResults(indices, data, composite, nResultCodes, threshold, verbose: int = ..., screenResults: Any | None = ..., callback: Any | None = ..., appendExamples: int = ..., goodVotes: Any | None = ..., badVotes: Any | None = ..., noVotes: Any | None = ..., errorEstimate: int = ...): ...
def ScreenIt(composite, indices, data, partialVote: int = ..., voteTol: float = ..., verbose: int = ..., screenResults: Any | None = ..., goodVotes: Any | None = ..., badVotes: Any | None = ..., noVotes: Any | None = ...): ...
def PrepareDataFromDetails(model, details, data, verbose: int = ...): ...
def ScreenFromDetails(models, details, callback: Any | None = ..., setup: Any | None = ..., appendExamples: int = ..., goodVotes: Any | None = ..., badVotes: Any | None = ..., noVotes: Any | None = ..., data: Any | None = ..., enrichments: Any | None = ...): ...
def GetScreenImage(nGood, nBad, nRej, size: Any | None = ...): ...
def ScreenToHtml(nGood, nBad, nRej, avgGood, avgBad, avgSkip, voteTable, imgDir: str = ..., fullPage: int = ..., skipImg: int = ..., includeDefs: int = ...): ...
def MakePredPlot(details, indices, data, goodVotes, badVotes, nRes, idCol: int = ..., verbose: int = ...) -> None: ...
def Go(details) -> None: ...
def SetDefaults(details: Any | None = ...): ...
def Usage() -> None: ...
def ShowVersion(includeArgs: int = ...) -> None: ...
def ParseArgs(details): ...