# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []
        self.curr = 0        


    def process(self, request):
        #print (self.finish_time)
        
        self.curr = request.arrived_at
        
        
        #pop the processed requests
        if len(self.finish_time) > 0:
            
            self.curr = max(self.finish_time[-1], request.arrived_at)

            for i in self.finish_time:
                
                #drop the request if the buffer has been reached
                if request.arrived_at < i: #and len(self.finish_time) == self.size:
                    if len(self.finish_time) > self.size:
                        return Response(True,-1)
                    
                if request.arrived_at >= i:
                    self.finish_time.pop(0)
                    
        #if there is space in the queue, add the request to the queue
        if len(self.finish_time) < self.size:
                
                self.finish_time.append(self.curr + request.time_to_process)
                
                return Response(False,self.curr)
        
        #otherwise, drop the request.
        else: 
            return Response(True,-1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
