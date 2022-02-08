# compchem-typeshed
An experimental typeshed for distributing type annotations in a small subset of computational chemistry tools via [stubs](https://www.python.org/dev/peps/pep-0484/#stub-files).

### Usage

Until/if this is packaged, it must be cloned and then `mypy` instructed how to find the files using
either the [`$MYPYPATH`](https://mypy.readthedocs.io/en/stable/config_file.html#confval-mypy_path) environment variable or [import discovery magic](https://mypy.readthedocs.io/en/stable/config_file.html#confval-mypy_path)
