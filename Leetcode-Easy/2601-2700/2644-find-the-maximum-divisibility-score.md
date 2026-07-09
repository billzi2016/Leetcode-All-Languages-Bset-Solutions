# 2644. Find the Maximum Divisibility Score

## Cpp

```cpp
class Solution {
public:
    int maxDivScore(vector<int>& nums, vector<int>& divisors) {
        int bestCnt = -1;
        int bestDiv = 0;
        for (int d : divisors) {
            int cnt = 0;
            for (int x : nums) {
                if (x % d == 0) ++cnt;
            }
            if (cnt > bestCnt || (cnt == bestCnt && d < bestDiv)) {
                bestCnt = cnt;
                bestDiv = d;
            }
        }
        return bestDiv;
    }
};
```

## Java

```java
class Solution {
    public int maxDivScore(int[] nums, int[] divisors) {
        int bestDiv = Integer.MAX_VALUE;
        int bestCount = -1;
        for (int d : divisors) {
            int cnt = 0;
            for (int n : nums) {
                if (n % d == 0) {
                    cnt++;
                }
            }
            if (cnt > bestCount || (cnt == bestCount && d < bestDiv)) {
                bestCount = cnt;
                bestDiv = d;
            }
        }
        return bestDiv;
    }
}
```

## Python

```python
class Solution(object):
    def maxDivScore(self, nums, divisors):
        """
        :type nums: List[int]
        :type divisors: List[int]
        :rtype: int
        """
        best_score = -1
        best_divisor = None
        for d in divisors:
            cnt = 0
            for n in nums:
                if n % d == 0:
                    cnt += 1
            if cnt > best_score or (cnt == best_score and (best_divisor is None or d < best_divisor)):
                best_score = cnt
                best_divisor = d
        return best_divisor
```

## Python3

```python
from typing import List

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        best_score = -1
        answer = 0
        for d in divisors:
            cnt = 0
            for x in nums:
                if x % d == 0:
                    cnt += 1
            if cnt > best_score or (cnt == best_score and d < answer):
                best_score = cnt
                answer = d
        return answer
```

## C

```c
int maxDivScore(int* nums, int numsSize, int* divisors, int divisorsSize) {
    int bestDiv = 0;
    int bestCount = -1;
    for (int i = 0; i < divisorsSize; ++i) {
        int d = divisors[i];
        int cnt = 0;
        for (int j = 0; j < numsSize; ++j) {
            if (nums[j] % d == 0) {
                ++cnt;
            }
        }
        if (cnt > bestCount || (cnt == bestCount && d < bestDiv)) {
            bestCount = cnt;
            bestDiv = d;
        }
    }
    return bestDiv;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxDivScore(int[] nums, int[] divisors) {
        int bestScore = -1;
        int bestDivisor = int.MaxValue;
        foreach (int d in divisors) {
            int cnt = 0;
            foreach (int n in nums) {
                if (n % d == 0) cnt++;
            }
            if (cnt > bestScore || (cnt == bestScore && d < bestDivisor)) {
                bestScore = cnt;
                bestDivisor = d;
            }
        }
        return bestDivisor;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} divisors
 * @return {number}
 */
var maxDivScore = function(nums, divisors) {
    let bestCount = -1;
    let bestDiv = Infinity;
    
    for (let d of divisors) {
        let cnt = 0;
        for (let n of nums) {
            if (n % d === 0) cnt++;
        }
        if (cnt > bestCount || (cnt === bestCount && d < bestDiv)) {
            bestCount = cnt;
            bestDiv = d;
        }
    }
    
    return bestDiv;
};
```

## Typescript

```typescript
function maxDivScore(nums: number[], divisors: number[]): number {
    let bestDiv = Number.MAX_SAFE_INTEGER;
    let bestCount = -1;
    for (const d of divisors) {
        let cnt = 0;
        for (const n of nums) {
            if (n % d === 0) cnt++;
        }
        if (cnt > bestCount || (cnt === bestCount && d < bestDiv)) {
            bestCount = cnt;
            bestDiv = d;
        }
    }
    return bestDiv;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $divisors
     * @return Integer
     */
    function maxDivScore($nums, $divisors) {
        $bestScore = -1;
        $answer = PHP_INT_MAX;

        foreach ($divisors as $d) {
            $cnt = 0;
            foreach ($nums as $n) {
                if ($n % $d === 0) {
                    $cnt++;
                }
            }

            if ($cnt > $bestScore || ($cnt == $bestScore && $d < $answer)) {
                $bestScore = $cnt;
                $answer = $d;
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func maxDivScore(_ nums: [Int], _ divisors: [Int]) -> Int {
        var bestScore = -1
        var bestDiv = Int.max
        for d in divisors {
            var count = 0
            for n in nums {
                if n % d == 0 {
                    count += 1
                }
            }
            if count > bestScore || (count == bestScore && d < bestDiv) {
                bestScore = count
                bestDiv = d
            }
        }
        return bestDiv
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxDivScore(nums: IntArray, divisors: IntArray): Int {
        var bestScore = -1
        var answer = Int.MAX_VALUE
        for (d in divisors) {
            var cnt = 0
            for (n in nums) {
                if (n % d == 0) cnt++
            }
            if (cnt > bestScore || (cnt == bestScore && d < answer)) {
                bestScore = cnt
                answer = d
            }
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maxDivScore(List<int> nums, List<int> divisors) {
    int bestDiv = divisors[0];
    int bestCount = -1;
    for (int d in divisors) {
      int cnt = 0;
      for (int n in nums) {
        if (n % d == 0) cnt++;
      }
      if (cnt > bestCount || (cnt == bestCount && d < bestDiv)) {
        bestCount = cnt;
        bestDiv = d;
      }
    }
    return bestDiv;
  }
}
```

