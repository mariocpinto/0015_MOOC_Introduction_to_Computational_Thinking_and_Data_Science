# L01 - Problem 3 & 4

FILE_PATH = 'C:/Users/Mario/Documents/GitHub/0015_MOOC_Introduction_to_Computational_Thinking_and_Data_Science/Exercises/L_01/julyTemps.txt'

import pylab as plt
import numpy as np

#Load file
inFile = open(FILE_PATH,'r')

# Initialize arrays for high and low temperatures
day = []
hi = []
lo = []

for line in inFile:
    line.rstrip()
    fields = line.split()
    
    if len(fields) != 3 or not fields[0].isdigit():
        continue
    
    else:
        day += [int(fields[0])]
        hi += [int(fields[1])]
        lo += [int(fields[2])]

#Calculate Diff in Temperatures
diffTemp = (np.array(hi) - np.array(lo)).tolist()

plt.figure(1)
plt.plot(day, diffTemp,'o')
plt.title( 'Day by Day Ranges in Temperature in Boston in July 2012')
plt.xlabel('Days')
plt.ylabel('Temperature Ranges')
plt.show()