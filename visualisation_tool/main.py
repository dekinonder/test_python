### pltPnts.py version Ekin_2023_09_13####
### Calling initial libraries #####
from typing import List

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
font = {'family': 'monospace',
        'weight': 'bold',
        }
plt.rc('font', **font)


class data:
    baseLines: list[str]

    def __init__(self):
        ### Assigning the related paths ####
        self.path_baseFile = "C://Users//dekin//Desktop//Gabor_data_test_pojects//inhouse1//baseFile.txt"
        self.path_sampleFile = "C://Users//dekin//Desktop//Gabor_data_test_pojects//inhouse1//sampleFile.txt"
        self.baseFile = []
        self.sampleFile = []
        self.d = []
        self.baseX = []
        self.baseY = []
        self.baseZ = []
        self.baseLines = []
        # Activate following line when output file needed
        # self.path_outputFile = "C://Users//dekin//Desktop//Gabor_data_test_pojects//inhouse1//black3outputFile.txt"

    ### Reading the data ####
    @property
    def base_File(self):
        with open(self.path_baseFile) as f:
            self.baseLines = f.readlines()

        for i in range(0, len(self.baseLines)):
            self.d = [float(l) for l in self.baseLines[i].replace("\n", "0").replace(",", ".").split(" ")]
            self.d = self.d[0:-1]

            for j in range(0, len(self.d) // 3):
                self.baseX.append(self.d[3 * j])
                self.baseY.append(self.d[3 * j + 1])
                self.baseZ.append(self.d[3 * j + 2])

        return self.baseX, self.baseY, self.baseZ

    def sample_File(self):

        with open(self.path_sampleFile) as f:
            self.baseLines = f.readlines()

        for i in range(0, len(self.baseLines)):
            self.d = [float(l) for l in self.baseLines[i].replace("\n", "0").replace(",", ".").split(" ")]
            self.d = self.d[0:-1]

            for j in range(0, len(self.d) // 3):
                self.baseX.append(self.d[3 * j])
                self.baseY.append(self.d[3 * j + 1])
                self.baseZ.append(self.d[3 * j + 2])

        return self.baseX, self.baseY, self.baseZ


## plotting the data
class plot:
    def __init__(self, baseX, baseY, baseZ, sampX, sampY, sampZ):
        self.baseX = baseX
        self.baseY = baseY
        self.baseZ = baseZ
        self.sampX = sampX
        self.sampY = sampY
        self.sampZ = sampZ

    def set_plotXY(self):
        # fig, ax = plt.subplots()
        ax.plot(self.baseX, self.baseY, "*b")
        ax.plot(self.sampX, self.sampY, "*r")

    def set_plotXZ(self):
        # fig, ax = plt.subplots()
        ax.plot(self.baseX, self.baseZ, "og")
        ax.plot(self.sampX, self.sampZ, "ok")
        plt.show()
    def set_plotYZ(self):
        # fig, ax = plt.subplots()
        ax.plot(self.baseY, self.baseZ, ".c")
        ax.plot(self.sampY, self.sampZ, ".m")



if __name__ == "__main__":
    read_data = data()
    baseX, baseY, baseZ = read_data.base_File
    sampX, sampY, sampZ = read_data.sample_File()

    plot_data = plot(baseX, baseY, baseZ, sampX, sampY, sampZ)

    # plot_data.set_plotXY()
    plot_data.set_plotXZ()
    # plot_data.set_plotYZ()





