# 3144. Minimum Substring Partition of Equal Character Frequency

## Cpp

```cpp
class Solution {
public:
    int minimumSubstringsInPartition(string s) {
        int n = s.size();
        const int INF = n + 5;
        vector<int> dp(n + 1, INF);
        dp[0] = 0;
        for (int i = 1; i <= n; ++i) {
            int cnt[26] = {0};
            int maxFreq = 0;
            for (int j = i - 1; j >= 0; --j) {
                int idx = s[j] - 'a';
                ++cnt[idx];
                if (cnt[idx] > maxFreq) maxFreq = cnt[idx];
                
                bool balanced = true;
                for (int k = 0; k < 26; ++k) {
                    if (cnt[k] > 0 && cnt[k] != maxFreq) {
                        balanced = false;
                        break;
                    }
                }
                if (balanced) {
                    dp[i] = min(dp[i], dp[j] + 1);
                }
            }
        }
        return dp[n];
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int minimumSubstringsInPartition(String s) {
        int n = s.length();
        int[] dp = new int[n + 1];
        Arrays.fill(dp, n + 1);
        dp[0] = 0;
        char[] chars = s.toCharArray();

        for (int i = 1; i <= n; ++i) {
            int[] cnt = new int[26];
            for (int j = i - 1; j >= 0; --j) {
                cnt[chars[j] - 'a']++;
                if (isBalanced(cnt)) {
                    dp[i] = Math.min(dp[i], dp[j] + 1);
                }
            }
        }
        return dp[n];
    }

    private boolean isBalanced(int[] cnt) {
        int target = 0;
        for (int c : cnt) {
            if (c > 0) {
                target = c;
                break;
            }
        }
        if (target == 0) return false; // empty substring, shouldn't happen
        for (int c : cnt) {
            if (c > 0 && c != target) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def minimumSubstringsInPartition(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # prefix counts
        pref = [[0] * 26 for _ in range(n + 1)]
        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            for c in range(26):
                pref[i + 1][c] = pref[i][c]
            pref[i + 1][idx] += 1

        def balanced(cnt):
            freq = 0
            for v in cnt:
                if v:
                    if freq == 0:
                        freq = v
                    elif v != freq:
                        return False
            return True

        INF = n + 1
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            # try all possible previous cuts
            for j in range(i):
                # compute counts of s[j:i]
                cnt = [pref[i][c] - pref[j][c] for c in range(26)]
                if balanced(cnt):
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n]
```

## Python3

```python
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        INF = n + 5
        dp = [INF] * n
        chars = [ord(c) - 97 for c in s]

        for start in range(n):
            counts = [0] * 26
            max_freq = 0
            for end in range(start, n):
                idx = chars[end]
                counts[idx] += 1
                if counts[idx] > max_freq:
                    max_freq = counts[idx]

                # find minimum non‑zero frequency
                min_freq = INF
                for cnt in counts:
                    if 0 < cnt < min_freq:
                        min_freq = cnt

                if max_freq == min_freq:   # balanced substring s[start..end]
                    prev = dp[start - 1] if start > 0 else 0
                    cur = prev + 1
                    if cur < dp[end]:
                        dp[end] = cur

        return dp[-1]
```

## C

