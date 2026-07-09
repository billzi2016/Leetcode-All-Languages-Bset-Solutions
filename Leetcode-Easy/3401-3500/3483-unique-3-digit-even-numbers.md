# 3483. Unique 3-Digit Even Numbers

## Cpp

```cpp
class Solution {
public:
    int totalNumbers(vector<int>& digits) {
        int n = digits.size();
        unordered_set<int> uniq;
        for (int i = 0; i < n; ++i) {
            if (digits[i] == 0) continue; // leading zero not allowed
            for (int j = 0; j < n; ++j) {
                if (j == i) continue;
                for (int k = 0; k < n; ++k) {
                    if (k == i || k == j) continue;
                    if (digits[k] % 2 != 0) continue; // must be even
                    int num = digits[i] * 100 + digits[j] * 10 + digits[k];
                    uniq.insert(num);
                }
            }
        }
        return uniq.size();
    }
};
```

## Java

```java
class Solution {
    public int totalNumbers(int[] digits) {
        Set<Integer> unique = new HashSet<>();
        int n = digits.length;
        for (int i = 0; i < n; i++) {
            if (digits[i] == 0) continue; // leading zero not allowed
            for (int j = 0; j < n; j++) {
                if (j == i) continue;
                for (int k = 0; k < n; k++) {
                    if (k == i || k == j) continue;
                    if ((digits[k] & 1) == 1) continue; // last digit must be even
                    int num = digits[i] * 100 + digits[j] * 10 + digits[k];
                    unique.add(num);
                }
            }
        }
        return unique.size();
    }
}
```

## Python

```python
class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        from itertools import permutations
        unique_numbers = set()
        for a, b, c in permutations(digits, 3):
            if a == 0:
                continue
            if c % 2 != 0:
                continue
            unique_numbers.add(100 * a + 10 * b + c)
        return len(unique_numbers)
```

## Python3

```python
from typing import List
import itertools

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique_numbers = set()
        for a, b, c in itertools.permutations(digits, 3):
            if a == 0 or c % 2 != 0:
                continue
            unique_numbers.add(100 * a + 10 * b + c)
        return len(unique_numbers)
```

## C

```c
int totalNumbers(int* digits, int digitsSize) {
    int seen[1000] = {0};
    int count = 0;
    for (int i = 0; i < digitsSize; ++i) {
        if (digits[i] == 0) continue; // leading zero not allowed
        for (int j = 0; j < digitsSize; ++j) {
            if (j == i) continue;
            for (int k = 0; k < digitsSize; ++k) {
                if (k == i || k == j) continue;
                if (digits[k] % 2 != 0) continue; // must be even
                int num = digits[i] * 100 + digits[j] * 10 + digits[k];
                if (!seen[num]) {
                    seen[num] = 1;
                    ++count;
                }
            }
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int TotalNumbers(int[] digits) {
        var uniqueNumbers = new System.Collections.Generic.HashSet<int>();
        int n = digits.Length;
        for (int i = 0; i < n; i++) {
            if (digits[i] == 0) continue; // leading zero not allowed
            for (int j = 0; j < n; j++) {
                if (j == i) continue;
                for (int k = 0; k < n; k++) {
                    if (k == i || k == j) continue;
                    if ((digits[k] & 1) != 0) continue; // last digit must be even
                    int number = digits[i] * 100 + digits[j] * 10 + digits[k];
                    uniqueNumbers.Add(number);
                }
            }
        }
        return uniqueNumbers.Count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} digits
 * @return {number}
 */
var totalNumbers = function(digits) {
    const n = digits.length;
    const seen = new Set();
    for (let i = 0; i < n; ++i) {
        if (digits[i] === 0) continue; // leading zero not allowed
        for (let j = 0; j < n; ++j) {
            if (j === i) continue;
            for (let k = 0; k < n; ++k) {
                if (k === i || k === j) continue;
                const unit = digits[k];
                if (unit % 2 !== 0) continue; // must be even
                const num = digits[i] * 100 + digits[j] * 10 + unit;
                seen.add(num);
            }
        }
    }
    return seen.size;
};
```

