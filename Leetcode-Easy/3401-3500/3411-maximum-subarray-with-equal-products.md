# 3411. Maximum Subarray With Equal Products

## Cpp

```cpp
class Solution {
public:
    int maxLength(vector<int>& nums) {
        const vector<int> primes = {2, 3, 5, 7};
        int n = nums.size();
        int best = 0;
        for (int i = 0; i < n; ++i) {
            int cnt[4] = {0, 0, 0, 0};
            for (int j = i; j < n; ++j) {
                int x = nums[j];
                for (int k = 0; k < 4; ++k) {
                    if (x % primes[k] == 0) cnt[k]++;
                }
                bool ok = true;
                int len = j - i + 1;
                if (len >= 3) {
                    for (int k = 0; k < 4; ++k) {
                        if (cnt[k] >= 2) { ok = false; break; }
                    }
                }
                if (ok) best = max(best, len);
            }
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int maxLength(int[] nums) {
        int n = nums.length;
        int[] masks = new int[n];
        int[] primes = {2, 3, 5, 7};
        for (int i = 0; i < n; ++i) {
            int x = nums[i];
            int mask = 0;
            for (int p = 0; p < primes.length; ++p) {
                if (x % primes[p] == 0) {
                    mask |= 1 << p;
                    while (x % primes[p] == 0) {
                        x /= primes[p];
                    }
                }
            }
            masks[i] = mask;
        }

        int maxLen = 0;
        for (int i = 0; i < n; ++i) {
            // length 1 subarray
            if (nums[i] == 1) {
                maxLen = Math.max(maxLen, 1);
            }
            int curMask = masks[i];
            for (int j = i + 1; j < n; ++j) {
                int len = j - i + 1;
                int m = masks[j];
                if ((curMask & m) != 0) {
                    // overlapping prime factors: subarray of length >=2 is still valid,
                    // but cannot be extended further.
                    maxLen = Math.max(maxLen, 2);
                    break;
                }
                curMask |= m;
                if (len == 2) {
                    maxLen = Math.max(maxLen, 2);
                } else {
                    maxLen = Math.max(maxLen, len);
                }
            }
        }
        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        primes = [2, 3, 5, 7]  # possible prime factors for numbers <=10
        masks = []
        for v in nums:
            m = 0
            for i, p in enumerate(primes):
                if v % p == 0:
                    m |= 1 << i
            masks.append(m)

        n = len(nums)
        left = 0
        cur_mask = 0
        best = 1  # at least one element (all ones are valid)
        for right in range(n):
            m = masks[right]
            while cur_mask & m:
                cur_mask ^= masks[left]
                left += 1
            cur_mask |= m
            best = max(best, right - left + 1)

        # any subarray of length 2 is always product equivalent
        if n >= 2:
            best = max(best, 2)
        return best
```

## Python3

```python
class Solution:
    def maxLength(self, nums):
        from math import inf
        # primes up to 10
        primes = [2, 3, 5, 7]
        # precompute exponent vectors for each number
        exp_list = []
        for x in nums:
            vec = []
            for p in primes:
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                vec.append(cnt)
            exp_list.append(vec)

        n = len(nums)
        best = 1  # at least one element subarray always satisfies condition
        for i in range(n):
            sum_e = [0] * 4
            max_e = [0] * 4
            min_e = [inf] * 4
            for j in range(i, n):
                vec = exp_list[j]
                for k in range(4):
                    e = vec[k]
                    sum_e[k] += e
                    if e > max_e[k]:
                        max_e[k] = e
                    if e < min_e[k]:
                        min_e[k] = e
                # check condition: for each prime, sum == max + min
                ok = True
                for k in range(4):
                    if sum_e[k] != max_e[k] + min_e[k]:
                        ok = False
                        break
                if ok:
                    length = j - i + 1
                    if length > best:
                        best = length
        return best
```

## C

