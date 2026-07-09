# 1856. Maximum Subarray Min-Product

## Cpp

```cpp
class Solution {
public:
    int maxSumMinProduct(vector<int>& nums) {
        const long long MOD = 1'000'000'007LL;
        int n = nums.size();
        vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        
        vector<int> left(n), right(n);
        stack<int> st;
        // compute left boundaries
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && nums[st.top()] >= nums[i]) st.pop();
            left[i] = st.empty() ? -1 : st.top();
            st.push(i);
        }
        while (!st.empty()) st.pop();
        // compute right boundaries
        for (int i = n - 1; i >= 0; --i) {
            while (!st.empty() && nums[st.top()] >= nums[i]) st.pop();
            right[i] = st.empty() ? n : st.top();
            st.push(i);
        }
        
        long long best = 0;
        for (int i = 0; i < n; ++i) {
            long long sum = prefix[right[i]] - prefix[left[i] + 1];
            long long prod = sum * nums[i];
            if (prod > best) best = prod;
        }
        return (int)(best % MOD);
    }
};
```

## Java

```java
class Solution {
    public int maxSumMinProduct(int[] nums) {
        int n = nums.length;
        long MOD = 1_000_000_007L;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }

        int[] left = new int[n];
        int[] right = new int[n];
        java.util.ArrayDeque<Integer> stack = new java.util.ArrayDeque<>();

        // previous less element
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) {
                stack.pop();
            }
            left[i] = stack.isEmpty() ? 0 : stack.peek() + 1;
            stack.push(i);
        }

        // next less element
        stack.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) {
                stack.pop();
            }
            right[i] = stack.isEmpty() ? n - 1 : stack.peek() - 1;
            stack.push(i);
        }

        long maxProd = 0;
        for (int i = 0; i < n; i++) {
            long sum = prefix[right[i] + 1] - prefix[left[i]];
            long prod = sum * (long) nums[i];
            if (prod > maxProd) {
                maxProd = prod;
            }
        }

        return (int) (maxProd % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def maxSumMinProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        # prefix sums
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        right = [n] * n
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        max_product = 0
        for i in range(n):
            total = pref[right[i]] - pref[left[i] + 1]
            product = nums[i] * total
            if product > max_product:
                max_product = product

        return max_product % MOD
```

## Python3

```python
from typing import List

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        left = [-1] * n
        right = [n] * n

        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        MOD = 10 ** 9 + 7
        ans = 0
        for i in range(n):
            total = prefix[right[i]] - prefix[left[i] + 1]
            prod = total * nums[i]
            if prod > ans:
                ans = prod

        return ans % MOD
```

## C

```c
#include <stdlib.h>

int maxSumMinProduct(int* nums, int numsSize) {
    const long long MOD = 1000000007LL;
    int n = numsSize;

    long long *pref = (long long *)malloc((n + 1) * sizeof(long long));
    pref[0] = 0;
    for (int i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + nums[i];
    }

    int *left = (int *)malloc(n * sizeof(int));
    int *right = (int *)malloc(n * sizeof(int));
    int *stack = (int *)malloc(n * sizeof(int));
    int top = -1;

    // previous less element
    for (int i = 0; i < n; ++i) {
        while (top >= 0 && nums[stack[top]] >= nums[i]) {
            --top;
        }
        left[i] = (top == -1) ? 0 : stack[top] + 1;
        stack[++top] = i;
    }

    // next less element
    top = -1;
    for (int i = n - 1; i >= 0; --i) {
        while (top >= 0 && nums[stack[top]] >= nums[i]) {
            --top;
        }
        right[i] = (top == -1) ? n - 1 : stack[top] - 1;
        stack[++top] = i;
    }

    long long maxProd = 0;
    for (int i = 0; i < n; ++i) {
        long long sum = pref[right[i] + 1] - pref[left[i]];
        long long prod = (long long)nums[i] * sum;
        if (prod > maxProd) {
            maxProd = prod;
        }
    }

    free(pref);
    free(left);
    free(right);
    free(stack);

    return (int)(maxProd % MOD);
}
```

## Csharp

