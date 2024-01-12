import matplotlib.pyplot as plt
from matplotlib import style
import glob
import pandas as pd
from pathlib import Path
import pdb
def main():
    files = getFiles()
    labels = []
    dfs = readCSVs(files, labels)
    plotData(dfs, labels)
def getFiles():
    p = Path('')
    files = []
    for filename in list(p.glob("**/*.csv")):
        files.append(str(filename))
    return files
def readCSVs(files, labels):
    manydf = []
    colnames = ["alpha","CL","CD","CDp","Cm","Top Xtr","Bot Xtr","Cpmin","Chinge","XCp"]
    for file in files:
        #Skip the first 10 rows as we handle those seperately.
        df = pd.read_csv(file, names = colnames, skiprows = 10)
        label = pd.read_csv(file, nrows = 9, on_bad_lines = 'skip')
        #Remove rows that have an alpha < -10 or > 20
        df.drop(df.index[(df['alpha']< -10.) | (df['alpha'] > 20.)], inplace = True)
        manydf.append(df)
        labels.append(label)
    return manydf
def plotData(dfs, labels):
    print("Creating graphs")
    plotGraph(dfs, labels, 'alpha', 'CL', "Alpha (degrees)", "CL", "CLAlpha")
    plotGraph(dfs, labels, 'CD', 'CL', "CD", "CL", "CLCD")
    plotGraph(dfs, labels, 'alpha', 'Cm', "Alpha (degrees)", "CM", "CMAlpha")
    
    #Idk what to do about this bottom graph since there's no clear y axis, so I made it manually
    
    title = "CL/CD vs alpha at Re = 350000"
    plt.title(title)
    key = "Calculated polar for: "
    i = 0
    for df in dfs:
        tmp = labels[i].loc[0].astype("string")
        tmp = tmp.iloc[0]
        plt.plot(df['alpha'],(df['CL']/df['CD']), label = tmp[len(key)+1:])
        i += 1
    print("Creating CL/CD graph")
    plt.gca().grid()
    plt.legend(fontsize="10")
    plt.xlabel("Alpha (degrees)")
    plt.ylabel("CL/CD")
    plt.savefig("CLCDalpha.png", dpi = 300, edgecolor = "none")
    plt.cla()
    plt.clf()
    plt.close()
#Given a list of dfs, the x and y axis, plots a given number of graphs
def plotGraph(dfs, labels, x, y, xlab, ylab, name, latex:bool):
    #Depending on how things go, may change how we write the title
    
    title = y + " vs " + x + " at RE = 350000" #TODO:Change y and x to subscript instead (so C_D instead of CD)
    plt.title(title)
    key = "Calculated polar for: "
    i = 0
    for df in dfs:
        tmp = labels[i].loc[0].astype("string")
        tmp = tmp.iloc[0]
        plt.plot(df[x], df[y], label = tmp[len(key)+1:])
        i += 1
    plt.gca().grid()
    plt.legend(fontsize="10")
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.savefig(name + ".png", dpi = 300, edgecolor = "none")
    plt.cla()
    plt.clf()
    plt.close()
main()