
def is_pangram(sentence):
    
    print('Looking for a - z ...')
    
    for i in range(97, 123):
        letter = chr(i)
        loc = sentence.lower().find(letter)
        if loc is -1:                       # if the letter is not found at the location
            
            pangram = False
            print('Not Pangram-->', sentence)
            print('missing letter:', letter)
            break
        else:
            print('Found', '"', letter, '"', 'at position:', loc,'\n')           
    
    if pangram: print('Pangram--> ', sentence)

# test data
#sentence = 'the quick brown fo jumps over the lazy dog THE QUICK BROWN FOX\
#                     JUMPS OVER THE LAZY DOG'
#sentence = 'abcdefghjjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
sentence = 'five boxing wizards jump quickly at it'
is_pangram(sentence)