```csharp
public class Solution {
    public int MaxSumMinProduct(int[] nums) {
        int n = nums.Length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; ++i)
            prefix[i + 1] = prefix[i] + nums[i];

        int[] left = new int[n];
        int[] right = new int[n];
        var stack = new Stack<int>();

        // Find previous smaller element index
        for (int i = 0; i < n; ++i) {
            while (stack.Count > 0 && nums[stack.Peek()] >= nums[i])
                stack.Pop();
            left[i] = stack.Count == 0 ? -1 : stack.Peek();
            stack.Push(i);
        }

        stack.Clear();

        // Find next smaller element index
        for (int i = n - 1; i >= 0; --i) {
            while (stack.Count > 0 && nums[stack.Peek()] >= nums[i])
                stack.Pop();
            right[i] = stack.Count == 0 ? n : stack.Peek();
            stack.Push(i);
        }

        long maxProduct = 0;
        const long MOD = 1_000_000_007L;

        for (int i = 0; i < n; ++i) {
            int l = left[i] + 1;
            int r = right[i] - 1;
            long sum = prefix[r + 1] - prefix[l];
            long product = (long)nums[i] * sum;
            if (product > maxProduct)
                maxProduct = product;
        }

        return (int)(maxProduct % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSumMinProduct = function(nums) {
    const n = nums.length;
    const pref = new Array(n + 1);
    pref[0] = 0n;
    for (let i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + BigInt(nums[i]);
    }

    const left = new Array(n);
    const right = new Array(n);
    let stack = [];

    // previous less element
    for (let i = 0; i < n; ++i) {
        while (stack.length && nums[stack[stack.length - 1]] >= nums[i]) {
            stack.pop();
        }
        left[i] = stack.length ? stack[stack.length - 1] : -1;
        stack.push(i);
    }

    // next less element
    stack = [];
    for (let i = n - 1; i >= 0; --i) {
        while (stack.length && nums[stack[stack.length - 1]] >= nums[i]) {
            stack.pop();
        }
        right[i] = stack.length ? stack[stack.length - 1] : n;
        stack.push(i);
    }

    const MOD = 1000000007n;
    let ans = 0n;

    for (let i = 0; i < n; ++i) {
        const l = left[i] + 1;
        const r = right[i] - 1;
        const sum = pref[r + 1] - pref[l];
        const prod = BigInt(nums[i]) * sum;
        if (prod > ans) ans = prod;
    }

    return Number(ans % MOD);
};
```

## Typescript

```typescript
function maxSumMinProduct(nums: number[]): number {
    const n = nums.length;
    const prefix = new Array<number>(n + 1);
    prefix[0] = 0;
    for (let i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + nums[i];
    }

    const MOD = 1000000007n;
    let maxProd = 0n;
    const stack: number[] = [];

    for (let i = 0; i < n; i++) {
        while (stack.length && nums[stack[stack.length - 1]] > nums[i]) {
            const idx = stack.pop()!;
            const left = stack.length ? stack[stack.length - 1] : -1;
            const right = i;
            const sum = prefix[right] - prefix[left + 1];
            const prod = BigInt(nums[idx]) * BigInt(sum);
            if (prod > maxProd) maxProd = prod;
        }
        stack.push(i);
    }

    while (stack.length) {
        const idx = stack.pop()!;
        const left = stack.length ? stack[stack.length - 1] : -1;
        const right = n;
        const sum = prefix[right] - prefix[left + 1];
        const prod = BigInt(nums[idx]) * BigInt(sum);
        if (prod > maxProd) maxProd = prod;
    }

    return Number(maxProd % MOD);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSumMinProduct($nums) {
        $mod = 1000000007;
        $n = count($nums);
        // Prefix sums
        $prefix = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $prefix[$i + 1] = $prefix[$i] + $nums[$i];
        }
        // Previous less element
        $prevLess = array_fill(0, $n, -1);
        $stack = [];
        for ($i = 0; $i < $n; $i++) {
            while (!empty($stack) && $nums[end($stack)] >= $nums[$i]) {
                array_pop($stack);
            }
            $prevLess[$i] = empty($stack) ? -1 : end($stack);
            $stack[] = $i;
        }
        // Next less element
        $nextLess = array_fill(0, $n, $n);
        $stack = [];
        for ($i = $n - 1; $i >= 0; $i--) {
            while (!empty($stack) && $nums[end($stack)] >= $nums[$i]) {
                array_pop($stack);
            }
            $nextLess[$i] = empty($stack) ? $n : end($stack);
            $stack[] = $i;
        }
        // Compute max product
        $maxProd = 0;
        for ($i = 0; $i < $n; $i++) {
            $left = $prevLess[$i];
            $right = $nextLess[$i];
            $sum = $prefix[$right] - $prefix[$left + 1];
            $prod = $nums[$i] * $sum;
            if ($prod > $maxProd) {
                $maxProd = $prod;
            }
        }
        return $maxProd % $mod;
    }
}
```

