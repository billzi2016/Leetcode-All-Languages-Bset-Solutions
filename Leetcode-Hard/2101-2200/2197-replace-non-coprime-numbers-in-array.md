# 2197. Replace Non-Coprime Numbers in Array

## Cpp

```cpp
class Solution {
public:
    vector<int> replaceNonCoprimes(vector<int>& nums) {
        vector<long long> st;
        for (int v : nums) {
            st.push_back(v);
            while (st.size() >= 2) {
                long long b = st.back();
                long long a = st[st.size() - 2];
                long long g = std::gcd(a, b);
                if (g == 1) break;
                long long lcm = a / g * b;
                st.pop_back();          // remove b
                st.back() = lcm;        // replace a with lcm
            }
        vector<int> ans(st.size());
        for (size_t i = 0; i < st.size(); ++i) ans[i] = static_cast<int>(st[i]);
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> replaceNonCoprimes(int[] nums) {
        Deque<Integer> stack = new ArrayDeque<>();
        for (int num : nums) {
            int cur = num;
            while (!stack.isEmpty()) {
                int prev = stack.peekLast();
                long g = gcd(prev, cur);
                if (g == 1) break;
                stack.pollLast(); // pop
                cur = (int) ((long) prev / g * cur); // lcm
            }
            stack.addLast(cur);
        }
        return new ArrayList<>(stack);
    }

    private long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Python

```python
class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from math import gcd
        stack = []
        for x in nums:
            stack.append(x)
            while len(stack) >= 2:
                b = stack[-1]
                a = stack[-2]
                g = gcd(a, b)
                if g > 1:
                    lcm = a // g * b
                    stack.pop()
                    stack.pop()
                    stack.append(lcm)
                else:
                    break
        return stack
```

## Python3

```python
class Solution:
    def replaceNonCoprimes(self, nums):
        import math
        stack = []
        for x in nums:
            stack.append(x)
            while len(stack) >= 2:
                a = stack[-2]
                b = stack[-1]
                g = math.gcd(a, b)
                if g == 1:
                    break
                lcm = a // g * b
                stack.pop()
                stack[-1] = lcm
        return stack
```

## C

```c
#include <stdlib.h>