```c
#include <limits.h>

int minimumSubstringsInPartition(char* s) {
    int n = 0;
    while (s[n]) n++;
    const int INF = 1000000000;
    int dp[1001];
    for (int i = 0; i <= n; ++i) dp[i] = INF;
    dp[0] = 0;

    for (int i = 1; i <= n; ++i) {
        int freq[26] = {0};
        for (int j = i - 1; j >= 0; --j) {
            freq[s[j] - 'a']++;

            int maxf = 0, minf = INT_MAX;
            int distinct = 0;
            for (int k = 0; k < 26; ++k) {
                if (freq[k]) {
                    ++distinct;
                    if (freq[k] > maxf) maxf = freq[k];
                    if (freq[k] < minf) minf = freq[k];
                }
            }

            if (distinct == 0 || maxf == minf) {
                if (dp[j] + 1 < dp[i]) dp[i] = dp[j] + 1;
            }
        }
    }
    return dp[n];
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumSubstringsInPartition(string s) {
        int n = s.Length;
        // prefix counts for each character
        int[,] pref = new int[26, n + 1];
        for (int i = 0; i < n; i++) {
            int chIdx = s[i] - 'a';
            for (int c = 0; c < 26; c++) {
                pref[c, i + 1] = pref[c, i];
            }
            pref[chIdx, i + 1]++;
        }

        int[] dp = new int[n];
        const int INF = 1005;
        for (int i = 0; i < n; i++) dp[i] = INF;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                // check if substring s[j..i] is balanced
                int target = -1;
                bool ok = true;
                for (int c = 0; c < 26; c++) {
                    int cnt = pref[c, i + 1] - pref[c, j];
                    if (cnt > 0) {
                        if (target == -1) target = cnt;
                        else if (cnt != target) { ok = false; break; }
                    }
                }
                if (ok) {
                    int prev = (j > 0) ? dp[j - 1] : 0;
                    dp[i] = Math.Min(dp[i], prev + 1);
                }
            }
        }

        return dp[n - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minimumSubstringsInPartition = function(s) {
    const n = s.length;
    const INF = 1 << 30;
    const dp = new Array(n + 1).fill(INF);
    dp[0] = 0;

    for (let start = 0; start < n; ++start) {
        const cnt = new Array(26).fill(0);
        let maxFreq = 0;
        for (let end = start; end < n; ++end) {
            const idx = s.charCodeAt(end) - 97;
            cnt[idx]++;
            if (cnt[idx] > maxFreq) maxFreq = cnt[idx];

            // find min frequency among characters that appear
            let minFreq = INF;
            for (let k = 0; k < 26; ++k) {
                const c = cnt[k];
                if (c > 0 && c < minFreq) minFreq = c;
            }

            if (maxFreq === minFreq) {
                dp[end + 1] = Math.min(dp[end + 1], dp[start] + 1);
            }
        }
    }

    return dp[n];
};
```

## Typescript

```typescript
function minimumSubstringsInPartition(s: string): number {
    const n = s.length;
    const INF = n + 1;
    const dp = new Array(n + 1).fill(INF);
    dp[0] = 0;

    for (let i = 1; i <= n; ++i) {
        const cnt = new Array(26).fill(0);
        let maxFreq = 0;
        for (let j = i - 1; j >= 0; --j) {
            const idx = s.charCodeAt(j) - 97;
            cnt[idx]++;
            if (cnt[idx] > maxFreq) maxFreq = cnt[idx];

            // find minimum non‑zero frequency
            let minFreq = Infinity;
            for (let k = 0; k < 26; ++k) {
                const c = cnt[k];
                if (c > 0 && c < minFreq) minFreq = c;
            }

            if (maxFreq === minFreq) {
                dp[i] = Math.min(dp[i], dp[j] + 1);
            }
        }
    }

    return dp[n];
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minimumSubstringsInPartition($s) {
        $n = strlen($s);
        $dp = array_fill(0, $n + 1, $n + 1);
        $dp[0] = 0;
        for ($i = 1; $i <= $n; $i++) {
            // frequency of characters in current substring s[j..i-1]
            $cnt = array_fill(0, 26, 0);
            $maxFreq = 0;
            for ($j = $i - 1; $j >= 0; $j--) {
                $idx = ord($s[$j]) - 97; // 'a' ascii is 97
                $cnt[$idx]++;
                if ($cnt[$idx] > $maxFreq) {
                    $maxFreq = $cnt[$idx];
                }
                // compute min non‑zero frequency
                $minFreq = PHP_INT_MAX;
                foreach ($cnt as $c) {
                    if ($c > 0 && $c < $minFreq) {
                        $minFreq = $c;
                    }
                }
                // balanced iff all non‑zero frequencies are equal
                if ($maxFreq == $minFreq) {
                    $dp[$i] = min($dp[$i], $dp[$j] + 1);
                }
            }
        }
        return $dp[$n];
    }
}
```

## Swift

