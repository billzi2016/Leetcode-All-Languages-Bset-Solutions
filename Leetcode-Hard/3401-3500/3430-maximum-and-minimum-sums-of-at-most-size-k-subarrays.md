# 3430. Maximum and Minimum Sums of at Most Size K Subarrays

## Cpp

```cpp
class Solution {
public:
    long long minMaxSubarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> prevGreater(n), nextGE(n);
        vector<int> prevSmaller(n), nextSE(n);
        stack<int> st;
        // previous greater (strict)
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && nums[st.top()] <= nums[i]) st.pop();
            prevGreater[i] = st.empty() ? -1 : st.top();
            st.push(i);
        }
        while (!st.empty()) st.pop();
        // next greater or equal
        for (int i = n - 1; i >= 0; --i) {
            while (!st.empty() && nums[st.top()] < nums[i]) st.pop();
            nextGE[i] = st.empty() ? n : st.top();
            st.push(i);
        }
        while (!st.empty()) st.pop();
        // previous smaller (strict)
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && nums[st.top()] >= nums[i]) st.pop();
            prevSmaller[i] = st.empty() ? -1 : st.top();
            st.push(i);
        }
        while (!st.empty()) st.pop();
        // next smaller or equal
        for (int i = n - 1; i >= 0; --i) {
            while (!st.empty() && nums[st.top()] > nums[i]) st.pop();
            nextSE[i] = st.empty() ? n : st.top();
            st.push(i);
        }
        auto countPairs = [&](long long L, long long R) -> long long {
            // number of (l,r) with 1<=l<=L, 0<=r<R and l+r <= k
            long long limit = (long long)k - (R - 1);
            long long A = min(L, limit);
            if (A < 0) A = 0;
            long long B = min(L, (long long)k);
            if (B < 0) B = 0;
            long long total = A * R;
            if (B > A) {
                long long cnt = B - A; // number of l values in second region
                long long first = (long long)k - (A + 1) + 1; // k - (A+1) + 1 = k - A
                long long last  = (long long)k - B + 1;
                total += cnt * (first + last) / 2;
            }
            return total;
        };
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            long long L = i - prevGreater[i];
            long long R = nextGE[i] - i;
            long long cnt = countPairs(L, R);
            ans += cnt * (long long)nums[i];
        }
        for (int i = 0; i < n; ++i) {
            long long L = i - prevSmaller[i];
            long long R = nextSE[i] - i;
            long long cnt = countPairs(L, R);
            ans += cnt * (long long)nums[i];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long minMaxSubarraySum(int[] nums, int k) {
        int n = nums.length;
        int[] leftGreater = new int[n];
        int[] rightGreater = new int[n];
        int[] leftSmaller = new int[n];
        int[] rightSmaller = new int[n];

        java.util.ArrayDeque<Integer> stack = new java.util.ArrayDeque<>();

        // previous greater (strict)
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] <= nums[i]) {
                stack.pop();
            }
            int prev = stack.isEmpty() ? -1 : stack.peek();
            leftGreater[i] = i - prev;
            stack.push(i);
        }

        // next greater or equal
        stack.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && nums[stack.peek()] < nums[i]) {
                stack.pop();
            }
            int nxt = stack.isEmpty() ? n : stack.peek();
            rightGreater[i] = nxt - i;
            stack.push(i);
        }

        // previous smaller (strict)
        stack.clear();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) {
                stack.pop();
            }
            int prev = stack.isEmpty() ? -1 : stack.peek();
            leftSmaller[i] = i - prev;
            stack.push(i);
        }

        // next smaller or equal
        stack.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && nums[stack.peek()] > nums[i]) {
                stack.pop();
            }
            int nxt = stack.isEmpty() ? n : stack.peek();
            rightSmaller[i] = nxt - i;
            stack.push(i);
        }

        long limit = (long) k + 1; // maximum allowed x+y
        long total = 0L;

        for (int i = 0; i < n; i++) {
            long cntMax = countPairs(leftGreater[i], rightGreater[i], limit);
            total += cntMax * (long) nums[i];
            long cntMin = countPairs(leftSmaller[i], rightSmaller[i], limit);
            total += cntMin * (long) nums[i];
        }

        return total;
    }

    private long countPairs(int aInt, int bInt, long limit) {
        long a = aInt;
        long b = bInt;
        if (a == 0 || b == 0) return 0L;
        // maximum possible sum of distances is a + b
        if (a + b <= limit) {
            return a * b;
        }
        long total = 0L;

        // x where limit - x >= b  => x <= limit - b
        long maxFullX = Math.min(a, Math.max(0L, limit - b));
        if (maxFullX > 0) {
            total += maxFullX * b;
        }

        long start = Math.max(1L, limit - b + 1);
        long end = Math.min(a, limit - 1);
        if (start <= end) {
            long cnt = end - start + 1;
            long sumX = (start + end) * cnt / 2;
            total += cnt * limit - sumX;
        }

        return total;
    }
}
```

## Python

```python
class Solution(object):
    def minMaxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        K = k + 1  # we use condition a+b <= K

        def pair_count(L, R):
            # count pairs (a,b) with 1<=a<=L,1<=b<=R and a+b <= K
            max_a = min(L, K - 1)
            if max_a <= 0:
                return 0
            t = K - R
            full_a = 0
            if t > 0:
                full_a = min(L, t)
            if full_a > max_a:
                full_a = max_a
            total = full_a * R
            start = full_a + 1
            if start <= max_a:
                cnt = max_a - full_a
                first = start
                last = max_a
                sum_a = (first + last) * cnt // 2
                total += cnt * K - sum_a
            return total

        # previous greater (strict)
        prev_greater = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            prev_greater[i] = stack[-1] if stack else -1
            stack.append(i)

        # next greater or equal
        next_greater_eq = [n] * n
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            next_greater_eq[i] = stack[-1] if stack else n
            stack.append(i)

        # previous smaller (strict)
        prev_smaller = [-1] * n
        stack.clear()
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        # next smaller or equal
        next_smaller_eq = [n] * n
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            next_smaller_eq[i] = stack[-1] if stack else n
            stack.append(i)

        total = 0
        for i in range(n):
            left = i - prev_greater[i]
            right = next_greater_eq[i] - i
            cnt_max = pair_count(left, right)
            total += nums[i] * cnt_max

            left = i - prev_smaller[i]
            right = next_smaller_eq[i] - i
            cnt_min = pair_count(left, right)
            total += nums[i] * cnt_min

        return total
```

## Python3

