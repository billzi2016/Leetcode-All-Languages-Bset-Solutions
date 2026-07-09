# 0321. Create Maximum Number

## Cpp

```cpp
class Solution {
public:
    vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
        auto maxSubseq = [&](const vector<int>& nums, int t) {
            vector<int> res;
            int drop = (int)nums.size() - t;
            for (int num : nums) {
                while (!res.empty() && drop > 0 && res.back() < num) {
                    res.pop_back();
                    --drop;
                }
                res.push_back(num);
            }
            if ((int)res.size() > t) res.resize(t);
            return res;
        };
        
        auto greaterSeq = [&](const vector<int>& a, int i, const vector<int>& b, int j) {
            while (i < (int)a.size() && j < (int)b.size() && a[i] == b[j]) {
                ++i; ++j;
            }
            if (j == (int)b.size()) return true;
            if (i == (int)a.size()) return false;
            return a[i] > b[j];
        };
        
        auto merge = [&](const vector<int>& a, const vector<int>& b) {
            vector<int> res;
            int i = 0, j = 0;
            while (i < (int)a.size() || j < (int)b.size()) {
                if (greaterSeq(a, i, b, j))
                    res.push_back(a[i++]);
                else
                    res.push_back(b[j++]);
            }
            return res;
        };
        
        vector<int> best(k, 0);
        int m = nums1.size(), n = nums2.size();
        int start = max(0, k - n), end = min(k, m);
        for (int i = start; i <= end; ++i) {
            vector<int> part1 = maxSubseq(nums1, i);
            vector<int> part2 = maxSubseq(nums2, k - i);
            vector<int> candidate = merge(part1, part2);
            if (greaterSeq(candidate, 0, best, 0))
                best = std::move(candidate);
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int[] maxNumber(int[] nums1, int[] nums2, int k) {
        int m = nums1.length, n = nums2.length;
        int[] best = new int[k];
        boolean initialized = false;
        for (int i = Math.max(0, k - n); i <= Math.min(k, m); i++) {
            int[] part1 = maxSubsequence(nums1, i);
            int[] part2 = maxSubsequence(nums2, k - i);
            int[] candidate = merge(part1, part2);
            if (!initialized || greater(candidate, 0, best, 0)) {
                best = candidate;
                initialized = true;
            }
        }
        return best;
    }

    private int[] maxSubsequence(int[] nums, int t) {
        int len = nums.length;
        int[] stack = new int[t];
        int top = -1;
        int remain = len;
        for (int i = 0; i < len; i++) {
            int num = nums[i];
            while (top >= 0 && stack[top] < num && (top + 1 + (remain - 1)) >= t) {
                top--;
            }
            if (top + 1 < t) {
                stack[++top] = num;
            }
            remain--;
        }
        return stack;
    }

    private int[] merge(int[] a, int[] b) {
        int total = a.length + b.length;
        int[] res = new int[total];
        int i = 0, j = 0, r = 0;
        while (i < a.length && j < b.length) {
            if (greater(a, i, b, j)) {
                res[r++] = a[i++];
            } else {
                res[r++] = b[j++];
            }
        }
        while (i < a.length) {
            res[r++] = a[i++];
        }
        while (j < b.length) {
            res[r++] = b[j++];
        }
        return res;
    }

    private boolean greater(int[] a, int i, int[] b, int j) {
        int alen = a.length, blen = b.length;
        while (i < alen && j < blen && a[i] == b[j]) {
            i++;
            j++;
        }
        if (j == blen) return true;
        if (i == alen) return false;
        return a[i] > b[j];
    }
}
```

## Python

```python
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def max_subsequence(nums, t):
            drop = len(nums) - t
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:t]

        def merge(seq1, seq2):
            i = j = 0
            merged = []
            while i < len(seq1) or j < len(seq2):
                # compare remaining parts lexicographically
                if seq1[i:] > seq2[j:]:
                    merged.append(seq1[i])
                    i += 1
                else:
                    merged.append(seq2[j])
                    j += 1
            return merged

        m, n = len(nums1), len(nums2)
        start = max(0, k - n)
        end = min(k, m)
        best = [0] * k
        for i in range(start, end + 1):
            part1 = max_subsequence(nums1, i)
            part2 = max_subsequence(nums2, k - i)
            candidate = merge(part1, part2)
            if candidate > best:
                best = candidate
        return best
```

