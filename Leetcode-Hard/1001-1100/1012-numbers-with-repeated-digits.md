# 1012. Numbers With Repeated Digits

## Cpp

```cpp
class Solution {
public:
    long long perm(int m, int k) {
        long long res = 1;
        for (int i = 0; i < k; ++i) {
            res *= (m - i);
        }
        return res;
    }

    int numDupDigitsAtMostN(int n) {
        vector<int> digits;
        while (n > 0) {
            digits.push_back(n % 10);
            n /= 10;
        }
        reverse(digits.begin(), digits.end());
        int m = digits.size();

        long long uniqueCount = 0;

        // numbers with length less than m
        for (int len = 1; len < m; ++len) {
            uniqueCount += 9 * perm(9, len - 1);
        }

        // numbers with same length
        bool used[10] = {false};
        for (int i = 0; i < m; ++i) {
            int cur = digits[i];
            for (int d = (i == 0 ? 1 : 0); d < cur; ++d) {
                if (!used[d]) {
                    int remaining = m - i - 1;
                    int available = 10 - (i + 1);
                    uniqueCount += perm(available, remaining);
                }
            }
            if (used[cur]) {
                // cannot proceed further
                return (int)((long long)stoi(to_string(digits[0])) * 0 + (long long)n - uniqueCount); // placeholder not used
            }
            used[cur] = true;
        }

        // n itself has all unique digits
        uniqueCount += 1;

        int totalNumbers = stoi(string(digits.begin(), digits.end()));
        return totalNumbers - (int)uniqueCount;
    }
};
```

## Java

```java
class Solution {
    public int numDupDigitsAtMostN(int n) {
        return n + 1 - countUnique(n);
    }

    private int countUnique(int n) {
        // Extract digits of n
        int[] digits = new int[10];
        int len = 0;
        while (n > 0) {
            digits[len++] = n % 10;
            n /= 10;
        }
        if (len == 0) return 1; // only number 0

        // Reverse to get most significant first
        for (int i = 0; i < len / 2; ++i) {
            int tmp = digits[i];
            digits[i] = digits[len - 1 - i];
            digits[len - 1 - i] = tmp;
        }

        int count = 1; // include number 0

        // Numbers with fewer digits than len
        for (int k = 1; k < len; ++k) {
            count += 9 * perm(9, k - 1);
        }

        boolean[] used = new boolean[10];
        for (int i = 0; i < len; ++i) {
            int cur = digits[i];
            for (int d = (i == 0 ? 1 : 0); d < cur; ++d) {
                if (!used[d]) {
                    count += perm(10 - (i + 1), len - i - 1);
                }
            }
            if (used[cur]) {
                return count;
            }
            used[cur] = true;
        }

        // n itself has all unique digits
        count++;
        return count;
    }

    private int perm(int m, int k) {
        int res = 1;
        for (int i = 0; i < k; ++i) {
            res *= (m - i);
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def numDupDigitsAtMostN(self, n):
        """
        :type n: int
        :rtype: int
        """
        def perm(m, k):
            res = 1
            for i in range(k):
                res *= (m - i)
            return res

        s = list(map(int, str(n)))
        m = len(s)
        total_unique = 0

        # numbers with length less than m
        for k in range(1, m):
            total_unique += 9 * perm(9, k - 1)

        used = set()
        for i, d in enumerate(s):
            start = 1 if i == 0 else 0
            for x in range(start, d):
                if x not in used:
                    total_unique += perm(10 - (i + 1), m - i - 1)
            if d in used:
                break
            used.add(d)
        else:
            # n itself has all unique digits
            total_unique += 1

        return n - total_unique
```

## Python3

```python
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = list(map(int, str(n)))
        m = len(s)
        total_unique = 0

        # numbers with length less than m
        for k in range(1, m):
            cnt = 9
            avail = 9
            for _ in range(1, k):
                cnt *= avail
                avail -= 1
            total_unique += cnt

        used = set()
        for i, cur in enumerate(s):
            start = 1 if i == 0 else 0
            for d in range(start, cur):
                if d in used:
                    continue
                remaining = m - i - 1
                avail = 10 - (i + 1)  # digits left after choosing d
                cnt = 1
                for _ in range(remaining):
                    cnt *= avail
                    avail -= 1
                total_unique += cnt
            if cur in used:
                break
            used.add(cur)
        else:
            # n itself has all unique digits
            total_unique += 1

        return n - total_unique
```

