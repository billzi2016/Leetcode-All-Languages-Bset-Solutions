# 2866. Beautiful Towers II

## Cpp

```cpp
class Solution {
public:
    long long maximumSumOfHeights(std::vector<int>& maxHeights) {
        int n = maxHeights.size();
        std::vector<long long> left(n), right(n);
        // compute left contributions
        std::stack<std::pair<long long,int>> st;
        long long cur = 0;
        for (int i = 0; i < n; ++i) {
            long long h = maxHeights[i];
            int cnt = 1;
            while (!st.empty() && st.top().first >= h) {
                cur -= st.top().first * st.top().second;
                cnt += st.top().second;
                st.pop();
            }
            st.push({h, cnt});
            cur += h * cnt;
            left[i] = cur;
        }
        // compute right contributions
        while (!st.empty()) st.pop();
        cur = 0;
        for (int i = n - 1; i >= 0; --i) {
            long long h = maxHeights[i];
            int cnt = 1;
            while (!st.empty() && st.top().first >= h) {
                cur -= st.top().first * st.top().second;
                cnt += st.top().second;
                st.pop();
            }
            st.push({h, cnt});
            cur += h * cnt;
            right[i] = cur;
        }
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            long long total = left[i] + right[i] - maxHeights[i];
            if (total > ans) ans = total;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long maximumSumOfHeights(java.util.List<Integer> maxHeights) {
        int n = maxHeights.size();
        long[] left = new long[n];
        long[] right = new long[n];

        java.util.ArrayDeque<long[]> stack = new java.util.ArrayDeque<>();
        long cur = 0;
        for (int i = 0; i < n; i++) {
            long h = maxHeights.get(i);
            long len = 1;
            while (!stack.isEmpty() && stack.peek()[0] >= h) {
                long[] top = stack.pop();
                len += top[1];
                cur -= top[0] * top[1];
            }
            stack.push(new long[]{h, len});
            cur += h * len;
            left[i] = cur;
        }

        stack.clear();
        cur = 0;
        for (int i = n - 1; i >= 0; i--) {
            long h = maxHeights.get(i);
            long len = 1;
            while (!stack.isEmpty() && stack.peek()[0] >= h) {
                long[] top = stack.pop();
                len += top[1];
                cur -= top[0] * top[1];
            }
            stack.push(new long[]{h, len});
            cur += h * len;
            right[i] = cur;
        }

        long ans = 0;
        for (int i = 0; i < n; i++) {
            long total = left[i] + right[i] - maxHeights.get(i);
            if (total > ans) ans = total;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maximumSumOfHeights(self, maxHeights):
        """
        :type maxHeights: List[int]
        :rtype: int
        """
        n = len(maxHeights)
        left = [0] * n
        stack = []
        for i in range(n):
            # find previous index with smaller height
            while stack and maxHeights[stack[-1]] >= maxHeights[i]:
                stack.pop()
            prev = stack[-1] if stack else -1
            left[i] = (left[prev] if prev != -1 else 0) + maxHeights[i] * (i - prev)
            stack.append(i)

        right = [0] * n
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and maxHeights[stack[-1]] >= maxHeights[i]:
                stack.pop()
            nxt = stack[-1] if stack else n
            right[i] = (right[nxt] if nxt != n else 0) + maxHeights[i] * (nxt - i)
            stack.append(i)

        ans = 0
        for i in range(n):
            total = left[i] + right[i] - maxHeights[i]
            if total > ans:
                ans = total
        return ans
```

## Python3

```python
class Solution:
    def maximumSumOfHeights(self, maxHeights):
        n = len(maxHeights)
        left = [0] * n
        right = [0] * n

        stack = []
        for i in range(n):
            while stack and maxHeights[stack[-1]] >= maxHeights[i]:
                stack.pop()
            if stack:
                prev = stack[-1]
                left[i] = (i - prev) * maxHeights[i] + left[prev]
            else:
                left[i] = (i + 1) * maxHeights[i]
            stack.append(i)

        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and maxHeights[stack[-1]] >= maxHeights[i]:
                stack.pop()
            if stack:
                nxt = stack[-1]
                right[i] = (nxt - i) * maxHeights[i] + right[nxt]
            else:
                right[i] = (n - i) * maxHeights[i]
            stack.append(i)

        ans = 0
        for i in range(n):
            total = left[i] + right[i] - maxHeights[i]
            if total > ans:
                ans = total
        return ans
```