```c
int factorMask(int x){
    int mask = 0;
    if (x % 2 == 0) mask |= 1;   // bit 0 for prime 2
    if (x % 3 == 0) mask |= 2;   // bit 1 for prime 3
    if (x % 5 == 0) mask |= 4;   // bit 2 for prime 5
    if (x % 7 == 0) mask |= 8;   // bit 3 for prime 7
    return mask;
}

int maxLength(int* nums, int numsSize) {
    int left = 0, best = 0;
    int curMask = 0;
    for (int right = 0; right < numsSize; ++right) {
        int m = factorMask(nums[right]);
        while ((curMask & m) != 0) {
            curMask ^= factorMask(nums[left]);
            ++left;
        }
        curMask |= m;
        if (right - left + 1 > best)
            best = right - left + 1;
    }
    return best;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MaxLength(int[] nums) {
        int n = nums.Length;
        int[] prime = new int[] {2,3,5,7};
        int[] masks = new int[n];
        for (int i = 0; i < n; i++) {
            int m = 0;
            if (nums[i] % 2 == 0) m |= 1 << 0;
            if (nums[i] % 3 == 0) m |= 1 << 1;
            if (nums[i] % 5 == 0) m |= 1 << 2;
            if (nums[i] % 7 == 0) m |= 1 << 3;
            masks[i] = m;
        }

        int left = 0, curMask = 0, best = 0;
        for (int right = 0; right < n; right++) {
            while ((curMask & masks[right]) != 0) {
                curMask ^= masks[left];
                left++;
            }
            curMask |= masks[right];
            int len = right - left + 1;
            if (len > best) best = len;
        }

        // any subarray of length 2 is always product equivalent
        int atLeastTwo = Math.Min(2, n);
        return Math.Max(best, atLeastTwo);
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxLength = function(nums) {
    const factorMap = {
        1: [0,0,0,0],
        2: [1,0,0,0],
        3: [0,1,0,0],
        4: [2,0,0,0],
        5: [0,0,1,0],
        6: [1,1,0,0],
        7: [0,0,0,1],
        8: [3,0,0,0],
        9: [0,2,0,0],
        10:[1,0,1,0]
    };
    const n = nums.length;
    let best = 0;
    for (let i = 0; i < n; ++i) {
        const sum = [0,0,0,0];
        const maxExp = [0,0,0,0];
        const minExp = [Infinity, Infinity, Infinity, Infinity];
        for (let j = i; j < n; ++j) {
            const f = factorMap[nums[j]];
            for (let p = 0; p < 4; ++p) {
                const e = f[p];
                sum[p] += e;
                if (e > maxExp[p]) maxExp[p] = e;
                if (e < minExp[p]) minExp[p] = e;
            }
            let ok = true;
            for (let p = 0; p < 4; ++p) {
                const mx = maxExp[p];
                const mn = (minExp[p] === Infinity ? 0 : minExp[p]);
                if (sum[p] !== mx + mn) { ok = false; break; }
            }
            if (ok) {
                const len = j - i + 1;
                if (len > best) best = len;
            }
        }
    }
    return best;
};
```

## Typescript

