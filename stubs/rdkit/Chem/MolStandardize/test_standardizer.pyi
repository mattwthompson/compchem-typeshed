import unittest
from rdkit import Chem as Chem
from rdkit.Chem.MolStandardize.standardize import Standardizer as Standardizer

class FakeStandardizer(Standardizer):
    def normalize(self): ...

class TestCase(unittest.TestCase):
    def testPreserveProps(self) -> None: ...
