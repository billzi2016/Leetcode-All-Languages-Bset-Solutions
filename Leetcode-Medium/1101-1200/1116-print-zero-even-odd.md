# 1116. Print Zero Even Odd

## Cpp

```cpp
#include <functional>
#include <mutex>
#include <condition_variable>

class ZeroEvenOdd {
private:
    int n;
    int cur = 1;                 // next number to print
    int state = 0;               // 0: zero turn, 1: odd turn, 2: even turn
    std::mutex mtx;
    std::condition_variable cv;

public:
    ZeroEvenOdd(int n) {
        this->n = n;
    }

    // printNumber(x) outputs "x", where x is an integer.
    void zero(std::function<void(int)> printNumber) {
        for (int i = 0; i < n; ++i) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [&] { return state == 0; });
            printNumber(0);
            state = (cur % 2 == 1) ? 1 : 2;
            cv.notify_all();
        }
        // Wake up any waiting threads so they can terminate
        std::unique_lock<std::mutex> lock(mtx);
        cv.notify_all();
    }

    void odd(std::function<void(int)> printNumber) {
        while (true) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [&] { return state == 1 || cur > n; });
            if (cur > n) break;
            printNumber(cur);
            ++cur;
            state = 0;
            cv.notify_all();
        }
    }

    void even(std::function<void(int)> printNumber) {
        while (true) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [&] { return state == 2 || cur > n; });
            if (cur > n) break;
            printNumber(cur);
            ++cur;
            state = 0;
            cv.notify_all();
        }
    }
};
```

## Java

```java
import java.util.concurrent.Semaphore;
import java.util.function.IntConsumer;

class ZeroEvenOdd {
    private int n;
    private final Semaphore zero = new Semaphore(1);
    private final Semaphore odd = new Semaphore(0);
    private final Semaphore even = new Semaphore(0);

    public ZeroEvenOdd(int n) {
        this.n = n;
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n; i++) {
            zero.acquire();
            printNumber.accept(0);
            if ((i & 1) == 1) {
                odd.release();
            } else {
                even.release();
            }
        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n; i += 2) {
            odd.acquire();
            printNumber.accept(i);
            zero.release();
        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        for (int i = 2; i <= n; i += 2) {
            even.acquire();
            printNumber.accept(i);
            zero.release();
        }
    }
}
```

## Python

```python
import threading

class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.zero_sem = threading.Semaphore(1)
        self.even_sem = threading.Semaphore(0)
        self.odd_sem = threading.Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n + 1):
            self.zero_sem.acquire()
            printNumber(0)
            if i % 2:
                self.odd_sem.release()
            else:
                self.even_sem.release()

    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(2, self.n + 1, 2):
            self.even_sem.acquire()
            printNumber(i)
            self.zero_sem.release()

    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n + 1, 2):
            self.odd_sem.acquire()
            printNumber(i)
            self.zero_sem.release()
```

## Python3

```python
import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_sem = threading.Semaphore(1)
        self.even_sem = threading.Semaphore(0)
        self.odd_sem = threading.Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.zero_sem.acquire()
            printNumber(0)
            if i % 2 == 1:
                self.odd_sem.release()
            else:
                self.even_sem.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.even_sem.acquire()
            printNumber(i)
            self.zero_sem.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_sem.acquire()
            printNumber(i)
            self.zero_sem.release()
```

## C

```c
#include <stdlib.h>
#include <semaphore.h>

typedef struct {
    int n;
    sem_t zeroSem;
    sem_t oddSem;
    sem_t evenSem;
} ZeroEvenOdd;

ZeroEvenOdd* zeroEvenOddCreate(int n) {
    ZeroEvenOdd* obj = (ZeroEvenOdd*)malloc(sizeof(ZeroEvenOdd));
    obj->n = n;
    sem_init(&obj->zeroSem, 0, 1);
    sem_init(&obj->oddSem, 0, 0);
    sem_init(&obj->evenSem, 0, 0);
    return obj;
}

// You may call global function `void printNumber(int x)`
// to output "x", where x is an integer.

void zero(ZeroEvenOdd* obj) {
    for (int i = 1; i <= obj->n; ++i) {
        sem_wait(&obj->zeroSem);
        printNumber(0);
        if (i % 2 == 1)
            sem_post(&obj->oddSem);
        else
            sem_post(&obj->evenSem);
    }
}

void odd(ZeroEvenOdd* obj) {
    for (int i = 1; i <= obj->n; i += 2) {
        sem_wait(&obj->oddSem);
        printNumber(i);
        sem_post(&obj->zeroSem);
    }
}

void even(ZeroEvenOdd* obj) {
    for (int i = 2; i <= obj->n; i += 2) {
        sem_wait(&obj->evenSem);
        printNumber(i);
        sem_post(&obj->zeroSem);
    }
}

void zeroEvenOddFree(ZeroEvenOdd* obj) {
    sem_destroy(&obj->zeroSem);
    sem_destroy(&obj->oddSem);
    sem_destroy(&obj->evenSem);
    free(obj);
}
```

## Csharp

```csharp
using System;
using System.Threading;

public class ZeroEvenOdd {
    private int n;
    private SemaphoreSlim zeroSem = new SemaphoreSlim(1);
    private SemaphoreSlim oddSem = new SemaphoreSlim(0);
    private SemaphoreSlim evenSem = new SemaphoreSlim(0);

    public ZeroEvenOdd(int n) {
        this.n = n;
    }

    // printNumber(x) outputs "x", where x is an integer.
    public void Zero(Action<int> printNumber) {
        for (int i = 1; i <= n; i++) {
            zeroSem.Wait();
            printNumber(0);
            if ((i & 1) == 1) {
                oddSem.Release();
            } else {
                evenSem.Release();
            }
        }
    }

    public void Even(Action<int> printNumber) {
        for (int i = 2; i <= n; i += 2) {
            evenSem.Wait();
            printNumber(i);
            zeroSem.Release();
        }
    }

    public void Odd(Action<int> printNumber) {
        for (int i = 1; i <= n; i += 2) {
            oddSem.Wait();
            printNumber(i);
            zeroSem.Release();
        }
    }
}
```
