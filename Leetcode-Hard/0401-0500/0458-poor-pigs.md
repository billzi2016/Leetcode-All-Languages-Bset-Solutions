# 0458. Poor Pigs

## Cpp

```cpp
class Solution {
public:
    int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        if (buckets <= 1) return 0;
        int rounds = minutesToTest / minutesToDie;
        int states = rounds + 1; // each pig can die in one of the rounds or survive
        int pigs = 0;
        long long capacity = 1;
        while (capacity < buckets) {
            capacity *= states;
            ++pigs;
        }
        return pigs;
    }
};
```

## Java

```java
class Solution {
    public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        int rounds = minutesToTest / minutesToDie;
        long states = 1;
        int pigs = 0;
        while (states < buckets) {
            pigs++;
            states *= (rounds + 1);
        }
        return pigs;
    }
}
```

## Python

```python
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        rounds = minutesToTest // minutesToDie
        states_per_pig = rounds + 1
        pigs = 0
        capacity = 1
        while capacity < buckets:
            pigs += 1
            capacity *= states_per_pig
        return pigs
```

## Python3

```python
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rounds = minutesToTest // minutesToDie
        base = rounds + 1
        pigs = 0
        while pow(base, pigs) < buckets:
            pigs += 1
        return pigs
```

## C

```c
int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
    if (buckets <= 1) return 0;
    int tests = minutesToTest / minutesToDie; // number of rounds
    long long capacity = 1;
    int pigs = 0;
    while (capacity < buckets) {
        ++pigs;
        capacity *= (tests + 1);
    }
    return pigs;
}
```

## Csharp

```csharp
public class Solution
{
    public int PoorPigs(int buckets, int minutesToDie, int minutesToTest)
    {
        if (buckets <= 1) return 0;
        int rounds = minutesToTest / minutesToDie;
        int statesPerPig = rounds + 1;

        int pigs = 0;
        long capacity = 1;
        while (capacity < buckets)
        {
            capacity *= statesPerPig;
            pigs++;
        }
        return pigs;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} buckets
 * @param {number} minutesToDie
 * @param {number} minutesToTest
 * @return {number}
 */
var poorPigs = function(buckets, minutesToDie, minutesToTest) {
    if (buckets <= 1) return 0;
    const rounds = Math.floor(minutesToTest / minutesToDie);
    const states = rounds + 1; // each pig can have this many distinct outcomes
    let pigs = 0;
    let capacity = 1;
    while (capacity < buckets) {
        capacity *= states;
        pigs++;
    }
    return pigs;
};
```

## Typescript

```typescript
function poorPigs(buckets: number, minutesToDie: number, minutesToTest: number): number {
    if (buckets <= 1) return 0;
    const rounds = Math.floor(minutesToTest / minutesToDie);
    const statesPerPig = rounds + 1;
    let pigs = 0;
    let capacity = 1; // statesPerPig^pigs
    while (capacity < buckets) {
        pigs++;
        capacity *= statesPerPig;
    }
    return pigs;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $buckets
     * @param Integer $minutesToDie
     * @param Integer $minutesToTest
     * @return Integer
     */
    function poorPigs($buckets, $minutesToDie, $minutesToTest) {
        if ($buckets <= 1) {
            return 0;
        }
        $tests = intdiv($minutesToTest, $minutesToDie);
        $states = $tests + 1; // each pig can have this many outcomes
        $pigs = 0;
        $capacity = 1; // states^pigs
        while ($capacity < $buckets) {
            $pigs++;
            $capacity *= $states;
        }
        return $pigs;
    }
}
```

## Swift

```swift
class Solution {
    func poorPigs(_ buckets: Int, _ minutesToDie: Int, _ minutesToTest: Int) -> Int {
        if buckets == 1 { return 0 }
        let tests = minutesToTest / minutesToDie
        var pigs = 0
        var states = 1 // (tests + 1)^pigs
        
        while states < buckets {
            pigs += 1
            // Multiply safely, cap at buckets to avoid overflow
            if states > buckets / (tests + 1) {
                states = buckets
            } else {
                states *= (tests + 1)
            }
        }
        return pigs
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun poorPigs(buckets: Int, minutesToDie: Int, minutesToTest: Int): Int {
        if (buckets == 1) return 0
        val rounds = minutesToTest / minutesToDie
        var pigs = 0
        var states = 1.0
        val base = (rounds + 1).toDouble()
        while (states < buckets) {
            pigs++
            states *= base
        }
        return pigs
    }
}
```

