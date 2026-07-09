# 1195. Fizz Buzz Multithreaded

## Cpp

```cpp
class FizzBuzz {
private:
    int n;
    int cur = 1;
    std::mutex mtx;
    std::condition_variable cv;

public:
    FizzBuzz(int n) {
        this->n = n;
    }

    // printFizz() outputs "fizz".
    void fizz(std::function<void()> printFizz) {
        while (true) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [&] { return cur > n || (cur % 3 == 0 && cur % 5 != 0); });
            if (cur > n) break;
            printFizz();
            ++cur;
            cv.notify_all();
        }
    }

    // printBuzz() outputs "buzz".
    void buzz(std::function<void()> printBuzz) {
        while (true) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [&] { return cur > n || (cur % 5 == 0 && cur % 3 != 0); });
            if (cur > n) break;
            printBuzz();
            ++cur;
            cv.notify_all();
        }
    }

    // printFizzBuzz() outputs "fizzbuzz".
    void fizzbuzz(std::function<void()> printFizzBuzz) {
        while (true) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [&] { return cur > n || (cur % 15 == 0); });
            if (cur > n) break;
            printFizzBuzz();
            ++cur;
            cv.notify_all();
        }
    }

    // printNumber(x) outputs "x", where x is an integer.
    void number(std::function<void(int)> printNumber) {
        while (true) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [&] { return cur > n || (cur % 3 != 0 && cur % 5 != 0); });
            if (cur > n) break;
            printNumber(cur);
            ++cur;
            cv.notify_all();
        }
    }
};
```

## Java

```java
import java.util.function.IntConsumer;

class FizzBuzz {
    private final int n;
    private int cur = 1;

    public FizzBuzz(int n) {
        this.n = n;
    }

    // printFizz.run() outputs "fizz".
    public void fizz(Runnable printFizz) throws InterruptedException {
        while (true) {
            synchronized (this) {
                while (cur <= n && !(cur % 3 == 0 && cur % 5 != 0)) {
                    if (cur > n) return;
                    this.wait();
                }
                if (cur > n) {
                    this.notifyAll();
                    return;
                }
                printFizz.run();
                cur++;
                this.notifyAll();
            }
        }
    }

    // printBuzz.run() outputs "buzz".
    public void buzz(Runnable printBuzz) throws InterruptedException {
        while (true) {
            synchronized (this) {
                while (cur <= n && !(cur % 5 == 0 && cur % 3 != 0)) {
                    if (cur > n) return;
                    this.wait();
                }
                if (cur > n) {
                    this.notifyAll();
                    return;
                }
                printBuzz.run();
                cur++;
                this.notifyAll();
            }
        }
    }

    // printFizzBuzz.run() outputs "fizzbuzz".
    public void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
        while (true) {
            synchronized (this) {
                while (cur <= n && !(cur % 15 == 0)) {
                    if (cur > n) return;
                    this.wait();
                }
                if (cur > n) {
                    this.notifyAll();
                    return;
                }
                printFizzBuzz.run();
                cur++;
                this.notifyAll();
            }
        }
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void number(IntConsumer printNumber) throws InterruptedException {
        while (true) {
            synchronized (this) {
                while (cur <= n && (cur % 3 == 0 || cur % 5 == 0)) {
                    if (cur > n) return;
                    this.wait();
                }
                if (cur > n) {
                    this.notifyAll();
                    return;
                }
                printNumber.accept(cur);
                cur++;
                this.notifyAll();
            }
        }
    }
}
```

## Python