## Python3

```python
from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def max_subsequence(nums: List[int], t: int) -> List[int]:
            drop = len(nums) - t
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:t]

        def merge(seq1: List[int], seq2: List[int]) -> List[int]:
            res = []
            i = j = 0
            while i < len(seq1) or j < len(seq2):
                if seq1[i:] > seq2[j:]:
                    res.append(seq1[i])
                    i += 1
                else:
                    res.append(seq2[j])
                    j += 1
            return res

        best = [0] * k
        start = max(0, k - len(nums2))
        end = min(k, len(nums1))
        for i in range(start, end + 1):
            part1 = max_subsequence(nums1, i)
            part2 = max_subsequence(nums2, k - i)
            candidate = merge(part1, part2)
            if candidate > best:
                best = candidate
        return best
```

## C

```c
#include <stdlib.h>

/* Return 1 if the subarray a[i:] is greater than b[j:], otherwise 0 */
static int greater(const int *a, int aSize, int i,
                   const int *b, int bSize, int j) {
    while (i < aSize && j < bSize && a[i] == b[j]) {
        ++i;
        ++j;
    }
    if (j == bSize) return 1;          /* b exhausted */
    if (i == aSize) return 0;          /* a exhausted */
    return a[i] > b[j];
}

/* Build the maximum subsequence of length k from nums[0..n-1] */
static int *maxSubsequence(const int *nums, int n, int k) {
    int drop = n - k;
    int *stack = (int *)malloc(k * sizeof(int));
    int top = 0;                       /* current size of stack */

    for (int i = 0; i < n; ++i) {
        int cur = nums[i];
        while (top > 0 && drop > 0 && stack[top - 1] < cur) {
            --top;
            --drop;
        }
        if (top < k) {
            stack[top++] = cur;
        } else {
            /* discard cur, cannot push because we already have k elements */
        }
    }
    return stack;                      /* size is exactly k */
}

/* Merge two subsequences into the largest possible sequence of length k */
static int *merge(const int *a, int aSize,
                  const int *b, int bSize, int k) {
    int *res = (int *)malloc(k * sizeof(int));
    int i = 0, j = 0, r = 0;
    while (r < k) {
        if (greater(a, aSize, i, b, bSize, j))
            res[r++] = a[i++];
        else
            res[r++] = b[j++];
    }
    return res;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxNumber(int* nums1, int nums1Size,
               int* nums2, int nums2Size,
               int k, int* returnSize) {
    *returnSize = k;
    int start = (k > nums2Size) ? (k - nums2Size) : 0;
    int end   = (k < nums1Size) ? k : nums1Size;

    int *best = NULL;

    for (int i = start; i <= end; ++i) {
        int len1 = i;
        int len2 = k - i;
        if (len1 > nums1Size || len2 > nums2Size) continue;

        int *sub1 = maxSubsequence(nums1, nums1Size, len1);
        int *sub2 = maxSubsequence(nums2, nums2Size, len2);
        int *candidate = merge(sub1, len1, sub2, len2, k);

        if (!best || greater(candidate, k, 0, best, k, 0)) {
            free(best);
            best = candidate;
        } else {
            free(candidate);
        }

        free(sub1);
        free(sub2);
    }
    return best;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution
{
    public int[] MaxNumber(int[] nums1, int[] nums2, int k)
    {
        int start = Math.Max(0, k - nums2.Length);
        int end = Math.Min(k, nums1.Length);
        int[] best = null;
        for (int i = start; i <= end; i++)
        {
            int[] part1 = MaxSubsequence(nums1, i);
            int[] part2 = MaxSubsequence(nums2, k - i);
            int[] candidate = Merge(part1, part2);
            if (best == null || Greater(candidate, 0, best, 0))
                best = candidate;
        }
        return best;
    }

    private static int[] MaxSubsequence(int[] nums, int k)
    {
        int drop = nums.Length - k;
        var result = new List<int>();
        foreach (int num in nums)
        {
            while (drop > 0 && result.Count > 0 && result[result.Count - 1] < num)
            {
                result.RemoveAt(result.Count - 1);
                drop--;
            }
            result.Add(num);
        }
        if (result.Count > k)
            result = result.GetRange(0, k);
        return result.ToArray();
    }

    private static int[] Merge(int[] a, int[] b)
    {
        int i = 0, j = 0;
        var merged = new List<int>(a.Length + b.Length);
        while (i < a.Length || j < b.Length)
        {
            if (Greater(a, i, b, j))
                merged.Add(a[i++]);
            else
                merged.Add(b[j++]);
        }
        return merged.ToArray();
    }

    private static bool Greater(int[] a, int i, int[] b, int j)
    {
        while (i < a.Length && j < b.Length && a[i] == b[j])
        {
            i++;
            j++;
        }
        if (j == b.Length) return true;
        if (i == a.Length) return false;
        return a[i] > b[j];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number[]}
 */
var maxNumber = function(nums1, nums2, k) {
    const maxSubsequence = (nums, t) => {
        const stack = [];
        let drop = nums.length - t;
        for (let num of nums) {
            while (stack.length && drop > 0 && stack[stack.length - 1] < num) {
                stack.pop();
                drop--;
            }
            if (stack.length < t) {
                stack.push(num);
            } else {
                // skip current number
                drop--; // effectively discard this element from consideration
            }
        }
        return stack;
    };
    
    const greater = (arr1, i, arr2, j) => {
        while (i < arr1.length && j < arr2.length && arr1[i] === arr2[j]) {
            i++;
            j++;
        }
        if (j === arr2.length) return true;
        if (i === arr1.length) return false;
        return arr1[i] > arr2[j];
    };
    
    const merge = (arr1, arr2) => {
        const merged = [];
        let i = 0, j = 0;
        while (i < arr1.length || j < arr2.length) {
            if (greater(arr1, i, arr2, j)) {
                merged.push(arr1[i++]);
            } else {
                merged.push(arr2[j++]);
            }
        }
        return merged;
    };
    
    let best = new Array(k).fill(0);
    const start = Math.max(0, k - nums2.length);
    const end = Math.min(k, nums1.length);
    for (let i = start; i <= end; i++) {
        const part1 = maxSubsequence(nums1, i);
        const part2 = maxSubsequence(nums2, k - i);
        const candidate = merge(part1, part2);
        if (greater(candidate, 0, best, 0)) {
            best = candidate;
        }
    }
    return best;
};
```

