# -*- coding: utf-8 -*-
"""
    The dataloader methods used for CCEA.

:Author: Yan Zhou

:License: BSD 3-Clause, see LICENSE file.
"""

from .KTH_dataloader import *
from .UCI_dataloader import *
from .NMNIST_dataloader import *


__all__ = [
    "KTH_classification",
    "UCI_classification",
    "NMNIST_classification",
]