## Swift

```swift
class Solution {
    func maxSumMinProduct(_ nums: [Int]) -> Int {
        let n = nums.count
        var prefix = [Int64](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + Int64(nums[i])
        }
        
        var left = [Int](repeating: -1, count: n)
        var right = [Int](repeating: n, count: n)
        var stack = [Int]()
        
        // previous smaller element (strictly less)
        for i in 0..<n {
            while let last = stack.last, nums[last] >= nums[i] {
                stack.removeLast()
            }
            left[i] = stack.last ?? -1
            stack.append(i)
        }
        
        stack.removeAll()
        // next smaller element (strictly less) using opposite comparison to handle duplicates
        for i in stride(from: n - 1, through: 0, by: -1) {
            while let last = stack.last, nums[last] > nums[i] {
                stack.removeLast()
            }
            right[i] = stack.last ?? n
            stack.append(i)
        }
        
        let MOD: Int64 = 1_000_000_007
        var best: Int64 = 0
        
        for i in 0..<n {
            let l = left[i]
            let r = right[i]
            // sum of subarray (l+1 ... r-1)
            let total = prefix[r] - prefix[l + 1]
            let product = Int64(nums[i]) * total
            if product > best {
                best = product
            }
        }
        
        return Int(best % MOD)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxSumMinProduct(nums: IntArray): Int {
        val n = nums.size
        val pref = LongArray(n + 1)
        for (i in 0 until n) {
            pref[i + 1] = pref[i] + nums[i].toLong()
        }

        val left = IntArray(n)
        val right = IntArray(n)

        val stack = java.util.ArrayDeque<Int>()

        // previous smaller element
        for (i in 0 until n) {
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) {
                stack.pop()
            }
            left[i] = if (stack.isEmpty()) -1 else stack.peek()
            stack.push(i)
        }

        stack.clear()

        // next smaller element
        for (i in n - 1 downTo 0) {
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) {
                stack.pop()
            }
            right[i] = if (stack.isEmpty()) n else stack.peek()
            stack.push(i)
        }

        var maxProd = 0L
        val MOD = 1_000_000_007L

        for (i in 0 until n) {
            val l = left[i]
            val r = right[i]
            val sum = pref[r] - pref[l + 1]
            val prod = nums[i].toLong() * sum
            if (prod > maxProd) maxProd = prod
        }

        return ((maxProd % MOD).toInt())
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int maxSumMinProduct(List<int> nums) {
    final int n = nums.length;
    final List<int> prefix = List.filled(n + 1, 0);
    for (int i = 0; i < n; ++i) {
      prefix[i + 1] = prefix[i] + nums[i];
    }

    final List<int> left = List.filled(n, -1);
    final List<int> right = List.filled(n, n);
    final List<int> stack = [];

    // previous smaller element (strict)
    for (int i = 0; i < n; ++i) {
      while (stack.isNotEmpty && nums[stack.last] >= nums[i]) {
        stack.removeLast();
      }
      left[i] = stack.isEmpty ? -1 : stack.last;
      stack.add(i);
    }

    // next smaller element (strict)
    stack.clear();
    for (int i = n - 1; i >= 0; --i) {
      while (stack.isNotEmpty && nums[stack.last] > nums[i]) {
        stack.removeLast();
      }
      right[i] = stack.isEmpty ? n : stack.last;
      stack.add(i);
    }

    int maxProd = 0;
    for (int i = 0; i < n; ++i) {
      final int sum = prefix[right[i]] - prefix[left[i] + 1];
      final int prod = nums[i] * sum;
      if (prod > maxProd) maxProd = prod;
    }

    return maxProd % _MOD;
  }
}
```

## Golang

```go
func maxSumMinProduct(nums []int) int {
	const MOD int64 = 1_000_000_007
	n := len(nums)

	// Prefix sums
	prefix := make([]int64, n+1)
	for i, v := range nums {
		prefix[i+1] = prefix[i] + int64(v)
	}

	left := make([]int, n)
	right := make([]int, n)

	// Compute left boundaries (previous smaller element)
	stack := []int{}
	for i := 0; i < n; i++ {
		for len(stack) > 0 && nums[stack[len(stack)-1]] >= nums[i] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			left[i] = -1
		} else {
			left[i] = stack[len(stack)-1]
		}
		stack = append(stack, i)
	}

	// Compute right boundaries (next smaller element)
	stack = []int{}
	for i := n - 1; i >= 0; i-- {
		for len(stack) > 0 && nums[stack[len(stack)-1]] > nums[i] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			right[i] = n
		} else {
			right[i] = stack[len(stack)-1]
		}
		stack = append(stack, i)
	}

	var maxProd int64
	for i := 0; i < n; i++ {
		sum := prefix[right[i]] - prefix[left[i]+1]
		prod := int64(nums[i]) * sum
		if prod > maxProd {
			maxProd = prod
		}
	}
	return int(maxProd % MOD)
}
```

