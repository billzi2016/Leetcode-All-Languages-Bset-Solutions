# 1894. Find the Student that Will Replace the Chalk

## Cpp

```cpp
class Solution {
public:
    int chalkReplacer(std::vector<int>& chalk, int k) {
        long long total = 0;
        for (int c : chalk) total += c;
        long long remaining = k % total;
        for (int i = 0; i < (int)chalk.size(); ++i) {
            if (remaining < chalk[i]) return i;
            remaining -= chalk[i];
        }
        return 0; // Should never reach here
    }
};
```

## Java

```java
class Solution {
    public int chalkReplacer(int[] chalk, int k) {
        long total = 0;
        for (int c : chalk) {
            total += c;
        }
        long remaining = k % total;
        for (int i = 0; i < chalk.length; i++) {
            if (remaining < chalk[i]) {
                return i;
            }
            remaining -= chalk[i];
        }
        return 0;
    }
}
```

## Python

```python
class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        total = sum(chalk)
        k %= total
        for i, c in enumerate(chalk):
            if k < c:
                return i
            k -= c
        # Should never reach here due to problem constraints
        return 0
```

## Python3

```python
from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        k %= total
        for i, c in enumerate(chalk):
            if k < c:
                return i
            k -= c
        # Should never reach here due to problem constraints
        return 0
```

## C

```c
int chalkReplacer(int* chalk, int chalkSize, int k) {
    long long total = 0;
    for (int i = 0; i < chalkSize; ++i) {
        total += (long long)chalk[i];
    }
    long long remaining = k % total;
    for (int i = 0; i < chalkSize; ++i) {
        if (remaining < (long long)chalk[i]) {
            return i;
        }
        remaining -= (long long)chalk[i];
    }
    return 0;
}
```

## Csharp

```csharp
public class Solution
{
    public int ChalkReplacer(int[] chalk, int k)
    {
        long total = 0;
        foreach (int c in chalk)
            total += c;

        long remaining = k % total;

        for (int i = 0; i < chalk.Length; i++)
        {
            if (remaining < chalk[i])
                return i;
            remaining -= chalk[i];
        }

        // Should never reach here due to problem constraints
        return 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} chalk
 * @param {number} k
 * @return {number}
 */
var chalkReplacer = function(chalk, k) {
    let total = 0;
    for (let v of chalk) total += v;
    k %= total;
    for (let i = 0; i < chalk.length; ++i) {
        if (k < chalk[i]) return i;
        k -= chalk[i];
    }
    return 0;
};
```

## Typescript

```typescript
function chalkReplacer(chalk: number[], k: number): number {
    let total = 0;
    for (const c of chalk) total += c;
    k %= total;
    for (let i = 0; i < chalk.length; i++) {
        if (k < chalk[i]) return i;
        k -= chalk[i];
    }
    return 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $chalk
     * @param Integer $k
     * @return Integer
     */
    function chalkReplacer($chalk, $k) {
        $total = 0;
        foreach ($chalk as $c) {
            $total += $c;
        }
        $k %= $total;

        foreach ($chalk as $i => $c) {
            if ($k < $c) {
                return $i;
            }
            $k -= $c;
        }

        // Should never reach here due to problem constraints
        return 0;
    }
}
```

## Swift

```swift
class Solution {
    func chalkReplacer(_ chalk: [Int], _ k: Int) -> Int {
        var total = 0
        for c in chalk { total += c }
        var remaining = k % total
        for (i, c) in chalk.enumerated() {
            if remaining < c {
                return i
            }
            remaining -= c
        }
        return 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun chalkReplacer(chalk: IntArray, k: Int): Int {
        var total = 0L
        for (c in chalk) {
            total += c.toLong()
        }
        var remaining = k.toLong() % total
        for (i in chalk.indices) {
            val need = chalk[i].toLong()
            if (remaining < need) return i
            remaining -= need
        }
        return 0
    }
}
```

## Dart

```dart
class Solution {
  int chalkReplacer(List<int> chalk, int k) {
    int total = 0;
    for (var c in chalk) {
      total += c;
    }
    k %= total;
    for (int i = 0; i < chalk.length; i++) {
      if (k < chalk[i]) {
        return i;
      }
      k -= chalk[i];
    }
    return 0;
  }
}
```

## Golang

```go
func chalkReplacer(chalk []int, k int) int {
    var total int64
    for _, v := range chalk {
        total += int64(v)
    }
    rem := int64(k) % total
    for i, v := range chalk {
        if rem < int64(v) {
            return i
        }
        rem -= int64(v)
    }
    return 0
}
```

## Ruby

```ruby
def chalk_replacer(chalk, k)
  total = 0
  chalk.each { |c| total += c }
  k %= total
  chalk.each_with_index do |c, i|
    return i if k < c
    k -= c
  end
end
```

## Scala

```scala
object Solution {
    def chalkReplacer(chalk: Array[Int], k: Int): Int = {
        val total: Long = chalk.foldLeft(0L){ (acc, v) => acc + v.toLong }
        var remaining: Long = k.toLong % total
        for(i <- chalk.indices){
            val need = chalk(i).toLong
            if(remaining < need) return i
            remaining -= need
        }
        0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn chalk_replacer(chalk: Vec<i32>, k: i32) -> i32 {
        let mut total: i64 = 0;
        for &c in &chalk {
            total += c as i64;
        }
        let mut remaining = (k as i64) % total;
        for (i, &c) in chalk.iter().enumerate() {
            if remaining < c as i64 {
                return i as i32;
            }
            remaining -= c as i64;
        }
        0
    }
}
```

## Racket

```racket
(define/contract (chalk-replacer chalk k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((total (foldl + 0 chalk))
         (rem   (remainder k total)))
    (let loop ((lst chalk) (idx 0) (remaining rem))
      (cond
        [(null? lst) 0] ; should never reach here
        [(< remaining (car lst)) idx]
        [else (loop (cdr lst) (+ idx 1) (- remaining (car lst)))]))))
```

## Erlang

```erlang
-module(solution).
-export([chalk_replacer/2]).

-spec chalk_replacer(Chalk :: [integer()], K :: integer()) -> integer().
chalk_replacer(Chalk, K) ->
    Sum = lists:sum(Chalk),
    Rem = K rem Sum,
    find_student(Chalk, Rem, 0).

find_student([H|_], K, Index) when K < H ->
    Index;
find_student([H|T], K, Index) ->
    find_student(T, K - H, Index + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec chalk_replacer(chalk :: [integer], k :: integer) :: integer
  def chalk_replacer(chalk, k) do
    total = Enum.reduce(chalk, 0, &+/2)
    remaining = rem(k, total)
    find_student(chalk, remaining, 0)
  end

  defp find_student([h | t], k, idx) do
    if k < h do
      idx
    else
      find_student(t, k - h, idx + 1)
    end
  end
end
```