```swift
class Solution {
    func minimumSubstringsInPartition(_ s: String) -> Int {
        let bytes = Array(s.utf8)
        let n = bytes.count
        var dp = Array(repeating: Int.max / 2, count: n + 1)
        dp[0] = 0
        
        for i in 0..<n {
            var cnt = Array(repeating: 0, count: 26)
            var distinct = 0
            for j in i..<n {
                let idx = Int(bytes[j] - 97) // 'a' ascii is 97
                if cnt[idx] == 0 { distinct += 1 }
                cnt[idx] += 1
                
                let len = j - i + 1
                if len % distinct == 0 {
                    let freq = len / distinct
                    var ok = true
                    for k in 0..<26 where cnt[k] > 0 {
                        if cnt[k] != freq {
                            ok = false
                            break
                        }
                    }
                    if ok {
                        dp[j + 1] = min(dp[j + 1], dp[i] + 1)
                    }
                }
            }
        }
        
        return dp[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumSubstringsInPartition(s: String): Int {
        val n = s.length
        val INF = n + 5
        val dp = IntArray(n + 1) { INF }
        dp[0] = 0
        for (i in 1..n) {
            val freq = IntArray(26)
            for (j in i - 1 downTo 0) {
                val idx = s[j] - 'a'
                freq[idx]++
                var maxCnt = 0
                var minCnt = Int.MAX_VALUE
                for (c in 0 until 26) {
                    val f = freq[c]
                    if (f > 0) {
                        if (f > maxCnt) maxCnt = f
                        if (f < minCnt) minCnt = f
                    }
                }
                if (maxCnt == minCnt) {
                    dp[i] = kotlin.math.min(dp[i], dp[j] + 1)
                }
            }
        }
        return dp[n]
    }
}
```

## Dart

```dart
class Solution {
  int minimumSubstringsInPartition(String s) {
    int n = s.length;
    const int INF = 1 << 30;
    List<int> dp = List.filled(n + 1, INF);
    dp[0] = 0;

    // temporary count array reused for each i
    List<int> cnt = List.filled(26, 0);

    for (int i = 1; i <= n; ++i) {
      // reset counts for new end position i-1
      for (int k = 0; k < 26; ++k) cnt[k] = 0;

      for (int j = i - 1; j >= 0; --j) {
        int idx = s.codeUnitAt(j) - 97;
        cnt[idx]++;

        if (_isBalanced(cnt)) {
          dp[i] = dp[i] < dp[j] + 1 ? dp[i] : dp[j] + 1;
        }
      }
    }

    return dp[n];
  }

  bool _isBalanced(List<int> cnt) {
    int base = 0;
    for (int c in cnt) {
      if (c > 0) {
        base = c;
        break;
      }
    }
    if (base == 0) return false; // empty substring, shouldn't happen
    for (int c in cnt) {
      if (c > 0 && c != base) return false;
    }
    return true;
  }
}
```

## Golang

```go
func minimumSubstringsInPartition(s string) int {
	n := len(s)
	pref := make([][26]int, n+1)
	for i, ch := range s {
		pref[i+1] = pref[i]
		pref[i+1][ch-'a']++
	}
	const INF = 1 << 30
	dp := make([]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = INF
	}
	dp[0] = 0
	for i := 1; i <= n; i++ {
		for j := 0; j < i; j++ {
			base := -1
			balanced := true
			for c := 0; c < 26; c++ {
				cnt := pref[i][c] - pref[j][c]
				if cnt > 0 {
					if base == -1 {
						base = cnt
					} else if cnt != base {
						balanced = false
						break
					}
				}
			}
			if balanced && dp[j]+1 < dp[i] {
				dp[i] = dp[j] + 1
			}
		}
	}
	return dp[n]
}
```

## Ruby

```ruby
def minimum_substrings_in_partition(s)
  n = s.length
  chars = s.bytes.map { |b| b - 97 }
  INF = n + 1
  dp = Array.new(n + 1, INF)
  dp[0] = 0

  (1..n).each do |i|
    freq = Array.new(26, 0)
    j = i - 1
    while j >= 0
      idx = chars[j]
      freq[idx] += 1

      target = nil
      balanced = true
      26.times do |c|
        cnt = freq[c]
        next if cnt == 0
        if target.nil?
          target = cnt
        elsif cnt != target
          balanced = false
          break
        end
      end

      if balanced
        val = dp[j] + 1
        dp[i] = val if val < dp[i]
      end

      j -= 1
    end
  end

  dp[n]
end
```

