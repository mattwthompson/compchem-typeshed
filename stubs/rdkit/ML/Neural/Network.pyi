from rdkit.ML.Neural import ActFuncs as ActFuncs, NetNode as NetNode
from typing import Any

class Network:
    def ConstructRandomWeights(self, minWeight: int = ..., maxWeight: int = ...) -> None: ...
    nConnections: Any
    def FullyConnectNodes(self) -> None: ...
    nodeCounts: Any
    numInputNodes: Any
    numOutputNodes: Any
    numHiddenLayers: Any
    numInHidden: Any
    nodeList: Any
    layerIndices: Any
    def ConstructNodes(self, nodeCounts, actFunc, actFuncParms) -> None: ...
    def GetInputNodeList(self): ...
    def GetOutputNodeList(self): ...
    def GetHiddenLayerNodeList(self, which): ...
    def GetNumNodes(self): ...
    def GetNumHidden(self): ...
    def GetNode(self, which): ...
    def GetAllNodes(self): ...
    lastResults: Any
    def ClassifyExample(self, example, appendExamples: int = ...): ...
    def GetLastOutputs(self): ...
    def __init__(self, nodeCounts, nodeConnections: Any | None = ..., actFunc=..., actFuncParms=..., weightBounds: int = ...) -> None: ...
