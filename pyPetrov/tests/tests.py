import numpy as np


def is_equal_shape(psi0: np.array,psi1:np.array,psi2:np.array,psi3:np.array,psi4:np.array)-> bool:
    if psi0.shape==psi1.shape and psi0.shape==psi2.shape and psi0.shape==psi3.shape and psi0.shape==psi3.shape:
        return True
    else:
        return False
    
