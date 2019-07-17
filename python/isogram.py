def is_isogram(string):
    # strip spaces, hyphens and convert to lower case
    stripped_string = string.strip().replace(' ','').replace('-','').lower()

    # convert the stripped down string (word or phrase) to an unordered collection
    # of its own letters by set comprehension
    string_set = {x for x in stripped_string}

    # The Python set (of an isogrammatic string) is a collection of unique letters.
    # For an isogram, it is True that the length of the stripped down string
    # equals the length of its set.
    return  len(stripped_string) == len(string_set)



string = 'isogram'
print(is_isogram(string))
