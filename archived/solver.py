import itertools
import json
import numpy as np
import os
from scipy.optimize import fsolve
from typing import Dict, List

from src.expansion_coefficients.positive_coefficient import coefPlus
from src.expansion_coefficients.negative_coefficient import coefMinus
from src.couplings import *
from src.utils.atomic_data import HBAR

class Solver():

    def __init__(
        self,
        m1: List[float] ,
        m2: List[float] ,
        q1: List[float] ,
        q2: List[float] ,
        omega1: List[float],
        omega2: List[float],
        tau: List[float],
        r: List[float],
        epsilon0: float = 1.0,
        S0: float = -10.0,
        log_dir: str = './results'
    ) -> None:

        self.m1 = m1
        self.m2 = m2
        self.q1 = q1
        self.q2 = q2
        self.omega1 = omega1
        self.omega2 = omega2
        self.tau = tau
        self.r = r
        self.x0 = [epsilon0, S0]
        self.log_dir = log_dir

        self.grid = self._prepare_grid()

    def solve(self) -> List[float]:

        for i in range(len(self.grid)):

            alpha_ = alpha(self.grid[i]['m1'], self.grid[i]['m2'], self.grid[i]['q1'], self.grid[i]['q2'], self.grid[i]['tau'])
            beta_ = beta(self.grid[i]['m1'], self.grid[i]['m2'], self.grid[i]['q1'], self.grid[i]['q2'], self.grid[i]['omega1'], self.grid[i]['omega2'], self.grid[i]['r'])
            gamma_ = gamma(self.grid[i]['m1'], self.grid[i]['m2'], self.grid[i]['q1'], self.grid[i]['q2'], self.grid[i]['r'])
            delta_ = delta(self.grid[i]['m1'], self.grid[i]['m2'], self.grid[i]['q1'], self.grid[i]['q2'], self.grid[i]['r'])
            H = ((self.grid[i]['m1'] + self.grid[i]['m2']) / (self.grid[i]['m1'] * self.grid[i]['m2'])) * HBAR**2 / 2

            x = fsolve(self.equations, self.x0, args=(alpha_, beta_, gamma_, delta_, H))

            self.grid[i]['epsilon'] = x[0]
            self.grid[i]['S'] = x[1]

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

        for octuple in itertools.product(self.m1, self.m2, self.q1, self.q2, self.omega1, self.omega2, self.tau, self.r):

            grid.append({
                'm1': octuple[0],
                'm2': octuple[1],
                'q1': octuple[2],
                'q2': octuple[3],
                'omega1': octuple[4],
                'omega2': octuple[5],
                'tau': octuple[6],
                'r': octuple[7]
            })

        return grid

    def _dump_results(self) -> None:

        with open(os.path.join(self.log_dir, 'results.json'), 'w') as f:
            json.dump(self.grid, f, indent=4)