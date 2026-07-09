# 3043. Find the Length of the Longest Common Prefix

## Cpp

```cpp
class Solution {
public:
    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {
        unordered_set<int> pref;
        pref.reserve(arr1.size() * 10);
        for (int x : arr1) {
            int v = x;
            while (v > 0 && !pref.count(v)) {
                pref.insert(v);
                v /= 10;
            }
        }
        int best = 0;
        for (int y : arr2) {
            int v = y;
            while (v > 0 && !pref.count(v)) {
                v /= 10;
            }
            if (v > 0) {
                int len = 0, tmp = v;
                while (tmp) {
                    ++len;
                    tmp /= 10;
                }
                best = max(best, len);
            }
        }
        return best;
    }
};
```

## Java

```java
import java.util.HashSet;

class Solution {
    public int longestCommonPrefix(int[] arr1, int[] arr2) {
        HashSet<Integer> prefixes = new HashSet<>();
        for (int num : arr1) {
            int cur = num;
            while (cur > 0) {
                prefixes.add(cur);
                cur /= 10;
            }
        }

        int best = 0;
        for (int num : arr2) {
            int cur = num;
            while (cur > 0 && !prefixes.contains(cur)) {
                cur /= 10;
            }
            if (cur > 0) {
                int len = digitCount(cur);
                if (len > best) {
                    best = len;
                }
            }
        }
        return best;
    }

    private int digitCount(int x) {
        int cnt = 0;
        while (x > 0) {
            cnt++;
            x /= 10;
        }
        return cnt;
    }
}
```

## Python

```python
class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        prefixes = set()
        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10

        best = 0
        for num in arr2:
            cur = num
            while cur > 0 and cur not in prefixes:
                cur //= 10
            if cur > 0:
                length = len(str(cur))
                if length > best:
                    best = length
        return best
```

## Python3

```python
from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for v in arr1:
            while v > 0 and v not in prefixes:
                prefixes.add(v)
                v //= 10

        best = 0
        for v in arr2:
            cur = v
            while cur > 0 and cur not in prefixes:
                cur //= 10
            if cur > 0:
                length = len(str(cur))
                if length > best:
                    best = length
        return best
```

## C

```c
#include <stdlib.h>

static int cmp_int(const void *a, const void *b) {
    int va = *(const int *)a;
    int vb = *(const int *)b;
    return (va > vb) - (va < vb);
}

int longestCommonPrefix(int* arr1, int arr1Size, int* arr2, int arr2Size) {
    if (arr1Size == 0 || arr2Size == 0) return 0;

    /* collect all prefixes from arr1 */
    int maxPrefixes = arr1Size * 10;               // each number has at most 9 prefixes + original
    int *prefixes = (int *)malloc(maxPrefixes * sizeof(int));
    int psize = 0;
    for (int i = 0; i < arr1Size; ++i) {
        int v = arr1[i];
        while (v > 0) {
            prefixes[psize++] = v;
            v /= 10;
        }
    }

    /* sort and deduplicate */
    qsort(prefixes, psize, sizeof(int), cmp_int);
    int uniqSize = 0;
    for (int i = 0; i < psize; ++i) {
        if (i == 0 || prefixes[i] != prefixes[i - 1]) {
            prefixes[uniqSize++] = prefixes[i];
        }
    }

    int answer = 0;

    for (int i = 0; i < arr2Size; ++i) {
        int v = arr2[i];
        /* compute digit length of original number */
        int len = 0;
        int tmp = v;
        while (tmp > 0) { tmp /= 10; ++len; }

        while (v > 0) {
            if (bsearch(&v, prefixes, uniqSize, sizeof(int), cmp_int)) {
                if (len > answer) answer = len;
                break;          // longest prefix for this number found
            }
            v /= 10;
            --len;
        }
    }

    free(prefixes);
    return answer;
}
```

## Csharp