```python
import threading

class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.current = 1
        self.cv = threading.Condition()

    def fizz(self, printFizz):
        while True:
            with self.cv:
                while self.current <= self.n and (self.current % 3 != 0 or self.current % 5 == 0):
                    self.cv.wait()
                if self.current > self.n:
                    self.cv.notify_all()
                    return
                printFizz()
                self.current += 1
                self.cv.notify_all()

    def buzz(self, printBuzz):
        while True:
            with self.cv:
                while self.current <= self.n and (self.current % 5 != 0 or self.current % 3 == 0):
                    self.cv.wait()
                if self.current > self.n:
                    self.cv.notify_all()
                    return
                printBuzz()
                self.current += 1
                self.cv.notify_all()

    def fizzbuzz(self, printFizzBuzz):
        while True:
            with self.cv:
                while self.current <= self.n and (self.current % 15 != 0):
                    self.cv.wait()
                if self.current > self.n:
                    self.cv.notify_all()
                    return
                printFizzBuzz()
                self.current += 1
                self.cv.notify_all()

    def number(self, printNumber):
        while True:
            with self.cv:
                while self.current <= self.n and (self.current % 3 == 0 or self.current % 5 == 0):
                    self.cv.wait()
                if self.current > self.n:
                    self.cv.notify_all()
                    return
                printNumber(self.current)
                self.current += 1
                self.cv.notify_all()
```

## Python3

```python
import threading
from typing import Callable

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.current = 1
        self.cv = threading.Condition()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            with self.cv:
                while self.current <= self.n and (self.current % 3 != 0 or self.current % 5 == 0):
                    self.cv.wait()
                if self.current > self.n:
                    self.cv.notify_all()
                    return
                printFizz()
                self.current += 1
                self.cv.notify_all()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.cv:
                while self.current <= self.n and (self.current % 5 != 0 or self.current % 3 == 0):
                    self.cv.wait()
                if self.current > self.n:
                    self.cv.notify_all()
                    return
                printBuzz()
                self.current += 1
                self.cv.notify_all()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.cv:
                while self.current <= self.n and (self.current % 15 != 0):
                    self.cv.wait()
                if self.current > self.n:
                    self.cv.notify_all()
                    return
                printFizzBuzz()
                self.current += 1
                self.cv.notify_all()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.cv:
                while self.current <= self.n and (self.current % 3 == 0 or self.current % 5 == 0):
                    self.cv.wait()
                if self.current > self.n:
                    self.cv.notify_all()
                    return
                printNumber(self.current)
                self.current += 1
                self.cv.notify_all()
```

## C

```c
#include <stdlib.h>
#include <pthread.h>

typedef struct {
    int n;
    int cur;
    pthread_mutex_t mtx;
    pthread_cond_t cv;
} FizzBuzz;

FizzBuzz* fizzBuzzCreate(int n) {
    FizzBuzz* obj = (FizzBuzz*)malloc(sizeof(FizzBuzz));
    obj->n = n;
    obj->cur = 1;
    pthread_mutex_init(&obj->mtx, NULL);
    pthread_cond_init(&obj->cv, NULL);
    return obj;
}

// Don't change the following declarations
void printNumber(int a);
void printFizz();
void printBuzz();
void printFizzBuzz();

void fizz(FizzBuzz* obj) {
    while (1) {
        pthread_mutex_lock(&obj->mtx);
        while (obj->cur <= obj->n && !(obj->cur % 3 == 0 && obj->cur % 5 != 0)) {
            if (obj->cur > obj->n) break;
            pthread_cond_wait(&obj->cv, &obj->mtx);
        }
        if (obj->cur > obj->n) {
            pthread_mutex_unlock(&obj->mtx);
            break;
        }
        printFizz();
        obj->cur++;
        pthread_cond_broadcast(&obj->cv);
        pthread_mutex_unlock(&obj->mtx);
    }
}

void buzz(FizzBuzz* obj) {
    while (1) {
        pthread_mutex_lock(&obj->mtx);
        while (obj->cur <= obj->n && !(obj->cur % 5 == 0 && obj->cur % 3 != 0)) {
            if (obj->cur > obj->n) break;
            pthread_cond_wait(&obj->cv, &obj->mtx);
        }
        if (obj->cur > obj->n) {
            pthread_mutex_unlock(&obj->mtx);
            break;
        }
        printBuzz();
        obj->cur++;
        pthread_cond_broadcast(&obj->cv);
        pthread_mutex_unlock(&obj->mtx);
    }
}

void fizzbuzz(FizzBuzz* obj) {
    while (1) {
        pthread_mutex_lock(&obj->mtx);
        while (obj->cur <= obj->n && !(obj->cur % 15 == 0)) {
            if (obj->cur > obj->n) break;
            pthread_cond_wait(&obj->cv, &obj->mtx);
        }
        if (obj->cur > obj->n) {
            pthread_mutex_unlock(&obj->mtx);
            break;
        }
        printFizzBuzz();
        obj->cur++;
        pthread_cond_broadcast(&obj->cv);
        pthread_mutex_unlock(&obj->mtx);
    }
}

void number(FizzBuzz* obj) {
    while (1) {
        pthread_mutex_lock(&obj->mtx);
        while (obj->cur <= obj->n && (obj->cur % 3 == 0 || obj->cur % 5 == 0)) {
            if (obj->cur > obj->n) break;
            pthread_cond_wait(&obj->cv, &obj->mtx);
        }
        if (obj->cur > obj->n) {
            pthread_mutex_unlock(&obj->mtx);
            break;
        }
        printNumber(obj->cur);
        obj->cur++;
        pthread_cond_broadcast(&obj->cv);
        pthread_mutex_unlock(&obj->mtx);
    }
}

void fizzBuzzFree(FizzBuzz* obj) {
    if (!obj) return;
    pthread_mutex_destroy(&obj->mtx);
    pthread_cond_destroy(&obj->cv);
    free(obj);
}
```