## C

```c
#include <stdlib.h>

long long maximumSumOfHeights(int* maxHeights, int maxHeightsSize) {
    int n = maxHeightsSize;
    long long *left = (long long *)malloc(n * sizeof(long long));
    long long *right = (long long *)malloc(n * sizeof(long long));

    // Stack for values and counts
    int *stackVal = (int *)malloc(n * sizeof(int));
    int *stackCnt = (int *)malloc(n * sizeof(int));
    int top = -1;
    long long cur = 0;

    // Compute left contributions
    for (int i = 0; i < n; ++i) {
        int cnt = 1;
        while (top >= 0 && stackVal[top] >= maxHeights[i]) {
            cur -= (long long)stackVal[top] * stackCnt[top];
            cnt += stackCnt[top];
            top--;
        }
        stackVal[++top] = maxHeights[i];
        stackCnt[top] = cnt;
        cur += (long long)maxHeights[i] * cnt;
        left[i] = cur;
    }

    // Reset for right contributions
    top = -1;
    cur = 0;

    for (int i = n - 1; i >= 0; --i) {
        int cnt = 1;
        while (top >= 0 && stackVal[top] >= maxHeights[i]) {
            cur -= (long long)stackVal[top] * stackCnt[top];
            cnt += stackCnt[top];
            top--;
        }
        stackVal[++top] = maxHeights[i];
        stackCnt[top] = cnt;
        cur += (long long)maxHeights[i] * cnt;
        right[i] = cur;
    }

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        long long total = left[i] + right[i] - maxHeights[i];
        if (total > ans) ans = total;
    }

    free(left);
    free(right);
    free(stackVal);
    free(stackCnt);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long MaximumSumOfHeights(IList<int> maxHeights) {
        int n = maxHeights.Count;
        long[] left = new long[n];
        long[] right = new long[n];

        // Compute left sums: sum of minima for subarrays ending at i
        var valStack = new Stack<long>();
        var cntStack = new Stack<int>();
        long curSum = 0;
        for (int i = 0; i < n; i++) {
            long val = maxHeights[i];
            int cnt = 1;
            while (valStack.Count > 0 && valStack.Peek() >= val) {
                long topVal = valStack.Pop();
                int topCnt = cntStack.Pop();
                curSum -= topVal * topCnt;
                cnt += topCnt;
            }
            valStack.Push(val);
            cntStack.Push(cnt);
            curSum += val * cnt;
            left[i] = curSum;
        }

        // Compute right sums: sum of minima for subarrays starting at i
        var rValStack = new Stack<long>();
        var rCntStack = new Stack<int>();
        curSum = 0;
        for (int i = n - 1; i >= 0; i--) {
            long val = maxHeights[i];
            int cnt = 1;
            while (rValStack.Count > 0 && rValStack.Peek() >= val) {
                long topVal = rValStack.Pop();
                int topCnt = rCntStack.Pop();
                curSum -= topVal * topCnt;
                cnt += topCnt;
            }
            rValStack.Push(val);
            rCntStack.Push(cnt);
            curSum += val * cnt;
            right[i] = curSum;
        }

        long answer = 0;
        for (int i = 0; i < n; i++) {
            long total = left[i] + right[i] - maxHeights[i];
            if (total > answer) answer = total;
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} maxHeights
 * @return {number}
 */
var maximumSumOfHeights = function (maxHeights) {
    const n = maxHeights.length;
    const left = new Array(n);
    const right = new Array(n);
    let stack = [];

    // compute left sums: sum of minima for subarrays ending at i
    for (let i = 0; i < n; i++) {
        while (stack.length && maxHeights[stack[stack.length - 1]] >= maxHeights[i]) {
            stack.pop();
        }
        const prev = stack.length ? stack[stack.length - 1] : -1;
        left[i] = maxHeights[i] * (i - prev) + (prev >= 0 ? left[prev] : 0);
        stack.push(i);
    }

    // compute right sums: sum of minima for subarrays starting at i
    stack = [];
    for (let i = n - 1; i >= 0; i--) {
        while (stack.length && maxHeights[stack[stack.length - 1]] >= maxHeights[i]) {
            stack.pop();
        }
        const next = stack.length ? stack[stack.length - 1] : n;
        right[i] = maxHeights[i] * (next - i) + (next < n ? right[next] : 0);
        stack.push(i);
    }

    let ans = 0;
    for (let i = 0; i < n; i++) {
        const total = left[i] + right[i] - maxHeights[i];
        if (total > ans) ans = total;
    }
    return ans;
};
```

