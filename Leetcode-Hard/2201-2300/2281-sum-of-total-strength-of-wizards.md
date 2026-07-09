# 2281. Sum of Total Strength of Wizards

## Cpp

```cpp
class Solution {
public:
    int totalStrength(vector<int>& strength) {
        const int MOD = 1000000007;
        int n = strength.size();
        vector<long long> pre(n + 1, 0), pre2(n + 2, 0);
        for (int i = 0; i < n; ++i) {
            pre[i + 1] = (pre[i] + strength[i]) % MOD;
        }
        for (int i = 0; i <= n; ++i) {
            pre2[i + 1] = (pre2[i] + pre[i]) % MOD;
        }

        vector<int> left(n), right(n);
        vector<int> st;

        // previous less (strict)
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && strength[st.back()] >= strength[i]) st.pop_back();
            left[i] = st.empty() ? -1 : st.back();
            st.push_back(i);
        }
        st.clear();
        // next less-or-equal
        for (int i = n - 1; i >= 0; --i) {
            while (!st.empty() && strength[st.back()] > strength[i]) st.pop_back();
            right[i] = st.empty() ? n : st.back();
            st.push_back(i);
        }

        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            long long cntL = i - left[i];
            long long cntR = right[i] - i;

            long long sumR = (pre2[right[i] + 1] - pre2[i + 1]) % MOD;
            if (sumR < 0) sumR += MOD;
            long long sumL = (pre2[i + 1] - pre2[left[i] + 1]) % MOD;
            if (sumL < 0) sumL += MOD;

            long long contrib = (cntL % MOD * sumR % MOD - cntR % MOD * sumL % MOD) % MOD;
            if (contrib < 0) contrib += MOD;

            ans = (ans + (strength[i] % MOD) * contrib) % MOD;
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int totalStrength(int[] strength) {
        int n = strength.length;
        long MOD = 1_000_000_007L;

        long[] pre = new long[n + 1];
        for (int i = 0; i < n; ++i) {
            pre[i + 1] = (pre[i] + strength[i]) % MOD;
        }

        long[] pre2 = new long[n + 2];
        for (int i = 0; i <= n; ++i) {
            pre2[i + 1] = (pre2[i] + pre[i]) % MOD;
        }

        int[] left = new int[n];
        int[] right = new int[n];
        java.util.Deque<Integer> stack = new java.util.ArrayDeque<>();

        // previous less element (strictly)
        for (int i = 0; i < n; ++i) {
            while (!stack.isEmpty() && strength[stack.peek()] >= strength[i]) {
                stack.pop();
            }
            left[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);
        }

        stack.clear();

        // next less element (strictly)
        for (int i = n - 1; i >= 0; --i) {
            while (!stack.isEmpty() && strength[stack.peek()] > strength[i]) {
                stack.pop();
            }
            right[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);
        }

        long ans = 0;
        for (int i = 0; i < n; ++i) {
            int l = left[i];
            int r = right[i];

            long leftCount = i - l;
            long rightCount = r - i;

            long sumLeft = (pre2[i + 1] - pre2[l + 1] + MOD) % MOD;
            long sumRight = (pre2[r] - pre2[i] + MOD) % MOD;

            long contrib = (sumRight * leftCount % MOD - sumLeft * rightCount % MOD + MOD) % MOD;
            ans = (ans + (strength[i] % MOD) * contrib) % MOD;
        }

        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def totalStrength(self, strength):
        """
        :type strength: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(strength)

        # prefix sums of strengths
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = (pref[i] + strength[i]) % MOD

        # prefix sums of prefix sums
        pref2 = [0] * (n + 2)
        for i in range(n + 1):
            pref2[i + 1] = (pref2[i] + pref[i]) % MOD

        # previous less element (strictly less)
        ple = [-1] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                stack.pop()
            ple[i] = stack[-1] if stack else -1
            stack.append(i)

        # next less element (less or equal on the right side)
        nle = [n] * n
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                stack.pop()
            nle[i] = stack[-1] if stack else n
            stack.append(i)

        ans = 0
        for i in range(n):
            left = i - ple[i]
            right = nle[i] - i

            # sum of pref[r+1] for r from i to nle[i]-1
            s1 = (pref2[nle[i] + 1] - pref2[i + 1]) % MOD
            # sum of pref[l] for l from ple[i]+1 to i
            sum_pref_l = (pref2[i + 1] - pref2[ple[i] + 1]) % MOD

            total = (left * s1 - right * sum_pref_l) % MOD
            ans = (ans + strength[i] * total) % MOD

        return ans % MOD
```

## Python3

```python
class Solution:
    def totalStrength(self, strength):
        MOD = 10**9 + 7
        n = len(strength)

        left = [-1] * n
        right = [n] * n

        stack = []
        for i, val in enumerate(strength):
            while stack and strength[stack[-1]] >= val:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()
        for i in range(n - 1, -1, -1):
            val = strength[i]
            while stack and strength[stack[-1]] > val:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = (pre[i] + strength[i]) % MOD

        pre2 = [0] * (n + 2)
        for i in range(n + 1):
            pre2[i + 1] = (pre2[i] + pre[i]) % MOD

        ans = 0
        for i in range(n):
            l = i - left[i]
            r = right[i] - i
            sum_right = (pre2[right[i] + 1] - pre2[i + 1]) % MOD
            sum_left = (pre2[i + 1] - pre2[left[i] + 1]) % MOD
            contrib = strength[i] * ((l * sum_right - r * sum_left) % MOD) % MOD
            ans = (ans + contrib) % MOD

        return ans
```

