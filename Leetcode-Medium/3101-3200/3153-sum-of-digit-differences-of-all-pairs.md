# 3153. Sum of Digit Differences of All Pairs

## Cpp

```cpp
class Solution {
public:
    long long sumDigitDifferences(vector<int>& nums) {
        int n = nums.size();
        // Determine number of digits (all numbers have same length)
        int len = 0;
        int temp = nums[0];
        while (temp > 0) {
            ++len;
            temp /= 10;
        }
        long long total = 0;
        long long pow10 = 1;
        for (int pos = 0; pos < len; ++pos) {
            int cnt[10] = {0};
            for (int x : nums) {
                int digit = (x / pow10) % 10;
                ++cnt[digit];
            }
            long long contribution = 0;
            for (int d = 0; d < 10; ++d) {
                contribution += (long long)cnt[d] * (n - cnt[d]);
            }
            total += contribution;
            pow10 *= 10;
        }
        // each unordered pair counted twice
        return total / 2;
    }
};
```

## Java

```java
class Solution {
    public long sumDigitDifferences(int[] nums) {
        int n = nums.length;
        // Determine the number of digits (all numbers have same length)
        int maxDigits = 0;
        int temp = nums[0];
        while (temp > 0) {
            maxDigits++;
            temp /= 10;
        }
        long answer = 0L;
        int divisor = 1;
        for (int pos = 0; pos < maxDigits; pos++) {
            int[] freq = new int[10];
            for (int num : nums) {
                int digit = (num / divisor) % 10;
                freq[digit]++;
            }
            long diffPairs = 0L;
            for (int cnt : freq) {
                diffPairs += (long) cnt * (n - cnt);
            }
            answer += diffPairs / 2; // each unordered pair counted twice
            divisor *= 10;
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def sumDigitDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0

        # Determine number of digits (all numbers have same length)
        first = nums[0]
        L = 0
        while first > 0:
            L += 1
            first //= 10

        # counts[pos][digit] = frequency of digit at position pos (0 = units)
        counts = [[0] * 10 for _ in range(L)]

        for num in nums:
            x = num
            for pos in range(L):
                d = x % 10
                counts[pos][d] += 1
                x //= 10

        total_pairs = n * (n - 1) // 2
        ans = 0
        for pos in range(L):
            same = 0
            for c in counts[pos]:
                same += c * (c - 1) // 2
            ans += total_pairs - same

        return ans
```

## Python3

```python
class Solution:
    def sumDigitDifferences(self, nums):
        n = len(nums)
        strs = [str(num) for num in nums]
        L = len(strs[0])
        ans = 0
        for i in range(L):
            cnt = [0] * 10
            for s in strs:
                d = ord(s[i]) - 48
                cnt[d] += 1
            for c in cnt:
                ans += c * (n - c)
        return ans // 2
```

## C

