import itertools
import json
import numpy as np
import os
from scipy.optimize import fsolve
from typing import Dict, List

from src.engine.expansion_coefficients.positive_coefficient import coefPlus
from src.engine.expansion_coefficients.negative_coefficient import coefMinus
from src.engine.couplings import *
from src.engine.utils.atomic_data import *

class Solver():

    def __init__(
        self,
        atom1: str,
        atom2: str,
        tau: List[float],
        r: List[float],
        epsilon0: float = 1.0,
        S0: float = -10.0,
        energy_unit: str = 'hartree',
        log_dir: str = './results'
    ) -> None:

        self.atom1 = atom1
        self.atom2 = atom2

        self.m1 = ATOMIC_PARAMETERS[atom1]['m']
        self.q1 = ATOMIC_PARAMETERS[atom1]['q']
        self.omega1 = ATOMIC_PARAMETERS[atom1]['omega']
        self.m2 = ATOMIC_PARAMETERS[atom2]['m']
        self.q2 = ATOMIC_PARAMETERS[atom2]['q']
        self.omega2 = ATOMIC_PARAMETERS[atom2]['omega']

        self.tau = tau
        self.r = r
        self.x0 = [epsilon0, S0]
        self.energy_unit = energy_unit

        self.log_dir = os.path.join(log_dir, self.atom1 + '-' + self.atom2)
        os.makedirs(self.log_dir, exist_ok=True)

        self.grid = self._prepare_grid()

    def solve(self) -> List[float]:

        for i in range(len(self.grid)):

            alpha_ = alpha(self.m1, self.m2, self.q1, self.q2, self.grid[i]['tau'])
            beta_ = beta(self.m1, self.m2, self.q1, self.q2, self.omega1, self.omega2, self.grid[i]['r'])
            gamma_ = gamma(self.m1, self.m2, self.q1, self.q2, self.grid[i]['r'])
            delta_ = delta(self.m1, self.m2, self.q1, self.q2, self.grid[i]['r'])
            H = ((self.m1 + self.m2) / (self.m1 * self.m2)) * HBAR**2 / 2

            x = fsolve(self.equations, self.x0, args=(alpha_, beta_, gamma_, delta_, H))

            self.grid[i]['epsilon'] = x[0] * ENERGY_UNIT_CONVERSION_FACTOR[self.energy_unit]
            self.grid[i]['energy_unit'] = self.energy_unit
            #self.grid[i]['S'] = x[1]

        self._dump_results()

    def equations(
        self,
        x: np.ndarray,
        alpha: float,
        beta: float,
        gamma: float,
        delta: float,
        H: float
    ) -> np.ndarray:

        equation0 = coefPlus(
            epsilon=x[0],
            S=x[1],
            alpha=alpha,
            beta=beta,
            gamma=gamma,
            delta=delta,
            H=H
        )

        equation1 = coefMinus(
            epsilon=x[0],
            S=x[1],
            alpha=alpha,
            beta=beta,
            gamma=gamma,
            delta=delta,
            H=H
        )

        return [equation0, equation1]

    def _prepare_grid(self) -> List[Dict[str, float]]:

        grid: List[Dict[str, float]] = []

        for pair in itertools.product(self.tau, self.r):

            grid.append({
                'tau': pair[0],
                'r': pair[1]
            })

        return grid

    def _dump_results(self) -> None:

        with open(os.path.join(self.log_dir, 'results.json'), 'w') as f:
            json.dump(self.grid, f, indent=4)