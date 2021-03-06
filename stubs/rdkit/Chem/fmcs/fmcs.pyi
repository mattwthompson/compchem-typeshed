from collections.abc import Generator
from itertools import product as product
from rdkit import Chem as Chem
from typing import Any, NamedTuple

class Default:
    timeout: Any
    timeoutString: str
    maximize: str
    atomCompare: str
    bondCompare: str
    matchValences: bool
    ringMatchesRingOnly: bool
    completeRingsOnly: bool

class AtomSmartsNoAromaticity(dict):
    def __missing__(self, eleno): ...

def atom_typer_any(atoms): ...
def atom_typer_elements(atoms): ...
def atom_typer_isotopes(atoms): ...
def bond_typer_any(bonds): ...
def bond_typer_bondtypes(bonds): ...

atom_typers: Any
bond_typers: Any
default_atom_typer: Any
default_bond_typer: Any

def get_isotopes(mol): ...
def set_isotopes(mol, isotopes) -> None: ...
def save_isotopes(mol, isotopes) -> None: ...
def save_atom_classes(mol, atom_classes) -> None: ...
def get_selected_atom_classes(mol, atom_indices): ...
def restore_isotopes(mol) -> None: ...
def assign_isotopes_from_class_tag(mol, atom_class_tag) -> None: ...

class TypedMolecule:
    rdmol: Any
    rdmol_atoms: Any
    rdmol_bonds: Any
    atom_smarts_types: Any
    bond_smarts_types: Any
    canonical_bondtypes: Any
    def __init__(self, rdmol, rdmol_atoms, rdmol_bonds, atom_smarts_types, bond_smarts_types, canonical_bondtypes) -> None: ...

class FragmentedTypedMolecule:
    rdmol: Any
    rdmol_atoms: Any
    orig_atoms: Any
    orig_bonds: Any
    atom_smarts_types: Any
    bond_smarts_types: Any
    canonical_bondtypes: Any
    def __init__(self, rdmol, rdmol_atoms, orig_atoms, orig_bonds, atom_smarts_types, bond_smarts_types, canonical_bondtypes) -> None: ...

class TypedFragment:
    rdmol: Any
    orig_atoms: Any
    orig_bonds: Any
    atom_smarts_types: Any
    bond_smarts_types: Any
    canonical_bondtypes: Any
    def __init__(self, rdmol, orig_atoms, orig_bonds, atom_smarts_types, bond_smarts_types, canonical_bondtypes) -> None: ...

def get_canonical_bondtypes(rdmol, bonds, atom_smarts_types, bond_smarts_types): ...
def get_typed_molecule(rdmol, atom_typer, bond_typer, matchValences=..., ringMatchesRingOnly=...): ...
def get_specified_types(rdmol, atom_types, ringMatchesRingOnly): ...
def convert_input_to_typed_molecules(mols, atom_typer, bond_typer, matchValences, ringMatchesRingOnly): ...
def get_counts(it): ...
def intersect_counts(counts1, counts2): ...
def get_canonical_bondtype_counts(typed_mols): ...
def remove_unknown_bondtypes(typed_mol, supported_canonical_bondtypes): ...
def find_upper_fragment_size_limits(rdmol, atoms): ...

class EnumerationMolecule(NamedTuple):
    rdmol: Any
    atoms: Any
    bonds: Any
    directed_edges: Any

class Atom(NamedTuple):
    real_atom: Any
    atom_smarts: Any
    bond_indices: Any
    is_in_ring: Any

class Bond(NamedTuple):
    real_bond: Any
    bond_smarts: Any
    canonical_bondtype: Any
    atom_indices: Any
    is_in_ring: Any

class DirectedEdge(NamedTuple):
    bond_index: Any
    end_atom_index: Any

class Subgraph(NamedTuple):
    atom_indices: Any
    bond_indices: Any

def get_typed_fragment(typed_mol, atom_indices): ...
def fragmented_mol_to_enumeration_mols(typed_mol, minNumAtoms: int = ...): ...
def gen_primes() -> Generator[Any, None, None]: ...

class CangenNode:
    index: Any
    atom_smarts: Any
    value: int
    neighbors: Any
    rank: int
    outgoing_edges: Any
    def __init__(self, index, atom_smarts) -> None: ...

class OutgoingEdge(NamedTuple):
    from_atom_index: Any
    bond_index: Any
    bond_smarts: Any
    other_node_idx: Any
    other_node: Any