## Typescript

```typescript
function maxNumber(nums1: number[], nums2: number[], k: number): number[] {
    const m = nums1.length, n = nums2.length;
    let best: number[] = [];

    const start = Math.max(0, k - n);
    const end = Math.min(k, m);

    for (let i = start; i <= end; i++) {
        const part1 = maxSubsequence(nums1, i);
        const part2 = maxSubsequence(nums2, k - i);
        const candidate = merge(part1, part2);
        if (greater(candidate, 0, best, 0)) {
            best = candidate;
        }
    }

    return best;
}

function maxSubsequence(nums: number[], k: number): number[] {
    const drop = nums.length - k;
    const stack: number[] = [];
    let toDrop = drop;

    for (const num of nums) {
        while (toDrop > 0 && stack.length && stack[stack.length - 1] < num) {
            stack.pop();
            toDrop--;
        }
        stack.push(num);
    }

    return stack.slice(0, k);
}

function merge(seq1: number[], seq2: number[]): number[] {
    const merged: number[] = [];
    let i = 0, j = 0;
    while (i < seq1.length || j < seq2.length) {
        if (greater(seq1, i, seq2, j)) {
            merged.push(seq1[i++]);
        } else {
            merged.push(seq2[j++]);
        }
    }
    return merged;
}

function greater(a: number[], i: number, b: number[], j: number): boolean {
    while (i < a.length && j < b.length) {
        if (a[i] > b[j]) return true;
        if (a[i] < b[j]) return false;
        i++;
        j++;
    }
    return (a.length - i) > (b.length - j);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k
     * @return Integer[]
     */
    function maxNumber($nums1, $nums2, $k) {
        $m = count($nums1);
        $n = count($nums2);
        $best = [];

        $start = max(0, $k - $n);
        $end   = min($k, $m);

        for ($i = $start; $i <= $end; $i++) {
            $sub1 = $this->maxSubsequence($nums1, $i);
            $sub2 = $this->maxSubsequence($nums2, $k - $i);
            $candidate = $this->merge($sub1, $sub2);
            if (empty($best) || $this->greater($candidate, $best)) {
                $best = $candidate;
            }
        }

        return $best;
    }

    private function maxSubsequence($nums, $t) {
        $stack = [];
        $drop = count($nums) - $t;

        foreach ($nums as $digit) {
            while (!empty($stack) && $drop > 0 && end($stack) < $digit) {
                array_pop($stack);
                $drop--;
            }
            $stack[] = $digit;
        }

        return array_slice($stack, 0, $t);
    }

    private function merge($seq1, $seq2) {
        $merged = [];

        while (!empty($seq1) || !empty($seq2)) {
            if ($this->greater($seq1, $seq2)) {
                $merged[] = array_shift($seq1);
            } else {
                $merged[] = array_shift($seq2);
            }
        }

        return $merged;
    }

    private function greater($a, $b) {
        $lenA = count($a);
        $lenB = count($b);
        $i = 0;
        while ($i < $lenA && $i < $lenB) {
            if ($a[$i] != $b[$i]) {
                return $a[$i] > $b[$i];
            }
            $i++;
        }
        return $lenA > $lenB;
    }
}
```

