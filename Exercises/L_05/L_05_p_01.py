import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    draws = 3
    desired_sequence = ['RRR', 'BBB']
    success_count = 0
    
    for trial in range(numTrials):
        
        balls = ['R','R','R','B','B','B']
        sequence = ''
        
        for draw in range(draws):
            selected = random.choice(balls)
            sequence += selected
            balls.remove(selected)
            
        if sequence in desired_sequence:
            success_count += 1
            
        #print sequence, success_count
    
    return float(success_count)/numTrials

#print noReplacementSimulation(50)