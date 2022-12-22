import numpy as np
import pandas as panda
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics



db = panda.read_csv('cardio_train.csv')

Age = db.loc[db.cardio == 1].age
Age /= 356
Age = np.floor(Age)



ageMean = Age.mean()
ageMedian = Age.median()
ageMode = Age.mode()
ageSD = Age.std()

ageQ25,ageQ75 = np.percentile(Age,[25,75])


plt.boxplot(Age)
plt.title("BoxPlot Of The Age")
plt.ylabel("Age")
plt.show()

# Data Is Clean Already

unique,count = np.unique(Age, return_counts=True)

r = statistics.correlation(unique,count)
print("Correlation Between Age And Heart Disease = " +  str(r))

x,y = np.polyfit(unique,count,1)
plt.scatter(unique,count)
plt.plot(unique,x*unique + y)

plt.title("Best Linear Fit Of The Data")
plt.ylabel("Frequency")
plt.xlabel("Age")
plt.show()


plt.hist(Age,10)
plt.title("Histogram Of The Age Column Of Patient")
plt.ylabel("Frequency")
plt.xlabel("Age")
plt.show()


AgeRightSide = Age.loc[Age >= ageMean]
AgeLeftSide = Age.loc[Age <= ageMean]


rightSideMean = AgeRightSide.mean()
leftSideMean = AgeLeftSide.mean()

print("Data Mean = " + str(ageMean))
print("Right Side Mean = " + str(rightSideMean))
print("Left Side Mean = " + str(leftSideMean))


rightSideCount = AgeRightSide.count()
leftSideCount = AgeLeftSide.count()

PhighAge = (rightSideCount) * 100 / (Age.count())
PLowAge = (leftSideCount) * 100 / (Age.count())

print("Propability Of High Age And Heart Disease = " + str(PhighAge))
print("Propability Of Low Age And Heart Disease = " + str(PLowAge))



