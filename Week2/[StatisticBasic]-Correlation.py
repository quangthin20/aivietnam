#Thống kê cơ bản - Correlation 

#! @author: QuangThin
import random
import numpy as np
# Data generation function
def dataGenerationFunction(size):
    data = np.random.randint(1, 100, size=(size, ))
    return data
def correlationFunction(x,y):
    eXY = np.mean(x*y)
    eX = np.mean(x)
    eY = np.mean(y)
    stdX = np.std(x);
    stdY = np.std(y);
    covariance = eXY - eX * eY
    return covariance / (stdX * stdY)
x = dataGenerationFunction(10)
print(x)
y = dataGenerationFunction(10)
print(y)
print("Correlation x và y:",correlationFunction(x,y))

    
    
    
    