## Typescript

```typescript
function totalNumbers(digits: number[]): number {
    const n = digits.length;
    const unique = new Set<number>();
    for (let i = 0; i < n; i++) {
        if (digits[i] === 0) continue; // leading zero not allowed
        for (let j = 0; j < n; j++) {
            if (j === i) continue;
            for (let k = 0; k < n; k++) {
                if (k === i || k === j) continue;
                const last = digits[k];
                if (last % 2 !== 0) continue; // must be even
                const num = digits[i] * 100 + digits[j] * 10 + last;
                unique.add(num);
            }
        }
    }
    return unique.size;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $digits
     * @return Integer
     */
    function totalNumbers($digits) {
        $n = count($digits);
        $unique = [];
        for ($i = 0; $i < $n; ++$i) {
            if ($digits[$i] == 0) continue; // leading zero not allowed
            for ($j = 0; $j < $n; ++$j) {
                if ($j == $i) continue;
                for ($k = 0; $k < $n; ++$k) {
                    if ($k == $i || $k == $j) continue;
                    if ($digits[$k] % 2 != 0) continue; // must be even
                    $num = $digits[$i] * 100 + $digits[$j] * 10 + $digits[$k];
                    $unique[$num] = true;
                }
            }
        }
        return count($unique);
    }
}
```

## Swift

```swift
class Solution {
    func totalNumbers(_ digits: [Int]) -> Int {
        var uniqueNumbers = Set<Int>()
        let n = digits.count
        for i in 0..<n {
            if digits[i] == 0 { continue } // leading zero not allowed
            for j in 0..<n where j != i {
                for k in 0..<n where k != i && k != j {
                    if digits[k] % 2 != 0 { continue } // must be even
                    let number = digits[i] * 100 + digits[j] * 10 + digits[k]
                    uniqueNumbers.insert(number)
                }
            }
        }
        return uniqueNumbers.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun totalNumbers(digits: IntArray): Int {
        val n = digits.size
        val unique = HashSet<Int>()
        for (i in 0 until n) {
            if (digits[i] == 0) continue  // leading zero not allowed
            for (j in 0 until n) {
                if (j == i) continue
                for (k in 0 until n) {
                    if (k == i || k == j) continue
                    if (digits[k] % 2 != 0) continue  // must be even
                    val number = digits[i] * 100 + digits[j] * 10 + digits[k]
                    unique.add(number)
                }
            }
        }
        return unique.size
    }
}
```

## Dart

```dart
class Solution {
  int totalNumbers(List<int> digits) {
    Set<int> uniqueNumbers = {};
    int n = digits.length;
    for (int i = 0; i < n; i++) {
      if (digits[i] == 0) continue; // leading zero not allowed
      for (int j = 0; j < n; j++) {
        if (j == i) continue;
        for (int k = 0; k < n; k++) {
          if (k == i || k == j) continue;
          if (digits[k] % 2 != 0) continue; // must be even
          int number = digits[i] * 100 + digits[j] * 10 + digits[k];
          uniqueNumbers.add(number);
        }
      }
    }
    return uniqueNumbers.length;
  }
}
```

## Golang

```go
func totalNumbers(digits []int) int {
	n := len(digits)
	seen := make(map[int]struct{})
	for i := 0; i < n; i++ {
		if digits[i] == 0 {
			continue
		}
		for j := 0; j < n; j++ {
			if j == i {
				continue
			}
			for k := 0; k < n; k++ {
				if k == i || k == j {
					continue
				}
				if digits[k]%2 != 0 {
					continue
				}
				num := digits[i]*100 + digits[j]*10 + digits[k]
				seen[num] = struct{}{}
			}
		}
	}
	return len(seen)
}
```

