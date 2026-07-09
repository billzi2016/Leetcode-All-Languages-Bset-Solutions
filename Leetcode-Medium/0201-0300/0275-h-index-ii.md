# 0275. H-Index II

## Cpp

```cpp
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        int left = 0, right = n - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int h = n - mid;
            if (citations[mid] >= h) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return n - left;
    }
};
```

## Java

```java
class Solution {
    public int hIndex(int[] citations) {
        int n = citations.length;
        int left = 0, right = n - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int h = n - mid;
            if (citations[mid] >= h) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left == n ? 0 : n - left;
    }
}
```

## Python

```python
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        left, right = 0, n - 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid:
                ans = n - mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid:
                ans = n - mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
```

## C

```c
int hIndex(int* citations, int citationsSize) {
    int left = 0, right = citationsSize - 1;
    int answer = 0;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        int papers = citationsSize - mid; // number of papers with at least citations[mid] citations
        if (citations[mid] >= papers) {
            answer = papers;          // possible h-index, try to find smaller index
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return answer;
}
```

## Csharp

```csharp
public class Solution
{
    public int HIndex(int[] citations)
    {
        int n = citations.Length;
        int left = 0, right = n - 1;
        int ans = 0;

        while (left <= right)
        {
            int mid = left + (right - left) / 2;
            int h = n - mid;

            if (citations[mid] >= h)
            {
                ans = h;          // possible h-index
                right = mid - 1;   // try to find a smaller index for larger h
            }
            else
            {
                left = mid + 1;
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    const n = citations.length;
    let low = 0, high = n - 1;
    let result = 0;
    while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        const papersWithAtLeastCitations = n - mid; // number of papers from mid to end
        if (citations[mid] >= papersWithAtLeastCitations) {
            result = papersWithAtLeastCitations;
            high = mid - 1; // try to find a smaller index
        } else {
            low = mid + 1;
        }
    }
    return result;
};
```

## Typescript

```typescript
function hIndex(citations: number[]): number {
    const n = citations.length;
    let left = 0, right = n - 1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (citations[mid] >= n - mid) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return n - left;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $citations
     * @return Integer
     */
    function hIndex($citations) {
        $n = count($citations);
        $low = 0;
        $high = $n - 1;
        $answer = 0;

        while ($low <= $high) {
            $mid = intdiv($low + $high, 2);
            $papersWithAtLeastMidCitations = $n - $mid;

            if ($citations[$mid] >= $papersWithAtLeastMidCitations) {
                $answer = $papersWithAtLeastMidCitations;
                $high = $mid - 1; // try to find a smaller index (larger h)
            } else {
                $low = $mid + 1;
            }
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func hIndex(_ citations: [Int]) -> Int {
        let n = citations.count
        var left = 0
        var right = n - 1
        var result = 0
        
        while left <= right {
            let mid = (left + right) / 2
            let h = n - mid
            if citations[mid] >= h {
                result = h
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun hIndex(citations: IntArray): Int {
        val n = citations.size
        var left = 0
        var right = n - 1
        while (left <= right) {
            val mid = left + (right - left) / 2
            if (citations[mid] >= n - mid) {
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        return n - left
    }
}
```

## Dart

```dart
class Solution {
  int hIndex(List<int> citations) {
    int n = citations.length;
    int left = 0, right = n - 1;
    int ans = 0;
    while (left <= right) {
      int mid = left + ((right - left) >> 1);
      int h = n - mid;
      if (citations[mid] >= h) {
        ans = h;
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func hIndex(citations []int) int {
	n := len(citations)
	left, right := 0, n-1
	ans := 0
	for left <= right {
		mid := left + (right-left)/2
		if citations[mid] >= n-mid {
			ans = n - mid
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return ans
}
```

## Ruby

```ruby
def h_index(citations)
  n = citations.length
  left = 0
  right = n - 1
  result = 0
  while left <= right
    mid = (left + right) / 2
    if citations[mid] >= n - mid
      result = n - mid
      right = mid - 1
    else
      left = mid + 1
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def hIndex(citations: Array[Int]): Int = {
        val n = citations.length
        var left = 0
        var right = n - 1
        var result = 0
        while (left <= right) {
            val mid = left + (right - left) / 2
            val h = n - mid
            if (citations(mid) >= h) {
                result = h
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn h_index(citations: Vec<i32>) -> i32 {
        let n = citations.len();
        let mut left = 0usize;
        let mut right = n; // exclusive upper bound
        while left < right {
            let mid = (left + right) / 2;
            if citations[mid] as usize >= n - mid {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        (n - left) as i32
    }
}
```

## Racket

```racket
(define/contract (h-index citations)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((vec (list->vector citations))
         (n (vector-length vec)))
    (let loop ((lo 0) (hi (- n 1)) (ans 0))
      (if (> lo hi)
          ans
          (let* ((mid (quotient (+ lo hi) 2))
                 (c (vector-ref vec mid))
                 (papers (- n mid)))
            (if (>= c papers)
                (loop lo (- mid 1) papers)
                (loop (+ mid 1) hi ans)))))))
```

## Erlang

```erlang
-module(solution).
-export([h_index/1]).

-spec h_index(Citations :: [integer()]) -> integer().
h_index(Citations) ->
    Tuple = list_to_tuple(Citations),
    N = tuple_size(Tuple),
    binary_search(Tuple, N, 0, N - 1).

binary_search(_Tuple, N, Low, High) when Low > High ->
    case Low < N of
        true -> N - Low;
        false -> 0
    end;
binary_search(Tuple, N, Low, High) ->
    Mid = (Low + High) div 2,
    Citation = element(Mid + 1, Tuple),
    Papers = N - Mid,
    if
        Citation >= Papers ->
            binary_search(Tuple, N, Low, Mid - 1);
        true ->
            binary_search(Tuple, N, Mid + 1, High)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec h_index(citations :: [integer]) :: integer
  def h_index(citations) do
    cit = List.to_tuple(citations)
    n = tuple_size(cit)

    binary_search(cit, n, 0, n - 1)
  end

  defp binary_search(_cit, n, lo, hi) when lo > hi, do: n - lo

  defp binary_search(cit, n, lo, hi) do
    mid = div(lo + hi, 2)
    c = elem(cit, mid)
    papers = n - mid

    if c >= papers do
      binary_search(cit, n, lo, mid - 1)
    else
      binary_search(cit, n, mid + 1, hi)
    end
  end
end
```
