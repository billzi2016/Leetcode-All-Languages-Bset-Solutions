# 1960. Maximum Product of the Length of Two Palindromic Substrings

## Cpp

```cpp
class Solution {
public:
    long long maxProduct(string s) {
        int n = s.size();
        vector<int> d1(n);
        int l = 0, r = -1;
        for (int i = 0; i < n; ++i) {
            int k = (i > r) ? 1 : min(d1[l + r - i], r - i + 1);
            while (i - k >= 0 && i + k < n && s[i - k] == s[i + k]) ++k;
            d1[i] = k;
            if (i + k - 1 > r) {
                l = i - k + 1;
                r = i + k - 1;
            }
        }

        vector<long long> maxEnd(n, 0), maxStart(n, 0);

        // compute max palindrome length ending exactly at each position
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pqEnd; // (center, rightReach)
        for (int e = 0; e < n; ++e) {
            int reach = e + d1[e] - 1;
            pqEnd.emplace(e, reach);
            while (!pqEnd.empty() && pqEnd.top().second < e) pqEnd.pop();
            if (!pqEnd.empty()) {
                int i = pqEnd.top().first;
                maxEnd[e] = 2LL * (e - i) + 1;
            }
        }

        // compute max palindrome length starting exactly at each position
        priority_queue<pair<int,int>> pqStart; // (center, leftReach)
        for (int p = n - 1; p >= 0; --p) {
            int left = p - d1[p] + 1;
            pqStart.emplace(p, left);
            while (!pqStart.empty() && pqStart.top().second > p) pqStart.pop();
            if (!pqStart.empty()) {
                int i = pqStart.top().first;
                maxStart[p] = 2LL * (i - p) + 1;
            }
        }

        vector<long long> pref(n), suff(n);
        pref[0] = maxEnd[0];
        for (int i = 1; i < n; ++i) pref[i] = max(pref[i-1], maxEnd[i]);
        suff[n-1] = maxStart[n-1];
        for (int i = n - 2; i >= 0; --i) suff[i] = max(suff[i+1], maxStart[i]);

        long long ans = 0;
        for (int i = 0; i < n - 1; ++i) {
            ans = max(ans, pref[i] * suff[i + 1]);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long maxProduct(String s) {
        int n = s.length();
        int[] d1 = new int[n];
        // Manacher's algorithm for odd length palindromes
        int l = 0, r = -1;
        for (int i = 0; i < n; i++) {
            int k = (i > r) ? 1 : Math.min(d1[l + r - i], r - i + 1);
            while (i - k >= 0 && i + k < n && s.charAt(i - k) == s.charAt(i + k)) {
                k++;
            }
            d1[i] = k;
            if (i + k - 1 > r) {
                l = i - k + 1;
                r = i + k - 1;
            }
        }

        // Prefix: maximum palindrome length ending at each position
        int[] bestEndLen = new int[n];
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0])); // min c
        for (int i = 0; i < n; i++) {
            int maxEnd = i + d1[i] - 1;
            pq.offer(new int[]{i, maxEnd});
            while (!pq.isEmpty() && pq.peek()[1] < i) {
                pq.poll();
            }
            if (!pq.isEmpty()) {
                int c = pq.peek()[0];
                bestEndLen[i] = 2 * (i - c) + 1;
            } else {
                bestEndLen[i] = 0;
            }
        }

        int[] prefixMax = new int[n];
        for (int i = 0; i < n; i++) {
            if (i == 0) prefixMax[i] = bestEndLen[i];
            else prefixMax[i] = Math.max(prefixMax[i - 1], bestEndLen[i]);
        }

        // Suffix: maximum palindrome length starting at each position
        int[] bestStartLen = new int[n];
        PriorityQueue<int[]> pq2 = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0])); // max c
        for (int i = n - 1; i >= 0; i--) {
            int minStart = i - d1[i] + 1;
            pq2.offer(new int[]{i, minStart});
            while (!pq2.isEmpty() && pq2.peek()[1] > i) {
                pq2.poll();
            }
            if (!pq2.isEmpty()) {
                int c = pq2.peek()[0];
                bestStartLen[i] = 2 * (c - i) + 1;
            } else {
                bestStartLen[i] = 0;
            }
        }

        int[] suffixMax = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            if (i == n - 1) suffixMax[i] = bestStartLen[i];
            else suffixMax[i] = Math.max(suffixMax[i + 1], bestStartLen[i]);
        }

        long ans = 0;
        for (int i = 0; i < n - 1; i++) {
            long prod = (long) prefixMax[i] * suffixMax[i + 1];
            if (prod > ans) ans = prod;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # Manacher's algorithm for odd length palindromes
        d1 = [0] * n
        l = 0
        r = -1
        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d1[i] = k
            if i + k - 1 > r:
                l = i - k + 1
                r = i + k - 1

        max_len_end = [0] * n   # longest odd palindrome ending at position i
        max_len_start = [0] * n # longest odd palindrome starting at position i

        for i in range(n):
            radius = d1[i]
            length = 2 * radius - 1
            left = i - radius + 1
            right = i + radius - 1
            if max_len_end[right] < length:
                max_len_end[right] = length
            if max_len_start[left] < length:
                max_len_start[left] = length

        # best palindrome length for each prefix (ending <= i)
        best_left = [0] * n
        cur = 0
        for i in range(n):
            if cur < max_len_end[i]:
                cur = max_len_end[i]
            best_left[i] = cur

        # best palindrome length for each suffix (starting >= i)
        best_right = [0] * n
        cur = 0
        for i in range(n - 1, -1, -1):
            if cur < max_len_start[i]:
                cur = max_len_start[i]
            best_right[i] = cur

        ans = 0
        for i in range(n - 1):
            prod = best_left[i] * best_right[i + 1]
            if prod > ans:
                ans = prod
        return ans
```

