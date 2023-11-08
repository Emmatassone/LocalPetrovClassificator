from numpy import sqrt,array
from numpy.linalg import det

class Invariants:
    
    def I_invariant(psi0: float,psi1:float,psi2:float,psi3:float,psi4:float)-> complex:
           return psi4*psi0 - 4*psi3*psi1 + 3*psi2**2
    
    def J_invariant(psi0: float,psi1:float,psi2:float,psi3:float,psi4:float)-> complex:
        """
           This is a description of my_function.
    
           Parameters
           ----------
           arg1 : np.ndarray
               Description of arg1. It should be a NumPy array.
           arg2 : np.ndarray
               Description of arg2. It should be a NumPy array.
    
           Returns
           -------
           tuple of np.ndarray
               This function returns two NumPy arrays.
       """
        _M=[[psi4,psi3,psi2],
            [psi3,psi2,psi1],
            [psi2,psi1,psi0]]
        
        return det(array(_M))
    
    def D_index(psi0: float,psi1:float,psi2:float,psi3:float,psi4:float)-> complex:
        return sqrt(12/Invariants.I_invariant(psi0, psi1, psi2, psi3, psi4))*(psi2-psi3**2/psi4**2)
    
    def S_index(psi0: float,psi1:float,psi2:float,psi3:float,psi4:float)-> complex:
        return 27*Invariants.J_invariant(psi0, psi1, psi2, psi3, psi4)**2/Invariants.I_invariant(psi0, psi1, psi2, psi3, psi4)**3
    
    def DN_index(psi0: float,psi1:float,psi2:float,psi3:float,psi4:float)-> complex:
        return sqrt(Invariants.I_invariant(psi0, psi1, psi2, psi3, psi4)/12)*psi4/(psi2-psi3**2)
    
    def DN0_index(psi0: float,psi1:float,psi2:float,psi3:float,psi4:float)-> complex:
        return 9*(psi2-psi1**2/psi0)

    
    