## C

```c
#include <stdlib.h>

int totalStrength(int* strength, int strengthSize) {
    const long long MOD = 1000000007LL;
    int n = strengthSize;

    long long *pre = (long long*)malloc((n + 1) * sizeof(long long));
    long long *pre2 = (long long*)malloc((n + 2) * sizeof(long long));
    int *left = (int*)malloc(n * sizeof(int));
    int *right = (int*)malloc(n * sizeof(int));

    pre[0] = 0;
    for (int i = 0; i < n; ++i) {
        pre[i + 1] = (pre[i] + strength[i]) % MOD;
    }
    pre2[0] = 0;
    for (int i = 0; i <= n; ++i) {
        pre2[i + 1] = (pre2[i] + pre[i]) % MOD;
    }

    int *stack = (int*)malloc(n * sizeof(int));
    int top = -1;

    // previous less (strict)
    for (int i = 0; i < n; ++i) {
        while (top >= 0 && strength[stack[top]] > strength[i]) top--;
        left[i] = (top == -1 ? -1 : stack[top]);
        stack[++top] = i;
    }

    // next less-or-equal
    top = -1;
    for (int i = 0; i < n; ++i) {
        while (top >= 0 && strength[stack[top]] >= strength[i]) {
            int idx = stack[top--];
            right[idx] = i;
        }
        stack[++top] = i;
    }
    while (top >= 0) {
        int idx = stack[top--];
        right[idx] = n;
    }

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        long long L = left[i];
        long long R = right[i];

        long long cntL = i - L;      // choices for start
        long long cntR = R - i;      // choices for end

        long long sumPreR = (pre2[R + 1] - pre2[i + 1]) % MOD;
        if (sumPreR < 0) sumPreR += MOD;

        long long sumPreL = (pre2[i + 1] - pre2[L + 1]) % MOD;
        if (sumPreL < 0) sumPreL += MOD;

        long long total = (cntL * sumPreR) % MOD;
        long long sub   = (cntR * sumPreL) % MOD;
        total = (total - sub) % MOD;
        if (total < 0) total += MOD;

        long long contrib = (strength[i] % MOD) * total % MOD;
        ans += contrib;
        if (ans >= MOD) ans -= MOD;
    }

    free(pre);
    free(pre2);
    free(left);
    free(right);
    free(stack);

    return (int)(ans % MOD);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int TotalStrength(int[] strength) {
        const long MOD = 1_000_000_007L;
        int n = strength.Length;
        // previous less (strict)
        int[] left = new int[n];
        var stack = new Stack<int>();
        for (int i = 0; i < n; i++) {
            while (stack.Count > 0 && strength[stack.Peek()] > strength[i]) stack.Pop();
            left[i] = stack.Count == 0 ? -1 : stack.Peek();
            stack.Push(i);
        }
        // next less-or-equal
        int[] right = new int[n];
        stack.Clear();
        for (int i = n - 1; i >= 0; i--) {
            while (stack.Count > 0 && strength[stack.Peek()] >= strength[i]) stack.Pop();
            right[i] = stack.Count == 0 ? n : stack.Peek();
            stack.Push(i);
        }
        // prefix sums
        long[] pre = new long[n + 1];
        for (int i = 0; i < n; i++) {
            pre[i + 1] = (pre[i] + strength[i]) % MOD;
        }
        // prefix of prefix sums, size n+2 to safely access R+1 where R==n
        long[] pre2 = new long[n + 2];
        for (int i = 0; i <= n; i++) {
            pre2[i + 1] = (pre2[i] + pre[i]) % MOD;
        }
        long ans = 0;
        for (int i = 0; i < n; i++) {
            int L = left[i];
            int R = right[i];
            long leftCnt = i - L;
            long rightCnt = R - i;
            long sumRight = (pre2[R + 1] - pre2[i + 1] + MOD) % MOD;
            long sumLeft = (pre2[i + 1] - pre2[L + 1] + MOD) % MOD;
            long total = (leftCnt * sumRight % MOD - rightCnt * sumLeft % MOD + MOD) % MOD;
            long contrib = (strength[i] % MOD) * total % MOD;
            ans = (ans + contrib) % MOD;
        }
        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} strength
 * @return {number}
 */
var totalStrength = function(strength) {
    const MOD = 1000000007n;
    const n = strength.length;
    
    // previous less (strict)
    const left = new Array(n);
    let stack = [];
    for (let i = 0; i < n; ++i) {
        while (stack.length && BigInt(strength[stack[stack.length - 1]]) >= BigInt(strength[i])) {
            stack.pop();
        }
        left[i] = stack.length ? stack[stack.length - 1] : -1;
        stack.push(i);
    }
    
    // next less-or-equal
    const right = new Array(n);
    stack = [];
    for (let i = n - 1; i >= 0; --i) {
        while (stack.length && BigInt(strength[stack[stack.length - 1]]) > BigInt(strength[i])) {
            stack.pop();
        }
        right[i] = stack.length ? stack[stack.length - 1] : n;
        stack.push(i);
    }
    
    // prefix sums of strengths
    const pre = new Array(n + 1).fill(0n);          // pre[k] = sum_{0..k-1} strength
    for (let i = 0; i < n; ++i) {
        pre[i + 1] = (pre[i] + BigInt(strength[i])) % MOD;
    }
    
    // prefix sums of prefix sums
    const pre2 = new Array(n + 2).fill(0n);         // pre2[t] = sum_{j=0}^{t-1} pre[j]
    for (let i = 0; i <= n; ++i) {
        pre2[i + 1] = (pre2[i] + pre[i]) % MOD;
    }
    
    let ans = 0n;
    for (let i = 0; i < n; ++i) {
        const L = BigInt(i - left[i]);
        const R = BigInt(right[i] - i);
        
        // sum_{k=i+1}^{right} pre[k]
        let sumPreE = (pre2[right[i] + 1] - pre2[i + 1]) % MOD;
        if (sumPreE < 0n) sumPreE += MOD;
        
        // sum_{k=left+1}^{i} pre[k]
        let sumPreS = (pre2[i + 1] - pre2[left[i] + 1]) % MOD;
        if (sumPreS < 0n) sumPreS += MOD;
        
        const total = (L * sumPreE % MOD - R * sumPreS % MOD + MOD) % MOD;
        ans = (ans + BigInt(strength[i]) * total) % MOD;
    }
    
    return Number(ans);
};
```