```csharp
public class Solution
{
    public int LongestCommonPrefix(int[] arr1, int[] arr2)
    {
        var prefixes = new HashSet<int>();
        foreach (int num in arr1)
        {
            int v = num;
            while (v > 0 && !prefixes.Contains(v))
            {
                prefixes.Add(v);
                v /= 10;
            }
        }

        int best = 0;
        foreach (int num in arr2)
        {
            int v = num;
            while (v > 0 && !prefixes.Contains(v))
                v /= 10;

            if (v > 0)
            {
                int len = DigitCount(v);
                if (len > best) best = len;
            }
        }

        return best;
    }

    private int DigitCount(int x)
    {
        int cnt = 0;
        while (x > 0)
        {
            cnt++;
            x /= 10;
        }
        return cnt;
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
var longestCommonPrefix = function(arr1, arr2) {
    const prefixes = new Set();
    for (const num of arr1) {
        let v = num;
        while (v > 0) {
            prefixes.add(v);
            v = Math.floor(v / 10);
        }
    }

    let best = 0;
    for (const num of arr2) {
        let v = num;
        while (v > 0 && !prefixes.has(v)) {
            v = Math.floor(v / 10);
        }
        if (v > 0) {
            const len = v.toString().length;
            if (len > best) best = len;
        }
    }
    return best;
};
```

## Typescript

```typescript
function longestCommonPrefix(arr1: number[], arr2: number[]): number {
    const prefixes = new Set<number>();
    // Store all possible prefixes from arr1
    for (const num of arr1) {
        let v = num;
        while (v > 0) {
            prefixes.add(v);
            v = Math.floor(v / 10);
        }
    }

    const digitLength = (n: number): number => {
        let len = 0;
        while (n > 0) {
            len++;
            n = Math.floor(n / 10);
        }
        return len;
    };

    let maxLen = 0;
    // Check each number in arr2 for the longest matching prefix
    for (const num of arr2) {
        let v = num;
        while (v > 0 && !prefixes.has(v)) {
            v = Math.floor(v / 10);
        }
        if (v > 0) {
            const len = digitLength(v);
            if (len > maxLen) maxLen = len;
        }
    }

    return maxLen;
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
    function longestCommonPrefix($arr1, $arr2) {
        $prefixSet = [];

        // Store all prefixes of numbers in arr1
        foreach ($arr1 as $num) {
            while ($num > 0) {
                $prefixSet[$num] = true;
                $num = intdiv($num, 10);
            }
        }

        $maxLen = 0;

        // For each number in arr2, find the longest matching prefix
        foreach ($arr2 as $num) {
            $temp = $num;
            while ($temp > 0) {
                if (isset($prefixSet[$temp])) {
                    $len = strlen((string)$temp);
                    if ($len > $maxLen) {
                        $maxLen = $len;
                    }
                    break; // longest prefix for this number found
                }
                $temp = intdiv($temp, 10);
            }
        }

        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func longestCommonPrefix(_ arr1: [Int], _ arr2: [Int]) -> Int {
        var prefixSet = Set<Int>()
        for num in arr1 {
            var v = num
            while v > 0 {
                prefixSet.insert(v)
                v /= 10
            }
        }
        
        var maxLen = 0
        for num in arr2 {
            var v = num
            while v > 0 && !prefixSet.contains(v) {
                v /= 10
            }
            if v > 0 {
                let len = digitCount(v)
                if len > maxLen { maxLen = len }
            }
        }
        return maxLen
    }
    
    private func digitCount(_ x: Int) -> Int {
        var cnt = 0
        var v = x
        while v > 0 {
            cnt += 1
            v /= 10
        }
        return cnt
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun longestCommonPrefix(arr1: IntArray, arr2: IntArray): Int {
        val prefixes = HashSet<Int>()
        for (v in arr1) {
            var x = v
            while (x > 0) {
                prefixes.add(x)
                x /= 10
            }
        }

        var maxLen = 0
        for (v in arr2) {
            var y = v
            while (y > 0 && !prefixes.contains(y)) {
                y /= 10
            }
            if (y > 0) {
                val len = digitCount(y)
                if (len > maxLen) maxLen = len
            }
        }
        return maxLen
    }

    private fun digitCount(num: Int): Int {
        var n = num
        var cnt = 0
        while (n > 0) {
            cnt++
            n /= 10
        }
        return cnt
    }
}
```

