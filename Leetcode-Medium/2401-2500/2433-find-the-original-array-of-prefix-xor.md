# 2433. Find The Original Array of Prefix Xor

## Cpp

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        int n = pref.size();
        vector<int> arr(n);
        if (n == 0) return arr;
        arr[0] = pref[0];
        for (int i = 1; i < n; ++i) {
            arr[i] = pref[i] ^ pref[i - 1];
        }
        return arr;
    }
};
```

## Java

```java
class Solution {
    public int[] findArray(int[] pref) {
        int n = pref.length;
        int[] arr = new int[n];
        if (n == 0) return arr;
        arr[0] = pref[0];
        for (int i = 1; i < n; i++) {
            arr[i] = pref[i] ^ pref[i - 1];
        }
        return arr;
    }
}
```

## Python

```python
class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        n = len(pref)
        if n == 0:
            return []
        arr = [0] * n
        arr[0] = pref[0]
        for i in range(1, n):
            arr[i] = pref[i] ^ pref[i - 1]
        return arr
```

## Python3

```python
from typing import List

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        if n == 0:
            return []
        arr = [pref[0]]
        for i in range(1, n):
            arr.append(pref[i] ^ pref[i - 1])
        return arr
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findArray(int* pref, int prefSize, int* returnSize) {
    int* arr = (int*)malloc(sizeof(int) * prefSize);
    if (!arr) {
        *returnSize = 0;
        return NULL;
    }
    if (prefSize > 0) {
        arr[0] = pref[0];
        for (int i = 1; i < prefSize; ++i) {
            arr[i] = pref[i] ^ pref[i - 1];
        }
    }
    *returnSize = prefSize;
    return arr;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] FindArray(int[] pref)
    {
        int n = pref.Length;
        int[] arr = new int[n];
        if (n == 0) return arr;

        arr[0] = pref[0];
        for (int i = 1; i < n; i++)
        {
            arr[i] = pref[i] ^ pref[i - 1];
        }
        return arr;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} pref
 * @return {number[]}
 */
var findArray = function(pref) {
    const n = pref.length;
    const arr = new Array(n);
    if (n === 0) return arr;
    arr[0] = pref[0];
    for (let i = 1; i < n; ++i) {
        arr[i] = pref[i] ^ pref[i - 1];
    }
    return arr;
};
```

## Typescript

```typescript
function findArray(pref: number[]): number[] {
    const n = pref.length;
    const arr = new Array<number>(n);
    if (n === 0) return arr;
    arr[0] = pref[0];
    for (let i = 1; i < n; i++) {
        arr[i] = pref[i] ^ pref[i - 1];
    }
    return arr;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $pref
     * @return Integer[]
     */
    function findArray($pref) {
        $n = count($pref);
        $arr = [];
        if ($n === 0) {
            return $arr;
        }
        $arr[0] = $pref[0];
        for ($i = 1; $i < $n; $i++) {
            $arr[$i] = $pref[$i] ^ $pref[$i - 1];
        }
        return $arr;
    }
}
```

## Swift

```swift
class Solution {
    func findArray(_ pref: [Int]) -> [Int] {
        let n = pref.count
        guard n > 0 else { return [] }
        var arr = Array(repeating: 0, count: n)
        arr[0] = pref[0]
        for i in 1..<n {
            arr[i] = pref[i] ^ pref[i - 1]
        }
        return arr
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findArray(pref: IntArray): IntArray {
        val n = pref.size
        val arr = IntArray(n)
        if (n == 0) return arr
        arr[0] = pref[0]
        for (i in 1 until n) {
            arr[i] = pref[i] xor pref[i - 1]
        }
        return arr
    }
}
```

## Dart

```dart
class Solution {
  List<int> findArray(List<int> pref) {
    int n = pref.length;
    List<int> arr = List.filled(n, 0);
    if (n == 0) return arr;
    arr[0] = pref[0];
    for (int i = 1; i < n; i++) {
      arr[i] = pref[i] ^ pref[i - 1];
    }
    return arr;
  }
}
```

## Golang

```go
func findArray(pref []int) []int {
    n := len(pref)
    arr := make([]int, n)
    if n == 0 {
        return arr
    }
    arr[0] = pref[0]
    for i := 1; i < n; i++ {
        arr[i] = pref[i] ^ pref[i-1]
    }
    return arr
}
```

## Ruby

```ruby
def find_array(pref)
  n = pref.length
  return [] if n == 0
  arr = Array.new(n)
  arr[0] = pref[0]
  (1...n).each do |i|
    arr[i] = pref[i] ^ pref[i - 1]
  end
  arr
end
```

## Scala

```scala
object Solution {
    def findArray(pref: Array[Int]): Array[Int] = {
        val n = pref.length
        val arr = new Array[Int](n)
        if (n == 0) return arr
        arr(0) = pref(0)
        var i = 1
        while (i < n) {
            arr(i) = pref(i) ^ pref(i - 1)
            i += 1
        }
        arr
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_array(pref: Vec<i32>) -> Vec<i32> {
        let n = pref.len();
        if n == 0 {
            return Vec::new();
        }
        let mut arr = Vec::with_capacity(n);
        arr.push(pref[0]);
        for i in 1..n {
            arr.push(pref[i] ^ pref[i - 1]);
        }
        arr
    }
}
```

## Racket

```racket
(define/contract (find-array pref)
  (-> (listof exact-integer?) (listof exact-integer?))
  (if (null? pref)
      '()
      (let loop ((prev (car pref))
                 (rest (cdr pref))
                 (acc (list (car pref))))
        (if (null? rest)
            (reverse acc)
            (let* ((curr (car rest))
                   (val (bitwise-xor curr prev)))
              (loop curr (cdr rest) (cons val acc)))))))
```

## Erlang

```erlang
-spec find_array(Pref :: [integer()]) -> [integer()].
find_array([]) ->
    [];
find_array([H|T]) ->
    lists:reverse(find_array(T, H, [H])).

find_array([], _Prev, Acc) ->
    Acc;
find_array([Curr|Rest], Prev, Acc) ->
    Val = Curr bxor Prev,
    find_array(Rest, Curr, [Val | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_array(pref :: [integer]) :: [integer]
  def find_array(pref) do
    require Bitwise

    {rev, _} =
      Enum.reduce(pref, {[], nil}, fn cur, {acc, prev} ->
        val = if prev == nil, do: cur, else: Bitwise.bxor(cur, prev)
        {[val | acc], cur}
      end)

    Enum.reverse(rev)
  end
end
```