```python
class Solution:
    def minMaxSubarraySum(self, nums, k):
        n = len(nums)

        left_max = [0] * n
        right_max = [0] * n
        left_min = [0] * n
        right_min = [0] * n

        # previous greater (strict)
        stack = []
        for i, v in enumerate(nums):
            while stack and nums[stack[-1]] <= v:
                stack.pop()
            left_max[i] = i - (stack[-1] if stack else -1)
            stack.append(i)

        # next greater or equal
        stack.clear()
        for i in range(n - 1, -1, -1):
            v = nums[i]
            while stack and nums[stack[-1]] < v:
                stack.pop()
            right_max[i] = (stack[-1] if stack else n) - i
            stack.append(i)

        # previous smaller (strict)
        stack.clear()
        for i, v in enumerate(nums):
            while stack and nums[stack[-1]] >= v:
                stack.pop()
            left_min[i] = i - (stack[-1] if stack else -1)
            stack.append(i)

        # next smaller or equal
        stack.clear()
        for i in range(n - 1, -1, -1):
            v = nums[i]
            while stack and nums[stack[-1]] > v:
                stack.pop()
            right_min[i] = (stack[-1] if stack else n) - i
            stack.append(i)

        def count_pairs(A, B, k):
            t = k - 1
            max_len = A + B - 2
            if t >= max_len:
                return A * B

            # a where full B fits
            cnt_full = 0
            limit_a = t - (B - 1)
            if limit_a >= 0:
                cnt_full = min(A, limit_a + 1)

            start = cnt_full
            last = min(A - 1, t)
            if last < start:
                partial = 0
            else:
                m = last - start + 1
                first_term = t - start + 1
                last_term = t - last + 1
                partial = m * (first_term + last_term) // 2

            return cnt_full * B + partial

        total = 0
        for i in range(n):
            total += nums[i] * count_pairs(left_max[i], right_max[i], k)
            total += nums[i] * count_pairs(left_min[i], right_min[i], k)

        return total
```

## C

```c
long long countLeq(long long S, long long T, long long K) {
    if (K < 0) return 0;
    long long maxSum = S + T - 2;
    if (K >= maxSum) return S * T;

    long long a_max = (K < S - 1) ? K : S - 1;          // maximum a we can take
    long long threshold = K - (T - 1);                 // last a where b can reach T-1
    long long a0 = (threshold >= 0) ? ((threshold < a_max) ? threshold : a_max) : -1;

    long long cnt = 0;
    if (a0 >= 0) {
        cnt += (a0 + 1) * T;                           // for these a, b can be any of T choices
    }
    long long start = a0 + 1;
    if (start <= a_max) {
        long long n = a_max - start + 1;               // number of remaining a values
        // sum_{a=start}^{a_max} (K - a + 1)
        long long sum_a = (start + a_max) * n / 2;
        cnt += n * (K + 1) - sum_a;
    }
    return cnt;
}

long long minMaxSubarraySum(int* nums, int numsSize, int k) {
    int n = numsSize;
    int *Lmax = (int*)malloc(n * sizeof(int));
    int *Rmax = (int*)malloc(n * sizeof(int));
    int *Lmin = (int*)malloc(n * sizeof(int));
    int *Rmin = (int*)malloc(n * sizeof(int));

    // previous greater (strict) for max
    int *stack = (int*)malloc(n * sizeof(int));
    int top = -1;
    for (int i = 0; i < n; ++i) {
        while (top >= 0 && nums[stack[top]] <= nums[i]) top--;
        int prev = (top >= 0) ? stack[top] : -1;
        Lmax[i] = i - prev;
        stack[++top] = i;
    }

    // next greater or equal for max
    top = -1;
    for (int i = n - 1; i >= 0; --i) {
        while (top >= 0 && nums[stack[top]] < nums[i]) top--;
        int nxt = (top >= 0) ? stack[top] : n;
        Rmax[i] = nxt - i;
        stack[++top] = i;
    }

    // previous smaller (strict) for min
    top = -1;
    for (int i = 0; i < n; ++i) {
        while (top >= 0 && nums[stack[top]] >= nums[i]) top--;
        int prev = (top >= 0) ? stack[top] : -1;
        Lmin[i] = i - prev;
        stack[++top] = i;
    }

    // next smaller or equal for min
    top = -1;
    for (int i = n - 1; i >= 0; --i) {
        while (top >= 0 && nums[stack[top]] > nums[i]) top--;
        int nxt = (top >= 0) ? stack[top] : n;
        Rmin[i] = nxt - i;
        stack[++top] = i;
    }

    free(stack);

    long long ans = 0;
    long long K = (long long)k - 1;

    for (int i = 0; i < n; ++i) {
        long long cntMax = countLeq((long long)Lmax[i], (long long)Rmax[i], K);
        long long cntMin = countLeq((long long)Lmin[i], (long long)Rmin[i], K);
        ans += (long long)nums[i] * cntMax;
        ans += (long long)nums[i] * cntMin;
    }

    free(Lmax);
    free(Rmax);
    free(Lmin);
    free(Rmin);

    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long MinMaxSubarraySum(int[] nums, int k) {
        int n = nums.Length;
        int[] leftGreater = new int[n];
        int[] rightGreaterEq = new int[n];
        var stack = new System.Collections.Generic.Stack<int>();

        // previous greater (strict)
        for (int i = 0; i < n; i++) {
            while (stack.Count > 0 && nums[stack.Peek()] <= nums[i]) stack.Pop();
            leftGreater[i] = stack.Count == 0 ? -1 : stack.Peek();
            stack.Push(i);
        }
        stack.Clear();

        // next greater-or-equal
        for (int i = n - 1; i >= 0; i--) {
            while (stack.Count > 0 && nums[stack.Peek()] < nums[i]) stack.Pop();
            rightGreaterEq[i] = stack.Count == 0 ? n : stack.Peek();
            stack.Push(i);
        }
        stack.Clear();

        // previous smaller (strict)
        int[] leftSmaller = new int[n];
        for (int i = 0; i < n; i++) {
            while (stack.Count > 0 && nums[stack.Peek()] >= nums[i]) stack.Pop();
            leftSmaller[i] = stack.Count == 0 ? -1 : stack.Peek();
            stack.Push(i);
        }
        stack.Clear();

        // next smaller-or-equal
        int[] rightSmallerEq = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            while (stack.Count > 0 && nums[stack.Peek()] > nums[i]) stack.Pop();
            rightSmallerEq[i] = stack.Count == 0 ? n : stack.Peek();
            stack.Push(i);
        }

        long total = 0;
        long limit = k - 1L;

        for (int i = 0; i < n; i++) {
            // contribution as maximum
            long L = i - leftGreater[i];
            long R = rightGreaterEq[i] - i;
            long cntMax = CountPairs(L, R, limit);
            total += cntMax * (long)nums[i];

            // contribution as minimum
            L = i - leftSmaller[i];
            R = rightSmallerEq[i] - i;
            long cntMin = CountPairs(L, R, limit);
            total += cntMin * (long)nums[i];
        }

        return total;
    }

    private long CountPairs(long L, long R, long limit) {
        if (L <= 0 || R <= 0) return 0;
        // If the longest possible subarray using this element is within limit
        if ((L - 1) + (R - 1) <= limit) return L * R;

        long m = Math.Min(L - 1, limit);          // max left offset allowed
        long a0 = limit - (R - 1);                // threshold where right side fully fits
        long fullEnd = Math.Min(m, a0);           // last left offset with full right range

        long total = 0;
        if (fullEnd >= 0) {
            total += (fullEnd + 1) * R;           // those have all R choices on the right
        }

        long start = Math.Max(fullEnd + 1, 0);
        if (start <= m) {
            long cnt = m - start + 1;
            long first = limit - start + 1;       // allowed right offsets for smallest left offset
            long last = limit - m + 1;            // for largest left offset
            total += cnt * (first + last) / 2;    // arithmetic series sum
        }

        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minMaxSubarraySum = function(nums, k) {
    const n = nums.length;
    const prevGreater = new Array(n);
    const nextGE = new Array(n);
    const prevSmaller = new Array(n);
    const nextLE = new Array(n);

    // previous greater (strict)
    let stack = [];
    for (let i = 0; i < n; ++i) {
        while (stack.length && nums[stack[stack.length - 1]] <= nums[i]) stack.pop();
        prevGreater[i] = stack.length ? stack[stack.length - 1] : -1;
        stack.push(i);
    }

    // next greater or equal
    stack = [];
    for (let i = n - 1; i >= 0; --i) {
        while (stack.length && nums[stack[stack.length - 1]] < nums[i]) stack.pop();
        nextGE[i] = stack.length ? stack[stack.length - 1] : n;
        stack.push(i);
    }

    // previous smaller (strict)
    stack = [];
    for (let i = 0; i < n; ++i) {
        while (stack.length && nums[stack[stack.length - 1]] >= nums[i]) stack.pop();
        prevSmaller[i] = stack.length ? stack[stack.length - 1] : -1;
        stack.push(i);
    }

    // next smaller or equal
    stack = [];
    for (let i = n - 1; i >= 0; --i) {
        while (stack.length && nums[stack[stack.length - 1]] > nums[i]) stack.pop();
        nextLE[i] = stack.length ? stack[stack.length - 1] : n;
        stack.push(i);
    }

    const K = k - 1;

    function countPairs(L, R, limit) {
        if (limit < 0) return 0;
        const maxA = Math.min(L - 1, limit);
        if (maxA < 0) return 0;
        const a0 = maxA;               // last possible a
        const nA = a0 + 1;              // number of a values
        const split = limit - (R - 1);  // threshold where min switches
        let total = 0;

        if (split >= 0) {
            const fullA = Math.min(nA, split + 1); // a where b can reach R-1
            total += fullA * R;
            const remaining = nA - fullA;
            if (remaining > 0) {
                const start = fullA; // first a in the remaining part
                // sum_{a=start}^{a0} (limit - a + 1)
                total += remaining * (limit + 1) - ((start + a0) * remaining / 2);
            }
        } else {
            // all a have limited b = limit - a
            total += nA * (limit + 1) - ((a0) * nA / 2);
        }
        return total;
    }

    let result = 0;

    for (let i = 0; i < n; ++i) {
        const Lmax = i - prevGreater[i];
        const Rmax = nextGE[i] - i;
        const cntMax = countPairs(Lmax, Rmax, K);
        result += nums[i] * cntMax;

        const Lmin = i - prevSmaller[i];
        const Rmin = nextLE[i] - i;
        const cntMin = countPairs(Lmin, Rmin, K);
        result += nums[i] * cntMin;
    }

    return result;
};
```

