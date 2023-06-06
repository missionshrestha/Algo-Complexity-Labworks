start_time = time()
    # start_time = time_ns()
    linear_search(data, data[-1])
    end_time = time()
    # end_time = time_ns()

    time_taken = end_time-start_time
    print(time_taken)