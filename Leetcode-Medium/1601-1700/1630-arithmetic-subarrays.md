# 1630. Arithmetic Subarrays

## Cpp

```cpp
class Solution {
public:
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
        int m = l.size();
        vector<bool> ans;
        ans.reserve(m);
        for (int i = 0; i < m; ++i) {
            int left = l[i], right = r[i];
            vector<int> sub;
            sub.reserve(right - left + 1);
            for (int j = left; j <= right; ++j) {
                sub.push_back(nums[j]);
            }
            sort(sub.begin(), sub.end());
            int diff = sub[1] - sub[0];
            bool ok = true;
            for (size_t k = 2; k < sub.size(); ++k) {
                if (sub[k] - sub[k - 1] != diff) {
                    ok = false;
                    break;
                }
            }
            ans.push_back(ok);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        List<Boolean> result = new ArrayList<>();
        for (int i = 0; i < l.length; i++) {
            int start = l[i];
            int end = r[i];
            int len = end - start + 1;
            int[] sub = new int[len];
            System.arraycopy(nums, start, sub, 0, len);
            Arrays.sort(sub);
            int diff = sub[1] - sub[0];
            boolean ok = true;
            for (int j = 2; j < len; j++) {
                if (sub[j] - sub[j - 1] != diff) {
                    ok = false;
                    break;
                }
            }
            result.add(ok);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        result = []
        for start, end in zip(l, r):
            sub = nums[start:end + 1]
            sub.sort()
            diff = sub[1] - sub[0]
            ok = True
            for i in range(2, len(sub)):
                if sub[i] - sub[i - 1] != diff:
                    ok = False
                    break
            result.append(ok)
        return result
```

## Python3

```python
from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for start, end in zip(l, r):
            sub = nums[start:end + 1]
            sub.sort()
            diff = sub[1] - sub[0]
            ok = True
            for i in range(2, len(sub)):
                if sub[i] - sub[i - 1] != diff:
                    ok = False
                    break
            result.append(ok)
        return result
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* checkArithmeticSubarrays(int* nums, int numsSize, int* l, int lSize,
                               int* r, int rSize, int* returnSize) {
    bool *ans = (bool *)malloc(lSize * sizeof(bool));
    *returnSize = lSize;
    
    for (int i = 0; i < lSize; ++i) {
        int start = l[i];
        int end   = r[i];
        int len = end - start + 1;
        
        int *sub = (int *)malloc(len * sizeof(int));
        for (int j = 0; j < len; ++j) {
            sub[j] = nums[start + j];
        }
        qsort(sub, len, sizeof(int), cmp_int);
        
        bool ok = true;
        int diff = sub[1] - sub[0];
        for (int j = 2; j < len; ++j) {
            if (sub[j] - sub[j-1] != diff) {
                ok = false;
                break;
            }
        }
        ans[i] = ok;
        free(sub);
    }
    
    return ans;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<bool> CheckArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        int m = l.Length;
        var answer = new List<bool>(m);
        for (int i = 0; i < m; i++) {
            int start = l[i];
            int end = r[i];
            int len = end - start + 1;
            int[] sub = new int[len];
            System.Array.Copy(nums, start, sub, 0, len);
            System.Array.Sort(sub);
            bool ok = true;
            int diff = sub[1] - sub[0];
            for (int j = 2; j < len; j++) {
                if (sub[j] - sub[j - 1] != diff) {
                    ok = false;
                    break;
                }
            }
            answer.Add(ok);
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} l
 * @param {number[]} r
 * @return {boolean[]}
 */
var checkArithmeticSubarrays = function(nums, l, r) {
    const m = l.length;
    const ans = new Array(m);
    for (let i = 0; i < m; i++) {
        const sub = nums.slice(l[i], r[i] + 1);
        sub.sort((a, b) => a - b);
        const diff = sub[1] - sub[0];
        let ok = true;
        for (let j = 2; j < sub.length; j++) {
            if (sub[j] - sub[j - 1] !== diff) {
                ok = false;
                break;
            }
        }
        ans[i] = ok;
    }
    return ans;
};
```

## Typescript