## C

```c
int numDupDigitsAtMostN(int n) {
    if (n <= 0) return 0;
    
    // helper: count positive integers in [1, n] with all unique digits
    auto countUnique = [](int x) -> long long {
        if (x == 0) return 0;
        int tmp = x;
        int digits[10];
        int m = 0;
        while (tmp > 0) {
            digits[m++] = tmp % 10;
            tmp /= 10;
        }
        // reverse to get most significant first
        for (int i = 0; i < m / 2; ++i) {
            int t = digits[i];
            digits[i] = digits[m - 1 - i];
            digits[m - 1 - i] = t;
        }
        
        long long total = 0;
        // numbers with length less than m
        for (int len = 1; len < m; ++len) {
            long long cnt = 9;               // first digit cannot be zero
            int avail = 9;                    // remaining digits to choose from
            for (int i = 1; i < len; ++i) {
                cnt *= avail;
                --avail;
            }
            total += cnt;
        }
        
        bool used[10] = {0};
        for (int i = 0; i < m; ++i) {
            int cur = digits[i];
            int start = (i == 0) ? 1 : 0;
            for (int d = start; d < cur; ++d) {
                if (used[d]) continue;
                long long cnt = 1;
                int avail = 10 - (i + 1); // digits left after fixing this one
                for (int j = i + 1; j < m; ++j) {
                    cnt *= avail;
                    --avail;
                }
                total += cnt;
            }
            if (used[cur]) {
                return total; // repeated digit encountered, stop
            }
            used[cur] = true;
        }
        // x itself has all unique digits
        total += 1;
        return total;
    };
    
    long long uniquePos = countUnique(n);
    return n - (int)uniquePos;
}
```

## Csharp

```csharp
public class Solution {
    public int NumDupDigitsAtMostN(int n) {
        // Extract digits of n
        var digits = new List<int>();
        int temp = n;
        while (temp > 0) {
            digits.Add(temp % 10);
            temp /= 10;
        }
        digits.Reverse();
        int m = digits.Count;

        int countUnique = 0;

        // Count numbers with length less than m
        for (int k = 1; k < m; k++) {
            int cnt = 9;               // first digit cannot be zero
            int available = 9;         // remaining digits (including zero)
            for (int i = 1; i < k; i++) {
                cnt *= available;
                available--;
            }
            countUnique += cnt;
        }

        bool[] used = new bool[10];
        for (int i = 0; i < m; i++) {
            int cur = digits[i];
            // Try placing a smaller digit at position i
            for (int d = (i == 0 ? 1 : 0); d < cur; d++) {
                if (used[d]) continue;
                int available = 10 - (i + 1);
                int remain = m - i - 1;
                int perm = 1;
                for (int j = 0; j < remain; j++) {
                    perm *= (available - j);
                }
                countUnique += perm;
            }

            // If current digit already used, further numbers will have repeats
            if (used[cur]) {
                return n - countUnique;
            }
            used[cur] = true;
        }

        // n itself has all unique digits
        countUnique++;

        return n - countUnique;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var numDupDigitsAtMostN = function(n) {
    // count numbers with all unique digits in [1, n]
    const countUnique = (num) => {
        const digits = String(num).split('').map(ch => ch.charCodeAt(0) - 48);
        const len = digits.length;
        let cnt = 0;

        // numbers with length less than len
        for (let l = 1; l < len; ++l) {
            let perm = 9;          // first digit cannot be zero
            let available = 9;     // remaining digits after picking the first one
            for (let i = 1; i < l; ++i) {
                perm *= available;
                --available;
            }
            cnt += perm;
        }

        const used = new Set();
        for (let i = 0; i < len; ++i) {
            const cur = digits[i];
            const start = i === 0 ? 1 : 0;
            for (let d = start; d < cur; ++d) {
                if (!used.has(d)) {
                    let remaining = 10 - (i + 1);          // digits left after choosing d
                    let positions = len - i - 1;           // slots to fill
                    let perm = 1;
                    for (let k = 0; k < positions; ++k) {
                        perm *= (remaining - k);
                    }
                    cnt += perm;
                }
            }
            if (used.has(cur)) {
                return cnt; // repeated digit encountered, stop
            }
            used.add(cur);
        }

        // n itself has all unique digits
        cnt += 1;
        return cnt;
    };

    const unique = countUnique(n);
    return n - unique;
};
```