## Typescript

```typescript
function maximumSumOfHeights(maxHeights: number[]): number {
    const n = maxHeights.length;
    const left = new Array<number>(n);
    const right = new Array<number>(n);
    let stack: number[] = [];

    // compute left sums
    for (let i = 0; i < n; i++) {
        while (stack.length && maxHeights[stack[stack.length - 1]] >= maxHeights[i]) {
            stack.pop();
        }
        const prev = stack.length ? stack[stack.length - 1] : -1;
        if (prev === -1) {
            left[i] = maxHeights[i] * (i + 1);
        } else {
            left[i] = left[prev] + maxHeights[i] * (i - prev);
        }
        stack.push(i);
    }

    // compute right sums
    stack = [];
    for (let i = n - 1; i >= 0; i--) {
        while (stack.length && maxHeights[stack[stack.length - 1]] >= maxHeights[i]) {
            stack.pop();
        }
        const next = stack.length ? stack[stack.length - 1] : n;
        if (next === n) {
            right[i] = maxHeights[i] * (n - i);
        } else {
            right[i] = right[next] + maxHeights[i] * (next - i);
        }
        stack.push(i);
    }

    // combine left and right, subtract peak counted twice
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const total = left[i] + right[i] - maxHeights[i];
        if (total > ans) ans = total;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $maxHeights
     * @return Integer
     */
    function maximumSumOfHeights($maxHeights) {
        $n = count($maxHeights);
        if ($n == 0) return 0;

        $left = array_fill(0, $n, 0);
        $stack = [];

        // Compute left sums
        for ($i = 0; $i < $n; ++$i) {
            while (!empty($stack) && $maxHeights[$stack[count($stack)-1]] >= $maxHeights[$i]) {
                array_pop($stack);
            }
            if (empty($stack)) {
                $prev = -1;
                $left[$i] = $maxHeights[$i] * ($i - $prev);
            } else {
                $prev = $stack[count($stack)-1];
                $left[$i] = $left[$prev] + $maxHeights[$i] * ($i - $prev);
            }
            $stack[] = $i;
        }

        // Compute right sums
        $right = array_fill(0, $n, 0);
        $stack = [];
        for ($i = $n - 1; $i >= 0; --$i) {
            while (!empty($stack) && $maxHeights[$stack[count($stack)-1]] >= $maxHeights[$i]) {
                array_pop($stack);
            }
            if (empty($stack)) {
                $next = $n;
                $right[$i] = $maxHeights[$i] * ($next - $i);
            } else {
                $next = $stack[count($stack)-1];
                $right[$i] = $right[$next] + $maxHeights[$i] * ($next - $i);
            }
            $stack[] = $i;
        }

        // Find maximum total sum
        $ans = 0;
        for ($i = 0; $i < $n; ++$i) {
            $total = $left[$i] + $right[$i] - $maxHeights[$i];
            if ($total > $ans) {
                $ans = $total;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maximumSumOfHeights(_ maxHeights: [Int]) -> Int {
        let n = maxHeights.count
        var left = Array(repeating: Int64(0), count: n)
        var stackVal = [Int]()
        var stackCnt = [Int]()
        var cur: Int64 = 0
        
        for i in 0..<n {
            var cnt = 1
            while let last = stackVal.last, last >= maxHeights[i] {
                let poppedVal = stackVal.removeLast()
                let poppedCnt = stackCnt.removeLast()
                cnt += poppedCnt
                cur -= Int64(poppedVal) * Int64(poppedCnt)
            }
            stackVal.append(maxHeights[i])
            stackCnt.append(cnt)
            cur += Int64(maxHeights[i]) * Int64(cnt)
            left[i] = cur
        }
        
        var right = Array(repeating: Int64(0), count: n)
        stackVal.removeAll()
        stackCnt.removeAll()
        cur = 0
        
        for i in stride(from: n - 1, through: 0, by: -1) {
            var cnt = 1
            while let last = stackVal.last, last >= maxHeights[i] {
                let poppedVal = stackVal.removeLast()
                let poppedCnt = stackCnt.removeLast()
                cnt += poppedCnt
                cur -= Int64(poppedVal) * Int64(poppedCnt)
            }
            stackVal.append(maxHeights[i])
            stackCnt.append(cnt)
            cur += Int64(maxHeights[i]) * Int64(cnt)
            right[i] = cur
        }
        
        var ans: Int64 = 0
        for i in 0..<n {
            let total = left[i] + right[i] - Int64(maxHeights[i])
            if total > ans { ans = total }
        }
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumSumOfHeights(maxHeights: List<Int>): Long {
        val n = maxHeights.size
        val a = IntArray(n) { maxHeights[it] }
        val left = LongArray(n)
        val stack = IntArray(n)
        var top = -1

        // compute left contributions
        for (i in 0 until n) {
            while (top >= 0 && a[stack[top]] >= a[i]) {
                top--
            }
            if (top == -1) {
                left[i] = a[i].toLong() * (i + 1)
            } else {
                val j = stack[top]
                left[i] = left[j] + a[i].toLong() * (i - j)
            }
            stack[++top] = i
        }

        // compute right contributions
        val right = LongArray(n)
        top = -1
        for (i in n - 1 downTo 0) {
            while (top >= 0 && a[stack[top]] >= a[i]) {
                top--
            }
            if (top == -1) {
                right[i] = a[i].toLong() * (n - i)
            } else {
                val j = stack[top]
                right[i] = right[j] + a[i].toLong() * (j - i)
            }
            stack[++top] = i
        }

        var ans = 0L
        for (i in 0 until n) {
            val total = left[i] + right[i] - a[i]
            if (total > ans) ans = total
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maximumSumOfHeights(List<int> maxHeights) {
    int n = maxHeights.length;
    List<int> left = List.filled(n, 0);
    List<int> stack = [];

    for (int i = 0; i < n; i++) {
      while (stack.isNotEmpty &&
          maxHeights[stack.last] >= maxHeights[i]) {
        stack.removeLast();
      }
      int prev = stack.isEmpty ? -1 : stack.last;
      left[i] = (prev == -1 ? 0 : left[prev]) +
          maxHeights[i] * (i - prev);
      stack.add(i);
    }

    List<int> right = List.filled(n, 0);
    stack.clear();

    for (int i = n - 1; i >= 0; i--) {
      while (stack.isNotEmpty &&
          maxHeights[stack.last] >= maxHeights[i]) {
        stack.removeLast();
      }
      int next = stack.isEmpty ? n : stack.last;
      right[i] = (next == n ? 0 : right[next]) +
          maxHeights[i] * (next - i);
      stack.add(i);
    }

    int ans = 0;
    for (int i = 0; i < n; i++) {
      int total = left[i] + right[i] - maxHeights[i];
      if (total > ans) ans = total;
    }
    return ans;
  }
}
```

