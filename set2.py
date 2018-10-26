# Gilat Mandelbaum Set2

from nltk.tokenize import word_tokenize
import numpy as np
import nltk
#nltk.download()

def data_stream():
    """Stream the data in 'leipzig100k.txt' """
    with open('leipzig100k.txt', 'r') as f:
        for line in f:
            for w in word_tokenize(line):
                if w.isalnum():
                    yield w
   
def bloom_filter_set():
    """Stream the data in 'Proper.txt' """
    with open('Proper.txt', 'r') as f:
        for line in f:
            yield line.strip()



############### DO NOT MODIFY ABOVE THIS LINE #################


# Implement a universal hash family of functions below: each function from the
# family should be able to hash a word from the data stream to a number in the
# appropriate range needed.

def findPrime(n):
    """Returns a prime number larger than n
    """
    def isPrime(k):
        import math
        for divisor in range(2, round(math.sqrt(n)-0.5)):
            if k%divisor==0:
                return False
        return True
    if n%2==0:
        candidate = n+1
    else:
        candidate = n
    while not isPrime(candidate):
        candidate += 2
    return candidate  

class Hash(object):
    def __init__(self, size):
        self.size = size
        self.bits = [0]*size
        
    def add(self, num):
        num = num % self.size
        self.bits[num] = 1
        
    def get(self, num):
        num = num % self.size
        return self.bits[num]

def uhf(rng):
    """Returns a hash function that can map a word to a number in the range
    0 - rng
    """
    p = findPrime(rng)
    m = 2*rng
    a = np.random.randint(1,p)
    b = np.random.randint(0,p)
    return lambda x: ((a*x+b)%p)%m


############### 

################### Part 1 ######################

from bitarray import bitarray
size = 2**18   # size of the filter

hash_fns = [None, None, None, None, None]  # place holder for hash functions
bloom_filter = bitarray(size)
num_words = 0         # number in data stream
num_words_in_set = 0  # number in Bloom filter's set

# Create 5 hash functions
for i in range(len(hash_fns)):
    hash_fns[i] = uhf((size-1)/5)

#for word in bloom_filter_set(): # add the word to the filter by hashing etc.
#    pass
# Create dictionary that holds all words in data set as keys, and values as list of positions declared by the hash functions
dictionary = dict()

# Loop through bloom_filter_set
for word in bloom_filter_set():
    num_words_in_set += 1 # count number of words
    dictionary[word] = []
    for h in hash_fns:
        x = int(h(num_words_in_set) % size) # utilize hash functions
        dictionary[word].append(x) # save position in dictionary list
        bloom_filter[x] = True #add to bloom filter array

# Create another dictionary to collect words that are not in the bloom_filter_set dictionary, along with list of their positions declared by the hash functions
dict_stream = dict()

# Loop through data stream 
for word in data_stream(): 
    num_words += 1 # count number of words
    if word not in dictionary.keys(): # If word not in dictionary, add to data stream's dictionary
        dict_stream[word]=[]
        for h in hash_fns:
            y = int(h(num_words) % size)
            dict_stream[word].append(y)
    else:
        pass

# Count number of faLse positives
fp = 0 # False positives counter
for key in dict_stream.keys():
    count_p = 0 # Counts number of bloom filter positions where the position is True
    for i in dict_stream[key]:
        if bloom_filter[i] == True:
            count_p += 1
        else:
            pass
        if count_p == 5: # If all 5 positions were taken place, then counts as false positive
            fp += 1
        else:
            pass
            
print('False Positives count:',fp)
print('Total number of words in stream = %s'%(num_words,))
print('Total number of words in stream = %s'%(num_words_in_set,))
      
################### Part 2 ######################

hash_range = 24 # number of bits in the range of the hash functions
fm_hash_functions = [None]*35  # Create the appropriate hashes here

def num_trailing_bits(n):
    """Returns the number of trailing zeros in bin(n)

    n: integer
    """
    pass

num_distinct = 0

#for word in data_stream(): # Implement the Flajolet-Martin algorithm
#    pass

print("Estimate of number of distinct elements = %s"%(num_distinct,))

################### Part 3 ######################

var_reservoir = [0]*512
second_moment = 0
third_moment = 0

# You can use numpy.random's API for maintaining the reservoir of variables

#for word in data_stream(): # Imoplement the AMS algorithm here
#    pass 
      
print("Estimate of second moment = %s"%(second_moment,))
print("Estimate of third moment = %s"%(third_moment,))
