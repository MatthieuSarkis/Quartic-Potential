import itertools
import json
import numpy as np
import os
from scipy.optimize import fsolve
from typing import Dict, List
import warnings
warnings.filterwarnings("error")

from src.engine.expansion_coefficients.N_15.positive_coefficient import coefPlus
from src.engine.expansion_coefficients.N_15.negative_coefficient import coefMinus
from src.engine.expansion_coefficients.N_20.rational_numerator import rational_numerator
from src.engine.expansion_coefficients.N_20.rational_denominator import rational_denominator
from src.engine.couplings import *
from src.engine.utils.atomic_data import *

class Solver():

    def __init__(
        self,
        atom1: str,
        atom2: str,
        tau: List[float],
        r: List[float],
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
        #self.epsilon0_list = [n for n in range(-10, 30)]
        #self.S0_list = [n for n in range(-20, 20)]
        self.epsilon0_list = [-10]
        self.S0_list = [0]
        self.energy_unit = energy_unit

        self.log_dir = os.path.join(log_dir, self.atom1 + '-' + self.atom2)
        os.makedirs(self.log_dir, exist_ok=True)

        self.grid = self._prepare_grid()

    def solve(self) -> None:

        for i in range(len(self.grid)):

            alpha_ = alpha(self.m1, self.m2, self.q1, self.q2, self.grid[i]['tau'])
            beta_ = beta(self.m1, self.m2, self.q1, self.q2, self.omega1, self.omega2, self.grid[i]['r'])
            gamma_ = gamma(self.m1, self.m2, self.q1, self.q2, self.grid[i]['r'])
            delta_ = delta(self.m1, self.m2, self.q1, self.q2, self.grid[i]['r'])
            H_ = ((self.m1 + self.m2) / (self.m1 * self.m2)) * HBAR**2 / 2

            lowest_S = float('inf')
            lowest_epsilon = float('inf')
            for pair in itertools.product(self.epsilon0_list, self.S0_list):

                #print(pair)

                epsilon0 = pair[0]
                S0 = pair[1]
                x0 = [epsilon0, S0]

                try:
                    x = fsolve(self.equations, x0, args=(alpha_, beta_, gamma_, delta_, H_))

                except RuntimeWarning:
                    continue

                epsilon = x[0]
                S = x[1]

                if epsilon < lowest_epsilon:
                    lowest_epsilon = epsilon
                    lowest_S = S

            self.grid[i]['S'] = lowest_S
            self.grid[i]['epsilon'] = lowest_epsilon
            self.grid[i]['epsilon (in {})'.format(self.energy_unit)] = self.grid[i]['epsilon'] * ENERGY_UNIT_CONVERSION_FACTOR[self.energy_unit]

            self._dump_json()
        self._dump_numpy_for_latex()

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

    def _dump_json(self) -> None:

        with open(os.path.join(self.log_dir, 'results.json'), 'w') as f:
            json.dump(self.grid, f, indent=4)

    def _dump_numpy_for_latex(self) -> None:
        r'''Saves the output data in a txt file, nicely formatted for latex tables.
        The first column are the various values of the distance r.
        The top left value is set to 0 and is totally irrelevant, just here for formatting reasons.
        '''

        energy_array = np.zeros(shape=(len(self.tau) * len(self.r),))
        for i in range(len(self.grid)):
            energy_array[i] = self.grid[i]['epsilon']

        energy_array = energy_array.reshape((len(self.tau), len(self.r))).T
        r = np.array(self.r).reshape((-1, 1))
        tau = np.array([0] + self.tau).reshape((1, -1))
        energy_array = np.concatenate((r, energy_array), axis=1)
        energy_array = np.concatenate((tau, energy_array), axis=0)

        np.savetxt(os.path.join(self.log_dir, "r_vs_tau_table.txt"), energy_array, delimiter=' & ', fmt='%f', newline=' \\\\\n')