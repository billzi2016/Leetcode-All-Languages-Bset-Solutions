# 1226. The Dining Philosophers

## Cpp

```cpp
#include <functional>
#include <mutex>
#include <array>

class DiningPhilosophers {
    std::array<std::mutex, 5> forks;
public:
    DiningPhilosophers() {}

    void wantsToEat(int philosopher,
                    std::function<void()> pickLeftFork,
                    std::function<void()> pickRightFork,
                    std::function<void()> eat,
                    std::function<void()> putLeftFork,
                    std::function<void()> putRightFork) {
        int left = philosopher;
        int right = (philosopher + 1) % 5;

        std::unique_lock<std::mutex> lockLeft(forks[left], std::defer_lock);
        std::unique_lock<std::mutex> lockRight(forks[right], std::defer_lock);
        std::lock(lockLeft, lockRight); // acquire both without deadlock

        pickLeftFork();
        pickRightFork();

        eat();

        putLeftFork();
        putRightFork();
        // locks are released automatically when going out of scope
    }
};
```

## Java

```java
import java.util.concurrent.Semaphore;

class DiningPhilosophers {

    private final Semaphore[] forks = new Semaphore[5];

    public DiningPhilosophers() {
        for (int i = 0; i < 5; i++) {
            forks[i] = new Semaphore(1);
        }
    }

    // call the run() method of any runnable to execute its code
    public void wantsToEat(int philosopher,
                           Runnable pickLeftFork,
                           Runnable pickRightFork,
                           Runnable eat,
                           Runnable putLeftFork,
                           Runnable putRightFork) throws InterruptedException {
        int left = philosopher;
        int right = (philosopher + 1) % 5;

        if (philosopher % 2 == 0) { // even: pick left then right
            forks[left].acquire();
            pickLeftFork.run();

            forks[right].acquire();
            pickRightFork.run();
        } else { // odd: pick right then left
            forks[right].acquire();
            pickRightFork.run();

            forks[left].acquire();
            pickLeftFork.run();
        }

        eat.run();

        if (philosopher % 2 == 0) {
            putRightFork.run();
            forks[right].release();

            putLeftFork.run();
            forks[left].release();
        } else {
            putLeftFork.run();
            forks[left].release();

            putRightFork.run();
            forks[right].release();
        }
    }
}
```

## Python

```python
import threading

class DiningPhilosophers:
    def __init__(self):
        self.forks = [threading.Lock() for _ in range(5)]
        # allow at most 4 philosophers to try picking forks simultaneously
        self.sema = threading.Semaphore(4)

    def wantsToEat(self, philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork):
        left = philosopher
        right = (philosopher + 1) % 5

        # limit concurrency to avoid deadlock
        self.sema.acquire()

        # acquire forks
        self.forks[left].acquire()
        pickLeftFork()
        self.forks[right].acquire()
        pickRightFork()

        # eat
        eat()

        # put down forks
        putLeftFork()
        self.forks[left].release()
        putRightFork()
        self.forks[right].release()

        # release semaphore slot
        self.sema.release()
```

## Python3

```python
import threading

class DiningPhilosophers:
    def __init__(self):
        self.forks = [threading.Lock() for _ in range(5)]

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        left = philosopher
        right = (philosopher + 1) % 5

        # Acquire forks in a global order to avoid deadlock
        first, second = (left, right) if left < right else (right, left)

        # Pick up first fork
        self.forks[first].acquire()
        if first == left:
            pickLeftFork()
        else:
            pickRightFork()

        # Pick up second fork
        self.forks[second].acquire()
        if second == left:
            pickLeftFork()
        else:
            pickRightFork()

        # Eat
        eat()

        # Put down forks (reverse order)
        if second == left:
            putLeftFork()
        else:
            putRightFork()
        self.forks[second].release()

        if first == left:
            putLeftFork()
        else:
            putRightFork()
        self.forks[first].release()
```
