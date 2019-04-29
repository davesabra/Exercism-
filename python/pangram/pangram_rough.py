# is_pangram() finds and confirms a pangram by a null measurement.

# searching the sentence sequentially looking for the absence of
#   ASCII letters a-z inclusive, Unicode subset 97-122.
# The first null search of the sentence sets 'pangram' to False.
# Otherwise the sentence is a True 'pangram'.

# test data
#sentence = 'the quick brown fo jumps over the lazy dog THE QUICK BROWN FOX\
#                     JUMPS OVER THE LAZY DOG'
#sentence = 'abcdefghjjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
sentence = 'five boxing wizards jump quickly at it'

# Case insensitivity is handled by lower().find() method which generates
# a default lower-case version of the input at runtime.


def is_pangram(sentence):
    
    
    print('Looking for a - z ...')
    
    for i in range(97, 123):
        letter = chr(i)
        loc = sentence.lower().find(letter)
        
        #if loc == None:       # doesnt work
        #if loc == -1:         # works but is not prefered and fails unit tests
        if loc is -1:          # fails the unit tests with AssertionError-None is not False
        #if loc == '':         # doesnt work -  zero values != no value
        #if loc is None:       # doesnt work. None is not 'not found'
            pangram = False
            print('Not Pangram-->', sentence)
            print('missing letter:', letter)
            break
        else:
            print('Found', '"', letter, '"', 'at position:', loc,'\n')           
    
    if pangram: print('Pangram--> ', sentence)


is_pangram(sentence)

# None is not False, None is not True

#Best practice
#Compare values to None using the pattern ---- if cond is None

#The code below uses the PEP 8 preferred pattern of --  if cond is None.

#number = None

#if number is None:
#    print("PEP 8 Style Guide prefers this pattern")

#Here the identity operator is is used. It will check whether number is identical to None. is will return to True only if the two variables point to the same object.

# this prints nothing
#x = None 
#if x: 
#    print('if x') 
#if x is not None: 
#    print('if x is not None')

# 
#x = [] 
#if x: 
#    print( 'if x') 
#if x is not None: 
#    print( 'if x is not None')
    
# prints ---  if x if x is not None 
#x = 42
#if x: 
#    print('if x', x) 
#if x is not None: 
#    print('if x is not None', x)



