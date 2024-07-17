import threading

from concurrent import futures


class Foo:
    def __init__(self):
        self.semSecond = threading.Semaphore(value=0)
        self.semThird = threading.Semaphore(value=0)
        pass

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        print('first')
        self.semSecond.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.semSecond.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        print('second')
        self.semThird.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.semThird.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        print('third')
        self.semThird.release()


someClass = Foo()
with futures.ThreadPoolExecutor(3) as executor:
    executor.submit(someClass.second, None)
    executor.submit(someClass.third, None)
    executor.submit(someClass.first, None)
