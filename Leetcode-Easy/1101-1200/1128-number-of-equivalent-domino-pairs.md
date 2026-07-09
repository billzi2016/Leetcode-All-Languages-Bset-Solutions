# 1128. Number of Equivalent Domino Pairs

## Cpp

```cpp
class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        vector<int> cnt(100, 0);
        int ans = 0;
        for (const auto& d : dominoes) {
            int a = d[0], b = d[1];
            if (a > b) swap(a, b);
            int key = a * 10 + b;
            ans += cnt[key];
            ++cnt[key];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        int[] count = new int[100];
        int result = 0;
        for (int[] d : dominoes) {
            int a = d[0], b = d[1];
            if (a > b) {
                int tmp = a;
                a = b;
                b = tmp;
            }
            int key = a * 10 + b;
            result += count[key];
            count[key]++;
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        count = [0] * 100
        res = 0
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            idx = a * 10 + b
            res += count[idx]
            count[idx] += 1
        return res
```

## Python3

```python
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = [0] * 100
        ans = 0
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            key = a * 10 + b
            ans += cnt[key]
            cnt[key] += 1
        return ans
```

## C

```c
int numEquivDominoPairs(int** dominoes, int dominoesSize, int* dominoesColSize) {
    int count[100] = {0};
    int result = 0;
    for (int i = 0; i < dominoesSize; ++i) {
        int a = dominoes[i][0];
        int b = dominoes[i][1];
        if (a > b) {
            int tmp = a;
            a = b;
            b = tmp;
        }
        int key = a * 10 + b;
        result += count[key];
        ++count[key];
    }
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int NumEquivDominoPairs(int[][] dominoes) {
        int[] count = new int[100];
        long pairs = 0;
        foreach (var d in dominoes) {
            int a = d[0], b = d[1];
            if (a > b) {
                int temp = a;
                a = b;
                b = temp;
            }
            int key = a * 10 + b;
            pairs += count[key];
            count[key]++;
        }
        return (int)pairs;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} dominoes
 * @return {number}
 */
var numEquivDominoPairs = function(dominoes) {
    const count = new Array(100).fill(0);
    let result = 0;
    for (const [a, b] of dominoes) {
        const x = Math.min(a, b);
        const y = Math.max(a, b);
        const key = x * 10 + y; // since values are 1..9, key fits in [11,99]
        result += count[key];
        count[key]++;
    }
    return result;
};
```

## Typescript

```typescript
function numEquivDominoPairs(dominoes: number[][]): number {
    const cnt = new Array(100).fill(0);
    let res = 0;
    for (const [x, y] of dominoes) {
        const a = Math.min(x, y);
        const b = Math.max(x, y);
        const key = a * 10 + b;
        res += cnt[key];
        cnt[key]++;
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $dominoes
     * @return Integer
     */
    function numEquivDominoPairs($dominoes) {
        $cnt = array_fill(0, 100, 0);
        $result = 0;
        foreach ($dominoes as $d) {
            $a = $d[0];
            $b = $d[1];
            if ($a > $b) {
                $tmp = $a;
                $a = $b;
                $b = $tmp;
            }
            $key = $a * 10 + $b;
            $result += $cnt[$key];
            $cnt[$key]++;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func numEquivDominoPairs(_ dominoes: [[Int]]) -> Int {
        var count = [Int](repeating: 0, count: 100)
        var result = 0
        for d in dominoes {
            let a = d[0]
            let b = d[1]
            let key = (min(a, b) * 10) + max(a, b)
            result += count[key]
            count[key] += 1
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numEquivDominoPairs(dominoes: Array<IntArray>): Int {
        val count = IntArray(100)
        var result = 0L
        for (d in dominoes) {
            val a = d[0]
            val b = d[1]
            val key = if (a <= b) a * 10 + b else b * 10 + a
            result += count[key].toLong()
            count[key]++
        }
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int numEquivDominoPairs(List<List<int>> dominoes) {
    final counts = List.filled(100, 0);
    int result = 0;
    for (var d in dominoes) {
      int a = d[0];
      int b = d[1];
      if (a > b) {
        int temp = a;
        a = b;
        b = temp;
      }
      int key = a * 10 + b;
      result += counts[key];
      counts[key]++;
    }
    return result;
  }
}
```

## Golang

```go
func numEquivDominoPairs(dominoes [][]int) int {
    var cnt [100]int
    res := 0
    for _, d := range dominoes {
        a, b := d[0], d[1]
        if a > b {
            a, b = b, a
        }
        key := a*10 + b
        res += cnt[key]
        cnt[key]++
    }
    return res
}
```

## Ruby

```ruby
def num_equiv_domino_pairs(dominoes)
  counts = Array.new(100, 0)
  pairs = 0
  dominoes.each do |a, b|
    if a > b
      a, b = b, a
    end
    idx = a * 10 + b
    pairs += counts[idx]
    counts[idx] += 1
  end
  pairs
end
```

## Scala

```scala
object Solution {
    def numEquivDominoPairs(dominoes: Array[Array[Int]]): Int = {
        val freq = new Array[Int](100)
        var result: Long = 0L
        for (d <- dominoes) {
            val a = d(0)
            val b = d(1)
            val x = if (a <= b) a else b
            val y = if (a <= b) b else a
            val key = x * 10 + y
            result += freq(key)
            freq(key) += 1
        }
        result.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_equiv_domino_pairs(dominoes: Vec<Vec<i32>>) -> i32 {
        let mut count = [0i32; 100];
        let mut result: i32 = 0;
        for d in dominoes.iter() {
            let a = d[0] as usize;
            let b = d[1] as usize;
            let (x, y) = if a <= b { (a, b) } else { (b, a) };
            let key = x * 10 + y;
            result += count[key];
            count[key] += 1;
        }
        result
    }
}
```

## Racket

```racket
(define/contract (num-equiv-domino-pairs dominoes)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let ([counts (make-vector 100 0)])
    (let loop ((lst dominoes) (total 0))
      (if (null? lst)
          total
          (let* ([d (car lst)]
                 [a (first d)]
                 [b (second d)]
                 [x (min a b)]
                 [y (max a b)]
                 [key (+ (* x 10) y)])
            (let ([c (vector-ref counts key)])
              (vector-set! counts key (+ c 1))
              (loop (cdr lst) (+ total c))))))))
```

## Erlang

```erlang
-spec num_equiv_domino_pairs(Dominoes :: [[integer()]]) -> integer().
num_equiv_domino_pairs(Dominoes) ->
    num_equiv_domino_pairs(Dominoes, #{}, 0).

num_equiv_domino_pairs([], _Map, Res) ->
    Res;
num_equiv_domino_pairs([[A,B]|Rest], Map, Res) ->
    {X,Y} = if A =< B -> {A,B}; true -> {B,A} end,
    Key = X*10 + Y,
    Count = maps:get(Key, Map, 0),
    NewRes = Res + Count,
    NewMap = maps:put(Key, Count + 1, Map),
    num_equiv_domino_pairs(Rest, NewMap, NewRes).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_equiv_domino_pairs(dominoes :: [[integer]]) :: integer
  def num_equiv_domino_pairs(dominoes) do
    {_freq, result} =
      Enum.reduce(dominoes, {%{}, 0}, fn [a, b], {freq, acc} ->
        {x, y} = if a <= b, do: {a, b}, else: {b, a}
        key = x * 10 + y
        count = Map.get(freq, key, 0)
        {Map.put(freq, key, count + 1), acc + count}
      end)

    result
  end
end
```
