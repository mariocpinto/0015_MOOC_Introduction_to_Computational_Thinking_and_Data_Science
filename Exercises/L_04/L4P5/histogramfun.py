import pylab

# You may have to change this path
WORDLIST_FILENAME = "C:/Users/Mario/Documents/GitHub/0015_MOOC_Introduction_to_Computational_Thinking_and_Data_Science/Exercises/L_04/L4P5/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=20):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
 
    vowel_fraction = [ sum(letter in 'aeiou' for letter in word)/float(len(word)) for word in wordList]
#    print vowel_fraction
    pylab.hist(vowel_fraction, numBins)
    pylab.title('Distribution of proportion of vowels in a word')
    pylab.xlabel('Proportion of vowels in a word')
    pylab.ylabel('Number of words')
    pylab.show()
    
 
if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)

#plotVowelProportionHistogram(['ab'], numBins=15)
