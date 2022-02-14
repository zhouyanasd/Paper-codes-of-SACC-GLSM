# -*- coding: utf-8 -*-
"""
    The optimization methods used for NAS.

:Author: Yan Zhou

:License: BSD 3-Clause, see LICENSE file.
"""

from .bayesian import *
from .ccea import *
from .de import *
from .surrogate import *

__all__ = [
    "DiffEvol",
    "BayesianOptimization",
    "GaussianProcess_BayesianOptimization",
    "RandomForestRegressor_BayesianOptimization",
    "RandomForestRegressor_surrogate",
    "RandomForestRegressor_surrogate_wang",
    "GaussianProcess_surrogate",
    "CCEA",
    "CCEA_surrogate",
    "CCEA_fitness_inheritance",
]