## Typescript

```typescript
function totalStrength(strength: number[]): number {
    const MOD = 1000000007n;
    const n = strength.length;
    const a = strength.map(v => BigInt(v));

    const pref = new Array<bigint>(n + 1);
    const pref2 = new Array<bigint>(n + 1);
    pref[0] = 0n;
    pref2[0] = 0n;
    for (let i = 0; i < n; i++) {
        pref[i + 1] = (pref[i] + a[i]) % MOD;
        pref2[i + 1] = (pref2[i] + pref[i + 1]) % MOD;
    }

    const left = new Array<number>(n);
    const right = new Array<number>(n);
    let stack: number[] = [];

    // previous strictly smaller
    for (let i = 0; i < n; i++) {
        while (stack.length && a[stack[stack.length - 1]] >= a[i]) stack.pop();
        left[i] = stack.length ? stack[stack.length - 1] : -1;
        stack.push(i);
    }

    // next smaller or equal
    stack = [];
    for (let i = n - 1; i >= 0; i--) {
        while (stack.length && a[stack[stack.length - 1]] > a[i]) stack.pop();
        right[i] = stack.length ? stack[stack.length - 1] : n;
        stack.push(i);
    }

    let ans = 0n;
    for (let i = 0; i < n; i++) {
        const L = left[i];
        const R = right[i];

        const leftCnt = BigInt(i - L);
        const rightCnt = BigInt(R - i);

        // sum of pref[t] for t in [i+1, R]
        let sumPrefRight = (pref2[R] - pref2[i + 1]) % MOD;
        if (sumPrefRight < 0) sumPrefRight += MOD;

        // sum of pref[l] for l in [L+1, i]
        let sumPrefLeft = (pref2[i + 1] - pref2[L + 1]) % MOD;
        if (sumPrefLeft < 0) sumPrefLeft += MOD;

        let total = (leftCnt * sumPrefRight - rightCnt * sumPrefLeft) % MOD;
        if (total < 0) total += MOD;

        ans = (ans + a[i] * total) % MOD;
    }

    return Number(ans);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $strength
     * @return Integer
     */
    function totalStrength($strength) {
        $mod = 1000000007;
        $n = count($strength);
        // prefix sums of strengths
        $pre = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; ++$i) {
            $pre[$i + 1] = ($pre[$i] + $strength[$i]) % $mod;
        }
        // prefix sums of prefix sums
        $prePref = array_fill(0, $n + 1, 0);
        $prePref[0] = $pre[0];
        for ($i = 1; $i <= $n; ++$i) {
            $prePref[$i] = ($prePref[$i - 1] + $pre[$i]) % $mod;
        }

        // previous less element (strict)
        $left = array_fill(0, $n, -1);
        $stack = [];
        for ($i = 0; $i < $n; ++$i) {
            while (!empty($stack) && $strength[end($stack)] > $strength[$i]) {
                array_pop($stack);
            }
            $left[$i] = empty($stack) ? -1 : end($stack);
            $stack[] = $i;
        }

        // next less or equal element
        $right = array_fill(0, $n, $n);
        $stack = [];
        for ($i = $n - 1; $i >= 0; --$i) {
            while (!empty($stack) && $strength[end($stack)] >= $strength[$i]) {
                array_pop($stack);
            }
            $right[$i] = empty($stack) ? $n : end($stack);
            $stack[] = $i;
        }

        $ans = 0;
        for ($i = 0; $i < $n; ++$i) {
            $l = $i - $left[$i];
            $r = $right[$i] - $i;

            // sum of pre[a] where a in [left+1, i]
            $leftIdx = $left[$i];
            $sumLeft = ($prePref[$i] - ($leftIdx >= 0 ? $prePref[$leftIdx] : 0) + $mod) % $mod;

            // sum of pre[t] where t in [i+1, right]
            $rightIdx = $right[$i];
            $sumRight = ($prePref[$rightIdx] - $prePref[$i] + $mod) % $mod;

            $temp = ((($l * $sumRight) % $mod) - (($r * $sumLeft) % $mod)) % $mod;
            if ($temp < 0) {
                $temp += $mod;
            }

            $ans = ($ans + ($strength[$i] % $mod) * $temp) % $mod;
        }

        return (int)$ans;
    }
}
```