## Typescript

```typescript
function minMaxSubarraySum(nums: number[], k: number): number {
    const n = nums.length;
    const prevGreater = new Array<number>(n);
    const nextGreaterOrEqual = new Array<number>(n).fill(n);
    const prevSmaller = new Array<number>(n);
    const nextSmallerOrEqual = new Array<number>(n).fill(n);

    // previous greater (strict)
    let stack: number[] = [];
    for (let i = 0; i < n; i++) {
        while (stack.length && nums[stack[stack.length - 1]] <= nums[i]) stack.pop();
        prevGreater[i] = stack.length ? stack[stack.length - 1] : -1;
        stack.push(i);
    }

    // next greater or equal
    stack = [];
    for (let i = 0; i < n; i++) {
        while (stack.length && nums[i] > nums[stack[stack.length - 1]]) {
            const idx = stack.pop()!;
            nextGreaterOrEqual[idx] = i;
        }
        stack.push(i);
    }

    // previous smaller (strict)
    stack = [];
    for (let i = 0; i < n; i++) {
        while (stack.length && nums[stack[stack.length - 1]] >= nums[i]) stack.pop();
        prevSmaller[i] = stack.length ? stack[stack.length - 1] : -1;
        stack.push(i);
    }

    // next smaller or equal
    stack = [];
    for (let i = 0; i < n; i++) {
        while (stack.length && nums[i] < nums[stack[stack.length - 1]]) {
            const idx = stack.pop()!;
            nextSmallerOrEqual[idx] = i;
        }
        stack.push(i);
    }

    function countPairs(A: number, B: number, limit: number): number {
        if (limit < 0) return 0;
        const maxSum = A + B - 2;
        if (limit >= maxSum) return A * B;

        const Ap = Math.min(A, limit + 1);
        const Bm = B - 1; // maximum dr
        let cntFull = 0;
        if (limit - Bm >= 0) {
            cntFull = Math.min(Ap, limit - Bm + 1);
        }
        const rem = Ap - cntFull;
        const fullSum = cntFull * B;
        const partialSum = rem * (limit - cntFull + 1) - (rem * (rem - 1)) / 2;
        return fullSum + partialSum;
    }

    let total = 0;
    const limit = k - 1;

    for (let i = 0; i < n; i++) {
        const leftLenMax = i - prevGreater[i];
        const rightLenMax = nextGreaterOrEqual[i] - i;
        const cntMax = countPairs(leftLenMax, rightLenMax, limit);
        total += nums[i] * cntMax;

        const leftLenMin = i - prevSmaller[i];
        const rightLenMin = nextSmallerOrEqual[i] - i;
        const cntMin = countPairs(leftLenMin, rightLenMin, limit);
        total += nums[i] * cntMin;
    }

    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function minMaxSubarraySum($nums, $k) {
        $n = count($nums);
        if ($n == 0) return 0;

        // previous greater (strict)
        $leftGreater = array_fill(0, $n, -1);
        $stack = [];
        for ($i = 0; $i < $n; ++$i) {
            while (!empty($stack) && $nums[end($stack)] <= $nums[$i]) {
                array_pop($stack);
            }
            $leftGreater[$i] = empty($stack) ? -1 : end($stack);
            $stack[] = $i;
        }

        // next greater or equal
        $rightGreater = array_fill(0, $n, $n);
        $stack = [];
        for ($i = $n - 1; $i >= 0; --$i) {
            while (!empty($stack) && $nums[end($stack)] < $nums[$i]) {
                array_pop($stack);
            }
            $rightGreater[$i] = empty($stack) ? $n : end($stack);
            $stack[] = $i;
        }

        // previous smaller (strict)
        $leftSmaller = array_fill(0, $n, -1);
        $stack = [];
        for ($i = 0; $i < $n; ++$i) {
            while (!empty($stack) && $nums[end($stack)] >= $nums[$i]) {
                array_pop($stack);
            }
            $leftSmaller[$i] = empty($stack) ? -1 : end($stack);
            $stack[] = $i;
        }

        // next smaller or equal
        $rightSmaller = array_fill(0, $n, $n);
        $stack = [];
        for ($i = $n - 1; $i >= 0; --$i) {
            while (!empty($stack) && $nums[end($stack)] > $nums[$i]) {
                array_pop($stack);
            }
            $rightSmaller[$i] = empty($stack) ? $n : end($stack);
            $stack[] = $i;
        }

        $total = 0;
        for ($i = 0; $i < $n; ++$i) {
            $Lmax = $i - $leftGreater[$i];
            $Rmax = $rightGreater[$i] - $i;
            $cntMax = $this->countPairs($Lmax, $Rmax, $k);

            $Lmin = $i - $leftSmaller[$i];
            $Rmin = $rightSmaller[$i] - $i;
            $cntMin = $this->countPairs($Lmin, $Rmin, $k);

            $total += $nums[$i] * ($cntMax + $cntMin);
        }

        return $total;
    }

    private function countPairs(int $L, int $R, int $k): int {
        $limit = $k - 1; // a + b <= limit
        if ($limit < 0) return 0;

        // all pairs fit
        if ($limit >= $L + $R - 2) {
            return $L * $R;
        }

        // number of a where we can take full R choices
        $aFull = $limit - ($R - 1);
        if ($aFull < 0) {
            $aFull = 0;
        } else {
            $aFull = min($L, $aFull + 1); // count of such a values
        }

        $maxA = min($L - 1, $limit);
        $remainingCnt = $maxA - $aFull + 1;
        if ($remainingCnt < 0) $remainingCnt = 0;

        $total = $aFull * $R;
        if ($remainingCnt > 0) {
            // sum_{i=0}^{cnt-1} (limit - (aFull + i) + 1)
            $firstTerm = $limit - $aFull + 1;
            $total += $remainingCnt * $firstTerm - intdiv($remainingCnt * ($remainingCnt - 1), 2);
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func minMaxSubarraySum(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        if n == 0 { return 0 }
        
        // Helper to count subarrays where element is extreme with length <= k
        func countSubarrays(_ L: Int, _ R: Int, _ k: Int) -> Int64 {
            // L and R are distances (>=1)
            var cntFull = 0
            if k >= R {
                let limit = k - R
                cntFull = min(L, limit + 1)
            }
            var total: Int64 = Int64(cntFull) * Int64(R)
            
            let start = cntFull
            let end = min(L - 1, k - 1)
            if start <= end {
                let m = end - start + 1
                let sumX = Int64(start + end) * Int64(m) / 2
                let part = Int64(m) * Int64(k) - sumX
                total += part
            }
            return total
        }
        
        // Distances for maximum contributions
        var leftGreater = [Int](repeating: 0, count: n)
        var stack = [Int]()
        for i in 0..<n {
            while let last = stack.last, nums[last] <= nums[i] {
                stack.removeLast()
            }
            if let last = stack.last {
                leftGreater[i] = i - last
            } else {
                leftGreater[i] = i + 1
            }
            stack.append(i)
        }
        
        var rightGreater = [Int](repeating: 0, count: n)
        stack.removeAll()
        for i in stride(from: n - 1, through: 0, by: -1) {
            while let last = stack.last, nums[last] < nums[i] {
                stack.removeLast()
            }
            if let last = stack.last {
                rightGreater[i] = last - i
            } else {
                rightGreater[i] = n - i
            }
            stack.append(i)
        }
        
        // Distances for minimum contributions
        var leftSmaller = [Int](repeating: 0, count: n)
        stack.removeAll()
        for i in 0..<n {
            while let last = stack.last, nums[last] >= nums[i] {
                stack.removeLast()
            }
            if let last = stack.last {
                leftSmaller[i] = i - last
            } else {
                leftSmaller[i] = i + 1
            }
            stack.append(i)
        }
        
        var rightSmaller = [Int](repeating: 0, count: n)
        stack.removeAll()
        for i in stride(from: n - 1, through: 0, by: -1) {
            while let last = stack.last, nums[last] > nums[i] {
                stack.removeLast()
            }
            if let last = stack.last {
                rightSmaller[i] = last - i
            } else {
                rightSmaller[i] = n - i
            }
            stack.append(i)
        }
        
        var result: Int64 = 0
        for i in 0..<n {
            let cntMax = countSubarrays(leftGreater[i], rightGreater[i], k)
            result += Int64(nums[i]) * cntMax
            let cntMin = countSubarrays(leftSmaller[i], rightSmaller[i], k)
            result += Int64(nums[i]) * cntMin
        }
        
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minMaxSubarraySum(nums: IntArray, k: Int): Long {
        val n = nums.size
        val leftMax = IntArray(n)
        val rightMax = IntArray(n)
        val leftMin = IntArray(n)
        val rightMin = IntArray(n)

        // previous greater (strict) for max
        val stack = java.util.ArrayDeque<Int>()
        for (i in 0 until n) {
            while (!stack.isEmpty() && nums[stack.peek()] <= nums[i]) {
                stack.pop()
            }
            val prev = if (stack.isEmpty()) -1 else stack.peek()
            leftMax[i] = i - prev
            stack.push(i)
        }

        // next greater or equal for max
        stack.clear()
        for (i in n - 1 downTo 0) {
            while (!stack.isEmpty() && nums[stack.peek()] < nums[i]) {
                stack.pop()
            }
            val nxt = if (stack.isEmpty()) n else stack.peek()
            rightMax[i] = nxt - i
            stack.push(i)
        }

        // previous smaller (strict) for min
        stack.clear()
        for (i in 0 until n) {
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) {
                stack.pop()
            }
            val prev = if (stack.isEmpty()) -1 else stack.peek()
            leftMin[i] = i - prev
            stack.push(i)
        }

        // next smaller or equal for min
        stack.clear()
        for (i in n - 1 downTo 0) {
            while (!stack.isEmpty() && nums[stack.peek()] > nums[i]) {
                stack.pop()
            }
            val nxt = if (stack.isEmpty()) n else stack.peek()
            rightMin[i] = nxt - i
            stack.push(i)
        }

        var result = 0L
        val limit = k - 1 // maximum sum of offsets

        for (i in 0 until n) {
            val cntMax = countPairs(leftMax[i], rightMax[i], limit)
            result += nums[i].toLong() * cntMax
            val cntMin = countPairs(leftMin[i], rightMin[i], limit)
            result += nums[i].toLong() * cntMin
        }
        return result
    }

    private fun countPairs(a: Int, b: Int, kMinusOne: Int): Long {
        if (kMinusOne < 0) return 0L
        val maxSum = a + b - 2
        if (kMinusOne >= maxSum) return a.toLong() * b

        val t = kMinusOne + 1 // allowed sum of offsets plus one
        var res = 0L

        // Full contribution where offset on right can take all b values
        if (t > b) {
            val cntFull = kotlin.math.min(a, t - b + 1)
            if (cntFull > 0) {
                res += cntFull.toLong() * b
            }
        }

        // Partial contribution where right offset limited by t - x
        val start = kotlin.math.max(0, t - b + 1)
        val end = kotlin.math.min(a - 1, t - 1)
        if (start <= end) {
            val cnt = (end - start + 1).toLong()
            val sumX = (start + end).toLong() * cnt / 2
            res += cnt * t - sumX
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  int minMaxSubarraySum(List<int> nums, int k) {
    int n = nums.length;
    List<int> prevGreater = List.filled(n, -1);
    List<int> nextGE = List.filled(n, n);
    List<int> stack = [];

    // previous greater (strict)
    for (int i = 0; i < n; ++i) {
      while (stack.isNotEmpty && nums[stack.last] <= nums[i]) {
        stack.removeLast();
      }
      prevGreater[i] = stack.isEmpty ? -1 : stack.last;
      stack.add(i);
    }

    stack.clear();

    // next greater or equal
    for (int i = n - 1; i >= 0; --i) {
      while (stack.isNotEmpty && nums[stack.last] < nums[i]) {
        stack.removeLast();
      }
      nextGE[i] = stack.isEmpty ? n : stack.last;
      stack.add(i);
    }

    // previous smaller (strict)
    List<int> prevSmaller = List.filled(n, -1);
    List<int> nextSE = List.filled(n, n);
    stack.clear();

    for (int i = 0; i < n; ++i) {
      while (stack.isNotEmpty && nums[stack.last] >= nums[i]) {
        stack.removeLast();
      }
      prevSmaller[i] = stack.isEmpty ? -1 : stack.last;
      stack.add(i);
    }

    stack.clear();

    // next smaller or equal
    for (int i = n - 1; i >= 0; --i) {
      while (stack.isNotEmpty && nums[stack.last] > nums[i]) {
        stack.removeLast();
      }
      nextSE[i] = stack.isEmpty ? n : stack.last;
      stack.add(i);
    }

    int limit = k - 1;

    int countPairs(int leftLen, int rightLen) {
      if (limit < 0) return 0;
      int a = leftLen;
      int b = rightLen;
      int maxDl = limit < a - 1 ? limit : a - 1;
      if (maxDl < 0) return 0;
      int x = maxDl;

      // If b is larger than any possible t, min always equals t
      if (b > limit + 1) {
        // sum_{dl=0}^{x} (limit - dl + 1)
        return (x + 1) * (limit + 1) - (x * (x + 1)) ~/ 2;
      }

      int threshold = limit - b + 1; // first dl where t <= b
      if (threshold <= 0) {
        // all t <= b, same as above
        return (x + 1) * (limit + 1) - (x * (x + 1)) ~/ 2;
      }

      int p = threshold - 1; // max dl where t > b
      if (p > x) p = x;

      int cnt = (p + 1) * b; // region where min = b

      int start = p + 1;
      if (start <= x) {
        int m = x - start + 1; // number of terms in second region
        int sumDl = (start + x) * m ~/ 2;
        cnt += m * (limit + 1) - sumDl; // sum of t = limit+1 - dl
      }
      return cnt;
    }

    int ans = 0;

    for (int i = 0; i < n; ++i) {
      int leftLen = i - prevGreater[i];
      int rightLen = nextGE[i] - i;
      int cnt = countPairs(leftLen, rightLen);
      ans += nums[i] * cnt;
    }

    for (int i = 0; i < n; ++i) {
      int leftLen = i - prevSmaller[i];
      int rightLen = nextSE[i] - i;
      int cnt = countPairs(leftLen, rightLen);
      ans += nums[i] * cnt;
    }

    return ans;
  }
}
```

