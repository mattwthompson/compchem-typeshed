from rdkit.DataStructs.VectCollection import VectCollection as VectCollection
from rdkit.ML import InfoTheory as InfoTheory
from rdkit.ML.DecTree import SigTree as SigTree
from rdkit.ML.FeatureSelect import CMIM as CMIM
from typing import Any

def BuildSigTree(examples, nPossibleRes, ensemble: Any | None = ..., random: int = ..., metric=..., biasList=..., depth: int = ..., maxDepth: int = ..., useCMIM: int = ..., allowCollections: bool = ..., verbose: int = ..., **kwargs): ...
def SigTreeBuilder(examples, attrs, nPossibleVals, initialVar: Any | None = ..., ensemble: Any | None = ..., randomDescriptors: int = ..., **kwargs): ...
