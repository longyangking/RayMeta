import numpy as np 

class Ray:
    def __init__(self, nfun, ts, init_postion, init_momentum=None, k0=1):    
        self.nfun = nfun
        self.lda = lda
        self.ts = ts  
        self.k0 = k0

        self.postion = init_postion
        self.positions = list()

        if init_momentum is None:
            n = nfun(self.postion)
            self.momentum = n*k0*np.array([1, 0, 0])    # defult as x-direction
        else:
            self.momentum = init_momentum

    def get_position(self, tindex):
        position = self.positions[tindex]
        return position

    def Hamiltonian(self, position, momentum):
        n = self.nfun(position)
        px, py, pz = momentum
        p0 = n*self.k0

        H = - np.sqrt(p0**2 - px**2 - py**2 - pz**2)
        return H

    def calculate(self, dt=None):
        # if dt is None:  # set default value
        #     interval_ts = self.ts[1:] - self.ts[:-1]
        #     min_interval_ts = np.min(interval_ts)
        #     dt = min_interval_ts/100

        momentum = self.momentum
        position = self.position
        self.positions.append(position)

        n_steps = 0
        for i in range(1, len(self.ts)):
            interval_t = self.ts[i] - self.ts[i-1]
            if dt is None:
                n_steps = 100
                dt = interval_t/n_steps
            else:
                n_steps = interval_t/dt

            
            



