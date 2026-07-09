# 1115. Print FooBar Alternately

## Cpp

```cpp
#include <functional>
#include <mutex>
#include <condition_variable>

class FooBar {
private:
    int n;
    std::mutex mtx;
    std::condition_variable cv;
    bool fooTurn = true;

public:
    FooBar(int n) {
        this->n = n;
    }

    void foo(std::function<void()> printFoo) {
        for (int i = 0; i < n; ++i) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [this] { return fooTurn; });
            // printFoo() outputs "foo". Do not change or remove this line.
            printFoo();
            fooTurn = false;
            lock.unlock();
            cv.notify_one();
        }
    }

    void bar(std::function<void()> printBar) {
        for (int i = 0; i < n; ++i) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [this] { return !fooTurn; });
            // printBar() outputs "bar". Do not change or remove this line.
            printBar();
            fooTurn = true;
            lock.unlock();
            cv.notify_one();
        }
    }
};
```

## Java

```java
import java.util.concurrent.Semaphore;

class FooBar {
    private int n;
    private final Semaphore fooSem = new Semaphore(1);
    private final Semaphore barSem = new Semaphore(0);

    public FooBar(int n) {
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            fooSem.acquire();
            // printFoo.run() outputs "foo". Do not change or remove this line.
            printFoo.run();
            barSem.release();
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        for (int i = 0; i < n; i++) {
            barSem.acquire();
            // printBar.run() outputs "bar". Do not change or remove this line.
            printBar.run();
            fooSem.release();
        }
    }
}
```

## Python

```python
import threading

class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.foo_sem = threading.Semaphore(1)
        self.bar_sem = threading.Semaphore(0)

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.foo_sem.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_sem.release()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.bar_sem.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_sem.release()
```

## Python3

```python
import threading
from typing import Callable

class FooBar:
    def __init__(self, n):
        self.n = n
        self._foo_sem = threading.Semaphore(1)
        self._bar_sem = threading.Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            self._foo_sem.acquire()
            printFoo()
            self._bar_sem.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            self._bar_sem.acquire()
            printBar()
            self._foo_sem.release()
```

## C

```c
#include <stdlib.h>
#include <pthread.h>

typedef struct {
    int n;
} FooBar;

// Function declarations. Do not change or remove this line
void printFoo();
void printBar();

static pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
static pthread_cond_t cond = PTHREAD_COND_INITIALIZER;
static int turn = 0; // 0: foo's turn, 1: bar's turn

FooBar* fooBarCreate(int n) {
    FooBar* obj = (FooBar*)malloc(sizeof(FooBar));
    obj->n = n;
    return obj;
}

void foo(FooBar* obj) {
    for (int i = 0; i < obj->n; i++) {
        pthread_mutex_lock(&lock);
        while (turn != 0) {
            pthread_cond_wait(&cond, &lock);
        }
        // printFoo() outputs "foo". Do not change or remove this line.
        printFoo();
        turn = 1;
        pthread_cond_signal(&cond);
        pthread_mutex_unlock(&lock);
    }
}

void bar(FooBar* obj) {
    for (int i = 0; i < obj->n; i++) {
        pthread_mutex_lock(&lock);
        while (turn != 1) {
            pthread_cond_wait(&cond, &lock);
        }
        // printBar() outputs "bar". Do not change or remove this line.
        printBar();
        turn = 0;
        pthread_cond_signal(&cond);
        pthread_mutex_unlock(&lock);
    }
}

void fooBarFree(FooBar* obj) {
    free(obj);
}
```

## Csharp

```csharp
using System;
using System.Threading;

public class FooBar {
    private int n;
    private SemaphoreSlim fooSem = new SemaphoreSlim(1);
    private SemaphoreSlim barSem = new SemaphoreSlim(0);

    public FooBar(int n) {
        this.n = n;
    }

    public void Foo(Action printFoo) {
        for (int i = 0; i < n; i++) {
            fooSem.Wait();
            // printFoo() outputs "foo". Do not change or remove this line.
            printFoo();
            barSem.Release();
        }
    }

    public void Bar(Action printBar) {
        for (int i = 0; i < n; i++) {
            barSem.Wait();
            // printBar() outputs "bar". Do not change or remove this line.
            printBar();
            fooSem.Release();
        }
    }
}
```

## Golang

```go
type FooBar struct {
	n   int
	foo chan struct{}
	bar chan struct{}
}

func NewFooBar(n int) *FooBar {
	fb := &FooBar{
		n:   n,
		foo: make(chan struct{}, 1),
		bar: make(chan struct{}),
	}
	// start with foo allowed to print first
	fb.foo <- struct{}{}
	return fb
}

func (fb *FooBar) Foo(printFoo func()) {
	for i := 0; i < fb.n; i++ {
		<-fb.foo
		printFoo()
		fb.bar <- struct{}{}
	}
}

func (fb *FooBar) Bar(printBar func()) {
	for i := 0; i < fb.n; i++ {
		<-fb.bar
		printBar()
		fb.foo <- struct{}{}
	}
}
```