## Golang

```go
func maximumSumOfHeights(maxHeights []int) int64 {
	type pair struct {
		h   int64
		cnt int64
	}
	n := len(maxHeights)
	left := make([]int64, n)
	right := make([]int64, n)

	// compute left sums
	stack := make([]pair, 0)
	var sum int64 = 0
	for i := 0; i < n; i++ {
		h := int64(maxHeights[i])
		cnt := int64(1)
		for len(stack) > 0 && stack[len(stack)-1].h > h {
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			sum -= top.h * top.cnt
			cnt += top.cnt
		}
		stack = append(stack, pair{h: h, cnt: cnt})
		sum += h * cnt
		left[i] = sum
	}

	// compute right sums
	stack = stack[:0]
	sum = 0
	for i := n - 1; i >= 0; i-- {
		h := int64(maxHeights[i])
		cnt := int64(1)
		for len(stack) > 0 && stack[len(stack)-1].h > h {
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			sum -= top.h * top.cnt
			cnt += top.cnt
		}
		stack = append(stack, pair{h: h, cnt: cnt})
		sum += h * cnt
		right[i] = sum
	}

	var ans int64 = 0
	for i := 0; i < n; i++ {
		total := left[i] + right[i] - int64(maxHeights[i])
		if total > ans {
			ans = total
		}
	}
	return ans
}
```

