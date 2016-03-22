def stdDevOfLengths(L):
    '''
    L: List of strings
    Returned Value: the standard deviation of the lengths of the strings
    Returns float('NaN') if L is empty
    '''
    
    num_of_strings = len(L)
    
    if num_of_strings == 0:
        return float('NaN')
    
    mean = 0
    var = 0
    
    for string in L:
        mean += len(string)

    mean = mean/float(num_of_strings)
     
    for string in L:
        var += (len(string) - mean)**2
    
    var = var/float(num_of_strings)  

    std_dev = (var)**0.5
    
    return std_dev