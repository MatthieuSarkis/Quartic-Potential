import itertools
import numpy as np
from scipy.optimize import fsolve
from typing import Dict, List

from src.coefficients import *

HBAR = 1

class Solver():

    def __init__(
        self,
        m1: List[float] ,
        m2: List[float] ,
        q1: List[float] ,
        q2: List[float] ,
        omega1: List[float],
        omega2: List[float],
        r: List[float],
    ) -> None:

        self.m1 = m1
        self.m2 = m2
        self.q1 = q1
        self.q2 = q2
        self.omega1 = omega1
        self.omega1 = omega2
        self.r = r
        
        epsilon0 = 1
        S0 = -10
        self.x0 = np.array([epsilon0, S0])

        self.grid = self._prepare_grid()

    def solve(self) -> List[float]:

        for i in range(len(self.grid)):
            
            alpha = alpha(self.grid[i].m1, self.grid[i].m2, self.grid[i].q1, self.grid[i].q2, self.grid[i].tau)
            beta = beta(self.grid[i].m1, self.grid[i].m2, self.grid[i].q1, self.grid[i].q2, self.grid[i].omega1, self.grid[i].omega2, self.grid[i].r)
            gamma = gamma(self.grid[i].m1, self.grid[i].m2, self.grid[i].q1, self.grid[i].q2, self.grid[i].r)
            delta = delta(self.grid[i].m1, self.grid[i].m2, self.grid[i].q1, self.grid[i].q2, self.grid[i].r)
            H = ((self.grid[i].m1 + self.grid[i].m2) / (self.grid[i].m1 * self.grid[i].m2)) * HBAR**2 / 2
            
            x = fsolve(self.f, self.x0, args=(alpha, beta, gamma, delta, H))
            
            self.grid[i]['epsilon'] = x[0]
            self.grid[i]['S'] = x[1]

    def equations(
        x: np.ndarray,
        alpha: float,
        beta: float,
        gamma: float,
        delta: float,
        H: float
    ) -> np.ndarray:

        equation0 = coefPlus(
            x[0],
            x[1],
            alpha,
            beta,
            gamma,
            delta,
            H
        )

        equation1 = coefMinus(
            x[0],
            x[1],
            alpha,
            beta,
            gamma,
            delta,
            H
        )

        return np.array([equation0, equation1])

    def _prepare_grid(self) -> List[Dict[str, float]]:

        grid: List[Dict[str, float]] = []

        for septuple in itertools.product(self.m1, self.m2, self.q1, self.q2, self.omega1, self.omega2, self.r):

            grid.append({
                'm1': septuple[0],
                'm2': septuple[1],
                'q1': septuple[2],
                'q2': septuple[3],
                'omega1': septuple[4],
                'omega2': septuple[5],
                'r': septuple[6],
            })

        return grid