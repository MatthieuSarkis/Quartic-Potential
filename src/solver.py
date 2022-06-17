import itertools
import numpy as np
from scipy.optimize import fsolve
from typing import Dict, List

from src.coefficients import *

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

        self.alpha_list = alpha_list
        self.beta_list = beta_list
        self.gamma_list = gamma_list
        self.delta_list = delta_list

        self.grid = self._prepare_grid()

    def solve(self) -> List[float]:

        pass

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

        for pair in itertools.product(self.alpha_list, self.beta_list, self.gamma_list, self.delta_list):

            grid.append({
                'alpha': pair[0],
                'sigma': pair[1]
            })

        return grid