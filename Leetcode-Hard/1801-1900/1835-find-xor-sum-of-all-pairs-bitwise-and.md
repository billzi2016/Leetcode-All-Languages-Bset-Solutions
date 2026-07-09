# 1835. Find XOR Sum of All Pairs Bitwise AND

## Cpp

```cpp
class Solution {
public:
    int getXORSum(vector<int>& arr1, vector<int>& arr2) {
        int xor1 = 0, xor2 = 0;
        for (int v : arr1) xor1 ^= v;
        for (int v : arr2) xor2 ^= v;
        return xor1 & xor2;
    }
};
```

## Java

```java
class Solution {
    public int getXORSum(int[] arr1, int[] arr2) {
        int xor1 = 0;
        for (int num : arr1) {
            xor1 ^= num;
        }
        int xor2 = 0;
        for (int num : arr2) {
            xor2 ^= num;
        }
        return xor1 & xor2;
    }
}
```

## Python

```python
class Solution(object):
    def getXORSum(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        xor1 = 0
        for num in arr1:
            xor1 ^= num
        xor2 = 0
        for num in arr2:
            xor2 ^= num
        return xor1 & xor2
```

## Python3

```python
from typing import List

class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        xor1 = 0
        for num in arr1:
            xor1 ^= num
        xor2 = 0
        for num in arr2:
            xor2 ^= num
        return xor1 & xor2
```

## C

```c
int getXORSum(int* arr1, int arr1Size, int* arr2, int arr2Size) {
    int xor1 = 0;
    for (int i = 0; i < arr1Size; ++i) {
        xor1 ^= arr1[i];
    }
    int xor2 = 0;
    for (int i = 0; i < arr2Size; ++i) {
        xor2 ^= arr2[i];
    }
    return xor1 & xor2;
}
```

## Csharp

```csharp
public class Solution {
    public int GetXORSum(int[] arr1, int[] arr2) {
        int xor1 = 0;
        foreach (int num in arr1) {
            xor1 ^= num;
        }
        int xor2 = 0;
        foreach (int num in arr2) {
            xor2 ^= num;
        }
        return xor1 & xor2;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number}
 */
var getXORSum = function(arr1, arr2) {
    let xor1 = 0;
    for (let num of arr1) {
        xor1 ^= num;
    }
    let xor2 = 0;
    for (let num of arr2) {
        xor2 ^= num;
    }
    return xor1 & xor2;
};
```

## Typescript

```typescript
function getXORSum(arr1: number[], arr2: number[]): number {
    let xor1 = 0;
    for (const num of arr1) {
        xor1 ^= num;
    }
    let xor2 = 0;
    for (const num of arr2) {
        xor2 ^= num;
    }
    return xor1 & xor2;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @return Integer
     */
    function getXORSum($arr1, $arr2) {
        $xor1 = 0;
        foreach ($arr1 as $v) {
            $xor1 ^= $v;
        }
        $xor2 = 0;
        foreach ($arr2 as $v) {
            $xor2 ^= $v;
        }
        return $xor1 & $xor2;
    }
}
```

## Swift

```swift
class Solution {
    func getXORSum(_ arr1: [Int], _ arr2: [Int]) -> Int {
        var xor1 = 0
        for num in arr1 {
            xor1 ^= num
        }
        var xor2 = 0
        for num in arr2 {
            xor2 ^= num
        }
        return xor1 & xor2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getXORSum(arr1: IntArray, arr2: IntArray): Int {
        var xor1 = 0
        for (v in arr1) {
            xor1 = xor1 xor v
        }
        var xor2 = 0
        for (v in arr2) {
            xor2 = xor2 xor v
        }
        return xor1 and xor2
    }
}
```

## Dart

```dart
class Solution {
  int getXORSum(List<int> arr1, List<int> arr2) {
    int xor1 = 0;
    for (var v in arr1) {
      xor1 ^= v;
    }
    int xor2 = 0;
    for (var v in arr2) {
      xor2 ^= v;
    }
    return xor1 & xor2;
  }
}
```

## Golang

```go
func getXORSum(arr1 []int, arr2 []int) int {
	xor1 := 0
	for _, v := range arr1 {
		xor1 ^= v
	}
	xor2 := 0
	for _, v := range arr2 {
		xor2 ^= v
	}
	return xor1 & xor2
}
```

## Ruby

```ruby
def get_xor_sum(arr1, arr2)
  xor1 = 0
  arr1.each { |v| xor1 ^= v }
  xor2 = 0
  arr2.each { |v| xor2 ^= v }
  xor1 & xor2
end
```

## Scala

```scala
object Solution {
    def getXORSum(arr1: Array[Int], arr2: Array[Int]): Int = {
        var xor1 = 0
        for (v <- arr1) xor1 ^= v
        var xor2 = 0
        for (v <- arr2) xor2 ^= v
        xor1 & xor2
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_xor_sum(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        let mut xor1 = 0i32;
        for v in arr1 {
            xor1 ^= v;
        }
        let mut xor2 = 0i32;
        for v in arr2 {
            xor2 ^= v;
        }
        xor1 & xor2
    }
}
```

## Racket

```racket
(define/contract (get-xor-sum arr1 arr2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((xor1 (foldl bitwise-xor 0 arr1))
         (xor2 (foldl bitwise-xor 0 arr2)))
    (bitwise-and xor1 xor2)))
```

## Erlang

```erlang
-module(solution).
-export([get_xor_sum/2]).

-spec get_xor_sum(Arr1 :: [integer()], Arr2 :: [integer()]) -> integer().
get_xor_sum(Arr1, Arr2) ->
    Xor1 = lists:foldl(fun (X, Acc) -> X bxor Acc end, 0, Arr1),
    Xor2 = lists:foldl(fun (Y, Acc) -> Y bxor Acc end, 0, Arr2),
    Xor1 band Xor2.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_xor_sum(arr1 :: [integer], arr2 :: [integer]) :: integer
  def get_xor_sum(arr1, arr2) do
    xor1 = Enum.reduce(arr1, 0, fn x, acc -> Bitwise.bxor(acc, x) end)
    xor2 = Enum.reduce(arr2, 0, fn x, acc -> Bitwise.bxor(acc, x) end)
    Bitwise.band(xor1, xor2)
  end
end
```
