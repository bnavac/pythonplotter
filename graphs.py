import matplotlib.pyplot as plt
import glob
import pandas as pd
from pathlib import Path
import pdb
def main():
    files = getFiles()
    dfs = readCSVs(files)
    plotData(dfs)
def getFiles():
    p = Path('')
    files = []
    for filename in list(p.glob("**/*.csv")):
        files.append(str(filename))
    return files
def readCSVs(files):
    #pdb.set_trace()
    manydf = []
    colnames = ["alpha","CL","CD","CDp","Cm","Top Xtr","Bot Xtr","Cpmin","Chinge","XCp"]
    for file in files:
        #Skip the first 10 rows as we handle those seperately.
        df = pd.read_csv(file, names = colnames, skiprows = 10)
        pdb.set_trace()
        #Remove rows that have an alpha < -10 or > 20
        df.drop(df.index[(df['alpha']< -10.) | (df['alpha'] > 20.)], inplace = True)
        manydf.append(df)
    
    return manydf
def plotData(dfs):
    pdb.set_trace()
    for df in dfs:
        plt.plot(df['alpha'],df['CL'])
        plt.show()
main()