## Golang

```go
func minMaxSubarraySum(nums []int, k int) int64 {
    n := len(nums)
    leftGreater := make([]int, n)
    rightGreater := make([]int, n)
    leftSmaller := make([]int, n)
    rightSmaller := make([]int, n)

    // previous greater (strict)
    stack := []int{}
    for i := 0; i < n; i++ {
        for len(stack) > 0 && nums[stack[len(stack)-1]] <= nums[i] {
            stack = stack[:len(stack)-1]
        }
        if len(stack) == 0 {
            leftGreater[i] = -1
        } else {
            leftGreater[i] = stack[len(stack)-1]
        }
        stack = append(stack, i)
    }

    // next greater or equal
    stack = []int{}
    for i := n - 1; i >= 0; i-- {
        for len(stack) > 0 && nums[stack[len(stack)-1]] < nums[i] {
            stack = stack[:len(stack)-1]
        }
        if len(stack) == 0 {
            rightGreater[i] = n
        } else {
            rightGreater[i] = stack[len(stack)-1]
        }
        stack = append(stack, i)
    }

    // previous smaller (strict)
    stack = []int{}
    for i := 0; i < n; i++ {
        for len(stack) > 0 && nums[stack[len(stack)-1]] >= nums[i] {
            stack = stack[:len(stack)-1]
        }
        if len(stack) == 0 {
            leftSmaller[i] = -1
        } else {
            leftSmaller[i] = stack[len(stack)-1]
        }
        stack = append(stack, i)
    }

    // next smaller or equal
    stack = []int{}
    for i := n - 1; i >= 0; i-- {
        for len(stack) > 0 && nums[stack[len(stack)-1]] > nums[i] {
            stack = stack[:len(stack)-1]
        }
        if len(stack) == 0 {
            rightSmaller[i] = n
        } else {
            rightSmaller[i] = stack[len(stack)-1]
        }
        stack = append(stack, i)
    }

    limit := k - 1

    pairCount := func(L, R, lim int) int64 {
        if lim >= L+R-2 {
            return int64(L) * int64(R)
        }
        t := lim
        if t > L-1 {
            t = L - 1
        }
        p := lim - (R - 1)

        var full int
        if p >= 0 {
            if p > t {
                full = t + 1
            } else {
                full = p + 1
            }
        } else {
            full = 0
        }

        total := int64(full) * int64(R)
        start := full
        if start <= t {
            cnt := t - start + 1
            // sum_{l=start}^{t} (lim - l + 1)
            total += int64(cnt)*(int64(lim)+1) - int64(start+t)*int64(cnt)/2
        }
        return total
    }

    var ans int64 = 0
    for i := 0; i < n; i++ {
        leftLen := i - leftGreater[i]
        rightLen := rightGreater[i] - i
        cntMax := pairCount(leftLen, rightLen, limit)
        ans += int64(nums[i]) * cntMax

        leftLen = i - leftSmaller[i]
        rightLen = rightSmaller[i] - i
        cntMin := pairCount(leftLen, rightLen, limit)
        ans += int64(nums[i]) * cntMin
    }
    return ans
}
```