```typescript
function checkArithmeticSubarrays(nums: number[], l: number[], r: number[]): boolean[] {
    const m = l.length;
    const result: boolean[] = new Array(m);
    for (let i = 0; i < m; i++) {
        const sub = nums.slice(l[i], r[i] + 1);
        sub.sort((a, b) => a - b);
        const diff = sub[1] - sub[0];
        let ok = true;
        for (let j = 2; j < sub.length; j++) {
            if (sub[j] - sub[j - 1] !== diff) {
                ok = false;
                break;
            }
        }
        result[i] = ok;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $l
     * @param Integer[] $r
     * @return Boolean[]
     */
    function checkArithmeticSubarrays($nums, $l, $r) {
        $m = count($l);
        $result = [];
        for ($i = 0; $i < $m; $i++) {
            $len = $r[$i] - $l[$i] + 1;
            $sub = array_slice($nums, $l[$i], $len);
            sort($sub, SORT_NUMERIC);
            $diff = $sub[1] - $sub[0];
            $isArithmetic = true;
            for ($j = 2; $j < $len; $j++) {
                if ($sub[$j] - $sub[$j - 1] !== $diff) {
                    $isArithmetic = false;
                    break;
                }
            }
            $result[] = $isArithmetic;
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func checkArithmeticSubarrays(_ nums: [Int], _ l: [Int], _ r: [Int]) -> [Bool] {
        var answer = [Bool]()
        let m = l.count
        for i in 0..<m {
            let start = l[i]
            let end = r[i]
            var minVal = Int.max
            var maxVal = Int.min
            var set = Set<Int>()
            for idx in start...end {
                let val = nums[idx]
                if val < minVal { minVal = val }
                if val > maxVal { maxVal = val }
                set.insert(val)
            }
            let length = end - start + 1
            let diffNumerator = maxVal - minVal
            if diffNumerator % (length - 1) != 0 {
                answer.append(false)
                continue
            }
            let diff = diffNumerator / (length - 1)
            var ok = true
            var current = minVal
            for _ in 0..<length {
                if !set.contains(current) {
                    ok = false
                    break
                }
                current += diff
            }
            answer.append(ok)
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkArithmeticSubarrays(nums: IntArray, l: IntArray, r: IntArray): List<Boolean> {
        val m = l.size
        val result = ArrayList<Boolean>(m)
        for (i in 0 until m) {
            val start = l[i]
            val end = r[i]
            val len = end - start + 1
            val sub = IntArray(len)
            var idx = 0
            for (j in start..end) {
                sub[idx++] = nums[j]
            }
            java.util.Arrays.sort(sub)
            var ok = true
            if (len >= 2) {
                val diff = sub[1] - sub[0]
                for (k in 2 until len) {
                    if (sub[k] - sub[k - 1] != diff) {
                        ok = false
                        break
                    }
                }
            }
            result.add(ok)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<bool> checkArithmeticSubarrays(List<int> nums, List<int> l, List<int> r) {
    List<bool> answer = [];
    for (int i = 0; i < l.length; i++) {
      List<int> sub = nums.sublist(l[i], r[i] + 1);
      sub.sort();
      bool isArithmetic = true;
      int diff = sub[1] - sub[0];
      for (int j = 2; j < sub.length; j++) {
        if (sub[j] - sub[j - 1] != diff) {
          isArithmetic = false;
          break;
        }
      }
      answer.add(isArithmetic);
    }
    return answer;
  }
}
```

## Golang

```go
package main

import "sort"

func checkArithmeticSubarrays(nums []int, l []int, r []int) []bool {
	m := len(l)
	ans := make([]bool, m)
	for i := 0; i < m; i++ {
		start, end := l[i], r[i]
		size := end - start + 1
		sub := make([]int, size)
		copy(sub, nums[start:end+1])
		sort.Ints(sub)
		diff := sub[1] - sub[0]
		ok := true
		for j := 2; j < size; j++ {
			if sub[j]-sub[j-1] != diff {
				ok = false
				break
			}
		}
		ans[i] = ok
	}
	return ans
}
```

## Ruby

```ruby
def check_arithmetic_subarrays(nums, l, r)
  m = l.length
  result = Array.new(m)
  (0...m).each do |i|
    sub = nums[l[i]..r[i]]
    sub.sort!
    diff = sub[1] - sub[0]
    ok = true
    j = 2
    while j < sub.length
      if sub[j] - sub[j - 1] != diff
        ok = false
        break
      end
      j += 1
    end
    result[i] = ok
  end
  result
end
```