## Dart

```dart
class Solution {
  int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
    if (buckets <= 1) return 0;
    int rounds = minutesToTest ~/ minutesToDie;
    int states = rounds + 1;
    int pigs = 0;
    int capacity = 1;
    while (capacity < buckets) {
      capacity *= states;
      pigs++;
    }
    return pigs;
  }
}
```

## Golang

```go
func poorPigs(buckets int, minutesToDie int, minutesToTest int) int {
	if buckets <= 1 {
		return 0
	}
	tests := minutesToTest / minutesToDie
	statesPerPig := tests + 1

	pigs := 0
	capacity := 1
	for capacity < buckets {
		pigs++
		capacity *= statesPerPig
	}
	return pigs
}
```

## Ruby

```ruby
def poor_pigs(buckets, minutes_to_die, minutes_to_test)
  return 0 if buckets <= 1
  rounds = minutes_to_test / minutes_to_die
  states_per_pig = rounds + 1
  pigs = 0
  capacity = 1
  while capacity < buckets
    pigs += 1
    capacity *= states_per_pig
  end
  pigs
end
```

## Scala

```scala
object Solution {
    def poorPigs(buckets: Int, minutesToDie: Int, minutesToTest: Int): Int = {
        if (buckets <= 1) return 0
        val tests = minutesToTest / minutesToDie
        val states = tests + 1
        var pigs = 0
        var capacity: Long = 1L
        while (capacity < buckets) {
            pigs += 1
            capacity *= states
        }
        pigs
    }
}
```

## Rust

```rust
impl Solution {
    pub fn poor_pigs(buckets: i32, minutes_to_die: i32, minutes_to_test: i32) -> i32 {
        let rounds = minutes_to_test / minutes_to_die;
        let base = (rounds + 1) as i64;
        let mut pigs = 0i32;
        let mut capacity: i64 = 1;
        while capacity < buckets as i64 {
            pigs += 1;
            capacity *= base;
        }
        pigs
    }
}
```

## Racket

```racket
(define/contract (poor-pigs buckets minutesToDie minutesToTest)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ((rounds (quotient minutesToTest minutesToDie))
         (states (+ rounds 1)))
    (let loop ((pigs 0) (capacity 1))
      (if (>= capacity buckets)
          pigs
          (loop (+ pigs 1) (* capacity states))))))
```

## Erlang

```erlang
-module(solution).
-export([poor_pigs/3]).

-spec poor_pigs(Buckets :: integer(), MinutesToDie :: integer(), MinutesToTest :: integer()) -> integer().
poor_pigs(Buckets, MinutesToDie, MinutesToTest) ->
    Rounds = MinutesToTest div MinutesToDie,
    Base = Rounds + 1,
    find_pigs(0, Base, Buckets).

find_pigs(Pigs, Base, Buckets) ->
    case pow(Base, Pigs) >= Buckets of
        true -> Pigs;
        false -> find_pigs(Pigs + 1, Base, Buckets)
    end.

pow(_, 0) -> 1;
pow(B, E) when E > 0 -> B * pow(B, E - 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec poor_pigs(buckets :: integer, minutes_to_die :: integer, minutes_to_test :: integer) :: integer
  def poor_pigs(buckets, minutes_to_die, minutes_to_test) do
    rounds = div(minutes_to_test, minutes_to_die)
    base = rounds + 1

    if buckets <= 1 do
      0
    else
      min_pigs(buckets, base, 0, 1)
    end
  end

  defp min_pigs(buckets, _base, cnt, acc) when acc >= buckets, do: cnt

  defp min_pigs(buckets, base, cnt, acc) do
    min_pigs(buckets, base, cnt + 1, acc * base)
  end
end
```
