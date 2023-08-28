# Dictionaries: 

# Question 3: Implement a function word_frequency(sentence) that takes 
# a sentence and returns a dictionary containing the frequency of each 
# word in the sentence. 
# Ignore punctuation and consider words in a case-insensitive manner. 

def word_frequency(sequence):
    count = {}
    a = sequence.lower().split()
    
    for i in a:
      if i  in count:
       count[i] +=1
      else:
       count[i] = 1
    
    return count
print(word_frequency("This is a test sentence. This sentence is a test."))