## Typescript

```typescript
function numDupDigitsAtMostN(n: number): number {
    const digits = String(n).split('').map(ch => Number(ch));
    const len = digits.length;
    let uniqueCount = 0;

    // Count numbers with length less than len
    for (let l = 1; l < len; ++l) {
        let cnt = 9;
        let available = 9;
        for (let i = 2; i <= l; ++i) {
            cnt *= available;
            available--;
        }
        uniqueCount += cnt;
    }

    const used = new Set<number>();
    for (let i = 0; i < len; ++i) {
        const cur = digits[i];
        const start = i === 0 ? 1 : 0;

        // Try placing a smaller digit at position i
        for (let d = start; d < cur; ++d) {
            if (!used.has(d)) {
                let cnt = 1;
                let avail = 10 - (used.size + 1); // digits left after choosing d
                for (let k = 0; k < len - i - 1; ++k) {
                    cnt *= avail;
                    avail--;
                }
                uniqueCount += cnt;
            }
        }

        if (used.has(cur)) {
            return n - uniqueCount;
        }
        used.add(cur);
    }

    // n itself has all unique digits
    uniqueCount += 1;
    return n - uniqueCount;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function numDupDigitsAtMostN($n) {
        $digits = str_split((string)$n);
        $len = count($digits);
        $uniqueCount = 0;

        // Count numbers with length less than len that have all unique digits
        for ($i = 1; $i < $len; $i++) {
            $uniqueCount += 9 * $this->perm(9, $i - 1);
        }

        // Count numbers with the same length as n and unique digits
        $used = [];
        $isUnique = true;
        for ($i = 0; $i < $len; $i++) {
            $cur = intval($digits[$i]);
            $start = ($i == 0) ? 1 : 0;
            for ($d = $start; $d < $cur; $d++) {
                if (in_array($d, $used)) continue;
                $remaining = $len - $i - 1;
                $uniqueCount += $this->perm(10 - ($i + 1), $remaining);
            }
            if (in_array($cur, $used)) {
                $isUnique = false;
                break;
            }
            $used[] = $cur;
        }

        if ($isUnique) {
            // n itself has all unique digits
            $uniqueCount += 1;
        }

        return $n - $uniqueCount;
    }

    private function perm($m, $k) {
        $res = 1;
        for ($i = 0; $i < $k; $i++) {
            $res *= ($m - $i);
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func numDupDigitsAtMostN(_ n: Int) -> Int {
        var digits = [Int]()
        for ch in String(n) {
            digits.append(Int(String(ch))!)
        }
        let len = digits.count
        var totalUnique = 1   // count zero
        
        if len > 1 {
            for k in 1..<len {
                var count = 9
                var available = 9
                if k > 1 {
                    for _ in 1..<k {
                        count *= available
                        available -= 1
                    }
                }
                totalUnique += count
            }
        }
        
        var used = [Bool](repeating: false, count: 10)
        for i in 0..<len {
            let cur = digits[i]
            let start = (i == 0) ? 1 : 0
            if start < cur {
                for d in start..<cur {
                    if !used[d] {
                        var avail = 10 - (i + 1)
                        var perm = 1
                        for _ in 0..<(len - i - 1) {
                            perm *= avail
                            avail -= 1
                        }
                        totalUnique += perm
                    }
                }
            }
            
            if used[cur] {
                break
            }
            used[cur] = true
            
            if i == len - 1 {
                totalUnique += 1   // n itself has unique digits
            }
        }
        
        return n - totalUnique + 1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numDupDigitsAtMostN(n: Int): Int {
        val unique = countUnique(n)
        return n - unique + 1
    }

    private fun countUnique(n: Int): Int {
        if (n < 10) return n + 1 // includes zero
        val digits = mutableListOf<Int>()
        var temp = n
        while (temp > 0) {
            digits.add(temp % 10)
            temp /= 10
        }
        digits.reverse()
        val m = digits.size
        var count = 1 // for zero

        // numbers with length less than m
        for (len in 1 until m) {
            count += 9 * permute(9, len - 1)
        }

        val used = BooleanArray(10)
        for (i in 0 until m) {
            val cur = digits[i]
            val start = if (i == 0) 1 else 0
            for (d in start until cur) {
                if (!used[d]) {
                    count += permute(10 - (i + 1), m - i - 1)
                }
            }
            if (used[cur]) {
                return count
            }
            used[cur] = true
        }
        // n itself has all unique digits
        count += 1
        return count
    }

    private fun permute(m: Int, k: Int): Int {
        var res = 1
        for (i in 0 until k) {
            res *= (m - i)
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  int numDupDigitsAtMostN(int n) {
    int unique = _countUnique(n);
    return n - unique + 1;
  }

  int _permute(int m, int k) {
    int res = 1;
    for (int i = 0; i < k; ++i) {
      res *= (m - i);
    }
    return res;
  }

  int _countUnique(int n) {
    List<int> digits = n.toString().split('').map((c) => int.parse(c)).toList();
    int L = digits.length;
    int total = 1; // count zero

    for (int k = 1; k < L; ++k) {
      total += 9 * _permute(9, k - 1);
    }

    Set<int> used = {};
    for (int i = 0; i < L; ++i) {
      int d = digits[i];
      for (int x = (i == 0 ? 1 : 0); x < d; ++x) {
        if (!used.contains(x)) {
          total += _permute(9 - i, L - i - 1);
        }
      }
      if (used.contains(d)) {
        return total;
      }
      used.add(d);
    }

    // n itself has unique digits
    total += 1;
    return total;
  }
}
```

