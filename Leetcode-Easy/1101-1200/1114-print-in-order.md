# 1114. Print in Order

## Cpp

```cpp
#include <functional>
#include <mutex>
#include <condition_variable>

class Foo {
    std::mutex m_;
    std::condition_variable cv_;
    bool first_done_ = false;
    bool second_done_ = false;
public:
    Foo() {}

    void first(std::function<void()> printFirst) {
        printFirst();
        {
            std::lock_guard<std::mutex> lk(m_);
            first_done_ = true;
        }
        cv_.notify_all();
    }

    void second(std::function<void()> printSecond) {
        {
            std::unique_lock<std::mutex> lk(m_);
            cv_.wait(lk, [this]{ return first_done_; });
        }
        printSecond();
        {
            std::lock_guard<std::mutex> lk(m_);
            second_done_ = true;
        }
        cv_.notify_all();
    }

    void third(std::function<void()> printThird) {
        {
            std::unique_lock<std::mutex> lk(m_);
            cv_.wait(lk, [this]{ return second_done_; });
        }
        printThird();
    }
};
```

## Java

```java
class Foo {
    private final java.util.concurrent.CountDownLatch firstDone = new java.util.concurrent.CountDownLatch(1);
    private final java.util.concurrent.CountDownLatch secondDone = new java.util.concurrent.CountDownLatch(1);

    public Foo() {
    }

    public void first(Runnable printFirst) throws InterruptedException {
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        firstDone.countDown();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        firstDone.await();
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        secondDone.countDown();
    }

    public void third(Runnable printThird) throws InterruptedException {
        secondDone.await();
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}
```

## Python

```python
import threading

class Foo(object):
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_done.set()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.first_done.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_done.set()

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.second_done.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
```

## Python3

```python
import threading

class Foo:
    def __init__(self):
        self.first_done = threading.Semaphore(0)
        self.second_done = threading.Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_done.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_done.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_done.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_done.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
```

## C

```c
#include <stdlib.h>
#include <semaphore.h>

typedef struct {
    sem_t sem2;
    sem_t sem3;
} Foo;

// Function Declaration, do not remove
void printFirst();
void printSecond();
void printThird();

Foo* fooCreate() {
    Foo* obj = (Foo*)malloc(sizeof(Foo));
    if (!obj) return NULL;
    sem_init(&obj->sem2, 0, 0);
    sem_init(&obj->sem3, 0, 0);
    return obj;
}

void first(Foo* obj) {
    // printFirst() outputs "first". Do not change or remove this line.
    printFirst();
    sem_post(&obj->sem2);   // allow second()
}

void second(Foo* obj) {
    sem_wait(&obj->sem2);   // wait for first()
    // printSecond() outputs "second". Do not change or remove this line.
    printSecond();
    sem_post(&obj->sem3);   // allow third()
}

void third(Foo* obj) {
    sem_wait(&obj->sem3);   // wait for second()
    // printThird() outputs "third". Do not change or remove this line.
    printThird();
}

void fooFree(Foo* obj) {
    if (!obj) return;
    sem_destroy(&obj->sem2);
    sem_destroy(&obj->sem3);
    free(obj);
}
```

## Csharp

```csharp
using System;
using System.Threading;

public class Foo {
    private readonly ManualResetEventSlim _firstDone = new ManualResetEventSlim(false);
    private readonly ManualResetEventSlim _secondDone = new ManualResetEventSlim(false);

    public Foo() { }

    public void First(Action printFirst) {
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        _firstDone.Set();
    }

    public void Second(Action printSecond) {
        _firstDone.Wait();
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        _secondDone.Set();
    }

    public void Third(Action printThird) {
        _secondDone.Wait();
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
    }
}
```
