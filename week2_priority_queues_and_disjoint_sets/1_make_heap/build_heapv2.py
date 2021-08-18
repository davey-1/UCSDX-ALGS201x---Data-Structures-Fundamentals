# python3
import sys
import time
import math

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    
    This is a binary min heap
    """

    heap = MinHeap(len(data))
    
    heap.Heap = data
    # if len(data) > 100:
    #     heap.Heap.insert(0,0)
    # heap.Heap.insert(0,0)
    heap.size = len(data)
    
    #print("heap1 =",heap.Heap)
    heap.minHeap()
    #print("heap2 =",heap.Heap)
    
    return heap.swap_list
    

class MinHeap:
 
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize +1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1
        self.numswaps = 0
        self.swap_list = [] #updated
 
    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return int(math.floor((pos-1)/2))
 
    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        leftchildindex =  2 * pos +1
        # handle if leftchildindex goes out of index
        if leftchildindex >= self.size:
            return -1
        return leftchildindex
 
    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChild(self, pos):
        rightchildindex = 2 * pos + 2

        # handle if rightchildindex goes out of index
        if rightchildindex >= self.size:
            return -1
        return rightchildindex

    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        if pos >= int(math.floor(self.size/2)) and pos <= self.size:
            return True
        return False
 
    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.swap_list.append([fpos, spos])        #update
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]
        self.numswaps += 1 #updated
        #print("numswaps =",self.numswaps) #updated

 
    # Function to heapify the node at pos
    def minHeapify(self, pos):
        # If the node is a non-leaf node and greater
        # than any of its child
        #print("minHeapify called on pos", pos)
        if not self.isLeaf(pos):
            #added handle if leftchildindex or rightchildindex becomes -1
            if self.leftChild(pos) != -1 and  self.rightChild(pos) != -1 and ((self.Heap[pos] > self.Heap[self.leftChild(pos)] or
               self.Heap[pos] > self.Heap[self.rightChild(pos)])):
                
                # Swap with the left child and heapify
                # the left child
                #print(self.leftChild(pos), self.rightChild(pos), pos, len(self.Heap))

                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
 
                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))
 
    # Function to insert a node into the heap
    def insert(self, element):
        if self.size >= self.maxsize :
            return
        self.size+= 1
        self.Heap[self.size] = element
        current = self.size
 
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
 
    # Function to print the contents of the heap
    def Print(self):
        for i in range(0, int(math.floor(self.size/2))):
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1]))
 
    # Function to build the min heap using
    # the minHeapify function
    def minHeap(self):
        #print("minHeap called")
        for pos in range(int(math.floor(self.size/2)), -1, -1):
            #print("Pos is :",pos)
            self.minHeapify(pos)
 
    # Function to remove and return the minimum
    # element from the heap
    def remove(self):
 
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size-= 1
        self.minHeapify(self.FRONT)
        return popped    

def main():
    n = int(input())
    # file = open("test.txt","r")
    # lines = file.readlines()
    # n = int(lines[0])
    # data = list(map(int, lines[1].split()))
    data = list(map(int, input().split()))
    assert len(data) == n

    #start = time.time()

    swaps = build_heap(data)
    
    #end = time.time()

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

    #print("elapsed time:", end - start)

if __name__ == "__main__":
    main()
