import numpy as np

def coefPlus(
    epsilon: float,
    S: float,
    alpha: float,
    beta: float,
    gamma: float,
    delta: float,
    H: float
) -> float:

    aux0=(((3.*alpha)+((9.*beta)+(6.*(H*((2.+S)*(np.sqrt(delta)))))))-\
    delta)*(delta**2)
    aux1=(3.*(beta*delta))+(2.*((alpha+(H*((5.+(2.*S))*(np.sqrt(delta)))))*\
    delta))
    aux2=(-4.*(H*((2.+S)*(beta*(np.sqrt(delta))))))+(((alpha+beta)*delta)+(\
    2.*(H*((5.+S)*(delta**1.5)))))
    aux3=(beta**2)+((2.*(H*((2.+S)*(beta*(np.sqrt(delta))))))+(-2.*(H*(\
    delta**1.5))))
    aux4=delta*((H*((11.*H)+((15.*(H*S))+(-3.*(np.sqrt(delta))))))+(-3.*\
    epsilon))
    aux5=(-24.*((H**2)*((3.+S)*(delta**2))))+((6.*(alpha*aux3))+(4.*(beta*\
    aux4)))
    aux6=(3.*(beta**3.))+((6.*(H*((5.+(2.*S))*((beta**2)*(np.sqrt(delta))))\
    ))+aux5)
    aux7=alpha*(((2.*(beta*delta))+(2.*(H*((5.+(2.*S))*(delta**1.5)))))-(\
    beta**2))
    aux8=(4.*(H*((4.+S)*(beta*(delta**1.5)))))+(aux7+(4.*((delta**2)*((6.*\
    ((H**2)*(1.+S)))-epsilon))))
    aux9=(-2.*(H*((2.+S)*((beta**2)*(np.sqrt(delta))))))+(((alpha**2)*\
    delta)+(((beta**2)*delta)+aux8))
    aux10=((3.*((2.+S)*alpha))+((H*((11.+(15.*S))*(np.sqrt(delta))))+(-3.*\
    delta)))*(delta**1.5)
    aux11=(-12.*(H*((5.+(2.*S))*(beta*(delta**1.5)))))+((-4.*(H*aux10))+(\
    12.*((delta**2)*epsilon)))
    aux12=(-3.*((alpha**2)*delta))+((-12.*(alpha*(beta*delta)))+((-9.*((\
    beta**2)*delta))+aux11))
    aux13=4.*(delta*((H*((11.*H)+((15.*(H*S))+(2.*(np.sqrt(delta))))))+(-3.\
    *epsilon)))
    aux14=alpha*((3.*(beta**2))+((6.*(H*((5.+(2.*S))*(beta*(np.sqrt(delta))\
    ))))+aux13))
    aux15=(delta**1.5)*((2.*(H*((3.*H)+((9.*(H*S))+(np.sqrt(delta))))))-((\
    9.+S)*epsilon))
    aux16=aux14+((12.*(beta*(delta*((6.*((H**2)*(1.+S)))-epsilon))))+(8.*(\
    H*aux15)))
    aux17=(3.*((alpha**2)*(beta+(2.*(H*((2.+S)*(np.sqrt(delta))))))))+((6.*\
    (H*((3.+S)*((beta**2)*(np.sqrt(delta))))))+aux16)
    aux18=(-64.*((gamma**3.)*((delta**3.)*((beta**3.)+aux12))))+(512.*((\
    delta**6.)*((alpha**3.)+((beta**3.)+aux17))))
    aux19=(-256.*(gamma*((delta**5.)*((3.*((alpha**2)*beta))+aux6))))+((-\
    384.*((gamma**2)*((delta**4.)*(aux9-(beta**3.)))))+aux18)
    aux20=(96.*((gamma**4.)*((delta**3.)*(aux2-(beta*((2.*alpha)+(3.*beta)\
    ))))))+aux19
    aux21=(12.*((gamma**7.)*(delta*(delta-beta))))+((-48.*((gamma**5.)*((\
    delta**2)*(aux1-(beta**2)))))+aux20)
    aux22=(gamma**9.)+((-6.*((gamma**8.)*delta))+((8.*((gamma**6.)*aux0))+\
    aux21))
    output=0.0000406901*((H**-3.)*((delta**-7.5)*aux22))

    return output