## Ruby

```ruby
def total_numbers(digits)
  n = digits.length
  seen = {}
  (0...n).each do |i|
    next if digits[i] == 0
    (0...n).each do |j|
      next if j == i
      (0...n).each do |k|
        next if k == i || k == j
        next unless digits[k].even?
        num = digits[i] * 100 + digits[j] * 10 + digits[k]
        seen[num] = true
      end
    end
  end
  seen.size
end
```

## Scala

```scala
object Solution {
    def totalNumbers(digits: Array[Int]): Int = {
        val n = digits.length
        val unique = scala.collection.mutable.HashSet[Int]()
        for (i <- 0 until n) {
            if (digits(i) != 0) { // leading digit cannot be zero
                for (j <- 0 until n if j != i) {
                    for (k <- 0 until n if k != i && k != j) {
                        if (digits(k) % 2 == 0) { // last digit must be even
                            val num = digits(i) * 100 + digits(j) * 10 + digits(k)
                            unique += num
                        }
                    }
                }
            }
        }
        unique.size
    }
}
```

## Rust

```rust
impl Solution {
    pub fn total_numbers(digits: Vec<i32>) -> i32 {
        use std::collections::HashSet;
        let n = digits.len();
        let mut uniq = HashSet::new();

        for i in 0..n {
            if digits[i] == 0 { continue; } // leading zero not allowed
            for j in 0..n {
                if j == i { continue; }
                for k in 0..n {
                    if k == i || k == j { continue; }
                    let last = digits[k];
                    if last % 2 != 0 { continue; } // must be even
                    let num = digits[i] * 100 + digits[j] * 10 + last;
                    uniq.insert(num);
                }
            }
        }

        uniq.len() as i32
    }
}
```

## Racket

```racket
(define/contract (total-numbers digits)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length digits))
         (vec (list->vector digits))
         (hs (make-hash)))
    (for ([i (in-range n)])
      (for ([j (in-range n)])
        (when (not (= i j))
          (for ([k (in-range n)])
            (when (and (not (= k i)) (not (= k j)))
              (let* ((d1 (vector-ref vec i))
                     (d2 (vector-ref vec j))
                     (d3 (vector-ref vec k))
                     (num (+ (* 100 d1) (* 10 d2) d3)))
                (when (and (not (= d1 0)) (even? d3))
                  (hash-set! hs num #t))))))))
    (hash-count hs)))
```

## Erlang

```erlang
-module(solution).
-export([total_numbers/1]).

-spec total_numbers(Digits :: [integer()]) -> integer().
total_numbers(Digits) ->
    Numbers = gen_numbers(Digits),
    length(lists:usort(Numbers)).

gen_numbers(Digits) ->
    [X*100 + Y*10 + Z ||
        {X, Rest1} <- pick_one(Digits),
        X =/= 0,
        {Y, Rest2} <- pick_one(Rest1),
        {Z, _Rest3} <- pick_one(Rest2),
        Z rem 2 == 0].

pick_one([]) -> [];
pick_one([H|T]) ->
    [{H,T}] ++
    [ {E, [H|R]} || {E,R} <- pick_one(T) ].
```

## Elixir

```elixir
defmodule Solution do
  @spec total_numbers(digits :: [integer]) :: integer
  def total_numbers(digits) do
    n = length(digits)
    idxs = Enum.to_list(0..(n - 1))

    idxs
    |> for(i <- &1, j <- &1, k <- &1, i != j, j != k, i != k, do: {Enum.at(digits, i), Enum.at(digits, j), Enum.at(digits, k)})
    |> Enum.filter(fn {a, _b, c} -> a != 0 and rem(c, 2) == 0 end)
    |> Enum.map(fn {a, b, c} -> a * 100 + b * 10 + c end)
    |> MapSet.new()
    |> MapSet.size()
  end
end
```
