import pandas as pd
from scipy import stats
import math

def sample_size_estimate(data, known=False, p=0.5, e=0.03, alpha=0.05):
    """With known as False,
    n = (z^2)*p(1-p) / (e^2)
    if known is True,
     n = (z^2)*p(1-p) / ((e^2)+(z^2)*p(1-p)/N)
    """
    z2 = (stats.norm.ppf(alpha/2))**2
    e2 = e**2
    s2 = p*(1-p)
    #print(z2, e2, s2)
    if known == False:
        n = z2*s2/e2
    else:
        N = data.shape[0]
        n = z2*s2/(e2+(z2*s2)/N)
    return math.ceil(n)

