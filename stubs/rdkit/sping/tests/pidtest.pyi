from rdkit.sping.pid import *
from rdkit.sping import pagesizes as pagesizes
from typing import Any

backends: Any

def minimal(canvasClass): ...
def drawMinimal(canvas): ...
def basics(canvasClass): ...
def drawBasics(canvas): ...
def advanced(canvasClass): ...
def drawAdvanced(canvas): ...
def bluefunc(x): ...
def redfunc(x): ...
def greenfunc(x): ...
def spectrum(canvasClass): ...
def drawSpectrum(canvas): ...
def strings(canvasClass): ...
def drawStrings(canvas): ...
def CenterAndBox(canvas, s, cx: int = ..., y: int = ...) -> None: ...
def rotstring(canvasClass): ...
def drawRotstring(canvas): ...
def tkTest(testfunc): ...
def wxTest(testfunc): ...
def runtest(backend, testfunc) -> None: ...
def mainLoop(): ...

tests: Any