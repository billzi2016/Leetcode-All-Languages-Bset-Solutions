# 2126. Destroying Asteroids

## Cpp

```cpp
class Solution {
public:
    bool asteroidsDestroyed(int mass, vector<int>& asteroids) {
        sort(asteroids.begin(), asteroids.end());
        long long cur = mass;
        for (int a : asteroids) {
            if (cur < a) return false;
            cur += a;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean asteroidsDestroyed(int mass, int[] asteroids) {
        java.util.Arrays.sort(asteroids);
        long cur = mass; // use long to avoid overflow
        for (int a : asteroids) {
            if (cur < a) return false;
            cur += a;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()
        for a in asteroids:
            if mass < a:
                return False
            mass += a
        return True
```

## Python3

```python
from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for a in asteroids:
            if mass < a:
                return False
            mass += a
        return True
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

static int cmpInt(const void *a, const void *b) {
    int ai = *(const int *)a;
    int bi = *(const int *)b;
    return ai - bi;
}

bool asteroidsDestroyed(int mass, int* asteroids, int asteroidsSize) {
    qsort(asteroids, (size_t)asteroidsSize, sizeof(int), cmpInt);
    for (int i = 0; i < asteroidsSize; ++i) {
        if (mass >= asteroids[i]) {
            mass += asteroids[i];
        } else {
            return false;
        }
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool AsteroidsDestroyed(int mass, int[] asteroids) {
        Array.Sort(asteroids);
        foreach (int a in asteroids) {
            if (mass < a) return false;
            mass += a;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} mass
 * @param {number[]} asteroids
 * @return {boolean}
 */
var asteroidsDestroyed = function(mass, asteroids) {
    asteroids.sort((a, b) => a - b);
    for (let a of asteroids) {
        if (mass < a) return false;
        mass += a;
    }
    return true;
};
```

## Typescript

```typescript
function asteroidsDestroyed(mass: number, asteroids: number[]): boolean {
    asteroids.sort((a, b) => a - b);
    for (const a of asteroids) {
        if (mass < a) return false;
        mass += a;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $mass
     * @param Integer[] $asteroids
     * @return Boolean
     */
    function asteroidsDestroyed($mass, $asteroids) {
        sort($asteroids);
        foreach ($asteroids as $a) {
            if ($mass < $a) {
                return false;
            }
            $mass += $a;
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func asteroidsDestroyed(_ mass: Int, _ asteroids: [Int]) -> Bool {
        var currentMass = mass
        let sortedAsteroids = asteroids.sorted()
        for asteroid in sortedAsteroids {
            if currentMass < asteroid {
                return false
            }
            currentMass += asteroid
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun asteroidsDestroyed(mass: Int, asteroids: IntArray): Boolean {
        var current = mass.toLong()
        asteroids.sort()
        for (a in asteroids) {
            if (current < a) return false
            current += a
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool asteroidsDestroyed(int mass, List<int> asteroids) {
    asteroids.sort();
    for (int a in asteroids) {
      if (mass < a) return false;
      mass += a;
    }
    return true;
  }
}
```

## Golang

```go
func asteroidsDestroyed(mass int, asteroids []int) bool {
    sort.Ints(asteroids)
    for _, a := range asteroids {
        if mass < a {
            return false
        }
        mass += a
    }
    return true
}
```

## Ruby

```ruby
def asteroids_destroyed(mass, asteroids)
  asteroids.sort.each do |a|
    return false if mass < a
    mass += a
  end
  true
end
```

## Scala

```scala
object Solution {
    def asteroidsDestroyed(mass: Int, asteroids: Array[Int]): Boolean = {
        val sorted = asteroids.sorted
        var curMass: Long = mass.toLong
        for (a <- sorted) {
            if (curMass < a) return false
            curMass += a
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn asteroids_destroyed(mass: i32, mut asteroids: Vec<i32>) -> bool {
        asteroids.sort_unstable();
        let mut cur = mass as i64;
        for a in asteroids {
            if cur >= a as i64 {
                cur += a as i64;
            } else {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (asteroids-destroyed mass asteroids)
  (-> exact-integer? (listof exact-integer?) boolean?)
  (let* ((sorted (sort asteroids <)))
    (let loop ((cur mass) (lst sorted))
      (cond
        [(null? lst) #t]
        [(>= cur (car lst)) (loop (+ cur (car lst)) (cdr lst))]
        [else #f]))))
```

## Erlang

```erlang
-module(solution).
-export([asteroids_destroyed/2]).

-spec asteroids_destroyed(Mass :: integer(), Asteroids :: [integer()]) -> boolean().
asteroids_destroyed(Mass, Asteroids) ->
    Sorted = lists:sort(Asteroids),
    can_destroy(Sorted, Mass).

can_destroy([], _Mass) -> true;
can_destroy([A|Rest], Mass) when Mass >= A ->
    can_destroy(Rest, Mass + A);
can_destroy(_, _) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec asteroids_destroyed(mass :: integer, asteroids :: [integer]) :: boolean
  def asteroids_destroyed(mass, asteroids) do
    result =
      asteroids
      |> Enum.sort()
      |> Enum.reduce_while(mass, fn a, cur_mass ->
        if cur_mass >= a do
          {:cont, cur_mass + a}
        else
          {:halt, false}
        end
      end)

    case result do
      false -> false
      _ -> true
    end
  end
end
```