```c
long long sumDigitDifferences(int* nums, int numsSize) {
    if (numsSize <= 1) return 0;
    int n = numsSize;
    // Determine number of digits (all numbers have same length)
    int temp = nums[0];
    int digitCount = 0;
    while (temp > 0) {
        digitCount++;
        temp /= 10;
    }
    long long result = 0;
    int divisor = 1; // 10^position
    for (int pos = 0; pos < digitCount; ++pos) {
        int cnt[10] = {0};
        for (int i = 0; i < n; ++i) {
            int digit = (nums[i] / divisor) % 10;
            cnt[digit]++;
        }
        long long diffPairsOrdered = 0;
        for (int d = 0; d < 10; ++d) {
            long long c = cnt[d];
            diffPairsOrdered += c * (n - c);
        }
        // each unordered pair counted twice
        result += diffPairsOrdered / 2;
        divisor *= 10;
    }
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public long SumDigitDifferences(int[] nums) {
        int n = nums.Length;
        // Determine the number of digits (all numbers have same length)
        int temp = nums[0];
        int digitCount = 0;
        while (temp > 0) {
            digitCount++;
            temp /= 10;
        }

        long total = 0;
        int divisor = 1;
        for (int pos = 0; pos < digitCount; pos++) {
            int[] freq = new int[10];
            foreach (int num in nums) {
                int digit = (num / divisor) % 10;
                freq[digit]++;
            }

            long sumDiff = 0;
            for (int d = 0; d <= 9; d++) {
                sumDiff += (long)freq[d] * (n - freq[d]);
            }
            total += sumDiff / 2; // each unordered pair counted twice
            divisor *= 10;
        }

        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var sumDigitDifferences = function(nums) {
    const n = nums.length;
    // determine the common digit length
    let len = 0;
    let t = nums[0];
    while (t > 0) {
        len++;
        t = Math.floor(t / 10);
    }
    // precompute powers of 10
    const pow10 = new Array(len + 1);
    pow10[0] = 1;
    for (let i = 1; i <= len; i++) pow10[i] = pow10[i - 1] * 10;

    let total = 0;
    for (let pos = 0; pos < len; pos++) {
        const cnt = new Array(10).fill(0);
        const div = pow10[pos];
        for (const num of nums) {
            const digit = Math.floor(num / div) % 10;
            cnt[digit]++;
        }
        let diffPairsSum = 0;
        for (let d = 0; d < 10; d++) {
            const c = cnt[d];
            diffPairsSum += c * (n - c);
        }
        total += diffPairsSum / 2; // each unordered pair counted twice
    }
    return total;
};
```

## Typescript

```typescript
function sumDigitDifferences(nums: number[]): number {
    const n = nums.length;
    if (n < 2) return 0;

    // Determine the common number of digits
    let temp = nums[0];
    let digitCount = 0;
    while (temp > 0) {
        digitCount++;
        temp = Math.floor(temp / 10);
    }

    let total = 0;
    let pow = 1; // 10^position

    for (let pos = 0; pos < digitCount; pos++) {
        const cnt = new Array(10).fill(0);
        for (const num of nums) {
            const digit = Math.floor(num / pow) % 10;
            cnt[digit]++;
        }

        let posSum = 0;
        for (let d = 0; d < 10; d++) {
            posSum += cnt[d] * (n - cnt[d]);
        }
        total += posSum / 2; // each unordered pair counted twice
        pow *= 10;
    }

    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumDigitDifferences($nums) {
        $n = count($nums);
        // All numbers have the same length; get it from first element
        $len = strlen((string)$nums[0]);
        $pow10 = 1;
        $total = 0;

        for ($pos = 0; $pos < $len; $pos++) {
            $freq = array_fill(0, 10, 0);
            foreach ($nums as $num) {
                $digit = intdiv($num, $pow10) % 10;
                $freq[$digit]++;
            }
            for ($d = 0; $d < 10; $d++) {
                $c = $freq[$d];
                if ($c > 0) {
                    $total += $c * ($n - $c);
                }
            }
            $pow10 *= 10;
        }

        // each unordered pair counted twice
        return intdiv($total, 2);
    }
}
```

## Swift

