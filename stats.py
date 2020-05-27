import numpy as np 
import matplotlib.pyplot as plt 


def _ecdf(ara1d):
    n = len(ara1d)
    x = np.sort(ara1d)
    y = np.arange(1, n+1)/n
    return x,y



