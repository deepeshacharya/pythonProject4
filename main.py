import openpyxl
data= openpyxl.load_workbook("D:\csv\stock.xlsx")
#from typing import List
from pickletools import optimize


#import pandas as pd

a  = [1] * 4
b = [1] * 4
n = 0
cn = 0
j = 0.001

while n <4000:
    while cn  < 10000:
        b[0] = a[0] * float (data [n][0])
        b[1] = a[1] * float (data[n][1])
        b[2] = a[2] * float (data[n][2])
        b[3] = a[3] * float (data[n][3])
        result = b[0] + b[1] + b[2] + b[3]

        if float (data [n+1] [0]) < result:
            maxl = max (b[0], b[1], b[2], b[3])
            if maxl == b[0]:
                optimize = 0
            if maxl == b[1]:
                optimize = 1
            if maxl == b[2]:
                optimize = 2
            if maxl == b[3]:
                optimize = 3

            a[optimize] = a[optimize]- j

        if float (data [n+1] [0]) > result:
            maxl = max (b[0], b[1], b[2], b[3])
            if maxl == b[0]:
                optimize = 0
            if maxl == b[1]:
                optimize = 1
            if maxl == b[2]:
                optimize = 2
            if maxl == b[3]:
                optimize = 3

            a[optimize] = a[optimize]+ j

        cn = cn + 1

    n = n+1
    print(str(result)+"---"+ str(result/ float(data[n+1][0])))
