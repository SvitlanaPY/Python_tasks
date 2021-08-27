import threading
import time

def handler(started=0, finished=0):   # started: 0;  finished: 67108864
    result = 0   # result after task1 = 140737471580160;  result after task2 = 140737479966720
    for i in range(started, finished):
        result += i
    results.append(result)

# params = {'finished': 2 ** 26}   # 2 ** 26 = 67108864

results = []

task1 = threading.Thread(target=handler, kwargs={'finished': 2**12})   # from 0 to 2**12
task2 = threading.Thread(target=handler, kwargs={'started': 2**12, 'finished': 2**24})   # from 2**12 to 2**24

started_at = time.time()
task1.start()
task2.start()

task1.join()
task2.join()

print('RESULTS 1')
print('Time: {}'.format(time.time()-started_at))
print('Value: ', sum(results))

results = []
started_at = time.time()
handler(finished=2**24)
print('RESULT2')
print("Time: {}".format(time.time() - started_at))
print('Value: ', sum(results))
