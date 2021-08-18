# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]




def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    for cur_query in queries:
        
        #add
        if cur_query.type == 'add':
            contacts[cur_query.number] = cur_query.name 
                
        #del
        elif cur_query.type == 'del':
            if cur_query.number in contacts:
                del contacts[cur_query.number]
            
        #find
        elif cur_query.type == 'find':
            if cur_query.number in contacts:
                response = contacts[cur_query.number]
            else:
                response = 'not found'
            result.append(response)
        
        else:
            response = 'not found'
            if contacts[cur_query.number]:
                response = contacts[cur_query.number]
            
            result.append(response)

        print (contacts)
        
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

