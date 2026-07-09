# 0274. H-Index

## Cpp

```cpp
class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(), citations.end(), greater<int>());
        int h = 0;
        for (int i = 0; i < (int)citations.size(); ++i) {
            if (citations[i] > i)
                h = i + 1;
            else
                break;
        }
        return h;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        int n = citations.length;
        int h = 0;
        for (int i = n - 1; i >= 0; i--) {
            int papers = n - i;
            if (citations[i] >= papers) {
                h = papers;
            } else {
                break;
            }
        }
        return h;
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
        buckets = [0] * (n + 1)
        for c in citations:
            if c >= n:
                buckets[n] += 1
            else:
                buckets[c] += 1

        total = 0
        for i in range(n, -1, -1):
            total += buckets[i]
            if total >= i:
                return i
        return 0
```

## Python3

```python
class Solution:
    def hIndex(self, citations):
        n = len(citations)
        buckets = [0] * (n + 1)
        for c in citations:
            if c >= n:
                buckets[n] += 1
            else:
                buckets[c] += 1
        total = 0
        for i in range(n, -1, -1):
            total += buckets[i]
            if total >= i:
                return i
        return 0
```

## C

```c
#include <stdlib.h>

int hIndex(int* citations, int citationsSize) {
    int *bucket = (int *)calloc(citationsSize + 1, sizeof(int));
    if (!bucket) return 0;
    
    for (int i = 0; i < citationsSize; ++i) {
        int c = citations[i];
        if (c > citationsSize)
            bucket[citationsSize]++;
        else
            bucket[c]++;
    }
    
    int sum = 0;
    for (int i = citationsSize; i >= 0; --i) {
        sum += bucket[i];
        if (sum >= i) {
            free(bucket);
            return i;
        }
    }
    
    free(bucket);
    return 0;
}
```

## Csharp

```csharp
public class Solution {
    public int HIndex(int[] citations) {
        int n = citations.Length;
        int[] buckets = new int[n + 1];
        foreach (int c in citations) {
            if (c >= n) {
                buckets[n]++;
            } else {
                buckets[c]++;
            }
        }
        int total = 0;
        for (int i = n; i >= 0; i--) {
            total += buckets[i];
            if (total >= i) return i;
        }
        return 0;
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
    const buckets = new Array(n + 1).fill(0);
    
    for (let c of citations) {
        if (c >= n) {
            buckets[n] += 1;
        } else {
            buckets[c] += 1;
        }
    }
    
    let total = 0;
    for (let i = n; i >= 0; i--) {
        total += buckets[i];
        if (total >= i) {
            return i;
        }
    }
    return 0;
};
```

## Typescript

```typescript
function hIndex(citations: number[]): number {
    citations.sort((a, b) => b - a);
    let h = 0;
    for (let i = 0; i < citations.length; i++) {
        if (citations[i] >= i + 1) {
            h = i + 1;
        } else {
            break;
        }
    }
    return h;
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
        rsort($citations);
        $h = 0;
        foreach ($citations as $i => $c) {
            if ($c >= $i + 1) {
                $h = $i + 1;
            } else {
                break;
            }
        }
        return $h;
    }
}
```

## Swift

```swift
class Solution {
    func hIndex(_ citations: [Int]) -> Int {
        let sorted = citations.sorted(by: >)
        var h = 0
        for (i, c) in sorted.enumerated() {
            if c >= i + 1 {
                h = i + 1
            } else {
                break
            }
        }
        return h
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun hIndex(citations: IntArray): Int {
        val sorted = citations.sortedArrayDescending()
        var h = 0
        for (i in sorted.indices) {
            if (sorted[i] > i) {
                h = i + 1
            } else {
                break
            }
        }
        return h
    }
}
```

## Dart

```dart
class Solution {
  int hIndex(List<int> citations) {
    citations.sort((a, b) => b - a);
    int h = 0;
    for (int i = 0; i < citations.length; i++) {
      if (citations[i] >= i + 1) {
        h = i + 1;
      } else {
        break;
      }
    }
    return h;
  }
}
```

## Golang

```go
func hIndex(citations []int) int {
	n := len(citations)
	buckets := make([]int, n+1)
	for _, c := range citations {
		if c >= n {
			buckets[n]++
		} else {
			buckets[c]++
		}
	}
	sum := 0
	for i := n; i >= 0; i-- {
		sum += buckets[i]
		if sum >= i {
			return i
		}
	}
	return 0
}
```

## Ruby

```ruby
def h_index(citations)
  n = citations.length
  buckets = Array.new(n + 1, 0)
  citations.each do |c|
    if c >= n
      buckets[n] += 1
    else
      buckets[c] += 1
    end
  end
  total = 0
  i = n
  while i >= 0
    total += buckets[i]
    return i if total >= i
    i -= 1
  end
  0
end
```

## Scala

```scala
object Solution {
  def hIndex(citations: Array[Int]): Int = {
    val n = citations.length
    val buckets = new Array[Int](n + 1)
    for (c <- citations) {
      if (c >= n) buckets(n) += 1 else buckets(c) += 1
    }
    var sum = 0
    var i = n
    while (i >= 0) {
      sum += buckets(i)
      if (sum >= i) return i
      i -= 1
    }
    0
  }
}
```

## Rust

```rust
impl Solution {
    pub fn h_index(citations: Vec<i32>) -> i32 {
        let n = citations.len();
        let mut buckets = vec![0usize; n + 1];
        for &c in &citations {
            if (c as usize) >= n {
                buckets[n] += 1;
            } else {
                buckets[c as usize] += 1;
            }
        }
        let mut total = 0usize;
        for i in (0..=n).rev() {
            total += buckets[i];
            if total >= i {
                return i as i32;
            }
        }
        0
    }
}
```

## Racket

```racket
(define/contract (h-index citations)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((sorted (sort citations >))
         (len (length sorted)))
    (let loop ((i 0) (best 0))
      (if (= i len)
          best
          (let* ((c (list-ref sorted i))
                 (h (+ i 1))) ; number of papers considered so far
            (if (>= c h)
                (loop (+ i 1) h)
                best))))))
```

## Erlang

```erlang
-module(solution).
-export([h_index/1]).

-spec h_index(Citations :: [integer()]) -> integer().
h_index(Citations) ->
    Sorted = lists:reverse(lists:sort(Citations)),
    compute_h(Sorted, 1, 0).

compute_h([], _Idx, H) -> H;
compute_h([C|Rest], Idx, _H) when C >= Idx ->
    compute_h(Rest, Idx + 1, Idx);
compute_h(_List, _Idx, H) -> H.
```

## Elixir

```elixir
defmodule Solution do
  @spec h_index(citations :: [integer]) :: integer
  def h_index(citations) do
    sorted = Enum.sort(citations, &>=/2)

    {h, _} =
      Enum.reduce_while(Enum.with_index(sorted), {0, nil}, fn {c, idx}, {_curr_h, _prev_c} ->
        if c >= idx + 1 do
          {:cont, {idx + 1, c}}
        else
          {:halt, {idx, c}}
        end
      end)

    h
  end
end
```
