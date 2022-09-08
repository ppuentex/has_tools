# pressure formula 
## p ~ p0 * exp((-g*h*M)/(T0*R0))
'''
p0: reference pressure in pascals
M: moler mass of air kg/mol
g: gravity m/s2
R0: gas constant j/mol K
h: height in meters 
T0: temp in Kelvin 
'''


# %%
import math 
import numpy as np 

#%% 

# p0 = 101325
# M = 0.02896968
# g = 9.81
# R0 = 8.314462618
# T0 = 273

h_list = range(0, 1000, 100)
#%% 

def air_pressure_at_height(h):
    p0 = 101325
    M = 0.02896968
    g = 9.81
    R0 = 8.314462618
    T0 = 273   
    ratio = -(g * h * M) / (R0 * T0)
    p = p0 * math.exp(ratio)
    return p

for h in h_list: 
    p = air_pressure_at_height(h)
    print(h,'   ',p)