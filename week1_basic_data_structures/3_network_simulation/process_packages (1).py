"""
Lets switch up the Buffer implementation a little bit; to optimize
"""

class Buffer:
	
	# Class Initialization 
	# self.size --> int 
	# self.finish_time --> list containing finish time for different packages at every index 
	def __init__(self, size): 
		self.size = size 
		self.finish_time = []


	@property 
	def check_if_buffer_full(self):
		#Buffer is full if length of finish time (all the packets) is equal to size of buffer
		if len(self.finish_time)==self.size: 
			return True 
		return False 

	@property
	def check_if_buffer_empty(self):
		#buffer is empty if there is no value in finish time 
		if len(self.finish_time) == 0:
			return True
		return False 

	@property
	def get_last_element(self):
		return(self.finish_time[-1])

	def flush_processed(self, request):
		## flush processes if the buffer has been reached
		while self.finish_time:
			if self.finish_time[0] <= request.arrival_time:
				self.finish_time.pop(0)
			else:
				break

	def process(self,request):
		# for every request: flush the request if the buffer has been reached
		self.flush_processed(request)
		# if the buffer is full: drop the package; 
		if self.check_if_buffer_full:
			return Response(True, -1)

		#if the buffer is empty; GREAT!!! just calculate the finish time for current request and
		# initialize the self.finish_time list with it 
		if self.check_if_buffer_empty:
			self.finish_time = [request.arrival_time + request.processing_time]
			# Response(is_dropped = False, arrival_time = request.arrival_time)
			return Response(False, request.arrival_time)

		#if the buffer is neither full nor empty; it just means there's some space left
		#process the package and append time taken into self.finish time
		response = Response(False, self.get_last_element)
		self.finish_time.append(self.get_last_element + request.processing_time)
		return Response

#Class definition for Request
#Contains two class variables: 
#self.arrival_time --> arrival time for packages
#self.processing_time --> processing time for packages
class Request: 
	def __init__(self, arrival_time, process_time): 
		self.arrival_time = arrival_time
		self.processing_time = process_time

#class definition for Response 
#Contains two class variables 
#self.dropped --> True if package was dropped: false otherwise 
#start_time --> start of the time for processing package

class Response: 
	def __init__(self, dropped , start_time): 
		self.dropped = dropped 
		self.start_time = start_time


#helper function to print output
def print_output(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

#helper function to read requests
def read_requests(n_requests):
    requests = []
    for i in range(n_requests):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

#helper function to process requests
def process_requests(requests, buffer):
    return [buffer.process(r) for r in requests]



if __name__ == "__main__":
    size, n_requests = map(int, input().strip().split())
    requests = read_requests(n_requests)
    buffer = Buffer(size)
    responses = process_requests(requests, buffer)
    print_output(responses)