## Python3

```python
class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        # Manacher's algorithm for odd-length palindromes
        d1 = [0] * n  # radius count (palindrome length = 2*d1[i]-1)
        l = 0
        r = -1
        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d1[i] = k
            k -= 1
            if i + k > r:
                l = i - k
                r = i + k

        best_end_at = [0] * n   # max palindrome length ending at position i
        best_start_at = [0] * n # max palindrome length starting at position i

        for i in range(n):
            rad = d1[i] - 1
            length = 2 * rad + 1
            left = i - rad
            right = i + rad
            if best_end_at[right] < length:
                best_end_at[right] = length
            if best_start_at[left] < length:
                best_start_at[left] = length

        pref_max = [0] * n
        cur = 0
        for i in range(n):
            if best_end_at[i] > cur:
                cur = best_end_at[i]
            pref_max[i] = cur

        suff_max = [0] * n
        cur = 0
        for i in range(n - 1, -1, -1):
            if best_start_at[i] > cur:
                cur = best_start_at[i]
            suff_max[i] = cur

        ans = 0
        for i in range(n - 1):
            prod = pref_max[i] * suff_max[i + 1]
            if prod > ans:
                ans = prod
        return ans
```

## C

```c
#include <string.h>
#include <stdlib.h>

long long maxProduct(char* s) {
    int n = (int)strlen(s);
    if (n < 2) return 0;
    
    // Manacher odd-length radii
    int *d1 = (int*)malloc(n * sizeof(int));
    int l = 0, r = -1;
    for (int i = 0; i < n; ++i) {
        int k = (i > r) ? 1 : (d1[l + r - i] < (r - i + 1) ? d1[l + r - i] : (r - i + 1));
        while (i - k >= 0 && i + k < n && s[i - k] == s[i + k]) ++k;
        d1[i] = k;
        if (i + k - 1 > r) {
            l = i - k + 1;
            r = i + k - 1;
        }
    }
    
    int *pref = (int*)calloc(n, sizeof(int));
    int *suff = (int*)calloc(n, sizeof(int));
    
    // Fill pref with max palindrome length ending at each position
    for (int i = 0; i < n; ++i) {
        int rad = d1[i];
        int len = 2 * rad - 1;
        int right = i + rad - 1;
        if (len > pref[right]) pref[right] = len;
    }
    for (int i = 1; i < n; ++i) {
        if (pref[i-1] > pref[i]) pref[i] = pref[i-1];
    }
    
    // Fill suff with max palindrome length starting at each position
    for (int i = 0; i < n; ++i) {
        int rad = d1[i];
        int len = 2 * rad - 1;
        int left = i - rad + 1;
        if (len > suff[left]) suff[left] = len;
    }
    for (int i = n - 2; i >= 0; --i) {
        if (suff[i+1] > suff[i]) suff[i] = suff[i+1];
    }
    
    long long ans = 0;
    for (int i = 0; i < n - 1; ++i) {
        long long prod = (long long)pref[i] * (long long)suff[i + 1];
        if (prod > ans) ans = prod;
    }
    
    free(d1);
    free(pref);
    free(suff);
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public long MaxProduct(string s) {
        int n = s.Length;
        char[] ch = s.ToCharArray();
        int[] d1 = new int[n];
        int l = 0, r = -1;
        for (int i = 0; i < n; i++) {
            int k = (i > r) ? 1 : Math.Min(d1[l + r - i], r - i + 1);
            while (i - k >= 0 && i + k < n && ch[i - k] == ch[i + k]) {
                k++;
            }
            d1[i] = k;
            if (i + k - 1 > r) {
                l = i - k + 1;
                r = i + k - 1;
            }
        }

        int[] maxEnd = new int[n];
        int[] maxStart = new int[n];

        for (int i = 0; i < n; i++) {
            int len = 2 * d1[i] - 1;
            int right = i + d1[i] - 1;
            if (len > maxEnd[right]) maxEnd[right] = len;

            int left = i - d1[i] + 1;
            if (len > maxStart[left]) maxStart[left] = len;
        }

        int[] pref = new int[n];
        pref[0] = maxEnd[0];
        for (int i = 1; i < n; i++) {
            pref[i] = Math.Max(pref[i - 1], maxEnd[i]);
        }

        int[] suff = new int[n];
        suff[n - 1] = maxStart[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suff[i] = Math.Max(suff[i + 1], maxStart[i]);
        }

        long ans = 0;
        for (int i = 0; i < n - 1; i++) {
            long prod = (long)pref[i] * suff[i + 1];
            if (prod > ans) ans = prod;
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maxProduct = function(s) {
    const n = s.length;
    // Manacher's algorithm for odd-length palindromes
    const d1 = new Array(n);
    let l = 0, r = -1;
    for (let i = 0; i < n; ++i) {
        let k = (i > r) ? 1 : Math.min(d1[l + r - i], r - i + 1);
        while (i - k >= 0 && i + k < n && s[i - k] === s[i + k]) {
            ++k;
        }
        d1[i] = k;
        if (i + k - 1 > r) {
            l = i - k + 1;
            r = i + k - 1;
        }
    }

    const maxEnd = new Array(n).fill(0);   // longest odd palindrome ending at position i
    const maxStart = new Array(n).fill(0); // longest odd palindrome starting at position i

    for (let i = 0; i < n; ++i) {
        const len = 2 * d1[i] - 1;
        const L = i - (d1[i] - 1);
        const R = i + (d1[i] - 1);
        if (len > maxEnd[R]) maxEnd[R] = len;
        if (len > maxStart[L]) maxStart[L] = len;
    }

    const pref = new Array(n).fill(0);
    pref[0] = maxEnd[0];
    for (let i = 1; i < n; ++i) {
        pref[i] = Math.max(pref[i - 1], maxEnd[i]);
    }

    const suff = new Array(n).fill(0);
    suff[n - 1] = maxStart[n - 1];
    for (let i = n - 2; i >= 0; --i) {
        suff[i] = Math.max(suff[i + 1], maxStart[i]);
    }

    let ans = 0;
    for (let split = 0; split < n - 1; ++split) {
        const prod = pref[split] * suff[split + 1];
        if (prod > ans) ans = prod;
    }
    return ans;
};
```

