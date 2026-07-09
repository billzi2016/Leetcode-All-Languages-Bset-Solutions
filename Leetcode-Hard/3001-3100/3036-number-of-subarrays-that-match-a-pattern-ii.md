# 3036. Number of Subarrays That Match a Pattern II

## Cpp

```cpp
class Solution {
public:
    int countMatchingSubarrays(vector<int>& nums, vector<int>& pattern) {
        int n = nums.size();
        int m = pattern.size();
        if (n < 2 || m == 0) return 0;
        // Build diff array of size n-1
        vector<int> diff(n - 1);
        for (int i = 0; i < n - 1; ++i) {
            if (nums[i + 1] > nums[i]) diff[i] = 1;
            else if (nums[i + 1] == nums[i]) diff[i] = 0;
            else diff[i] = -1;
        }
        // KMP prefix function for pattern
        vector<int> pi(m, 0);
        for (int i = 1; i < m; ++i) {
            int j = pi[i - 1];
            while (j > 0 && pattern[i] != pattern[j]) {
                j = pi[j - 1];
            }
            if (pattern[i] == pattern[j]) ++j;
            pi[i] = j;
        }
        // Search
        long long ans = 0;
        int j = 0;
        for (int x : diff) {
            while (j > 0 && x != pattern[j]) {
                j = pi[j - 1];
            }
            if (x == pattern[j]) ++j;
            if (j == m) {
                ++ans;
                j = pi[j - 1];
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int countMatchingSubarrays(int[] nums, int[] pattern) {
        int n = nums.length;
        int m = pattern.length;
        // Build the difference array of size n-1
        int[] diff = new int[n - 1];
        for (int i = 0; i < n - 1; i++) {
            if (nums[i + 1] > nums[i]) diff[i] = 1;
            else if (nums[i + 1] == nums[i]) diff[i] = 0;
            else diff[i] = -1;
        }
        // Build LPS array for KMP
        int[] lps = new int[m];
        for (int i = 1, len = 0; i < m; ) {
            if (pattern[i] == pattern[len]) {
                lps[i++] = ++len;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i++] = 0;
                }
            }
        }
        // KMP search
        int count = 0;
        for (int i = 0, j = 0; i < diff.length; ) {
            if (diff[i] == pattern[j]) {
                i++;
                j++;
                if (j == m) {
                    count++;
                    j = lps[j - 1];
                }
            } else {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def countMatchingSubarrays(self, nums, pattern):
        """
        :type nums: List[int]
        :type pattern: List[int]
        :rtype: int
        """
        n = len(nums)
        m = len(pattern)

        # Build the difference array representing comparisons between consecutive elements.
        diff = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                diff[i] = 1
            elif nums[i + 1] == nums[i]:
                diff[i] = 0
            else:
                diff[i] = -1

        # Compute LPS (longest proper prefix which is also suffix) array for KMP.
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        # KMP search for pattern in diff.
        count = 0
        i = j = 0  # i -> index in diff, j -> index in pattern
        while i < n - 1:
            if diff[i] == pattern[j]:
                i += 1
                j += 1
                if j == m:
                    count += 1
                    j = lps[j - 1]
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return count
```

## Python3

```python
from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        # Build the comparison array of length n-1
        diffs = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                diffs[i] = 1
            elif nums[i + 1] == nums[i]:
                diffs[i] = 0
            else:
                diffs[i] = -1

        # KMP prefix function for pattern
        pi = [0] * m
        for i in range(1, m):
            j = pi[i - 1]
            while j > 0 and pattern[i] != pattern[j]:
                j = pi[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            pi[i] = j

        # KMP search over diffs
        cnt = 0
        j = 0
        for val in diffs:
            while j > 0 and val != pattern[j]:
                j = pi[j - 1]
            if val == pattern[j]:
                j += 1
            if j == m:
                cnt += 1
                j = pi[j - 1]

        return cnt
```

## C

