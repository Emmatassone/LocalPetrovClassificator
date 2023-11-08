from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class Visualizer:
    def __init__(self, spacetime_classification):
        self.classification=spacetime_classification
        
    def plot_Dindex_curve(self,roots='All',spacetime_name='Spacetime', angle_axis='angle1'):
        
        sns.set(style = "darkgrid")
        
        if roots=='All':
            for i in range(4):
                Dindex=np.real(self.classification[angle_axis]['root'+str(i+1)]['D'])
                if len(self.classification['r_axis'])==len(Dindex):
                    plt.plot(self.classification['r_axis'], Dindex, ls=(0,(5,2*i)),label='root'+str(i+1))
                else:
                    continue
                
        else:
            plt.plot(self.classification['r_axis'], self.classification[angle_axis]['D'])
            
        
        angle_string=str(round(self.classification[angle_axis]['angle'],2))
        plt.xlabel("r",color='forestgreen')
        plt.ylabel("$\mathcal{D}$",color='forestgreen',rotation=0)
        plt.title("$\mathcal{D}$ index")
        plt.text(0.5, 2.5, r"$\theta$ =" + angle_string)
        plt.ylim(-3, 3)
        plt.legend()
        
        save_filename=spacetime_name+'_Dindex_'+angle_string+'.png' 
        plt.savefig(save_filename)
        
        return
    
    def plot_classification_surface(self, angle_view_th=30 ,angle_view_phi=30, spacetime_name='Spacetime'):

        sns.set(style = "darkgrid")

        fig = plt.figure()
        ax = fig.add_subplot(111, projection = '3d')

        ax.set_xlabel("x",color='forestgreen')
        ax.set_ylabel("z",color='forestgreen')
        ax.zaxis.set_rotate_label(False) 
        ax.set_zlabel("$\mathcal{D}$",rotation=0)
        plt.title(spacetime_name+' Petrov Structure')
        im=ax.scatter(self.x_range, self.z_range, self.Dindex , c=self.Sindex, vmin=0, vmax=1,cmap='rocket_r')
        fig.colorbar(im,label='S',location = 'left').ax.set_ylabel('S', rotation=0, fontsize = 15, labelpad=0,loc='bottom',color='darkred')

        
        ax.view_init(angle_view_th,angle_view_phi)
        save_filename=spacetime_name+'_classification_'+'angleview_'+str(angle_view_th)+'_'+str(angle_view_phi)+'.png' 
        plt.savefig(save_filename)
        return
    
    
    def extend_quadrant_to_quadrants(self):
        length_th=np.ones(len(self.th_range))
        quadI=np.array([self.r_range,self.th_range, self.Dindex,self.Sindex])
        quadII=np.array([self.r_range,self.th_range+length_th*np.pi/2, self.Dindex,self.Sindex])
        quadIII=np.array([self.r_range,self.th_range+length_th*np.pi, self.Dindex,self.Sindex])
        quadIV=np.array([self.r_range,self.th_range+length_th*3*np.pi/2, self.Dindex,self.Sindex])
        _newcoord=np.concatenate((quadI,quadII,quadIII,quadIV))
        return _newcoord
    
    def radial_to_cartesian(self,angle_axis):
        self.classification[angle_axis]['x_axis']=self.classification['r_axis']*np.sin(self.classification[angle_axis]['angle'])
        self.classification[angle_axis]['z_axis']=self.classification['r_axis']*np.cos(self.classification[angle_axis]['angle'])

    