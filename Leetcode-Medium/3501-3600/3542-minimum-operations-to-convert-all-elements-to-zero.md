# 3542. Minimum Operations to Convert All Elements to Zero

## Cpp

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums) {
        vector<int> st;
        int ans = 0;
        for (int x : nums) {
            if (x == 0) continue;
            while (!st.empty() && st.back() > x) st.pop_back();
            if (!st.empty() && st.back() == x) continue;
            st.push_back(x);
            ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minOperations(int[] nums) {
        java.util.ArrayDeque<Integer> stack = new java.util.ArrayDeque<>();
        stack.push(0); // sentinel
        int ans = 0;
        for (int x : nums) {
            while (!stack.isEmpty() && stack.peek() > x) {
                stack.pop();
            }
            if (x != 0 && stack.peek() < x) {
                ans++;
                stack.push(x);
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        ans = 0
        for x in nums:
            if x == 0:
                # zero acts as barrier; finish all pending higher values
                while stack:
                    ans += 1
                    stack.pop()
                continue
            # pop larger values that cannot cross current smaller value
            while stack and stack[-1] > x:
                ans += 1
                stack.pop()
            if not stack or stack[-1] < x:
                stack.append(x)
            # if equal, do nothing (same segment)
        ans += len(stack)
        return ans
```

## Python3

```python
import sys
from collections import defaultdict

class Solution:
    def minOperations(self, nums):
        n = len(nums)
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            if v > 0:
                pos[v].append(i)

        bit = [0] * (n + 2)

        def add(idx, val):
            idx += 1
            while idx <= n:
                bit[idx] += val
                idx += idx & -idx

        def prefix(idx):
            idx += 1
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & -idx
            return s

        def range_sum(l, r):
            if l > r:
                return 0
            return prefix(r) - (prefix(l - 1) if l > 0 else 0)

        for i, v in enumerate(nums):
            if v == 0:
                add(i, 1)

        ans = 0
        for value in sorted(pos.keys()):
            indices = pos[value]
            seg = 0
            prev = -1
            for idx in indices:
                if seg == 0:
                    seg = 1
                else:
                    if range_sum(prev + 1, idx - 1) > 0:
                        seg += 1
                prev = idx
            ans += seg
            for idx in indices:
                add(idx, 1)

        return ans
```

## C

```c
int minOperations(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    int *stack = (int *)malloc(numsSize * sizeof(int));
    int top = -1;
    int ans = 0;
    for (int i = 0; i < numsSize; ++i) {
        int val = nums[i];
        if (val == 0) {
            while (top >= 0 && stack[top] > 0) {
                ans++;
                top--;
            }
            continue;
        }
        while (top >= 0 && stack[top] > val) {
            ans++;
            top--;
        }
        if (top >= 0 && stack[top] == val) {
            // already present, nothing to do
        } else {
            stack[++top] = val;
        }
    }
    while (top >= 0) {
        ans++;
        top--;
    }
    free(stack);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinOperations(int[] nums) {
        int n = nums.Length;
        bool[] removed = new bool[n];
        var map = new SortedDictionary<int, List<int>>();
        
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                removed[i] = true;
                continue;
            }
            if (!map.ContainsKey(nums[i])) map[nums[i]] = new List<int>();
            map[nums[i]].Add(i);
        }
        
        int ops = 0;
        foreach (var kvp in map) {
            var indices = kvp.Value;
            // count operations for this value using current removed state
            foreach (int idx in indices) {
                if (idx == 0 || removed[idx - 1]) ops++;
            }
            // now mark these positions as zeroed for future values
            foreach (int idx in indices) {
                removed[idx] = true;
            }
        }
        
        return ops;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    const stack = [];
    let ops = 0;
    for (const x of nums) {
        while (stack.length && stack[stack.length - 1] > x) {
            stack.pop();
        }
        if (x === 0) {
            // keep a zero as barrier
            if (!stack.length || stack[stack.length - 1] !== 0) {
                stack.push(0);
            }
        } else {
            if (!stack.length || stack[stack.length - 1] < x) {
                ops++;
                stack.push(x);
            }
            // if top == x, nothing to do
        }
    }
    return ops;
};
```

## Typescript

```typescript
function minOperations(nums: number[]): number {
    let ans = 0;
    const stack: number[] = [];
    for (const x of nums) {
        if (x === 0) {
            while (stack.length) {
                stack.pop();
                ans++;
            }
            continue;
        }
        while (stack.length && stack[stack.length - 1] > x) {
            stack.pop();
            ans++;
        }
        if (stack.length && stack[stack.length - 1] === x) {
            // same value already in current segment, no new operation needed
        } else {
            stack.push(x);
        }
    }
    ans += stack.length;
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minOperations($nums) {
        $stack = [];
        $ops = 0;
        foreach ($nums as $num) {
            if ($num == 0) {
                // zero breaks all current segments
                $stack = [];
                continue;
            }
            while (!empty($stack) && end($stack) > $num) {
                array_pop($stack);
            }
            if (empty($stack) || end($stack) < $num) {
                $stack[] = $num;
                $ops++;
            }
        }
        return $ops;
    }
}
```

## Swift

```swift
class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var stack = [Int]()
        var ans = 0
        for v in nums {
            if v == 0 {
                stack.removeAll()
                continue
            }
            while let last = stack.last, last > v {
                stack.removeLast()
            }
            if let last = stack.last, last == v {
                continue
            } else {
                stack.append(v)
                ans += 1
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
import java.util.StringTokenizer
import kotlin.math.*

class Fenwick(private val n: Int) {
    private val bit = IntArray(n + 2)
    fun add(idx: Int, delta: Int) {
        var i = idx + 1
        while (i <= n) {
            bit[i] += delta
            i += i and -i
        }
    }

    fun sum(idx: Int): Int {
        var i = idx + 1
        var res = 0
        while (i > 0) {
            res += bit[i]
            i -= i and -i
        }
        return res
    }
}

class Solution {
    fun minOperations(nums: IntArray): Int {
        val n = nums.size
        val fenwick = Fenwick(n)
        val map = HashMap<Int, MutableList<Int>>()
        for (i in 0 until n) {
            val v = nums[i]
            if (v == 0) {
                fenwick.add(i, 1) // already zero
            } else {
                map.computeIfAbsent(v) { mutableListOf() }.add(i)
            }
        }
        var ans = 0
        val keys = map.keys.sorted()
        for (key in keys) {
            val list = map[key]!!
            var prevIdx = -1
            for (idx in list) {
                if (prevIdx == -1) {
                    ans++
                } else {
                    val between = fenwick.sum(idx) - fenwick.sum(prevIdx)
                    if (between > 0) ans++
                }
                prevIdx = idx
            }
            // mark these positions as visited (zeroed)
            for (idx in list) {
                fenwick.add(idx, 1)
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minOperations(List<int> nums) {
    int n = nums.length;
    int maxVal = 0;
    for (int v in nums) {
      if (v > maxVal) maxVal = v;
    }
    // Buckets of indices for each value
    List<List<int>> buckets = List.generate(maxVal + 1, (_) => []);
    for (int i = 0; i < n; ++i) {
      int v = nums[i];
      if (v > 0) {
        buckets[v].add(i);
      }
    }

    // DSU structures
    List<int> parent = List.filled(n, -1);
    List<int> size = List.filled(n, 1);

    int find(int x) {
      while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
      }
      return x;
    }

    void union(int a, int b) {
      int ra = find(a);
      int rb = find(b);
      if (ra == rb) return;
      if (size[ra] < size[rb]) {
        int tmp = ra;
        ra = rb;
        rb = tmp;
      }
      parent[rb] = ra;
      size[ra] += size[rb];
    }

    int ans = 0;

    for (int v = maxVal; v >= 1; --v) {
      List<int> idxList = buckets[v];
      if (idxList.isEmpty) continue;

      // Activate positions with value v and union with active neighbors
      for (int idx in idxList) {
        parent[idx] = idx;
        // left neighbor
        if (idx > 0 && parent[idx - 1] != -1) {
          union(idx, idx - 1);
        }
        // right neighbor
        if (idx + 1 < n && parent[idx + 1] != -1) {
          union(idx, idx + 1);
        }
      }

      // Count distinct components that contain at least one v
      Set<int> roots = {};
      for (int idx in idxList) {
        roots.add(find(idx));
      }
      ans += roots.length;
    }

    return ans;
  }
}
```

## Golang

```go
func minOperations(nums []int) int {
    stack := make([]int, 0)
    ops := 0
    for _, v := range nums {
        for len(stack) > 0 && stack[len(stack)-1] > v {
            stack = stack[:len(stack)-1]
        }
        if (len(stack) == 0 || stack[len(stack)-1] < v) && v > 0 {
            stack = append(stack, v)
            ops++
        }
    }
    return ops
}
```

## Ruby

```ruby
def min_operations(nums)
  stack = []
  ans = 0
  nums.each do |num|
    if num == 0
      stack.clear
      next
    end
    while !stack.empty? && stack[-1] > num
      stack.pop
    end
    if stack.empty? || stack[-1] < num
      stack << num
      ans += 1
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def minOperations(nums: Array[Int]): Int = {
        var ops = 0
        val stack = new scala.collection.mutable.ArrayDeque[Int]()
        for (x <- nums) {
            if (x == 0) {
                stack.clear()
            } else {
                while (stack.nonEmpty && stack.last > x) {
                    stack.removeLast()
                }
                if (stack.isEmpty || stack.last < x) {
                    ops += 1
                    stack.append(x)
                }
            }
        }
        ops
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut stack: Vec<i32> = Vec::new();
        let mut ans: i32 = 0;
        for &x in nums.iter() {
            if x == 0 {
                continue;
            }
            while let Some(&top) = stack.last() {
                if top > x {
                    stack.pop();
                } else {
                    break;
                }
            }
            match stack.last() {
                Some(&top) if top == x => {}
                _ => {
                    stack.push(x);
                    ans += 1;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (min-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  (letrec
      ((pop-while-greater
        (lambda (stk v)
          (cond [(null? stk) '()]
                [(> (car stk) v) (pop-while-greater (cdr stk) v)]
                [else stk])))
       (iter
        (lambda (lst stack ans)
          (if (null? lst)
              ans
              (let ((val (car lst)))
                (cond [(zero? val)
                       (iter (cdr lst) '() ans)]
                      [else
                       (let ((new-stack (pop-while-greater stack val)))
                         (if (or (null? new-stack) (< (car new-stack) val))
                             (iter (cdr lst) (cons val new-stack) (+ ans 1))
                             (iter (cdr lst) new-stack ans)))]))))))
    (iter nums '() 0)))
```

## Erlang

```erlang
-module(solution).
-export([min_operations/1]).

-spec min_operations(Nums :: [integer()]) -> integer().
min_operations(Nums) ->
    min_ops(Nums, -1, 0).

min_ops([], _Prev, Acc) ->
    Acc;
min_ops([H|T], Prev, Acc) ->
    NewAcc = 
        if
            H == 0 -> Acc;
            Prev < H -> Acc + 1;
            true -> Acc
        end,
    min_ops(T, H, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer]) :: integer
  def min_operations(nums) do
    {ans, _stack} =
      Enum.reduce(nums, {0, []}, fn val, {cnt, stack} ->
        if val == 0 do
          {cnt, stack}
        else
          new_stack = pop_greater(stack, val)

          case new_stack do
            [] -> {cnt + 1, [val]}
            [h | _] when h == val -> {cnt, new_stack}
            _ -> {cnt + 1, [val | new_stack]}
          end
        end
      end)

    ans
  end

  defp pop_greater([], _val), do: []
  defp pop_greater([h | t], val) when h > val, do: pop_greater(t, val)
  defp pop_greater(stack, _val), do: stack
end
```
