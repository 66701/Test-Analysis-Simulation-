# Extract the data from Word given by supervisor
import matplotlib.pyplot as plt
import numpy as np

fname = r"\DataProjectFMLs.txt" # File with all th information, only copy paste the info in a .txt without the header.
PATH = r"C:\Users\loren\Desktop\PythonProjectAE2223-I"
Header = ['FML type', 'MVF', 'Thickness [mm]', r'MVF $E_{x}$[GPa]', r'MVF $\sigma_{y}$ [MPa]', r'MVF $\sigma_{ut}$ [MPa]', r'FEM $E_{x}$[GPa]', r'FEM $\sigma_{y}$ [MPa]', r'FEM $\sigma_{ut}$ [MPa]', r'EXP $E_{x}$[GPa]', r'EXP $\sigma_{y}$ [MPa]', r'EXP $\sigma_{ut}$ [MPa]']
f = open(PATH + fname, 'r'); lines = f.readlines(); f.close()
lines = list(map(lambda s: s.strip(), lines))
counter, i = 0, 0
for line in lines:
    if line == '':
        counter += 1

while i < counter:
    lines.pop(lines.index(''))
    i += 1

newlines, total, numLines = [], '', 0
for line in lines:
    #print(line)
    if "Glare" in line:
        newlines.append(total)
        total = line
        numLines += 1
        continue
    total += (' ' + line)
newlines.pop(newlines.index(''))
data = []
for line in newlines:
    line = line.split(' ')
    Material = line[0] + ' ' + line[1] + ' ' + line[2]
    finalLine = [Material] + line[3:]
    k = 1
    while k < len(finalLine):
        finalLine[k] = float(finalLine[k])
        k += 1
    data.append(finalLine)
data = np.array(data)
finalData = []
for point in data:
    print(point)
    INF_tup = (point[0], point[1], point[2])
    MVF_tup = (float(point[3])*10**9, float(point[4])*10**6, float(point[5])*10**6)
    FEM_tup = (float(point[6])*10**9, float(point[7])*10**6, float(point[8])*10**6)
    EXP_tup = (float(point[9])*10**9, float(point[10])*10**6, float(point[11])*10**6)
    orderedData = [INF_tup, MVF_tup, FEM_tup, EXP_tup]
    finalData.append(orderedData)

########################################################################################################################
## Constituents:
# stress-strain aluminium
strainAl = np.array([0, 0.00407, 0.00422, 0.00454, 0.00526, 0.00856, 0.0144, 0.0254, 0.0385, 0.0554, 0.0841, 0.1512])
stressAl = np.array([0, 300, 320, 340, 355, 375, 390, 410, 430, 450, 470, 484])
stressAl = np.array([x*10**6 for x in stressAl])

strainGlassEpoxy = np.array([0, 0.04])
stressGlassEpoxy = np.array([0, 790*10**6])
print(stressAl)
strain_u_Al = 0.1512
def stresStrain(E, sigma_y, x, sigma_u, strainAtFailure):
    '''
    :param E: Young's modulus from data
    :param sigma_y: Yield strength from data
    :param x: strain
    :param sigma_u: ultimate strength from data
    :param strainAtFailure: strain at failure
    :return: array representing the approximated stress strain curve
    '''
    result = []
    for item in x:
        if item > strainAtFailure:
            result.append(0); continue
        if float(item * E) < sigma_y:
            result.append(item * E); continue
        else:
            result.append(sigma_y + (item-(sigma_y/E))*(sigma_u-sigma_y)/(strainAtFailure-(sigma_y/E))); continue
    return result

def CompareFEM_MVF_EXP(data, maxStrain = strain_u_Al, dataNumber = 0):
    '''
    :param data: list of data from the extraction
    :param dataNumber: row (from 0) in the table of the data to analyse
    :param maxStrain: Maximum strain of the laminate
    :return: Graph comparing FEM, MVF and EXP methods under the linear spline analysis
    '''
    strain = np.linspace(0, maxStrain, 100)
    # INF_results = data[dataNumber][0]
    MVF_results = np.array(stresStrain(data[dataNumber][1][0], data[dataNumber][1][1], strain, data[dataNumber][1][2], maxStrain))
    FEM_results = np.array(stresStrain(data[dataNumber][2][0], data[dataNumber][2][1], strain, data[dataNumber][2][2], maxStrain))
    EXP_results = np.array(stresStrain(data[dataNumber][3][0], data[dataNumber][3][1], strain, data[dataNumber][3][2], maxStrain))
    plt.plot(strain*100, MVF_results*10**-6, label='MVF', c='b')
    plt.plot(strain*100, FEM_results*10**-6, label='FEM', c='darkorange')
    plt.plot(strain*100, EXP_results*10**-6, label='Test', c='g')
    plt.grid()
    plt.legend(loc='lower right')
    # plt.title(data[dataNumber][0][0])
    plt.text(0, 500, f'FML: {data[dataNumber][0][0]}\nMVF: {data[dataNumber][0][1]}', style='normal', fontsize=11,
            bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10})
    plt.xlabel('Strain [%]')
    plt.ylabel('Stress $\sigma$ [MPa]')
    plt.show()
    return True

def CompareFMLs(data, FMLs, maxStrain):
    '''

    :param data: A list with all the required data
    :param FMLs: A list with the number (starting from 0) of the FMLs in the table given by the supervisor
    :param maxStrain: A list of the maximum strain in the same order as the FMLs
    :return: graph comparing the FMLs
    '''
    i = 0
    for FML in FMLs:
        strain = np.linspace(0, maxStrain[i], 100)
        EXP_results = np.array(stresStrain(data[FML][3][0], data[FML][3][1], strain, data[FML][3][2], maxStrain[i]))
        plt.plot(strain*100, EXP_results*10**-6, label=data[FML][0][0])
        i += 1
    plt.legend(loc='lower right')
    plt.grid()
    plt.xlabel('Strain [%]')
    plt.ylabel('Stress $\sigma$ [MPa]')
    plt.show()
    return True

def CompareFML_Constituents(data, dataNumber):
    '''
    Note that all GLARE analysed are made of aluminium and glass epoxy, therefore, no special consideration for different values the constituents was taken.
    :param data:
    :param dataNumber:
    :return: Graph comparing the constituents to the FML
    '''
    plt.plot(strainAl*100, stressAl/10**6, label='Aluminium')
    strain = np.linspace(0, strain_u_Al, 100)
    EXP_results = np.array(stresStrain(data[dataNumber][3][0], data[dataNumber][3][1], strain, data[dataNumber][3][2], strain_u_Al))
    plt.plot(strain*100, EXP_results/10**6, label=f'{data[dataNumber][0][0]}')
    plt.plot(strainGlassEpoxy*100, stressGlassEpoxy/10**6, label='Glass Epoxy')
    plt.legend(loc='lower right')
    plt.grid()
    plt.xlabel('Strain [%]')
    plt.ylabel('Stress $\sigma$ [MPa]')
    plt.show()

CompareFML_Constituents(finalData, 10)