## Swift

```swift
class Solution {
    func maxNumber(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> [Int] {
        var best = [Int]()
        let m = nums1.count
        let n = nums2.count
        let start = max(0, k - n)
        let end = min(k, m)
        if start > end { return [] }
        for i in start...end {
            let part1 = maxSubsequence(nums1, i)
            let part2 = maxSubsequence(nums2, k - i)
            let candidate = merge(part1, part2)
            if greater(candidate, 0, best, 0) {
                best = candidate
            }
        }
        return best
    }

    private func maxSubsequence(_ nums: [Int], _ k: Int) -> [Int] {
        var drop = nums.count - k
        var stack = [Int]()
        for num in nums {
            while drop > 0 && !stack.isEmpty && stack.last! < num {
                stack.removeLast()
                drop -= 1
            }
            stack.append(num)
        }
        if stack.count > k {
            return Array(stack[0..<k])
        }
        return stack
    }

    private func merge(_ a: [Int], _ b: [Int]) -> [Int] {
        var i = 0, j = 0
        var result = [Int]()
        while i < a.count || j < b.count {
            if greater(a, i, b, j) {
                result.append(a[i])
                i += 1
            } else {
                result.append(b[j])
                j += 1
            }
        }
        return result
    }

    private func greater(_ a: [Int], _ i: Int, _ b: [Int], _ j: Int) -> Bool {
        var ii = i, jj = j
        while ii < a.count && jj < b.count {
            if a[ii] > b[jj] { return true }
            if a[ii] < b[jj] { return false }
            ii += 1
            jj += 1
        }
        return (a.count - ii) > (b.count - jj)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxNumber(nums1: IntArray, nums2: IntArray, k: Int): IntArray {
        val m = nums1.size
        val n = nums2.size
        var best = IntArray(k)
        var start = kotlin.math.max(0, k - n)
        var end = kotlin.math.min(k, m)
        for (i in start..end) {
            val part1 = maxSubsequence(nums1, i)
            val part2 = maxSubsequence(nums2, k - i)
            val candidate = merge(part1, part2)
            if (greater(candidate, 0, best, 0)) {
                best = candidate
            }
        }
        return best
    }

    private fun maxSubsequence(nums: IntArray, k: Int): IntArray {
        val drop = nums.size - k
        val stack = IntArray(k)
        var top = 0
        var remainDrop = drop
        for (num in nums) {
            while (top > 0 && stack[top - 1] < num && remainDrop > 0) {
                top--
                remainDrop--
            }
            if (top < k) {
                stack[top++] = num
            } else {
                // discard extra numbers; they are effectively dropped
                remainDrop--
            }
        }
        return stack
    }

    private fun merge(seq1: IntArray, seq2: IntArray): IntArray {
        val m = seq1.size
        val n = seq2.size
        val result = IntArray(m + n)
        var i = 0
        var j = 0
        var r = 0
        while (i < m || j < n) {
            if (greater(seq1, i, seq2, j)) {
                result[r++] = seq1[i++]
            } else {
                result[r++] = seq2[j++]
            }
        }
        return result
    }

    private fun greater(arr1: IntArray, i: Int, arr2: IntArray, j: Int): Boolean {
        var ii = i
        var jj = j
        while (ii < arr1.size && jj < arr2.size) {
            if (arr1[ii] != arr2[jj]) return arr1[ii] > arr2[jj]
            ii++
            jj++
        }
        return (arr1.size - i) > (arr2.size - j)
    }
}
```

