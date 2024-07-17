import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self.semFoo = threading.Semaphore(value=1)
        self.semBar = threading.Semaphore(value=0)


    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.semFoo.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.semBar.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.semBar.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.semFoo.release()
