import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here 
    
    num_draws = 3
    favourable_choice = ['RRR', 'GGG']
    
    favourable_count = 0
    
    for trial in range(numTrials):
        
        bag = ['R', 'R', 'R', 'R', 'G', 'G', 'G', 'G']
        
        balls_drawn = ''
        
        for draw in range(num_draws):
            selection = random.choice(bag)
            balls_drawn += selection
            bag.remove(selection)
        
        if balls_drawn in favourable_choice: favourable_count += 1
        
        #print balls_drawn, favourable_count
        
    if numTrials > 0: 
        return float(favourable_count)/numTrials
    else:
        return 0.0
        
print drawing_without_replacement_sim(10000)
            
            
            