## Ruby

```ruby
def min_max_subarray_sum(nums, k)
  n = nums.length
  limit = k - 1

  # Helper to count pairs (a,b) with a in [0,l-1], b in [0,r-1], a+b <= limit
  count_pairs = lambda do |l, r, lim|
    return 0 if lim < 0
    a_max = l - 1
    a_max = lim if a_max > lim

    thresh = lim - (r - 1)
    a0 = thresh
    a0 = a_max if a0 > a_max
    sum = 0

    if a0 && a0 >= 0
      sum += r * (a0 + 1)
      start = a0 + 1
    else
      start = 0
    end

    if start <= a_max
      n2 = a_max - start + 1
      first_term = lim - start + 1
      last_term = lim - a_max + 1
      sum += n2 * (first_term + last_term) / 2
    end
    sum
  end

  # Max contributions
  left_len_max = Array.new(n)
  stack = []
  nums.each_with_index do |val, i|
    while !stack.empty? && nums[stack[-1]] <= val
      stack.pop
    end
    prev = stack.empty? ? -1 : stack[-1]
    left_len_max[i] = i - prev
    stack << i
  end

  right_len_max = Array.new(n)
  stack.clear
  (n - 1).downto(0) do |i|
    val = nums[i]
    while !stack.empty? && nums[stack[-1]] < val
      stack.pop
    end
    nxt = stack.empty? ? n : stack[-1]
    right_len_max[i] = nxt - i
    stack << i
  end

  # Min contributions
  left_len_min = Array.new(n)
  stack.clear
  nums.each_with_index do |val, i|
    while !stack.empty? && nums[stack[-1]] >= val
      stack.pop
    end
    prev = stack.empty? ? -1 : stack[-1]
    left_len_min[i] = i - prev
    stack << i
  end

  right_len_min = Array.new(n)
  stack.clear
  (n - 1).downto(0) do |i|
    val = nums[i]
    while !stack.empty? && nums[stack[-1]] > val
      stack.pop
    end
    nxt = stack.empty? ? n : stack[-1]
    right_len_min[i] = nxt - i
    stack << i
  end

  total = 0
  (0...n).each do |i|
    cnt_max = count_pairs.call(left_len_max[i], right_len_max[i], limit)
    cnt_min = count_pairs.call(left_len_min[i], right_len_min[i], limit)
    total += nums[i] * cnt_max
    total += nums[i] * cnt_min
  end

  total
end
```