## Ruby

```ruby
def maximum_sum_of_heights(max_heights)
  n = max_heights.length
  left = Array.new(n, 0)
  stack = []

  (0...n).each do |i|
    while !stack.empty? && max_heights[stack[-1]] >= max_heights[i]
      stack.pop
    end
    if stack.empty?
      left[i] = max_heights[i] * (i + 1)
    else
      prev = stack[-1]
      left[i] = left[prev] + max_heights[i] * (i - prev)
    end
    stack << i
  end

  right = Array.new(n, 0)
  stack.clear

  (n - 1).downto(0) do |i|
    while !stack.empty? && max_heights[stack[-1]] >= max_heights[i]
      stack.pop
    end
    if stack.empty?
      right[i] = max_heights[i] * (n - i)
    else
      nxt = stack[-1]
      right[i] = right[nxt] + max_heights[i] * (nxt - i)
    end
    stack << i
  end

  ans = 0
  (0...n).each do |i|
    total = left[i] + right[i] - max_heights[i]
    ans = total if total > ans
  end
  ans
end
```

## Scala

```scala
object Solution {
    def maximumSumOfHeights(maxHeights: List[Int]): Long = {
        val n = maxHeights.length
        val a = maxHeights.map(_.toLong).toArray
        val left = new Array[Long](n)
        val right = new Array[Long](n)

        import java.util.ArrayDeque
        val stack = new ArrayDeque[Int]()

        // compute left sums (prefix minima contributions)
        var i = 0
        while (i < n) {
            while (!stack.isEmpty && a(stack.peekLast()) >= a(i)) {
                stack.pollLast()
            }
            val prev = if (stack.isEmpty) -1 else stack.peekLast()
            val cnt = i - prev
            left(i) = (if (prev == -1) 0L else left(prev)) + a(i) * cnt
            stack.addLast(i)
            i += 1
        }

        // compute right sums (suffix minima contributions)
        stack.clear()
        i = n - 1
        while (i >= 0) {
            while (!stack.isEmpty && a(stack.peekLast()) >= a(i)) {
                stack.pollLast()
            }
            val next = if (stack.isEmpty) n else stack.peekLast()
            val cnt = next - i
            right(i) = (if (next == n) 0L else right(next)) + a(i) * cnt
            stack.addLast(i)
            i -= 1
        }

        var ans: Long = 0L
        i = 0
        while (i < n) {
            val total = left(i) + right(i) - a(i)
            if (total > ans) ans = total
            i += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_sum_of_heights(max_heights: Vec<i32>) -> i64 {
        let n = max_heights.len();
        if n == 0 {
            return 0;
        }
        // left[i]: sum for prefix [0..i] when i is the peak
        let mut left = vec![0i64; n];
        let mut stack: Vec<usize> = Vec::new(); // increasing values

        for i in 0..n {
            while let Some(&top) = stack.last() {
                if max_heights[top] >= max_heights[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            let prev: isize = if let Some(&top) = stack.last() {
                top as isize
            } else {
                -1
            };
            let prev_sum = if prev == -1 { 0 } else { left[prev as usize] };
            let cnt = (i as i64) - prev; // i - (-1) => i+1 when prev==-1
            left[i] = prev_sum + cnt * max_heights[i] as i64;
            stack.push(i);
        }

        // right[i]: sum for suffix [i..n-1] when i is the peak
        let mut right = vec![0i64; n];
        let mut stack2: Vec<usize> = Vec::new(); // increasing values from right to left

        for i_rev in (0..n).rev() {
            while let Some(&top) = stack2.last() {
                if max_heights[top] >= max_heights[i_rev] {
                    stack2.pop();
                } else {
                    break;
                }
            }
            let next: isize = if let Some(&top) = stack2.last() {
                top as isize
            } else {
                n as isize
            };
            let next_sum = if next == n as isize { 0 } else { right[next as usize] };
            let cnt = next - i_rev as isize; // number of positions from i_rev to next-1 inclusive
            right[i_rev] = next_sum + (cnt as i64) * max_heights[i_rev] as i64;
            stack2.push(i_rev);
        }

        let mut ans: i64 = 0;
        for i in 0..n {
            let total = left[i] + right[i] - max_heights[i] as i64; // peak counted twice
            if total > ans {
                ans = total;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (maximum-sum-of-heights maxHeights)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((arr (list->vector maxHeights))
         (n (vector-length arr)))
    (if (= n 0)
        0
        (let ((left (make-vector n 0))
              (right (make-vector n 0)))
          ;; compute left sums
          (let loop-left ((i 0) (stack '()))
            (when (< i n)
              (let* ((h (vector-ref arr i))
                     (new-stack
                      (let pop ((stk stack))
                        (if (or (null? stk)
                                (< (vector-ref arr (car stk)) h))
                            stk
                            (pop (cdr stk))))))
                (define j (if (null? new-stack) -1 (car new-stack)))
                (define left-sum (* h (- i j)))
                (when (> j -1)
                  (set! left-sum (+ left-sum (vector-ref left j))))
                (vector-set! left i left-sum)
                (loop-left (+ i 1) (cons i new-stack)))))
          ;; compute right sums
          (let loop-right ((i (- n 1)) (stack '()))
            (when (>= i 0)
              (let* ((h (vector-ref arr i))
                     (new-stack
                      (let pop ((stk stack))
                        (if (or (null? stk)
                                (< (vector-ref arr (car stk)) h))
                            stk
                            (pop (cdr stk))))))
                (define j (if (null? new-stack) n (car new-stack)))
                (define right-sum (* h (- j i)))
                (when (< j n)
                  (set! right-sum (+ right-sum (vector-ref right j))))
                (vector-set! right i right-sum)
                (loop-right (- i 1) (cons i new-stack)))))
          ;; find maximum total
          (let ((best 0))
            (for ([i (in-range n)])
              (define total
                (+ (vector-ref left i)
                   (vector-ref right i)
                   (- (vector-ref arr i))))
              (when (> total best)
                (set! best total)))
            best)))))
```