```swift
class Solution {
    func sumDigitDifferences(_ nums: [Int]) -> Int {
        let n = nums.count
        if n < 2 { return 0 }
        
        // Determine number of digits (all numbers have same length)
        var temp = nums[0]
        var digitCount = 0
        repeat {
            digitCount += 1
            temp /= 10
        } while temp > 0
        
        var result: Int64 = 0
        var pow10 = 1
        for _ in 0..<digitCount {
            var freq = [Int](repeating: 0, count: 10)
            for num in nums {
                let digit = (num / pow10) % 10
                freq[digit] += 1
            }
            
            let totalPairs = Int64(n) * Int64(n - 1) / 2
            var samePairs: Int64 = 0
            for cnt in freq where cnt > 1 {
                samePairs += Int64(cnt) * Int64(cnt - 1) / 2
            }
            result += totalPairs - samePairs
            pow10 *= 10
        }
        
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sumDigitDifferences(nums: IntArray): Long {
        val n = nums.size
        var maxDigits = 0
        var temp = nums[0]
        while (temp > 0) {
            maxDigits++
            temp /= 10
        }
        var result = 0L
        var divisor = 1
        repeat(maxDigits) {
            val freq = IntArray(10)
            for (num in nums) {
                val digit = (num / divisor) % 10
                freq[digit]++
            }
            var diffPairs = 0L
            for (c in freq) {
                diffPairs += c.toLong() * (n - c)
            }
            result += diffPairs / 2
            divisor *= 10
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int sumDigitDifferences(List<int> nums) {
    int n = nums.length;
    if (n < 2) return 0;

    // All numbers have the same number of digits.
    int len = nums[0].toString().length;

    // Precompute powers of 10 for digit extraction.
    List<int> pow10 = List.filled(len, 1);
    for (int i = 1; i < len; i++) {
      pow10[i] = pow10[i - 1] * 10;
    }

    int total = 0;

    for (int pos = 0; pos < len; pos++) {
      List<int> freq = List.filled(10, 0);
      int divisor = pow10[pos];
      for (int num in nums) {
        int digit = (num ~/ divisor) % 10;
        freq[digit]++;
      }
      for (int d = 0; d < 10; d++) {
        total += freq[d] * (n - freq[d]);
      }
    }

    return total ~/ 2;
  }
}
```

## Golang

```go
func sumDigitDifferences(nums []int) int64 {
    n := len(nums)
    if n == 0 {
        return 0
    }

    // Determine the number of digits (all numbers have same length)
    maxDigits := 0
    temp := nums[0]
    for temp > 0 {
        maxDigits++
        temp /= 10
    }

    // Precompute powers of 10 for each digit position
    pow10 := make([]int, maxDigits)
    p := 1
    for i := 0; i < maxDigits; i++ {
        pow10[i] = p
        p *= 10
    }

    var total int64
    nInt64 := int64(n)

    for pos := 0; pos < maxDigits; pos++ {
        freq := [10]int{}
        divisor := pow10[pos]
        for _, num := range nums {
            digit := (num / divisor) % 10
            freq[digit]++
        }

        var sum int64
        for d := 0; d < 10; d++ {
            c := int64(freq[d])
            sum += c * (nInt64 - c)
        }
        total += sum / 2 // each unordered pair counted twice
    }

    return total
}
```

## Ruby

```ruby
def sum_digit_differences(nums)
  n = nums.length
  len = nums[0].to_s.length
  total = 0
  pow10 = 1
  len.times do
    counts = Array.new(10, 0)
    nums.each do |num|
      digit = (num / pow10) % 10
      counts[digit] += 1
    end
    counts.each { |c| total += c * (n - c) }
    pow10 *= 10
  end
  total / 2
end
```

## Scala

