from argparse import ArgumentParser
import numpy as np
import os
from typing import List

from src.couplings import *
from src.coefficients import *
from src.solver import Solver

def main(args) -> None:

    log_dir = './results'
    os.makedirs(log_dir, exist_ok=True)

    solver = Solver(
        m1=args.m1,
        m2=args.m2,
        q1=args.q1,
        q2=args.q2,
        omega1=args.omega1,
        omega2=args.omega2,
        tau=args.tau,
        r = args.r,
        log_dir=log_dir
    )

    solver.solve()

if __name__ == '__main__':

    parser = ArgumentParser()

    parser.add_argument('--m1',     nargs='+', type=float, default=1.0,   help="Mass of QDO 1")
    parser.add_argument('--m2',     nargs='+', type=float, default=1.0,   help="Mass of QDO 2")
    parser.add_argument('--q1',     nargs='+', type=float, default=1.0,   help="Charge of QDO 1")
    parser.add_argument('--q2',     nargs='+', type=float, default=1.0,   help="Charge of QDO 2")
    parser.add_argument('--omega1', nargs='+', type=float, default=1.0,   help="Frequency of QDO 1")
    parser.add_argument('--omega2', nargs='+', type=float, default=1.0,   help="Frequency of QDO 2")
    parser.add_argument('--r',      nargs='+', type=float, default=1.0,   help="Distance between the two QDOs")
    parser.add_argument('--tau',    nargs='+', type=float, default=1.0,   help="Strength of the external electric field")
    parser.add_argument('--epsilon0',          type=float, default=1.0,   help="Initialization of the ground state energy")
    parser.add_argument('--S0',                type=float, default=-10.0, help="Initialization of the fictitious variable")

    args = parser.parse_args()

    main(args)

