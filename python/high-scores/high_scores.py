
class HighScores(object):
    
    def __init__(self, scores):
        self.scores=scores

    
    def latest(self):
            
        if len(self.scores)==0:
            raise ValueError('The list is empty')
        else:
            return self.scores[-1]   


    def personal_best(self):
        
        if len(self.scores)==0:
            raise ValueError('The list is empty')
        else:
            return  max(self.scores) 
    
    
    def personal_top_three(self):                                    
    
        if len(self.scores)==0:
            raise ValueError('The list is empty')
        else:
            return sorted(self.scores, reverse = True)[:3] 
        
 
# main()
#scores = [10, 30, 90, 30, 100, 20, 10, 0, 30, 40, 40, 70, 70]
#results = HighScores(scores)
#print( 'Latest Score: ' + str(results.latest()) )
#print( 'Personal Best: ' + str(results.personal_best()) )
#print('Personal Top:', *results.personal_top_three(), sep=' ')






    