## Ruby

```ruby
def max_sum_min_product(nums)
  n = nums.length
  pref = Array.new(n + 1, 0)
  (0...n).each { |i| pref[i + 1] = pref[i] + nums[i] }

  left = Array.new(n)
  stack = []
  (0...n).each do |i|
    while !stack.empty? && nums[stack[-1]] >= nums[i]
      stack.pop
    end
    left[i] = stack.empty? ? 0 : stack[-1] + 1
    stack << i
  end

  right = Array.new(n)
  stack.clear
  (n - 1).downto(0) do |i|
    while !stack.empty? && nums[stack[-1]] > nums[i]
      stack.pop
    end
    right[i] = stack.empty? ? n - 1 : stack[-1] - 1
    stack << i
  end

  max_product = 0
  (0...n).each do |i|
    total = pref[right[i] + 1] - pref[left[i]]
    prod = nums[i] * total
    max_product = prod if prod > max_product
  end

  max_product % 1_000_000_007
end
```

## Scala

```scala
object Solution {
  def maxSumMinProduct(nums: Array[Int]): Int = {
    val n = nums.length
    val pref = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) + nums(i).toLong
      i += 1
    }

    val left = new Array[Int](n)
    val right = new Array[Int](n)

    import java.util.ArrayDeque
    val stack = new ArrayDeque[Int]()

    // previous smaller element (strictly less)
    i = 0
    while (i < n) {
      while (!stack.isEmpty && nums(stack.peekLast) >= nums(i)) {
        stack.pollLast()
      }
      left(i) = if (stack.isEmpty) -1 else stack.peekLast
      stack.addLast(i)
      i += 1
    }

    // next smaller element (strictly less)
    stack.clear()
    i = n - 1
    while (i >= 0) {
      while (!stack.isEmpty && nums(stack.peekLast) > nums(i)) {
        stack.pollLast()
      }
      right(i) = if (stack.isEmpty) n else stack.peekLast
      stack.addLast(i)
      i -= 1
    }

    var ans: Long = 0L
    val MOD = 1000000007L

    i = 0
    while (i < n) {
      val l = left(i) + 1
      val r = right(i) - 1
      val sum = pref(r + 1) - pref(l)
      val prod = nums(i).toLong * sum
      if (prod > ans) ans = prod
      i += 1
    }

    ((ans % MOD).toInt)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_sum_min_product(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let mut left = vec![0usize; n];
        let mut right = vec![n - 1; n];

        // Find previous smaller element for each position
        let mut stack: Vec<usize> = Vec::new();
        for i in 0..n {
            while let Some(&last) = stack.last() {
                if nums[last] >= nums[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            left[i] = if let Some(&last) = stack.last() { last + 1 } else { 0 };
            stack.push(i);
        }

        // Find next smaller element for each position
        stack.clear();
        for i in (0..n).rev() {
            while let Some(&last) = stack.last() {
                if nums[last] >= nums[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            right[i] = if let Some(&last) = stack.last() { last - 1 } else { n - 1 };
            stack.push(i);
        }

        // Prefix sums
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + nums[i] as i64;
        }

        const MOD: i64 = 1_000_000_007;
        let mut max_prod: i64 = 0;

        for i in 0..n {
            let sum = pref[right[i] + 1] - pref[left[i]];
            let prod = nums[i] as i64 * sum;
            if prod > max_prod {
                max_prod = prod;
            }
        }

        (max_prod % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(define/contract (max-sum-min-product nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((v (list->vector nums))
         (n (vector-length v))
         (pref (make-vector (+ n 1) 0)))
    ;; prefix sums
    (for ([i (in-range n)])
      (vector-set! pref (add1 i)
                   (+ (vector-ref pref i) (vector-ref v i))))
    (define max-prod 0)
    (define stack (make-vector n))
    (define top -1)

    ;; main scan
    (let loop ((i 0))
      (when (< i n)
        (let inner ()
          (when (and (>= top 0)
                     (< (vector-ref v i) (vector-ref v (vector-ref stack top))))
            (define idx (vector-ref stack top))
            (set! top (- top 1))
            (define left (if (>= top 0) (vector-ref stack top) -1))
            (define right (sub1 i))
            (define sum
              (- (vector-ref pref (add1 right))
                 (vector-ref pref (add1 left))))
            (define prod (* (vector-ref v idx) sum))
            (when (> prod max-prod) (set! max-prod prod))
            (inner)))
        (set! top (+ top 1))
        (vector-set! stack top i)
        (loop (add1 i))))

    ;; process remaining elements in stack
    (let recur ()
      (when (>= top 0)
        (define idx (vector-ref stack top))
        (set! top (- top 1))
        (define left (if (>= top 0) (vector-ref stack top) -1))
        (define right (sub1 n))
        (define sum
          (- (vector-ref pref (add1 right))
             (vector-ref pref (add1 left))))
        (define prod (* (vector-ref v idx) sum))
        (when (> prod max-prod) (set! max-prod prod))
        (recur)))
    (modulo max-prod MOD)))
```

