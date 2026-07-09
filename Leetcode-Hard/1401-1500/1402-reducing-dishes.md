# 1402. Reducing Dishes

## Cpp

```cpp
class Solution {
public:
    int maxSatisfaction(vector<int>& satisfaction) {
        sort(satisfaction.begin(), satisfaction.end());
        long long best = 0, cur = 0, sum = 0;
        for (int i = (int)satisfaction.size() - 1; i >= 0; --i) {
            sum += satisfaction[i];
            cur += sum;
            if (cur > best) best = cur;
        }
        return (int)best;
    }
};
```

## Java

```java
class Solution {
    public int maxSatisfaction(int[] satisfaction) {
        java.util.Arrays.sort(satisfaction);
        long total = 0;
        long suffixSum = 0;
        for (int i = satisfaction.length - 1; i >= 0; --i) {
            suffixSum += satisfaction[i];
            if (suffixSum > 0) {
                total += suffixSum;
            } else {
                break;
            }
        }
        return (int) total;
    }
}
```

## Python

```python
class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        satisfaction.sort()
        total = 0
        suffix_sum = 0
        for s in reversed(satisfaction):
            suffix_sum += s
            if suffix_sum > 0:
                total += suffix_sum
        return total
```

## Python3

```python
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        cur = 0
        ans = 0
        for s in satisfaction:
            if cur + s > 0:
                cur += s
                ans += cur
            else:
                break
        return ans
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

int maxSatisfaction(int* satisfaction, int satisfactionSize) {
    if (satisfactionSize == 0) return 0;
    qsort(satisfaction, (size_t)satisfactionSize, sizeof(int), cmp_int);
    
    long long total = 0;
    long long prefix = 0;
    for (int i = satisfactionSize - 1; i >= 0; --i) {
        prefix += satisfaction[i];
        if (prefix > 0) {
            total += prefix;
        } else {
            break;
        }
    }
    return (int)total;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxSatisfaction(int[] satisfaction) {
        Array.Sort(satisfaction);
        long cur = 0, sum = 0, ans = 0;
        for (int i = satisfaction.Length - 1; i >= 0; --i) {
            sum += satisfaction[i];
            if (sum > 0) {
                cur += sum;
                if (cur > ans) ans = cur;
            } else {
                break;
            }
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} satisfaction
 * @return {number}
 */
var maxSatisfaction = function(satisfaction) {
    satisfaction.sort((a, b) => a - b);
    let total = 0;
    let suffixSum = 0;
    for (let i = satisfaction.length - 1; i >= 0; i--) {
        suffixSum += satisfaction[i];
        if (suffixSum > 0) {
            total += suffixSum;
        } else {
            break;
        }
    }
    return total;
};
```

## Typescript

```typescript
function maxSatisfaction(satisfaction: number[]): number {
    satisfaction.sort((a, b) => a - b);
    let total = 0;
    let prefixSum = 0;
    for (let i = satisfaction.length - 1; i >= 0; i--) {
        prefixSum += satisfaction[i];
        if (prefixSum > 0) {
            total += prefixSum;
        } else {
            break;
        }
    }
    return total;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $satisfaction
     * @return Integer
     */
    function maxSatisfaction($satisfaction) {
        sort($satisfaction);
        $n = count($satisfaction);
        $total = 0;
        $curSum = 0;
        $ans = 0;
        for ($i = $n - 1; $i >= 0; --$i) {
            $curSum += $satisfaction[$i];
            $total += $curSum;
            if ($total > $ans) {
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
    func maxSatisfaction(_ satisfaction: [Int]) -> Int {
        let sorted = satisfaction.sorted()
        var result = 0
        var suffixSum = 0
        for i in stride(from: sorted.count - 1, through: 0, by: -1) {
            suffixSum += sorted[i]
            if suffixSum > 0 {
                result += suffixSum
            } else {
                break
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSatisfaction(satisfaction: IntArray): Int {
        satisfaction.sort()
        var total = 0L
        var suffixSum = 0L
        for (i in satisfaction.lastIndex downTo 0) {
            suffixSum += satisfaction[i]
            if (suffixSum > 0) {
                total += suffixSum
            } else {
                break
            }
        }
        return total.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maxSatisfaction(List<int> satisfaction) {
    satisfaction.sort();
    int total = 0;
    int cur = 0;
    for (int i = satisfaction.length - 1; i >= 0; --i) {
      cur += satisfaction[i];
      if (cur > 0) {
        total += cur;
      } else {
        break;
      }
    }
    return total;
  }
}
```

## Golang

```go
package main

import "sort"

func maxSatisfaction(satisfaction []int) int {
	sort.Ints(satisfaction)
	total, cur := 0, 0
	for i := len(satisfaction) - 1; i >= 0; i-- {
		cur += satisfaction[i]
		if cur > 0 {
			total += cur
		} else {
			break
		}
	}
	return total
}
```

## Ruby

```ruby
def max_satisfaction(satisfaction)
  satisfaction.sort!
  total = 0
  cur_sum = 0
  (satisfaction.length - 1).downto(0) do |i|
    cur_sum += satisfaction[i]
    break if cur_sum <= 0
    total += cur_sum
  end
  total
end
```

## Scala

```scala
object Solution {
  def maxSatisfaction(satisfaction: Array[Int]): Int = {
    val sorted = satisfaction.sorted
    var curSum: Long = 0L
    var result: Long = 0L
    var i = sorted.length - 1
    while (i >= 0) {
      curSum += sorted(i)
      if (curSum > 0) {
        result += curSum
        i -= 1
      } else {
        return result.toInt
      }
    }
    result.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_satisfaction(mut satisfaction: Vec<i32>) -> i32 {
        satisfaction.sort();
        let mut total: i64 = 0;
        let mut cur: i64 = 0;
        for &s in satisfaction.iter().rev() {
            cur += s as i64;
            if cur > 0 {
                total += cur;
            } else {
                break;
            }
        }
        total as i32
    }
}
```

## Racket

```racket
(define/contract (max-satisfaction satisfaction)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([sorted (sort satisfaction <)]
         [len (length sorted)])
    (let loop ((i (- len 1)) (cur 0) (ans 0))
      (if (< i 0)
          ans
          (let* ([v (list-ref sorted i)]
                 [new-cur (+ cur v)])
            (if (> new-cur 0)
                (loop (- i 1) new-cur (+ ans new-cur))
                ans))))))
```

## Erlang

```erlang
-spec max_satisfaction(Satisfaction :: [integer()]) -> integer().
max_satisfaction(Satisfaction) ->
    Sorted = lists:sort(Satisfaction),
    RevSorted = lists:reverse(Sorted),
    max_satisfaction_loop(RevSorted, 0, 0).

max_satisfaction_loop([], _Cur, Ans) ->
    Ans;
max_satisfaction_loop([H|T], Cur, Ans) ->
    NewCur = Cur + H,
    if
        NewCur > 0 ->
            max_satisfaction_loop(T, NewCur, Ans + NewCur);
        true ->
            Ans
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_satisfaction(satisfaction :: [integer]) :: integer
  def max_satisfaction(satisfaction) do
    satisfaction
    |> Enum.sort(:desc)
    |> Enum.reduce_while({0, 0}, fn s, {sum, res} ->
      if sum + s > 0 do
        new_sum = sum + s
        {:cont, {new_sum, res + new_sum}}
      else
        {:halt, {sum, res}}
      end
    end)
    |> elem(1)
  end
end
```
