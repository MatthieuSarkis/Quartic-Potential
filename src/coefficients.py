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

    num = 4096*alpha**4*delta**8+16384*alpha**3*beta*delta**8+24576*alpha**2*beta**2*delta**8+16384*alpha*beta**3*delta**8+4096*beta**4*delta**8+98304*alpha**2*delta**9*epsilon+196608*alpha*beta*delta**9*epsilon+98304*beta**2*delta**9*epsilon+65536*delta**10*epsilon**2+8192*alpha**3*beta*delta**7*gamma+24576*alpha**2*beta**2*delta**7*gamma+24576*alpha*beta**3*delta**7*gamma+8192*beta**4*delta**7*gamma+98304*alpha*beta*delta**8*epsilon*gamma+98304*beta**2*delta**8*epsilon*gamma+6144*alpha**2*beta**2*delta**6*gamma**2+12288*alpha*beta**3*delta**6*gamma**2+6144*beta**4*delta**6*gamma**2+4096*alpha**3*delta**7*gamma**2+12288*alpha**2*beta*delta**7*gamma**2+12288*alpha*beta**2*delta**7*gamma**2+4096*beta**3*delta**7*gamma**2+24576*beta**2*delta**7*epsilon*gamma**2+49152*alpha*delta**8*epsilon*gamma**2+49152*beta*delta**8*epsilon*gamma**2+2048*alpha*beta**3*delta**5*gamma**3+2048*beta**4*delta**5*gamma**3+2048*alpha**3*delta**6*gamma**3+12288*alpha**2*beta*delta**6*gamma**3+18432*alpha*beta**2*delta**6*gamma**3+8192*beta**3*delta**6*gamma**3+24576*alpha*delta**7*epsilon*gamma**3+49152*beta*delta**7*epsilon*gamma**3+256*beta**4*delta**4*gamma**4+3072*alpha**2*beta*delta**5*gamma**4+9216*alpha*beta**2*delta**5*gamma**4+6144*beta**3*delta**5*gamma**4+1536*alpha**2*delta**6*gamma**4+3072*alpha*beta*delta**6*gamma**4+1536*beta**2*delta**6*gamma**4+12288*beta*delta**6*epsilon*gamma**4+6144*delta**7*epsilon*gamma**4+1536*alpha*beta**2*delta**4*gamma**5+2048*beta**3*delta**4*gamma**5+1536*alpha**2*delta**5*gamma**5+4608*alpha*beta*delta**5*gamma**5+3072*beta**2*delta**5*gamma**5+6144*delta**6*epsilon*gamma**5+256*beta**3*delta**3*gamma**6+384*alpha**2*delta**4*gamma**6+2304*alpha*beta*delta**4*gamma**6+2304*beta**2*delta**4*gamma**6+256*alpha*delta**5*gamma**6+256*beta*delta**5*gamma**6+1536*delta**5*epsilon*gamma**6+384*alpha*beta*delta**3*gamma**7+768*beta**2*delta**3*gamma**7+384*alpha*delta**4*gamma**7+512*beta*delta**4*gamma**7+96*beta**2*delta**2*gamma**8+192*alpha*delta**3*gamma**8+384*beta*delta**3*gamma**8+16*delta**4*gamma**8+32*alpha*delta**2*gamma**9+128*beta*delta**2*gamma**9+32*delta**3*gamma**9+16*beta*delta*gamma**10+24*delta**2*gamma**10+8*delta*gamma**11+gamma**12+81920*alpha**3*delta**8.5*H+294912*alpha**2*beta*delta**8.5*H+344064*alpha*beta**2*delta**8.5*H+131072*beta**3*delta**8.5*H+131072*alpha**2*delta**9.5*H+131072*alpha*beta*delta**9.5*H+1376256*alpha*delta**9.5*epsilon*H+1572864*beta*delta**9.5*epsilon*H+122880*alpha**2*beta*delta**7.5*gamma*H+294912*alpha*beta**2*delta**7.5*gamma*H+172032*beta**3*delta**7.5*gamma*H+49152*alpha**2*delta**8.5*gamma*H+32768*alpha*beta*delta**8.5*gamma*H+49152*beta**2*delta**8.5*gamma*H+688128*beta*delta**8.5*epsilon*gamma*H+196608*delta**9.5*epsilon*gamma*H+61440*alpha*beta**2*delta**6.5*gamma**2*H+73728*beta**3*delta**6.5*gamma**2*H+73728*alpha**2*delta**7.5*gamma**2*H+221184*alpha*beta*delta**7.5*gamma**2*H+147456*beta**2*delta**7.5*gamma**2*H+32768*alpha*delta**8.5*gamma**2*H+393216*delta**8.5*epsilon*gamma**2*H+10240*beta**3*delta**5.5*gamma**3*H+30720*alpha**2*delta**6.5*gamma**3*H+147456*alpha*beta*delta**6.5*gamma**3*H+141312*beta**2*delta**6.5*gamma**3*H+8192*alpha*delta**7.5*gamma**3*H+24576*beta*delta**7.5*gamma**3*H+172032*delta**7.5*epsilon*gamma**3*H+30720*alpha*beta*delta**5.5*gamma**4*H+55296*beta**2*delta**5.5*gamma**4*H+33792*alpha*delta**6.5*gamma**4*H+49152*beta*delta**6.5*gamma**4*H+7680*beta**2*delta**4.5*gamma**5*H+18432*alpha*delta**5.5*gamma**5*H+38400*beta*delta**5.5*gamma**5*H+3072*delta**6.5*gamma**5*H+3840*alpha*delta**4.5*gamma**6*H+13824*beta*delta**4.5*gamma**6*H+5120*delta**5.5*gamma**6*H+1920*beta*delta**3.5*gamma**7*H+3456*delta**4.5*gamma**7*H+1152*delta**3.5*gamma**8*H+160*delta**2.5*gamma**9*H+573440*alpha**2*delta**9*H**2+1703936*alpha*beta*delta**9*H**2+1179648*beta**2*delta**9*H**2+1310720*alpha*delta**10*H**2+393216*beta*delta**10*H**2+4718592*delta**10*epsilon*H**2+573440*alpha*beta*delta**8*gamma*H**2+851968*beta**2*delta**8*gamma*H**2+688128*alpha*delta**9*gamma*H**2+655360*beta*delta**9*gamma*H**2+143360*beta**2*delta**7*gamma**2*H**2+425984*alpha*delta**8*gamma**2*H**2+933888*beta*delta**8*gamma**2*H**2+16384*delta**9*gamma**2*H**2+143360*alpha*delta**7*gamma**3*H**2+425984*beta*delta**7*gamma**3*H**2+163840*delta**8*gamma**3*H**2+71680*beta*delta**6*gamma**4*H**2+159744*delta**7*gamma**4*H**2+53248*delta**6*gamma**5*H**2+8960*delta**5*gamma**6*H**2+1638400*alpha*delta**9.5*H**3+3145728*beta*delta**9.5*H**3+2097152*delta**10.5*H**3+819200*beta*delta**8.5*gamma*H**3+2359296*delta**9.5*gamma*H**3+786432*delta**8.5*gamma**2*H**3+204800*delta**7.5*gamma**3*H**3+1572864*delta**10*H**4+32768*alpha**3*delta**8.5*H*S+98304*alpha**2*beta*delta**8.5*H*S+98304*alpha*beta**2*delta**8.5*H*S+32768*beta**3*delta**8.5*H*S+131072*alpha*delta**9.5*epsilon*H*S+131072*beta*delta**9.5*epsilon*H*S+49152*alpha**2*beta*delta**7.5*gamma*H*S+98304*alpha*beta**2*delta**7.5*gamma*H*S+49152*beta**3*delta**7.5*gamma*H*S+65536*beta*delta**8.5*epsilon*gamma*H*S+24576*alpha*beta**2*delta**6.5*gamma**2*H*S+24576*beta**3*delta**6.5*gamma**2*H*S+24576*alpha**2*delta**7.5*gamma**2*H*S+49152*alpha*beta*delta**7.5*gamma**2*H*S+24576*beta**2*delta**7.5*gamma**2*H*S+32768*delta**8.5*epsilon*gamma**2*H*S+4096*beta**3*delta**5.5*gamma**3*H*S+12288*alpha**2*delta**6.5*gamma**3*H*S+49152*alpha*beta*delta**6.5*gamma**3*H*S+36864*beta**2*delta**6.5*gamma**3*H*S+16384*delta**7.5*epsilon*gamma**3*H*S+12288*alpha*beta*delta**5.5*gamma**4*H*S+18432*beta**2*delta**5.5*gamma**4*H*S+6144*alpha*delta**6.5*gamma**4*H*S+6144*beta*delta**6.5*gamma**4*H*S+3072*beta**2*delta**4.5*gamma**5*H*S+6144*alpha*delta**5.5*gamma**5*H*S+9216*beta*delta**5.5*gamma**5*H*S+1536*alpha*delta**4.5*gamma**6*H*S+4608*beta*delta**4.5*gamma**6*H*S+512*delta**5.5*gamma**6*H*S+768*beta*delta**3.5*gamma**7*H*S+768*delta**4.5*gamma**7*H*S+384*delta**3.5*gamma**8*H*S+64*delta**2.5*gamma**9*H*S+589824*alpha**2*delta**9*H**2*S+1376256*alpha*beta*delta**9*H**2*S+786432*beta**2*delta**9*H**2*S+131072*alpha*delta**10*H**2*S+1048576*delta**10*epsilon*H**2*S+589824*alpha*beta*delta**8*gamma*H**2*S+688128*beta**2*delta**8*gamma*H**2*S+196608*alpha*delta**9*gamma*H**2*S+196608*beta*delta**9*gamma*H**2*S+147456*beta**2*delta**7*gamma**2*H**2*S+344064*alpha*delta**8*gamma**2*H**2*S+491520*beta*delta**8*gamma**2*H**2*S+147456*alpha*delta**7*gamma**3*H**2*S+344064*beta*delta**7*gamma**3*H**2*S+49152*delta**8*gamma**3*H**2*S+73728*beta*delta**6*gamma**4*H**2*S+73728*delta**7*gamma**4*H**2*S+43008*delta**6*gamma**5*H**2*S+9216*delta**5*gamma**6*H**2*S+3407872*alpha*delta**9.5*H**3*S+4718592*beta*delta**9.5*H**3*S+524288*delta**10.5*H**3*S+1703936*beta*delta**8.5*gamma*H**3*S+1572864*delta**9.5*gamma*H**3*S+1179648*delta**8.5*gamma**2*H**3*S+425984*delta**7.5*gamma**3*H**3*S+6291456*delta**10*H**4*S
    den = 1572864*delta**10*H**4

    coef = num / den

    return coef

