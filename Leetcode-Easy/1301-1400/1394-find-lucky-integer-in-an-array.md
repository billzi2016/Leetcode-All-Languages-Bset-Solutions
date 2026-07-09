# 1394. Find Lucky Integer in an Array

## Cpp

```cpp
class Solution {
public:
    int findLucky(vector<int>& arr) {
        const int MAXV = 501;
        int freq[MAXV] = {0};
        for (int x : arr) {
            if (x < MAXV) ++freq[x];
        }
        int ans = -1;
        for (int i = 1; i < MAXV; ++i) {
            if (freq[i] == i && i > ans) ans = i;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int findLucky(int[] arr) {
        int[] freq = new int[501];
        for (int num : arr) {
            if (num <= 500) {
                freq[num]++;
            }
        }
        int result = -1;
        for (int i = 1; i <= 500; i++) {
            if (freq[i] == i && i > result) {
                result = i;
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        lucky = -1
        for num, cnt in freq.items():
            if num == cnt and num > lucky:
                lucky = num
        return lucky
```

## Python3

```python
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = [0] * 501
        for num in arr:
            if num <= 500:
                freq[num] += 1
        ans = -1
        for val in range(1, 501):
            if freq[val] == val and val > ans:
                ans = val
        return ans
```

## C

```c
int findLucky(int* arr, int arrSize) {
    int freq[501] = {0};
    for (int i = 0; i < arrSize; ++i) {
        int v = arr[i];
        if (v >= 1 && v <= 500) {
            freq[v]++;
        }
    }
    int ans = -1;
    for (int i = 1; i <= 500; ++i) {
        if (freq[i] == i && i > ans) {
            ans = i;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindLucky(int[] arr)
    {
        const int MAX = 501;
        int[] freq = new int[MAX];
        foreach (int num in arr)
        {
            if (num < MAX) freq[num]++;
        }

        int result = -1;
        for (int i = 1; i < MAX; i++)
        {
            if (freq[i] == i && i > result)
                result = i;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var findLucky = function(arr) {
    const freq = new Array(501).fill(0);
    for (const num of arr) {
        freq[num]++;
    }
    let ans = -1;
    for (let i = 1; i < freq.length; i++) {
        if (freq[i] === i && i > ans) {
            ans = i;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function findLucky(arr: number[]): number {
    const freq = new Array(501).fill(0);
    for (const v of arr) {
        if (v <= 500) freq[v]++;
    }
    let ans = -1;
    for (let i = 1; i <= 500; i++) {
        if (freq[i] === i && i > ans) {
            ans = i;
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function findLucky($arr) {
        $freq = [];
        foreach ($arr as $num) {
            if (!isset($freq[$num])) {
                $freq[$num] = 0;
            }
            $freq[$num]++;
        }

        $ans = -1;
        foreach ($freq as $value => $count) {
            if ($value == $count && $value > $ans) {
                $ans = $value;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func findLucky(_ arr: [Int]) -> Int {
        var freq = [Int: Int]()
        for num in arr {
            freq[num, default: 0] += 1
        }
        var result = -1
        for (num, count) in freq {
            if num == count && num > result {
                result = num
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findLucky(arr: IntArray): Int {
        val freq = IntArray(501)
        for (num in arr) {
            if (num <= 500) freq[num]++
        }
        var ans = -1
        for (i in 1..500) {
            if (freq[i] == i && i > ans) ans = i
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int findLucky(List<int> arr) {
    const int maxVal = 500;
    List<int> freq = List.filled(maxVal + 1, 0);
    for (int v in arr) {
      if (v >= 0 && v <= maxVal) freq[v]++;
    }
    int ans = -1;
    for (int i = 1; i <= maxVal; i++) {
      if (freq[i] == i && i > ans) ans = i;
    }
    return ans;
  }
}
```

## Golang

```go
func findLucky(arr []int) int {
    freq := make(map[int]int)
    for _, v := range arr {
        freq[v]++
    }
    result := -1
    for val, cnt := range freq {
        if val == cnt && val > result {
            result = val
        }
    }
    return result
}
```

## Ruby

```ruby
def find_lucky(arr)
  freq = Hash.new(0)
  arr.each { |x| freq[x] += 1 }
  ans = -1
  freq.each do |num, cnt|
    ans = num if cnt == num && num > ans
  end
  ans
end
```

## Scala

```scala
object Solution {
    def findLucky(arr: Array[Int]): Int = {
        val maxVal = 500
        val freq = new Array[Int](maxVal + 1)
        for (v <- arr) {
            if (v <= maxVal) freq(v) += 1
        }
        var ans = -1
        for (i <- 1 to maxVal) {
            if (freq(i) == i && i > ans) ans = i
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_lucky(arr: Vec<i32>) -> i32 {
        let mut freq = vec![0usize; 501];
        for &v in &arr {
            if (v as usize) < freq.len() {
                freq[v as usize] += 1;
            }
        }
        let mut ans = -1i32;
        for i in 1..=500 {
            if freq[i] == i {
                ans = ans.max(i as i32);
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (find-lucky arr)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([max-n 500]
         [freq (make-vector (+ max-n 1) 0)])
    (for ([x arr])
      (when (and (>= x 0) (<= x max-n))
        (vector-set! freq x (add1 (vector-ref freq x)))))
    (let loop ((i max-n))
      (cond [(< i 0) -1]
            [(= (vector-ref freq i) i) i]
            [else (loop (sub1 i))]))))
```

## Erlang

```erlang
-spec find_lucky(Arr :: [integer()]) -> integer().
find_lucky(Arr) ->
    Freq = lists:foldl(
        fun(X, Acc) ->
            maps:update_with(X, fun(C) -> C + 1 end, 1, Acc)
        end,
        #{},
        Arr
    ),
    maps:fold(
        fun(Key, Count, Current) ->
            if Key == Count, Key > Current -> Key;
               true -> Current
            end
        end,
        -1,
        Freq
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_lucky(arr :: [integer]) :: integer
  def find_lucky(arr) do
    freq =
      Enum.reduce(arr, %{}, fn x, acc ->
        Map.update(acc, x, 1, &(&1 + 1))
      end)

    lucky =
      freq
      |> Enum.filter(fn {k, v} -> k == v end)
      |> Enum.map(fn {k, _v} -> k end)

    case lucky do
      [] -> -1
      _ -> Enum.max(lucky)
    end
  end
end
```
