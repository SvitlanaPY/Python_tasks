import threading
import time

def producer():
    time.sleep(10)
    print("Product found!")
    product.set()   # повідомляє всіх слухачів, що подія відбулась
    product.clear()   # очищуємо подію і потрібно знову її чекати

def consumer():
    print('product wait')
    product.wait()   # той, хто очікує подію
    print("Product exists!")

product = threading.Event()   # екземпляр класу Event

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=consumer)

task1.start()
task2.start()

task1.join()
task2.join()