## Golang

```go
import "strconv"

func perm(m, k int) int {
    res := 1
    for i := 0; i < k; i++ {
        res *= m - i
    }
    return res
}

func numDupDigitsAtMostN(n int) int {
    s := strconv.Itoa(n)
    m := len(s)

    // count numbers with unique digits and length less than m
    total := 0
    for k := 1; k < m; k++ {
        cnt := 9
        available := 9
        for i := 1; i < k; i++ {
            cnt *= available
            available--
        }
        total += cnt
    }

    used := make([]bool, 10)
    for i := 0; i < m; i++ {
        digit := int(s[i] - '0')
        start := 0
        if i == 0 {
            start = 1
        }
        for d := start; d < digit; d++ {
            if !used[d] {
                remaining := 10 - (i + 1)
                total += perm(remaining, m-i-1)
            }
        }
        if used[digit] {
            return n - total
        }
        used[digit] = true
    }

    // n itself has all unique digits
    total++
    return n - total
}
```

## Ruby

```ruby
def perm(m, k)
  return 0 if k < 0 || k > m
  res = 1
  i = 0
  while i < k
    res *= (m - i)
    i += 1
  end
  res
end

def count_unique_up_to(n)
  s = n.to_s
  len = s.length
  total = 0

  # numbers with length less than len
  (1...len).each do |k|
    total += 9 * perm(9, k - 1)
  end

  used = Array.new(10, false)

  (0...len).each do |i|
    cur = s[i].ord - 48
    start_digit = i.zero? ? 1 : 0

    (start_digit...cur).each do |d|
      next if used[d]
      remaining = len - i - 1
      available = 10 - (i + 1) # after picking this digit, total used will be i+1
      total += perm(available, remaining)
    end

    return total unless !used[cur]   # duplicate found, stop
    used[cur] = true
  end

  total + 1  # n itself has all unique digits
end

# @param {Integer} n
# @return {Integer}
def num_dup_digits_at_most_n(n)
  uniq = count_unique_up_to(n)
  n - uniq
end
```

