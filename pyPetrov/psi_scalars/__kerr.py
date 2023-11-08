from numpy import cos, sin, sqrt

class Kerr:
    def __init__(self,M=1,a=1,th=0):
        self.M=M
        self.a=a
        self.th=th
    
    def psi0(self,r):
        return 0*r
    
    def psi1(self,r):
        return 0*r
    
    def psi2(self,r):
        numerator = 4*self.M*(3j*self.a**3*cos(3*self.th) + 3j*self.a*(3*self.a**2 - 20*r**2)*cos(self.th) + 24*self.a**2*r*cos(2*self.th) + 24*self.a**2*r - 40*r**3)
        denominator = 3*(self.a**2*cos(2*self.th) + self.a**2 + 2*r**2)**4
        return numerator / denominator
    
    def psi3(self,r):
        numerator = 1j*sqrt(2)*self.a*self.M*sin(self.th)*(self.a**2*cos(2*self.th) + self.a**2 - 6j*self.a*r*cos(self.th) - 5*r**2)
        denominator = (r - 1j*self.a*cos(self.th))**5 * (r + 1j*self.a*cos(self.th))**3
        return numerator / denominator
    
    def psi4(self,r):
        numerator = self.a**2 * self.M * sin(self.th)**2 * (11*r + 5j*self.a*cos(self.th))
        denominator = (r - 1j*self.a*cos(self.th))**6 * (r + 1j*self.a*cos(self.th))**2
        return numerator / denominator
    
    