## Dart

```dart
class Solution {
  List<int> maxNumber(List<int> nums1, List<int> nums2, int k) {
    int m = nums1.length;
    int n = nums2.length;
    List<int> best = List.filled(k, 0);
    for (int i = 0; i <= k; ++i) {
      if (i > m || k - i > n) continue;
      List<int> seq1 = _maxSubsequence(nums1, i);
      List<int> seq2 = _maxSubsequence(nums2, k - i);
      List<int> candidate = _merge(seq1, seq2);
      if (_greater(candidate, 0, best, 0)) {
        best = candidate;
      }
    }
    return best;
  }

  List<int> _maxSubsequence(List<int> nums, int k) {
    if (k == 0) return [];
    int drop = nums.length - k;
    List<int> stack = [];
    for (int num in nums) {
      while (stack.isNotEmpty && drop > 0 && stack.last < num) {
        stack.removeLast();
        drop--;
      }
      stack.add(num);
    }
    if (stack.length > k) {
      return stack.sublist(0, k);
    }
    return List.from(stack);
  }

  List<int> _merge(List<int> a, List<int> b) {
    int i = 0, j = 0;
    List<int> merged = [];
    while (i < a.length || j < b.length) {
      if (_greater(a, i, b, j)) {
        merged.add(a[i]);
        i++;
      } else {
        merged.add(b[j]);
        j++;
      }
    }
    return merged;
  }

  bool _greater(List<int> a, int i, List<int> b, int j) {
    while (i < a.length && j < b.length) {
      if (a[i] != b[j]) return a[i] > b[j];
      i++;
      j++;
    }
    return (a.length - i) > (b.length - j);
  }
}
```

## Golang

```go
func maxNumber(nums1 []int, nums2 []int, k int) []int {
    // helper: get maximum subsequence of length t from nums
    maxSubseq := func(nums []int, t int) []int {
        drop := len(nums) - t
        stack := make([]int, 0, t)
        for _, num := range nums {
            for len(stack) > 0 && drop > 0 && stack[len(stack)-1] < num {
                stack = stack[:len(stack)-1]
                drop--
            }
            if len(stack) < t {
                stack = append(stack, num)
            }
        }
        return stack
    }

    // helper: compare remaining parts of two sequences lexicographically
    greater := func(a []int, i int, b []int, j int) bool {
        for i < len(a) && j < len(b) {
            if a[i] > b[j] {
                return true
            }
            if a[i] < b[j] {
                return false
            }
            i++
            j++
        }
        return (len(a)-i) > (len(b)-j)
    }

    // helper: merge two sequences into the largest possible one
    merge := func(a, b []int) []int {
        i, j := 0, 0
        merged := make([]int, 0, len(a)+len(b))
        for i < len(a) || j < len(b) {
            if greater(a, i, b, j) {
                merged = append(merged, a[i])
                i++
            } else {
                merged = append(merged, b[j])
                j++
            }
        }
        return merged
    }

    m, n := len(nums1), len(nums2)
    start := 0
    if k-n > 0 {
        start = k - n
    }
    end := k
    if m < end {
        end = m
    }

    var best []int
    for i := start; i <= end; i++ {
        j := k - i
        subseq1 := maxSubseq(nums1, i)
        subseq2 := maxSubseq(nums2, j)
        candidate := merge(subseq1, subseq2)
        if len(best) == 0 || greater(candidate, 0, best, 0) {
            best = candidate
        }
    }
    return best
}
```

