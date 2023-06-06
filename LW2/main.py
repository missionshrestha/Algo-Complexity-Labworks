from random import sample
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from time import time_ns
from time import time


def run(n):
    data = sample(range(1, n+1), n)
    # print(data)
    # start_time = time()
    start_time = time_ns()
    insertion_sort(data)
    # sortedData = merge_sort(data, 0, n-1)
    # print(sortedData)
    # end_time = time()
    end_time = time_ns()

    time_taken = end_time-start_time
    print(time_taken)


for i in range(1000, 10001, 1000):
    run(i)
# for i in range(100000, 1000001, 100000):
#     run(i)
