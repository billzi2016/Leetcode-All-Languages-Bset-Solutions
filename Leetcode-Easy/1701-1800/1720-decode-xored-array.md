# 1720. Decode XORed Array

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
        int n = encoded.size() + 1;
        vector<int> arr(n);
        arr[0] = first;
        for (int i = 0; i < (int)encoded.size(); ++i) {
            arr[i + 1] = encoded[i] ^ arr[i];
        }
        return arr;
    }
};
```

## Java

```java
class Solution {
    public int[] decode(int[] encoded, int first) {
        int n = encoded.length + 1;
        int[] arr = new int[n];
        arr[0] = first;
        for (int i = 0; i < encoded.length; i++) {
            arr[i + 1] = encoded[i] ^ arr[i];
        }
        return arr;
    }
}
```

## Python

```python
class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        arr = [first]
        for val in encoded:
            arr.append(arr[-1] ^ val)
        return arr
```

## Python3

```python
from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n = len(encoded) + 1
        arr = [0] * n
        arr[0] = first
        for i in range(len(encoded)):
            arr[i + 1] = encoded[i] ^ arr[i]
        return arr
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* decode(int* encoded, int encodedSize, int first, int* returnSize) {
    int n = encodedSize + 1;
    int* arr = (int*)malloc(n * sizeof(int));
    if (!arr) {
        *returnSize = 0;
        return NULL;
    }
    arr[0] = first;
    for (int i = 0; i < encodedSize; ++i) {
        arr[i + 1] = encoded[i] ^ arr[i];
    }
    *returnSize = n;
    return arr;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] Decode(int[] encoded, int first)
    {
        int n = encoded.Length + 1;
        int[] arr = new int[n];
        arr[0] = first;
        for (int i = 0; i < encoded.Length; i++)
        {
            arr[i + 1] = encoded[i] ^ arr[i];
        }
        return arr;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} encoded
 * @param {number} first
 * @return {number[]}
 */
var decode = function(encoded, first) {
    const n = encoded.length + 1;
    const arr = new Array(n);
    arr[0] = first;
    for (let i = 0; i < encoded.length; ++i) {
        arr[i + 1] = encoded[i] ^ arr[i];
    }
    return arr;
};
```

## Typescript

```typescript
function decode(encoded: number[], first: number): number[] {
    const n = encoded.length + 1;
    const arr = new Array<number>(n);
    arr[0] = first;
    for (let i = 0; i < encoded.length; i++) {
        arr[i + 1] = encoded[i] ^ arr[i];
    }
    return arr;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $encoded
     * @param Integer $first
     * @return Integer[]
     */
    function decode($encoded, $first) {
        $arr = [];
        $arr[] = $first;
        foreach ($encoded as $i => $val) {
            $arr[] = $val ^ $arr[$i];
        }
        return $arr;
    }
}
```

## Swift

```swift
class Solution {
    func decode(_ encoded: [Int], _ first: Int) -> [Int] {
        var arr = [first]
        var prev = first
        for e in encoded {
            let next = prev ^ e
            arr.append(next)
            prev = next
        }
        return arr
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun decode(encoded: IntArray, first: Int): IntArray {
        val n = encoded.size + 1
        val arr = IntArray(n)
        arr[0] = first
        for (i in encoded.indices) {
            arr[i + 1] = encoded[i] xor arr[i]
        }
        return arr
    }
}
```

## Dart

```dart
class Solution {
  List<int> decode(List<int> encoded, int first) {
    int n = encoded.length + 1;
    List<int> arr = List.filled(n, 0);
    arr[0] = first;
    for (int i = 0; i < encoded.length; ++i) {
      arr[i + 1] = encoded[i] ^ arr[i];
    }
    return arr;
  }
}
```

## Golang

```go
func decode(encoded []int, first int) []int {
    n := len(encoded) + 1
    arr := make([]int, n)
    arr[0] = first
    for i, v := range encoded {
        arr[i+1] = v ^ arr[i]
    }
    return arr
}
```

## Ruby

```ruby
def decode(encoded, first)
  arr = [first]
  encoded.each do |e|
    arr << (e ^ arr[-1])
  end
  arr
end
```

## Scala

```scala
object Solution {
    def decode(encoded: Array[Int], first: Int): Array[Int] = {
        val n = encoded.length + 1
        val arr = new Array[Int](n)
        arr(0) = first
        var i = 0
        while (i < encoded.length) {
            arr(i + 1) = arr(i) ^ encoded(i)
            i += 1
        }
        arr
    }
}
```

## Rust

```rust
impl Solution {
    pub fn decode(encoded: Vec<i32>, first: i32) -> Vec<i32> {
        let mut arr = Vec::with_capacity(encoded.len() + 1);
        arr.push(first);
        for i in 0..encoded.len() {
            let next = arr[i] ^ encoded[i];
            arr.push(next);
        }
        arr
    }
}
```

## Racket

```racket
(define/contract (decode encoded first)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let loop ((enc encoded) (prev first) (acc (list first)))
    (if (null? enc)
        (reverse acc)
        (let ((next (bitwise-xor (car enc) prev)))
          (loop (cdr enc) next (cons next acc))))))
```

## Erlang

```erlang
-module(solution).
-export([decode/2]).

-spec decode(Encoded :: [integer()], First :: integer()) -> [integer()].
decode(Encoded, First) ->
    lists:reverse(decode_rev(Encoded, First, [First])).

decode_rev([], _Prev, Acc) -> Acc;
decode_rev([E|Rest], Prev, Acc) ->
    Next = bxor(E, Prev),
    decode_rev(Rest, Next, [Next|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  require Bitwise

  @spec decode(encoded :: [integer], first :: integer) :: [integer]
  def decode(encoded, first) do
    {rev, _} =
      Enum.reduce(encoded, {[first], first}, fn e, {rev, prev} ->
        nxt = Bitwise.bxor(e, prev)
        {[nxt | rev], nxt}
      end)

    Enum.reverse(rev)
  end
end
```