## Ruby

```ruby
def max_subsequence(nums, t)
  drop = nums.length - t
  stack = []
  nums.each do |num|
    while !stack.empty? && drop > 0 && stack[-1] < num
      stack.pop
      drop -= 1
    end
    stack << num
  end
  stack[0, t]
end

def greater(seq1, i, seq2, j)
  while i < seq1.length && j < seq2.length && seq1[i] == seq2[j]
    i += 1
    j += 1
  end
  return true if j == seq2.length
  return false if i == seq1.length
  seq1[i] > seq2[j]
end

def merge(seq1, seq2)
  i = j = 0
  merged = []
  while i < seq1.length || j < seq2.length
    if greater(seq1, i, seq2, j)
      merged << seq1[i]
      i += 1
    else
      merged << seq2[j]
      j += 1
    end
  end
  merged
end

def max_number(nums1, nums2, k)
  best = nil
  start = [0, k - nums2.length].max
  finish = [k, nums1.length].min
  (start..finish).each do |i|
    seq1 = max_subsequence(nums1, i)
    seq2 = max_subsequence(nums2, k - i)
    candidate = merge(seq1, seq2)
    best = candidate if best.nil? || candidate > best
  end
  best
end
```

## Scala

```scala
object Solution {
    def maxNumber(nums1: Array[Int], nums2: Array[Int], k: Int): Array[Int] = {
        val m = nums1.length
        val n = nums2.length
        var best: Array[Int] = new Array[Int](0)
        val start = Math.max(0, k - n)
        val end = Math.min(k, m)
        for (i <- start to end) {
            val part1 = maxSubsequence(nums1, i)
            val part2 = maxSubsequence(nums2, k - i)
            val candidate = merge(part1, part2)
            if (greater(candidate, 0, best, 0)) best = candidate
        }
        best
    }

    private def maxSubsequence(nums: Array[Int], t: Int): Array[Int] = {
        val drop = nums.length - t
        val stack = new scala.collection.mutable.ArrayBuffer[Int]()
        var toDrop = drop
        for (num <- nums) {
            while (stack.nonEmpty && toDrop > 0 && stack.last < num) {
                stack.remove(stack.size - 1)
                toDrop -= 1
            }
            stack.append(num)
        }
        stack.take(t).toArray
    }

    private def merge(seq1: Array[Int], seq2: Array[Int]): Array[Int] = {
        val res = new scala.collection.mutable.ArrayBuffer[Int]()
        var i = 0
        var j = 0
        while (i < seq1.length || j < seq2.length) {
            if (greater(seq1, i, seq2, j)) {
                res.append(seq1(i))
                i += 1
            } else {
                res.append(seq2(j))
                j += 1
            }
        }
        res.toArray
    }

    private def greater(a: Array[Int], i: Int, b: Array[Int], j: Int): Boolean = {
        var ii = i
        var jj = j
        while (ii < a.length && jj < b.length) {
            if (a(ii) != b(jj)) return a(ii) > b(jj)
            ii += 1
            jj += 1
        }
        // If we reached the end of one array, the other is considered greater.
        if (jj == b.length) true else false
    }
}
```

