def alpha(
    m1: float,
    m2: float,
    q1: float,
    q2: float,
    tau: float
) -> float:

    return - tau * (m1 * q2 + m2 * q1) / (m1 + m2)

def beta(
    m1: float,
    m2: float,
    q1: float,
    q2: float,
    omega1: float,
    omega2: float,
    r: float,
) -> float:

    return ((m1 * m2) / ((m1 + m2)**2)) * ((2 * q1 * q2) / (r**3)) + 0.5 * ((m1 * m2) / (m1 + m2)) * (m1 * omega2**2 + m2 * omega1**1) / (m1 + m2)

def gamma(
    m1: float,
    m2: float,
    q1: float,
    q2: float,
    r: float,
) -> float:

    return - ((m1 * m2) / ((m1 + m2)**2)) * (3 * q1 * q2) / (r**4)

def delta(
    m1: float,
    m2: float,
    q1: float,
    q2: float,
    r: float,
) -> float:

    return ((2 * m1 * m2 * (2 * m1**2 + 3 * m1 * m2 + 2 * m2**2)) / ((m1 + m2)**4)) * ((q1 * q2) / (r**5))