## Scala

```scala
object Solution {
    def minimumSubstringsInPartition(s: String): Int = {
        val n = s.length
        val INF = n + 5
        val dp = Array.fill(n + 1)(INF)
        dp(0) = 0

        for (i <- 0 until n) {
            if (dp(i) == INF) {
                // unreachable prefix, skip
            } else {
                val cnt = new Array[Int](26)
                var distinct = 0
                for (j <- i until n) {
                    val idx = s.charAt(j) - 'a'
                    if (cnt(idx) == 0) distinct += 1
                    cnt(idx) += 1

                    var maxF = 0
                    var minF = Int.MaxValue
                    for (k <- 0 until 26) {
                        val c = cnt(k)
                        if (c > 0) {
                            if (c > maxF) maxF = c
                            if (c < minF) minF = c
                        }
                    }

                    if (maxF == minF) {
                        val newVal = dp(i) + 1
                        if (newVal < dp(j + 1)) dp(j + 1) = newVal
                    }
                }
            }
        }

        dp(n)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_substrings_in_partition(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut dp = vec![i32::MAX / 2; n + 1];
        dp[0] = 0;
        for i in 1..=n {
            let mut freq = [0i32; 26];
            for j in (0..i).rev() {
                let idx = (bytes[j] - b'a') as usize;
                freq[idx] += 1;
                if Self::is_balanced(&freq) {
                    dp[i] = dp[i].min(dp[j] + 1);
                }
            }
        }
        dp[n]
    }

    fn is_balanced(freq: &[i32; 26]) -> bool {
        let mut target = 0i32;
        for &c in freq.iter() {
            if c > 0 {
                if target == 0 {
                    target = c;
                } else if c != target {
                    return false;
                }
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (minimum-substrings-in-partition s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (max-part (+ n 1))                     ; upper bound
         (dp (make-vector (+ n 1) max-part)))   ; dp[i] = min partitions for prefix length i
    (vector-set! dp 0 0)
    (for ([j (in-range n)])
      (when (< (vector-ref dp j) max-part)       ; reachable state
        (let ((counts (make-vector 26 0))
              (distinct 0))
          (for ([i (in-range (+ j 1) (+ n 1))])
            (define idx (- (char->integer (string-ref s (- i 1))) (char->integer #\a)))
            (define old (vector-ref counts idx))
            (when (= old 0) (set! distinct (+ distinct 1)))
            (vector-set! counts idx (+ old 1))
            ;; check if substring s[j..i-1] is balanced
            (let ((freq -1)
                  (balanced #t))
              (for ([k (in-range 26)])
                (define c (vector-ref counts k))
                (when (> c 0)
                  (if (= freq -1)
                      (set! freq c)
                      (when (not (= c freq)) (set! balanced #f)))))
              (when balanced
                (let ((cand (+ (vector-ref dp j) 1)))
                  (when (< cand (vector-ref dp i))
                    (vector-set! dp i cand))))))))))
    (vector-ref dp n)))
```

## Erlang