## Csharp

```csharp
public class FizzBuzz {
    private readonly int n;
    private int cur = 1;
    private readonly object lockObj = new object();

    public FizzBuzz(int n) {
        this.n = n;
    }

    // printFizz() outputs "fizz".
    public void Fizz(Action printFizz) {
        while (true) {
            lock (lockObj) {
                while (cur <= n && !(cur % 3 == 0 && cur % 5 != 0)) {
                    System.Threading.Monitor.Wait(lockObj);
                }
                if (cur > n) {
                    System.Threading.Monitor.PulseAll(lockObj);
                    return;
                }
                printFizz();
                cur++;
                System.Threading.Monitor.PulseAll(lockObj);
            }
        }
    }

    // printBuzz() outputs "buzz".
    public void Buzz(Action printBuzz) {
        while (true) {
            lock (lockObj) {
                while (cur <= n && !(cur % 5 == 0 && cur % 3 != 0)) {
                    System.Threading.Monitor.Wait(lockObj);
                }
                if (cur > n) {
                    System.Threading.Monitor.PulseAll(lockObj);
                    return;
                }
                printBuzz();
                cur++;
                System.Threading.Monitor.PulseAll(lockObj);
            }
        }
    }

    // printFizzBuzz() outputs "fizzbuzz".
    public void Fizzbuzz(Action printFizzBuzz) {
        while (true) {
            lock (lockObj) {
                while (cur <= n && !(cur % 15 == 0)) {
                    System.Threading.Monitor.Wait(lockObj);
                }
                if (cur > n) {
                    System.Threading.Monitor.PulseAll(lockObj);
                    return;
                }
                printFizzBuzz();
                cur++;
                System.Threading.Monitor.PulseAll(lockObj);
            }
        }
    }

    // printNumber(x) outputs "x", where x is an integer.
    public void Number(Action<int> printNumber) {
        while (true) {
            lock (lockObj) {
                while (cur <= n && !(cur % 3 != 0 && cur % 5 != 0)) {
                    System.Threading.Monitor.Wait(lockObj);
                }
                if (cur > n) {
                    System.Threading.Monitor.PulseAll(lockObj);
                    return;
                }
                printNumber(cur);
                cur++;
                System.Threading.Monitor.PulseAll(lockObj);
            }
        }
    }
}
```