## Typescript

```typescript
function maxProduct(s: string): number {
    const n = s.length;
    const rad = new Array<number>(n);
    let l = 0, r = -1;
    for (let i = 0; i < n; i++) {
        let k = (i > r) ? 1 : Math.min(rad[l + r - i], r - i + 1);
        while (i - k >= 0 && i + k < n && s[i - k] === s[i + k]) {
            ++k;
        }
        rad[i] = k;
        if (i + k - 1 > r) {
            l = i - k + 1;
            r = i + k - 1;
        }
    }

    const pref = new Array<number>(n).fill(0);
    const suff = new Array<number>(n).fill(0);

    for (let i = 0; i < n; i++) {
        const len = 2 * rad[i] - 1;
        const start = i - (rad[i] - 1);
        const end = i + (rad[i] - 1);
        if (pref[end] < len) pref[end] = len;
        if (suff[start] < len) suff[start] = len;
    }

    for (let i = 1; i < n; i++) {
        if (pref[i] < pref[i - 1]) pref[i] = pref[i - 1];
    }
    for (let i = n - 2; i >= 0; i--) {
        if (suff[i] < suff[i + 1]) suff[i] = suff[i + 1];
    }

    let ans = 0;
    for (let i = 0; i < n - 1; i++) {
        const prod = pref[i] * suff[i + 1];
        if (prod > ans) ans = prod;
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function maxProduct($s) {
        $n = strlen($s);
        // Manacher's algorithm for odd length palindromes
        $d1 = array_fill(0, $n, 0);
        $l = 0;
        $r = -1;
        for ($i = 0; $i < $n; $i++) {
            $k = ($i > $r) ? 1 : min($d1[$l + $r - $i], $r - $i + 1);
            while ($i - $k >= 0 && $i + $k < $n && $s[$i - $k] === $s[$i + $k]) {
                $k++;
            }
            $d1[$i] = $k;
            if ($i + $k - 1 > $r) {
                $l = $i - $k + 1;
                $r = $i + $k - 1;
            }
        }

        // Prepare interval events
        $startAt = array_fill(0, $n, []);
        $endAt   = array_fill(0, $n, []);
        for ($c = 0; $c < $n; $c++) {
            $radius = $d1[$c];
            $L = $c - ($radius - 1);
            $R = $c + ($radius - 1);
            $interval = ['c' => $c, 'L' => $L, 'R' => $R];
            $startAt[$L][] = $interval;
            $endAt[$R][]   = $interval;
        }

        // Max palindrome length ending at each position (prefix)
        $maxLenLeft = array_fill(0, $n, 0);
        $pq = new SplPriorityQueue();               // min-heap by center using negative priority
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        for ($pos = 0; $pos < $n; $pos++) {
            foreach ($startAt[$pos] as $inter) {
                $pq->insert($inter, -$inter['c']);
            }
            while (!$pq->isEmpty()) {
                $top = $pq->top();
                if ($top['R'] < $pos) {
                    $pq->extract();
                } else {
                    break;
                }
            }
            if (!$pq->isEmpty()) {
                $minC = $pq->top()['c'];
                $maxLenLeft[$pos] = 2 * $pos - 2 * $minC + 1;
            }
        }

        // Prefix maximums
        $pref = array_fill(0, $n, 0);
        $pref[0] = $maxLenLeft[0];
        for ($i = 1; $i < $n; $i++) {
            $pref[$i] = max($pref[$i - 1], $maxLenLeft[$i]);
        }

        // Max palindrome length starting at each position (suffix)
        $maxLenRight = array_fill(0, $n, 0);
        $pq2 = new SplPriorityQueue();              // max-heap by center (default priority)
        $pq2->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        for ($pos = $n - 1; $pos >= 0; $pos--) {
            foreach ($endAt[$pos] as $inter) {
                $pq2->insert($inter, $inter['c']);
            }
            while (!$pq2->isEmpty()) {
                $top = $pq2->top();
                if ($top['L'] > $pos) {
                    $pq2->extract();
                } else {
                    break;
                }
            }
            if (!$pq2->isEmpty()) {
                $maxC = $pq2->top()['c'];
                $maxLenRight[$pos] = 2 * $maxC - 2 * $pos + 1;
            }
        }

        // Suffix maximums
        $suf = array_fill(0, $n, 0);
        $suf[$n - 1] = $maxLenRight[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) {
            $suf[$i] = max($suf[$i + 1], $maxLenRight[$i]);
        }

        // Compute answer
        $ans = 0;
        for ($i = 0; $i < $n - 1; $i++) {
            $product = $pref[$i] * $suf[$i + 1];
            if ($product > $ans) {
                $ans = $product;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxProduct(_ s: String) -> Int {
        let chars = Array(s.utf8)
        let n = chars.count
        if n < 2 { return 0 }
        
        // Manacher's algorithm for odd length palindromes
        var d1 = [Int](repeating: 0, count: n)
        var l = 0
        var r = -1
        for i in 0..<n {
            var k = (i > r) ? 1 : min(d1[l + r - i], r - i + 1)
            while i - k >= 0 && i + k < n && chars[i - k] == chars[i + k] {
                k += 1
            }
            d1[i] = k
            if i + k - 1 > r {
                l = i - k + 1
                r = i + k - 1
            }
        }
        
        var bestLeft = [Int](repeating: 0, count: n)
        var bestRight = [Int](repeating: 0, count: n)
        
        for c in 0..<n {
            let radius = d1[c]
            let len = 2 * radius - 1
            let left = c - (radius - 1)
            let right = c + (radius - 1)
            if bestLeft[right] < len { bestLeft[right] = len }
            if bestRight[left] < len { bestRight[left] = len }
        }
        
        // Prefix maximums
        for i in 1..<n {
            if bestLeft[i] < bestLeft[i - 1] {
                bestLeft[i] = bestLeft[i - 1]
            }
        }
        // Suffix maximums
        if n >= 2 {
            for i in stride(from: n - 2, through: 0, by: -1) {
                if bestRight[i] < bestRight[i + 1] {
                    bestRight[i] = bestRight[i + 1]
                }
            }
        }
        
        var answer = 0
        for i in 0..<(n - 1) {
            let prod = bestLeft[i] * bestRight[i + 1]
            if prod > answer { answer = prod }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxProduct(s: String): Long {
        val n = s.length
        val d = IntArray(n)
        var l = 0
        var r = -1
        for (i in 0 until n) {
            var k = if (i > r) 1 else kotlin.math.min(d[l + r - i], r - i + 1)
            while (i - k >= 0 && i + k < n && s[i - k] == s[i + k]) {
                k++
            }
            d[i] = k
            if (i + k - 1 > r) {
                l = i - k + 1
                r = i + k - 1
            }
        }

        val leftMax = IntArray(n)
        val rightMax = IntArray(n)

        for (c in 0 until n) {
            val rad = d[c] - 1
            val len = rad * 2 + 1
            val start = c - rad
            val end = c + rad
            if (len > leftMax[end]) leftMax[end] = len
            if (len > rightMax[start]) rightMax[start] = len
        }

        for (i in 1 until n) {
            if (leftMax[i - 1] > leftMax[i]) leftMax[i] = leftMax[i - 1]
        }
        for (i in n - 2 downTo 0) {
            if (rightMax[i + 1] > rightMax[i]) rightMax[i] = rightMax[i + 1]
        }

        var ans = 0L
        for (i in 0 until n - 1) {
            val prod = leftMax[i].toLong() * rightMax[i + 1].toLong()
            if (prod > ans) ans = prod
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxProduct(String s) {
    int n = s.length;
    List<int> d1 = List.filled(n, 0);
    int l = 0, r = -1;
    for (int i = 0; i < n; i++) {
      int k = (i > r) ? 1 : (d1[l + r - i] < r - i + 1 ? d1[l + r - i] : r - i + 1);
      while (i - k >= 0 && i + k < n && s[i - k] == s[i + k]) {
        k++;
      }
      d1[i] = k;
      if (i + k - 1 > r) {
        l = i - k + 1;
        r = i + k - 1;
      }
    }

    List<int> bestEnd = List.filled(n, 0);
    List<int> bestStart = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      int radius = d1[i];
      int len = 2 * radius - 1;
      int left = i - (radius - 1);
      int right = i + (radius - 1);
      if (len > bestEnd[right]) bestEnd[right] = len;
      if (len > bestStart[left]) bestStart[left] = len;
    }

    List<int> pref = List.filled(n, 0);
    int cur = 0;
    for (int i = 0; i < n; i++) {
      if (bestEnd[i] > cur) cur = bestEnd[i];
      pref[i] = cur;
    }

    List<int> suff = List.filled(n, 0);
    cur = 0;
    for (int i = n - 1; i >= 0; i--) {
      if (bestStart[i] > cur) cur = bestStart[i];
      suff[i] = cur;
    }

    int ans = 0;
    for (int i = 0; i < n - 1; i++) {
      int prod = pref[i] * suff[i + 1];
      if (prod > ans) ans = prod;
    }
    return ans;
  }
}
```

