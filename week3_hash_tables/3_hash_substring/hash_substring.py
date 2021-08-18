# python3
import random
import math

def read_input():
    return (input().rstrip(), input().rstrip())

def polyHash(pattern, p, x):
    return sum([ord(pattern[i]) * (x**i) for i in range(len(pattern))]) % p


def precomputeHashes(text,lenPat,p,x):
    
    #gets the index of the last substring to analyze
    lastIndex = len(text) - lenPat
    
    H = [0]*(lastIndex+1)    
    S = text[lastIndex:]

    H[lastIndex] = polyHash(S,p,x)
    #print(lastIndex,":",H[lastIndex],"(polyHash)")
    
    xexp = x**(lenPat-1)

    for i in range( lastIndex-1, -1, -1):
        H[i] = ( ord(text[i]) +  (H[i+1] - ord(text[i+lenPat])*(xexp) )*x ) %p 
        # print("--------")
        # print("text[i] =",i,text[i])
        # print("ord(text[i+lenPat-1])",ord(text[i+lenPat-1]),",",text[i+lenPat-1])
        # print("x**(lenPat-1)",x**(lenPat-1))
        #print(i,":",H[i])
        #print("--------")
        
    return H

def print_occurrences(output):
    
    string = ""
    for i in output:
        string += str(i) + " "
    print(string)

def get_occurrences(pattern, text):
    p = 1000000007 #large prime number
    x = random.randint(1, p-1)
    #print("x :",x)
    
    positions = []
    
    #hash the pattern
    pHash = polyHash(pattern, p, x)
    #print("pHash =", pHash)
    
    #implement recurrence equation
    H = precomputeHashes(text,len(pattern),p,x)
    
    for i in range(len(text) - len(pattern) + 1):
        #print ("i =",i)
         
        #check if pattern hash matches text hash

        if pHash == H[i]:
            if text[i:i+len(pattern)] == pattern:
                positions.append(i)
    
    # print("pHash =", pHash)
                
    return positions

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

