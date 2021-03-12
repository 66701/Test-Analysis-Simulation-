import numpy as np
import math
import matplotlib.pyplot as plt
import scipy

#In the loading direction
FML_type = []
FML_number = 4
#Classical Laminate Theory

E_Modulus = [80, 90, 100, 110]
Yield_strength = [150, 150, 150, 150]
Ultimate_strength = [200, 210, 200, 210]
Strain_max = []

#FEM prediction

E_Modulus_2 = [100, 110, 130, 180]
Yield_strength_2 = []
Ultimate_strength_2 = []
Strain_max_2 = []

#Experimental results
E_Modulus_3 = [200, 210, 190, 170]
Yield_strength_3 = []
Ultimate_strength_3 = []
Strain_max_3 = []

#Create the plot

fig, ax = plt.subplots()
index = np.arange (FML_number)
bar_width = 0.2
opacity = 0.8

rects_1 = plt.bar(index, E_Modulus, bar_width, alpha = opacity, color = "crimson", label = "MVF")

rects_2 = plt.bar(index + bar_width, E_Modulus_2, bar_width, alpha = opacity, color = "teal", label = "FEM")

rects_3 = plt.bar(index +2*bar_width, E_Modulus_3, bar_width, alpha = opacity, color = "orange", label="Experimental")

#E_Modulus Graph
plt.xlabel("FML name")
plt.ylabel("Young's Modulus")
plt.title("Something")

#Names should be put in manually
plt.xticks(index + bar_width, ("Name 1", "Name 2", "Name 3", "Name 4"))
plt.legend()

plt.tight_layout()
plt.show()

#Repeat for other parameters

#data = np.genfromtxt("#File name", skip_header = #, skip_footer = #)
#list_1 = data[:, #]


