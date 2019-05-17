def distance(strand_a, strand_b):
    
    if len(strand_a) != len(strand_b):
        raise ValueError("strands not equal length!")
    
    ctr = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            ctr += 1
    return ctr

# equivalently, more readable?
#     
#def distance(strand_a, strand_b):
#   if not len(strand_a) == len(strand_b):
#      raise ValueError("The strands have different length")
#   count = 0
#    for a, b in zip(strand_a, strand_b):
#        if a != b:
#            count += 1
#    return count

