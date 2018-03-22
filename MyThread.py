import threading
from threading import Lock

lock = Lock()

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        '''
        构造函数，指定函数、参数、函数名称
        :param func: 函数
        :param args: 参数列表
        :param name: 函数名称
        '''
        lock.acquire()
        threading.Thread.__init__(self)     #Thread的子类的构造器，必须调用父类的构造器
        self.name = name
        self.args = args
        self.func = func
        lock.release()

    def getResult(self):
        return self.res

    def run(self):
        self.res = self.func(*self.args)

