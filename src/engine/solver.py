import itertools
import json
import numpy as np
import numpy.polynomial.polynomial as poly
import os
from typing import Dict, List
import warnings
warnings.filterwarnings("error")

from src.engine.expansion_coefficients.N_20.coefficients_array import *
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
        n_eigenvalues: int = 3,
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
        self.energy_unit = energy_unit
        self.n_eigenvalues = n_eigenvalues

        self.log_dir = os.path.join(log_dir, self.atom1 + '-' + self.atom2)
        os.makedirs(self.log_dir, exist_ok=True)

        self.grid = self._prepare_grid()

    def solve(self) -> None:

        for i in range(len(self.grid)):

            alpha_ = alpha(self.m1, self.m2, self.q1, self.q2, self.grid[i]['tau'])
            beta_ = beta(self.m1, self.m2, self.q1, self.q2, self.omega1, self.omega2, self.grid[i]['r'])
            gamma_ = gamma(self.m1, self.m2, self.q1, self.q2, self.grid[i]['r'])
            delta_ = delta(self.m1, self.m2, self.q1, self.q2, self.grid[i]['r'])
            H_ = np.sqrt(((self.m1 + self.m2) / (self.m1 * self.m2)) * HBAR**2 / 2)

            pnum = poly.Polynomial(numerator_coefficients_array(alpha_, beta_, gamma_, delta_, H_))
            pden = poly.Polynomial(denominator_coefficients_array(alpha_, beta_, gamma_, delta_, H_))

            num_roots = poly.Polynomial.roots(pnum)[:self.n_eigenvalues]
            #den_roots = poly.Polynomial.roots(pden)

            self.grid[i]['energy_spectrum'] = num_roots.tolist()
            #self.grid[i]['pole_spectrum'] = den_roots.tolist()
            #self.grid[i]['energy_spectrum (in {})'.format(self.energy_unit)] = (num_roots * ENERGY_UNIT_CONVERSION_FACTOR[self.energy_unit]).tolist()

            try:
                self._dump_json()
            except TypeError:
                print(self.grid[i])

        #self._dump_numpy_for_latex()


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