## Scala

```scala
object Solution {
    def minMaxSubarraySum(nums: Array[Int], k: Int): Long = {
        val n = nums.length

        // Helper to count pairs (a,b) with a in [0, L-1], b in [0, R-1] and a+b <= limit
        def countPairs(L: Int, R: Int, limit: Int): Long = {
            if (limit < 0) return 0L
            val maxSum = L + R - 2
            if (limit >= maxSum) return L.toLong * R
            var a0 = limit - (R - 1)
            if (a0 < 0) a0 = 0
            val t = Math.min(L - 1, limit)
            if (a0 > t) {
                val cnt = t + 1 // number of a values
                return (limit + 1).toLong * cnt - (t.toLong * (t + 1) / 2)
            } else {
                val part1 = (a0 + 1).toLong * R
                val cnt = t - a0
                // sum_{i=1}^{cnt} (limit - a0 - i + 1)
                val part2 = cnt.toLong * (limit - a0).toLong - (cnt.toLong * (cnt - 1) / 2)
                return part1 + part2
            }
        }

        // Arrays for max contribution
        val prevGreater = new Array[Int](n)
        val nextGE = new Array[Int](n)

        // previous greater (strictly >)
        var stack = new Array[Int](n)
        var top = 0
        var i = 0
        while (i < n) {
            while (top > 0 && nums(stack(top - 1)) <= nums(i)) top -= 1
            prevGreater(i) = if (top == 0) -1 else stack(top - 1)
            stack(top) = i
            top += 1
            i += 1
        }

        // next greater or equal (>=)
        top = 0
        i = n - 1
        while (i >= 0) {
            while (top > 0 && nums(stack(top - 1)) < nums(i)) top -= 1
            nextGE(i) = if (top == 0) n else stack(top - 1)
            stack(top) = i
            top += 1
            i -= 1
        }

        // Arrays for min contribution
        val prevSmaller = new Array[Int](n)
        val nextSE = new Array[Int](n)

        // previous smaller (strictly <)
        top = 0
        i = 0
        while (i < n) {
            while (top > 0 && nums(stack(top - 1)) >= nums(i)) top -= 1
            prevSmaller(i) = if (top == 0) -1 else stack(top - 1)
            stack(top) = i
            top += 1
            i += 1
        }

        // next smaller or equal (<=)
        top = 0
        i = n - 1
        while (i >= 0) {
            while (top > 0 && nums(stack(top - 1)) > nums(i)) top -= 1
            nextSE(i) = if (top == 0) n else stack(top - 1)
            stack(top) = i
            top += 1
            i -= 1
        }

        var totalMax: Long = 0L
        var totalMin: Long = 0L
        val limit = k - 1

        i = 0
        while (i < n) {
            val left = i - prevGreater(i)
            val right = nextGE(i) - i
            val cnt = countPairs(left, right, limit)
            totalMax += nums(i).toLong * cnt
            i += 1
        }

        i = 0
        while (i < n) {
            val left = i - prevSmaller(i)
            val right = nextSE(i) - i
            val cnt = countPairs(left, right, limit)
            totalMin += nums(i).toLong * cnt
            i += 1
        }

        totalMax + totalMin
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_max_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let k_usize = k as usize;
        let limit = if k_usize == 0 { 0 } else { k_usize - 1 };

        // helper to count pairs with length constraint
        fn count_pairs(l: usize, r: usize, k_minus_one: usize) -> i64 {
            let max_sum = l + r - 2;
            if k_minus_one >= max_sum {
                return (l as i64) * (r as i64);
            }
            let K = k_minus_one;

            // x where we can take full R choices
            let mut full_cnt: i64 = 0;
            if K >= r - 1 {
                let max_x_full = std::cmp::min(l - 1, K - (r - 1));
                full_cnt = (max_x_full + 1) as i64;
            }
            let mut total = full_cnt * r as i64;

            // remaining x where only part of R is allowed
            let start = if K >= r - 1 {
                std::cmp::min(l - 1, K - (r - 1)) + 1
            } else {
                0
            };
            let end = std::cmp::min(l - 1, K);
            if end >= start {
                let n2 = (end - start + 1) as i64;
                let a1 = (K - start + 1) as i64;
                let an = (K - end + 1) as i64;
                total += n2 * (a1 + an) / 2;
            }
            total
        }

        // distances for maximum contributions
        let mut left_max = vec![0usize; n];
        let mut stack: Vec<usize> = Vec::new();
        for i in 0..n {
            while let Some(&idx) = stack.last() {
                if nums[idx] <= nums[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            left_max[i] = if let Some(&idx) = stack.last() { i - idx } else { i + 1 };
            stack.push(i);
        }

        let mut right_max = vec![0usize; n];
        stack.clear();
        for i in (0..n).rev() {
            while let Some(&idx) = stack.last() {
                if nums[idx] < nums[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            right_max[i] = if let Some(&idx) = stack.last() { idx - i } else { n - i };
            stack.push(i);
        }

        // distances for minimum contributions
        let mut left_min = vec![0usize; n];
        stack.clear();
        for i in 0..n {
            while let Some(&idx) = stack.last() {
                if nums[idx] >= nums[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            left_min[i] = if let Some(&idx) = stack.last() { i - idx } else { i + 1 };
            stack.push(i);
        }

        let mut right_min = vec![0usize; n];
        stack.clear();
        for i in (0..n).rev() {
            while let Some(&idx) = stack.last() {
                if nums[idx] > nums[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            right_min[i] = if let Some(&idx) = stack.last() { idx - i } else { n - i };
            stack.push(i);
        }

        // accumulate contributions
        let mut total: i64 = 0;
        for i in 0..n {
            let cnt_max = count_pairs(left_max[i], right_max[i], limit);
            let cnt_min = count_pairs(left_min[i], right_min[i], limit);
            total += nums[i] as i64 * (cnt_max + cnt_min);
        }
        total
    }
}
```

