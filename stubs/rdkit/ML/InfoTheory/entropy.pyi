from typing import Any

hascEntropy: int

def PyInfoEntropy(results): ...
def PyInfoGain(varMat): ...

InfoEntropy: Any
InfoGain: Any
InfoEntropy = PyInfoEntropy
InfoGain = PyInfoGain
