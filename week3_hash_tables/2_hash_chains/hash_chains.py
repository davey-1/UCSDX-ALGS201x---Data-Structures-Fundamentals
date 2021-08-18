# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one Dict
        self.elems = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query( input().split() )

    def process_query(self, query):
        
        if query.type == "check":
            hkey = query.ind

            if hkey in self.elems.keys():
                #print("hkey =",hkey,"self.elems[query.ind] =",self.elems[hkey])

                self.write_chain(cur for cur in reversed(self.elems[hkey]))

            else:
                print()
                
        else:

            qhash = self._hash_func( query.s )     
        
            #try:#   Change to Dict
                #ind = self.elems.index(query.s)
                
            #except ValueError:#   Chage to dict
                #ind = -1
                
            if query.type == 'find':                
                if qhash not in self.elems:
                    return print('no')
                else:
                    self.write_search_result(query.s in self.elems[qhash])   
    
            elif query.type == 'add':               
            
                if qhash not in self.elems.keys():
                    self.elems[qhash] = [query.s] 
                    #print(qhash , ":" , self.elems[qhash],"added")

                else:
                    if query.s not in self.elems[qhash]:
                        self.elems[qhash].append(str(query.s))
                        #print(qhash , ":" , self.elems[qhash],"added1")
                
                    
            else:#  #this covers the 'del' query
                if qhash in self.elems:
                    if query.s in self.elems[qhash]:
                        self.elems[qhash].remove(query.s)




    def process_queries(self): #process n queries
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':

    #for inputting manually
    
    # bucket_count = int(input())
    # proc = QueryProcessor(bucket_count)
    # proc.process_queries()
    
    #for auto-inputting case #6
    file = open("06.txt","r")
    lines = file.readlines()
    bucket_count = int(lines[0])
    proc = QueryProcessor(bucket_count)
    proc.process_queries(lines)
    file.close
    # n = int(lines[1])
    # for x in range(2, n):
    #     self.process_query(Query(lines[x].split()))