## Racket

```racket
(define/contract (min-max-subarray-sum nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v))
         ;; distances for maximum
         (left-greater (make-vector n))
         (right-greater (make-vector n))
         ;; distances for minimum
         (left-smaller (make-vector n))
         (right-smaller (make-vector n)))
    ;; previous greater (strict)
    (let ((stack (make-vector n)) (top -1))
      (for ([i (in-range n)])
        (let loop ()
          (when (and (>= top 0)
                     (<= (vector-ref v (vector-ref stack top))
                         (vector-ref v i)))
            (set! top (- top 1))
            (loop)))
        (define prev (if (< top 0) -1 (vector-ref stack top)))
        (vector-set! left-greater i (- i prev))
        (set! top (+ top 1))
        (vector-set! stack top i)))
    ;; next greater-or-equal
    (let ((stack (make-vector n)) (top -1))
      (for ([i (in-range (sub1 n) -1 -1)])
        (let loop ()
          (when (and (>= top 0)
                     (< (vector-ref v (vector-ref stack top))
                        (vector-ref v i)))
            (set! top (- top 1))
            (loop)))
        (define nxt (if (< top 0) n (vector-ref stack top)))
        (vector-set! right-greater i (- nxt i))
        (set! top (+ top 1))
        (vector-set! stack top i)))
    ;; previous smaller (strict)
    (let ((stack (make-vector n)) (top -1))
      (for ([i (in-range n)])
        (let loop ()
          (when (and (>= top 0)
                     (>= (vector-ref v (vector-ref stack top))
                         (vector-ref v i)))
            (set! top (- top 1))
            (loop)))
        (define prev (if (< top 0) -1 (vector-ref stack top)))
        (vector-set! left-smaller i (- i prev))
        (set! top (+ top 1))
        (vector-set! stack top i)))
    ;; next smaller-or-equal
    (let ((stack (make-vector n)) (top -1))
      (for ([i (in-range (sub1 n) -1 -1)])
        (let loop ()
          (when (and (>= top 0)
                     (> (vector-ref v (vector-ref stack top))
                        (vector-ref v i)))
            (set! top (- top 1))
            (loop)))
        (define nxt (if (< top 0) n (vector-ref stack top)))
        (vector-set! right-smaller i (- nxt i))
        (set! top (+ top 1))
        (vector-set! stack top i)))
    ;; helper to count pairs with length constraint
    (define (count-pairs L R K)
      (if (< K 0)
          0
          (let* ((A L) (B R))
            (if (>= K (+ A B -2))
                (* A B)
                (let* ((a-max (min (- A 1) K))
                       (threshold (+ K (- B) 1)) ; K - B + 1
                       (cnt-full (if (>= threshold 0)
                                     (add1 (min a-max threshold))
                                     0))
                       (remaining (- (+ a-max 1) cnt-full))) ; number of a with partial contribution
                  (let* ((full-contrib (* cnt-full B))
                         (sum-partial (if (> remaining 0)
                                          (quotient (* remaining
                                                       (+ (- K cnt-full 1)   ; first term: K - cnt-full + 1
                                                          (- K a-max 1)))   ; last term: K - a-max + 1
                                                   2)
                                          0)))
                    (+ full-contrib sum-partial)))))))
    ;; accumulate answer
    (let ((ans 0))
      (for ([i (in-range n)])
        (define Lmax (vector-ref left-greater i))
        (define Rmax (vector-ref right-greater i))
        (define Lmin (vector-ref left-smaller i))
        (define Rmin (vector-ref right-smaller i))
        (define cnt-max (count-pairs Lmax Rmax (- k 1)))
        (define cnt-min (count-pairs Lmin Rmin (- k 1)))
        (set! ans (+ ans (* (vector-ref v i) (+ cnt-max cnt-min)))))
      ans)))
```

## Erlang

