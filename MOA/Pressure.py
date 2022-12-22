import numpy as np
import pandas as panda
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics


# Consider Gluc Values > 1 Is A Diabetes

db = panda.read_csv('cardio_train.csv')

UpPressure = db.loc[db.cardio == 1].ap_hi
DownPressure = db.loc[db.cardio == 1].ap_lo

UpPressureQ25,UpPressureQ75 = np.percentile(UpPressure,[25,75])

IQR = UpPressureQ75 - UpPressureQ25


plt.boxplot(UpPressure)
plt.title("Before Cleaning")
plt.show()

# Cleaning Data
UpPressure = UpPressure.loc[UpPressure >= (UpPressureQ25 - 1.5 * IQR)].loc[UpPressure <= (UpPressureQ75 + 1.5 * IQR)]


plt.boxplot(UpPressure)
plt.title("After Cleaning")
plt.show()

UpPressureMean = UpPressure.mean()
UpPressureMedian = UpPressure.median()
UpPressureMode = UpPressure.mode()
UpPressureSD = UpPressure.std()


print("Systolic blood pressure Mean = " + str(UpPressureMean))
print("Systolic blood pressure Median = " + str(UpPressureMedian))
# print("Systolic blood pressure Mode = " + str(UpPressureMode))
print("Systolic blood pressure Standard Deviation = " + str(UpPressureSD))

# Hypothesis: Abnormal Systolic blood Pressure is a sign of heart disease
# Check If Probabilty Of Having Both Normal blood pressure and heart disease is greater than having abnormal blood pressure


NormalPressure = UpPressure.loc[UpPressure >= 120].loc[UpPressure < 130]
UpLowPressure = UpPressure.loc[UpPressure < 120]
UpHighPressure = UpPressure.loc[UpPressure >= 130]


PNormalPressure = (NormalPressure.count()) * 100 / UpPressure.count()
PabNormalPressure = (UpLowPressure.count() + UpHighPressure.count()) * 100 / UpPressure.count()

print("Propability of Of Having Both Normal blood pressure and heart disease = " + str(PNormalPressure))
print("Propability of Of Having Both Abnormal blood pressure and heart disease = " + str(PabNormalPressure))

plt.pie([PNormalPressure,PabNormalPressure],labels= ["Normal Pressure", "Abnormal Pressure"])
plt.title("Probability of having")
plt.show()

#=====================================================================================================

# DownPressureQ25,DownPressureQ75 = np.percentile(DownPressure,[25,75])
# IQR = DownPressureQ75 - DownPressureQ25

# plt.boxplot(UpPressure)
# plt.title("Before Cleaning")
# plt.show()

# Cleaning Data
# DownPressure = DownPressure.loc[DownPressure >= (DownPressureQ25 - 1.5 * IQR)].loc[DownPressure <= (DownPressureQ75 + 1.5 * IQR)]

# DownPressureMean = DownPressure.mean()
# DownPressureMedian = DownPressure.median()
# DownPressureMode = DownPressure.mode()
# DownPressureSD = DownPressure.std()

# # plt.boxplot(UpPressure)
# # plt.title("After Cleaning")
# # plt.show()


# NormalPressure = UpPressure.loc[UpPressure]