## Golang

```go
func maxProduct(s string) int64 {
    n := len(s)
    rad := make([]int, n)
    l, r := 0, -1
    for i := 0; i < n; i++ {
        k := 1
        if i <= r {
            mirror := l + r - i
            if rad[mirror] < r-i+1 {
                k = rad[mirror]
            } else {
                k = r - i + 1
            }
        }
        for i-k >= 0 && i+k < n && s[i-k] == s[i+k] {
            k++
        }
        rad[i] = k - 1
        if i+rad[i] > r {
            l = i - rad[i]
            r = i + rad[i]
        }
    }

    endMax := make([]int, n)
    startMax := make([]int, n)

    for c := 0; c < n; c++ {
        length := 2*rad[c] + 1
        L := c - rad[c]
        R := c + rad[c]
        if length > endMax[R] {
            endMax[R] = length
        }
        if length > startMax[L] {
            startMax[L] = length
        }
    }

    prefix := make([]int, n)
    cur := 0
    for i := 0; i < n; i++ {
        if endMax[i] > cur {
            cur = endMax[i]
        }
        prefix[i] = cur
    }

    suffix := make([]int, n)
    cur = 0
    for i := n - 1; i >= 0; i-- {
        if startMax[i] > cur {
            cur = startMax[i]
        }
        suffix[i] = cur
    }

    var ans int64 = 0
    for i := 0; i < n-1; i++ {
        prod := int64(prefix[i]) * int64(suffix[i+1])
        if prod > ans {
            ans = prod
        }
    }
    return ans
}
```

