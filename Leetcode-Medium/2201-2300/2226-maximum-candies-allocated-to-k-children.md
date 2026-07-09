# 2226. Maximum Candies Allocated to K Children

## Cpp

```cpp
class Solution {
public:
    int maximumCandies(vector<int>& candies, long long k) {
        int maxPile = *max_element(candies.begin(), candies.end());
        long long left = 0, right = maxPile;
        while (left < right) {
            long long mid = (left + right + 1) / 2; // candidate candies per child
            long long cnt = 0;
            for (int c : candies) {
                cnt += c / mid;
                if (cnt >= k) break; // early exit
            }
            if (cnt >= k)
                left = mid;
            else
                right = mid - 1;
        }
        return static_cast<int>(left);
    }
};
```

## Java

```java
class Solution {
    public int maximumCandies(int[] candies, long k) {
        int maxPile = 0;
        for (int c : candies) {
            if (c > maxPile) maxPile = c;
        }
        int left = 0, right = maxPile;
        while (left < right) {
            int mid = left + (right - left + 1) / 2; // avoid overflow
            if (canAllocate(candies, k, mid)) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }

    private boolean canAllocate(int[] candies, long k, int perChild) {
        if (perChild == 0) return true; // trivially possible
        long childrenServed = 0;
        for (int c : candies) {
            childrenServed += c / perChild;
            if (childrenServed >= k) {
                return true;
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, max(candies)
        while left < right:
            mid = (left + right + 1) // 2
            total = 0
            for c in candies:
                total += c // mid
                if total >= k:   # early stop to avoid overflow
                    break
            if total >= k:
                left = mid
            else:
                right = mid - 1
        return left
```

## Python3

```python
class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        if not candies:
            return 0
        left, right = 0, max(candies)
        while left < right:
            mid = (left + right + 1) // 2
            total = 0
            for c in candies:
                total += c // mid
                if total >= k:  # early stop to avoid overflow
                    break
            if total >= k:
                left = mid
            else:
                right = mid - 1
        return left
```

## C

```c
int maximumCandies(int* candies, int candiesSize, long long k) {
    if (candiesSize == 0) return 0;
    int maxPile = 0;
    for (int i = 0; i < candiesSize; ++i) {
        if (candies[i] > maxPile) maxPile = candies[i];
    }
    
    int left = 0, right = maxPile;
    while (left < right) {
        int mid = left + (right - left + 1) / 2; // upper mid
        long long children = 0;
        for (int i = 0; i < candiesSize; ++i) {
            children += candies[i] / mid;
            if (children >= k) break; // early stop to avoid overflow
        }
        if (children >= k)
            left = mid;
        else
            right = mid - 1;
    }
    return left;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaximumCandies(int[] candies, long k)
    {
        long left = 0;
        long right = 0;
        foreach (int c in candies)
            if (c > right) right = c;

        while (left < right)
        {
            long mid = (left + right + 1) / 2;
            long children = 0;
            foreach (int c in candies)
            {
                children += c / mid;
                if (children >= k) break; // early exit
            }

            if (children >= k)
                left = mid;
            else
                right = mid - 1;
        }

        return (int)left;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} candies
 * @param {number} k
 * @return {number}
 */
var maximumCandies = function(candies, k) {
    let maxPile = 0;
    for (const c of candies) {
        if (c > maxPile) maxPile = c;
    }
    let left = 0, right = maxPile;
    while (left < right) {
        const mid = Math.floor((left + right + 1) / 2);
        let children = 0;
        for (const c of candies) {
            children += Math.floor(c / mid);
            if (children >= k) break; // early exit
        }
        if (children >= k) {
            left = mid;
        } else {
            right = mid - 1;
        }
    }
    return left;
};
```

## Typescript

```typescript
function maximumCandies(candies: number[], k: number): number {
    let left = 0;
    let right = Math.max(...candies);
    while (left < right) {
        const mid = Math.floor((left + right + 1) / 2);
        let children = 0;
        for (const pile of candies) {
            children += Math.floor(pile / mid);
            if (children >= k) break;
        }
        if (children >= k) {
            left = mid;
        } else {
            right = mid - 1;
        }
    }
    return left;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $candies
     * @param Integer $k
     * @return Integer
     */
    function maximumCandies($candies, $k) {
        $maxPile = 0;
        foreach ($candies as $c) {
            if ($c > $maxPile) $maxPile = $c;
        }

        $left = 0;
        $right = $maxPile;

        while ($left < $right) {
            // upper mid to avoid infinite loop
            $mid = intdiv($left + $right + 1, 2);
            $children = 0;
            foreach ($candies as $c) {
                $children += intdiv($c, $mid);
                if ($children >= $k) break; // early exit
            }
            if ($children >= $k) {
                $left = $mid;
            } else {
                $right = $mid - 1;
            }
        }

        return $left;
    }
}
```

## Swift