def get_initial_cangen_nodes(subgraph, enumeration_mol, atom_assignment, do_initial_assignment: bool = ...): ...
def rerank(cangen_nodes) -> None: ...
def find_duplicates(cangen_nodes, start, end): ...
def canon(cangen_nodes): ...
def get_closure_label(bond_smarts, closure): ...
def generate_smarts(cangen_nodes): ...
def make_canonical_smarts(subgraph, enumeration_mol, atom_assignment): ...
def make_arbitrary_smarts(subgraph, enumeration_mol, atom_assignment): ...
def powerset(iterable): ...
def nonempty_powerset(iterable): ...

tiebreaker: Any

def find_extensions(atom_indices, visited_bond_indices, directed_edges): ...
def all_subgraph_extensions(enumeration_mol, subgraph, visited_bond_indices, internal_bonds, external_edges) -> Generator[Any, None, None]: ...
def find_extension_size(enumeration_mol, known_atoms, exclude_bonds, directed_edges): ...

class CachingTargetsMatcher(dict):
    targets: Any
    required_match_count: Any
    def __init__(self, targets, required_match_count: Any | None = ...) -> None: ...
    def shift_targets(self) -> None: ...
    def __missing__(self, smarts): ...

class VerboseCachingTargetsMatcher:
    targets: Any
    cache: Any
    required_match_count: Any
    num_lookups: int
    num_search_true: int
    def __init__(self, targets, required_match_count: Any | None = ...) -> None: ...
    def shift_targets(self) -> None: ...
    def __getitem__(self, smarts, missing=...): ...
    def report(self) -> None: ...

def prune_maximize_bonds(subgraph, mol, num_remaining_atoms, num_remaining_bonds, best_sizes): ...
def prune_maximize_atoms(subgraph, mol, num_remaining_atoms, num_remaining_bonds, best_sizes): ...

class _SingleBest:
    best_num_atoms: int
    best_smarts: Any
    sizes: Any
    timer: Any
    verbose: Any
    def __init__(self, timer, verbose) -> None: ...
    def get_result(self, completed): ...

class MCSResult:
    num_atoms: Any
    num_bonds: Any
    smarts: Any
    completed: Any
    def __init__(self, num_atoms, num_bonds, smarts, completed) -> None: ...
    def __nonzero__(self): ...

class SingleBestAtoms(_SingleBest):
    def add_new_match(self, subgraph, mol, smarts): ...

class SingleBestBonds(_SingleBest):
    def add_new_match(self, subgraph, mol, smarts): ...

def check_completeRingsOnly(smarts, subgraph, enumeration_mol): ...

class SingleBestAtomsCompleteRingsOnly(_SingleBest):
    def add_new_match(self, subgraph, mol, smarts): ...

class SingleBestBondsCompleteRingsOnly(_SingleBest):
    def add_new_match(self, subgraph, mol, smarts): ...

def enumerate_subgraphs(enumeration_mols, prune, atom_assignment, matches_all_targets, hits, timeout, heappush, heappop): ...

class Uniquer(dict):
    counter: Any
    def __init__(self) -> None: ...
    def __missing__(self, key): ...

def MATCH(mol, pat): ...

class VerboseHeapOps:
    num_seeds_added: int
    num_seeds_processed: int
    verboseDelay: Any
    trigger: Any
    def __init__(self, trigger, verboseDelay) -> None: ...
    def heappush(self, seeds, item): ...
    def heappop(self, seeds): ...
    def trigger_report(self) -> None: ...
    def report(self) -> None: ...

def compute_mcs(fragmented_mols, typed_mols, minNumAtoms, threshold_count: Any | None = ..., maximize=..., completeRingsOnly=..., timeout=..., timer: Any | None = ..., verbose: bool = ..., verboseDelay: float = ...): ...

class Timer:
    mark_times: Any
    def __init__(self) -> None: ...
    def mark(self, name) -> None: ...

def fmcs(mols, minNumAtoms: int = ..., maximize=..., atomCompare=..., bondCompare=..., threshold: float = ..., matchValences=..., ringMatchesRingOnly: bool = ..., completeRingsOnly: bool = ..., timeout=..., times: Any | None = ..., verbose: bool = ..., verboseDelay: float = ...): ...
def subgraph_to_fragment(mol, subgraph): ...
def make_fragment_smiles(mcs, mol, subgraph, args: Any | None = ...): ...
def make_fragment_sdf(mcs, mol, subgraph, args): ...
def make_complete_sdf(mcs, mol, subgraph, args): ...

structure_format_functions: Any

def make_structure_format(format_name, mcs, mol, subgraph, args): ...
def parse_num_atoms(s): ...
def parse_threshold(s): ...
def parse_timeout(s): ...

class starting_from:
    left: Any
    def __init__(self, left) -> None: ...
    def __contains__(self, value): ...

range_pat: Any
value_pat: Any

def parse_select(s): ...

compare_shortcuts: Any

def main(args: Any | None = ...) -> None: ...
