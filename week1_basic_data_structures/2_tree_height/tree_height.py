# python3

import sys
import threading
from time import time

def build_tree(n, parents):
    
    pc_rel = []
    for i in range(n):
        pc_rel.append([])
        
    for i in range(len(parents)):
        if parents[i] == -1:
            pass
        else:
            pc_rel[parents[i]].append(i)
    #print(pc_rel)
    return pc_rel
    
def compute_height(curr, pc_rel, height):

            
    if not pc_rel[curr]: 
        return height
    
    max_height = 0
    for i in pc_rel[curr]:
    
        max_height = max(max_height, compute_height(i, pc_rel, height+1))
            
    return max_height
    


def main():
    
    #print("n= int input")
    n = int(input())
    #print("value of n is", n)
    parents = list(map(int, input().split()))
    #print(parents)
    
    #start = time()

    pc_rel = build_tree(n, parents)
    
    for i in range(len(parents)):
        if parents[i] == -1:
            root = i

    print(compute_height(root, pc_rel, 1))
    
    #end = time()
    
    #print("elapsed time:", end - start)
    
if __name__ == "__main__":
    main()



# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
