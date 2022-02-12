from collections.abc import Generator
from rdkit import Chem as Chem
from rdkit.Chem import AllChem as AllChem
from typing import Any

def GetHeterocycleReactionSmarts(): ...

REACTION_CACHE: Any

def GetHeterocycleReactions(): ...
def EnumerateHeterocycles(inputmol, depth: Any | None = ...) -> Generator[Any, None, None]: ...