def coefMinus(
    epsilon: float,
    S: float,
    alpha: float,
    beta: float,
    gamma: float,
    delta: float,
    H: float
) -> float:

    num = 4096*alpha**4*delta**8+16384*alpha**3*beta*delta**8+24576*alpha**2*beta**2*delta**8+16384*alpha*beta**3*delta**8+4096*beta**4*delta**8+98304*alpha**2*delta**9*epsilon+196608*alpha*beta*delta**9*epsilon+98304*beta**2*delta**9*epsilon+65536*delta**10*epsilon**2+8192*alpha**3*beta*delta**7*gamma+24576*alpha**2*beta**2*delta**7*gamma+24576*alpha*beta**3*delta**7*gamma+8192*beta**4*delta**7*gamma+98304*alpha*beta*delta**8*epsilon*gamma+98304*beta**2*delta**8*epsilon*gamma+6144*alpha**2*beta**2*delta**6*gamma**2+12288*alpha*beta**3*delta**6*gamma**2+6144*beta**4*delta**6*gamma**2+4096*alpha**3*delta**7*gamma**2+12288*alpha**2*beta*delta**7*gamma**2+12288*alpha*beta**2*delta**7*gamma**2+4096*beta**3*delta**7*gamma**2+24576*beta**2*delta**7*epsilon*gamma**2+49152*alpha*delta**8*epsilon*gamma**2+49152*beta*delta**8*epsilon*gamma**2+2048*alpha*beta**3*delta**5*gamma**3+2048*beta**4*delta**5*gamma**3+2048*alpha**3*delta**6*gamma**3+12288*alpha**2*beta*delta**6*gamma**3+18432*alpha*beta**2*delta**6*gamma**3+8192*beta**3*delta**6*gamma**3+24576*alpha*delta**7*epsilon*gamma**3+49152*beta*delta**7*epsilon*gamma**3+256*beta**4*delta**4*gamma**4+3072*alpha**2*beta*delta**5*gamma**4+9216*alpha*beta**2*delta**5*gamma**4+6144*beta**3*delta**5*gamma**4+1536*alpha**2*delta**6*gamma**4+3072*alpha*beta*delta**6*gamma**4+1536*beta**2*delta**6*gamma**4+12288*beta*delta**6*epsilon*gamma**4+6144*delta**7*epsilon*gamma**4+1536*alpha*beta**2*delta**4*gamma**5+2048*beta**3*delta**4*gamma**5+1536*alpha**2*delta**5*gamma**5+4608*alpha*beta*delta**5*gamma**5+3072*beta**2*delta**5*gamma**5+6144*delta**6*epsilon*gamma**5+256*beta**3*delta**3*gamma**6+384*alpha**2*delta**4*gamma**6+2304*alpha*beta*delta**4*gamma**6+2304*beta**2*delta**4*gamma**6+256*alpha*delta**5*gamma**6+256*beta*delta**5*gamma**6+1536*delta**5*epsilon*gamma**6+384*alpha*beta*delta**3*gamma**7+768*beta**2*delta**3*gamma**7+384*alpha*delta**4*gamma**7+512*beta*delta**4*gamma**7+96*beta**2*delta**2*gamma**8+192*alpha*delta**3*gamma**8+384*beta*delta**3*gamma**8+16*delta**4*gamma**8+32*alpha*delta**2*gamma**9+128*beta*delta**2*gamma**9+32*delta**3*gamma**9+16*beta*delta*gamma**10+24*delta**2*gamma**10+8*delta*gamma**11+gamma**12+81920*alpha**3*delta**8.5*H+294912*alpha**2*beta*delta**8.5*H+344064*alpha*beta**2*delta**8.5*H+131072*beta**3*delta**8.5*H+131072*alpha**2*delta**9.5*H+131072*alpha*beta*delta**9.5*H+1376256*alpha*delta**9.5*epsilon*H+1572864*beta*delta**9.5*epsilon*H+122880*alpha**2*beta*delta**7.5*gamma*H+294912*alpha*beta**2*delta**7.5*gamma*H+172032*beta**3*delta**7.5*gamma*H+49152*alpha**2*delta**8.5*gamma*H+32768*alpha*beta*delta**8.5*gamma*H+49152*beta**2*delta**8.5*gamma*H+688128*beta*delta**8.5*epsilon*gamma*H+196608*delta**9.5*epsilon*gamma*H+61440*alpha*beta**2*delta**6.5*gamma**2*H+73728*beta**3*delta**6.5*gamma**2*H+73728*alpha**2*delta**7.5*gamma**2*H+221184*alpha*beta*delta**7.5*gamma**2*H+147456*beta**2*delta**7.5*gamma**2*H+32768*alpha*delta**8.5*gamma**2*H+393216*delta**8.5*epsilon*gamma**2*H+10240*beta**3*delta**5.5*gamma**3*H+30720*alpha**2*delta**6.5*gamma**3*H+147456*alpha*beta*delta**6.5*gamma**3*H+141312*beta**2*delta**6.5*gamma**3*H+8192*alpha*delta**7.5*gamma**3*H+24576*beta*delta**7.5*gamma**3*H+172032*delta**7.5*epsilon*gamma**3*H+30720*alpha*beta*delta**5.5*gamma**4*H+55296*beta**2*delta**5.5*gamma**4*H+33792*alpha*delta**6.5*gamma**4*H+49152*beta*delta**6.5*gamma**4*H+7680*beta**2*delta**4.5*gamma**5*H+18432*alpha*delta**5.5*gamma**5*H+38400*beta*delta**5.5*gamma**5*H+3072*delta**6.5*gamma**5*H+3840*alpha*delta**4.5*gamma**6*H+13824*beta*delta**4.5*gamma**6*H+5120*delta**5.5*gamma**6*H+1920*beta*delta**3.5*gamma**7*H+3456*delta**4.5*gamma**7*H+1152*delta**3.5*gamma**8*H+160*delta**2.5*gamma**9*H+573440*alpha**2*delta**9*H**2+1703936*alpha*beta*delta**9*H**2+1179648*beta**2*delta**9*H**2+1310720*alpha*delta**10*H**2+393216*beta*delta**10*H**2+4718592*delta**10*epsilon*H**2+573440*alpha*beta*delta**8*gamma*H**2+851968*beta**2*delta**8*gamma*H**2+688128*alpha*delta**9*gamma*H**2+655360*beta*delta**9*gamma*H**2+143360*beta**2*delta**7*gamma**2*H**2+425984*alpha*delta**8*gamma**2*H**2+933888*beta*delta**8*gamma**2*H**2+16384*delta**9*gamma**2*H**2+143360*alpha*delta**7*gamma**3*H**2+425984*beta*delta**7*gamma**3*H**2+163840*delta**8*gamma**3*H**2+71680*beta*delta**6*gamma**4*H**2+159744*delta**7*gamma**4*H**2+53248*delta**6*gamma**5*H**2+8960*delta**5*gamma**6*H**2+1638400*alpha*delta**9.5*H**3+3145728*beta*delta**9.5*H**3+2097152*delta**10.5*H**3+819200*beta*delta**8.5*gamma*H**3+2359296*delta**9.5*gamma*H**3+786432*delta**8.5*gamma**2*H**3+204800*delta**7.5*gamma**3*H**3+1572864*delta**10*H**4+32768*alpha**3*delta**8.5*H*S+98304*alpha**2*beta*delta**8.5*H*S+98304*alpha*beta**2*delta**8.5*H*S+32768*beta**3*delta**8.5*H*S+131072*alpha*delta**9.5*epsilon*H*S+131072*beta*delta**9.5*epsilon*H*S+49152*alpha**2*beta*delta**7.5*gamma*H*S+98304*alpha*beta**2*delta**7.5*gamma*H*S+49152*beta**3*delta**7.5*gamma*H*S+65536*beta*delta**8.5*epsilon*gamma*H*S+24576*alpha*beta**2*delta**6.5*gamma**2*H*S+24576*beta**3*delta**6.5*gamma**2*H*S+24576*alpha**2*delta**7.5*gamma**2*H*S+49152*alpha*beta*delta**7.5*gamma**2*H*S+24576*beta**2*delta**7.5*gamma**2*H*S+32768*delta**8.5*epsilon*gamma**2*H*S+4096*beta**3*delta**5.5*gamma**3*H*S+12288*alpha**2*delta**6.5*gamma**3*H*S+49152*alpha*beta*delta**6.5*gamma**3*H*S+36864*beta**2*delta**6.5*gamma**3*H*S+16384*delta**7.5*epsilon*gamma**3*H*S+12288*alpha*beta*delta**5.5*gamma**4*H*S+18432*beta**2*delta**5.5*gamma**4*H*S+6144*alpha*delta**6.5*gamma**4*H*S+6144*beta*delta**6.5*gamma**4*H*S+3072*beta**2*delta**4.5*gamma**5*H*S+6144*alpha*delta**5.5*gamma**5*H*S+9216*beta*delta**5.5*gamma**5*H*S+1536*alpha*delta**4.5*gamma**6*H*S+4608*beta*delta**4.5*gamma**6*H*S+512*delta**5.5*gamma**6*H*S+768*beta*delta**3.5*gamma**7*H*S+768*delta**4.5*gamma**7*H*S+384*delta**3.5*gamma**8*H*S+64*delta**2.5*gamma**9*H*S+589824*alpha**2*delta**9*H**2*S+1376256*alpha*beta*delta**9*H**2*S+786432*beta**2*delta**9*H**2*S+131072*alpha*delta**10*H**2*S+1048576*delta**10*epsilon*H**2*S+589824*alpha*beta*delta**8*gamma*H**2*S+688128*beta**2*delta**8*gamma*H**2*S+196608*alpha*delta**9*gamma*H**2*S+196608*beta*delta**9*gamma*H**2*S+147456*beta**2*delta**7*gamma**2*H**2*S+344064*alpha*delta**8*gamma**2*H**2*S+491520*beta*delta**8*gamma**2*H**2*S+147456*alpha*delta**7*gamma**3*H**2*S+344064*beta*delta**7*gamma**3*H**2*S+49152*delta**8*gamma**3*H**2*S+73728*beta*delta**6*gamma**4*H**2*S+73728*delta**7*gamma**4*H**2*S+43008*delta**6*gamma**5*H**2*S+9216*delta**5*gamma**6*H**2*S+3407872*alpha*delta**9.5*H**3*S+4718592*beta*delta**9.5*H**3*S+524288*delta**10.5*H**3*S+1703936*beta*delta**8.5*gamma*H**3*S+1572864*delta**9.5*gamma*H**3*S+1179648*delta**8.5*gamma**2*H**3*S+425984*delta**7.5*gamma**3*H**3*S+6291456*delta**10*H**4*S
    den = 1572864*delta**10*H**4

    return num / den