## Swift

```swift
class Solution {
    func totalStrength(_ strength: [Int]) -> Int {
        let n = strength.count
        let MOD: Int64 = 1_000_000_007
        
        // Previous less element (strict)
        var left = [Int](repeating: -1, count: n)
        var stack = [Int]()
        for i in 0..<n {
            while let last = stack.last, strength[last] >= strength[i] {
                stack.removeLast()
            }
            left[i] = stack.last ?? -1
            stack.append(i)
        }
        
        // Next less or equal element
        var right = [Int](repeating: n, count: n)
        stack.removeAll()
        for i in stride(from: n - 1, through: 0, by: -1) {
            while let last = stack.last, strength[last] > strength[i] {
                stack.removeLast()
            }
            right[i] = stack.last ?? n
            stack.append(i)
        }
        
        // Prefix sums and prefix of prefix sums (modulo MOD)
        var pre = [Int64](repeating: 0, count: n + 1)
        for i in 0..<n {
            pre[i + 1] = (pre[i] + Int64(strength[i])) % MOD
        }
        var pre2 = [Int64](repeating: 0, count: n + 2) // size n+2 to access index n+1
        for i in 0...n {
            pre2[i + 1] = (pre2[i] + pre[i]) % MOD
        }
        
        var answer: Int64 = 0
        
        for i in 0..<n {
            let L = left[i]
            let R = right[i]
            let leftCount = Int64(i - L)
            let rightCount = Int64(R - i)
            
            var sumRight = (pre2[R + 1] - pre2[i + 1]) % MOD
            if sumRight < 0 { sumRight += MOD }
            var sumLeft = (pre2[i + 1] - pre2[L + 1]) % MOD
            if sumLeft < 0 { sumLeft += MOD }
            
            let total = (leftCount * sumRight % MOD - rightCount * sumLeft % MOD + MOD) % MOD
            answer = (answer + Int64(strength[i]) % MOD * total % MOD) % MOD
        }
        
        return Int(answer)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun totalStrength(strength: IntArray): Int {
        val MOD = 1_000_000_007L
        val n = strength.size

        // previous less element (strict)
        val left = IntArray(n)
        val stack = java.util.ArrayDeque<Int>()
        for (i in 0 until n) {
            while (!stack.isEmpty() && strength[stack.peek()] >= strength[i]) {
                stack.pop()
            }
            left[i] = if (stack.isEmpty()) -1 else stack.peek()
            stack.push(i)
        }

        // next less or equal element
        val right = IntArray(n)
        stack.clear()
        for (i in n - 1 downTo 0) {
            while (!stack.isEmpty() && strength[stack.peek()] > strength[i]) {
                stack.pop()
            }
            right[i] = if (stack.isEmpty()) n else stack.peek()
            stack.push(i)
        }

        // prefix sums of strengths
        val pre = LongArray(n + 1)
        for (i in 0 until n) {
            pre[i + 1] = (pre[i] + strength[i]) % MOD
        }
        // prefix of prefix sums
        val pre2 = LongArray(n + 2)
        for (i in 0..n) {
            pre2[i + 1] = (pre2[i] + pre[i]) % MOD
        }

        var ans = 0L
        for (i in 0 until n) {
            val l = left[i]
            val r = right[i]

            val leftCount = (i - l).toLong()
            val rightCount = (r - i).toLong()

            var sumR = (pre2[r + 1] - pre2[i + 1]) % MOD
            if (sumR < 0) sumR += MOD
            var sumL = (pre2[i + 1] - pre2[l + 1]) % MOD
            if (sumL < 0) sumL += MOD

            var total = (leftCount * sumR) % MOD
            total = (total - (rightCount * sumL) % MOD + MOD) % MOD
            total = (total * strength[i].toLong()) % MOD

            ans = (ans + total) % MOD
        }

        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int MOD = 1000000007;

  int totalStrength(List<int> strength) {
    int n = strength.length;
    List<int> left = List.filled(n, -1);
    List<int> right = List.filled(n, n);

    // previous less (strict)
    List<int> stack = [];
    for (int i = 0; i < n; i++) {
      while (stack.isNotEmpty && strength[stack.last] > strength[i]) {
        stack.removeLast();
      }
      left[i] = stack.isEmpty ? -1 : stack.last;
      stack.add(i);
    }

    // next less or equal
    stack.clear();
    for (int i = n - 1; i >= 0; i--) {
      while (stack.isNotEmpty && strength[stack.last] >= strength[i]) {
        stack.removeLast();
      }
      right[i] = stack.isEmpty ? n : stack.last;
      stack.add(i);
    }

    // prefix sums of strengths
    List<int> pre = List.filled(n + 1, 0);
    for (int i = 0; i < n; i++) {
      pre[i + 1] = (pre[i] + strength[i]) % MOD;
    }

    // prefix of prefix sums
    List<int> pre2 = List.filled(n + 2, 0);
    for (int i = 0; i <= n; i++) {
      pre2[i + 1] = (pre2[i] + pre[i]) % MOD;
    }

    int ans = 0;
    for (int i = 0; i < n; i++) {
      int L = left[i];
      int R = right[i];
      int leftCount = i - L;
      int rightCount = R - i;

      int sumRight = (pre2[R + 1] - pre2[i + 1]) % MOD;
      if (sumRight < 0) sumRight += MOD;
      int sumLeft = (pre2[i + 1] - pre2[L + 1]) % MOD;
      if (sumLeft < 0) sumLeft += MOD;

      int term1 = (leftCount % MOD) * sumRight % MOD;
      int term2 = (rightCount % MOD) * sumLeft % MOD;
      int total = (term1 - term2) % MOD;
      if (total < 0) total += MOD;
      total = total * (strength[i] % MOD) % MOD;

      ans += total;
      if (ans >= MOD) ans -= MOD;
    }

    return ans;
  }
}
```

