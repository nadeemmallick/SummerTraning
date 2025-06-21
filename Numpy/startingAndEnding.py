import numpy as np
import time

start_time = time.time()

arr = np.arange(1,1000000)

arr_squared = arr ** 2

end_time = time.time()

print("start time:",start_time)
print("end time:",end_time)
print("total time taken:",end_time-start_time,"seconds")


