import numpy as np 
import matplotlib.pyplot as plt 
from scipy.spatial import SphericalVoronoi, geometric_slerp

# Understand what is a geometric_slerp
# https://en.wikipedia.org/wiki/Slerp

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.SphericalVoronoi.html


sample_array = [[20,20],[29,17],[18,29],[27,35],[33,43],[38,13],[48,16],[43,46],[48,54],[45,64],[52,71],[60,77],[70,78],[80,80]]
center = (80, 80)
radius= 80

# sample_array = np.array([[0,0,1],[0,0,-1],[1,0,0],
#                         [0,1,0],[0,-1,0],[-1,0,0]])

# center = np.array([0,0,0])
# radius = 1
sv = SphericalVoronoi(sample_array, radius,center)
print(sv.vertices)
print(sv.samples)