## Rust

```rust
use std::cmp;

fn max_subsequence(nums: &[i32], t: usize) -> Vec<i32> {
    let mut drop = nums.len() - t;
    let mut stack: Vec<i32> = Vec::with_capacity(t);
    for &num in nums {
        while drop > 0 && !stack.is_empty() && *stack.last().unwrap() < num {
            stack.pop();
            drop -= 1;
        }
        stack.push(num);
    }
    stack.truncate(t);
    stack
}

fn greater(seq1: &[i32], i: usize, seq2: &[i32], j: usize) -> bool {
    let mut a = i;
    let mut b = j;
    while a < seq1.len() && b < seq2.len() {
        if seq1[a] != seq2[b] {
            return seq1[a] > seq2[b];
        }
        a += 1;
        b += 1;
    }
    (seq1.len() - a) > (seq2.len() - b)
}

fn merge(seq1: &[i32], seq2: &[i32]) -> Vec<i32> {
    let mut i = 0usize;
    let mut j = 0usize;
    let total = seq1.len() + seq2.len();
    let mut res = Vec::with_capacity(total);
    while i < seq1.len() || j < seq2.len() {
        if greater(seq1, i, seq2, j) {
            res.push(seq1[i]);
            i += 1;
        } else {
            res.push(seq2[j]);
            j += 1;
        }
    }
    res
}

impl Solution {
    pub fn max_number(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> Vec<i32> {
        let m = nums1.len();
        let n = nums2.len();
        let k_usize = k as usize;
        let mut best: Vec<i32> = Vec::new();

        let start = if k_usize > n { k_usize - n } else { 0 };
        let end = cmp::min(k_usize, m);
        for i in start..=end {
            let part1 = max_subsequence(&nums1, i);
            let part2 = max_subsequence(&nums2, k_usize - i);
            let candidate = merge(&part1, &part2);
            if greater(&candidate, 0, &best, 0) {
                best = candidate;
            }
        }
        best
    }
}
```

## Racket

```racket
(define (take lst n)
  (if (or (= n 0) (null? lst))
      '()
      (cons (car lst) (take (cdr lst) (- n 1)))))

(define (greater? a b)
  (cond [(null? a) #f]
        [(null? b) #t]
        [else (let ((x (car a)) (y (car b)))
                (if (> x y) #t
                    (if (< x y) #f
                        (greater? (cdr a) (cdr b)))))]))

(define (max-subseq nums t)
  (let* ((drop (- (length nums) t))
         (stack
          (let loop ((lst nums) (stk '()) (d drop))
            (if (null? lst)
                (reverse stk)
                (let ((digit (car lst)))
                  (let recur ((s stk) (dd d))
                    (if (and (> dd 0) (not (null? s)) (< (car s) digit))
                        (recur (cdr s) (- dd 1))
                        (loop (cdr lst) (cons digit s) dd))))))))
    (take stack t)))

(define (merge seq1 seq2)
  (let loop ((a seq1) (b seq2) (res '()))
    (cond [(null? a) (reverse (append res b))]
          [(null? b) (reverse (append res a))]
          [else (if (greater? a b)
                    (loop (cdr a) b (cons (car a) res))
                    (loop a (cdr b) (cons (car b) res)))])))

(define/contract (max-number nums1 nums2 k)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ((m (length nums1))
         (n (length nums2))
         (start (max 0 (- k n)))
         (end (min k m)))
    (let loop ((i start) (best '()))
      (if (> i end)
          best
          (let* ((sub1 (max-subseq nums1 i))
                 (sub2 (max-subseq nums2 (- k i)))
                 (candidate (merge sub1 sub2)))
            (loop (+ i 1)
                  (if (or (null? best) (greater? candidate best))
                      candidate
                      best)))))))
```

## Erlang

