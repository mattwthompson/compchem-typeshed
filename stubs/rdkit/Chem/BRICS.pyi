from collections.abc import Generator
from rdkit import Chem as Chem
from typing import Any

environs: Any
reactionDefs: Any
smartsGps: Any
g1: Any
g2: Any
bnd: Any
r1: Any
r2: Any
sma: Any
t: Any
environMatchers: Any
bondMatchers: Any
tmp: Any
e1: Any
e2: Any
patt: Any
reactions: Any
reverseReactions: Any
rs: Any
ps: Any
rxn: Any
labels: Any

def FindBRICSBonds(mol, randomizeOrder: bool = ..., silent: bool = ...) -> Generator[Any, None, None]: ...
def BreakBRICSBonds(mol, bonds: Any | None = ..., sanitize: bool = ..., silent: bool = ...): ...
def BRICSDecompose(mol, allNodes: Any | None = ..., minFragmentSize: int = ..., onlyUseReactions: Any | None = ..., silent: bool = ..., keepNonLeafNodes: bool = ..., singlePass: bool = ..., returnMols: bool = ...): ...

dummyPattern: Any

def BRICSBuild(fragments, onlyCompleteMols: bool = ..., seeds: Any | None = ..., uniquify: bool = ..., scrambleReagents: bool = ..., maxDepth: int = ...) -> Generator[Any, None, None]: ...
