from MyThread import MyThread
from time import ctime, sleep

def fac(x):
    sleep(x/10)
    if(x < 2):  return 1
    return x * fac(x - 1)

def main():
    threads =[]
    for i in range(3):
        t = MyThread(fac, (10-i,), fac.__name__)
        threads.append(t)

    for i in range(3):
        threads[i].start()

    for i in range(3):
        threads[i].join()
        print(threads[i].getResult())

if __name__ == "__main__":
    main()