## Golang

```go
func totalStrength(strength []int) int {
	const MOD int64 = 1000000007
	n := len(strength)

	pre := make([]int64, n+1)
	pre2 := make([]int64, n+1)
	for i := 0; i < n; i++ {
		pre[i+1] = (pre[i] + int64(strength[i])) % MOD
		pre2[i+1] = (pre2[i] + pre[i+1]) % MOD
	}

	left := make([]int, n)
	stack := []int{}
	for i := 0; i < n; i++ {
		for len(stack) > 0 && strength[stack[len(stack)-1]] >= strength[i] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			left[i] = -1
		} else {
			left[i] = stack[len(stack)-1]
		}
		stack = append(stack, i)
	}

	right := make([]int, n)
	for i := range right {
		right[i] = n
	}
	stack = []int{}
	for i := 0; i < n; i++ {
		for len(stack) > 0 && strength[i] <= strength[stack[len(stack)-1]] {
			idx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			right[idx] = i
		}
		stack = append(stack, i)
	}

	var ans int64
	for i := 0; i < n; i++ {
		L := left[i]
		R := right[i]

		leftCnt := int64(i - L)
		rightCnt := int64(R - i)

		sumLeft := (pre2[i+1] - pre2[L+1]) % MOD
		if sumLeft < 0 {
			sumLeft += MOD
		}
		sumRight := (pre2[R] - pre2[i]) % MOD
		if sumRight < 0 {
			sumRight += MOD
		}

		tmp := (rightCnt%MOD)*sumLeft%MOD - (leftCnt%MOD)*sumRight%MOD
		tmp %= MOD
		if tmp < 0 {
			tmp += MOD
		}
		contrib := int64(strength[i])%MOD * tmp % MOD
		ans = (ans + contrib) % MOD
	}

	return int(ans)
}
```

## Ruby

```ruby
def total_strength(strength)
  mod = 1_000_000_007
  n = strength.length

  pre = Array.new(n + 1, 0)
  (0...n).each do |i|
    pre[i + 1] = (pre[i] + strength[i]) % mod
  end

  pre2 = Array.new(n + 2, 0)
  (0..n).each do |i|
    pre2[i + 1] = (pre2[i] + pre[i]) % mod
  end

  left = Array.new(n)
  stack = []
  (0...n).each do |i|
    while !stack.empty? && strength[stack[-1]] >= strength[i]
      stack.pop
    end
    left[i] = stack.empty? ? -1 : stack[-1]
    stack << i
  end

  right = Array.new(n)
  stack.clear
  (n - 1).downto(0) do |i|
    while !stack.empty? && strength[stack[-1]] > strength[i]
      stack.pop
    end
    right[i] = stack.empty? ? n : stack[-1]
    stack << i
  end

  ans = 0
  (0...n).each do |i|
    l = left[i]
    r = right[i]
    cnt_l = i - l
    cnt_r = r - i

    sum_right = (pre2[r + 1] - pre2[i + 1]) % mod
    sum_left  = (pre2[i + 1] - pre2[l + 1]) % mod

    term = (cnt_l * sum_right) % mod
    term = (term - (cnt_r * sum_left) % mod) % mod

    contrib = (strength[i] % mod) * term % mod
    ans = (ans + contrib) % mod
  end

  ans
end
```

## Scala

