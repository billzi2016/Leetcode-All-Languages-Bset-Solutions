# 2048. Next Greater Numerically Balanced Number

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int nextBeautifulNumber(int n) {
        static vector<int> beautiful = []() {
            vector<int> res;
            for (int mask = 1; mask < (1 << 9); ++mask) {
                int totalLen = 0;
                string s;
                for (int d = 1; d <= 9; ++d) {
                    if (mask & (1 << (d - 1))) {
                        totalLen += d;
                        s.append(d, char('0' + d));
                    }
                }
                if (totalLen > 9) continue; // keep numbers within int range
                sort(s.begin(), s.end());
                do {
                    long long val = 0;
                    for (char c : s) {
                        val = val * 10 + (c - '0');
                    }
                    res.push_back((int)val);
                } while (next_permutation(s.begin(), s.end()));
            }
            sort(res.begin(), res.end());
            res.erase(unique(res.begin(), res.end()), res.end());
            return res;
        }();
        
        auto it = upper_bound(beautiful.begin(), beautiful.end(), n);
        return *it;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int nextBeautifulNumber(int n) {
        TreeSet<Integer> set = new TreeSet<>();
        int[] cnt = new int[10];
        dfs(cnt, 0L, set);
        Integer ans = set.higher(n);
        return ans == null ? -1 : ans;
    }

    private void dfs(int[] cnt, long val, TreeSet<Integer> set) {
        if (val > 0 && val <= Integer.MAX_VALUE) {
            boolean ok = true;
            for (int d = 1; d <= 9; d++) {
                if (cnt[d] != 0 && cnt[d] != d) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                set.add((int) val);
            }
        }
        if (val > Integer.MAX_VALUE) return;

        for (int d = 1; d <= 9; d++) {
            if (cnt[d] < d) {
                cnt[d]++;
                dfs(cnt, val * 10 + d, set);
                cnt[d]--;
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_beautiful(x):
            cnt = [0] * 10
            while x:
                d = x % 10
                cnt[d] += 1
                if cnt[d] > d:  # early exit, impossible to satisfy
                    return False
                x //= 10
            for d in range(1, 10):
                if cnt[d] != 0 and cnt[d] != d:
                    return False
            return True

        cur = n + 1
        while not is_beautiful(cur):
            cur += 1
        return cur
```

## Python3

```python
import itertools
import bisect

class Solution:
    def __init__(self):
        # Precompute all numerically balanced numbers (beautiful numbers)
        nums = []
        digits = [str(d) for d in range(1, 10)]
        for k in range(1, 10):
            for perm in itertools.permutations(digits, k):
                num_str = ''.join(d * int(d) for d in perm)
                nums.append(int(num_str))
        self.beautiful = sorted(nums)

    def nextBeautifulNumber(self, n: int) -> int:
        idx = bisect.bisect_right(self.beautiful, n)
        return self.beautiful[idx]
```

## C

```c
int nextBeautifulNumber(int n) {
    static std::vector<int> beautiful;
    if (beautiful.empty()) {
        for (int mask = 1; mask < (1 << 9); ++mask) {
            std::string s;
            int total_len = 0;
            for (int d = 1; d <= 9; ++d) {
                if (mask & (1 << (d - 1))) {
                    s.append(d, char('0' + d));
                    total_len += d;
                }
            }
            if ((int)s.size() > 9) continue; // keep within int range
            std::sort(s.begin(), s.end());
            do {
                int val = std::stoi(s);
                beautiful.push_back(val);
            } while (std::next_permutation(s.begin(), s.end()));
        }
        std::sort(beautiful.begin(), beautiful.end());
        beautiful.erase(std::unique(beautiful.begin(), beautiful.end()), beautiful.end());
    }
    auto it = std::upper_bound(beautiful.begin(), beautiful.end(), n);
    return *it;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

public class Solution {
    public int NextBeautifulNumber(int n) {
        var candidates = new List<int>();
        // generate all subsets of digits 1..9
        for (int mask = 1; mask < (1 << 9); ++mask) {
            var sb = new StringBuilder();
            for (int d = 1; d <= 9; ++d) {
                if ((mask >> (d - 1) & 1) == 1) {
                    sb.Append(new string((char)('0' + d), d));
                }
            }
            char[] arr = sb.ToString().ToCharArray(); // already sorted
            do {
                long val = 0;
                foreach (char c in arr) {
                    val = val * 10 + (c - '0');
                    if (val > int.MaxValue) break;
                }
                if (val <= int.MaxValue) candidates.Add((int)val);
            } while (NextPermutation(arr));
        }

        var sorted = candidates.Distinct().OrderBy(x => x).ToList();
        foreach (var v in sorted) {
            if (v > n) return v;
        }
        // Should never reach here for given constraints
        return -1;
    }

    private bool NextPermutation(char[] a) {
        int i = a.Length - 2;
        while (i >= 0 && a[i] >= a[i + 1]) i--;
        if (i < 0) return false;
        int j = a.Length - 1;
        while (a[j] <= a[i]) j--;
        char tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
        Array.Reverse(a, i + 1, a.Length - (i + 1));
        return true;
    }
}
```

## Javascript

```javascript
var _beautifulNumbers;
function _initBeautiful() {
    if (_beautifulNumbers) return;
    const LIMIT = 7; // maximum length needed for n <= 1e6
    const set = new Set();
    for (let mask = 1; mask < (1 << 9); mask++) {
        let total = 0;
        const cnt = Array(10).fill(0);
        for (let d = 1; d <= 9; d++) {
            if (mask & (1 << (d - 1))) {
                cnt[d] = d;
                total += d;
            }
        }
        if (total > LIMIT) continue;
        function backtrack(cur) {
            if (cur.length === total) {
                set.add(Number(cur));
                return;
            }
            for (let d = 1; d <= 9; d++) {
                if (cnt[d] > 0) {
                    cnt[d]--;
                    backtrack(cur + d);
                    cnt[d]++;
                }
            }
        }
        backtrack("");
    }
    _beautifulNumbers = Array.from(set);
    _beautifulNumbers.sort((a, b) => a - b);
}

/**
 * @param {number} n
 * @return {number}
 */
var nextBeautifulNumber = function (n) {
    _initBeautiful();
    for (const num of _beautifulNumbers) {
        if (num > n) return num;
    }
    // Should never reach here for given constraints
    return -1;
};
```

## Typescript

```typescript
function nextBeautifulNumber(n: number): number {
    const isBeautiful = (num: number): boolean => {
        const cnt = new Array(10).fill(0);
        let x = num;
        while (x > 0) {
            const d = x % 10;
            cnt[d]++;
            if (cnt[d] > d) return false; // early exit
            x = Math.floor(x / 10);
        }
        for (let d = 1; d <= 9; d++) {
            if (cnt[d] !== 0 && cnt[d] !== d) return false;
        }
        // digit 0 must not appear
        if (cnt[0] !== 0) return false;
        return true;
    };

    let cur = n + 1;
    while (true) {
        if (isBeautiful(cur)) return cur;
        cur++;
    }
}
```

## Php

```php
class Solution {
    private $beautiful = [];

    public function nextBeautifulNumber($n) {
        if (empty($this->beautiful)) {
            $this->precompute();
            sort($this->beautiful);
        }
        foreach ($this->beautiful as $num) {
            if ($num > $n) {
                return $num;
            }
        }
        return -1; // should never reach for given constraints
    }

    private function precompute() {
        $this->dfs(1, []);
    }

    private function dfs($startDigit, $digits) {
        if (!empty($digits)) {
            $this->addPermutations($digits);
        }
        for ($d = $startDigit; $d <= 9; $d++) {
            // limit length to keep generation reasonable (n ≤ 10^6)
            if (count($digits) + $d > 10) continue;
            $newDigits = array_merge($digits, array_fill(0, $d, $d));
            $this->dfs($d + 1, $newDigits);
        }
    }

    private function addPermutations($digits) {
        sort($digits);
        $len = count($digits);
        $used = array_fill(0, $len, false);
        $path = [];

        $self = $this;
        $permute = function() use (&$permute, &$digits, &$used, &$path, $len, $self) {
            if (count($path) === $len) {
                $num = 0;
                foreach ($path as $d) {
                    $num = $num * 10 + $d;
                }
                $self->beautiful[] = $num;
                return;
            }
            for ($i = 0; $i < $len; $i++) {
                if ($used[$i]) continue;
                if ($i > 0 && $digits[$i] === $digits[$i - 1] && !$used[$i - 1]) continue;
                $used[$i] = true;
                $path[] = $digits[$i];
                $permute();
                array_pop($path);
                $used[$i] = false;
            }
        };
        $permute();
    }
}
```

## Swift

```swift
class Solution {
    func nextBeautifulNumber(_ n: Int) -> Int {
        var candidates = [Int]()
        // Enumerate all subsets of digits 1..9
        for mask in 1..<(1 << 9) {
            var chars = [Character]()
            for d in 1...9 {
                if (mask >> (d - 1)) & 1 == 1 {
                    let ch: Character = Character("\(d)")
                    for _ in 0..<d { chars.append(ch) }
                }
            }
            if chars.isEmpty { continue }
            chars.sort()
            var used = Array(repeating: false, count: chars.count)
            var path = [Character]()
            func backtrack() {
                if path.count == chars.count {
                    let numStr = String(path)
                    if let val = Int(numStr) {
                        candidates.append(val)
                    }
                    return
                }
                for i in 0..<chars.count {
                    if used[i] { continue }
                    if i > 0 && chars[i] == chars[i - 1] && !used[i - 1] { continue }
                    used[i] = true
                    path.append(chars[i])
                    backtrack()
                    path.removeLast()
                    used[i] = false
                }
            }
            backtrack()
        }
        candidates.sort()
        for v in candidates where v > n {
            return v
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun nextBeautifulNumber(n: Int): Int {
        val candidates = mutableSetOf<Int>()
        // iterate over all subsets of digits 1..9
        for (mask in 1 until (1 shl 9)) {
            val cnt = IntArray(10)
            var totalLen = 0
            for (d in 1..9) {
                if ((mask shr (d - 1)) and 1 == 1) {
                    cnt[d] = d
                    totalLen += d
                }
            }
            // numbers longer than 10 digits cannot fit into Int
            if (totalLen > 10) continue
            val sb = StringBuilder()
            fun backtrack() {
                if (sb.length == totalLen) {
                    val value = sb.toString().toLong()
                    if (value <= Int.MAX_VALUE) candidates.add(value.toInt())
                    return
                }
                for (d in 1..9) {
                    if (cnt[d] > 0) {
                        cnt[d]--
                        sb.append(d)
                        backtrack()
                        sb.setLength(sb.length - 1)
                        cnt[d]++
                    }
                }
            }
            backtrack()
        }
        val list = candidates.toMutableList()
        list.sort()
        for (v in list) {
            if (v > n) return v
        }
        return -1 // should never happen with given constraints
    }
}
```

## Dart

```dart
class Solution {
  int nextBeautifulNumber(int n) {
    List<int> beautiful = [];
    List<int> cnt = List.filled(10, 0);

    void dfs(String cur) {
      if (cur.isNotEmpty) {
        beautiful.add(int.parse(cur));
      }
      if (cur.length >= 10) return; // enough for given constraints
      for (int d = 1; d <= 9; ++d) {
        if (cnt[d] < d) {
          cnt[d]++;
          dfs(cur + d.toString());
          cnt[d]--;
        }
      }
    }

    dfs('');
    beautiful.sort();
    for (int val in beautiful) {
      if (val > n) return val;
    }
    return -1; // should never reach here with given constraints
  }
}
```

## Golang

```go
func nextBeautifulNumber(n int) int {
	for x := n + 1; ; x++ {
		cnt := [10]int{}
		t := x
		if t == 0 { // handle zero case, though never reached because x>n>=0
			continue
		}
		for t > 0 {
			d := t % 10
			cnt[d]++
			t /= 10
		}
		ok := true
		for d := 0; d <= 9; d++ {
			if cnt[d] == 0 {
				continue
			}
			if cnt[d] != d {
				ok = false
				break
			}
		}
		if ok {
			return x
		}
	}
}
```

## Ruby

```ruby
require 'set'

def next_beautiful_number(n)
  max_len = 9
  best = (1 << 62)

  (1...(1 << 9)).each do |mask|
    digits = []
    total_len = 0

    (1..9).each do |d|
      if mask & (1 << (d - 1)) != 0
        d.times { digits << d }
        total_len += d
      end
    end

    next if total_len == 0 || total_len > max_len

    seen = Set.new
    digits.permutation.each do |perm|
      val = 0
      perm.each { |dig| val = val * 10 + dig }
      next if seen.include?(val)
      seen.add(val)

      if val > n && val < best
        best = val
      end
    end
  end

  best
end
```

## Scala

```scala
object Solution {
    def nextBeautifulNumber(n: Int): Int = {
        val beautiful = scala.collection.mutable.ArrayBuffer[Int]()
        val maxLen = 10
        val cnt = new Array[Int](10)

        def genPerm(len: Int, pos: Int, cur: Long): Unit = {
            if (pos == len) {
                if (cur <= Int.MaxValue) beautiful += cur.toInt
                return
            }
            for (d <- 1 to 9) {
                if (cnt(d) > 0) {
                    cnt(d) -= 1
                    genPerm(len, pos + 1, cur * 10 + d)
                    cnt(d) += 1
                }
            }
        }

        def backtrackDigit(d: Int, curLen: Int): Unit = {
            if (d == 10) {
                if (curLen > 0) genPerm(curLen, 0, 0L)
                return
            }
            // skip digit d
            backtrackDigit(d + 1, curLen)

            // include digit d
            val newLen = curLen + d
            if (newLen <= maxLen) {
                cnt(d) = d
                backtrackDigit(d + 1, newLen)
                cnt(d) = 0
            }
        }

        backtrackDigit(1, 0)

        val sorted = beautiful.distinct.sorted
        for (v <- sorted) if (v > n) return v
        -1 // should never reach per problem guarantees
    }
}
```

## Rust

```rust
impl Solution {
    pub fn next_beautiful_number(n: i32) -> i32 {
        fn dfs(counts: &mut [u8; 10], remaining: usize, cur: i64, res: &mut Vec<i64>) {
            if remaining == 0 {
                res.push(cur);
                return;
            }
            for d in 1..=9 {
                let idx = d as usize;
                if counts[idx] > 0 {
                    counts[idx] -= 1;
                    dfs(counts, remaining - 1, cur * 10 + d as i64, res);
                    counts[idx] += 1;
                }
            }
        }

        let mut candidates: Vec<i64> = Vec::new();

        // generate all numerically balanced numbers with total length up to 12
        for mask in 1..(1 << 9) {
            let mut total_len = 0usize;
            for d in 1..=9 {
                if (mask >> (d - 1)) & 1 == 1 {
                    total_len += d as usize;
                }
            }
            if total_len > 12 {
                continue;
            }
            let mut counts = [0u8; 10];
            for d in 1..=9 {
                if (mask >> (d - 1)) & 1 == 1 {
                    counts[d as usize] = d as u8;
                }
            }
            dfs(&mut counts, total_len, 0, &mut candidates);
        }

        candidates.sort_unstable();

        let target = n as i64;
        for val in candidates {
            if val > target {
                return val as i32;
            }
        }
        // Should never reach here with given constraints
        0
    }
}
```

## Racket

```racket
(define/contract (next-beautiful-number n)
  (-> exact-integer? exact-integer?)
  (let* ((candidates
          (let ((res '()))
            (for ([mask (in-range 1 (expt 2 9))]) ; iterate non‑empty subsets of {1..9}
              (define total 0)
              (define counts (make-vector 10 0))
              (for ([d (in-range 1 10)])
                (when (> (bitwise-and mask (arithmetic-shift 1 (- d 1))) 0)
                  (vector-set! counts d d)
                  (set! total (+ total d))))
              (when (<= total 9) ; only need numbers up to length 9 for given constraints
                (define (dfs len cur)
                  (if (= len total)
                      (set! res (cons cur res))
                      (for ([d (in-range 1 10)])
                        (when (> (vector-ref counts d) 0)
                          (vector-set! counts d (- (vector-ref counts d) 1))
                          (dfs (+ len 1) (+ (* cur 10) d))
                          (vector-set! counts d (+ (vector-ref counts d) 1))))))
                (dfs 0 0)))
            res))
         (sorted (sort candidates <)))
    (let loop ((lst sorted))
      (cond [(null? lst) -1]
            [(> (car lst) n) (car lst)]
            [else (loop (cdr lst))]))))
```

## Erlang

```erlang
-module(solution).
-export([next_beautiful_number/1]).

-spec next_beautiful_number(N :: integer()) -> integer().
next_beautiful_number(N) ->
    Candidates = generate_candidates(),
    find_next(Candidates, N).

generate_candidates() ->
    lists:sort(
        [build_number(Mask) || Mask <- lists:seq(1, 511)]
    ).

build_number(Mask) ->
    Digits = collect_digits(Mask, 1, []),
    list_to_integer(Digits).

collect_digits(_Mask, 10, Acc) -> lists:reverse(Acc);
collect_digits(Mask, D, Acc) ->
    case (Mask band (1 bsl (D-1))) of
        0 ->
            collect_digits(Mask, D + 1, Acc);
        _ ->
            NewAcc = repeat_digit(D, D, Acc),
            collect_digits(Mask, D + 1, NewAcc)
    end.

repeat_digit(_Digit, 0, Acc) -> Acc;
repeat_digit(Digit, Count, Acc) ->
    repeat_digit(Digit, Count - 1, [Digit | Acc]).

list_to_integer(Digits) ->
    lists:foldl(fun(Dig, Acc) -> Acc * 10 + Dig end, 0, Digits).

find_next([H|T], N) when H > N -> H;
find_next([_|T], N) -> find_next(T, N);
find_next([], _N) -> erlang:error(no_candidate).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec next_beautiful_number(n :: integer) :: integer
  def next_beautiful_number(n) do
    numbers = generate_balanced_numbers()
    Enum.find(numbers, fn x -> x > n end)
  end

  # Generate all numerically balanced numbers with total length <= 9
  defp generate_balanced_numbers do
    max_len = 9
    digits = Enum.to_list(1..9)

    1..((1 <<< 9) - 1)
    |> Enum.flat_map(fn mask ->
      {counts, len} = build_subset(mask, digits)

      if len <= max_len do
        permute_multiset(counts)
      else
        []
      end
    end)
    |> Enum.uniq()
    |> Enum.sort()
  end

  # Build a map %{digit => count} for the subset represented by mask
  defp build_subset(mask, digits) do
    Enum.reduce(Enum.with_index(digits), {%{}, 0}, fn {d, idx}, {map, sum} ->
      if (mask &&& (1 <<< idx)) != 0 do
        {Map.put(map, d, d), sum + d}
      else
        {map, sum}
      end
    end)
  end

  # Generate all permutations of the multiset represented by counts map
  defp permute_multiset(counts) do
    total = Enum.reduce(counts, 0, fn {_d, c}, acc -> acc + c end)
    dfs(0, total, counts)
  end

  defp dfs(_num, 0, _counts), do: [_num]

  defp dfs(num, remaining, counts) do
    counts
    |> Map.keys()
    |> Enum.flat_map(fn d ->
      c = Map.get(counts, d)

      if c > 0 do
        new_counts = Map.put(counts, d, c - 1)
        dfs(num * 10 + d, remaining - 1, new_counts)
      else
        []
      end
    end)
  end
end
```
