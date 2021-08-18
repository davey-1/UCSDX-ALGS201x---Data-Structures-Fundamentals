# python3
import random
import math

def read_input():
    return (input().rstrip(), input().rstrip())

# Try to update this using list comprehension
# the 5 lines in this function can be converted to one 
# 5 ^2 = 7 in python 
# math.pow(5,2) = 25
# 5 **2 = 25 as well

def polyHash(pattern, p,x):
    return sum([ord(pattern[i]) * math.pow(x,i) for i in range(len(pattern))]) % p

# def polyHash(pattern, p, x):
#     hash = 0
#     for i in range (0, len(pattern)):
#         #used math.pow instead of ^ operator
#         # or just using x ** i will work 
#         # not x^i
#         hash = hash + (ord(pattern[i]) * math.pow(x,i))
            
#     hash = hash % p
#     return hash

def precomputeHashes(text,lenPat,p,x):
        
        # I went from front to back and not from back to front 
        # technically these both are the same 
        # I just learnt it this way :xd 
    
        H = [0]*(len(text) - lenPat + 1 )
        S = text[0: lenPat]

        H[0] = polyHash(S,p,x)
        for i in range(1, len(text) - lenPat+1):
            H[i] = ((H[i-1] - (ord(text[i-1])*math.pow(x,lenPat-1)))*x + ord(text[i+2]))
            print(H[i])
            
        return H

def print_occurrences(output):
    
    string = ""
    for i in output:
        string += str(i) + " "
    print(string)

def get_occurrences(pattern, text):
    p = 1000007 #large prime number
    x = 15 #random.randint(1, p-1)
    
    positions = []
    
    #hash the pattern
    pHash = polyHash(pattern, p, x)
    print("pHash =", pHash)
    
    #implement recurrence equation
    H = precomputeHashes(text,len(pattern),p,x)
    print("H =",H)
    
    for i in range(len(text) - len(pattern) + 1): #+1 is necessary
        #print ("i =",i)
    
        
        #check if pattern hash matches text hash
        if pHash == H[i]:
            if text[i:i+len(pattern)] == pattern:
                positions.append(i)
                #print(i,"added")
                
    return positions

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

