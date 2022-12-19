import numpy as np
import pandas as panda
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics


db = panda.read_csv('heart.csv')

bloodPressure =  db.trestbps


# Blood Pressure Description

BPMean = bloodPressure.mean()
BPMedian = bloodPressure.median()
BPMin = bloodPressure.min()
BPMax = bloodPressure.max()
BPSD = bloodPressure.std()

print("========================================== Blood Pressure ==========================================")
print("Min Value = " + str(BPMin))
print("Max Value = " + str(BPMax))
print("Mean = " + str(BPMean))
print("Median = " + str(BPMedian))
print("Standard Deviation = " + str(BPSD))


plt.boxplot(bloodPressure)
plt.show()

q75,q25 = np.percentile(bloodPressure,[75,25])
IQR = q75 - q25

db = db.loc[db.trestbps > (q25 - 1.5 * IQR)]
db = db.loc[db.trestbps < (q75 + 1.5 * IQR)]

bloodPressure =  db.trestbps
noDisease = db.loc[db.target == 0].trestbps
Disease = db.loc[db.target == 1].trestbps

plt.boxplot(bloodPressure)
plt.show()

print("Mean = " + str(Disease.mean()))



plt.hist(Disease)
plt.show()



# This Section Belongs To diabetes.csv File ====!!!!
# Getting Distribution Of Blood Pressure

# print("========================= Blood Pressure ===================================")

# bloodPressureMean = bloodPressure.mean()
# bloodPressureSD = bloodPressure.std()

# print("Standard Deviation : " + str(bloodPressureSD))
# print("Mean = " + str(bloodPressureMean))

# y = np.array(cleanBloodPressure)
# unique, counts = np.unique(y, return_counts=True)


# plt.hist(cleanBloodPressure, bins = int(180/20), density=False, alpha=0.6, color='b')
# plt.title("Pressure Distribution")
# plt.xlabel("Pressure Measurment")
# plt.ylabel("Frequency")
# plt.show()


# plt.hist(cleanBloodPressure, bins = int(180/20), density=True, alpha=0.6, color='b')
# plt.plot(unique,norm.pdf(unique,bloodPressureMean,bloodPressureSD),'k')
# plt.ylabel("Probability")
# plt.show()

# # Checking Distribution of diabetes knowing that pressure is high  ==> P > 80 is high

# highPressureSamples = db.loc[db.trestbps >= 90]

# lowPressureSamples = db.loc[db.trestbps <= 60]
# lowPressureSamples = lowPressureSamples.loc[lowPressureSamples.trestbps > 30]

# goodPressureSamples = db.loc[db.trestbps > 60]
# goodPressureSamples = goodPressureSamples.loc[goodPressureSamples.trestbps < 90]
# goodP = goodPressureSamples.loc[goodPressureSamples.Outcome == 1].trestbps

# highP = highPressureSamples.trestbps
# diabetes = highPressureSamples.loc[highPressureSamples.Outcome == 1]
# highP = diabetes.trestbps

# lowP = lowPressureSamples.trestbps
# diabetes = lowPressureSamples.loc[lowPressureSamples.Outcome == 1]
# lowP = diabetes.trestbps

# print(goodP.count())

# # High Pressure Samples Plot
# plt.hist(highP, 10)
# plt.title("High Pressure Samples")
# plt.xlabel("Pressure")
# plt.ylabel("Frequency")
# plt.show()

# # Low Pressure Samples Plot
# plt.hist(lowP, 4)
# plt.title("Low Pressure Samples")
# plt.xlabel("Pressure")
# plt.ylabel("Frequency")
# plt.show()

# # Good Pressure Samples Plot
# plt.hist(goodP,15)
# plt.title("Good Pressure Samples")
# plt.xlabel("Pressure")
# plt.ylabel("Frequency")
# plt.show()

# # relation between pressure, age and diabetes

# goodPressureSamples = db.loc[db.trestbps > 60]
# goodPressureSamples = goodPressureSamples.loc[goodPressureSamples.trestbps < 90]
# goodP = goodPressureSamples.loc[goodPressureSamples.Outcome == 1].trestbps