## Erlang

```erlang
-spec max_sum_min_product(Nums :: [integer()]) -> integer().
max_sum_min_product(Nums) ->
    Mod = 1000000007,
    N = length(Nums),
    NumT = list_to_tuple(Nums),
    {_, RevPref} = lists:foldl(fun (Val,{Sum,Acc}) -> {Sum+Val,[Sum+Val|Acc]} end, {0, []}, Nums),
    PrefList = [0 | lists:reverse(RevPref)],
    PrefT = list_to_tuple(PrefList),
    MaxProd = loop(0, [], 0, NumT, PrefT, N),
    MaxProd rem Mod.

loop(I, Stack, Max, _NumT, _PrefT, N) when I > N ->
    Max;
loop(I, Stack, Max, NumT, PrefT, N) ->
    CurVal = if I < N -> element(I+1, NumT); true -> 0 end,
    {NewStack, NewMax} = pop_update(CurVal, I, Stack, Max, NumT, PrefT),
    loop(I+1, [I|NewStack], NewMax, NumT, PrefT, N).

pop_update(_CurVal, _I, [], Max, _NumT, _PrefT) ->
    {[], Max};
pop_update(CurVal, I, [Top|Rest]=Stack, Max, NumT, PrefT) ->
    TopVal = element(Top+1, NumT),
    if TopVal >= CurVal ->
            LeftIdx = case Rest of [] -> -1; [L|_] -> L end,
            RightIdx = I-1,
            Sum = element(RightIdx+1, PrefT) - element(LeftIdx+1, PrefT),
            Prod = TopVal * Sum,
            NewMax = if Prod > Max -> Prod; true -> Max end,
            pop_update(CurVal, I, Rest, NewMax, NumT, PrefT);
       true ->
            {Stack, Max}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @moduledoc false

  @spec max_sum_min_product(nums :: [integer]) :: integer
  def max_sum_min_product(nums) do
    mod = 1_000_000_007
    n = length(nums)
    nums_t = List.to_tuple(nums)

    # prefix sums tuple: prefix[i] = sum of first i elements, prefix[0]=0
    prefix_list =
      Enum.reduce(nums, [0], fn x, acc ->
        [hd(acc) + x | acc]
      end)
      |> :lists.reverse()

    prefix = List.to_tuple(prefix_list)

    {max_prod, _stack} =
      Enum.reduce(0..n, {0, []}, fn i, {cur_max, stack} ->
        cur_val = if i < n, do: elem(nums_t, i), else: 0

        {new_stack, new_max} = pop_while_less(cur_val, i, stack, nums_t, prefix, cur_max)

        final_stack = if i < n, do: [i | new_stack], else: new_stack
        {new_max, final_stack}
      end)

    rem(max_prod, mod)
  end

  defp pop_while_less(_cur, _idx, [], _nums_t, _prefix, max), do: {[], max}

  defp pop_while_less(cur, idx, [top | rest] = stack, nums_t, prefix, max) do
    top_val = elem(nums_t, top)

    if cur < top_val do
      left =
        case rest do
          [] -> -1
          [l | _] -> l
        end

      sum_sub = elem(prefix, idx) - elem(prefix, left + 1)
      prod = top_val * sum_sub
      new_max = if prod > max, do: prod, else: max
      pop_while_less(cur, idx, rest, nums_t, prefix, new_max)
    else
      {stack, max}
    end
  end
end
```
