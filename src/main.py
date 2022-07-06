from argparse import ArgumentParser
import os

from src.solver import Solver

def main(args) -> None:

    log_dir = './results'
    os.makedirs(log_dir, exist_ok=True)

    solver = Solver(
        atom1=args.atom1,
        atom2=args.atom2,
        tau=args.tau,
        r=args.r,
        energy_unit=args.energy_unit,
        n_eigenvalues=args.n_eigenvalues,
        log_dir=log_dir
    )

    solver.solve()

if __name__ == '__main__':

    parser = ArgumentParser()

    parser.add_argument('--atom1',             type=str,   default='H',       help='First atom in the diatomic molecule',  choices=['H', 'Li', 'K', 'Rb', 'Cs', 'He', 'Ne', 'Ar', 'Kr', 'Xe'])
    parser.add_argument('--atom2',             type=str,   default='H',       help='second atom in the diatomic molecule', choices=['H', 'Li', 'K', 'Rb', 'Cs', 'He', 'Ne', 'Ar', 'Kr', 'Xe'])
    parser.add_argument('--r',      nargs='+', type=float, default=1.0,       help="Distance between the two QDOs, measured in atomic units (multiple of Bohr radius)")
    parser.add_argument('--tau',    nargs='+', type=float, default=1.0,       help="Strength of the external electric field")
    parser.add_argument('--energy_unit',       type=str,   default='hartree', help="Unit of energies",                     choices=['hartree', 'eV', 'cm-1', 'kcalPerMol', 'kJPerMol', 'kelvin', 'J', 'Hz'])
    parser.add_argument('--n_eigenvalues',     type=int,   default=3,         help="Number of energy levels to compute",   choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    args = parser.parse_args()

    main(args)

