from .baseunit import BaseUnit as BaseUnit
from .unit import ScaledUnit as ScaledUnit, Unit as Unit
from typing import Any

class SiPrefix:
    prefix: Any
    factor: Any
    symbol: Any
    def __init__(self, prefix, factor, symbol) -> None: ...
    def __mul__(self, unit): ...

yotto: Any
zepto: Any
atto: Any
femto: Any
pico: Any
nano: Any
micro: Any
milli: Any
centi: Any
deci: Any
deka: Any
deca: Any
hecto: Any
kilo: Any
mega: Any
giga: Any
tera: Any
peta: Any
exa: Any
zetta: Any
yotta: Any
si_prefixes: Any

def define_prefixed_units(base_unit, module=...) -> None: ...

kibi: Any
mebi: Any
gibi: Any
tebi: Any
pebi: Any
exbi: Any
zebi: Any
yobi: Any
binary_prefixes: Any
