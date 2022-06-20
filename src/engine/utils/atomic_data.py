from typing import Tuple

HBAR = 1.0

# Obtained from "Quantum Drude Oscillators for Accurate Many-body Intermolecular Forces"
DISPERSION_PARAMETERS = {
    'H': {'alpha': 4.5, 'C6': 6.49, 'C8': 124.5},
    'He': {'alpha': 1.38, 'C6': 1.46, 'C8': 14.05},
    'Ne': {'alpha': 2.66, 'C6': 6.88, 'C8': 76},
}

# Obtained from "Quantum Drude oscillator model of atoms and molecules: Many-body polarization and dispersion interactions for atomistic simulation"
# Those quantities are in atomic units (q_e = 1, m_e = 1, hbar = 1, Energy in Hartree)
ATOMIC_PARAMETERS = {
    'H':  {'omega': 0.4273, 'm': 0.6099, 'q': 0.7080},
    'Li': {'omega': 0.0687, 'm': 1.2545, 'q': 0.9848},
    'K':  {'omega': 0.0630, 'm': 0.8101, 'q': 0.9670},
    'Rb': {'omega': 0.0603, 'm': 0.7343, 'q': 0.9274},
    'Cs': {'omega': 0.0531, 'm': 0.6939, 'q': 0.8950},
    'He': {'omega': 1.0187, 'm': 0.5083, 'q': 0.8532},
    'Ne': {'omega': 1.2965, 'm': 0.3491, 'q': 1.2494},
    'Ar': {'omega': 0.7272, 'm': 0.3020, 'q': 1.3314},
    'Kr': {'omega': 0.6359, 'm': 0.2796, 'q': 1.3741},
    'Xe': {'omega': 0.5152, 'm': 0.2541, 'q': 1.3570},
}

ENERGY_UNIT_CONVERSION_FACTOR = {
    'hartree': 1.0,
    'eV': 27.2107,
    'cm-1': 219474.63,
    'kcalPerMol': 627.503,
    'kJPerMol': 2625.5,
    'kelvin': 315777,
    'J': 43.60e-19,
    'Hz': 6.57966e15,
}

def m(
    alpha: float,
    C6: float,
    C8: float
) -> float:

    return (15 * HBAR**2 * alpha**2) / (4 * C8)

def q(
    alpha: float,
    C6: float,
    C8: float
) -> float:

    return 2 * (5 / 3)**0.5 * (C6**2 / (C8 * alpha))**2

def omega(
    alpha: float,
    C6: float,
    C8: float
) -> float:

    return (4 * C6) / (3 * HBAR * alpha**2)

def compute_QDO_parameters(
    atom_type: str = 'H'
) -> Tuple[float, float, float]:

    atom = DISPERSION_PARAMETERS[atom_type]

    mass = m(alpha=atom['alpha'], C6=atom['C6'], C8=atom['C8'])
    charge = q(alpha=atom['alpha'], C6=atom['C6'], C8=atom['C8'])
    frequency = omega(alpha=atom['alpha'], C6=atom['C6'], C8=atom['C8'])

    return mass, charge, frequency