import heapq 
import time

class Worker:
    """
    Implementing class worker; 
    The workers with lower release time have higher priority. 
    If the release time are same for two workers, their priority is based 
    on their thread id
    """
    def __init__(self, thread_id, release_time=0):
        ## thread_id --> int        id of current thread
        ## release_time -->         release time for current thread
        self.thread_id = thread_id
        self.release_time = release_time

    def __lt__(self,other):
        """
        Here we are overloading the '<' operator to make comparison between two worker objects.
        If the release time for calling object is less than the other, this returns True else false

        If the release time are same, the same operation is done on thread id
        """

        if self.release_time == other.release_time:
            return self.thread_id < other.thread_id
        return self.release_time < other.release_time

    def __gt__(self, other): 
        """Here we are overloading the '>' operator to make comparison between two worker objects. 
        If the release time for calling object is greater than the other, this returns True else False 

        If the release time are same, the same operation is don on thread id
        """
        if self.release_time == other.release_time: 
            return self.thread_id > other.thread_id
        return self.release_time > other.release_time

class JQ:
    """
    Implementing the job queue class:
    This class implements all the functions necessary to implement the 
    processing jobs in parallel task. 
    """
    
    def read_data(self): 
        #take input data
        self.n_workers, self.n_jobs = map(int, input().split())
        self.jobs_list = list(map(int, input().split()))
        self.size = len(self.jobs_list)
        assert self.n_jobs == self.size

    def display_output(self):
        #take values from self.result and display them as output
        for id, time in self.out: 
            print(id,time)

    def fast_assign_jobs(self):
        """
        This function implements the assign job task 
        Here we will put n workers in a heap queue (which is basically implemented as a list)
        See https://realpython.com/python-heapq-module/ for more details on this 
        
        Then we iterate over the jobs in hand; assign different workers according to their priority
        then store their (id, release_time) as tuple in the output list. 

        This will be later used to display the output of the program 
        """
        #Initializing the worker list
        self.workers = []

        #Creating a n_workers instances of Worker class
        for i in range(self.n_workers):
            self.workers.append(Worker(i))
        #Initializing the output list
        self.out = []

        #Looping through the jobs in hand
        for job in self.jobs_list:
            #getting the current worker from the heap queue (one with max priority)
            current_worker = heapq.heappop(self.workers)
            #append the current worker's id and release time in the output list 
            self.out.append((current_worker.thread_id, current_worker.release_time))
            #update the release_time of the current worker
            current_worker.release_time += job
            #put the current worker back in the workers list with updated release time
            heapq.heappush(self.workers,current_worker)

    def run(self):
        """Run function for implementing the jobs queue problem"""
        
        self.read_data()
        self.fast_assign_jobs()
        self.display_output()



if __name__ == "__main__":
    start = time.time()
    job_q = JQ()
    job_q.run()
    end = time.time()
    
    print(end - start)