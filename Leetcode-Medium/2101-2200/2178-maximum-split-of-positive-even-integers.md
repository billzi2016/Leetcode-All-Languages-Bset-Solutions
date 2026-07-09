# 2178. Maximum Split of Positive Even Integers

## Cpp

```cpp
class Solution {
public:
    vector<long long> maximumEvenSplit(long long finalSum) {
        if (finalSum % 2 != 0) return {};
        vector<long long> res;
        for (long long cur = 2; finalSum >= cur; cur += 2) {
            res.push_back(cur);
            finalSum -= cur;
        }
        if (!res.empty() && finalSum > 0) {
            res.back() += finalSum;
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public java.util.List<Long> maximumEvenSplit(long finalSum) {
        java.util.List<Long> result = new java.util.ArrayList<>();
        if ((finalSum & 1L) == 1L) {
            return result;
        }
        long cur = 2;
        while (finalSum - cur > cur) {
            result.add(cur);
            finalSum -= cur;
            cur += 2;
        }
        if (finalSum > 0) {
            result.add(finalSum);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def maximumEvenSplit(self, finalSum):
        """
        :type finalSum: int
        :rtype: List[int]
        """
        if finalSum % 2 == 1:
            return []
        res = []
        cur = 2
        while finalSum - cur > cur:
            res.append(cur)
            finalSum -= cur
            cur += 2
        if finalSum > 0:
            res.append(finalSum)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        res = []
        cur = 2
        while finalSum - cur > cur:
            res.append(cur)
            finalSum -= cur
            cur += 2
        res.append(finalSum)
        return res
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* maximumEvenSplit(long long finalSum, int* returnSize) {
    if (finalSum % 2 != 0) {
        *returnSize = 0;
        return NULL;
    }
    
    long long sum = finalSum;
    long long cur = 2;
    int cnt = 0;
    while (sum - cur > cur) {
        sum -= cur;
        cur += 2;
        ++cnt;
    }
    
    *returnSize = cnt + 1;               // include the last remaining number
    long long* res = (long long*)malloc(sizeof(long long) * (*returnSize));
    if (!res) {
        *returnSize = 0;
        return NULL;
    }
    
    sum = finalSum;
    cur = 2;
    int idx = 0;
    while (sum - cur > cur) {
        res[idx++] = cur;
        sum -= cur;
        cur += 2;
    }
    res[idx] = sum;                       // the final element
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<long> MaximumEvenSplit(long finalSum)
    {
        var result = new List<long>();
        if ((finalSum & 1) == 1) return result; // odd sum cannot be split into even numbers

        long cur = 2;
        while (finalSum > 0)
        {
            if (finalSum - cur > cur)
            {
                result.Add(cur);
                finalSum -= cur;
                cur += 2;
            }
            else
            {
                // Add the remaining sum as the last element
                result.Add(finalSum);
                break;
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} finalSum
 * @return {number[]}
 */
var maximumEvenSplit = function(finalSum) {
    if (finalSum % 2 !== 0) return [];
    const res = [];
    let cur = 2;
    while (finalSum > 0) {
        // If we can still take the current even number and leave a larger remainder
        if (finalSum - cur > cur) {
            res.push(cur);
            finalSum -= cur;
            cur += 2;
        } else {
            // Take all remaining sum as the last element
            res.push(finalSum);
            break;
        }
    }
    return res;
};
```

## Typescript

