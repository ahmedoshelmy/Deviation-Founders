import numpy as np
import pandas as panda
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics
import random

df = 1

def readAll():
    dt = panda.read_csv(
    'cardio_train.csv',
    header=0
    )
    dt = dt.loc[dt.cardio == 1]
    return dt
#===========================================================================================

def CleanData(df):
    q25,q75 = np.percentile(df.ap_hi,[25,75])
    IQR = q75 - q25
    df = df.loc[df.ap_hi >= (q25 - 1.5 * IQR)]
    df = df.loc[df.ap_hi <= (q75 + 1.5 * IQR)]
    return df


#===========================================================================================
def ChangeSample(p): 
    df = panda.read_csv(
         'CleanPressure.csv',
         header=0, 
         skiprows=lambda i: i>0 and random.random() > p
    )
    df = df.loc[df.cardio == 1]
    return df
#===========================================================================================
def GenerateSamples(p):
    SamplesArr = []

    df = ChangeSample(p)   #=== Sample Of Eleven Peobles ===#


    sampleSize = df.cardio.count()

    for i in range(0,1000):
        df = ChangeSample(p)
        SamplesArr.append(ChangeSample(p).ap_hi.mean())
    
    return SamplesArr,sampleSize
#===========================================================================================
# These Lines Just To Clean The Data 
# df = readAll()
# df = CleanData(df)
# df.to_csv('CleanPressure.csv',index=False)

#===========================================================================================

p = 0.0002999
FirstSampleArr, FirstSampleSize = GenerateSamples(p)
plt.hist(FirstSampleArr, color="red")

plt.title("Data Distribution for means from sample size = " + str(FirstSampleSize))
plt.xlabel("Mean")
plt.ylabel("Freq")
plt.show()

p = 0.0005998
SecondSampleArr, SecondSampleSize = GenerateSamples(p)
plt.hist(SecondSampleArr, color="green")
plt.title("Data Distribution for means from sample size = " + str(SecondSampleSize))
plt.xlabel("Mean")
plt.ylabel("Freq")
plt.show()

p = 0.0011996
ThirdSampleArr, ThirdSampleSize = GenerateSamples(p)
plt.hist(ThirdSampleArr, color="blue")
plt.title("Data Distribution for means from sample size = " + str(ThirdSampleSize))
plt.xlabel("Mean")
plt.ylabel("Freq")
plt.show()

# From Previous Results We Can Notice That the population is almost normal
plt.hist(FirstSampleArr, color="red")
plt.hist(SecondSampleArr, color="green")
plt.hist(ThirdSampleArr, color="blue")
plt.xlabel("Mean")
plt.ylabel("Freq")
plt.show()


sampleMin = np.min(ThirdSampleArr)
sampleMax = np.max(ThirdSampleArr)
sampleMean = np.mean(ThirdSampleArr)
sampleSD = np.std(ThirdSampleArr)
sampleSize = ThirdSampleSize
n = ThirdSampleSize

x_axis = np.arange(sampleMin, sampleMax, 1)

print("Sample Mean = Population Mean = " + str(sampleMean))
print("Sample Standard Deviation = " + str(sampleSD))


plt.plot(x_axis, norm.pdf(x_axis,sampleMean,sampleSD))
plt.xlabel("Mean")
plt.ylabel("Freq")
plt.show()


# Assuming 95% Level Of Confidence ===> Z = 1.96
z = 1.96

MaxError = z * sampleSD / np.sqrt(n)

transformed = (sampleMax - sampleMin) / 2
x_axis = np.arange(-1 * transformed, transformed, 1)



plt.plot(x_axis, norm.pdf(x_axis,0,sampleSD))
plt.plot([z,z],[0,0.09])
plt.plot([-1 * z,-1 * z],[0,0.09])
plt.show()


print("Maximum Error Estimated For Sample Of Size " + str(n) + " = " + str(MaxError))

LeftX = MaxError + sampleMean
RightX = sampleMean - MaxError

if LeftX > RightX:
    A = LeftX
    LeftX = RightX
    RightX = A

print("The Population Mean Is Between [" + str(LeftX) + "," + str(RightX) + "] With Confidence Of 95%") 