## Dart

```dart
class Solution {
  int longestCommonPrefix(List<int> arr1, List<int> arr2) {
    final Set<int> prefixes = <int>{};
    for (var val in arr1) {
      int cur = val;
      while (cur > 0 && !prefixes.contains(cur)) {
        prefixes.add(cur);
        cur ~/= 10;
      }
    }

    int best = 0;

    int digitCount(int x) {
      int cnt = 0;
      while (x > 0) {
        cnt++;
        x ~/= 10;
      }
      return cnt;
    }

    for (var val in arr2) {
      int cur = val;
      while (cur > 0 && !prefixes.contains(cur)) {
        cur ~/= 10;
      }
      if (cur > 0) {
        final len = digitCount(cur);
        if (len > best) best = len;
      }
    }

    return best;
  }
}
```

## Golang

```go
func longestCommonPrefix(arr1 []int, arr2 []int) int {
    prefixes := make(map[int]struct{})
    for _, v := range arr1 {
        x := v
        for x > 0 {
            prefixes[x] = struct{}{}
            x /= 10
        }
    }

    maxLen := 0
    for _, v := range arr2 {
        x := v
        for x > 0 {
            if _, ok := prefixes[x]; ok {
                // count digits of x
                cnt := 0
                t := x
                for t > 0 {
                    cnt++
                    t /= 10
                }
                if cnt > maxLen {
                    maxLen = cnt
                }
                break
            }
            x /= 10
        }
    }

    return maxLen
}
```

## Ruby

```ruby
require 'set'

def longest_common_prefix(arr1, arr2)
  prefixes = Set.new
  arr1.each do |num|
    while num > 0 && !prefixes.include?(num)
      prefixes.add(num)
      num /= 10
    end
  end

  max_len = 0
  arr2.each do |num|
    cur = num
    while cur > 0 && !prefixes.include?(cur)
      cur /= 10
    end
    if cur > 0
      len = cur.to_s.length
      max_len = len if len > max_len
    end
  end

  max_len
end
```

## Scala

```scala
object Solution {
    def longestCommonPrefix(arr1: Array[Int], arr2: Array[Int]): Int = {
        import scala.collection.mutable
        val prefixSet = mutable.HashSet[Int]()
        for (num <- arr1) {
            var v = num
            while (v > 0) {
                prefixSet.add(v)
                v /= 10
            }
        }
        var maxLen = 0
        for (num <- arr2) {
            var v = num
            while (v > 0 && !prefixSet.contains(v)) {
                v /= 10
            }
            if (v > 0) {
                var len = 0
                var temp = v
                while (temp > 0) {
                    len += 1
                    temp /= 10
                }
                if (len > maxLen) maxLen = len
            }
        }
        maxLen
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn longest_common_prefix(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        let mut prefixes: HashSet<i32> = HashSet::new();
        // store all prefixes of numbers in arr1
        for mut v in arr1 {
            while v > 0 && !prefixes.contains(&v) {
                prefixes.insert(v);
                v /= 10;
            }
        }

        let mut best: i32 = 0;

        for mut v in arr2 {
            // reduce until a matching prefix is found or v becomes 0
            while v > 0 && !prefixes.contains(&v) {
                v /= 10;
            }
            if v > 0 {
                // compute length of this prefix (number of digits)
                let mut len = 0;
                let mut tmp = v;
                while tmp > 0 {
                    len += 1;
                    tmp /= 10;
                }
                if len > best {
                    best = len;
                }
            }
        }

        best
    }
}
```