## Ruby

```ruby
def max_product(s)
  n = s.length
  d1 = Array.new(n, 0)
  l = 0
  r = -1
  (0...n).each do |i|
    k = i > r ? 1 : [d1[l + r - i], r - i + 1].min
    while i - k >= 0 && i + k < n && s[i - k] == s[i + k]
      k += 1
    end
    d1[i] = k
    if i + k - 1 > r
      l = i - k + 1
      r = i + k - 1
    end
  end

  left_max = Array.new(n, 0)
  right_max = Array.new(n, 0)

  (0...n).each do |center|
    radius = d1[center] - 1
    length = radius * 2 + 1
    l_idx = center - radius
    r_idx = center + radius
    left_max[r_idx] = length if length > left_max[r_idx]
    right_max[l_idx] = length if length > right_max[l_idx]
  end

  (1...n).each do |i|
    left_max[i] = left_max[i - 1] if left_max[i - 1] > left_max[i]
  end
  (n - 2).downto(0) do |i|
    right_max[i] = right_max[i + 1] if right_max[i + 1] > right_max[i]
  end

  ans = 0
  (0...n - 1).each do |i|
    prod = left_max[i] * right_max[i + 1]
    ans = prod if prod > ans
  end
  ans
end
```

## Scala

```scala
object Solution {
    def maxProduct(s: String): Long = {
        val n = s.length
        if (n < 2) return 0L

        // Manacher's algorithm for odd length palindromes
        val rad = new Array[Int](n)
        var center = 0
        var right = -1
        for (i <- 0 until n) {
            var r = 0
            if (i <= right) {
                val mirror = 2 * center - i
                r = Math.min(rad(mirror), right - i)
            }
            while (i - r - 1 >= 0 && i + r + 1 < n && s.charAt(i - r - 1) == s.charAt(i + r + 1)) {
                r += 1
            }
            rad(i) = r
            if (i + r > right) {
                center = i
                right = i + r
            }
        }

        // best palindrome length ending at each position, and starting at each position
        val bestEnd = new Array[Int](n)
        val bestStart = new Array[Int](n)

        for (i <- 0 until n) {
            val len = rad(i) * 2 + 1
            val L = i - rad(i)
            val R = i + rad(i)
            if (len > bestEnd(R)) bestEnd(R) = len
            if (len > bestStart(L)) bestStart(L) = len
        }

        // prefix maximum lengths
        val prefixMax = new Array[Int](n)
        var cur = 0
        for (i <- 0 until n) {
            if (bestEnd(i) > cur) cur = bestEnd(i)
            prefixMax(i) = cur
        }

        // suffix maximum lengths
        val suffixMax = new Array[Int](n)
        cur = 0
        for (i <- (n - 1) to 0 by -1) {
            if (bestStart(i) > cur) cur = bestStart(i)
            suffixMax(i) = cur
        }

        // compute maximum product across split points
        var ans: Long = 0L
        for (i <- 0 until n - 1) {
            val prod = prefixMax(i).toLong * suffixMax(i + 1).toLong
            if (prod > ans) ans = prod
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_product(s: String) -> i64 {
        let n = s.len();
        let bytes = s.as_bytes();

        // Manacher's algorithm for odd length palindromes
        let mut d1 = vec![0usize; n];
        let (mut l, mut r) = (0usize, 0usize);
        for i in 0..n {
            let mut k = if i > r { 1 } else { std::cmp::min(d1[l + r - i], r - i + 1) };
            while i >= k && i + k < n && bytes[i - k] == bytes[i + k] {
                k += 1;
            }
            d1[i] = k;
            if i + k - 1 > r {
                l = i + 1 - k;
                r = i + k - 1;
            }
        }

        // pref[i]: max odd palindrome length fully inside [0..=i]
        // suff[i]: max odd palindrome length fully inside [i..n-1]
        let mut pref = vec![0usize; n];
        let mut suff = vec![0usize; n];

        for i in 0..n {
            let rad = d1[i];
            let len = 2 * rad - 1;
            let left = i + 1 - rad;          // start index of palindrome
            let right = i + rad - 1;         // end index of palindrome
            if pref[right] < len { pref[right] = len; }
            if suff[left] < len { suff[left] = len; }
        }

        for i in 1..n {
            if pref[i - 1] > pref[i] {
                pref[i] = pref[i - 1];
            }
        }
        for i in (0..n - 1).rev() {
            if suff[i + 1] > suff[i] {
                suff[i] = suff[i + 1];
            }
        }

        let mut ans: i64 = 0;
        for i in 0..n - 1 {
            let prod = pref[i] as i64 * suff[i + 1] as i64;
            if prod > ans {
                ans = prod;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (max-product s)
  (-> string? exact-integer?)
  (let* ([n (string-length s)]
         [d1 (make-vector n 0)]
         [pref (make-vector n 0)]
         [suff (make-vector n 0)])
    ;; Manacher's algorithm for odd length palindromes
    (let ([l 0] [r -1])
      (for ([i (in-range n)])
        (define k (if (<= i r)
                      (min (vector-ref d1 (- l (+ r i))) (- (+ r i) i))
                      1))
        ;; expand around center i
        (let loop ((k k))
          (if (and (>= (- i k) 0)
                   (< (+ i k) n)
                   (char=? (string-ref s (- i k)) (string-ref s (+ i k))))
              (loop (add1 k))
              (begin
                (vector-set! d1 i k)
                (when (> (+ i (sub1 k)) r)
                  (set! l (- i (sub1 k)))
                  (set! r (+ i (sub1 k)))))))))
    ;; record best palindrome length ending at each position and starting at each position
    (for ([i (in-range n)])
      (define k (vector-ref d1 i))
      (define len (- (* 2 k) 1))          ; palindrome length
      (define L (- i (sub1 k)))           ; left index
      (define R (+ i (sub1 k)))           ; right index
      (when (> len (vector-ref pref R))
        (vector-set! pref R len))
      (when (> len (vector-ref suff L))
        (vector-set! suff L len)))
    ;; propagate prefix maximums
    (for ([i (in-range 1 n)])
      (let* ((prev (vector-ref pref (sub1 i)))
             (curr (vector-ref pref i)))
        (when (< curr prev)
          (vector-set! pref i prev))))
    ;; propagate suffix maximums
    (for ([i (in-range (- n 2) -1 -1)])
      (let* ((next (vector-ref suff (+ i 1)))
             (curr (vector-ref suff i)))
        (when (< curr next)
          (vector-set! suff i next))))
    ;; compute answer
    (for/fold ([best 0]) ([i (in-range (- n 1))])
      (let* ((left (vector-ref pref i))
             (right (vector-ref suff (+ i 1)))
             (prod (* left right)))
        (if (> prod best) prod best)))))
```

