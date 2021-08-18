# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

#consider class for the the worker, containing id and next free time.

class Worker:
    def __init__(self):        
        next_free_time = 0
        self.nft = next_free_time
        

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []                
    
    next_free_time = [0] * n_workers #two lists with n 
    
    for job in jobs:
        #takes too much time creating another loop.. solve it using a priority queue
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w]) 
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result
    
def fast_assign(n_workers, jobs):
    
    result = [] #list of len(jobs) results, with each entry as a tuple of: worker, time started
    pq = []

    for i in range(n_workers):
        
        pq.append([0,i]) #initialize each worker with nft = 0, worker_id#
        
    for i in range(len(jobs)):
        
        #assign the next free thread to job i
        free_thread = pq.pop(0)
        result.append(free_thread)
        
        #update the current thread's next free time
        pq.append( [free_thread[0] + jobs[i], free_thread[1]] )
        #pq.sort()
        
    return result

    

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = fast_assign(n_workers, jobs)

    for job in assigned_jobs:
        print(job[1],job[0])


if __name__ == "__main__":
    main()