```c
#include <stdlib.h>

int countMatchingSubarrays(int* nums, int numsSize, int* pattern, int patternSize) {
    if (numsSize - 1 < patternSize) return 0;

    // Build LPS array for KMP
    int *lps = (int *)malloc(sizeof(int) * patternSize);
    lps[0] = 0;
    for (int i = 1, len = 0; i < patternSize;) {
        if (pattern[i] == pattern[len]) {
            len++;
            lps[i] = len;
            i++;
        } else {
            if (len != 0) {
                len = lps[len - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }

    long long ans = 0;
    int j = 0; // index in pattern

    for (int i = 0; i < numsSize - 1; ++i) {
        int cur;
        if (nums[i + 1] > nums[i]) cur = 1;
        else if (nums[i + 1] == nums[i]) cur = 0;
        else cur = -1;

        while (j > 0 && cur != pattern[j]) {
            j = lps[j - 1];
        }
        if (cur == pattern[j]) {
            ++j;
        }
        if (j == patternSize) {
            ++ans;
            j = lps[j - 1];
        }
    }

    free(lps);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountMatchingSubarrays(int[] nums, int[] pattern)
    {
        int n = nums.Length;
        int m = pattern.Length;

        // Build the comparison array.
        int[] diff = new int[n - 1];
        for (int i = 0; i < n - 1; i++)
        {
            if (nums[i + 1] > nums[i]) diff[i] = 1;
            else if (nums[i + 1] == nums[i]) diff[i] = 0;
            else diff[i] = -1;
        }

        // Prefix function for KMP.
        int[] pi = new int[m];
        for (int i = 1; i < m; i++)
        {
            int j = pi[i - 1];
            while (j > 0 && pattern[i] != pattern[j])
                j = pi[j - 1];
            if (pattern[i] == pattern[j]) j++;
            pi[i] = j;
        }

        // KMP search.
        int count = 0;
        int jIdx = 0;
        for (int i = 0; i < diff.Length; i++)
        {
            while (jIdx > 0 && diff[i] != pattern[jIdx])
                jIdx = pi[jIdx - 1];
            if (diff[i] == pattern[jIdx]) jIdx++;
            if (jIdx == m)
            {
                count++;
                jIdx = pi[jIdx - 1];
            }
        }

        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} pattern
 * @return {number}
 */
var countMatchingSubarrays = function(nums, pattern) {
    const n = nums.length;
    const m = pattern.length;
    if (m === 0) return n; // not needed per constraints
    
    // Build diff array of length n-1 with values -1,0,1
    const diff = new Array(n - 1);
    for (let i = 0; i < n - 1; ++i) {
        const d = nums[i + 1] - nums[i];
        diff[i] = d > 0 ? 1 : (d < 0 ? -1 : 0);
    }
    
    // KMP prefix function for pattern
    const lps = new Array(m).fill(0);
    let len = 0;
    for (let i = 1; i < m; ++i) {
        while (len > 0 && pattern[i] !== pattern[len]) {
            len = lps[len - 1];
        }
        if (pattern[i] === pattern[len]) {
            ++len;
            lps[i] = len;
        }
    }
    
    // Scan diff using KMP
    let count = 0;
    let j = 0; // index in pattern
    for (let i = 0; i < diff.length; ++i) {
        while (j > 0 && diff[i] !== pattern[j]) {
            j = lps[j - 1];
        }
        if (diff[i] === pattern[j]) {
            ++j;
        }
        if (j === m) {
            ++count;
            j = lps[j - 1];
        }
    }
    
    return count;
};
```

## Typescript

