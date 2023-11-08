from psi_scalars import Kerr
import numpy as np

r=np.arange(0.1,20,0.1)
no_of_angles=128
theta_range=np.arange(1/no_of_angles,1,1/no_of_angles)*np.pi/2

#Initialize psi scalars
spacetime=Kerr(M=1,a=0.7,th=0)

psi0p,psi1p,psi2p,psi3p,psi4p=spacetime.psi0(r),spacetime.psi1(r),spacetime.psi2(r),spacetime.psi3(r),spacetime.psi4(r)
from transverse_frames import TransverseFrames
TF=TransverseFrames(psi0p,psi1p,psi2p,psi3p,psi4p)
lamb_1=TF.ev_1()

import sympy as sp

# Define symbols
a, lamb = sp.symbols('a lamb')
psi0, psi1, psi2, psi3, psi4 = sp.symbols('psi0 psi1 psi2 psi3 psi4')

# Define the null rotation operation
def null_rotation_I(a, psi0, psi1, psi2, psi3, psi4):
    return [
        psi0,
        psi1 + a*psi0,
        psi2 + 2*a*psi1 + a**2*psi0,
        psi3 + 3*a*psi2 + 3*a**2*psi1 + a**3*psi0,
        psi4 + 4*a*psi3 + 6*a**2*psi2 + 4*a**3*psi1 +  a**4*psi0
    ]

# Define the eigenvector equation
def eigenvector_equation(lamb, psi0, psi1, psi2, psi3, psi4):
    return 2*psi4*lamb - 4*Hhat(psi0, psi1, psi2, psi3, psi4)

# Define the rotated_alpha function
def rotated_alpha(a):
    Rpsi0, Rpsi1, Rpsi2, Rpsi3, Rpsi4 = null_rotation_I(a, psi0, psi1, psi2, psi3, psi4)
    return eigenvector_equation(lamb, Rpsi0, Rpsi1, Rpsi2, Rpsi3, Rpsi4)

# Define Hhat function (you'll need to provide this function)
def Hhat(psi0, psi1, psi2, psi3, psi4):
    # Define your Hhat function here
    return psi4*psi2 - psi3**2

a_parameter=[]
for p0,p1,p2,p3,p4,value in zip(psi0p,psi1p,psi2p,psi3p,psi4p,lamb_1):
    # Now you can use sympy to solve the equation rotated_alpha = 0
    specific_equation = rotated_alpha(a).subs(psi0, p0)
    specific_equation = specific_equation.subs(psi1, p1)
    specific_equation = specific_equation.subs(psi2, p2)
    specific_equation = specific_equation.subs(psi3, p3)
    specific_equation = specific_equation.subs(psi4, p4)
    specific_equation = specific_equation.subs(lamb, value)
    
    sol=np.roots(specific_equation)
    
    a_parameter.append(sol)
    
print(a_parameter)