## Racket

```racket
(define/contract (longest-common-prefix arr1 arr2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let ((prefix-set (make-hash)))
    ;; store all prefixes of numbers in arr1
    (for-each
     (lambda (val)
       (let loop ((v val))
         (when (> v 0)
           (hash-set! prefix-set v #t)
           (loop (quotient v 10)))))
     arr1)
    (define (digit-count n)
      (let loop ((x n) (cnt 0))
        (if (= x 0) cnt
            (loop (quotient x 10) (+ cnt 1)))))
    (let ((maxlen (box 0)))
      (for-each
       (lambda (val)
         (let loop ((v val))
           (cond
             [(= v 0) (void)]
             [(hash-has-key? prefix-set v)
              (let ((len (digit-count v)))
                (when (> len (unbox maxlen))
                  (set-box! maxlen len)))]
             [else (loop (quotient v 10))])))
       arr2)
      (unbox maxlen))))
```

## Erlang

```erlang
-module(solution).
-export([longest_common_prefix/2]).

-spec longest_common_prefix(Arr1 :: [integer()], Arr2 :: [integer()]) -> integer().
longest_common_prefix(Arr1, Arr2) ->
    PrefixSet = build_prefix_set(Arr1, #{}),
    find_longest(PrefixSet, Arr2, 0).

%% Build a set (map with dummy value) of all prefixes from numbers in Arr.
build_prefix_set([], Set) -> Set;
build_prefix_set([H|T], Set) ->
    NewSet = add_prefixes(H, Set),
    build_prefix_set(T, NewSet).

add_prefixes(0, Set) -> Set;  % stop when number becomes zero
add_prefixes(N, Set) when N > 0 ->
    UpdatedSet = maps:put(N, true, Set),
    add_prefixes(N div 10, UpdatedSet).

%% Find the maximum length of common prefix between any number in Arr2 and the set.
find_longest(_, [], Max) -> Max;
find_longest(Set, [H|T], Max) ->
    Len = longest_match_len(H, Set),
    NewMax = if Len > Max -> Len; true -> Max end,
    find_longest(Set, T, NewMax).

%% Return length of the longest prefix of N that exists in the set.
longest_match_len(N, Set) when N > 0 ->
    case maps:is_key(N, Set) of
        true -> digit_len(N);
        false -> longest_match_len(N div 10, Set)
    end;
longest_match_len(_, _) -> 0.

%% Compute number of digits in a positive integer.
digit_len(N) -> digit_len(N, 0).

digit_len(0, Count) -> Count;
digit_len(N, Count) ->
    digit_len(N div 10, Count + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_common_prefix(arr1 :: [integer], arr2 :: [integer]) :: integer
  def longest_common_prefix(arr1, arr2) do
    prefix_set = build_prefix_set(arr1, MapSet.new())

    Enum.reduce(arr2, 0, fn num, best ->
      case find_match(num, prefix_set) do
        nil -> best
        len -> max(best, len)
      end
    end)
  end

  defp build_prefix_set([], set), do: set

  defp build_prefix_set([h | t], set) do
    new_set = add_prefixes(h, set)
    build_prefix_set(t, new_set)
  end

  defp add_prefixes(0, set), do: set

  defp add_prefixes(val, set) when val > 0 do
    set = MapSet.put(set, val)
    add_prefixes(div(val, 10), set)
  end

  defp find_match(0, _set), do: nil

  defp find_match(val, set) when val > 0 do
    if MapSet.member?(set, val) do
      digit_len(val)
    else
      find_match(div(val, 10), set)
    end
  end

  defp digit_len(n), do: digit_len(n, 0)

  defp digit_len(0, acc), do: acc
  defp digit_len(num, acc), do: digit_len(div(num, 10), acc + 1)
end
```
