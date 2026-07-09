# 0089. Gray Code

## Cpp

```cpp
class Solution {
public:
    vector<int> grayCode(int n) {
        int total = 1 << n;
        vector<int> res(total);
        for (int i = 0; i < total; ++i) {
            res[i] = i ^ (i >> 1);
        }
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> grayCode(int n) {
        int total = 1 << n;
        List<Integer> result = new ArrayList<>(total);
        for (int i = 0; i < total; i++) {
            result.add(i ^ (i >> 1));
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        total = 1 << n
        return [i ^ (i >> 1) for i in range(total)]
```

## Python3

```python
from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        total = 1 << n
        return [i ^ (i >> 1) for i in range(total)]
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* grayCode(int n, int* returnSize) {
    int total = 1 << n;
    int* res = (int*)malloc(total * sizeof(int));
    for (int i = 0; i < total; ++i) {
        res[i] = i ^ (i >> 1);
    }
    *returnSize = total;
    return res;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<int> GrayCode(int n) {
        int total = 1 << n;
        List<int> result = new List<int>(total);
        for (int i = 0; i < total; i++) {
            result.Add(i ^ (i >> 1));
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number[]}
 */
var grayCode = function(n) {
    const total = 1 << n;
    const result = new Array(total);
    for (let i = 0; i < total; ++i) {
        result[i] = i ^ (i >> 1);
    }
    return result;
};
```

## Typescript

```typescript
function grayCode(n: number): number[] {
    const total = 1 << n;
    const result = new Array<number>(total);
    for (let i = 0; i < total; i++) {
        result[i] = i ^ (i >> 1);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer[]
     */
    function grayCode($n) {
        $result = [];
        $total = 1 << $n;
        for ($i = 0; $i < $total; $i++) {
            $result[] = $i ^ ($i >> 1);
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func grayCode(_ n: Int) -> [Int] {
        let total = 1 << n
        var result = [Int]()
        result.reserveCapacity(total)
        for i in 0..<total {
            result.append(i ^ (i >> 1))
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun grayCode(n: Int): List<Int> {
        val size = 1 shl n
        val result = ArrayList<Int>(size)
        for (i in 0 until size) {
            result.add(i xor (i shr 1))
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> grayCode(int n) {
    int total = 1 << n;
    List<int> res = List.filled(total, 0);
    for (int i = 0; i < total; ++i) {
      res[i] = i ^ (i >> 1);
    }
    return res;
  }
}
```

## Golang

```go
func grayCode(n int) []int {
	size := 1 << n
	res := make([]int, size)
	for i := 0; i < size; i++ {
		res[i] = i ^ (i >> 1)
	}
	return res
}
```

## Ruby

```ruby
def gray_code(n)
  total = 1 << n
  (0...total).map { |i| i ^ (i >> 1) }
end
```

## Scala

```scala
object Solution {
    def grayCode(n: Int): List[Int] = {
        val total = 1 << n
        (0 until total).map(i => i ^ (i >> 1)).toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn gray_code(n: i32) -> Vec<i32> {
        let n = n as u32;
        let total = 1usize << n;
        let mut res = Vec::with_capacity(total);
        for i in 0..total {
            let gray = (i as u32) ^ ((i as u32) >> 1);
            res.push(gray as i32);
        }
        res
    }
}
```

## Racket

```racket
(define/contract (gray-code n)
  (-> exact-integer? (listof exact-integer?))
  (let* ((total (expt 2 n)))
    (for/list ([i (in-range total)])
      (bitwise-xor i (arithmetic-shift i -1)))))
```

## Erlang

```erlang
-module(solution).
-export([gray_code/1]).

-spec gray_code(N :: integer()) -> [integer()].
gray_code(N) when N >= 0 ->
    Size = 1 bsl N,
    [I bxor (I bsr 1) || I <- lists:seq(0, Size - 1)].
```

## Elixir

```elixir
defmodule Solution do
  @spec gray_code(n :: integer) :: [integer]
  def gray_code(n) when n >= 0 do
    limit = 1 <<< n
    Enum.map(0..limit - 1, fn i ->
      Bitwise.bxor(i, Bitwise.bsr(i, 1))
    end)
  end
end
```