```typescript
function countMatchingSubarrays(nums: number[], pattern: number[]): number {
    const n = nums.length;
    const m = pattern.length;
    if (m === 0) return n; // not expected per constraints

    const diffLen = n - 1;
    const diff = new Int8Array(diffLen);
    for (let i = 0; i < diffLen; i++) {
        const a = nums[i + 1];
        const b = nums[i];
        diff[i] = a > b ? 1 : a === b ? 0 : -1;
    }

    // Build LPS array for KMP
    const lps = new Int32Array(m);
    let len = 0;
    for (let i = 1; i < m;) {
        if (pattern[i] === pattern[len]) {
            len++;
            lps[i] = len;
            i++;
        } else {
            if (len !== 0) {
                len = lps[len - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }

    // KMP search
    let count = 0;
    let i = 0; // index for diff
    let j = 0; // index for pattern
    while (i < diffLen) {
        if (diff[i] === pattern[j]) {
            i++;
            j++;
            if (j === m) {
                count++;
                j = lps[j - 1];
            }
        } else {
            if (j !== 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }

    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $pattern
     * @return Integer
     */
    function countMatchingSubarrays($nums, $pattern) {
        $n = count($nums);
        $m = count($pattern);
        if ($m == 0 || $n - 1 < $m) {
            return 0;
        }

        // Build diff array representing comparisons between consecutive nums
        $diff = [];
        for ($i = 0; $i < $n - 1; $i++) {
            $a = $nums[$i];
            $b = $nums[$i + 1];
            if ($b > $a) {
                $diff[] = 1;
            } elseif ($b < $a) {
                $diff[] = -1;
            } else {
                $diff[] = 0;
            }
        }

        // Build LPS (longest proper prefix which is also suffix) array for KMP
        $lps = array_fill(0, $m, 0);
        $len = 0;
        for ($i = 1; $i < $m; $i++) {
            while ($len > 0 && $pattern[$i] !== $pattern[$len]) {
                $len = $lps[$len - 1];
            }
            if ($pattern[$i] === $pattern[$len]) {
                $len++;
                $lps[$i] = $len;
            } else {
                $lps[$i] = 0;
            }
        }

        // KMP search
        $count = 0;
        $j = 0; // index in pattern
        $diffLen = $n - 1;
        for ($i = 0; $i < $diffLen; $i++) {
            while ($j > 0 && $diff[$i] !== $pattern[$j]) {
                $j = $lps[$j - 1];
            }
            if ($diff[$i] === $pattern[$j]) {
                $j++;
                if ($j == $m) {
                    $count++;
                    $j = $lps[$j - 1];
                }
            }
        }

        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func countMatchingSubarrays(_ nums: [Int], _ pattern: [Int]) -> Int {
        let n = nums.count
        let m = pattern.count
        if n < m + 1 { return 0 }
        
        // Build comparison array
        var diff = [Int]()
        diff.reserveCapacity(n - 1)
        for i in 0..<(n - 1) {
            let a = nums[i]
            let b = nums[i + 1]
            if b > a {
                diff.append(1)
            } else if b == a {
                diff.append(0)
            } else {
                diff.append(-1)
            }
        }
        
        // Prefix function for KMP
        var pi = [Int](repeating: 0, count: m)
        if m > 1 {
            for i in 1..<m {
                var j = pi[i - 1]
                while j > 0 && pattern[i] != pattern[j] {
                    j = pi[j - 1]
                }
                if pattern[i] == pattern[j] { j += 1 }
                pi[i] = j
            }
        }
        
        // KMP search
        var count = 0
        var j = 0
        for val in diff {
            while j > 0 && val != pattern[j] {
                j = pi[j - 1]
            }
            if val == pattern[j] { j += 1 }
            if j == m {
                count += 1
                j = pi[j - 1]
            }
        }
        
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countMatchingSubarrays(nums: IntArray, pattern: IntArray): Int {
        val n = nums.size
        val m = pattern.size
        if (n - 1 < m) return 0

        // Build comparison array
        val diff = IntArray(n - 1)
        for (i in 0 until n - 1) {
            diff[i] = when {
                nums[i + 1] > nums[i] -> 1
                nums[i + 1] == nums[i] -> 0
                else -> -1
            }
        }

        // Build LPS (prefix function) for pattern
        val lps = IntArray(m)
        var len = 0
        var i = 1
        while (i < m) {
            if (pattern[i] == pattern[len]) {
                len++
                lps[i] = len
                i++
            } else {
                if (len != 0) {
                    len = lps[len - 1]
                } else {
                    lps[i] = 0
                    i++
                }
            }
        }

        // KMP search
        var count = 0
        var j = 0
        i = 0
        while (i < diff.size) {
            if (diff[i] == pattern[j]) {
                i++; j++
                if (j == m) {
                    count++
                    j = lps[j - 1]
                }
            } else {
                if (j != 0) {
                    j = lps[j - 1]
                } else {
                    i++
                }
            }
        }

        return count
    }
}
```

## Dart

```dart
class Solution {
  int countMatchingSubarrays(List<int> nums, List<int> pattern) {
    int n = nums.length;
    int m = pattern.length;

    // Build the comparison array.
    List<int> diff = List.filled(n - 1, 0);
    for (int i = 0; i < n - 1; ++i) {
      if (nums[i + 1] > nums[i]) {
        diff[i] = 1;
      } else if (nums[i + 1] == nums[i]) {
        diff[i] = 0;
      } else {
        diff[i] = -1;
      }
    }

    // Build LPS (prefix function) for KMP.
    List<int> lps = List.filled(m, 0);
    int len = 0;
    for (int i = 1; i < m;) {
      if (pattern[i] == pattern[len]) {
        ++len;
        lps[i] = len;
        ++i;
      } else {
        if (len != 0) {
          len = lps[len - 1];
        } else {
          lps[i] = 0;
          ++i;
        }
      }
    }

    // KMP search.
    int count = 0;
    int i = 0; // index for diff
    int j = 0; // index for pattern
    while (i < diff.length) {
      if (diff[i] == pattern[j]) {
        ++i;
        ++j;
        if (j == m) {
          ++count;
          j = lps[j - 1];
        }
      } else {
        if (j != 0) {
          j = lps[j - 1];
        } else {
          ++i;
        }
      }
    }

    return count;
  }
}
```

