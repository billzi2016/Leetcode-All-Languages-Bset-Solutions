# 1250. Check If It Is a Good Array

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isGoodArray(vector<int>& nums) {
        int g = nums[0];
        for (size_t i = 1; i < nums.size(); ++i) {
            g = std::gcd(g, nums[i]);
            if (g == 1) return true;
        }
        return g == 1;
    }
};
```

## Java

```java
class Solution {
    public boolean isGoodArray(int[] nums) {
        int g = 0;
        for (int num : nums) {
            g = gcd(g, num);
            if (g == 1) return true;
        }
        return g == 1;
    }
    
    private int gcd(int a, int b) {
        while (b != 0) {
            int tmp = a % b;
            a = b;
            b = tmp;
        }
        return Math.abs(a);
    }
}
```

## Python

```python
import math

class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        g = 0
        for v in nums:
            g = math.gcd(g, v)
            if g == 1:
                return True
        return g == 1
```

## Python3

```python
from typing import List
import math

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        g = 0
        for num in nums:
            g = math.gcd(g, num)
            if g == 1:
                return True
        return g == 1
```

## C

```c
#include <stdbool.h>

static int gcd_int(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

bool isGoodArray(int* nums, int numsSize) {
    if (numsSize == 0) return false;
    int g = 0;
    for (int i = 0; i < numsSize; ++i) {
        g = gcd_int(g, nums[i]);
        if (g == 1) break;
    }
    return g == 1;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsGoodArray(int[] nums)
    {
        int g = nums[0];
        for (int i = 1; i < nums.Length; i++)
        {
            g = Gcd(g, nums[i]);
            if (g == 1) return true;
        }
        return g == 1;
    }

    private int Gcd(int a, int b)
    {
        while (b != 0)
        {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return Math.Abs(a);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isGoodArray = function(nums) {
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return Math.abs(a);
    };
    
    let g = nums[0];
    for (let i = 1; i < nums.length && g !== 1; ++i) {
        g = gcd(g, nums[i]);
    }
    return g === 1;
};
```

## Typescript

```typescript
function isGoodArray(nums: number[]): boolean {
    const gcd = (a: number, b: number): number => {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    
    let g = nums[0];
    for (let i = 1; i < nums.length; i++) {
        g = gcd(g, nums[i]);
        if (g === 1) return true;
    }
    return g === 1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function isGoodArray($nums) {
        $g = 0;
        foreach ($nums as $num) {
            $g = $this->gcd($g, $num);
            if ($g == 1) {
                return true;
            }
        }
        return $g === 1;
    }

    private function gcd($a, $b) {
        while ($b != 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return abs($a);
    }
}
```

## Swift

```swift
class Solution {
    func isGoodArray(_ nums: [Int]) -> Bool {
        var currentGCD = 0
        for num in nums {
            currentGCD = gcd(currentGCD, num)
            if currentGCD == 1 { return true }
        }
        return currentGCD == 1
    }
    
    private func gcd(_ a: Int, _ b: Int) -> Int {
        var x = a
        var y = b
        while y != 0 {
            let temp = x % y
            x = y
            y = temp
        }
        return abs(x)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isGoodArray(nums: IntArray): Boolean {
        var g = nums[0]
        for (i in 1 until nums.size) {
            g = gcd(g, nums[i])
            if (g == 1) return true
        }
        return g == 1
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val tmp = x % y
            x = y
            y = tmp
        }
        return kotlin.math.abs(x)
    }
}
```

## Dart

```dart
class Solution {
  bool isGoodArray(List<int> nums) {
    if (nums.isEmpty) return false;
    int g = nums[0].abs();
    for (int i = 1; i < nums.length; i++) {
      g = _gcd(g, nums[i].abs());
      if (g == 1) break; // early exit
    }
    return g == 1;
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      int temp = a % b;
      a = b;
      b = temp;
    }
    return a.abs();
  }
}
```

## Golang

```go
func isGoodArray(nums []int) bool {
	if len(nums) == 0 {
		return false
	}
	g := nums[0]
	for _, v := range nums[1:] {
		a, b := g, v
		for b != 0 {
			a, b = b, a%b
		}
		g = a
		if g == 1 {
			return true
		}
	}
	return g == 1
}
```

## Ruby

```ruby
def is_good_array(nums)
  g = nums.reduce(0) { |acc, x| acc.gcd(x) }
  g == 1
end
```

## Scala

```scala
object Solution {
    def isGoodArray(nums: Array[Int]): Boolean = {
        @annotation.tailrec
        def gcd(a: Int, b: Int): Int = {
            if (b == 0) math.abs(a)
            else gcd(b, a % b)
        }

        var g = nums(0)
        var i = 1
        while (i < nums.length && g != 1) {
            g = gcd(g, nums(i))
            i += 1
        }
        g == 1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_good_array(nums: Vec<i32>) -> bool {
        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a.abs()
        }

        let mut g = 0;
        for &num in nums.iter() {
            g = if g == 0 { num } else { gcd(g, num) };
            if g == 1 {
                return true;
            }
        }
        g == 1
    }
}
```

## Racket

```racket
(define/contract (is-good-array nums)
  (-> (listof exact-integer?) boolean?)
  (let loop ((lst nums) (g 0))
    (if (null? lst)
        (= g 1)
        (loop (cdr lst) (gcd g (car lst))))))
```

## Erlang

```erlang
-module(solution).
-export([is_good_array/1]).

-spec is_good_array(Nums :: [integer()]) -> boolean().
is_good_array(Nums) ->
    G = lists:foldl(fun(N, Acc) -> gcd(Acc, N) end, 0, Nums),
    G == 1.

gcd(A, B) when B =:= 0 -> A;
gcd(A, B) -> gcd(B, A rem B).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_good_array(nums :: [integer]) :: boolean
  def is_good_array(nums) do
    Enum.reduce(nums, 0, fn x, acc -> Integer.gcd(acc, x) end) == 1
  end
end
```
