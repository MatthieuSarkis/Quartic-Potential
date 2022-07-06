import numpy as np

from src.expansion_coefficients.N_20.numerator.rationalNumerator_coefficients import *
from src.expansion_coefficients.N_20.denominator.rationalDenominator_coefficients import *

def numerator_coefficients_array(
	alpha: float,
	beta: float,
	gamma: float,
	delta: float,
	H: float
) -> np.ndarray:

    return np.array([
        num_coef_degree_0(alpha, beta, gamma, delta, H),
        num_coef_degree_1(alpha, beta, gamma, delta, H),
        num_coef_degree_2(alpha, beta, gamma, delta, H),
        num_coef_degree_3(alpha, beta, gamma, delta, H),
        num_coef_degree_4(alpha, beta, gamma, delta, H),
        num_coef_degree_5(alpha, beta, gamma, delta, H),
        num_coef_degree_6(alpha, beta, gamma, delta, H),
        num_coef_degree_7(alpha, beta, gamma, delta, H),
        num_coef_degree_8(alpha, beta, gamma, delta, H),
        num_coef_degree_9(alpha, beta, gamma, delta, H),
        num_coef_degree_10(alpha, beta, gamma, delta, H),
        num_coef_degree_11(alpha, beta, gamma, delta, H),
        num_coef_degree_12(alpha, beta, gamma, delta, H),
        num_coef_degree_13(alpha, beta, gamma, delta, H),
        num_coef_degree_14(alpha, beta, gamma, delta, H),
        num_coef_degree_15(alpha, beta, gamma, delta, H),
        num_coef_degree_16(alpha, beta, gamma, delta, H),
        num_coef_degree_17(alpha, beta, gamma, delta, H),
        num_coef_degree_18(alpha, beta, gamma, delta, H),
        num_coef_degree_19(alpha, beta, gamma, delta, H)
    ])

def denominator_coefficients_array(
	alpha: float,
	beta: float,
	gamma: float,
	delta: float,
	H: float
) -> np.ndarray:

    return np.array([
        den_coef_degree_0(alpha, beta, gamma, delta, H),
        den_coef_degree_1(alpha, beta, gamma, delta, H),
        den_coef_degree_2(alpha, beta, gamma, delta, H),
        den_coef_degree_3(alpha, beta, gamma, delta, H),
        den_coef_degree_4(alpha, beta, gamma, delta, H),
        den_coef_degree_5(alpha, beta, gamma, delta, H),
        den_coef_degree_6(alpha, beta, gamma, delta, H),
        den_coef_degree_7(alpha, beta, gamma, delta, H),
        den_coef_degree_8(alpha, beta, gamma, delta, H),
        den_coef_degree_9(alpha, beta, gamma, delta, H)
    ])