```erlang
-spec min_max_subarray_sum(Nums :: [integer()], K :: integer()) -> integer().
min_max_subarray_sum(Nums, K) ->
    N = length(Nums),
    NumTuple = list_to_tuple(Nums),

    % previous greater (strict)
    PrevG = build_prev(0, N, NumTuple, [], array:new(N, {default, -1}),
                       fun(TV, CV) -> TV =< CV end),

    % next greater or equal
    NextGE = build_next(N - 1, N, NumTuple, [], array:new(N, {default, N}),
                        fun(TV, CV) -> TV < CV end),

    % previous smaller (strict)
    PrevS = build_prev(0, N, NumTuple, [], array:new(N, {default, -1}),
                       fun(TV, CV) -> TV >= CV end),

    % next smaller or equal
    NextSE = build_next(N - 1, N, NumTuple, [], array:new(N, {default, N}),
                        fun(TV, CV) -> TV > CV end),

    Total = calc_sum(0, N, NumTuple, PrevG, NextGE, PrevS, NextSE, K, 0, 0),
    Total.

%% Build previous index array using monotonic stack
build_prev(Index, N, NumTuple, Stack, Arr, Cond) when Index < N ->
    Val = element(Index + 1, NumTuple),
    NewStack = pop_while(Stack, Val, NumTuple, Cond),
    PrevIdx = case NewStack of [] -> -1; [Top | _] -> Top end,
    UpdatedArr = array:set(Index, PrevIdx, Arr),
    build_prev(Index + 1, N, NumTuple, [Index | NewStack], UpdatedArr, Cond);
build_prev(_, _, _, _, Arr, _) ->
    Arr.

%% Build next index array using monotonic stack (scan from right)
build_next(Index, N, NumTuple, Stack, Arr, Cond) when Index >= 0 ->
    Val = element(Index + 1, NumTuple),
    NewStack = pop_while(Stack, Val, NumTuple, Cond),
    NextIdx = case NewStack of [] -> N; [Top | _] -> Top end,
    UpdatedArr = array:set(Index, NextIdx, Arr),
    build_next(Index - 1, N, NumTuple, [Index | NewStack], UpdatedArr, Cond);
build_next(_, _, _, _, Arr, _) ->
    Arr.

%% Pop while condition holds
pop_while([], _Val, _NumTuple, _Cond) -> [];
pop_while([Top | Rest] = Stack, Val, NumTuple, Cond) ->
    TopVal = element(Top + 1, NumTuple),
    case Cond(TopVal, Val) of
        true -> pop_while(Rest, Val, NumTuple, Cond);
        false -> Stack
    end.

%% Calculate total sum of contributions
calc_sum(I, N, NumTuple, PrevG, NextGE, PrevS, NextSE, K, SumMax, SumMin) when I < N ->
    Val = element(I + 1, NumTuple),

    PG = array:get(I, PrevG),
    NG = array:get(I, NextGE),
    Lmax = I - PG,
    Rmax = NG - I,
    Cmax = count_pairs(Lmax, Rmax, K),

    PS = array:get(I, PrevS),
    NS = array:get(I, NextSE),
    Lmin = I - PS,
    Rmin = NS - I,
    Cmin = count_pairs(Lmin, Rmin, K),

    NewSumMax = SumMax + Val * Cmax,
    NewSumMin = SumMin + Val * Cmin,

    calc_sum(I + 1, N, NumTuple, PrevG, NextGE, PrevS, NextSE, K, NewSumMax, NewSumMin);
calc_sum(_, _, _, _, _, _, _, _, SumMax, SumMin) ->
    SumMax + SumMin.

%% Count pairs (dl, dr) with dl in [0,L-1], dr in [0,R-1] and dl+dr <= K-1
count_pairs(L, R, K) ->
    T = K - 1,
    MaxSum = L + R - 2,
    if
        T >= MaxSum -> L * R;
        true ->
            MaxDl = min(L - 1, T),
            Limit = T - (R - 1),
            A = case Limit >= 0 of
                    true -> min(L - 1, Limit);
                    false -> -1
                end,
            Count1 = if A >= 0 -> (A + 1) * R; true -> 0 end,
            Start = A + 1,
            if
                Start > MaxDl ->
                    Count1;
                true ->
                    N2 = MaxDl - Start + 1,
                    Sum2 = N2 * (T + 1) - ((Start + MaxDl) * N2 div 2),
                    Count1 + Sum2
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_max_subarray_sum(nums :: [integer], k :: integer) :: integer
  def min_max_subarray_sum(nums, k) do
    n = length(nums)
    nums_t = List.to_tuple(nums)

    # left lengths for maximum (previous greater strict)
    {_, left_max_rev} =
      Enum.reduce(0..(n - 1), {[], []}, fn i, {stack, acc} ->
        stack = pop_while(stack, fn idx -> elem(nums_t, idx) <= elem(nums_t, i) end)

        prev =
          case stack do
            [] -> -1
            [h | _] -> h
          end

        left_len = i - prev
        {[i | stack], [left_len | acc]}
      end)

    left_max = List.to_tuple(Enum.reverse(left_max_rev))

    # right lengths for maximum (next greater-or-equal)
    {right_max_arr, _} =
      Enum.reduce(0..(n - 1), {%array.new(n, default: 0), []}, fn i,
                                                                 {arr, stack} ->
        {arr, stack} = pop_and_set(arr, stack, i, nums_t, &>=/2)
        {arr, [i | stack]}
      end)

    right_max_arr =
      Enum.reduce(stack, right_max_arr, fn idx, arr ->
        :array.set(idx, n - idx, arr)
      end)

    # left lengths for minimum (previous smaller strict)
    {_, left_min_rev} =
      Enum.reduce(0..(n - 1), {[], []}, fn i, {stack, acc} ->
        stack = pop_while(stack, fn idx -> elem(nums_t, idx) >= elem(nums_t, i) end)

        prev =
          case stack do
            [] -> -1
            [h | _] -> h
          end

        left_len = i - prev
        {[i | stack], [left_len | acc]}
      end)

    left_min = List.to_tuple(Enum.reverse(left_min_rev))

    # right lengths for minimum (next smaller-or-equal)
    {right_min_arr, _} =
      Enum.reduce(0..(n - 1), {%array.new(n, default: 0), []}, fn i,
                                                                 {arr, stack} ->
        {arr, stack} = pop_and_set(arr, stack, i, nums_t, &<=/2)
        {arr, [i | stack]}
      end)

    right_min_arr =
      Enum.reduce(stack, right_min_arr, fn idx, arr ->
        :array.set(idx, n - idx, arr)
      end)

    # compute total contribution
    Enum.reduce(0..(n - 1), 0, fn i, acc ->
      val = elem(nums_t, i)

      lmax = elem(left_max, i)
      rmax = :array.get(i, right_max_arr)
      cnt_max = count_pairs(lmax, rmax, k)

      lmin = elem(left_min, i)
      rmin = :array.get(i, right_min_arr)
      cnt_min = count_pairs(lmin, rmin, k)

      acc + val * (cnt_max + cnt_min)
    end)
  end

  # pop while condition holds
  defp pop_while([], _fun), do: []
  defp pop_while([h | t] = stack, fun) do
    if fun.(h) do
      pop_while(t, fun)
    else
      stack
    end
  end

  # pop elements whose condition with current index holds and set their right length
  defp pop_and_set(arr, [], _cur_idx, _nums_t, _cmp), do: {arr, []}
  defp pop_and_set(arr, [h | t] = stack, cur_idx, nums_t, cmp) do
    if cmp.(elem(nums_t, cur_idx), elem(nums_t, h)) do
      dist = cur_idx - h
      arr = :array.set(h, dist, arr)
      pop_and_set(arr, t, cur_idx, nums_t, cmp)
    else
      {arr, stack}
    end
  end

  # count pairs (a,b) with a in [0,l-1], b in [0,r-1] and a+b <= k-1
  defp count_pairs(l, r, k) do
    limit = k - 1
    max_len = l + r - 2

    if limit >= max_len do
      l * r
    else
      a_max = min(l - 1, limit)
      t = limit - (r - 1)

      {cnt_full, start} =
        if t >= 0 do
          full_a_end = min(t, l - 1)
          {(full_a_end + 1) * r, full_a_end + 1}
        else
          {0, 0}
        end

      cnt_partial =
        if start <= a_max do
          n = a_max - start + 1
          sum = n * (limit + 1) - div((start + a_max) * n, 2)
          sum
        else
          0
        end

      cnt_full + cnt_partial
    end
  end
end
```
