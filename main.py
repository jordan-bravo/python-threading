import threading
import time

done = False

def worker(text):
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(f"{text}: {counter}")

thread_a = threading.Thread(target=worker, args=('thread A',))
thread_a.start()
# worker('this is the main thead')

input('Press any key to quit \n')
done = True

############## END OF SCRIPT ################################


# thread_b = threading.Thread(target=worker, daemon=True, args=('thread B',))
# thread_b.start()
