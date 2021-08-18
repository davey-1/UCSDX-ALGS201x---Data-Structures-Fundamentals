# python3



class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        
#3 2 1 0 5 4 2 5 1 0
#test case
        
        src_parent = self.get_parent(src)
        #print("src_parent = ", src_parent)
        dst_parent = self.get_parent(dst)
        
        # print("src =", src, "& dst =", dst)
        # print("---pre-merge---")
        # print("rc =",self.row_counts)
        # print("pa =",self.parents)

        if src_parent == dst_parent:
            # print("no merge needed")
            return False

        # merge two components
        # use union by rank heuristic
        else:
            
            #transfer all rows from table source to table destingation
            self.row_counts[dst_parent] += self.row_counts[src_parent]
            
            #clear source table
            self.row_counts[src_parent] = 0
            
            #set source parent to destination 
            self.parents[src] = dst
            
            # print("---post-merge---")
            # print("rc =",self.row_counts)
            # print("pa =",self.parents)

            # update max_row_count with the new maximum table size
            self.max_row_count = max(self.row_counts)

            
        return True

    def get_parent(self, table):
        # find parent and compress path
        
        
        # print("table (+1) = ", table + 1)
        # print("self.parents[table] (+1) =", self.parents[table] + 1)
        
        if table == self.parents[table]:            
            return table
        
        else:
            self.parents[table] = self.get_parent(self.parents[table])
            
        return self.parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(src - 1, dst - 1)  #python index starts at 0
        print(db.max_row_count)


if __name__ == "__main__":
    main()
