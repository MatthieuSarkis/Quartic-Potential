from argparse import ArgumentParser
import os

#from src.solver import Solver
from src.engine.solver_v2 import Solver

def main(args) -> None:

    log_dir = './results'
    os.makedirs(log_dir, exist_ok=True)

    solver = Solver(
        atom1=args.atom1,
        atom2=args.atom2,
        tau=args.tau,
        r=args.r,
        epsilon0=args.epsilon0,
        S0=args.S0,
        energy_unit=args.energy_unit,
        log_dir=log_dir
    )

    #solver = Solver(
    #    m1=args.m1,
    #    m2=args.m2,
    #    q1=args.q1,
    #    q2=args.q2,
    #    omega1=args.omega1,
    #    omega2=args.omega2,
    #    tau=args.tau,
    #    r=args.r,
    #    epsilon0=args.epsilon0,
    #    S0=args.S0,
    #    log_dir=log_dir
    #)

    solver.solve()

if __name__ == '__main__':

    parser = ArgumentParser()

    #parser.add_argument('--m1',     nargs='+', type=float, default=1.0,   help="Mass of QDO 1")
    #parser.add_argument('--m2',     nargs='+', type=float, default=1.0,   help="Mass of QDO 2")
    #parser.add_argument('--q1',     nargs='+', type=float, default=1.0,   help="Charge of QDO 1")
    #parser.add_argument('--q2',     nargs='+', type=float, default=1.0,   help="Charge of QDO 2")
    #parser.add_argument('--omega1', nargs='+', type=float, default=1.0,   help="Frequency of QDO 1")
    #parser.add_argument('--omega2', nargs='+', type=float, default=1.0,   help="Frequency of QDO 2")

    parser.add_argument('--atom1',             type=str,   default='H',       help='First atom in the diatomic molecule',  choices=['H', 'Li', 'K', 'Rb', 'Cs', 'He', 'Ne', 'Ar', 'Kr', 'Xe'])
    parser.add_argument('--atom2',             type=str,   default='H',       help='second atom in the diatomic molecule', choices=['H', 'Li', 'K', 'Rb', 'Cs', 'He', 'Ne', 'Ar', 'Kr', 'Xe'])
    parser.add_argument('--r',      nargs='+', type=float, default=1.0,       help="Distance between the two QDOs, measured in atomic units (multiple of Bohr radius)")
    parser.add_argument('--tau',    nargs='+', type=float, default=1.0,       help="Strength of the external electric field")
    parser.add_argument('--epsilon0',          type=float, default=1.0,       help="Initialization of the ground state energy")
    parser.add_argument('--S0',                type=float, default=-10.0,     help="Initialization of the fictitious variable")
    parser.add_argument('--energy_unit',       type=str,   default='hartree', help="Unit of energies", choices=['hartree', 'eV', 'cm-1', 'kcalPerMol', 'kJPerMol', 'kelvin', 'J', 'Hz'])

    args = parser.parse_args()

    main(args)