```erlang
-module(solution).
-export([max_number/3]).

-spec max_number(Nums1 :: [integer()], Nums2 :: [integer()], K :: integer()) -> [integer()].
max_number(Nums1, Nums2, K) ->
    Len1 = length(Nums1),
    Len2 = length(Nums2),
    StartI = erlang:max(0, K - Len2),
    EndI   = erlang:min(K, Len1),
    lists:foldl(
        fun(I, Best) ->
            Seq1 = max_subsequence(Nums1, I),
            Seq2 = max_subsequence(Nums2, K - I),
            Candidate = merge(Seq1, Seq2),
            case greater(Candidate, Best) of
                true -> Candidate;
                false -> Best
            end
        end,
        [],
        lists:seq(StartI, EndI)
    ).

%% Build the maximum subsequence of length T from List preserving order.
-spec max_subsequence([integer()], integer()) -> [integer()].
max_subsequence(_, 0) ->
    [];
max_subsequence(List, T) ->
    Drop = length(List) - T,
    Stack = build_stack(List, [], Drop),
    lists:sublist(lists:reverse(Stack), T).

%% Helper to construct stack with possible drops.
-spec build_stack([integer()], [integer()], integer()) -> [integer()].
build_stack([], Stack, _) ->
    Stack;
build_stack([H|Rest], [], Drop) ->
    build_stack(Rest, [H], Drop);
build_stack([H|Rest], [Top|Tail]=Stack, Drop) when Drop > 0, Top < H ->
    build_stack([H|Rest], Tail, Drop - 1);
build_stack([H|Rest], Stack, Drop) ->
    build_stack(Rest, [H|Stack], Drop).

%% Merge two sequences into the lexicographically maximum result.
-spec merge([integer()], [integer()]) -> [integer()].
merge([], B) -> B;
merge(A, []) -> A;
merge([HA|TA]=A, [HB|TB]=B) ->
    case greater(A, B) of
        true  -> [HA | merge(TA, B)];
        false -> [HB | merge(A, TB)]
    end.

%% Compare two lists lexicographically.
-spec greater([integer()], [integer()]) -> boolean().
greater([], []) -> false;
greater([], _)  -> false;
greater(_, [])  -> true;
greater([H1|T1], [H2|T2]) ->
    if
        H1 > H2 -> true;
        H1 < H2 -> false;
        true    -> greater(T1, T2)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_number(nums1 :: [integer], nums2 :: [integer], k :: integer) :: [integer]
  def max_number(nums1, nums2, k) do
    m = length(nums1)
    n = length(nums2)

    start_i = max(0, k - n)
    end_i = min(k, m)

    Enum.reduce(start_i..end_i, [], fn i, best ->
      seq1 = max_subseq(nums1, i)
      seq2 = max_subseq(nums2, k - i)
      merged = merge(seq1, seq2)

      if greater?(merged, best), do: merged, else: best
    end)
  end

  # Get the maximum subsequence of length t from nums preserving order.
  defp max_subseq(nums, t) do
    drop = length(nums) - t

    {stack_rev, _} =
      Enum.reduce(nums, {[], drop}, fn digit, {stack, d} ->
        pop_and_push(digit, stack, d)
      end)

    stack_rev
    |> Enum.reverse()
    |> Enum.take(t)
  end

  # Pops smaller elements while possible and then pushes the current digit.
  defp pop_and_push(digit, stack, drop) do
    cond do
      drop > 0 && stack != [] && hd(stack) < digit ->
        pop_and_push(digit, tl(stack), drop - 1)

      true ->
        {[digit | stack], drop}
    end
  end

  # Merge two sequences into the lexicographically largest sequence.
  defp merge([], b), do: b
  defp merge(a, []), do: a

  defp merge([ah | at] = a, [bh | bt] = b) do
    if greater?(a, b) do
      [ah | merge(at, b)]
    else
      [bh | merge(a, bt)]
    end
  end

  # Returns true if list a is lexicographically greater than list b.
  defp greater?([], []), do: false
  defp greater?([], _), do: false
  defp greater?(_, []), do: true

  defp greater?([ah | at], [bh | bt]) do
    cond do
      ah > bh -> true
      ah < bh -> false
      true -> greater?(at, bt)
    end
  end
end
```