```scala
object Solution {
    def sumDigitDifferences(nums: Array[Int]): Long = {
        val n = nums.length
        var len = 0
        var temp = nums(0)
        while (temp > 0) {
            len += 1
            temp /= 10
        }
        if (len == 0) len = 1

        val pow10 = new Array[Int](len)
        var p = 1
        var idx = 0
        while (idx < len) {
            pow10(idx) = p
            p *= 10
            idx += 1
        }

        var totalOrdered: Long = 0L

        var pos = 0
        while (pos < len) {
            val freq = new Array[Int](10)
            var i = 0
            while (i < n) {
                val digit = (nums(i) / pow10(pos)) % 10
                freq(digit) += 1
                i += 1
            }
            var d = 0
            while (d < 10) {
                val c = freq(d)
                totalOrdered += c.toLong * (n - c)
                d += 1
            }
            pos += 1
        }

        totalOrdered / 2
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sum_digit_differences(nums: Vec<i32>) -> i64 {
        let n = nums.len() as i64;
        if n <= 1 {
            return 0;
        }
        // Determine the maximum value to know how many digit positions exist
        let mut max_val = 0i32;
        for &v in &nums {
            if v > max_val {
                max_val = v;
            }
        }

        let mut ans: i64 = 0;
        let mut pow: i32 = 1; // 10^position

        while pow <= max_val {
            let mut cnt = [0i64; 10];
            for &num in &nums {
                let digit = ((num / pow) % 10) as usize;
                cnt[digit] += 1;
            }

            let mut pos_sum: i64 = 0;
            for &c in &cnt {
                pos_sum += c * (n - c);
            }
            ans += pos_sum / 2; // each unordered pair counted twice
            pow *= 10;
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (sum-digit-differences nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (first (car nums))
         (len (string-length (number->string first))))
    (let loop-pos ((pos 0) (total 0))
      (if (= pos len)
          (quotient total 2)
          (let ((counts (make-vector 10 0)))
            (for-each
             (lambda (num)
               (let* ((digit (modulo (quotient num (expt 10 pos)) 10)))
                 (vector-set! counts digit (+ (vector-ref counts digit) 1))))
             nums)
            (let loop-digit ((d 0) (pos-sum 0))
              (if (= d 10)
                  (loop-pos (+ pos 1) (+ total pos-sum))
                  (let* ((c (vector-ref counts d))
                         (add (* c (- n c))))
                    (loop-digit (+ d 1) (+ pos-sum add))))))))))
```

## Erlang

```erlang
-spec sum_digit_differences([integer()]) -> integer().
sum_digit_differences(Nums) ->
    N = length(Nums),
    [First|_] = Nums,
    Len = length(integer_to_list(First)),
    TotalOrdered = positions_contrib(N, Len, Nums, 0, 1, 0),
    TotalOrdered div 2.

positions_contrib(_N, Len, _Nums, Pos, _Divisor, Acc) when Pos == Len ->
    Acc;
positions_contrib(N, Len, Nums, Pos, Divisor, Acc) ->
    Counts = count_digits_at_pos(Nums, Divisor, erlang:make_tuple(10, 0)),
    PosContrib = contribution_from_counts(Counts, N),
    positions_contrib(N, Len, Nums, Pos + 1, Divisor * 10, Acc + PosContrib).

count_digits_at_pos([], _Divisor, Counts) ->
    Counts;
count_digits_at_pos([Num|Rest], Divisor, Counts) ->
    Digit = (Num div Divisor) rem 10,
    Index = Digit + 1,
    Old = element(Index, Counts),
    NewCounts = setelement(Index, Counts, Old + 1),
    count_digits_at_pos(Rest, Divisor, NewCounts).

contribution_from_counts(Counts, N) ->
    contribution_from_counts(Counts, N, 0, 1).

contribution_from_counts(_Counts, _N, Acc, Index) when Index > 10 ->
    Acc;
contribution_from_counts(Counts, N, Acc, Index) ->
    C = element(Index, Counts),
    contribution_from_counts(Counts, N, Acc + C * (N - C), Index + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec sum_digit_differences(nums :: [integer]) :: integer
  def sum_digit_differences(nums) do
    n = length(nums)
    first = hd(nums)
    digit_len = Integer.digits(first) |> length()

    pow10s = for i <- 0..(digit_len - 1), do: :math.pow(10, i) |> trunc()

    Enum.reduce(pow10s, 0, fn pow10, total ->
      freq =
        Enum.reduce(nums, %{}, fn num, acc ->
          digit = div(num, pow10) |> rem(10)
          Map.update(acc, digit, 1, &(&1 + 1))
        end)

      contrib =
        Enum.reduce(0..9, 0, fn d, sum ->
          c = Map.get(freq, d, 0)
          sum + c * (n - c)
        end)

      total + div(contrib, 2)
    end)
  end
end
```
