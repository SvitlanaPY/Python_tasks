import threading
import time

def handler(started=0, finished=0):   # started: 0;  finished: 67108864
    result = 0
    for i in range(started, finished):
        result += i
    print('Value: ', result)

params = {'finished': 2 ** 26}   # 2 ** 26 = 67108864

task = threading.Thread(target=handler, kwargs=params)
started_at = time.time()
print('RESULT1')
task.start()
task.join()
print('Time: {}'.format(time.time()-started_at))

started_at = time.time()
print('RESULT2')
handler(**params)
print("Time: {}".format(time.time() - started_at))