## Scala

```scala
object Solution {
    def numDupDigitsAtMostN(n: Int): Int = {
        val digits = n.toString.map(_.asDigit).toArray
        val L = digits.length
        var count: Long = 0L

        // Count numbers with unique digits and length less than L
        var k = 1
        while (k < L) {
            var perm: Long = 9L          // first digit cannot be zero
            var available = 9            // remaining digits (including zero)
            var i = 1
            while (i < k) {
                perm *= available
                available -= 1
                i += 1
            }
            count += perm
            k += 1
        }

        // Count numbers with the same length L and unique digits
        val used = new Array[Boolean](10)
        var i = 0
        var broken = false
        while (i < L && !broken) {
            val cur = digits(i)
            var d = if (i == 0) 1 else 0
            while (d < cur) {
                if (!used(d)) {
                    // permutations for the remaining positions
                    var perm: Long = 1L
                    var available = 10 - (i + 1)
                    var j = i + 1
                    while (j < L) {
                        perm *= available
                        available -= 1
                        j += 1
                    }
                    count += perm
                }
                d += 1
            }
            if (used(cur)) {
                broken = true
            } else {
                used(cur) = true
            }
            i += 1
        }

        // If n itself has all unique digits, include it
        if (!broken) count += 1

        val result = n.toLong - count
        result.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_dup_digits_at_most_n(n: i32) -> i32 {
        let unique = Self::count_unique(n as i64);
        (n as i64 - unique) as i32
    }

    fn count_unique(n: i64) -> i64 {
        if n == 0 {
            return 1;
        }
        // extract digits
        let mut digits = Vec::new();
        let mut x = n;
        while x > 0 {
            digits.push((x % 10) as i32);
            x /= 10;
        }
        digits.reverse();
        let len = digits.len();

        // numbers with fewer digits
        let mut cnt: i64 = 0;
        for k in 1..len {
            let mut cur = 9i64;          // first digit (cannot be zero)
            let mut avail = 9i64;        // remaining available digits including zero
            for _ in 0..(k - 1) {
                cur *= avail;
                avail -= 1;
            }
            cnt += cur;
        }

        // numbers with the same length
        let mut used = [false; 10];
        for i in 0..len {
            let cur_digit = digits[i] as usize;
            let start = if i == 0 { 1 } else { 0 };
            for d in start..cur_digit {
                if !used[d] {
                    let remaining = 10 - (i + 1);
                    let slots = len - i - 1;
                    cnt += Self::perm(remaining as i64, slots);
                }
            }
            if used[cur_digit] {
                return cnt; // duplicate encountered
            }
            used[cur_digit] = true;
        }
        // n itself has all unique digits
        cnt + 1
    }

    fn perm(m: i64, k: usize) -> i64 {
        let mut res = 1i64;
        for i in 0..k {
            res *= m - i as i64;
        }
        res
    }
}
```

## Racket

```racket
(define/contract (num-dup-digits-at-most-n n)
  (-> exact-integer? exact-integer?)
  (let* ((digits
          (map (lambda (c) (- (char->integer c) (char->integer #\0)))
               (string->list (number->string n))))
         (len (length digits))
         ;; permutation mPk
         (perm
          (lambda (m k)
            (let loop ((i 0) (res 1))
              (if (= i k)
                  res
                  (loop (+ i 1) (* res (- m i)))))))
         ;; count numbers with fewer digits than n having all distinct digits
         (cnt-less
          (let loop ((k 1) (sum 0))
            (if (> k (- len 1))
                sum
                (loop (+ k 1)
                      (+ sum (* 9 (perm 9 (- k 1))))))))
         ;; count numbers with the same length as n having all distinct digits and <= n
         (used '())
         (cnt-same 0)
         (break #f))
    (for ([i (in-range len)])
      (when (not break)
        (define cur (list-ref digits i))
        (define start (if (= i 0) 1 0))
        (for ([d (in-range start cur)])
          (unless (member d used)
            (define remaining (- len i 1))
            (define available (- 10 (length used) 1))
            (set! cnt-same (+ cnt-same (perm available remaining)))))
        (if (member cur used)
            (set! break #t)
            (set! used (cons cur used)))))
    (when (not break)
      (set! cnt-same (+ cnt-same 1))) ; n itself has all distinct digits
    (- n (+ cnt-less cnt-same))))
```

