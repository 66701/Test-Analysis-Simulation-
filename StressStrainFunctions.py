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

strain_u_Al = 16/100
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

def CompareFEM_MVF_EXP(finalData, maxStrain = strain_u_Al, dataNumber = 0):
    '''
    :param finalData: list of data from the extraction
    :param dataNumber: row (from 0) in the table of the data to analyse
    :param maxStrain: Maximum strain of the laminate
    :return: Graph comparing FEM, MVF and EXP methods under the linear spline analysis
    '''
    strain = np.linspace(0, maxStrain, 100)
    INF_results = finalData[dataNumber][0]
    MVF_results = np.array(stresStrain(finalData[dataNumber][1][0], finalData[dataNumber][1][1], strain, finalData[dataNumber][1][2], maxStrain))
    FEM_results = np.array(stresStrain(finalData[dataNumber][2][0], finalData[dataNumber][2][1], strain, finalData[dataNumber][2][2], maxStrain))
    EXP_results = np.array(stresStrain(finalData[dataNumber][3][0], finalData[dataNumber][3][1], strain, finalData[dataNumber][3][2], maxStrain))
    print(strain)
    print(MVF_results)
    plt.plot(strain*100, MVF_results*10**-6, label='MVF', c='b')
    plt.plot(strain*100, FEM_results*10**-6, label='FEM', c='darkorange')
    plt.plot(strain*100, EXP_results*10**-6, label='Test', c='g')
    plt.grid()
    plt.legend(loc='lower right')
    # plt.title('My title')
    plt.xlabel('Strain [%]')
    plt.ylabel('Stress $\sigma$ [MPa]')
    plt.show()
    # Note: tuple 1 is for basic infos, tuple 2 for MVF data, tuple 3 for FEM data, tuple 4 for EXP data

CompareFEM_MVF_EXP(finalData, strain_u_Al, 0)