# 2811. Check if it is Possible to Split Array

## Cpp

```cpp
class Solution {
public:
    bool canSplitArray(vector<int>& nums, int m) {
        int n = nums.size();
        if (n == 1) return true;
        for (int i = 0; i < n; ++i) {
            if (nums[i] >= m) return true;
            if (i + 1 < n && nums[i] + nums[i + 1] >= m) return true;
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean canSplitArray(java.util.List<Integer> nums, int m) {
        int n = nums.size();
        if (n == 1) return true;
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = nums.get(i);
        int[] pref = new int[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + a[i];

        boolean[][] dp = new boolean[n][n];
        for (int i = 0; i < n; i++) dp[i][i] = true;

        for (int len = 2; len <= n; len++) {
            for (int l = 0; l + len - 1 < n; l++) {
                int r = l + len - 1;
                int sum = pref[r + 1] - pref[l];
                if (sum < m) continue; // cannot be good, thus cannot split
                // try all possible split points
                for (int k = l; k < r; k++) {
                    if (dp[l][k] && dp[k + 1][r]) {
                        dp[l][r] = true;
                        break;
                    }
                }
            }
        }
        return dp[0][n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def canSplitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: bool
        """
        n = len(nums)
        if n <= 1:
            return True
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        for i in range(n):
            for j in range(i+2, n+1):  # subarray length at least 2
                if (prefix[j] - prefix[i]) % m == 0:
                    return True
        return False
```

## Python3

```python
class Solution:
    def canSplitArray(self, nums, m):
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        def seg_sum(l, r):
            return pref[r + 1] - pref[l]

        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for length in range(2, n + 1):
            for l in range(0, n - length + 1):
                r = l + length - 1
                ok = False
                for k in range(l, r):
                    left_len = k - l + 1
                    right_len = r - k
                    cond_left = (left_len == 1) or (seg_sum(l, k) >= m)
                    cond_right = (right_len == 1) or (seg_sum(k + 1, r) >= m)
                    if cond_left and cond_right and dp[l][k] and dp[k + 1][r]:
                        ok = True
                        break
                dp[l][r] = ok

        return dp[0][n - 1]
```

## C

```c
bool canSplitArray(int* nums, int numsSize, int m) {
    if (numsSize == 0) return true;
    static int dp[101][101];
    static int prefix[102];
    for (int i = 0; i <= numsSize; ++i) dp[i][i] = -1;
    prefix[0] = 0;
    for (int i = 0; i < numsSize; ++i) {
        prefix[i + 1] = prefix[i] + nums[i];
    }
    // helper lambda using recursion with memoization
    int (*solve)(int, int);
    solve = ^int(int l, int r) {
        if (l == r) return 1;
        int &res = dp[l][r];
        if (res != -1) return res;
        for (int k = l; k < r; ++k) {
            int leftLen = k - l + 1;
            int rightLen = r - k;
            int leftSum = prefix[k + 1] - prefix[l];
            int rightSum = prefix[r + 1] - prefix[k + 1];
            int leftGood = (leftLen == 1) || (leftSum >= m);
            int rightGood = (rightLen == 1) || (rightSum >= m);
            if (leftGood && rightGood) {
                if (solve(l, k) && solve(k + 1, r)) {
                    res = 1;
                    return res;
                }
            }
        }
        res = 0;
        return res;
    };
    // initialize dp with -1
    for (int i = 0; i < numsSize; ++i)
        for (int j = i; j < numsSize; ++j)
            dp[i][j] = -1;
    return solve(0, numsSize - 1);
}
```

## Csharp

```csharp
public class Solution {
    public bool CanSplitArray(IList<int> nums, int m) {
        var firstIdx = new Dictionary<int, int>();
        int prefix = 0;
        // index 0 corresponds to empty prefix
        firstIdx[0] = 0;
        for (int i = 0; i < nums.Count; i++) {
            prefix = (prefix + nums[i]) % m;
            if (firstIdx.TryGetValue(prefix, out int prev)) {
                // current position is i+1 elements processed
                if ((i + 1) - prev >= 2) return true;
            } else {
                firstIdx[prefix] = i + 1;
            }
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} m
 * @return {boolean}
 */
var canSplitArray = function(nums, m) {
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        prefix[i + 1] = prefix[i] + nums[i];
    }
    const dp = new Array(n + 1).fill(false);
    dp[0] = true;
    for (let i = 1; i <= n; ++i) {
        for (let j = 0; j < i; ++j) {
            if (dp[j] && prefix[i] - prefix[j] >= m) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[n];
};
```

## Typescript

