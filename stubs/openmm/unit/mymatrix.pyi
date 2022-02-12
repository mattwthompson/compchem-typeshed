from typing import Any

def eye(size): ...
def zeros(m, n: Any | None = ...): ...

class MyVector:
    data: Any
    def __init__(self, collection) -> None: ...
    def __getitem__(self, key): ...
    def __contains__(self, item): ...
    def __delitem__(self, key) -> None: ...
    def __iter__(self): ...
    def __len__(self): ...
    def __setitem__(self, key, value) -> None: ...
    def __rmul__(self, lhs): ...

class MyMatrix(MyVector):
    def numRows(self): ...
    def numCols(self): ...
    def __len__(self): ...
    def is_square(self): ...
    def __iter__(self): ...
    def __getitem__(self, m): ...
    def __setitem__(self, key, rhs) -> None: ...
    def __mul__(self, rhs): ...
    def __add__(self, rhs): ...
    def __sub__(self, rhs): ...
    def __pos__(self): ...
    def __neg__(self): ...
    def __invert__(self): ...
    def transpose(self): ...

class MyMatrixTranspose(MyMatrix):
    def transpose(self): ...
    def numRows(self): ...
    def numCols(self): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, rhs) -> None: ...
