# 2951. Find the Peaks

## Cpp

```cpp
class Solution {
public:
    vector<int> findPeaks(vector<int>& mountain) {
        int n = mountain.size();
        vector<int> res;
        for (int i = 1; i + 1 < n; ++i) {
            if (mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1]) {
                res.push_back(i);
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public java.util.List<Integer> findPeaks(int[] mountain) {
        java.util.List<Integer> res = new java.util.ArrayList<>();
        for (int i = 1; i < mountain.length - 1; i++) {
            if (mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1]) {
                res.add(i);
            }
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def findPeaks(self, mountain):
        """
        :type mountain: List[int]
        :rtype: List[int]
        """
        n = len(mountain)
        peaks = []
        for i in range(1, n - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```

## Python3

```python
from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        peaks = []
        for i in range(1, n - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findPeaks(int* mountain, int mountainSize, int* returnSize) {
    int maxPeaks = (mountainSize > 2) ? mountainSize - 2 : 0;
    int* peaks = (int*)malloc(sizeof(int) * maxPeaks);
    int cnt = 0;
    
    for (int i = 1; i < mountainSize - 1; ++i) {
        if (mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1]) {
            peaks[cnt++] = i;
        }
    }
    
    *returnSize = cnt;
    return peaks;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> FindPeaks(int[] mountain) {
        var result = new List<int>();
        for (int i = 1; i < mountain.Length - 1; i++) {
            if (mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1]) {
                result.Add(i);
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} mountain
 * @return {number[]}
 */
var findPeaks = function(mountain) {
    const n = mountain.length;
    const res = [];
    for (let i = 1; i < n - 1; ++i) {
        if (mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1]) {
            res.push(i);
        }
    }
    return res;
};
```

## Typescript

```typescript
function findPeaks(mountain: number[]): number[] {
    const res: number[] = [];
    for (let i = 1; i < mountain.length - 1; i++) {
        if (mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1]) {
            res.push(i);
        }
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $mountain
     * @return Integer[]
     */
    function findPeaks($mountain) {
        $n = count($mountain);
        $result = [];
        for ($i = 1; $i < $n - 1; $i++) {
            if ($mountain[$i] > $mountain[$i - 1] && $mountain[$i] > $mountain[$i + 1]) {
                $result[] = $i;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func findPeaks(_ mountain: [Int]) -> [Int] {
        var peaks = [Int]()
        let n = mountain.count
        guard n >= 3 else { return peaks }
        for i in 1..<(n - 1) {
            if mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1] {
                peaks.append(i)
            }
        }
        return peaks
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findPeaks(mountain: IntArray): List<Int> {
        val result = mutableListOf<Int>()
        for (i in 1 until mountain.size - 1) {
            if (mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1]) {
                result.add(i)
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> findPeaks(List<int> mountain) {
    List<int> peaks = [];
    for (int i = 1; i < mountain.length - 1; i++) {
      if (mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1]) {
        peaks.add(i);
      }
    }
    return peaks;
  }
}
```

## Golang

```go
func findPeaks(mountain []int) []int {
    n := len(mountain)
    peaks := make([]int, 0)
    for i := 1; i < n-1; i++ {
        if mountain[i] > mountain[i-1] && mountain[i] > mountain[i+1] {
            peaks = append(peaks, i)
        }
    }
    return peaks
}
```

## Ruby

```ruby
# @param {Integer[]} mountain
# @return {Integer[]}
def find_peaks(mountain)
  result = []
  (1...mountain.length - 1).each do |i|
    if mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1]
      result << i
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def findPeaks(mountain: Array[Int]): List[Int] = {
        val n = mountain.length
        val peaks = scala.collection.mutable.ListBuffer[Int]()
        for (i <- 1 until n - 1) {
            if (mountain(i) > mountain(i - 1) && mountain(i) > mountain(i + 1)) {
                peaks += i
            }
        }
        peaks.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_peaks(mountain: Vec<i32>) -> Vec<i32> {
        let n = mountain.len();
        let mut peaks = Vec::new();
        if n < 3 {
            return peaks;
        }
        for i in 1..n - 1 {
            if mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1] {
                peaks.push(i as i32);
            }
        }
        peaks
    }
}
```

## Racket

```racket
(define/contract (find-peaks mountain)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let ((n (length mountain)))
    (for/list ([i (in-range 1 (- n 1))]
               #:when (> (list-ref mountain i) (list-ref mountain (- i 1)))
               #:when (> (list-ref mountain i) (list-ref mountain (+ i 1))))
      i)))
```

## Erlang

```erlang
-spec find_peaks(Mountain :: [integer()]) -> [integer()].
find_peaks(Mountain) ->
    find_peaks(Mountain, 0, []).

find_peaks([_, _], _Idx, Acc) ->
    lists:reverse(Acc);
find_peaks([Prev, Curr, Next | Rest], Idx, Acc) ->
    NewAcc = case (Curr > Prev) andalso (Curr > Next) of
                true -> [Idx + 1 | Acc];
                false -> Acc
             end,
    find_peaks([Curr, Next | Rest], Idx + 1, NewAcc);
find_peaks(_, _Idx, Acc) ->
    lists:reverse(Acc).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_peaks(mountain :: [integer]) :: [integer]
  def find_peaks(mountain) do
    len = length(mountain)

    1..(len - 2)
    |> Enum.reduce([], fn i, acc ->
      val = Enum.at(mountain, i)

      if val > Enum.at(mountain, i - 1) and val > Enum.at(mountain, i + 1) do
        [i | acc]
      else
        acc
      end
    end)
    |> Enum.reverse()
  end
end
```