```typescript
function maxLength(nums: number[]): number {
    const n = nums.length;
    let ans = 0;

    const bigGcd = (a: bigint, b: bigint): bigint => {
        let x = a, y = b;
        while (y !== 0n) {
            const t = x % y;
            x = y;
            y = t;
        }
        return x;
    };
    const bigLcm = (a: bigint, b: bigint): bigint => {
        if (a === 0n || b === 0n) return 0n;
        return a / bigGcd(a, b) * b;
    };

    for (let i = 0; i < n; ++i) {
        let prod = 1n;
        let curGcd = 0n;
        let curLcm = 1n;
        for (let j = i; j < n; ++j) {
            const val = BigInt(nums[j]);
            prod *= val;
            if (j === i) {
                curGcd = val;
                curLcm = val;
            } else {
                curGcd = bigGcd(curGcd, val);
                curLcm = bigLcm(curLcm, val);
            }
            if (prod === curLcm * curGcd) {
                const len = j - i + 1;
                if (len > ans) ans = len;
            }
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxLength($nums) {
        $n = count($nums);
        $maxLen = 0;
        $primes = [2, 3, 5, 7];
        for ($i = 0; $i < $n; $i++) {
            $cnt = array_fill_keys($primes, 0);
            for ($j = $i; $j < $n; $j++) {
                $val = $nums[$j];
                foreach ($primes as $p) {
                    if ($val % $p == 0) {
                        $cnt[$p]++;
                    }
                }
                $valid = true;
                foreach ($cnt as $c) {
                    if ($c > 2) {
                        $valid = false;
                        break;
                    }
                }
                if (!$valid) {
                    // further extension will only increase counts, so stop this start index
                    break;
                }
                $len = $j - $i + 1;
                if ($len > $maxLen) {
                    $maxLen = $len;
                }
            }
        }
        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func maxLength(_ nums: [Int]) -> Int {
        let primes = [2, 3, 5, 7]
        // precompute exponent vectors for numbers 1...10
        var expTable = [[Int]](repeating: Array(repeating: 0, count: primes.count), count: 11)
        for num in 1...10 {
            var x = num
            for (idx, p) in primes.enumerated() {
                var cnt = 0
                while x % p == 0 && x > 0 {
                    cnt += 1
                    x /= p
                }
                expTable[num][idx] = cnt
            }
        }

        let n = nums.count
        var answer = 0

        for i in 0..<n {
            var sum = Array(repeating: 0, count: primes.count)
            var maxExp = Array(repeating: 0, count: primes.count)
            var minExp = Array(repeating: Int.max, count: primes.count)

            for j in i..<n {
                let vec = expTable[nums[j]]
                for k in 0..<primes.count {
                    sum[k] += vec[k]
                    if vec[k] > maxExp[k] { maxExp[k] = vec[k] }
                    if vec[k] < minExp[k] { minExp[k] = vec[k] }
                }

                var ok = true
                for k in 0..<primes.count {
                    if sum[k] != maxExp[k] + minExp[k] {
                        ok = false
                        break
                    }
                }
                if ok {
                    let len = j - i + 1
                    if len > answer { answer = len }
                }
            }
        }

        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxLength(nums: IntArray): Int {
        val primes = intArrayOf(2, 3, 5, 7)
        val cnt = IntArray(primes.size)
        var left = 0
        var best = 0
        for (right in nums.indices) {
            val v = nums[right]
            for (i in primes.indices) {
                if (v % primes[i] == 0) cnt[i]++
            }
            while (cnt.any { it > 2 }) {
                val lv = nums[left]
                for (i in primes.indices) {
                    if (lv % primes[i] == 0) cnt[i]--
                }
                left++
            }
            best = kotlin.math.max(best, right - left + 1)
        }
        return best
    }
}
```

## Dart

```dart
class Solution {
  int maxLength(List<int> nums) {
    int n = nums.length;
    const List<int> primes = [2, 3, 5, 7];
    List<int> masks = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      int x = nums[i];
      int mask = 0;
      for (int j = 0; j < primes.length; j++) {
        if (x % primes[j] == 0) {
          mask |= (1 << j);
        }
      }
      masks[i] = mask;
    }

    int left = 0;
    int usedMask = 0;
    int maxLen = 0;

    for (int right = 0; right < n; right++) {
      int curMask = masks[right];
      while ((usedMask & curMask) != 0) {
        usedMask ^= masks[left];
        left++;
      }
      usedMask |= curMask;
      int len = right - left + 1;
      if (len > maxLen) maxLen = len;
    }

    // Any subarray of length 2 is always product equivalent.
    int minTwo = n >= 2 ? 2 : n;
    return maxLen > minTwo ? maxLen : minTwo;
  }
}
```

## Golang

