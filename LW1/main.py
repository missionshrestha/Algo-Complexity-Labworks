from random import sample
from linear_search import linear_search
from binary_search import binary_search
from time import time_ns


def run(n):
    # data = sample(range(1, n+1), n)
    data = sorted(sample(range(1, n+1), n))

    
    # start_time = time_ns()
    # linear_search(data, data[-1])
    # end_time = time_ns()

    # time_taken = end_time-start_time
    # print(time_taken)


    start_time = time_ns()
    binary_search(data, data[-1])
    end_time = time_ns()

    time_taken = end_time-start_time
    print(time_taken)


for i in range(1000000,10000001,1000000):
    run(i)