def coefMinus(
    epsilon: float,
    S: float,
    alpha: float,
    beta: float,
    gamma: float,
    delta: float,
    H: float
) -> float:

    aux0=(delta**2)*((3.*alpha)+((-9.*beta)+((6.*(H*((-2.+S)*(np.sqrt(\
    delta)))))+delta)))
    aux1=(-3.*(beta*delta))+(2.*((alpha+(H*((-5.+(2.*S))*(np.sqrt(delta))))\
    )*delta))
    aux2=(4.*(H*((-2.+S)*(beta*(np.sqrt(delta))))))+(((beta-alpha)*delta)+(\
    -2.*(H*((-5.+S)*(delta**1.5)))))
    aux3=(-3.*((-2.+S)*alpha))+((H*((-11.+(15.*S))*(np.sqrt(delta))))+(3.*\
    delta))
    aux4=(12.*(beta*((alpha+(H*((-5.+(2.*S))*(np.sqrt(delta)))))*delta)))+(\
    (4.*(H*((delta**1.5)*aux3)))+(12.*((delta**2)*epsilon)))
    aux5=(delta**3.)*((beta**3.)+((-3.*((alpha**2)*delta))+((-9.*((beta**\
    2)*delta))+aux4)))
    aux6=alpha*(((2.*(beta*delta))+(2.*(H*((5.+(-2.*S))*(delta**1.5)))))-(\
    beta**2))
    aux7=(4.*(H*((-4.+S)*(beta*(delta**1.5)))))+(aux6+(4.*((delta**2)*((6.\
    *((H**2)*(-1.+S)))+epsilon))))
    aux8=((beta**3.)+((-2.*(H*((-2.+S)*((beta**2)*(np.sqrt(delta))))))+\
    aux7))-((beta**2)*delta)
    aux9=((2.*(H*((-2.+S)*(beta*(np.sqrt(delta))))))+(2.*(H*(delta**1.5))))\
    -(beta**2)
    aux10=beta*(delta*((H*((-11.*H)+((15.*(H*S))+(3.*(np.sqrt(delta))))))+(\
    3.*epsilon)))
    aux11=(6.*(H*((5.+(-2.*S))*((beta**2)*(np.sqrt(delta))))))+((24.*((H**\
    2)*((-3.+S)*(delta**2))))+((6.*(alpha*aux9))+(-4.*aux10)))
    aux12=256.*(gamma*((delta**5.)*((3.*((alpha**2)*beta))+((3.*(beta**3.)\
    )+aux11))))
    aux13=(delta**1.5)*((2.*(H*((3.*H)+((-9.*(H*S))+(np.sqrt(delta))))))+((\
    -9.+S)*epsilon))
    aux14=delta*((H*((-11.*H)+((15.*(H*S))+(-2.*(np.sqrt(delta))))))+(3.*\
    epsilon))
    aux15=(-3.*(beta**2))+((6.*(H*((-5.+(2.*S))*(beta*(np.sqrt(delta))))))+\
    (4.*aux14))
    aux16=(-12.*(beta*(delta*((6.*((H**2)*(-1.+S)))+epsilon))))+((8.*(H*\
    aux13))+(alpha*aux15))
    aux17=(3.*((alpha**2)*(beta+(-2.*(H*((-2.+S)*(np.sqrt(delta))))))))+((-\
    6.*(H*((-3.+S)*((beta**2)*(np.sqrt(delta))))))+aux16)
    aux18=(384.*((gamma**2)*((delta**4.)*(aux8-((alpha**2)*delta)))))+(\
    aux12+(512.*((delta**6.)*(((beta**3.)+aux17)-(alpha**3.)))))
    aux19=(96.*((gamma**4.)*((delta**3.)*((((2.*alpha)+(-3.*beta))*beta)+\
    aux2))))+((64.*((gamma**3.)*aux5))+aux18)
    aux20=(-8.*((gamma**6.)*aux0))+((-48.*((gamma**5.)*((delta**2)*((beta**\
    2)+aux1))))+aux19)
    aux21=(-6.*((gamma**8.)*delta))+((12.*((gamma**7.)*((beta-delta)*\
    delta)))+aux20)
    output=0.0000406901*((H**-3.)*((delta**-7.5)*(aux21-(gamma**9.))))

    return output