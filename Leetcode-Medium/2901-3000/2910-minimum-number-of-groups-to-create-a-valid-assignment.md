# 2910. Minimum Number of Groups to Create a Valid Assignment

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minGroupsForValidAssignment(vector<int>& balls) {
        unordered_map<int,int> cnt;
        for (int v : balls) ++cnt[v];
        int minFreq = INT_MAX;
        for (auto &p : cnt) minFreq = min(minFreq, p.second);
        int answer = balls.size(); // upper bound
        for (int x = 1; x <= minFreq; ++x) {
            long long total = 0;
            bool ok = true;
            int szSmall = x;
            int szLarge = x + 1;
            for (auto &p : cnt) {
                int f = p.second;
                int a = f / szLarge;
                int b = f % szLarge;
                if (b == 0) {
                    total += a;
                } else {
                    // need one group of size x to accommodate remainder
                    if (szSmall - b <= a) {
                        total += a + 1;
                    } else {
                        ok = false;
                        break;
                    }
                }
            }
            if (ok) answer = min<int>(answer, static_cast<int>(total));
        }
        return answer;
    }
};
```

## Java

```java
class Solution {
    public int minGroupsForValidAssignment(int[] balls) {
        java.util.HashMap<Integer, Integer> freq = new java.util.HashMap<>();
        for (int b : balls) {
            freq.merge(b, 1, Integer::sum);
        }
        int minFreq = Integer.MAX_VALUE;
        for (int f : freq.values()) {
            if (f < minFreq) minFreq = f;
        }
        int answer = Integer.MAX_VALUE;
        for (int x = 1; x <= minFreq; ++x) {
            long totalGroups = 0;
            boolean possible = true;
            for (int f : freq.values()) {
                int a = f / (x + 1);
                int b = f % (x + 1);
                if (b == 0) {
                    totalGroups += a;
                } else {
                    if (x - b <= a) {
                        totalGroups += a + 1;
                    } else {
                        possible = false;
                        break;
                    }
                }
            }
            if (possible && totalGroups < answer) {
                answer = (int) totalGroups;
            }
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def minGroupsForValidAssignment(self, balls):
        """
        :type balls: List[int]
        :rtype: int
        """
        from collections import Counter
        freq = list(Counter(balls).values())
        min_freq = min(freq)
        INF = 10**18
        answer = INF

        for x in range(1, min_freq + 1):
            total_groups = 0
            possible = True
            for f in freq:
                a = f // (x + 1)
                b = f % (x + 1)
                if b == 0:
                    groups = a
                elif x - b <= a:
                    groups = a + 1
                else:
                    possible = False
                    break
                total_groups += groups
            if possible and total_groups < answer:
                answer = total_groups

        return answer
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        freq = Counter(balls)
        min_freq = min(freq.values())
        INF = 10**9
        ans = INF
        for x in range(1, min_freq + 1):
            total_groups = 0
            possible = True
            for f in freq.values():
                a = f // (x + 1)
                b = f % (x + 1)
                if b == 0:
                    groups = a
                else:
                    if x - b <= a:
                        groups = a + 1
                    else:
                        possible = False
                        break
                total_groups += groups
            if possible and total_groups < ans:
                ans = total_groups
        return ans
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

int minGroupsForValidAssignment(int* balls, int ballsSize) {
    if (ballsSize == 0) return 0;

    qsort(balls, ballsSize, sizeof(int), cmp_int);

    // Collect frequencies of distinct numbers
    int *freq = (int *)malloc(ballsSize * sizeof(int));
    int distinct = 0;
    int curCnt = 1;
    for (int i = 1; i < ballsSize; ++i) {
        if (balls[i] == balls[i - 1]) {
            ++curCnt;
        } else {
            freq[distinct++] = curCnt;
            curCnt = 1;
        }
    }
    freq[distinct++] = curCnt;

    // Find minimum frequency among distinct numbers
    int minFreq = freq[0];
    for (int i = 1; i < distinct; ++i) {
        if (freq[i] < minFreq) minFreq = freq[i];
    }

    int answer = ballsSize; // upper bound

    for (int x = 1; x <= minFreq; ++x) {
        int totalGroups = 0;
        int feasible = 1;
        for (int i = 0; i < distinct; ++i) {
            int f = freq[i];
            int a = f / (x + 1);
            int b = f % (x + 1);
            int groups;
            if (b == 0) {
                groups = a;
            } else if (x - b <= a) {
                groups = a + 1;
            } else {
                feasible = 0;
                break;
            }
            totalGroups += groups;
        }
        if (feasible && totalGroups < answer) {
            answer = totalGroups;
        }
    }

    free(freq);
    return answer;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinGroupsForValidAssignment(int[] balls)
    {
        var freq = new Dictionary<int, int>();
        foreach (int b in balls)
        {
            if (!freq.ContainsKey(b))
                freq[b] = 0;
            freq[b]++;
        }

        int minFreq = int.MaxValue;
        foreach (var v in freq.Values)
            if (v < minFreq) minFreq = v;

        int answer = int.MaxValue;

        for (int x = 1; x <= minFreq; ++x)
        {
            int totalGroups = 0;
            bool possible = true;

            foreach (int f in freq.Values)
            {
                int a = f / (x + 1);
                int b = f % (x + 1);

                if (b == 0)
                {
                    totalGroups += a; // all groups of size x+1
                }
                else
                {
                    // need some groups of size x
                    if (x - b <= a)
                        totalGroups += a + 1;
                    else
                    {
                        possible = false;
                        break;
                    }
                }
            }

            if (possible && totalGroups < answer)
                answer = totalGroups;
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} balls
 * @return {number}
 */
var minGroupsForValidAssignment = function(balls) {
    const freqMap = new Map();
    for (const v of balls) {
        freqMap.set(v, (freqMap.get(v) || 0) + 1);
    }
    let minFreq = Infinity;
    for (const f of freqMap.values()) {
        if (f < minFreq) minFreq = f;
    }

    let answer = Infinity;

    for (let x = 1; x <= minFreq; ++x) {
        let totalGroups = 0;
        let possible = true;
        const groupSizeSmall = x;
        const groupSizeLarge = x + 1;

        for (const f of freqMap.values()) {
            const a = Math.floor(f / groupSizeLarge);
            const b = f % groupSizeLarge;
            if (b === 0) {
                totalGroups += a; // all groups size x+1
            } else {
                // need some groups of size x
                // condition derived: x - b <= a
                if (groupSizeSmall - b <= a) {
                    totalGroups += a + 1;
                } else {
                    possible = false;
                    break;
                }
            }
        }

        if (possible && totalGroups < answer) {
            answer = totalGroups;
        }
    }

    return answer;
};
```

## Typescript

```typescript
function minGroupsForValidAssignment(balls: number[]): number {
    const freq = new Map<number, number>();
    for (const b of balls) {
        freq.set(b, (freq.get(b) ?? 0) + 1);
    }

    let minFreq = Number.MAX_SAFE_INTEGER;
    for (const f of freq.values()) {
        if (f < minFreq) minFreq = f;
    }

    let answer = Number.MAX_SAFE_INTEGER;

    for (let x = 1; x <= minFreq; ++x) {
        const small = x;
        const large = x + 1;
        let total = 0;
        let possible = true;

        for (const f of freq.values()) {
            const a = Math.floor(f / large);
            const b = f % large;
            if (b === 0) {
                total += a;
            } else if ((small - b) <= a) {
                total += a + 1;
            } else {
                possible = false;
                break;
            }
        }

        if (possible && total < answer) {
            answer = total;
        }
    }

    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $balls
     * @return Integer
     */
    function minGroupsForValidAssignment($balls) {
        $freq = [];
        foreach ($balls as $v) {
            if (!isset($freq[$v])) {
                $freq[$v] = 0;
            }
            $freq[$v]++;
        }

        $minFreq = PHP_INT_MAX;
        foreach ($freq as $f) {
            if ($f < $minFreq) {
                $minFreq = $f;
            }
        }

        $ans = PHP_INT_MAX;

        for ($x = 1; $x <= $minFreq; $x++) {
            $total = 0;
            $ok = true;
            foreach ($freq as $f) {
                $a = intdiv($f, $x + 1);
                $b = $f % ($x + 1);
                if ($b == 0) {
                    $groups = $a;
                } else {
                    if ($x - $b <= $a) {
                        $groups = $a + 1;
                    } else {
                        $ok = false;
                        break;
                    }
                }
                $total += $groups;
            }
            if ($ok && $total < $ans) {
                $ans = $total;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minGroupsForValidAssignment(_ balls: [Int]) -> Int {
        var freq = [Int:Int]()
        for b in balls {
            freq[b, default: 0] += 1
        }
        guard let firstFreq = freq.values.first else { return 0 }
        var minFreq = firstFreq
        for v in freq.values where v < minFreq {
            minFreq = v
        }
        
        var answer = Int.max
        
        for x in 1...minFreq {
            var totalGroups = 0
            var possible = true
            for f in freq.values {
                let a = f / (x + 1)
                let b = f % (x + 1)
                if b == 0 {
                    totalGroups += a
                } else {
                    if x - b <= a {
                        totalGroups += a + 1
                    } else {
                        possible = false
                        break
                    }
                }
            }
            if possible && totalGroups < answer {
                answer = totalGroups
            }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minGroupsForValidAssignment(balls: IntArray): Int {
        val freq = HashMap<Int, Int>()
        for (b in balls) {
            freq[b] = (freq[b] ?: 0) + 1
        }
        var minFreq = Int.MAX_VALUE
        for (v in freq.values) {
            if (v < minFreq) minFreq = v
        }
        var answer = Int.MAX_VALUE
        for (x in 1..minFreq) {
            val div = x + 1
            var total = 0
            var ok = true
            for (f in freq.values) {
                val a = f / div
                val b = f % div
                if (b == 0) {
                    total += a
                } else {
                    if (x - b <= a) {
                        total += a + 1
                    } else {
                        ok = false
                        break
                    }
                }
            }
            if (ok && total < answer) answer = total
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int minGroupsForValidAssignment(List<int> balls) {
    // Count frequencies of each distinct number
    final Map<int, int> freq = {};
    for (var b in balls) {
      freq[b] = (freq[b] ?? 0) + 1;
    }
    final List<int> counts = freq.values.toList();
    if (counts.length == 1) return 1; // all balls are the same number

    int minFreq = counts.reduce((a, b) => a < b ? a : b);
    int answer = balls.length; // upper bound

    for (int x = 1; x <= minFreq; ++x) {
      bool feasible = true;
      int totalGroups = 0;

      for (var f in counts) {
        int a = f ~/ (x + 1); // groups of size x+1
        int b = f % (x + 1);   // remainder

        if (b == 0) {
          totalGroups += a;
        } else if (x - b <= a) {
          totalGroups += a + 1;
        } else {
          feasible = false;
          break;
        }
      }

      if (feasible && totalGroups < answer) {
        answer = totalGroups;
      }
    }

    return answer;
  }
}
```

## Golang

```go
func minGroupsForValidAssignment(balls []int) int {
	freq := make(map[int]int)
	for _, v := range balls {
		freq[v]++
	}
	minFreq := len(balls)
	for _, f := range freq {
		if f < minFreq {
			minFreq = f
		}
	}
	ans := len(balls)
	for x := 1; x <= minFreq; x++ {
		total, ok := 0, true
		for _, f := range freq {
			a := f / (x + 1)
			b := f % (x + 1)
			if b == 0 {
				total += a
			} else if x-b <= a {
				total += a + 1
			} else {
				ok = false
				break
			}
		}
		if ok && total < ans {
			ans = total
		}
	}
	return ans
}
```

## Ruby

```ruby
def min_groups_for_valid_assignment(balls)
  freq = Hash.new(0)
  balls.each { |b| freq[b] += 1 }
  min_f = freq.values.min
  ans = balls.size

  (1..min_f).each do |x|
    total = 0
    ok = true
    freq.each_value do |f|
      a = f / (x + 1)
      b = f % (x + 1)

      if b == 0
        groups = a
      else
        if x - b <= a
          groups = a + 1
        else
          ok = false
          break
        end
      end

      total += groups
    end
    ans = [ans, total].min if ok
  end

  ans
end
```

## Scala

```scala
object Solution {
  def minGroupsForValidAssignment(balls: Array[Int]): Int = {
    import scala.collection.mutable

    val freqMap = mutable.Map[Int, Int]()
    for (b <- balls) {
      freqMap.put(b, freqMap.getOrElse(b, 0) + 1)
    }

    var minFreq = Int.MaxValue
    for (f <- freqMap.values) {
      if (f < minFreq) minFreq = f
    }

    var answer = Int.MaxValue
    var x = 1
    while (x <= minFreq) {
      var total = 0
      var feasible = true
      val iter = freqMap.values.iterator
      while (iter.hasNext && feasible) {
        val f = iter.next()
        val a = f / (x + 1)
        val b = f % (x + 1)
        if (b == 0) {
          total += a
        } else {
          if (x - b <= a) {
            total += a + 1
          } else {
            feasible = false
          }
        }
      }
      if (feasible && total < answer) answer = total
      x += 1
    }

    answer
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn min_groups_for_valid_assignment(balls: Vec<i32>) -> i32 {
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for b in balls {
            *freq.entry(b).or_insert(0) += 1;
        }
        if freq.is_empty() {
            return 0;
        }

        // find minimum frequency among all numbers
        let min_freq = *freq.values().min().unwrap();

        let mut answer: i64 = i64::MAX;

        for x in 1..=min_freq {
            let mut total_groups: i64 = 0;
            let mut feasible = true;
            for &f in freq.values() {
                let a = f / (x + 1);
                let b = f % (x + 1);
                let groups = if b == 0 {
                    a
                } else if x - b <= a {
                    a + 1
                } else {
                    feasible = false;
                    break;
                };
                total_groups += groups as i64;
            }
            if feasible && total_groups < answer {
                answer = total_groups;
            }
        }

        answer as i32
    }
}
```

## Racket

```racket
(define/contract (min-groups-for-valid-assignment balls)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((freq (make-hash)))
    ;; build frequency map
    (for ([b balls])
      (hash-update! freq b (lambda (old) (+ old 1)) 0))
    (define freqs (hash-values freq))
    (define min-freq (apply min freqs))
    ;; helper: groups needed for a single frequency with given x, or #f if impossible
    (define (groups-needed f x)
      (let* ((den (+ x 1))
             (a (quotient f den))
             (b (remainder f den)))
        (cond [(= b 0) a]
              [(<= (- x b) a) (+ a 1)]
              [else #f])))
    ;; initial upper bound: put each ball in its own group
    (define best (+ 1 (apply + freqs)))
    (for ([x (in-range 1 (+ min-freq 1))])
      (let ((total 0)
            (ok #t))
        (for ([f freqs] #:break (not ok))
          (define g (groups-needed f x))
          (if g
              (set! total (+ total g))
              (set! ok #f)))
        (when ok
          (set! best (min best total)))))
    best))
```

## Erlang

```erlang
-module(solution).
-export([min_groups_for_valid_assignment/1]).

-spec min_groups_for_valid_assignment(Balls :: [integer()]) -> integer().
min_groups_for_valid_assignment(Balls) ->
    FreqMap = build_freq_map(Balls, #{}),
    Freqs = maps:values(FreqMap),
    MinFreq = lists:min(Freqs),
    InitialBest = length(Balls) + 1,
    find_min_groups(1, MinFreq, Freqs, InitialBest).

build_freq_map([], Map) -> Map;
build_freq_map([H|T], Map) ->
    Count = maps:get(H, Map, 0) + 1,
    build_freq_map(T, Map#{H => Count}).

find_min_groups(X, MaxX, _Freqs, Best) when X > MaxX ->
    Best;
find_min_groups(X, MaxX, Freqs, Best) ->
    case total_groups(Freqs, X) of
        {ok, Total} ->
            NewBest = if Total < Best -> Total; true -> Best end,
            find_min_groups(X + 1, MaxX, Freqs, NewBest);
        error ->
            find_min_groups(X + 1, MaxX, Freqs, Best)
    end.

total_groups(Freqs, X) ->
    {Status, Sum} = lists:foldl(
        fun(F, {ok, Acc}) ->
                A = F div (X + 1),
                B = F rem (X + 1),
                if
                    B == 0 ->
                        {ok, Acc + A};
                    X - B =< A ->
                        {ok, Acc + A + 1};
                    true ->
                        {error, undefined}
                end;
           (_, {error, _}) -> {error, undefined}
        end,
        {ok, 0},
        Freqs),
    case Status of
        ok -> {ok, Sum};
        error -> error
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_groups_for_valid_assignment(balls :: [integer]) :: integer
  def min_groups_for_valid_assignment(balls) do
    freq_map =
      Enum.reduce(balls, %{}, fn v, acc ->
        Map.update(acc, v, 1, &(&1 + 1))
      end)

    freqs = Map.values(freq_map)
    min_freq = Enum.min(freqs)
    n = length(balls)

    Enum.reduce(1..min_freq, n, fn x, best ->
      {feasible, total} =
        Enum.reduce_while(freqs, {true, 0}, fn f, {_ok, sum} ->
          a = div(f, x + 1)
          b = rem(f, x + 1)

          cond do
            b == 0 ->
              {:cont, {true, sum + a}}

            x - b <= a ->
              {:cont, {true, sum + a + 1}}

            true ->
              {:halt, {false, 0}}
          end
        end)

      if feasible and total < best, do: total, else: best
    end)
  end
end
```
