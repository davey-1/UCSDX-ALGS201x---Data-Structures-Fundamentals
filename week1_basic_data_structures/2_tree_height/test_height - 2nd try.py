import sys, threading
from collections import defaultdict
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Tree:
        def get_values(self):
                print("Enter Value of n")
                self.n = int(input())
                print("Enter the values")
                self.parent = list(map(int, input().split()))

        def compute_height(self):
                height_arr, queue, h = defaultdict(list), list(), 0
                for i, v in enumerate(self.parent):
                    height_arr[v].append(i)

                queue += height_arr[-1]
                while(True):
                    number_of_nodes = len(queue)
                    if number_of_nodes == 0:
                        return h
                    h += 1
                    while number_of_nodes > 0:
                        node = queue.pop(0)
                        if node in height_arr:
                            queue += height_arr[node]
                        number_of_nodes -= 1




def main():
  tree = Tree()
  tree.get_values()
  print(tree.compute_height())

threading.Thread(target=main).start()

