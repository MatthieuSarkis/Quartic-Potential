from argparse import ArgumentParser
import numpy as np
from typing import List

from src.couplings import *
from src.coefficients import *
from src.solver import Solver

HBAR = 1

def main(args) -> None:

    H = ((args.m1 + args.m2) / (args.m1 * args.m2)) * HBAR**2 / 2

    solver = Solver(
        alpha_list=args.
    )

    alpha = alpha(args.m1, args.m2, args.q1, args.q2, args.tau)
    beta = beta(args.m1, args.m2, args.q1, args.q2, args.omega1, args.omega2, args.r)
    gamma = gamma(args.m1, args.m2, args.q1, args.q2, args.r)
    delta = delta(args.m1, args.m2, args.q1, args.q2, args.r)

#epsilon0 = 1
#S0 = -10
#
#x0 = np.array([epsilon0, S0])
#x = fsolve(f, x0, args=(m1, m2, q1, q2, omega1, omega2, r, tau, H))

if __name__ == '__main__':

    parser = ArgumentParser()

    parser.add_argument('--m1',     nargs='+', type=float, default=1.0, help="Mass of QDO 1")
    parser.add_argument('--m2',     nargs='+', type=float, default=1.0, help="Mass of QDO 2")
    parser.add_argument('--q1',     nargs='+', type=float, default=1.0, help="Charge of QDO 1")
    parser.add_argument('--q2',     nargs='+', type=float, default=1.0, help="Charge of QDO 2")
    parser.add_argument('--omega1', nargs='+', type=float, default=1.0, help="Frequency of QDO 1")
    parser.add_argument('--omega2', nargs='+', type=float, default=1.0, help="Frequency of QDO 2")
    parser.add_argument('--r',      nargs='+', type=float, default=1.0, help="Distance between the two QDOs")
    parser.add_argument('--tau',    nargs='+', type=float, default=1.0, help="Strength of the external electric field")

    args = parser.parse_args()

    main(args)