## Golang

```go
func maxDivScore(nums []int, divisors []int) int {
	bestCount := -1
	ans := 0
	for _, d := range divisors {
		cnt := 0
		for _, n := range nums {
			if n%d == 0 {
				cnt++
			}
		}
		if cnt > bestCount || (cnt == bestCount && d < ans) {
			bestCount = cnt
			ans = d
		}
	}
	return ans
}
```

## Ruby

```ruby
def max_div_score(nums, divisors)
  best_div = nil
  best_cnt = -1
  divisors.each do |d|
    cnt = 0
    nums.each { |n| cnt += 1 if n % d == 0 }
    if cnt > best_cnt || (cnt == best_cnt && (best_div.nil? || d < best_div))
      best_cnt = cnt
      best_div = d
    end
  end
  best_div
end
```

## Scala

```scala
object Solution {
    def maxDivScore(nums: Array[Int], divisors: Array[Int]): Int = {
        var bestDiv = Int.MaxValue
        var bestCount = -1
        for (d <- divisors) {
            var cnt = 0
            var i = 0
            while (i < nums.length) {
                if (nums(i) % d == 0) cnt += 1
                i += 1
            }
            if (cnt > bestCount || (cnt == bestCount && d < bestDiv)) {
                bestCount = cnt
                bestDiv = d
            }
        }
        bestDiv
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_div_score(nums: Vec<i32>, divisors: Vec<i32>) -> i32 {
        let mut best_div = 0;
        let mut best_cnt = -1i32;
        for &d in &divisors {
            let mut cnt = 0;
            for &n in &nums {
                if n % d == 0 {
                    cnt += 1;
                }
            }
            if cnt > best_cnt || (cnt == best_cnt && d < best_div) {
                best_cnt = cnt;
                best_div = d;
            }
        }
        best_div
    }
}
```

## Racket

```racket
(define/contract (max-div-score nums divisors)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((first (car divisors))
         (first-count
          (let count-loop ((ns nums) (c 0))
            (if (null? ns)
                c
                (count-loop (cdr ns)
                            (+ c (if (= (remainder (car ns) first) 0) 1 0))))))
         (init-best-div first)
         (init-best-count first-count))
    (let loop ((ds (cdr divisors)) (best-div init-best-div) (best-count init-best-count))
      (if (null? ds)
          best-div
          (let* ((d (car ds))
                 (cnt
                  (let count-loop ((ns nums) (c 0))
                    (if (null? ns)
                        c
                        (count-loop (cdr ns)
                                    (+ c (if (= (remainder (car ns) d) 0) 1 0))))))
                 (new-best?
                  (or (> cnt best-count)
                      (and (= cnt best-count) (< d best-div)))))
            (loop (cdr ds)
                  (if new-best? d best-div)
                  (if new-best? cnt best-count)))))))
```

## Erlang

```erlang
-module(solution).
-export([max_div_score/2]).

-spec max_div_score(Nums :: [integer()], Divisors :: [integer()]) -> integer().
max_div_score(Nums, Divisors) ->
    case Divisors of
        [] -> 0;
        [First|Rest] ->
            InitialScore = count_divisible(Nums, First),
            {BestDiv, _} = lists:foldl(
                fun(D, {CurDiv, CurScore}) ->
                    Score = count_divisible(Nums, D),
                    case {Score > CurScore, Score == CurScore andalso D < CurDiv} of
                        {true, _} -> {D, Score};
                        {false, true} -> {D, Score};
                        _ -> {CurDiv, CurScore}
                    end
                end,
                {First, InitialScore},
                Rest),
            BestDiv
    end.

count_divisible(Nums, D) ->
    count_divisible(Nums, D, 0).

count_divisible([], _, Acc) -> Acc;
count_divisible([H|T], D, Acc) ->
    NewAcc = if H rem D =:= 0 -> Acc + 1; true -> Acc end,
    count_divisible(T, D, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_div_score(nums :: [integer], divisors :: [integer]) :: integer
  def max_div_score(nums, divisors) do
    {best_divisor, _} =
      Enum.reduce(divisors, {nil, -1}, fn d, {cur_best, cur_max} ->
        count = Enum.count(nums, fn n -> rem(n, d) == 0 end)

        cond do
          count > cur_max ->
            {d, count}

          count == cur_max and (cur_best == nil or d < cur_best) ->
            {d, count}

          true ->
            {cur_best, cur_max}
        end
      end)

    best_divisor
  end
end
```