```typescript
function canSplitArray(nums: number[], m: number): boolean {
    const n = nums.length;
    // dp[l][r] indicates whether subarray nums[l..r] (inclusive) is good.
    const dp: boolean[][] = Array.from({ length: n }, () => Array(n).fill(false));

    // Base case: single element arrays are always good.
    for (let i = 0; i < n; ++i) dp[i][i] = true;

    // Precompute prefix sums for quick range sum queries.
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) pref[i + 1] = pref[i] + nums[i];

    const rangeSum = (l: number, r: number): number => pref[r + 1] - pref[l];

    // Determine goodness of larger subarrays.
    for (let len = 2; len <= n; ++len) {
        for (let l = 0; l + len - 1 < n; ++l) {
            const r = l + len - 1;
            // An array is good if we can split it into two good parts.
            // The condition for a split to be valid is that both resulting
            // subarrays have sum not exceeding m. This follows from the
            // problem's definition and the provided hint.
            const total = rangeSum(l, r);
            if (total > 2 * m) continue; // impossible to keep both sides ≤ m

            for (let k = l; k < r; ++k) {
                const leftSum = rangeSum(l, k);
                const rightSum = total - leftSum;
                if (leftSum <= m && rightSum <= m && dp[l][k] && dp[k + 1][r]) {
                    dp[l][r] = true;
                    break;
                }
            }
        }
    }

    return dp[0][n - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $m
     * @return Boolean
     */
    function canSplitArray($nums, $m) {
        $seen = [];
        foreach ($nums as $num) {
            $rem = $num % $m;
            if ($rem == 0) {
                return true;
            }
            if (isset($seen[$rem])) {
                return true;
            }
            $seen[$rem] = true;
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func canSplitArray(_ nums: [Int], _ m: Int) -> Bool {
        let n = nums.count
        if n <= 1 { return true }
        var prefix = 0
        var seen = Set<Int>()
        for num in nums {
            prefix = (prefix + num) % m
            if prefix == 0 { return true }
            if seen.contains(prefix) { return true }
            seen.insert(prefix)
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canSplitArray(nums: List<Int>, m: Int): Boolean {
        val seen = HashSet<Int>()
        var sumMod = 0
        for (num in nums) {
            sumMod = (sumMod + num) % m
            if (sumMod == 0) return true
            if (!seen.add(sumMod)) return true
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool canSplitArray(List<int> nums, int m) {
    int n = nums.length;
    if (n == 1) return true;
    for (int i = 0; i < n; ++i) {
      int sum = 0;
      for (int j = i; j < n; ++j) {
        sum += nums[j];
        if (j - i + 1 >= 2 && sum % m == 0) return true;
      }
    }
    return false;
  }
}
```

## Golang

```go
func canSplitArray(nums []int, m int) bool {
	n := len(nums)
	if n == 0 {
		return true
	}
	prefix := make([]int, n+1)
	for i := 0; i < n; i++ {
		prefix[i+1] = prefix[i] + nums[i]
	}
	sum := func(l, r int) int { // inclusive indices
		return prefix[r+1] - prefix[l]
	}

	dp := make([][]bool, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]bool, n)
		dp[i][i] = true // single element is trivially good
	}

	for length := 2; length <= n; length++ {
		for l := 0; l+length-1 < n; l++ {
			r := l + length - 1
			for k := l; k < r; k++ {
				leftLen := k - l + 1
				rightLen := r - (k + 1) + 1

				leftGood := leftLen == 1 || sum(l, k)%m == 0
				rightGood := rightLen == 1 || sum(k+1, r)%m == 0

				if leftGood && rightGood && dp[l][k] && dp[k+1][r] {
					dp[l][r] = true
					break
				}
			}
		}
	}

	return dp[0][n-1]
}
```

## Ruby

```ruby
def can_split_array(nums, m)
  n = nums.length
  prefix = Array.new(n + 1, 0)
  (0...n).each { |i| prefix[i + 1] = prefix[i] + nums[i] }

  dp = Array.new(n) { Array.new(n, false) }
  (0...n).each { |i| dp[i][i] = true }

  (len = 2..n).each do |length|
    (0..n - length).each do |l|
      r = l + length - 1
      (l...r).each do |k|
        left_sum = prefix[k + 1] - prefix[l]
        right_sum = prefix[r + 1] - prefix[k + 1]
        if left_sum % m == 0 && right_sum % m == 0 && dp[l][k] && dp[k + 1][r]
          dp[l][r] = true
          break
        end
      end
    end
  end

  dp[0][n - 1]
end
```

## Scala