## Golang

```go
func countMatchingSubarrays(nums []int, pattern []int) int {
    n := len(nums)
    m := len(pattern)

    // Build the difference array.
    diffSize := n - 1
    diff := make([]int, diffSize)
    for i := 0; i < diffSize; i++ {
        if nums[i+1] > nums[i] {
            diff[i] = 1
        } else if nums[i+1] == nums[i] {
            diff[i] = 0
        } else {
            diff[i] = -1
        }
    }

    // Compute KMP prefix (lps) array for pattern.
    pi := make([]int, m)
    for i := 1; i < m; i++ {
        j := pi[i-1]
        for j > 0 && pattern[i] != pattern[j] {
            j = pi[j-1]
        }
        if pattern[i] == pattern[j] {
            j++
        }
        pi[i] = j
    }

    // KMP search.
    count := 0
    j := 0
    for i := 0; i < diffSize; i++ {
        for j > 0 && diff[i] != pattern[j] {
            j = pi[j-1]
        }
        if diff[i] == pattern[j] {
            j++
        }
        if j == m {
            count++
            j = pi[j-1]
        }
    }

    return count
}
```

## Ruby

```ruby
def count_matching_subarrays(nums, pattern)
  n = nums.length
  m = pattern.length

  # Build the difference array representing comparisons between consecutive elements.
  diff_len = n - 1
  diff = Array.new(diff_len)
  i = 0
  while i < diff_len
    a = nums[i]
    b = nums[i + 1]
    if b > a
      diff[i] = 1
    elsif b == a
      diff[i] = 0
    else
      diff[i] = -1
    end
    i += 1
  end

  # Compute LPS (longest proper prefix which is also suffix) array for KMP.
  lps = Array.new(m, 0)
  len = 0
  i = 1
  while i < m
    if pattern[i] == pattern[len]
      len += 1
      lps[i] = len
      i += 1
    else
      if len != 0
        len = lps[len - 1]
      else
        lps[i] = 0
        i += 1
      end
    end
  end

  # KMP search: count occurrences of pattern in diff.
  count = 0
  ti = 0   # index for diff (text)
  pi = 0   # index for pattern
  while ti < diff_len
    if diff[ti] == pattern[pi]
      ti += 1
      pi += 1
      if pi == m
        count += 1
        pi = lps[pi - 1]
      end
    else
      if pi != 0
        pi = lps[pi - 1]
      else
        ti += 1
      end
    end
  end

  count
end
```

## Scala

```scala
object Solution {
    def countMatchingSubarrays(nums: Array[Int], pattern: Array[Int]): Int = {
        val n = nums.length
        val m = pattern.length
        if (m > n - 1) return 0

        // Build difference array with values -1, 0, 1
        val diff = new Array[Int](n - 1)
        var i = 0
        while (i < n - 1) {
            diff(i) = java.lang.Integer.compare(nums(i + 1), nums(i))
            i += 1
        }

        // Build LPS array for KMP
        val lps = new Array[Int](m)
        var len = 0
        var idx = 1
        while (idx < m) {
            if (pattern(idx) == pattern(len)) {
                len += 1
                lps(idx) = len
                idx += 1
            } else {
                if (len != 0) {
                    len = lps(len - 1)
                } else {
                    lps(idx) = 0
                    idx += 1
                }
            }
        }

        // KMP search
        var count = 0
        var di = 0
        var pj = 0
        while (di < diff.length) {
            if (diff(di) == pattern(pj)) {
                di += 1
                pj += 1
                if (pj == m) {
                    count += 1
                    pj = lps(pj - 1)
                }
            } else {
                if (pj != 0) {
                    pj = lps(pj - 1)
                } else {
                    di += 1
                }
            }
        }

        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_matching_subarrays(nums: Vec<i32>, pattern: Vec<i32>) -> i32 {
        let n = nums.len();
        if pattern.is_empty() || n < 2 {
            return 0;
        }
        // Build the difference array representing comparisons between consecutive elements.
        let mut diff: Vec<i32> = Vec::with_capacity(n - 1);
        for i in 0..n - 1 {
            let val = if nums[i + 1] > nums[i] {
                1
            } else if nums[i + 1] == nums[i] {
                0
            } else {
                -1
            };
            diff.push(val);
        }

        // Build LPS (longest proper prefix which is also suffix) array for KMP.
        let m = pattern.len();
        let mut lps = vec![0usize; m];
        let mut len = 0usize;
        for i in 1..m {
            while len > 0 && pattern[i] != pattern[len] {
                len = lps[len - 1];
            }
            if pattern[i] == pattern[len] {
                len += 1;
                lps[i] = len;
            } else {
                lps[i] = len; // len is zero here
            }
        }

        // KMP search for pattern in diff.
        let mut count: i32 = 0;
        let mut j = 0usize; // index in pattern
        for &val in diff.iter() {
            while j > 0 && val != pattern[j] {
                j = lps[j - 1];
            }
            if val == pattern[j] {
                j += 1;
            }
            if j == m {
                count += 1;
                j = lps[j - 1];
            }
        }

        count
    }
}
```

