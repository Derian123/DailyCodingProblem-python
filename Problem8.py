# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
from threading import Timer

# Our job here will be to print out hello world after x milliseconds


def job():
    print("Hello World")

# Here we have when the job will happen


def job_scheduler(job, milliseconds):

    # Timer is set to seconds, function but since we need milliseconds we divide by 1000 to get it

    t = Timer(milliseconds/1000, job)

    # We start the timer

    t.start()


def main():
    job_scheduler(job, 10)


main()
