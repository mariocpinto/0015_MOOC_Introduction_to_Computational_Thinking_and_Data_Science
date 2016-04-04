import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    # TODO
    pylab.hist(values, numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title:
        pylab.title(title)
    pylab.show()

#makeHistogram([random.random() for i in range(10000)], 20, 'bins', 'frequency')
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    # TODO
    
    # Array to hold the longest run per trial
    longest_run = []
    
    for trial in range(numTrials):
        
        #Array to hold the output of each rol in a trial
        num = []
        
        for roll in range(numRolls):
            num += [die.roll()]
        
        #print num
        
        longest = 1
        start_index = 0
        
        while start_index < numRolls:
            
            count = 1
            
            for i in range(start_index + 1, numRolls):
                
                if num[i] == num[start_index]:
                    count += 1
                    start_index += 1
                    
                    if i == numRolls - 1:
                        if count > longest: longest = count
                
                else:
                    if count > longest: longest = count
                    break
            
            start_index += 1
        
        longest_run += [longest]
    
    makeHistogram(longest_run, 10, 'Length of Longest Run', 'Frequency', 'Frequency Distribution of Length of Longest Run')
    
    #return pylab.mean(longest_run)
    return sum(longest_run)/float(len(longest_run))
                
# One test case
#print getAverage(Die([1,2,3,4]),10,1)
#print getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000)
#print getAverage(Die([1]), 10, 1)
print getAverage(Die([1,2,3,4,5,6,6,6,7]), 1, 1000)