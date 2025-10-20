"""This package provides a comprehensive suite of tools for creating QUBO objects,
defining QUBO solvers, and using them to solve QUBO problems.
It also includes features for pre- and post-processing, as well as the ability to create
pipelines that integrate all these components seamlessly.


The :py:mod:`~tno.quantum.optimization.qubo` package can be installed using pip::

    pip install tno.quantum.optimization.qubo

By default, the package is installed without external solver dependencies. You can
specify which QUBO solvers you would like to install. Available options are
``[dwave, qubovert, dqo]``. Alternatively, you can install all solvers
simultaneously using the ``'[all]'`` option::

    pip install tno.quantum.optimization.qubo'[all]'


**Example**

The following example shows how to construct a
:py:class:`~tno.quantum.optimization.qubo.components.QUBO` object.

>>> from tno.quantum.optimization.qubo import QUBO
>>> qubo = QUBO([
...     [ 1, -2,  3],
...     [-4,  5, -6],
...     [ 7, -8,  9]
... ])

One can use the :py:class:`~tno.quantum.optimization.qubo.SolverConfig` class to find
and instantiate available solvers to solve this QUBO, as shown in the following example.

>>> from tno.quantum.optimization.qubo import SolverConfig
>>> list(SolverConfig.supported_items())  # doctest: +NORMALIZE_WHITESPACE
['bf_solver',
'custom_solver',
'daqo_solver',
'd_wave_clique_embedded_simulated_annealing_solver',
'd_wave_clique_sampler_solver',
'd_wave_embedded_simulated_annealing_solver',
'd_wave_parallel_embedding_solver',
'd_wave_sampler_solver',
'd_wave_tiling_solver',
'digital_adiabatic_quantum_optimization_solver',
'exact_sampler_solver',
'kerberos_sampler_solver',
'leap_hybrid_solver',
'neighborhood_solver',
'pipeline_solver',
'qaoa_solver',
'rs_solver',
'random_sampler_solver',
'sa2_solver',
'simulated_annealing_solver',
'steepest_descent_solver',
'tabu_solver',
'tree_decomposition_solver']
>>> solver = SolverConfig(name='bf_solver').get_instance()
>>>
>>> # Solve the QUBO
>>> result = solver.solve(qubo)
>>> result.best_bitvector
BitVector(000)

Similarly, one can use the :py:class:`~tno.quantum.optimization.qubo.PreprocessorConfig`
and :py:class:`~tno.quantum.optimization.qubo.PostprocessorConfig` classes to find and
instantiate available preprocessors and postprocessors.
"""  # noqa: D205

from __future__ import annotations

from tno.quantum.optimization.qubo.components import (
    QUBO,
    PostprocessorConfig,
    PreprocessorConfig,
    SolverConfig,
)

__all__: list[str] = [
    "QUBO",
    "PostprocessorConfig",
    "PreprocessorConfig",
    "SolverConfig",
]

__version__ = "1.0.1"
