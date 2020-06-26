import threading
import time
def hilo_1():
    print("Hilo 1")
def hilo_2():
    time.perf_counter()
    while time.perf_counter() < 3:
        pass
    print("Hilo 2")
if __name__ == "__main__":
    thread = threading.Thread(target=hilo_2)
    thread.start()
    hilo_1()
    a = input("DENETER BUCLE:")
    if a == "a":
        thread._stop()
    #thread.join()
    