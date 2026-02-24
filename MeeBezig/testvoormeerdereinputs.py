import threading
import time
data = None
def get_input():
    global data
    input()
    data = "4"
def get_input2():
    time.sleep(5)
    global data
    data = "2"
input_thread = threading.Thread(target=get_input)
input_thread.start()
input2_thread = threading.Thread(target=get_input2)
input2_thread.start()

while data is None:
    print("5")
    time.sleep(0.1)
print(data)