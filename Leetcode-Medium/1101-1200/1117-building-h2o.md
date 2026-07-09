# 1117. Building H2O

## Cpp

```cpp
class H2O {
private:
    std::mutex mtx;
    std::condition_variable cv;
    int hydrogenCount = 0;   // number of H threads in current molecule
    int oxygenCount = 0;     // number of O threads in current molecule
    int finished = 0;        // threads that have completed release in current molecule

public:
    H2O() {}

    void hydrogen(std::function<void()> releaseHydrogen) {
        std::unique_lock<std::mutex> lock(mtx);
        while (hydrogenCount == 2) {               // wait for next molecule slot
            cv.wait(lock);
        }
        ++hydrogenCount;
        if (hydrogenCount == 2 && oxygenCount == 1) {
            cv.notify_all();                       // molecule ready
        } else {
            cv.wait(lock, [&] { return hydrogenCount == 2 && oxygenCount == 1; });
        }
        lock.unlock();

        releaseHydrogen();

        lock.lock();
        ++finished;
        if (finished == 3) {                       // all three threads done
            hydrogenCount = 0;
            oxygenCount = 0;
            finished = 0;
            cv.notify_all();                       // wake up next batch
        }
        lock.unlock();
    }

    void oxygen(std::function<void()> releaseOxygen) {
        std::unique_lock<std::mutex> lock(mtx);
        while (oxygenCount == 1) {                  // wait for next molecule slot
            cv.wait(lock);
        }
        ++oxygenCount;
        if (hydrogenCount == 2 && oxygenCount == 1) {
            cv.notify_all();                       // molecule ready
        } else {
            cv.wait(lock, [&] { return hydrogenCount == 2 && oxygenCount == 1; });
        }
        lock.unlock();

        releaseOxygen();

        lock.lock();
        ++finished;
        if (finished == 3) {                       // all three threads done
            hydrogenCount = 0;
            oxygenCount = 0;
            finished = 0;
            cv.notify_all();                       // wake up next batch
        }
        lock.unlock();
    }
};
```

## Java

```java
import java.util.concurrent.Semaphore;
import java.util.concurrent.CyclicBarrier;
import java.util.concurrent.BrokenBarrierException;

class H2O {
    private final Semaphore hSem = new Semaphore(2);
    private final Semaphore oSem = new Semaphore(1);
    private final CyclicBarrier barrier = new CyclicBarrier(3, () -> {
        // Reset permits for the next molecule
        hSem.release(2);
        oSem.release(1);
    });

    public H2O() { }

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
        hSem.acquire();
        releaseHydrogen.run();
        try {
            barrier.await();
        } catch (BrokenBarrierException e) {
            Thread.currentThread().interrupt();
        }
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        oSem.acquire();
        releaseOxygen.run();
        try {
            barrier.await();
        } catch (BrokenBarrierException e) {
            Thread.currentThread().interrupt();
        }
    }
}
```

## Python

```python
import threading

class H2O(object):
    def __init__(self):
        self.h_sem = threading.Semaphore(2)   # allow two hydrogens per molecule
        self.o_sem = threading.Semaphore(1)   # allow one oxygen per molecule
        self.barrier = threading.Barrier(3)   # synchronize three threads

    def hydrogen(self, releaseHydrogen):
        """
        :type releaseHydrogen: method
        :rtype: void
        """
        self.h_sem.acquire()
        try:
            self.barrier.wait()
            releaseHydrogen()
        finally:
            self.h_sem.release()

    def oxygen(self, releaseOxygen):
        """
        :type releaseOxygen: method
        :rtype: void
        """
        self.o_sem.acquire()
        try:
            self.barrier.wait()
            releaseOxygen()
        finally:
            self.o_sem.release()
```

## Python3

```python
import threading

class H2O:
    def __init__(self):
        self.h_sem = threading.Semaphore(2)
        self.o_sem = threading.Semaphore(1)
        self.barrier = threading.Barrier(3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h_sem.acquire()
        try:
            self.barrier.wait()
            releaseHydrogen()
        finally:
            self.h_sem.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_sem.acquire()
        try:
            self.barrier.wait()
            releaseOxygen()
        finally:
            self.o_sem.release()
```

## C

```c
typedef struct {
    pthread_mutex_t lock;
    sem_t hSem;
    sem_t oSem;
    int hCount;
    int oCount;
} H2O;

void releaseHydrogen();
void releaseOxygen();

H2O* h2oCreate() {
    H2O* obj = (H2O*)malloc(sizeof(H2O));
    pthread_mutex_init(&obj->lock, NULL);
    sem_init(&obj->hSem, 0, 2);   // allow two hydrogens per molecule
    sem_init(&obj->oSem, 0, 1);   // allow one oxygen per molecule
    obj->hCount = 0;
    obj->oCount = 0;
    return obj;
}

static void tryReset(H2O* obj) {
    if (obj->hCount == 2 && obj->oCount == 1) {
        obj->hCount = 0;
        obj->oCount = 0;
        // release permits for the next molecule
        sem_post(&obj->hSem);
        sem_post(&obj->hSem);
        sem_post(&obj->oSem);
    }
}

void hydrogen(H2O* obj) {
    sem_wait(&obj->hSem);          // acquire slot for hydrogen
    releaseHydrogen();             // output "H"
    pthread_mutex_lock(&obj->lock);
    obj->hCount++;
    tryReset(obj);
    pthread_mutex_unlock(&obj->lock);
}

void oxygen(H2O* obj) {
    sem_wait(&obj->oSem);          // acquire slot for oxygen
    releaseOxygen();               // output "O"
    pthread_mutex_lock(&obj->lock);
    obj->oCount++;
    tryReset(obj);
    pthread_mutex_unlock(&obj->lock);
}

void h2oFree(H2O* obj) {
    if (!obj) return;
    sem_destroy(&obj->hSem);
    sem_destroy(&obj->oSem);
    pthread_mutex_destroy(&obj->lock);
    free(obj);
}
```

## Csharp

```csharp
public class H2O
{
    private readonly SemaphoreSlim _hydrogen = new SemaphoreSlim(2);
    private readonly SemaphoreSlim _oxygen = new SemaphoreSlim(1);
    private readonly Barrier _barrier;

    public H2O()
    {
        _barrier = new Barrier(3, b =>
        {
            // reset permits for the next molecule
            _hydrogen.Release(2);
            _oxygen.Release(1);
        });
    }

    public void Hydrogen(Action releaseHydrogen)
    {
        _hydrogen.Wait();
        releaseHydrogen();
        _barrier.SignalAndWait();
    }

    public void Oxygen(Action releaseOxygen)
    {
        _oxygen.Wait();
        releaseOxygen();
        _barrier.SignalAndWait();
    }
}
```