## Racket

```racket
#lang racket

;; Helper: compute prefix function for KMP
(define (compute-pi pat)
  (let* ([m (vector-length pat)]
         [pi (make-vector m 0)])
    (let loop ([i 1] [j 0])
      (when (< i m)
        (let recur ([j j])
          (if (and (> j 0) (not (= (vector-ref pat i) (vector-ref pat j))))
              (recur (vector-ref pi (- j 1)))
              (begin
                (when (= (vector-ref pat i) (vector-ref pat j))
                  (set! j (+ j 1)))
                (vector-set! pi i j)
                (loop (+ i 1) j))))))
    pi))

;; Helper: KMP search, returns number of occurrences
(define (kmp-search text pat pi)
  (let* ([n (vector-length text)]
         [m (vector-length pat)])
    (let loop ([i 0] [j 0] [cnt 0])
      (if (= i n)
          cnt
          (let recur ([j j])
            (if (and (> j 0) (not (= (vector-ref text i) (vector-ref pat j))))
                (recur (vector-ref pi (- j 1)))
                (let ([j2 (if (= (vector-ref text i) (vector-ref pat j)) (+ j 1) j)])
                  (if (= j2 m)
                      (loop (+ i 1) (vector-ref pi (- m 1)) (+ cnt 1))
                      (loop (+ i 1) j2 cnt)))))))))

;; Main function
(define/contract (count-matching-subarrays nums pattern)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)]
         [m (length pattern)])
    (if (> m (- n 1))
        0
        (let* ([v (list->vector nums)]
               [diff-len (- n 1)]
               [diff (make-vector diff-len)])
          (for ([i (in-range diff-len)])
            (let* ([a (vector-ref v i)]
                   [b (vector-ref v (+ i 1))]
                   [sgn (cond [(> b a) 1] [(< b a) -1] [else 0])])
              (vector-set! diff i sgn)))
          (define pat-vec (list->vector pattern))
          (define pi (compute-pi pat-vec))
          (kmp-search diff pat-vec pi)))))
```

## Erlang

