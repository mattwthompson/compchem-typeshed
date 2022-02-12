from typing import Any

def setDescriptorVersion(version: str = ...): ...

class VectorDescriptorNamespace(dict):
    def __init__(self, **kwargs) -> None: ...

class VectorDescriptorWrapper:
    func: Any
    names: Any
    func_key: Any
    namespace: Any
    def __init__(self, func, names, version, namespace): ...
    def call_desc(self, mol, index): ...