```scala
object Solution {
    def totalStrength(strength: Array[Int]): Int = {
        val MOD = 1000000007L
        val n = strength.length

        // prefix sums of strengths modulo MOD
        val pref = new Array[Long](n + 1)
        var i = 0
        while (i < n) {
            pref(i + 1) = (pref(i) + strength(i)) % MOD
            i += 1
        }

        // prefix sums of prefix sums modulo MOD
        val prePref = new Array[Long](n + 2)
        i = 0
        while (i <= n) {
            prePref(i + 1) = (prePref(i) + pref(i)) % MOD
            i += 1
        }

        // previous less element (strictly smaller)
        val left = new Array[Int](n)
        // next less-or-equal element
        val right = new Array[Int](n)

        import java.util.ArrayDeque
        val stack = new ArrayDeque[Int]()

        i = 0
        while (i < n) {
            while (!stack.isEmpty && strength(stack.peek()) >= strength(i)) {
                stack.pop()
            }
            left(i) = if (stack.isEmpty) -1 else stack.peek()
            stack.push(i)
            i += 1
        }

        stack.clear()

        i = n - 1
        while (i >= 0) {
            while (!stack.isEmpty && strength(stack.peek()) > strength(i)) {
                stack.pop()
            }
            right(i) = if (stack.isEmpty) n else stack.peek()
            stack.push(i)
            i -= 1
        }

        var ans = 0L
        i = 0
        while (i < n) {
            val l = left(i)
            val r = right(i)

            val leftCount = i - l
            val rightCount = r - i

            var sumR = prePref(r + 1) - prePref(i + 1)
            if (sumR < 0) sumR += MOD
            var sumL = prePref(i + 1) - prePref(l + 1)
            if (sumL < 0) sumL += MOD

            val part1 = (leftCount.toLong % MOD) * sumR % MOD
            val part2 = (rightCount.toLong % MOD) * sumL % MOD
            var contrib = (part1 - part2) % MOD
            if (contrib < 0) contrib += MOD
            contrib = contrib * (strength(i).toLong % MOD) % MOD

            ans += contrib
            if (ans >= MOD) ans -= MOD
            i += 1
        }

        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn total_strength(strength: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = strength.len();
        if n == 0 {
            return 0;
        }

        // previous less element (strict)
        let mut left = vec![-1isize; n];
        let mut stack: Vec<usize> = Vec::new();
        for i in 0..n {
            while let Some(&last) = stack.last() {
                if strength[last] >= strength[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            left[i] = if let Some(&last) = stack.last() {
                last as isize
            } else {
                -1
            };
            stack.push(i);
        }

        // next less-or-equal element
        let mut right = vec![n as isize; n];
        stack.clear();
        for i in (0..n).rev() {
            while let Some(&last) = stack.last() {
                if strength[last] > strength[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            right[i] = if let Some(&last) = stack.last() {
                last as isize
            } else {
                n as isize
            };
            stack.push(i);
        }

        // prefix sums of strengths
        let mut pre = vec![0i64; n + 1];
        for i in 0..n {
            pre[i + 1] = (pre[i] + strength[i] as i64) % MOD;
        }
        // prefix sums of prefix sums
        let mut pre2 = vec![0i64; n + 2];
        for i in 0..=n {
            pre2[i + 1] = (pre2[i] + pre[i]) % MOD;
        }

        let mut ans: i64 = 0;
        let mod_i128 = MOD as i128;

        for i in 0..n {
            let l = left[i];
            let r = right[i];

            let li = (i as isize - l) as i64; // i - L
            let ri = (r - i as isize) as i64; // R - i

            // sum of pre[k] for k in [i+1, R]
            let sum_pre_end = (pre2[(r as usize) + 1] - pre2[i + 1] + MOD) % MOD;
            // sum of pre[k] for k in [L+1, i]
            let l_plus_one = (l + 1) as usize;
            let sum_pre_start = (pre2[i + 1] - pre2[l_plus_one] + MOD) % MOD;

            let term = ((li as i128 * sum_pre_end as i128) % mod_i128
                - (ri as i128 * sum_pre_start as i128) % mod_i128
                + mod_i128)
                % mod_i128;
            let contrib = (term * strength[i] as i128) % mod_i128;

            ans += contrib as i64;
            if ans >= MOD {
                ans -= MOD;
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (total-strength strength)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([v (list->vector strength)]
         [n (vector-length v)]
         [ple (make-vector n -1)]
         [nle (make-vector n n)]
         [stack (make-vector n 0)])
    ;; previous less element (strict)
    (let loop ((i 0) (top -1))
      (when (< i n)
        (let inner ()
          (when (and (>= top 0)
                     (>= (vector-ref v (vector-ref stack top))
                         (vector-ref v i)))
            (set! top (- top 1))
            (inner)))
        (if (>= top 0)
            (vector-set! ple i (vector-ref stack top))
            (vector-set! ple i -1))
        (set! top (+ top 1))
        (vector-set! stack top i)
        (loop (+ i 1) top)))
    ;; next less or equal element
    (let loop ((i (- n 1)) (top -1))
      (when (>= i 0)
        (let inner ()
          (when (and (>= top 0)
                     (> (vector-ref v (vector-ref stack top))
                        (vector-ref v i)))
            (set! top (- top 1))
            (inner)))
        (if (>= top 0)
            (vector-set! nle i (vector-ref stack top))
            (vector-set! nle i n))
        (set! top (+ top 1))
        (vector-set! stack top i)
        (loop (- i 1) top)))
    ;; prefix sums of strengths
    (define ps (make-vector (+ n 1) 0))
    (for ([i (in-range n)])
      (vector-set! ps (+ i 1) (+ (vector-ref ps i) (vector-ref v i))))
    ;; prefix sums of prefix sums
    (define pps (make-vector (+ n 2) 0))
    (for ([i (in-range (+ n 1))])
      (vector-set! pps (+ i 1) (+ (vector-ref pps i) (vector-ref ps i))))
    ;; accumulate answer
    (let loop ((i 0) (ans 0))
      (if (= i n)
          (modulo ans MOD)
          (let* ([left (- i (vector-ref ple i))]
                 [right (- (vector-ref nle i) i)]
                 [sumR (- (vector-ref pps (+ (vector-ref nle i) 1))
                          (vector-ref pps (+ i 1)))]
                 [sumL (- (vector-ref pps (+ i 1))
                          (vector-ref pps (+ (vector-ref ple i) 1)))]
                 [contrib (* (vector-ref v i)
                             (- (* left sumR) (* right sumL)))])
            (loop (+ i 1) (+ ans contrib)))))))
```

