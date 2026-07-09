# 1399. Count Largest Group

## Cpp

```cpp
class Solution {
public:
    int countLargestGroup(int n) {
        unordered_map<int,int> cnt;
        int maxSize = 0;
        for (int i = 1; i <= n; ++i) {
            int x = i, sum = 0;
            while (x) {
                sum += x % 10;
                x /= 10;
            }
            int cur = ++cnt[sum];
            if (cur > maxSize) maxSize = cur;
        }
        int groups = 0;
        for (const auto& p : cnt) {
            if (p.second == maxSize) ++groups;
        }
        return groups;
    }
};
```

## Java

```java
class Solution {
    public int countLargestGroup(int n) {
        // Maximum possible digit sum for n <= 10000 is 9*5 = 45
        int[] freq = new int[46];
        for (int i = 1; i <= n; i++) {
            int s = digitSum(i);
            freq[s]++;
        }
        int max = 0;
        for (int c : freq) {
            if (c > max) max = c;
        }
        int groups = 0;
        for (int c : freq) {
            if (c == max && c != 0) groups++;
        }
        return groups;
    }

    private int digitSum(int x) {
        int sum = 0;
        while (x > 0) {
            sum += x % 10;
            x /= 10;
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        freq = {}
        for i in range(1, n + 1):
            s = 0
            x = i
            while x:
                s += x % 10
                x //= 10
            freq[s] = freq.get(s, 0) + 1

        max_size = max(freq.values())
        return sum(1 for v in freq.values() if v == max_size)
```

## Python3

```python
class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq = {}
        for i in range(1, n + 1):
            s = 0
            x = i
            while x:
                s += x % 10
                x //= 10
            freq[s] = freq.get(s, 0) + 1
        max_cnt = max(freq.values())
        return sum(1 for cnt in freq.values() if cnt == max_cnt)
```

## C

```c
int countLargestGroup(int n) {
    int freq[46] = {0}; // maximum digit sum for n <= 10000 is 45
    for (int i = 1; i <= n; ++i) {
        int x = i, s = 0;
        while (x) {
            s += x % 10;
            x /= 10;
        }
        freq[s]++;
    }
    int maxFreq = 0, groups = 0;
    for (int i = 0; i < 46; ++i) {
        if (freq[i] > maxFreq) {
            maxFreq = freq[i];
            groups = 1;
        } else if (freq[i] == maxFreq && maxFreq != 0) {
            groups++;
        }
    }
    return groups;
}
```

## Csharp

```csharp
public class Solution {
    public int CountLargestGroup(int n) {
        // Maximum possible digit sum for n <= 10000 is 9*5 = 45
        int[] freq = new int[46];
        for (int i = 1; i <= n; i++) {
            int sum = 0;
            int x = i;
            while (x > 0) {
                sum += x % 10;
                x /= 10;
            }
            freq[sum]++;
        }

        int maxSize = 0;
        for (int i = 0; i < freq.Length; i++) {
            if (freq[i] > maxSize) {
                maxSize = freq[i];
            }
        }

        int groups = 0;
        for (int i = 0; i < freq.Length; i++) {
            if (freq[i] == maxSize) {
                groups++;
            }
        }

        return groups;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countLargestGroup = function(n) {
    const counts = {};
    for (let i = 1; i <= n; ++i) {
        let x = i, sum = 0;
        while (x > 0) {
            sum += x % 10;
            x = Math.floor(x / 10);
        }
        counts[sum] = (counts[sum] || 0) + 1;
    }
    let maxSize = 0, groups = 0;
    for (const key in counts) {
        const sz = counts[key];
        if (sz > maxSize) {
            maxSize = sz;
            groups = 1;
        } else if (sz === maxSize) {
            ++groups;
        }
    }
    return groups;
};
```

## Typescript

```typescript
function countLargestGroup(n: number): number {
    const maxDigitSum = 9 * 5; // since n ≤ 10^4, at most 5 digits
    const counts = new Array(maxDigitSum + 1).fill(0);
    for (let i = 1; i <= n; i++) {
        let sum = 0;
        let x = i;
        while (x > 0) {
            sum += x % 10;
            x = Math.floor(x / 10);
        }
        counts[sum]++;
    }
    let maxSize = 0;
    for (const c of counts) {
        if (c > maxSize) maxSize = c;
    }
    let result = 0;
    for (const c of counts) {
        if (c === maxSize) result++;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countLargestGroup($n) {
        $freq = [];
        for ($i = 1; $i <= $n; $i++) {
            $sum = 0;
            $x = $i;
            while ($x > 0) {
                $sum += $x % 10;
                $x = intdiv($x, 10);
            }
            if (!isset($freq[$sum])) {
                $freq[$sum] = 0;
            }
            $freq[$sum]++;
        }

        $maxSize = max($freq);
        $count = 0;
        foreach ($freq as $size) {
            if ($size === $maxSize) {
                $count++;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countLargestGroup(_ n: Int) -> Int {
        var freq = [Int: Int]()
        for i in 1...n {
            var x = i
            var sum = 0
            while x > 0 {
                sum += x % 10
                x /= 10
            }
            freq[sum, default: 0] += 1
        }
        guard let maxSize = freq.values.max() else { return 0 }
        var result = 0
        for size in freq.values where size == maxSize {
            result += 1
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countLargestGroup(n: Int): Int {
        // Maximum possible digit sum for n <= 10000 is less than 100
        val freq = IntArray(100)
        for (i in 1..n) {
            var x = i
            var sum = 0
            while (x > 0) {
                sum += x % 10
                x /= 10
            }
            freq[sum]++
        }
        var maxSize = 0
        for (c in freq) {
            if (c > maxSize) maxSize = c
        }
        var groups = 0
        for (c in freq) {
            if (c == maxSize) groups++
        }
        return groups
    }
}
```

