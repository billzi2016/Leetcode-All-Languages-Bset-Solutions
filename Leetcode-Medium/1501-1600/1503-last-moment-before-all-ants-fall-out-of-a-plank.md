# 1503. Last Moment Before All Ants Fall Out of a Plank

## Cpp

```cpp
class Solution {
public:
    int getLastMoment(int n, vector<int>& left, vector<int>& right) {
        int ans = 0;
        for (int pos : left) {
            ans = max(ans, pos);
        }
        for (int pos : right) {
            ans = max(ans, n - pos);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int getLastMoment(int n, int[] left, int[] right) {
        int ans = 0;
        for (int pos : left) {
            if (pos > ans) ans = pos;
        }
        for (int pos : right) {
            int time = n - pos;
            if (time > ans) ans = time;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        ans = 0
        for pos in left:
            if pos > ans:
                ans = pos
        for pos in right:
            time = n - pos
            if time > ans:
                ans = time
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = 0
        for pos in left:
            if pos > ans:
                ans = pos
        for pos in right:
            time = n - pos
            if time > ans:
                ans = time
        return ans
```

## C

```c
int getLastMoment(int n, int* left, int leftSize, int* right, int rightSize) {
    int ans = 0;
    for (int i = 0; i < leftSize; ++i) {
        if (left[i] > ans) ans = left[i];
    }
    for (int i = 0; i < rightSize; ++i) {
        int t = n - right[i];
        if (t > ans) ans = t;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int GetLastMoment(int n, int[] left, int[] right) {
        int ans = 0;
        foreach (int pos in left) {
            if (pos > ans) ans = pos;
        }
        foreach (int pos in right) {
            int time = n - pos;
            if (time > ans) ans = time;
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[]} left
 * @param {number[]} right
 * @return {number}
 */
var getLastMoment = function(n, left, right) {
    let ans = 0;
    for (let pos of left) {
        if (pos > ans) ans = pos;
    }
    for (let pos of right) {
        const time = n - pos;
        if (time > ans) ans = time;
    }
    return ans;
};
```

## Typescript

```typescript
function getLastMoment(n: number, left: number[], right: number[]): number {
    let ans = 0;
    for (const pos of left) {
        if (pos > ans) ans = pos;
    }
    for (const pos of right) {
        const time = n - pos;
        if (time > ans) ans = time;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $left
     * @param Integer[] $right
     * @return Integer
     */
    function getLastMoment($n, $left, $right) {
        $ans = 0;
        foreach ($left as $pos) {
            if ($pos > $ans) {
                $ans = $pos;
            }
        }
        foreach ($right as $pos) {
            $time = $n - $pos;
            if ($time > $ans) {
                $ans = $time;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func getLastMoment(_ n: Int, _ left: [Int], _ right: [Int]) -> Int {
        var ans = 0
        for pos in left {
            if pos > ans { ans = pos }
        }
        for pos in right {
            let t = n - pos
            if t > ans { ans = t }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getLastMoment(n: Int, left: IntArray, right: IntArray): Int {
        var ans = 0
        for (pos in left) {
            if (pos > ans) ans = pos
        }
        for (pos in right) {
            val t = n - pos
            if (t > ans) ans = t
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int getLastMoment(int n, List<int> left, List<int> right) {
    int ans = 0;
    for (int pos in left) {
      if (pos > ans) ans = pos;
    }
    for (int pos in right) {
      int time = n - pos;
      if (time > ans) ans = time;
    }
    return ans;
  }
}
```

## Golang

```go
func getLastMoment(n int, left []int, right []int) int {
    ans := 0
    for _, p := range left {
        if p > ans {
            ans = p
        }
    }
    for _, p := range right {
        if n-p > ans {
            ans = n - p
        }
    }
    return ans
}
```

## Ruby

```ruby
def get_last_moment(n, left, right)
  ans = 0
  left.each { |pos| ans = pos if pos > ans }
  right.each { |pos| time = n - pos; ans = time if time > ans }
  ans
end
```

## Scala

```scala
object Solution {
    def getLastMoment(n: Int, left: Array[Int], right: Array[Int]): Int = {
        var ans = 0
        for (pos <- left) {
            if (pos > ans) ans = pos
        }
        for (pos <- right) {
            val t = n - pos
            if (t > ans) ans = t
        }
        ans
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn get_last_moment(n: i32, left: Vec<i32>, right: Vec<i32>) -> i32 {
        let mut ans = 0;
        for &pos in &left {
            if pos > ans {
                ans = pos;
            }
        }
        for &pos in &right {
            let t = n - pos;
            if t > ans {
                ans = t;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (get-last-moment n left right)
  (-> exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((max-left (if (null? left) 0 (apply max left)))
         (max-right (if (null? right)
                        0
                        (apply max (map (lambda (x) (- n x)) right))))
         (ans (max max-left max-right)))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([get_last_moment/3]).

-spec get_last_moment(N :: integer(), Left :: [integer()], Right :: [integer()]) -> integer().
get_last_moment(N, Left, Right) ->
    MaxLeft = case Left of
        [] -> 0;
        _ -> lists:max(Left)
    end,
    MaxRight = case Right of
        [] -> 0;
        _ -> lists:max([N - X || X <- Right])
    end,
    erlang:max(MaxLeft, MaxRight).
```

## Elixir

```elixir
defmodule Solution do
  @spec get_last_moment(n :: integer, left :: [integer], right :: [integer]) :: integer
  def get_last_moment(n, left, right) do
    max_left = Enum.reduce(left, 0, fn pos, acc -> if pos > acc, do: pos, else: acc end)
    max_right = Enum.reduce(right, 0, fn pos, acc ->
      time = n - pos
      if time > acc, do: time, else: acc
    end)

    if max_left > max_right, do: max_left, else: max_right
  end
end
```