## Erlang

```erlang
-module(solution).
-export([total_strength/1]).

-define(MOD, 1000000007).

-spec total_strength(Strength :: [integer()]) -> integer().
total_strength(Strength) ->
    N = length(Strength),
    StrT = list_to_tuple(Strength),

    %% Build prefix sums and double prefix sums (both modulo MOD)
    {PrefT, Pref2T} = build_prefixes(StrT, N),

    %% Compute previous less element indices (strictly less)
    LeftList = compute_left(StrT, N),
    LeftT = list_to_tuple(LeftList),

    %% Compute next less-or-equal element indices
    RightList = compute_right(StrT, N),
    RightT = list_to_tuple(RightList),

    %% Accumulate answer
    Ans = total_contribution(N, StrT, Pref2T, LeftT, RightT, 0, 0),
    Ans.

%% Build prefix sums and double prefix sums (modulo MOD)
-spec build_prefixes(tuple(), integer()) -> {tuple(), tuple()}.
build_prefixes(StrT, N) ->
    build_prefixes(0, 0, [], [], StrT, N).

build_prefixes(I, PrevPref, PrefAcc, Pref2Acc, _StrT, N) when I =:= N ->
    PrefList = lists:reverse(PrefAcc),
    Pref2List = lists:reverse(Pref2Acc),
    {list_to_tuple(PrefList), list_to_tuple(Pref2List)};
build_prefixes(I, PrevPref, PrefAcc, Pref2Acc, StrT, N) ->
    Val = element(I + 1, StrT),
    NewPref = (PrevPref + Val) rem ?MOD,
    NewPref2 = (case Pref2Acc of
                    [] -> NewPref;
                    [_|_] -> (hd(Pref2Acc) + NewPref) rem ?MOD
                end),
    build_prefixes(I + 1, NewPref, [NewPref | PrefAcc],
                   [NewPref2 | Pref2Acc], StrT, N).

%% Compute previous less indices (strictly less)
-spec compute_left(tuple(), integer()) -> [integer()].
compute_left(StrT, N) ->
    compute_left(0, [], [], StrT, N).

compute_left(I, Stack, Acc, _StrT, N) when I =:= N ->
    lists:reverse(Acc);
compute_left(I, Stack, Acc, StrT, N) ->
    CurVal = element(I + 1, StrT),
    NewStack = pop_while_ge(Stack, CurVal, StrT),
    LeftIdx = case NewStack of
                  [] -> -1;
                  [Top | _] -> Top
              end,
    compute_left(I + 1, [I | NewStack], [LeftIdx | Acc], StrT, N).

pop_while_ge([], _CurVal, _StrT) ->
    [];
pop_while_ge([Top | Rest] = Stack, CurVal, StrT) ->
    TopVal = element(Top + 1, StrT),
    if
        TopVal >= CurVal -> pop_while_ge(Rest, CurVal, StrT);
        true -> Stack
    end.

%% Compute next less-or-equal indices
-spec compute_right(tuple(), integer()) -> [integer()].
compute_right(StrT, N) ->
    compute_right(N - 1, [], [], StrT, N).

compute_right(I, _Stack, Acc, _StrT, N) when I < 0 ->
    lists:reverse(Acc);
compute_right(I, Stack, Acc, StrT, N) ->
    CurVal = element(I + 1, StrT),
    NewStack = pop_while_gt(Stack, CurVal, StrT),
    RightIdx = case NewStack of
                   [] -> N;
                   [Top | _] -> Top
               end,
    compute_right(I - 1, [I | NewStack], [RightIdx | Acc], StrT, N).

pop_while_gt([], _CurVal, _StrT) ->
    [];
pop_while_gt([Top | Rest] = Stack, CurVal, StrT) ->
    TopVal = element(Top + 1, StrT),
    if
        TopVal > CurVal -> pop_while_gt(Rest, CurVal, StrT);
        true -> Stack
    end.

%% Compute total contribution using accumulated answer
-spec total_contribution(integer(), tuple(), tuple(),
                         tuple(), tuple(), integer(), integer()) -> integer().
total_contribution(I, _StrT, _Pref2T, _LeftT, _RightT, _Ans, N) when I =:= N ->
    _Ans;
total_contribution(I, StrT, Pref2T, LeftT, RightT, AnsAcc, N) ->
    L = element(I + 1, LeftT),
    R = element(I + 1, RightT),

    CntL = I - L,
    CntR = R - I,

    SumRight = sub_mod(get_pref2(Pref2T, R - 1), get_pref2(Pref2T, I - 1)),
    SumLeft  = sub_mod(get_pref2(Pref2T, I - 1), get_pref2(Pref2T, L - 1)),

    Part1 = (CntL rem ?MOD) * SumRight rem ?MOD,
    Part2 = (CntR rem ?MOD) * SumLeft rem ?MOD,
    Temp = sub_mod(Part1, Part2),

    StrengthMod = element(I + 1, StrT) rem ?MOD,
    Contrib = StrengthMod * Temp rem ?MOD,

    NewAns = (AnsAcc + Contrib) rem ?MOD,
    total_contribution(I + 1, StrT, Pref2T, LeftT, RightT, NewAns, N).

%% Helper to get pref2 value at index (or 0 if idx < 0)
-spec get_pref2(tuple(), integer()) -> integer().
get_pref2(_Pref2T, Idx) when Idx < 0 ->
    0;
get_pref2(Pref2T, Idx) ->
    element(Idx + 1, Pref2T).

%% Modular subtraction ensuring non‑negative result
-spec sub_mod(integer(), integer()) -> integer().
sub_mod(A, B) ->
    ((A - B) rem ?MOD + ?MOD) rem ?MOD.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false
  @spec total_strength(strength :: [integer]) :: integer
  def total_strength(strength) do
    mod = 1_000_000_007
    n = length(strength)
    a = List.to_tuple(strength)

    # previous less (strict)
    {ple, _} =
      Enum.reduce(0..(n - 1), {:array.new(n, default: -1), []}, fn i, {ple_acc, stack} ->
        val_i = elem(a, i)

        stack2 =
          case stack do
            [] -> []
            [_ | _] -> pop_while(stack, fn idx -> elem(a, idx) >= val_i end)
          end

        ple_idx = if stack2 == [], do: -1, else: hd(stack2)
        ple_acc = :array.set(i, ple_idx, ple_acc)
        {ple_acc, [i | stack2]}
      end)

    # next less or equal (<=) using reverse pass
    {nle, _} =
      Enum.reduce(Enum.reverse(0..(n - 1)), {:array.new(n, default: n), []}, fn i,
                                                                              {nle_acc, stack} ->
        val_i = elem(a, i)

        stack2 =
          case stack do
            [] -> []
            [_ | _] -> pop_while(stack, fn idx -> elem(a, idx) > val_i end)
          end

        nle_idx = if stack2 == [], do: n, else: hd(stack2)
        nle_acc = :array.set(i, nle_idx, nle_acc)
        {nle_acc, [i | stack2]}
      end)

    # prefix sums pre[0]=0 ... pre[n]
    {pre, _} =
      Enum.reduce(0..(n - 1), {:array.new(n + 1, default: 0), 0}, fn i,
                                                                   {pre_acc, sum} ->
        new_sum = rem(sum + elem(a, i), mod)
        pre_acc = :array.set(i + 1, new_sum, pre_acc)
        {pre_acc, new_sum}
      end)

    # prefix of prefix sums pre2[0]=0 ... pre2[n+1]
    {pre2, _} =
      Enum.reduce(0..n, {:array.new(n + 2, default: 0), 0}, fn i,
                                                             {pre2_acc, s2} ->
        val = :array.get(i, pre)
        new_s2 = rem(s2 + val, mod)
        pre2_acc = :array.set(i + 1, new_s2, pre2_acc)
        {pre2_acc, new_s2}
      end)

    ans =
      Enum.reduce(0..(n - 1), 0, fn i, acc ->
        left = i - :array.get(i, ple)
        right = :array.get(i, nle) - i

        sum_r =
          (:array.get(:array.get(i, nle) + 1, pre2) -
             :array.get(i + 1, pre2))
          |> mod_fix(mod)

        sum_l =
          (:array.get(i + 1, pre2) -
             :array.get(:array.get(i, ple) + 1, pre2))
          |> mod_fix(mod)

        total = (left * sum_r - right * sum_l) |> mod_fix(mod)
        contrib = rem(elem(a, i) * total, mod)
        rem(acc + contrib, mod)
      end)

    ans
  end

  defp pop_while([h | t] = stack, fun) do
    if fun.(h), do: pop_while(t, fun), else: stack
  end

  defp pop_while([], _fun), do: []

  defp mod_fix(x, mod) do
    r = rem(x, mod)
    if r < 0, do: r + mod, else: r
  end
end
```