## Erlang

```erlang
-module(solution).
-export([maximum_sum_of_heights/1]).

-spec maximum_sum_of_heights(MaxHeights :: [integer()]) -> integer().
maximum_sum_of_heights(MaxHeights) ->
    N = length(MaxHeights),
    MaxArr = array:from_list(MaxHeights),

    %% compute left sums
    LeftInit = array:new(N, {default,0}),
    {LeftArr,_} = forward(0, N, MaxArr, LeftInit, []),

    %% compute right sums
    RightInit = array:new(N, {default,0}),
    RightArr = backward(N-1, N, MaxArr, RightInit, []),

    %% find maximum total
    MaxTotal = max_total(0, N, LeftArr, RightArr, MaxArr, 0),
    MaxTotal.

%% forward pass: compute left sums where each position is peak of prefix
forward(I, N, _MaxArr, LeftArr, Stack) when I == N ->
    {LeftArr, Stack};
forward(I, N, MaxArr, LeftArr, Stack) ->
    Curr = array:get(I, MaxArr),
    NewStack = pop_while(Stack, Curr, MaxArr),
    J = case NewStack of
            [] -> -1;
            [Top|_] -> Top
        end,
    LeftPrev = if J == -1 -> 0; true -> array:get(J, LeftArr) end,
    LeftI = LeftPrev + Curr * (I - J),
    UpdatedLeftArr = array:set(I, LeftI, LeftArr),
    forward(I+1, N, MaxArr, UpdatedLeftArr, [I|NewStack]).

%% backward pass: compute right sums where each position is peak of suffix
backward(I, _N, _MaxArr, RightArr, _Stack) when I < 0 ->
    RightArr;
backward(I, N, MaxArr, RightArr, Stack) ->
    Curr = array:get(I, MaxArr),
    NewStack = pop_while(Stack, Curr, MaxArr),
    J = case NewStack of
            [] -> N;
            [Top|_] -> Top
        end,
    RightPrev = if J == N -> 0; true -> array:get(J, RightArr) end,
    RightI = RightPrev + Curr * (J - I),
    UpdatedRightArr = array:set(I, RightI, RightArr),
    backward(I-1, N, MaxArr, UpdatedRightArr, [I|NewStack]).

%% pop elements from stack while their value >= current
pop_while([], _Curr, _MaxArr) ->
    [];
pop_while([Top|Rest]=Stack, Curr, MaxArr) ->
    TopVal = array:get(Top, MaxArr),
    if TopVal >= Curr -> pop_while(Rest, Curr, MaxArr);
       true -> Stack
    end.

%% compute maximum total sum over all possible peaks
max_total(I, N, LeftArr, RightArr, MaxArr, CurrentMax) when I == N ->
    CurrentMax;
max_total(I, N, LeftArr, RightArr, MaxArr, CurrentMax) ->
    L = array:get(I, LeftArr),
    R = array:get(I, RightArr),
    M = array:get(I, MaxArr),
    Total = L + R - M,
    NewMax = if Total > CurrentMax -> Total; true -> CurrentMax end,
    max_total(I+1, N, LeftArr, RightArr, MaxArr, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_sum_of_heights(max_heights :: [integer]) :: integer
  def maximum_sum_of_heights(max_heights) do
    n = length(max_heights)
    mh_arr = :array.from_list(max_heights)

    # compute left sums
    {left_arr, _stack_left, _cur_left} =
      Enum.reduce(0..(n - 1), {:array.new(n, default: 0), [], 0}, fn i,
                                                                    {arr, stack, cur} ->
        val = :array.get(i, mh_arr)
        cnt = 1

        {stack2, cur2, cnt2} = pop_greater(stack, cur, cnt, val)

        stack3 = [{val, cnt2} | stack2]
        cur3 = cur2 + val * cnt2
        arr = :array.set(i, cur3, arr)
        {arr, stack3, cur3}
      end)

    # compute right sums
    indices_desc = :lists.seq(n - 1, 0, -1)

    {right_arr, _stack_right, _cur_right} =
      Enum.reduce(indices_desc, {:array.new(n, default: 0), [], 0}, fn i,
                                                                      {arr, stack, cur} ->
        val = :array.get(i, mh_arr)
        cnt = 1

        {stack2, cur2, cnt2} = pop_greater(stack, cur, cnt, val)

        stack3 = [{val, cnt2} | stack2]
        cur3 = cur2 + val * cnt2
        arr = :array.set(i, cur3, arr)
        {arr, stack3, cur3}
      end)

    # find maximum total sum
    Enum.reduce(0..(n - 1), 0, fn i, best ->
      total =
        :array.get(i, left_arr) + :array.get(i, right_arr) - :array.get(i, mh_arr)

      if total > best, do: total, else: best
    end)
  end

  defp pop_greater([], cur, cnt, _val), do: {[], cur, cnt}

  defp pop_greater([{v, c} | rest], cur, cnt, val) when v >= val do
    cur = cur - v * c
    cnt = cnt + c
    pop_greater(rest, cur, cnt, val)
  end

  defp pop_greater(stack, cur, cnt, _val), do: {stack, cur, cnt}
end
```