## Scala

```scala
object Solution {
    def checkArithmeticSubarrays(nums: Array[Int], l: Array[Int], r: Array[Int]): List[Boolean] = {
        val result = scala.collection.mutable.ListBuffer[Boolean]()
        for (i <- l.indices) {
            val sub = nums.slice(l(i), r(i) + 1).sorted
            var ok = true
            if (sub.length >= 2) {
                val diff = sub(1) - sub(0)
                var j = 2
                while (j < sub.length && ok) {
                    if (sub(j) - sub(j - 1) != diff) ok = false
                    j += 1
                }
            }
            result += ok
        }
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_arithmetic_subarrays(nums: Vec<i32>, l: Vec<i32>, r: Vec<i32>) -> Vec<bool> {
        let mut result = Vec::with_capacity(l.len());
        for (&li, &ri) in l.iter().zip(r.iter()) {
            let start = li as usize;
            let end = ri as usize; // inclusive
            let mut sub = nums[start..=end].to_vec();
            sub.sort_unstable();
            let diff = sub[1] - sub[0];
            let mut ok = true;
            for i in 2..sub.len() {
                if sub[i] - sub[i - 1] != diff {
                    ok = false;
                    break;
                }
            }
            result.push(ok);
        }
        result
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (check-arithmetic-subarrays nums l r)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) (listof boolean?))
  (let* ([nums-vec (list->vector nums)]
         [m (length l)])
    (for/list ([i (in-range m)])
      (let* ([start (list-ref l i)]
             [end (list-ref r i)]
             [sub (for/list ([idx (in-range start (+ end 1))])
                    (vector-ref nums-vec idx))]
             [len (length sub)])
        (if (= len 2)
            #true
            (let* ([sorted-sub (sort sub <)]
                   [diff (- (second sorted-sub) (first sorted-sub))])
              (let loop ((prev (first sorted-sub))
                         (rest (rest sorted-sub)))
                (cond
                  [(null? rest) #true]
                  [(= (- (first rest) prev) diff)
                   (loop (first rest) (rest rest))]
                  [else #false])))))))))
```

## Erlang

```erlang
-spec check_arithmetic_subarrays(Nums :: [integer()], L :: [integer()], R :: [integer()]) -> [boolean()].
check_arithmetic_subarrays(Nums, L, R) ->
    process(L, R, Nums, []).

process([], [], _Nums, Acc) ->
    lists:reverse(Acc);
process([Lh|Lt], [Rh|Rt], Nums, Acc) ->
    Sub = subarray(Nums, Lh, Rh),
    Sorted = lists:sort(Sub),
    Res = is_arithmetic(Sorted),
    process(Lt, Rt, Nums, [Res|Acc]).

subarray(Ns, L, R) ->
    Len = R - L + 1,
    Tail = lists:nthtail(L, Ns),
    lists:sublist(Tail, Len).

is_arithmetic([_,_|_] = List) ->
    Diff = hd(tl(List)) - hd(List),
    check_consecutive(List, Diff);
is_arithmetic(_) -> false.

check_consecutive([_], _Diff) -> true;
check_consecutive([Prev, Curr|Rest], Diff) ->
    case Curr - Prev of
        D when D =:= Diff -> check_consecutive([Curr|Rest], Diff);
        _ -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_arithmetic_subarrays(nums :: [integer], l :: [integer], r :: [integer]) :: [boolean]
  def check_arithmetic_subarrays(nums, l, r) do
    Enum.map(Enum.with_index(l), fn {li, i} ->
      ri = Enum.at(r, i)
      sub = Enum.slice(nums, li, ri - li + 1)
      arithmetic?(sub)
    end)
  end

  defp arithmetic?(list) do
    sorted = Enum.sort(list)

    case sorted do
      [a, b | rest] ->
        diff = b - a
        check_diff(rest, diff, b)

      _ ->
        true
    end
  end

  defp check_diff([], _diff, _prev), do: true

  defp check_diff([h | t], diff, prev) do
    if h - prev == diff do
      check_diff(t, diff, h)
    else
      false
    end
  end
end
```
