import numpy as np
import math
import matplotlib.pyplot as plt
import scipy
import openpyxl
import pandas as pd

#DATA ANALYSIS

data = pd.read_excel("DATA.xlsx")
list1 = data.values.tolist()
print(list1)
upd_list = list1[1:]
print(upd_list)


#Chose the type from the Excel sheet

a = 1
b = 2
c = 3
d = 4

#Retrieve the lay-up names

list_of_names = [item[0] for item in upd_list]


name_1 = list_of_names[a - 1]
name_2 = list_of_names[b - 1]
name_3 = list_of_names[c - 1]
name_4 = list_of_names[d - 1]

#Retrieve the E modulus list (Theoretical Prediction)

list_of_E = [item[1] for item in upd_list]

E_1 = list_of_E[a - 1]
E_2 = list_of_E[b - 1]
E_3 = list_of_E[c - 1]
E_4 = list_of_E[d - 1]

E_MVF = [E_1, E_2, E_3, E_4]

#Retrieve the E modulus list (FEM Prediction)

list_of_E_FEM = [item[2] for item in upd_list]

E_1_FEM = list_of_E_FEM[a - 1]
E_2_FEM = list_of_E_FEM[b - 1]
E_3_FEM = list_of_E_FEM[c - 1]
E_4_FEM = list_of_E_FEM[d - 1]

E_FEM = [E_1_FEM, E_2_FEM, E_3_FEM, E_4_FEM]

#Retrieve the E modulus list (Experimental Results)

list_of_E_EXP = [item[3] for item in upd_list]

E_1_EXP = list_of_E_EXP[a - 1]
E_2_EXP = list_of_E_EXP[b - 1]
E_3_EXP = list_of_E_EXP[c - 1]
E_4_EXP = list_of_E_EXP[d - 1]

E_EXP = [E_1_EXP, E_2_EXP, E_3_EXP, E_4_EXP]

#Retrieve the Stress_yield (Theoretical Prediction)

list_of_Y = [item[4] for item in upd_list]

Y_1 = list_of_Y[a - 1]
Y_2 = list_of_Y[b - 1]
Y_3 = list_of_Y[c - 1]
Y_4 = list_of_Y[d - 1]

Y_MVF = [Y_1, Y_2, Y_3, Y_4]

#Retrieve the Stress_yield (FEM Prediction)

list_of_Y_FEM = [item[5] for item in upd_list]

Y_1_FEM = list_of_Y_FEM[a - 1]
Y_2_FEM = list_of_Y_FEM[b - 1]
Y_3_FEM = list_of_Y_FEM[c - 1]
Y_4_FEM = list_of_Y_FEM[d - 1]

Y_FEM = [Y_1_FEM, Y_2_FEM, Y_3_FEM, Y_4_FEM]

#Retrieve the Stress_yield (Experimental Results)

list_of_Y_EXP = [item[6] for item in upd_list]

Y_1_EXP = list_of_Y_EXP[a - 1]
Y_2_EXP = list_of_Y_EXP[b - 1]
Y_3_EXP = list_of_Y_EXP[c - 1]
Y_4_EXP = list_of_Y_EXP[d - 1]

Y_EXP = [Y_1_EXP, Y_2_EXP, Y_3_EXP, Y_4_EXP]

#Retrive the Stress_ultimate (Theoretical Prediction)

list_of_U = [item[7] for item in upd_list]

U_1 = list_of_U[a - 1]
U_2 = list_of_U[b - 1]
U_3 = list_of_U[c - 1]
U_4 = list_of_U[d - 1]

U_MVF = [U_1, U_2, U_3, U_4]

#Retrieve the Stress_ultimate (FEM Prediction)

list_of_U_FEM = [item[8] for item in upd_list]

U_1_FEM = list_of_U_FEM[a - 1]
U_2_FEM = list_of_U_FEM[b - 1]
U_3_FEM = list_of_U_FEM[c - 1]
U_4_FEM = list_of_U_FEM[d - 1]

U_FEM = [U_1_FEM, U_2_FEM, U_3_FEM, U_4_FEM]

#Retrieve the Stress_ultimate (Experimental Results)

list_of_U_EXP = [item[9] for item in upd_list]

U_1_EXP = list_of_U_EXP[a - 1]
U_2_EXP = list_of_U_EXP[b - 2]
U_3_EXP = list_of_U_EXP[c - 1]
U_4_EXP = list_of_U_EXP[d - 1]

U_EXP = [U_1_EXP, U_2_EXP, U_3_EXP, U_4_EXP]


#Create the plot

fig, ax = plt.subplots()
index = np.arange (4)
bar_width = 0.2
opacity = 0.8

rects_1 = plt.bar(index, E_MVF, bar_width, alpha = opacity, color = "crimson", label = "MVF")

rects_2 = plt.bar(index + bar_width, E_FEM, bar_width, alpha = opacity, color = "royalblue", label = "FEM")

rects_3 = plt.bar(index +2*bar_width, E_EXP, bar_width, alpha = opacity, color = "orange", label="Experimental")

#E_Modulus Graph
plt.xlabel("FML Lay-up")
plt.ylabel("Young's Modulus [GPa]")
#plt.title("Something")


plt.xticks(index + bar_width, ('{}'.format(name_1), '{}'.format(name_2), '{}'.format(name_3), '{}'.format(name_4)))
plt.legend()

plt.tight_layout()
plt.show()

#Yield strength plot

fig, ax = plt.subplots()
index = np.arange (4)
bar_width = 0.2
opacity = 0.8

rects_1 = plt.bar(index, Y_MVF, bar_width, alpha = opacity, color = "crimson", label = "MVF")

rects_2 = plt.bar(index + bar_width, Y_FEM, bar_width, alpha = opacity, color = "royalblue", label = "FEM")

rects_3 = plt.bar(index +2*bar_width, Y_EXP, bar_width, alpha = opacity, color = "orange", label="Experimental")


plt.xlabel("FML Lay-up")
plt.ylabel("Yield Strength [GPa]")
#plt.title("Something")


plt.xticks(index + bar_width, ('{}'.format(name_1), '{}'.format(name_2), '{}'.format(name_3), '{}'.format(name_4)))
plt.legend()

plt.tight_layout()
plt.show()

#Ultimate strength plot

fig, ax = plt.subplots()
index = np.arange (4)
bar_width = 0.2
opacity = 0.8

rects_1 = plt.bar(index, U_MVF, bar_width, alpha = opacity, color = "crimson", label = "MVF")

rects_2 = plt.bar(index + bar_width, U_FEM, bar_width, alpha = opacity, color = "royalblue", label = "FEM")

rects_3 = plt.bar(index +2*bar_width, U_EXP, bar_width, alpha = opacity, color = "orange", label="Experimental")

#E_Modulus Graph
plt.xlabel("FML Lay-up")
plt.ylabel("Ultimate Stregth [GPa]")
#plt.title("Something")


plt.xticks(index + bar_width, ('{}'.format(name_1), '{}'.format(name_2), '{}'.format(name_3), '{}'.format(name_4)))
plt.legend()

plt.tight_layout()
plt.show()