```swift
class Solution {
    func maximumCandies(_ candies: [Int], _ k: Int) -> Int {
        var maxPile = 0
        for c in candies {
            if c > maxPile { maxPile = c }
        }
        var left = 0
        var right = maxPile
        let targetK = Int64(k)
        
        func canAllocate(_ x: Int) -> Bool {
            if x == 0 { return true }
            var total: Int64 = 0
            for c in candies {
                total += Int64(c / x)
                if total >= targetK { return true }
            }
            return false
        }
        
        while left < right {
            let mid = (left + right + 1) / 2
            if canAllocate(mid) {
                left = mid
            } else {
                right = mid - 1
            }
        }
        return left
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumCandies(candies: IntArray, k: Long): Int {
        var left = 0
        var right = candies.maxOrNull() ?: 0
        while (left < right) {
            val mid = (left + right + 1) / 2
            if (mid > 0 && canAllocate(candies, k, mid)) {
                left = mid
            } else {
                right = mid - 1
            }
        }
        return left
    }

    private fun canAllocate(candies: IntArray, k: Long, x: Int): Boolean {
        var total = 0L
        for (c in candies) {
            total += c / x
            if (total >= k) return true
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  int maximumCandies(List<int> candies, int k) {
    int maxCandy = 0;
    for (var c in candies) {
      if (c > maxCandy) maxCandy = c;
    }
    int left = 0;
    int right = maxCandy;
    while (left < right) {
      int mid = ((left + right + 1) ~/ 2);
      if (mid == 0) break; // safety, though shouldn't happen
      int children = 0;
      for (var c in candies) {
        children += c ~/ mid;
        if (children >= k) break; // early exit to avoid overflow
      }
      if (children >= k) {
        left = mid;
      } else {
        right = mid - 1;
      }
    }
    return left;
  }
}
```

## Golang

```go
func maximumCandies(candies []int, k int64) int {
	if k == 0 {
		return 0
	}
	maxPile := 0
	for _, v := range candies {
		if v > maxPile {
			maxPile = v
		}
	}
	canAllocate := func(x int) bool {
		if x == 0 {
			return true
		}
		var cnt int64
		for _, v := range candies {
			cnt += int64(v / x)
			if cnt >= k {
				return true
			}
		}
		return false
	}

	left, right := 0, maxPile
	for left < right {
		mid := (left + right + 1) / 2
		if canAllocate(mid) {
			left = mid
		} else {
			right = mid - 1
		}
	}
	return left
}
```

## Ruby

```ruby
def maximum_candies(candies, k)
  left = 0
  right = candies.max || 0

  while left < right
    mid = (left + right + 1) / 2
    total = 0
    candies.each do |c|
      total += c / mid
      break if total >= k
    end

    if total >= k
      left = mid
    else
      right = mid - 1
    end
  end

  left
end
```

## Scala

```scala
object Solution {
    def maximumCandies(candies: Array[Int], k: Long): Int = {
        var left: Long = 0L
        var right: Long = candies.max.toLong
        while (left < right) {
            val mid = (left + right + 1) / 2
            var cnt: Long = 0L
            var i = 0
            while (i < candies.length && cnt < k) {
                cnt += candies(i).toLong / mid
                i += 1
            }
            if (cnt >= k) left = mid else right = mid - 1
        }
        left.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_candies(candies: Vec<i32>, k: i64) -> i32 {
        let max_candy = *candies.iter().max().unwrap() as i64;
        let mut left = 0i64;
        let mut right = max_candy;
        while left < right {
            let mid = (left + right + 1) / 2;
            let mut cnt: i64 = 0;
            for &c in &candies {
                cnt += (c as i64) / mid;
                if cnt >= k {
                    break;
                }
            }
            if cnt >= k {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        left as i32
    }
}
```

## Racket

```racket
(define/contract (maximum-candies candies k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((max-pile (apply max candies))
         (can-allocate?
          (lambda (cand-per-child)
            (>= (for/sum ([c candies])
                  (quotient c cand-per-child))
                k))))
    (let loop ((left 0) (right max-pile))
      (if (= left right)
          left
          (let* ((mid (quotient (+ left right 1) 2)))
            (if (can-allocate? mid)
                (loop mid right)
                (loop left (- mid 1))))))))
```

## Erlang

```erlang
-spec maximum_candies(Candies :: [integer()], K :: integer()) -> integer().
maximum_candies(Candies, K) ->
    MaxPile = lists:max(Candies),
    binary_search(Candies, K, 0, MaxPile).

binary_search(_Candies, _K, Left, Right) when Left >= Right ->
    Left;
binary_search(Candies, K, Left, Right) ->
    Mid = (Left + Right + 1) div 2,
    case can_allocate(Candies, K, Mid) of
        true -> binary_search(Candies, K, Mid, Right);
        false -> binary_search(Candies, K, Left, Mid - 1)
    end.

can_allocate(Candies, K, CandPerChild) ->
    Total = lists:foldl(fun(Pile, Acc) -> Acc + Pile div CandPerChild end, 0, Candies),
    Total >= K.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_candies(candies :: [integer], k :: integer) :: integer
  def maximum_candies(candies, k) do
    max_pile = Enum.max(candies)
    binary_search(candies, k, 0, max_pile)
  end

  defp binary_search(_candies, _k, left, right) when left == right, do: left

  defp binary_search(candies, k, left, right) do
    mid = div(left + right + 1, 2)

    total =
      Enum.reduce(candies, 0, fn pile, acc ->
        acc + div(pile, mid)
      end)

    if total >= k do
      binary_search(candies, k, mid, right)
    else
      binary_search(candies, k, left, mid - 1)
    end
  end
end
```
