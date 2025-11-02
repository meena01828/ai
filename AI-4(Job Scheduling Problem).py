class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    n = max(job.deadline for job in jobs)
    result = [None] * n
    for job in jobs:
        for j in range(min(n, job.deadline)-1, -1, -1):
            if result[j] is None:
                result[j] = job.id
                break
    print("Scheduled Jobs:", [job for job in result if job])

jobs = [Job('A', 2, 100), Job('B', 1, 19), Job('C', 2, 27), Job('D', 1, 25), Job('E', 3, 15)]
job_scheduling(jobs)
