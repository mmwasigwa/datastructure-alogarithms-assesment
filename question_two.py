# Question 2: Write a function remove_duplicates(sequence) that takes a 
# sequence (list or tuple) and returns a new sequence with duplicates 
# removed while maintaining the original order of elements. 

def remove_duplicates ():
    sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
    return set(sequence)
print (remove_duplicates)