## Dart

```dart
class Solution {
  int countLargestGroup(int n) {
    final Map<int, int> freq = {};
    int maxSize = 0;
    for (int i = 1; i <= n; i++) {
      int sum = 0;
      int x = i;
      while (x > 0) {
        sum += x % 10;
        x ~/= 10;
      }
      freq[sum] = (freq[sum] ?? 0) + 1;
      if (freq[sum]! > maxSize) {
        maxSize = freq[sum]!;
      }
    }
    int groups = 0;
    for (final count in freq.values) {
      if (count == maxSize) groups++;
    }
    return groups;
  }
}
```

## Golang

```go
func countLargestGroup(n int) int {
	cnt := make([]int, 100)
	maxCnt := 0
	for i := 1; i <= n; i++ {
		s := digitSum(i)
		cnt[s]++
		if cnt[s] > maxCnt {
			maxCnt = cnt[s]
		}
	}
	res := 0
	for _, c := range cnt {
		if c == maxCnt && c > 0 {
			res++
		}
	}
	return res
}

func digitSum(x int) int {
	sum := 0
	for x > 0 {
		sum += x % 10
		x /= 10
	}
	return sum
}
```

## Ruby

```ruby
def count_largest_group(n)
  freq = Hash.new(0)
  (1..n).each do |i|
    sum = 0
    x = i
    while x > 0
      sum += x % 10
      x /= 10
    end
    freq[sum] += 1
  end
  max_size = freq.values.max || 0
  freq.values.count { |v| v == max_size }
end
```

## Scala

```scala
object Solution {
    def countLargestGroup(n: Int): Int = {
        val freq = scala.collection.mutable.Map[Int, Int]()
        var i = 1
        while (i <= n) {
            var x = i
            var sum = 0
            while (x > 0) {
                sum += x % 10
                x /= 10
            }
            freq(sum) = freq.getOrElse(sum, 0) + 1
            i += 1
        }
        val maxSize = freq.values.max
        freq.count(_._2 == maxSize)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_largest_group(n: i32) -> i32 {
        let n_usize = n as usize;
        // Maximum digit sum for n <= 10^4 is 36, allocate a safe size.
        let mut freq = vec![0usize; 100];
        for i in 1..=n_usize {
            let mut x = i as i32;
            let mut s = 0i32;
            while x > 0 {
                s += x % 10;
                x /= 10;
            }
            freq[s as usize] += 1;
        }
        let max_cnt = *freq.iter().max().unwrap_or(&0);
        let mut ans = 0i32;
        for &c in &freq {
            if c == max_cnt && c > 0 {
                ans += 1;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define (digit-sum x)
  (let loop ((y x) (s 0))
    (if (= y 0)
        s
        (loop (quotient y 10) (+ s (remainder y 10))))))

(define/contract (count-largest-group n)
  (-> exact-integer? exact-integer?)
  (let ((counts (make-hash))
        (max-count 0))
    (for ([i (in-range 1 (add1 n))])
      (let* ((sum (digit-sum i))
             (cur (+ 1 (hash-ref counts sum 0))))
        (hash-set! counts sum cur)
        (when (> cur max-count)
          (set! max-count cur))))
    (let ((result 0))
      (for ([kv (in-hash counts)])
        (when (= (cdr kv) max-count)
          (set! result (+ result 1))))
      result)))
```

## Erlang

```erlang
-module(solution).
-export([count_largest_group/1]).

-spec count_largest_group(N :: integer()) -> integer().
count_largest_group(N) ->
    Counts = lists:foldl(
        fun(I, Acc) ->
            Sum = digit_sum(I),
            maps:update_with(Sum, fun(C) -> C + 1 end, 1, Acc)
        end,
        #{},
        lists:seq(1, N)
    ),
    MaxCount = maps:fold(
        fun(_Key, Val, Max) ->
            if Val > Max -> Val; true -> Max end
        end,
        0,
        Counts
    ),
    maps:fold(
        fun(_Key, Val, Acc) ->
            if Val == MaxCount -> Acc + 1; true -> Acc end
        end,
        0,
        Counts
    ).

digit_sum(0) -> 0;
digit_sum(X) when X > 0 ->
    digit_sum(X div 10) + (X rem 10).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_largest_group(n :: integer) :: integer
  def count_largest_group(n) do
    freq =
      1..n
      |> Enum.reduce(%{}, fn i, acc ->
        sum = digit_sum(i)
        Map.update(acc, sum, 1, &(&1 + 1))
      end)

    max = freq |> Map.values() |> Enum.max()
    freq |> Map.values() |> Enum.count(fn v -> v == max end)
  end

  defp digit_sum(x) do
    Integer.digits(x) |> Enum.sum()
  end
end
```
