from psi_scalars import Kerr
import numpy as np
from transverse_frames import TransverseFrames, Invariants

r=np.arange(0.1,20,0.1)
no_of_angles=2
theta_range=np.append(np.arange(1/no_of_angles,1,1/no_of_angles)*np.pi/2,np.pi/2)

   
spacetime_classification={'r_axis':r}

for count,angle in enumerate(theta_range):
    
    classification={'angle':angle,
                   'root1':{'a':[],'b':[],'D':[],'S':[],'DN':[],'DN0':[]},
                   'root2':{'a':[],'b':[],'D':[],'S':[],'DN':[],'DN0':[]},
                   'root3':{'a':[],'b':[],'D':[],'S':[],'DN':[],'DN0':[]},
                   'root4':{'a':[],'b':[],'D':[],'S':[],'DN':[],'DN0':[]}
                   }
    
    #Initialize psi scalars
    spacetime=Kerr(M=1,a=0.7,th=angle)
    
    psi0,psi1,psi2,psi3,psi4=spacetime.psi0(r),spacetime.psi1(r),spacetime.psi2(r),spacetime.psi3(r),spacetime.psi4(r)
    
    
    for p0,p1,p2,p3,p4 in zip(psi0,psi1,psi2,psi3,psi4):
        TF=TransverseFrames(p0,p1,p2,p3,p4)
        coeffs=np.array([TF.coeff0(TF.ev_1()),TF.coeff1(TF.ev_1()),TF.coeff2(TF.ev_1()),TF.coeff3(TF.ev_1()),TF.coeff4(TF.ev_1())])
        a=np.roots(coeffs.flatten())
        for i in range(len(a)):
        #a=a[0]
            root_number='root'+str(i+1)
            classification[root_number]['a'].append(a[i])
            
            psi0_T,psi1_T,psi2_T,psi3_T,psi4_T=TF.rotate_to_transverse(a[i])
            
            classification[root_number]['D'].append(Invariants.D_index(psi0_T,psi1_T,psi2_T,psi3_T,psi4_T))
            classification[root_number]['S'].append(Invariants.S_index(psi0_T,psi1_T,psi2_T,psi3_T,psi4_T))
            classification[root_number]['DN'].append(Invariants.DN_index(psi0_T,psi1_T,psi2_T,psi3_T,psi4_T))
            classification[root_number]['DN0'].append(Invariants.DN0_index(psi0_T,psi1_T,psi2_T,psi3_T,psi4_T))
    
    
    spacetime_classification['angle'+str(count+1)]=classification
    