```go
func maxLength(nums []int) int {
    n := len(nums)
    primes := []int{2, 3, 5, 7}
    exp := make([][4]int, n)
    for i, v := range nums {
        x := v
        for j, p := range primes {
            cnt := 0
            for x%p == 0 {
                cnt++
                x /= p
            }
            exp[i][j] = cnt
        }
    }

    maxLen := 0
    const INF = int(1 << 30)
    for l := 0; l < n; l++ {
        sum := [4]int{}
        min := [4]int{INF, INF, INF, INF}
        maxv := [4]int{}
        for r := l; r < n; r++ {
            for p := 0; p < 4; p++ {
                e := exp[r][p]
                sum[p] += e
                if e < min[p] {
                    min[p] = e
                }
                if e > maxv[p] {
                    maxv[p] = e
                }
            }
            ok := true
            for p := 0; p < 4; p++ {
                if sum[p] != min[p]+maxv[p] {
                    ok = false
                    break
                }
            }
            if ok {
                length := r - l + 1
                if length > maxLen {
                    maxLen = length
                }
            }
        }
    }
    return maxLen
}
```

## Ruby

```ruby
def max_length(nums)
  prime_to_bit = {2 => 0, 3 => 1, 5 => 2, 7 => 3}
  masks = nums.map do |x|
    m = 0
    y = x
    prime_to_bit.each do |p, bit|
      if y % p == 0
        m |= (1 << bit)
        while y % p == 0
          y /= p
        end
      end
    end
    m
  end

  left = 0
  used = 0
  max_len = 0

  masks.each_with_index do |mask, right|
    while (used & mask) != 0
      used ^= masks[left]
      left += 1
    end
    used |= mask
    cur = right - left + 1
    max_len = cur if cur > max_len
  end

  max_len
end
```

## Scala

```scala
object Solution {
    def maxLength(nums: Array[Int]): Int = {
        def gcd(a: Int, b: Int): Int = {
            var x = a
            var y = b
            while (y != 0) {
                val t = x % y
                x = y
                y = t
            }
            x
        }

        val n = nums.length
        var best = 0

        for (i <- 0 until n) {
            var prod: BigInt = BigInt(1)
            var curGcd = 0
            var curLcm: BigInt = BigInt(1)

            for (j <- i until n) {
                val x = nums(j)
                prod *= x

                if (curGcd == 0) curGcd = x
                else curGcd = gcd(curGcd, x)

                val g = curLcm.gcd(BigInt(x))
                curLcm = (curLcm / g) * x

                if (prod == curLcm * curGcd) {
                    best = math.max(best, j - i + 1)
                }
            }
        }

        best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_length(nums: Vec<i32>) -> i32 {
        fn factor(x: i32) -> [i32; 4] {
            let primes = [2, 3, 5, 7];
            let mut n = x;
            let mut res = [0i32; 4];
            for (idx, &p) in primes.iter().enumerate() {
                while n % p == 0 && n > 1 {
                    res[idx] += 1;
                    n /= p;
                }
            }
            res
        }

        let n = nums.len();
        let factors: Vec<[i32; 4]> = nums.iter().map(|&v| factor(v)).collect();

        let mut ans = 0i32;

        for i in 0..n {
            let mut sum = [0i32; 4];
            let mut min_exp = [i32::MAX; 4];
            let mut max_exp = [0i32; 4];

            for j in i..n {
                let f = factors[j];
                for p in 0..4 {
                    sum[p] += f[p];
                    if f[p] < min_exp[p] {
                        min_exp[p] = f[p];
                    }
                    if f[p] > max_exp[p] {
                        max_exp[p] = f[p];
                    }
                }

                let mut ok = true;
                for p in 0..4 {
                    if sum[p] != max_exp[p] + min_exp[p] {
                        ok = false;
                        break;
                    }
                }
                if ok {
                    ans = ans.max((j - i + 1) as i32);
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (max-length nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (vec (list->vector nums)))
    (let loop-i ((i 0) (best 0))
      (if (= i n)
          best
          (let inner-loop ((j i) (prod 1) (g 0) (l 1) (cur-best best))
            (if (= j n)
                (loop-i (+ i 1) cur-best)
                (let* ((val (vector-ref vec j))
                       (new-prod (* prod val))
                       (new-g (if (= g 0) val (gcd g val)))
                       (new-l (/ (* l val) (gcd l val))))
                  (define new-best
                    (if (= new-prod (* new-l new-g))
                        (max cur-best (+ 1 (- j i))) ; length of subarray [i..j]
                        cur-best))
                  (inner-loop (+ j 1) new-prod new-g new-l new-best)))))))))
```

