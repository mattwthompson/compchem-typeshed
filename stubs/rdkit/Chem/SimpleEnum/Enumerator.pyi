from collections.abc import Generator
from rdkit import Chem as Chem, RDConfig as RDConfig
from rdkit.Chem import AllChem as AllChem, rdChemReactions as rdChemReactions
from typing import Any

def PreprocessReaction(reaction, funcGroupFilename: Any | None = ..., propName: str = ...): ...
def EnumerateReaction(reaction, bbLists, uniqueProductsOnly: bool = ..., funcGroupFilename=..., propName: str = ...) -> Generator[None, None, Any]: ...