static int gcd_int(long long a, long long b) {
    while (b) {
        long long t = a % b;
        a = b;
        b = t;
    }
    return (int)a;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* replaceNonCoprimes(int* nums, int numsSize, int* returnSize) {
    if (!nums || numsSize == 0) {
        *returnSize = 0;
        return NULL;
    }
    
    int *stack = (int *)malloc(numsSize * sizeof(int));
    int sz = 0;
    
    for (int i = 0; i < numsSize; ++i) {
        stack[sz++] = nums[i];
        while (sz >= 2) {
            int a = stack[sz - 2];
            int b = stack[sz - 1];
            int g = gcd_int(a, b);
            if (g == 1) break;
            long long lcm = ((long long)a / g) * b; // fits in 64-bit
            stack[sz - 2] = (int)lcm;
            sz--; // remove top element
        }
    }
    
    int *res = (int *)malloc(sz * sizeof(int));
    for (int i = 0; i < sz; ++i) res[i] = stack[i];
    free(stack);
    
    *returnSize = sz;
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<int> ReplaceNonCoprimes(int[] nums)
    {
        var stack = new System.Collections.Generic.List<int>();
        foreach (var num in nums)
        {
            stack.Add(num);
            while (stack.Count >= 2)
            {
                int b = stack[stack.Count - 1];
                int a = stack[stack.Count - 2];
                int g = Gcd(a, b);
                if (g == 1) break;
                long lcm = ((long)a / g) * b; // safe multiplication
                stack.RemoveAt(stack.Count - 1);
                stack[stack.Count - 1] = (int)lcm;
            }
        }
        return stack;
    }

    private int Gcd(int a, int b)
    {
        while (b != 0)
        {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var replaceNonCoprimes = function(nums) {
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    
    const stack = [];
    for (let num of nums) {
        stack.push(num);
        while (stack.length >= 2) {
            const y = stack[stack.length - 1];
            const x = stack[stack.length - 2];
            const g = gcd(x, y);
            if (g > 1) {
                const lcm = (x / g) * y;
                stack.pop();               // remove y
                stack[stack.length - 1] = lcm; // replace x with lcm
            } else {
                break;
            }
        }
    }
    return stack;
};
```

## Typescript

```typescript
function replaceNonCoprimes(nums: number[]): number[] {
    const stack: number[] = [];
    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    for (const val of nums) {
        let cur = val;
        while (stack.length > 0) {
            const prev = stack[stack.length - 1];
            const g = gcd(prev, cur);
            if (g === 1) break;
            cur = (prev / g) * cur; // LCM
            stack.pop();
        }
        stack.push(cur);
    }
    return stack;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function replaceNonCoprimes($nums) {
        $stack = [];
        foreach ($nums as $num) {
            $cur = $num;
            while (!empty($stack)) {
                $top = $stack[count($stack) - 1];
                $g = $this->gcd($top, $cur);
                if ($g > 1) {
                    array_pop($stack);
                    // lcm = top / g * cur
                    $cur = intdiv($top, $g) * $cur;
                } else {
                    break;
                }
            }
            $stack[] = $cur;
        }
        return $stack;
    }

    private function gcd(int $a, int $b): int {
        while ($b != 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return $a;
    }
}
```

## Swift

```swift
class Solution {
    func replaceNonCoprimes(_ nums: [Int]) -> [Int] {
        var stack = [Int]()
        
        func gcd(_ a: Int, _ b: Int) -> Int {
            var x = a
            var y = b
            while y != 0 {
                let temp = x % y
                x = y
                y = temp
            }
            return x
        }
        
        for num in nums {
            var cur = num
            while let last = stack.last {
                let g = gcd(last, cur)
                if g == 1 { break }
                // compute LCM safely using Int64
                let lcm = Int((Int64(last) / Int64(g)) * Int64(cur))
                stack.removeLast()
                cur = lcm
            }
            stack.append(cur)
        }
        
        return stack
    }
}
```

## Kotlin

```kotlin
class Solution {
    private fun gcd(a: Long, b: Long): Long {
        var x = a
        var y = b
        while (y != 0L) {
            val t = x % y
            x = y
            y = t
        }
        return x
    }

    fun replaceNonCoprimes(nums: IntArray): List<Int> {
        val stack = java.util.ArrayList<Long>()
        for (num in nums) {
            stack.add(num.toLong())
            while (stack.size >= 2) {
                val b = stack[stack.size - 1]
                val a = stack[stack.size - 2]
                val g = gcd(a, b)
                if (g == 1L) break
                val lcm = a / g * b
                stack.removeAt(stack.size - 1)
                stack[stack.size - 1] = lcm
            }
        }
        return stack.map { it.toInt() }
    }
}
```

## Dart

```dart
class Solution {
  int _gcd(int a, int b) {
    while (b != 0) {
      int t = a % b;
      a = b;
      b = t;
    }
    return a;
  }

  List<int> replaceNonCoprimes(List<int> nums) {
    List<int> stack = [];
    for (int x in nums) {
      stack.add(x);
      while (stack.length >= 2) {
        int y = stack[stack.length - 2];
        int z = stack[stack.length - 1];
        int g = _gcd(y, z);
        if (g == 1) break;
        int lcm = (y ~/ g) * z;
        stack.removeLast();
        stack[stack.length - 1] = lcm;
      }
    }
    return stack;
  }
}
```

## Golang

```go
func replaceNonCoprimes(nums []int) []int {
    stack := make([]int, 0, len(nums))
    for _, v := range nums {
        cur := v
        for len(stack) > 0 {
            top := stack[len(stack)-1]
            g := gcd(top, cur)
            if g == 1 {
                break
            }
            // merge into LCM
            lcm := int(int64(top)/int64(g) * int64(cur))
            stack = stack[:len(stack)-1]
            cur = lcm
        }
        stack = append(stack, cur)
    }
    return stack
}

func gcd(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}
```

## Ruby

```ruby
def replace_non_coprimes(nums)
  stack = []
  nums.each do |x|
    stack << x
    while stack.size >= 2
      a = stack[-2]
      b = stack[-1]
      g = a.gcd(b)
      break if g == 1
      lcm = (a / g) * b
      stack.pop
      stack.pop
      stack << lcm
    end
  end
  stack
end
```

## Scala

```scala
object Solution {
    def replaceNonCoprimes(nums: Array[Int]): List[Int] = {
        val stack = new scala.collection.mutable.ArrayBuffer[Long]()
        def gcd(a: Long, b: Long): Long = {
            var x = a
            var y = b
            while (y != 0) {
                val t = x % y
                x = y
                y = t
            }
            x
        }
        for (num <- nums) {
            var cur = num.toLong
            var keepMerging = true
            while (keepMerging && stack.nonEmpty) {
                val top = stack.last
                val g = gcd(top, cur)
                if (g > 1) {
                    cur = (top / g) * cur // lcm
                    stack.remove(stack.size - 1)
                } else {
                    keepMerging = false
                }
            }
            stack.append(cur)
        }
        stack.map(_.toInt).toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn replace_non_coprimes(nums: Vec<i32>) -> Vec<i32> {
        fn gcd(mut a: i64, mut b: i64) -> i64 {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a.abs()
        }

        let mut stack: Vec<i64> = Vec::new();

        for num in nums {
            let mut cur = num as i64;
            while let Some(&last) = stack.last() {
                let g = gcd(last, cur);
                if g > 1 {
                    stack.pop();
                    // lcm = a / g * b
                    cur = last / g * cur;
                } else {
                    break;
                }
            }
            stack.push(cur);
        }

        stack.into_iter().map(|x| x as i32).collect()
    }
}
```

## Racket

```racket
(define/contract (replace-non-coprimes nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (define (gcd a b)
    (if (= b 0) a (gcd b (remainder a b))))
  (define (lcm a b)
    (/ (* a b) (gcd a b)))
  (let loop ((rest nums) (stack '()))
    (if (null? rest)
        (reverse stack)
        (let* ((x (car rest))
               (new-stack
                (let recur ((cur x) (stk stack))
                  (if (and (pair? stk)
                           (> (gcd cur (car stk)) 1))
                      (recur (lcm cur (car stk)) (cdr stk))
                      (cons cur stk)))))
          (loop (cdr rest) new-stack))))
```

## Erlang

```erlang
-spec replace_non_coprimes([integer()]) -> [integer()].
replace_non_coprimes(Nums) ->
    FinalStack = process(Nums, []),
    lists:reverse(FinalStack).

process([], Stack) -> Stack;
process([H|T], Stack) ->
    NewStack = push_and_merge(H, Stack),
    process(T, NewStack).

push_and_merge(X, []) -> [X];
push_and_merge(X, [Top|Rest]) ->
    G = gcd(X, Top),
    if
        G > 1 ->
            L = (X div G) * Top,
            push_and_merge(L, Rest);
        true ->
            [X, Top | Rest]
    end.

gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).
```

## Elixir

```elixir
defmodule Solution do
  @spec replace_non_coprimes(nums :: [integer]) :: [integer]
  def replace_non_coprimes(nums) do
    nums
    |> Enum.reduce([], fn x, acc -> merge([x | acc]) end)
    |> Enum.reverse()
  end

  defp merge([b, a | rest]) do
    g = gcd(a, b)

    if g > 1 do
      l = div(a, g) * b
      merge([l | rest])
    else
      [b, a | rest]
    end
  end

  defp merge(stack), do: stack

  defp gcd(a, 0), do: a
  defp gcd(a, b), do: gcd(b, rem(a, b))
end
```