```erlang
-module(solution).
-export([count_matching_subarrays/2]).

-spec count_matching_subarrays(Nums :: [integer()], Pattern :: [integer()]) -> integer().
count_matching_subarrays(Nums, Pattern) ->
    Diff = build_diff(Nums),
    PatT = list_to_tuple(Pattern),
    M = tuple_size(PatT),
    Lps = make_lps(PatT, M),
    scan(Diff, PatT, Lps, M, 0, 0).

build_diff([_]) -> [];
build_diff(List) ->
    build_diff_rev(List, []).

build_diff_rev([_], Acc) -> lists:reverse(Acc);
build_diff_rev([A,B|Rest], Acc) ->
    Sign = cmp(B, A),
    build_diff_rev([B|Rest], [Sign|Acc]).

cmp(X,Y) when X > Y -> 1;
cmp(X,Y) when X == Y -> 0;
cmp(_,_) -> -1.

make_lps(PatT, M) ->
    L0 = array:new(M, {default,0}),
    make_lps_loop(1, 0, PatT, L0, M).

make_lps_loop(I, Len, PatT, Lps, M) when I < M ->
    LenAdj = adjust_len(Len, PatT, I, Lps),
    LenNew = if element(PatT, LenAdj+1) == element(PatT, I+1) -> LenAdj + 1; true -> LenAdj end,
    Lps2 = array:set(I, LenNew, Lps),
    make_lps_loop(I+1, LenNew, PatT, Lps2, M);
make_lps_loop(_, _, _, Lps, _) ->
    Lps.

adjust_len(Len, PatT, I, Lps) when Len > 0,
   element(PatT, Len+1) =/= element(PatT, I+1) ->
    NewLen = array:get(Len-1, Lps),
    adjust_len(NewLen, PatT, I, Lps);
adjust_len(Len, _, _, _) -> Len.

scan([], _, _, _, _, Count) -> Count;
scan([X|Xs], PatT, Lps, M, K, Count) ->
    K1 = adjust_k(K, X, PatT, Lps),
    K2 = if element(PatT, K1+1) == X -> K1 + 1; true -> K1 end,
    NewCount = case K2 of
        M -> Count + 1;
        _ -> Count
    end,
    NextK = case K2 of
        M -> array:get(M-1, Lps);
        _ -> K2
    end,
    scan(Xs, PatT, Lps, M, NextK, NewCount).

adjust_k(K, X, PatT, Lps) when K > 0,
   element(PatT, K+1) =/= X ->
    NewK = array:get(K-1, Lps),
    adjust_k(NewK, X, PatT, Lps);
adjust_k(K, _, _, _) -> K.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_matching_subarrays(nums :: [integer], pattern :: [integer]) :: integer
  def count_matching_subarrays(nums, pattern) do
    diff = build_diff(nums, [])
    pat_tuple = List.to_tuple(pattern)
    diff_tuple = List.to_tuple(diff)

    m = tuple_size(pat_tuple)
    n2 = tuple_size(diff_tuple)

    if m == 0 or n2 < m do
      0
    else
      lps = build_lps(pat_tuple)
      scan(diff_tuple, pat_tuple, lps, n2, m, 0, 0, 0)
    end
  end

  # Build the difference array where each element is -1, 0 or 1.
  defp build_diff([_], acc), do: Enum.reverse(acc)

  defp build_diff([a, b | rest], acc) do
    sign =
      cond do
        b > a -> 1
        b == a -> 0
        true -> -1
      end

    build_diff([b | rest], [sign | acc])
  end

  # Compute the LPS (failure function) for KMP as a tuple.
  defp build_lps(pat_t) do
    m = tuple_size(pat_t)
    lps_arr = :array.new(m, default: 0)

    {final_arr, _} =
      Enum.reduce(1..(m - 1), {lps_arr, 0}, fn i, {arr, len} ->
        len2 =
          cond do
            elem(pat_t, i) == elem(pat_t, len) ->
              len + 1

            len > 0 ->
              fallback_len(pat_t, arr, len, i)

            true ->
              0
          end

        { :array.set(i, len2, arr), len2 }
      end)

    List.to_tuple(:array.to_list(final_arr))
  end

  defp fallback_len(pat_t, lps_arr, len, i) do
    if len == 0 do
      0
    else
      new_len = :array.get(len - 1, lps_arr)

      if elem(pat_t, i) == elem(pat_t, new_len) do
        new_len + 1
      else
        fallback_len(pat_t, lps_arr, new_len, i)
      end
    end
  end

  # Adjust the current match length using the LPS table.
  defp adjust_j(j, diff_val, pat_t, lps_t) do
    if j > 0 and diff_val != elem(pat_t, j) do
      adjust_j(elem(lps_t, j - 1), diff_val, pat_t, lps_t)
    else
      j
    end
  end

  # Tail‑recursive KMP scan over the difference array.
  defp scan(diff_t, pat_t, lps_t, n, m, i, j, cnt) when i < n do
    diff_val = elem(diff_t, i)
    j_adj = adjust_j(j, diff_val, pat_t, lps_t)

    j_new =
      if diff_val == elem(pat_t, j_adj) do
        j_adj + 1
      else
        j_adj
      end

    cnt2 = if j_new == m, do: cnt + 1, else: cnt
    j_next = if j_new == m, do: elem(lps_t, m - 1), else: j_new

    scan(diff_t, pat_t, lps_t, n, m, i + 1, j_next, cnt2)
  end

  defp scan(_, _, _, _, _, _, _, cnt), do: cnt
end
```