## Erlang

```erlang
-spec max_length(Nums :: [integer()]) -> integer().
max_length(Nums) ->
    N = length(Nums),
    Indices = lists:seq(0, N - 1),
    max_len_loop(Indices, Nums, 0).

max_len_loop([], _List, Max) ->
    Max;
max_len_loop([Start | Rest], List, Max) ->
    UpdatedMax = expand_from(Start, length(List), List, 0, 0, Max),
    max_len_loop(Rest, List, UpdatedMax).

expand_from(Pos, N, List, Mask, LenSoFar, MaxAcc) when Pos >= N ->
    MaxAcc;
expand_from(Pos, N, List, Mask, LenSoFar, MaxAcc) ->
    Num = lists:nth(Pos + 1, List),
    CurMask = prime_mask(Num),
    NewLen = LenSoFar + 1,
    case NewLen of
        1 ->
            NewMax = if Num == 1 -> erlang:max(MaxAcc, 1); true -> MaxAcc end,
            expand_from(Pos + 1, N, List, CurMask, NewLen, NewMax);
        2 ->
            Overlap = CurMask band Mask,
            Max2 = erlang:max(MaxAcc, 2),
            case Overlap of
                0 ->
                    NewMask = Mask bor CurMask,
                    expand_from(Pos + 1, N, List, NewMask, NewLen, Max2);
                _ ->
                    Max2
            end;
        _ ->
            if (CurMask band Mask) =/= 0 ->
                    MaxAcc;
               true ->
                    NewMask = Mask bor CurMask,
                    NewMax = erlang:max(MaxAcc, NewLen),
                    expand_from(Pos + 1, N, List, NewMask, NewLen, NewMax)
            end
    end.

prime_mask(1) -> 0;
prime_mask(N) ->
    M1 = if N rem 2 == 0 -> 1; true -> 0 end,
    M2 = if N rem 3 == 0 -> 2; true -> 0 end,
    M3 = if N rem 5 == 0 -> 4; true -> 0 end,
    M4 = if N rem 7 == 0 -> 8; true -> 0 end,
    M1 bor M2 bor M3 bor M4.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec max_length(nums :: [integer]) :: integer
  def max_length(nums) do
    masks = Enum.map(nums, &prime_mask/1)
    n = length(masks)

    {_, _, best} =
      Enum.reduce(0..(n - 1), %{left: 0, cur_mask: 0, ans: 0}, fn right, acc ->
        m = Enum.at(masks, right)

        {new_left, new_cur} = shrink(acc.left, acc.cur_mask, masks, m)

        updated_cur = new_cur ||| m
        window_len = right - new_left + 1
        new_ans = max(acc.ans, window_len)

        %{left: new_left, cur_mask: updated_cur, ans: new_ans}
      end)
      |> Map.pop(:left)
      |> elem(0)
      |> Map.pop(:cur_mask)
      |> elem(0)
      |> Map.pop(:ans)
      |> elem(0)

    max(best, 2)
  end

  defp prime_mask(num) do
    primes = [{2, 0}, {3, 1}, {5, 2}, {7, 3}]

    Enum.reduce(primes, 0, fn {p, bit}, acc ->
      if rem(num, p) == 0 do
        acc ||| (1 <<< bit)
      else
        acc
      end
    end)
  end

  defp shrink(left, cur_mask, masks, m) do
    if (cur_mask &&& m) != 0 do
      lmask = Enum.at(masks, left)
      shrink(left + 1, cur_mask ^^^ lmask, masks, m)
    else
      {left, cur_mask}
    end
  end
end
```