## Erlang

```erlang
-module(solution).
-export([num_dup_digits_at_most_n/1]).

-spec num_dup_digits_at_most_n(N :: integer()) -> integer().
num_dup_digits_at_most_n(N) ->
    Unique = count_unique(N),
    N + 1 - Unique.

%% Count numbers in [0, N] with all distinct digits
count_unique(N) ->
    Digits = [C - $0 || C <- integer_to_list(N)],
    Len = length(Digits),
    CountLess = count_len_less(Len),
    CountSame = same_len(Digits, [], 0),
    1 + CountLess + CountSame.   % include zero

%% Numbers with length less than L that have unique digits (positive numbers)
count_len_less(L) when L =< 1 -> 0;
count_len_less(L) ->
    count_len_less(1, L - 1, 0).

count_len_less(K, Max, Acc) when K > Max -> Acc;
count_len_less(K, Max, Acc) ->
    Add = 9 * perm(9, K - 1),
    count_len_less(K + 1, Max, Acc + Add).

%% Numbers with the same length as N and <= N having unique digits
same_len(Digits, Used, Pos) ->
    Len = length(Digits),
    if Pos == Len ->
            1;   % N itself has all distinct digits
       true ->
            Cur = lists:nth(Pos + 1, Digits),
            Start = case Pos of
                        0 -> 1;
                        _ -> 0
                    end,
            SmallerDigits = [D || D <- lists:seq(Start, Cur - 1), not lists:member(D, Used)],
            CountForPos = lists:foldl(
                fun(_Digit, Acc) ->
                    Remaining = Len - Pos - 1,
                    Available = 10 - (Pos + 1),
                    Acc + perm(Available, Remaining)
                end, 0, SmallerDigits),
            case lists:member(Cur, Used) of
                true -> CountForPos;
                false ->
                    NewUsed = [Cur | Used],
                    CountForPos + same_len(Digits, NewUsed, Pos + 1)
            end
    end.

%% Permutation P(m, r) = m * (m-1) * ... * (m-r+1)
perm(_, 0) -> 1;
perm(M, R) when R > 0 ->
    M * perm(M - 1, R - 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_dup_digits_at_most_n(n :: integer) :: integer
  def num_dup_digits_at_most_n(n) do
    unique = count_unique_including_zero(n)
    n - unique + 1
  end

  # counts numbers in [0, n] with all distinct digits (including 0)
  defp count_unique_including_zero(n) do
    digits = Integer.digits(n)
    len = length(digits)

    less =
      Enum.reduce(1..len - 1, 0, fn k, acc ->
        acc + 9 * perm(9, k - 1)
      end)

    {same, used, stopped} =
      Enum.reduce_while(Enum.with_index(digits), {0, MapSet.new(), false}, fn {cur, i},
                                                                             {acc, used, _stopped} ->
        start = if i == 0, do: 1, else: 0

        acc2 =
          Enum.reduce(start..(cur - 1), acc, fn d, a ->
            if MapSet.member?(used, d) do
              a
            else
              remaining = len - i - 1
              available = 10 - (MapSet.size(used) + 1)
              a + perm(available, remaining)
            end
          end)

        if MapSet.member?(used, cur) do
          {:halt, {acc2, used, true}}
        else
          {:cont, {acc2, MapSet.put(used, cur), false}}
        end
      end)

    pos_unique = less + same
    pos_unique = if stopped, do: pos_unique, else: pos_unique + 1
    pos_unique + 1
  end

  defp perm(_m, 0), do: 1

  defp perm(m, k) when k > 0 do
    Enum.reduce(0..k - 1, 1, fn i, acc -> acc * (m - i) end)
  end
end
```