```erlang
-spec minimum_substrings_in_partition(S :: unicode:unicode_binary()) -> integer().
minimum_substrings_in_partition(S) ->
    SList = binary_to_list(S),
    N = length(SList),
    CharArr = array:from_list(SList),
    DP0 = array:new(N + 1, {default, 0}),
    DP = process_i(1, N, CharArr, DP0),
    array:get(N, DP).

process_i(I, N, _CharArr, DP) when I > N ->
    DP;
process_i(I, N, CharArr, DP) ->
    Best = find_best(I, CharArr, DP),
    DP2 = array:set(I, Best, DP),
    process_i(I + 1, N, CharArr, DP2).

find_best(I, CharArr, DP) ->
    Counts0 = erlang:make_tuple(26, 0),
    go(I, I, CharArr, DP, Counts0, I + 1).

go(J, _I, _CharArr, _DP, _Counts, Best) when J < 1 ->
    Best;
go(J, I, CharArr, DP, Counts, Best) ->
    C = array:get(J - 1, CharArr),
    Idx = C - $a,
    NewCounts = update_counts(Idx, Counts),
    {MaxF, MinF} = max_min(NewCounts),
    NewBest =
        case MaxF == MinF of
            true ->
                Prev = array:get(J - 1, DP),
                erlang:min(Best, Prev + 1);
            false -> Best
        end,
    go(J - 1, I, CharArr, DP, NewCounts, NewBest).

update_counts(Index, Tuple) ->
    Old = element(Index + 1, Tuple),
    setelement(Index + 1, Tuple, Old + 1).

max_min(Tuple) ->
    max_min(1, Tuple, 0, undefined).

max_min(Pos, _Tuple, Max, Min) when Pos > 26 ->
    {Max, Min};
max_min(Pos, Tuple, Max, Min) ->
    V = element(Pos, Tuple),
    if
        V == 0 ->
            max_min(Pos + 1, Tuple, Max, Min);
        true ->
            NewMax = case V > Max of true -> V; false -> Max end,
            NewMin = case Min of
                        undefined -> V;
                        _ when V < Min -> V;
                        _ -> Min
                     end,
            max_min(Pos + 1, Tuple, NewMax, NewMin)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_substrings_in_partition(s :: String.t()) :: integer
  def minimum_substrings_in_partition(s) do
    chars = String.to_charlist(s)
    n = length(chars)

    zero_counts = List.duplicate(0, 26)

    # Build prefix count array
    pref_arr =
      :array.new(n + 1, default: zero_counts)
      |> :array.set(0, zero_counts)

    {pref_arr, _} =
      Enum.reduce(Enum.with_index(chars, 1), {pref_arr, zero_counts}, fn {ch, idx},
                                                                      {arr, prev_counts} ->
        new_counts = inc_counts(prev_counts, ch - ?a)
        arr = :array.set(idx, new_counts, arr)
        {arr, new_counts}
      end)

    # DP array
    dp =
      :array.new(n + 1, default: n + 1)
      |> :array.set(0, 0)

    dp = compute_dp(1, n, pref_arr, dp)
    :array.get(n, dp)
  end

  defp inc_counts(counts, idx) do
    List.update_at(counts, idx, &(&1 + 1))
  end

  defp compute_dp(i, n, _pref_arr, dp) when i > n, do: dp

  defp compute_dp(i, n, pref_arr, dp) do
    counts_i = :array.get(i, pref_arr)
    min_part = find_min(0, i - 1, counts_i, pref_arr, dp, n + 1)
    dp = :array.set(i, min_part, dp)
    compute_dp(i + 1, n, pref_arr, dp)
  end

  defp find_min(j, max_j, _counts_i, _pref_arr, _dp, cur_min) when j > max_j,
    do: cur_min

  defp find_min(j, max_j, counts_i, pref_arr, dp, cur_min) do
    counts_j = :array.get(j, pref_arr)

    if balanced?(counts_i, counts_j) do
      cand = :array.get(j, dp) + 1
      new_min = if cand < cur_min, do: cand, else: cur_min
      find_min(j + 1, max_j, counts_i, pref_arr, dp, new_min)
    else
      find_min(j + 1, max_j, counts_i, pref_arr, dp, cur_min)
    end
  end

  defp balanced?(counts_i, counts_j) do
    balanced_helper(counts_i, counts_j, 0, nil)
  end

  defp balanced_helper(_ci, _cj, 26, _base), do: true

  defp balanced_helper(ci, cj, idx, base) do
    cnt = Enum.at(ci, idx) - Enum.at(cj, idx)

    cond do
      cnt == 0 ->
        balanced_helper(ci, cj, idx + 1, base)

      base == nil ->
        balanced_helper(ci, cj, idx + 1, cnt)

      cnt == base ->
        balanced_helper(ci, cj, idx + 1, base)

      true ->
        false
    end
  end
end
```