## Erlang

```erlang
-module(solution).
-export([max_product/1]).

-spec max_product(S :: unicode:unicode_binary()) -> integer().
max_product(S) ->
    N = byte_size(S),
    %% Manacher's algorithm for odd length palindromes
    {RadiiMap, EndMap, StartMap} = manacher(0, -1, -1, #{}, #{}, #{}, S, N),
    %% Build prefix max lengths
    PrefList = build_prefix(N, EndMap),
    PrefTuple = list_to_tuple(PrefList),
    %% Build suffix max lengths
    SufList = build_suffix(N, StartMap),
    SufTuple = list_to_tuple(SufList),
    %% Compute maximum product over split points
    compute_max_product(N, PrefTuple, SufTuple).

%% Manacher loop
-spec manacher(
        I :: integer(),
        Center :: integer(),
        Right :: integer(),
        RadiiMap :: map(),
        EndMap :: map(),
        StartMap :: map(),
        binary(),
        N :: integer()
    ) -> {map(), map(), map()}.
manacher(I, _Center, _Right, RadiiMap, EndMap, StartMap, _S, N) when I >= N ->
    {RadiiMap, EndMap, StartMap};
manacher(I, Center, Right, RadiiMap, EndMap, StartMap, S, N) ->
    %% Initial radius based on previously known palindrome
    InitRadius =
        if
            I > Right -> 0;
            true ->
                Mirror = 2 * Center - I,
                Rmirror = maps:get(Mirror, RadiiMap, 0),
                MaxPossible = Right - I,
                erlang:min(Rmirror, MaxPossible)
        end,
    Radius = expand(S, N, I, InitRadius),
    %% Update center and right boundary
    {NewCenter, NewRight} =
        if
            I + Radius > Right -> {I, I + Radius};
            true -> {Center, Right}
        end,
    Len = 2 * Radius + 1,
    EndPos = I + Radius,
    StartPos = I - Radius,
    EndMap2 = maybe_put_max(EndPos, Len, EndMap),
    StartMap2 = maybe_put_max(StartPos, Len, StartMap),
    RadiiMap2 = maps:put(I, Radius, RadiiMap),
    manacher(I + 1, NewCenter, NewRight, RadiiMap2, EndMap2, StartMap2, S, N).

%% Expand palindrome centered at I starting from current radius R
-spec expand(binary(), integer(), integer(), integer()) -> integer().
expand(S, N, I, R) ->
    Left = I - (R + 1),
    Right = I + (R + 1),
    if
        Left >= 0,
        Right < N,
        binary:at(S, Left) =:= binary:at(S, Right) ->
            expand(S, N, I, R + 1);
        true -> R
    end.

%% Update map with maximum length for a given position
-spec maybe_put_max(integer(), integer(), map()) -> map().
maybe_put_max(Pos, Len, Map) ->
    case maps:get(Pos, Map, 0) of
        Existing when Len > Existing -> maps:put(Pos, Len, Map);
        _ -> Map
    end.

%% Build prefix maximum list where pref[i] = max palindrome length ending at or before i
-spec build_prefix(integer(), map()) -> [integer()].
build_prefix(N, EndMap) ->
    build_prefix(0, 0, N, EndMap, []).

-spec build_prefix(integer(), integer(), integer(), map(), [integer()]) -> [integer()].
build_prefix(I, PrevMax, N, _EndMap, Acc) when I >= N ->
    lists:reverse(Acc);
build_prefix(I, PrevMax, N, EndMap, Acc) ->
    LenAt = maps:get(I, EndMap, 0),
    CurMax = if LenAt > PrevMax -> LenAt; true -> PrevMax end,
    build_prefix(I + 1, CurMax, N, EndMap, [CurMax | Acc]).

%% Build suffix maximum list where suf[i] = max palindrome length starting at or after i
-spec build_suffix(integer(), map()) -> [integer()].
build_suffix(N, StartMap) ->
    build_suffix(N - 1, 0, N, StartMap, []).

-spec build_suffix(integer(), integer(), integer(), map(), [integer()]) -> [integer()].
build_suffix(I, PrevMax, _N, _StartMap, Acc) when I < 0 ->
    lists:reverse(Acc);
build_suffix(I, PrevMax, N, StartMap, Acc) ->
    LenAt = maps:get(I, StartMap, 0),
    CurMax = if LenAt > PrevMax -> LenAt; true -> PrevMax end,
    build_suffix(I - 1, CurMax, N, StartMap, [CurMax | Acc]).

%% Compute maximum product over all split points
-spec compute_max_product(integer(), tuple(), tuple()) -> integer().
compute_max_product(N, PrefTuple, SufTuple) ->
    compute_max_product(0, N - 2, PrefTuple, SufTuple, 0).

-spec compute_max_product(integer(), integer(), tuple(), tuple(), integer()) -> integer().
compute_max_product(I, MaxI, _Pref, _Suf, Best) when I > MaxI ->
    Best;
compute_max_product(I, MaxI, Pref, Suf, Best) ->
    LeftLen = element(I + 1, Pref),
    RightLen = element(I + 2, Suf),
    Prod = LeftLen * RightLen,
    NewBest = if Prod > Best -> Prod; true -> Best end,
    compute_max_product(I + 1, MaxI, Pref, Suf, NewBest).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_product(s :: String.t()) :: integer()
  def max_product(s) do
    n = byte_size(s)

    # Manacher's algorithm for odd length palindromes
    radii =
      Enum.reduce(0..(n - 1), {:array.new(n, default: 0), 0, -1}, fn i,
                                                                    {arr, center, right} ->
        mirror = 2 * center - i

        rad =
          if i < right do
            min(:array.get(mirror, arr), right - i)
          else
            0
          end

        rad_expanded = expand(s, n, i, rad)

        arr2 = :array.set(i, rad_expanded, arr)

        {new_center, new_right} =
          if i + rad_expanded > right do
            {i, i + rad_expanded}
          else
            {center, right}
          end

        {arr2, new_center, new_right}
      end)
      |> elem(0)

    # Arrays to store max palindrome length ending at each position and starting at each position
    end_max = :array.new(n, default: 0)
    start_max = :array.new(n, default: 0)

    {end_max, start_max} =
      Enum.reduce(0..(n - 1), {end_max, start_max}, fn i, {e_arr, s_arr} ->
        rad = :array.get(i, radii)
        len = rad * 2 + 1
        re = i + rad
        ls = i - rad

        e_cur = :array.get(re, e_arr)
        e_arr = if len > e_cur, do: :array.set(re, len, e_arr), else: e_arr

        s_cur = :array.get(ls, s_arr)
        s_arr = if len > s_cur, do: :array.set(ls, len, s_arr), else: s_arr

        {e_arr, s_arr}
      end)

    # Prefix best (max length ending at or before i)
    left_best =
      Enum.reduce(0..(n - 1), {:array.new(n, default: 0), 0}, fn i,
                                                                {l_arr, cur_max} ->
        val = :array.get(i, end_max)
        new_max = if val > cur_max, do: val, else: cur_max
        l_arr = :array.set(i, new_max, l_arr)
        {l_arr, new_max}
      end)
      |> elem(0)

    # Suffix best (max length starting at or after i)
    right_best =
      Enum.reduce(Enum.reverse(0..(n - 1)), {:array.new(n, default: 0), 0}, fn i,
                                                                          {r_arr,
                                                                           cur_max} ->
        val = :array.get(i, start_max)
        new_max = if val > cur_max, do: val, else: cur_max
        r_arr = :array.set(i, new_max, r_arr)
        {r_arr, new_max}
      end)
      |> elem(0)

    # Compute maximum product over split points
    Enum.reduce(0..(n - 2), 0, fn i, acc ->
      left_len = :array.get(i, left_best)
      right_len = :array.get(i + 1, right_best)
      prod = left_len * right_len
      if prod > acc, do: prod, else: acc
    end)
  end

  defp expand(s, n, i, rad) do
    cond do
      i - rad - 1 < 0 -> rad
      i + rad + 1 >= n -> rad
      :binary.at(s, i - rad - 1) == :binary.at(s, i + rad + 1) ->
        expand(s, n, i, rad + 1)

      true ->
        rad
    end
  end
end
```