```scala
object Solution {
    def canSplitArray(nums: List[Int], m: Int): Boolean = {
        var pref = 0
        val firstIdx = scala.collection.mutable.Map[Int, Int]()
        firstIdx(0) = 0 // prefix sum modulo at index 0
        var idx = 1
        for (num <- nums) {
            pref = (pref + num) % m
            if (firstIdx.contains(pref)) {
                val i = firstIdx(pref)
                if (idx - i >= 2) return true
            } else {
                firstIdx(pref) = idx
            }
            idx += 1
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_split_array(nums: Vec<i32>, m: i32) -> bool {
        let n = nums.len();
        if n <= 1 {
            return true;
        }
        // prefix sums
        let mut pref = vec![0i32; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + nums[i];
        }
        for i in 0..n {
            for j in (i + 2)..=n { // subarray length at least 2
                if (pref[j] - pref[i]) % m == 0 {
                    return true;
                }
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (can-split-array nums m)
  (-> (listof exact-integer?) exact-integer? boolean?)
  (let* ((n (length nums))
         (arr (list->vector nums))
         ;; prefix sums: pref[i] = sum of first i elements, pref[0]=0
         (pref (let ([v (make-vector (+ n 1) 0)])
                 (for ([i (in-range n)])
                   (vector-set! v (+ i 1) (+ (vector-ref v i) (vector-ref arr i))))
                 v))
         ;; helper to get sum of subarray [l, r] inclusive
         (subsum (lambda (l r)
                   (- (vector-ref pref (+ r 1)) (vector-ref pref l))))
         (memo (make-hash)))
    (letrec ((possible
               (lambda (l r)
                 (cond
                   [(= l r) #t] ; single element is always good
                   [else
                    (define key (cons l r))
                    (if (hash-has-key? memo key)
                        (hash-ref memo key)
                        (let loop ((k l))
                          (if (> k (- r 1))
                              (begin
                                (hash-set! memo key #f)
                                #f)
                              (let* ((left-good (or (= (+ 1 (- k l)) 1) ; length 1
                                                    (= (modulo (subsum l k) m) 0)))
                                     (right-good (or (= (+ 1 (- r k)) 1)
                                                     (= (modulo (subsum (+ k 1) r) m) 0))))
                                (if (and left-good right-good
                                         (possible l k)
                                         (possible (+ k 1) r))
                                    (begin
                                      (hash-set! memo key #t)
                                      #t)
                                    (loop (+ k 1))))))])))))
      (if (= n 0) #t (possible 0 (- n 1))))))
```

## Erlang

```erlang
-spec can_split_array([integer()], integer()) -> boolean().
can_split_array(Nums, M) ->
    case length(Nums) of
        1 -> true;
        N ->
            Prefix = build_prefix(Nums, M, [0]),
            check_subarray(Prefix, N + 1, M)
    end.

build_prefix([], _M, Acc) ->
    lists:reverse(Acc);
build_prefix([H|T], M, [Prev|_]=Acc) ->
    New = (Prev + H) rem M,
    build_prefix(T, M, [New|Acc]).

check_subarray(Prefix, Len, M) ->
    check_i(0, Prefix, Len, M).

check_i(I, _Prefix, Len, _M) when I >= Len - 2 -> false;
check_i(I, Prefix, Len, M) ->
    Pi = lists:nth(I + 1, Prefix), % prefix at position I
    case check_j(I + 2, Pi, Prefix, Len, M) of
        true -> true;
        false -> check_i(I + 1, Prefix, Len, M)
    end.

check_j(J, _Pi, _Prefix, Len, _M) when J > Len ->
    false;
check_j(J, Pi, Prefix, Len, M) ->
    Pj = lists:nth(J, Prefix),
    Diff = (Pj - Pi) rem M,
    Mod = if Diff < 0 -> Diff + M; true -> Diff end,
    if Mod == 0 ->
            true;
       true ->
            check_j(J + 1, Pi, Prefix, Len, M)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_split_array(nums :: [integer], m :: integer) :: boolean
  def can_split_array(nums, m) do
    n = length(nums)
    # build prefix sums
    prefix =
      Enum.reduce(nums, [0], fn x, acc ->
        [hd(acc) + x | acc]
      end)
      |> Enum.reverse()

    dp = %{}

    dp =
      Enum.reduce(1..n, dp, fn len, dp_acc ->
        Enum.reduce(0..(n - len), dp_acc, fn i, dp_inner ->
          j = i + len - 1
          sum = Enum.at(prefix, j + 1) - Enum.at(prefix, i)
          good = rem(sum, m) == 0

          if not good and len > 1 do
            split_good =
              Enum.any?(i..(j - 1), fn k ->
                Map.get(dp_inner, {i, k}, false) and Map.get(dp_inner, {k + 1, j}, false)
              end)

            good = good or split_good
          end

          if good do
            Map.put(dp_inner, {i, j}, true)
          else
            dp_inner
          end
        end)
      end)

    Map.get(dp, {0, n - 1}, false)
  end
end
```
