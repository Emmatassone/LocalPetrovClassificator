from .__invariants import Invariants as Inv
from numpy import sqrt,exp,pi,ones
from scipy.optimize import fsolve
import numpy as np
#from scipy.optimize import root

class TransverseFrames:
    
    def __init__(self,psi0:float, psi1:float, psi2:float, psi3:float, psi4:float):
        self.J=Inv.J_invariant(psi0, psi1, psi2, psi3, psi4)
        self.I=Inv.I_invariant(psi0, psi1, psi2, psi3, psi4)
        self.P=(self.J+sqrt(self.J**2-(self.I/3)**3))**(1/3)
        
        self.psi0, self.psi1, self.psi2, self.psi3, self.psi4=psi0, psi1, psi2, psi3, psi4
    
    def ev_1(self)-> complex:
        return -(self.P+self.I/(3*self.P))
    
    def ev_2(self)-> complex:
        return -(self.P*exp(4*pi*self.I/3)+self.I*exp(2*pi*self.I/3)/(3*self.P))
    
    def ev_3(self)-> complex:
        return -(self.P*exp(2*pi*self.I/3)+self.I*exp(4*pi*self.I/3)/(3*self.P))
        

    
    def null_rotation_I(self,a:float)-> (complex,complex,complex,complex,complex):
        return [
            self.psi0,
            self.psi1+a*self.psi0,
            self.psi2 + 2*a*self.psi1 + a**2*self.psi0,
            self.psi3 + 3*a*self.psi2 + 3*a**2*self.psi1 + a**3*self.psi0,
            self.psi4 + 4*a*self.psi3 + 6*a**2*self.psi2 + 4*a**3*self.psi1 +  a**4*self.psi0
            ]
    
    def null_rotation_II(self, b:float, psi0:complex, psi1:complex, psi2:complex, psi3:complex, psi4:complex)-> (complex,complex,complex,complex,complex):
        return [
            psi0 + 4*b*psi1 + 6*b**2*psi2 + 4*b**3*psi3 + b**4*psi4,
            psi1 + 3*b*psi2 + 3*b**2*psi3 + b**3*psi4,
            psi2 + 2*b*psi3 + b**2*psi4,
            psi3 + b*psi4,
            psi4
            ]
      
    def Hhat(self)-> complex:
        return self.psi4*self.psi2 - self.psi3**2
    
    def eigenvector_equation(self, lamb)-> complex:
        return 2*self.psi4*lamb - 4*self.Hhat(self.psi0, self.psi1, self.psi2, self.psi3, self.psi4)
    
    def rotated_alpha(self,a:float)-> complex:
        return self.ev_1()*(2*a**4*self.psi0 + 8*a**3*self.psi1 + 12*a**2*self.psi2 + 8*a*self.psi3 + 2*self.psi4) - 4*(a**2*self.psi0 + 2*a*self.psi1 + self.psi2)*(a**4*self.psi0 + 4*a**3*self.psi1 + 6*a**2*self.psi2 + 4*a*self.psi3 + self.psi4) + 4*(a**3*self.psi0 + 3*a**2*self.psi1 + 3*a*self.psi2 + self.psi3)**2
    
    def rotated_beta(self,a:float)-> complex:
        Rpsi0, Rpsi1, Rpsi2, Rpsi3, Rpsi4=self.null_rotation_I(a, self.psi0, self.psi1, self.psi2, self.psi3, self.psi4)
        return self.eigenvector_equation(self.ev_2(), Rpsi0, Rpsi1, Rpsi2, Rpsi3, Rpsi4)
    
    def rotated_gamma(self,a:float)-> complex:
        Rpsi0, Rpsi1, Rpsi2, Rpsi3, Rpsi4=self.null_rotation_I(a, self.psi0, self.psi1, self.psi2, self.psi3, self.psi4)
        return self.eigenvector_equation(self.ev_3(), Rpsi0, Rpsi1, Rpsi2, Rpsi3, Rpsi4)
    
    def typeII_rotation_parameter(self,a:float)-> complex:
        return -((self.psi3 + 3*a*self.psi2 + 3*a**2*self.psi1 + a**3*self.psi0)/(self.psi4 + 4*a*self.psi3 + 6*a**2*self.psi2 + 4*a**3*self.psi1 + a**4*self.psi0))
    
    def rotate_to_transverse(self,a_T:float) -> (complex,complex,complex,complex,complex):
        b_T=self.typeII_rotation_parameter(a_T)
        Rpsi0,Rpsi1,Rpsi2,Rpsi3,Rpsi4=self.null_rotation_I(a_T)
        return self.null_rotation_II(b_T,Rpsi0,Rpsi1,Rpsi2,Rpsi3,Rpsi4)
    
    def coeff0(self,lamb):
        return (2*lamb*self.psi0 - 4*self.psi0*self.psi2 + 4*self.psi1**2)
    
    def coeff1(self,lamb):
        return (8*lamb*self.psi1 - 8*self.psi0*self.psi3 + 8*self.psi1*self.psi2)
    
    def coeff2(self,lamb):
        return (12*lamb*self.psi2 - 4*self.psi0*self.psi4 - 8*self.psi1*self.psi3 + 12*self.psi2**2)

    def coeff3(self,lamb):
        return (8*lamb*self.psi3 - 8*self.psi1*self.psi4 + 8*self.psi2*self.psi3)
    
    def coeff4(self,lamb):
        return 2*lamb*self.psi4 - 4*self.psi2*self.psi4 + 4*self.psi3**2
    
        
         
    
    