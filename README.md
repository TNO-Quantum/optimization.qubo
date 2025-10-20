# TNO Quantum: Optimization - QUBO

TNO Quantum provides generic software components aimed at facilitating the development
of quantum applications.

This package provides a comprehensive suite of tools for creating QUBO objects, defining QUBO solvers, and using them to solve QUBO problems. It also includes features for pre- and post-processing, as well as the ability to create pipelines that integrate all these components seamlessly

## Documentation

Documentation of the `tno.quantum.optimization.qubo` package can be found [here](https://tno-quantum.github.io/documentation/).


## Install

Easily install the `tno.quantum.optimization.qubo` package using pip:

```console
$ pip install tno.quantum.optimization.qubo
```

By default, the package is installed without external solver dependencies. You can specify which QUBO solvers you would like to install. Available options are [dwave, qubovert, dqo]. Alternatively, you can install all solvers simultaneously using the [all] option:

```console
$ pip install tno.quantum.optimization.qubo[all]
```

## Usage

The following example shows how to construct a `QUBO` object.

```python
from tno.quantum.optimization.qubo import QUBO

qubo = QUBO([
    [ 1, -2,  3],
    [-4,  5, -6],
    [ 7, -8,  9]
])
```

```python
from tno.quantum.optimization.qubo import SolverConfig
solver = SolverConfig(name='bf_solver').get_instance()

# Solve the QUBO
result = solver.solve(qubo)
result.best_bitvector # BitVector(000)
```

## (End)use limitations
The content of this software may solely be used for applications that comply with international export control laws.