```typescript
function maximumEvenSplit(finalSum: number): number[] {
    if (finalSum % 2 !== 0) return [];
    const result: number[] = [];
    let cur = 2;
    while (finalSum - cur > cur) {
        result.push(cur);
        finalSum -= cur;
        cur += 2;
    }
    if (finalSum > 0) result.push(finalSum);
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $finalSum
     * @return Integer[]
     */
    function maximumEvenSplit($finalSum) {
        if ($finalSum % 2 != 0) {
            return [];
        }
        $result = [];
        $curr = 2;
        while ($finalSum - $curr > $curr) {
            $result[] = $curr;
            $finalSum -= $curr;
            $curr += 2;
        }
        $result[] = $finalSum;
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func maximumEvenSplit(_ finalSum: Int) -> [Int] {
        if finalSum % 2 != 0 { return [] }
        var result = [Int]()
        var cur = 2
        var remaining = finalSum
        while remaining - cur > cur {
            result.append(cur)
            remaining -= cur
            cur += 2
        }
        result.append(remaining)
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumEvenSplit(finalSum: Long): List<Long> {
        if (finalSum % 2L != 0L) return emptyList()
        var sum = finalSum
        val result = mutableListOf<Long>()
        var cur = 2L
        while (sum > cur) {
            if (sum - cur <= cur) break
            result.add(cur)
            sum -= cur
            cur += 2
        }
        if (sum > 0) {
            result.add(sum)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> maximumEvenSplit(int finalSum) {
    if (finalSum % 2 == 1) return [];
    List<int> res = [];
    int cur = 2;
    while (true) {
      if (finalSum - cur > cur) {
        res.add(cur);
        finalSum -= cur;
        cur += 2;
      } else {
        res.add(finalSum);
        break;
      }
    }
    return res;
  }
}
```

## Golang

```go
func maximumEvenSplit(finalSum int64) []int64 {
	if finalSum%2 == 1 {
		return []int64{}
	}
	var res []int64
	for i := int64(2); finalSum-i > i; i += 2 {
		res = append(res, i)
		finalSum -= i
	}
	if finalSum > 0 {
		res = append(res, finalSum)
	}
	return res
}
```

## Ruby

```ruby
def maximum_even_split(final_sum)
  return [] if final_sum.odd?
  result = []
  cur = 2
  while final_sum > 0
    if final_sum - cur > cur
      result << cur
      final_sum -= cur
      cur += 2
    else
      result << final_sum
      break
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def maximumEvenSplit(finalSum: Long): List[Long] = {
        if (finalSum % 2 != 0) return Nil
        var remaining = finalSum
        val result = scala.collection.mutable.ListBuffer[Long]()
        var cur = 2L
        while (remaining > 2 * cur) {
            result += cur
            remaining -= cur
            cur += 2
        }
        if (remaining > 0) result += remaining
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_even_split(final_sum: i64) -> Vec<i64> {
        if final_sum % 2 != 0 {
            return vec![];
        }
        let mut res = Vec::new();
        let mut cur = 2i64;
        let mut sum = final_sum;
        while sum - cur > cur {
            res.push(cur);
            sum -= cur;
            cur += 2;
        }
        if sum > 0 {
            res.push(sum);
        }
        res
    }
}
```

## Racket

```racket
(define/contract (maximum-even-split finalSum)
  (-> exact-integer? (listof exact-integer?))
  (if (odd? finalSum)
      '()
      (let loop ((remaining finalSum) (cur 2) (acc '()))
        (if (> (- remaining cur) cur)
            (loop (- remaining cur) (+ cur 2) (cons cur acc))
            (cons remaining acc)))))
```

## Erlang

```erlang
-module(solution).
-export([maximum_even_split/1]).

-spec maximum_even_split(FinalSum :: integer()) -> [integer()].
maximum_even_split(FinalSum) when FinalSum rem 2 =:= 1 ->
    [];
maximum_even_split(FinalSum) ->
    split(FinalSum, 2, []).

split(Remaining, Curr, Acc) when Remaining - Curr > Curr ->
    NewRemaining = Remaining - Curr,
    split(NewRemaining, Curr + 2, [Curr | Acc]);
split(Remaining, _Curr, Acc) ->
    lists:reverse([Remaining | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_even_split(final_sum :: integer) :: [integer]
  def maximum_even_split(final_sum) do
    if rem(final_sum, 2) == 1 do
      []
    else
      split(final_sum, 2, [])
    end
  end

  defp split(remaining, cur, acc) when remaining - cur > cur do
    split(remaining - cur, cur + 2, [cur | acc])
  end

  defp split(remaining, _cur, acc) do
    Enum.reverse([remaining | acc])
  end
end
```
