import pandas as pd
import matplotlib.pyplot as plt
exelfile = pd.read_excel("cancer patient data sets.xlsx")
#print(exelfile.iloc[:,24])#: all rows --> column number 1 and first elemnt[0]
count = 0
l = 0
minval = 1000
maxval = 0
#i in range(0,999)
for i in range(0,999):
    if exelfile.iloc[:,24][i] == 'High':
        count += exelfile.iloc[:,1][i]
        l += 1
    if exelfile.iloc[:,24][i] == 'High' and  exelfile.iloc[:,1][i] < minval:
        minval = exelfile.iloc[:,1][i]

    if exelfile.iloc[:,24][i] == 'High' and  exelfile.iloc[:,1][i] > maxval:
        maxval = exelfile.iloc[:,1][i]

c = int(count/l )
print(f"most people that has high lung cancer are range between"+
f"max age = {maxval}" +f" and min age = {minval}"+f" and mean = {c}")
plt.xlabel('Age')
# naming the y axis
plt.ylabel('Cancer level')
plt.plot(exelfile.iloc[:,1],exelfile.iloc[:,24],'o')
plt.title(f"most people that has high lung cancer are range between"+
f"max age = {maxval}" +f" and min age = {minval}"+f" and mean = {c}")
plt.show()
