from argparse import ArgumentParser
import numpy as np
from typing import List

from src.couplings import *
from src.coefficients import *
from src.solver import Solver



def main(args) -> None:

    

    solver = Solver(
        m1=args.m1,
        m2=args.m2,
        q1=args.q1,
        q2=args.q2,
        omega1=args.omega1,
    )


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

