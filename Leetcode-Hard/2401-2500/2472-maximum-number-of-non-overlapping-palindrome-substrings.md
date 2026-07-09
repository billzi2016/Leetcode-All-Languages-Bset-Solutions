# 2472. Maximum Number of Non-overlapping Palindrome Substrings

## Cpp

```cpp
class Solution {
public:
    int maxPalindromes(string s, int k) {
        int n = s.size();
        vector<vector<int>> startList(n);
        for (int center = 0; center < n; ++center) {
            // odd length palindromes
            int l = center, r = center;
            while (l >= 0 && r < n && s[l] == s[r]) {
                if (r - l + 1 >= k) startList[r].push_back(l);
                --l; ++r;
            }
            // even length palindromes
            l = center; r = center + 1;
            while (l >= 0 && r < n && s[l] == s[r]) {
                if (r - l + 1 >= k) startList[r].push_back(l);
                --l; ++r;
            }
        }
        vector<int> dp(n, 0);
        for (int i = 0; i < n; ++i) {
            if (i > 0) dp[i] = dp[i - 1];
            for (int l : startList[i]) {
                int cand = (l > 0 ? dp[l - 1] : 0) + 1;
                dp[i] = max(dp[i], cand);
            }
        }
        return dp.empty() ? 0 : dp.back();
    }
};
```

## Java

```java
class Solution {
    public int maxPalindromes(String s, int k) {
        int n = s.length();
        @SuppressWarnings("unchecked")
        ArrayList<Integer>[] palsEnd = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            palsEnd[i] = new ArrayList<>();
        }
        // expand around centers
        for (int center = 0; center < n; center++) {
            // odd length palindromes
            int l = center, r = center;
            while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 >= k) {
                    palsEnd[r].add(l);
                }
                l--;
                r++;
            }
            // even length palindromes
            l = center;
            r = center + 1;
            while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 >= k) {
                    palsEnd[r].add(l);
                }
                l--;
                r++;
            }
        }

        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            dp[i] = (i > 0 ? dp[i - 1] : 0);
            for (int start : palsEnd[i]) {
                int prev = (start > 0 ? dp[start - 1] : 0);
                dp[i] = Math.max(dp[i], prev + 1);
            }
        }
        return n == 0 ? 0 : dp[n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        # palindrome table
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n):
            is_pal[i][i] = True
        for i in range(n - 1):
            is_pal[i][i + 1] = (s[i] == s[i + 1])
        for length in range(3, n + 1):
            for l in range(0, n - length + 1):
                r = l + length - 1
                if s[l] == s[r] and is_pal[l + 1][r - 1]:
                    is_pal[l][r] = True

        dp = [0] * n
        for i in range(n):
            # skip current character
            if i > 0:
                dp[i] = dp[i - 1]
            else:
                dp[i] = 0
            # try to end a palindrome at i
            max_start = i - k + 1
            if max_start < 0:
                continue
            for j in range(0, max_start + 1):
                if is_pal[j][i]:
                    prev = dp[j - 1] if j > 0 else 0
                    dp[i] = max(dp[i], prev + 1)
        return dp[-1] if n else 0
```

## Python3

```python
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            si = s[i]
            row = pal[i]
            for j in range(i, n):
                if si == s[j] and (j - i < 2 or pal[i + 1][j - 1]):
                    row[j] = True
        dp = [0] * n
        for i in range(n):
            best = dp[i - 1] if i > 0 else 0
            start = i - k + 1
            for l in range(start, -1, -1):
                if pal[l][i]:
                    prev = dp[l - 1] if l > 0 else 0
                    if prev + 1 > best:
                        best = prev + 1
            dp[i] = best
        return dp[-1]
```

## C

```c
int maxPalindromes(char* s, int k) {
    int n = 0;
    while (s[n]) ++n;
    if (n == 0) return 0;

    char *pal = (char*)calloc((size_t)n * (size_t)n, sizeof(char));
    for (int i = n - 1; i >= 0; --i) {
        for (int j = i; j < n; ++j) {
            if (s[i] == s[j] && (j - i < 2 || pal[(i + 1) * n + (j - 1)])) {
                pal[i * n + j] = 1;
            }
        }
    }

    int *dp = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        dp[i] = (i > 0 ? dp[i - 1] : 0);
        for (int j = i; j >= 0; --j) {
            if (pal[j * n + i] && (i - j + 1) >= k) {
                int cand = (j > 0 ? dp[j - 1] : 0) + 1;
                if (cand > dp[i]) dp[i] = cand;
            }
        }
    }

    int ans = dp[n - 1];
    free(pal);
    free(dp);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxPalindromes(string s, int k)
    {
        int n = s.Length;
        if (k > n) return 0;

        List<int>[] ends = new List<int>[n];
        for (int i = 0; i < n; i++) ends[i] = new List<int>();

        char[] ch = s.ToCharArray();

        // odd length palindromes
        for (int center = 0; center < n; center++)
        {
            int l = center, r = center;
            while (l >= 0 && r < n && ch[l] == ch[r])
            {
                if (r - l + 1 >= k)
                    ends[r].Add(l);
                l--;
                r++;
            }
        }

        // even length palindromes
        for (int center = 0; center < n - 1; center++)
        {
            int l = center, r = center + 1;
            while (l >= 0 && r < n && ch[l] == ch[r])
            {
                if (r - l + 1 >= k)
                    ends[r].Add(l);
                l--;
                r++;
            }
        }

        int[] dp = new int[n];
        for (int i = 0; i < n; i++)
        {
            dp[i] = i > 0 ? dp[i - 1] : 0;
            foreach (int start in ends[i])
            {
                int prev = start > 0 ? dp[start - 1] : 0;
                dp[i] = Math.Max(dp[i], prev + 1);
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
 * @param {number} k
 * @return {number}
 */
var maxPalindromes = function(s, k) {
    const n = s.length;
    if (k > n) return 0;

    // precompute palindrome table
    const isPal = Array.from({ length: n }, () => Array(n).fill(false));
    for (let center = 0; center < n; ++center) {
        // odd length palindromes
        let l = center, r = center;
        while (l >= 0 && r < n && s[l] === s[r]) {
            isPal[l][r] = true;
            --l; ++r;
        }
        // even length palindromes
        l = center; r = center + 1;
        while (l >= 0 && r < n && s[l] === s[r]) {
            isPal[l][r] = true;
            --l; ++r;
        }
    }

    const dp = Array(n).fill(0);
    for (let i = 0; i < n; ++i) {
        dp[i] = i > 0 ? dp[i - 1] : 0;
        for (let start = 0; start <= i; ++start) {
            if (isPal[start][i] && (i - start + 1) >= k) {
                const cand = (start > 0 ? dp[start - 1] : 0) + 1;
                if (cand > dp[i]) dp[i] = cand;
            }
        }
    }
    return dp[n - 1];
};
```

## Typescript

```typescript
function maxPalindromes(s: string, k: number): number {
    const n = s.length;
    const endsAt: number[][] = Array.from({ length: n }, () => []);
    
    for (let center = 0; center < n; ++center) {
        // odd length palindromes
        let l = center, r = center;
        while (l >= 0 && r < n && s[l] === s[r]) {
            if (r - l + 1 >= k) endsAt[r].push(l);
            l--; r++;
        }
        // even length palindromes
        l = center; r = center + 1;
        while (l >= 0 && r < n && s[l] === s[r]) {
            if (r - l + 1 >= k) endsAt[r].push(l);
            l--; r++;
        }
    }

    const dp: number[] = new Array(n).fill(0);
    for (let i = 0; i < n; ++i) {
        if (i > 0) dp[i] = dp[i - 1];
        for (const start of endsAt[i]) {
            const cand = (start > 0 ? dp[start - 1] : 0) + 1;
            if (cand > dp[i]) dp[i] = cand;
        }
    }

    return n === 0 ? 0 : dp[n - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function maxPalindromes($s, $k) {
        $n = strlen($s);
        $dp = array_fill(0, $n + 1, 0); // dp[i]: max count for prefix length i

        for ($i = 0; $i < $n; $i++) {
            // Skip current character
            if ($dp[$i + 1] < $dp[$i]) {
                $dp[$i + 1] = $dp[$i];
            }

            // Odd length palindromes centered at i
            $l = $i;
            $r = $i;
            while ($l >= 0 && $r < $n && $s[$l] === $s[$r]) {
                if ($r - $l + 1 >= $k) {
                    $candidate = $dp[$l] + 1;
                    $idx = $r + 1;
                    if ($dp[$idx] < $candidate) {
                        $dp[$idx] = $candidate;
                    }
                }
                $l--;
                $r++;
            }

            // Even length palindromes centered between i and i+1
            $l = $i;
            $r = $i + 1;
            while ($l >= 0 && $r < $n && $s[$l] === $s[$r]) {
                if ($r - $l + 1 >= $k) {
                    $candidate = $dp[$l] + 1;
                    $idx = $r + 1;
                    if ($dp[$idx] < $candidate) {
                        $dp[$idx] = $candidate;
                    }
                }
                $l--;
                $r++;
            }
        }

        return $dp[$n];
    }
}
```

## Swift

```swift
class Solution {
    func maxPalindromes(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        if k > n { return 0 }
        
        var palEnds = Array(repeating: [Int](), count: n)
        
        for center in 0..<n {
            // odd length palindromes
            var left = center
            var right = center
            while left >= 0 && right < n && chars[left] == chars[right] {
                if right - left + 1 >= k {
                    palEnds[right].append(left)
                }
                left -= 1
                right += 1
            }
            // even length palindromes
            left = center
            right = center + 1
            while left >= 0 && right < n && chars[left] == chars[right] {
                if right - left + 1 >= k {
                    palEnds[right].append(left)
                }
                left -= 1
                right += 1
            }
        }
        
        var dp = Array(repeating: 0, count: n + 1) // dp[i]: best for first i characters
        for r in 0..<n {
            var bestCandidate = 0
            for l in palEnds[r] {
                let val = dp[l] + 1
                if val > bestCandidate { bestCandidate = val }
            }
            dp[r + 1] = max(dp[r], bestCandidate)
        }
        
        return dp[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxPalindromes(s: String, k: Int): Int {
        val n = s.length
        if (k > n) return 0
        val endsAt = Array(n) { mutableListOf<Int>() }

        // odd length palindromes
        for (center in 0 until n) {
            var l = center
            var r = center
            while (l >= 0 && r < n && s[l] == s[r]) {
                if (r - l + 1 >= k) endsAt[r].add(l)
                l--
                r++
            }
        }

        // even length palindromes
        for (center in 0 until n - 1) {
            var l = center
            var r = center + 1
            while (l >= 0 && r < n && s[l] == s[r]) {
                if (r - l + 1 >= k) endsAt[r].add(l)
                l--
                r++
            }
        }

        val dp = IntArray(n)
        for (i in 0 until n) {
            if (i > 0) dp[i] = dp[i - 1]
            for (start in endsAt[i]) {
                val prev = if (start > 0) dp[start - 1] else 0
                dp[i] = kotlin.math.max(dp[i], prev + 1)
            }
        }
        return dp[n - 1]
    }
}
```

## Dart

```dart
class Solution {
  int maxPalindromes(String s, int k) {
    int n = s.length;
    List<List<int>> palStartAtEnd = List.generate(n, (_) => []);
    // odd length palindromes
    for (int center = 0; center < n; ++center) {
      int l = center, r = center;
      while (l >= 0 && r < n && s.codeUnitAt(l) == s.codeUnitAt(r)) {
        if (r - l + 1 >= k) {
          palStartAtEnd[r].add(l);
        }
        --l;
        ++r;
      }
    }
    // even length palindromes
    for (int center = 0; center < n - 1; ++center) {
      int l = center, r = center + 1;
      while (l >= 0 && r < n && s.codeUnitAt(l) == s.codeUnitAt(r)) {
        if (r - l + 1 >= k) {
          palStartAtEnd[r].add(l);
        }
        --l;
        ++r;
      }
    }

    List<int> dp = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      int best = i > 0 ? dp[i - 1] : 0;
      for (int l in palStartAtEnd[i]) {
        int cand = (l > 0 ? dp[l - 1] : 0) + 1;
        if (cand > best) best = cand;
      }
      dp[i] = best;
    }
    return dp[n - 1];
  }
}
```

## Golang

```go
func maxPalindromes(s string, k int) int {
	n := len(s)
	ends := make([][]int, n)

	for center := 0; center < n; center++ {
		// odd length palindromes
		l, r := center, center
		for l >= 0 && r < n && s[l] == s[r] {
			if r-l+1 >= k {
				ends[r] = append(ends[r], l)
			}
			l--
			r++
		}
		// even length palindromes
		l, r = center, center+1
		for l >= 0 && r < n && s[l] == s[r] {
			if r-l+1 >= k {
				ends[r] = append(ends[r], l)
			}
			l--
			r++
		}
	}

	dp := make([]int, n)
	for i := 0; i < n; i++ {
		if i > 0 {
			dp[i] = dp[i-1]
		}
		for _, start := range ends[i] {
			prev := 0
			if start > 0 {
				prev = dp[start-1]
			}
			if prev+1 > dp[i] {
				dp[i] = prev + 1
			}
		}
	}
	return dp[n-1]
}
```

## Ruby

```ruby
def max_palindromes(s, k)
  n = s.length
  chars = s.bytes

  # Precompute palindrome table
  is_pal = Array.new(n) { Array.new(n, false) }
  i = n - 1
  while i >= 0
    is_pal[i][i] = true
    j = i + 1
    while j < n
      if chars[i] == chars[j] && (j - i == 1 || is_pal[i + 1][j - 1])
        is_pal[i][j] = true
      end
      j += 1
    end
    i -= 1
  end

  # For each start, find the shortest palindrome with length >= k
  min_end = Array.new(n)
  i = 0
  while i < n
    j = i + k - 1
    while j < n && !is_pal[i][j]
      j += 1
    end
    min_end[i] = (j < n) ? j : nil
    i += 1
  end

  # DP over prefix lengths
  dp = Array.new(n + 1, 0)
  i = 0
  while i < n
    dp[i + 1] = dp[i] if dp[i] > dp[i + 1]
    e = min_end[i]
    if e
      val = dp[i] + 1
      dp[e + 1] = val if val > dp[e + 1]
    end
    i += 1
  end

  dp[n]
end
```

## Scala

```scala
object Solution {
    def maxPalindromes(s: String, k: Int): Int = {
        val n = s.length
        if (n == 0) return 0
        val isPal = Array.ofDim[Boolean](n, n)
        for (i <- (0 until n).reverse) {
            var j = i
            while (j < n) {
                if (s.charAt(i) == s.charAt(j) && (j - i < 2 || isPal(i + 1)(j - 1))) {
                    isPal(i)(j) = true
                }
                j += 1
            }
        }
        val dp = Array.fill[Int](n)(0)
        for (i <- 0 until n) {
            if (i > 0) dp(i) = dp(i - 1)
            var start = 0
            val maxStart = i - k + 1
            while (start <= maxStart) {
                if (isPal(start)(i)) {
                    val cand = if (start > 0) dp(start - 1) + 1 else 1
                    if (cand > dp(i)) dp(i) = cand
                }
                start += 1
            }
        }
        dp(n - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_palindromes(s: String, k: i32) -> i32 {
        let n = s.len();
        if n == 0 { return 0; }
        let bytes = s.as_bytes();
        let k_usize = k as usize;
        let mut ends_at: Vec<Vec<usize>> = vec![Vec::new(); n];

        for center in 0..n {
            // odd length palindromes
            let mut l = center as i32;
            let mut r = center as i32;
            while l >= 0 && (r as usize) < n && bytes[l as usize] == bytes[r as usize] {
                let len = (r - l + 1) as usize;
                if len >= k_usize {
                    ends_at[r as usize].push(l as usize);
                }
                l -= 1;
                r += 1;
            }
            // even length palindromes
            let mut l = center as i32;
            let mut r = (center + 1) as i32;
            while l >= 0 && (r as usize) < n && bytes[l as usize] == bytes[r as usize] {
                let len = (r - l + 1) as usize;
                if len >= k_usize {
                    ends_at[r as usize].push(l as usize);
                }
                l -= 1;
                r += 1;
            }
        }

        let mut dp: Vec<i32> = vec![0; n];
        for i in 0..n {
            if i > 0 {
                dp[i] = dp[i - 1];
            }
            for &start in ends_at[i].iter() {
                let prev = if start > 0 { dp[start - 1] } else { 0 };
                dp[i] = dp[i].max(prev + 1);
            }
        }
        dp[n - 1]
    }
}
```

## Racket

```racket
(define/contract (max-palindromes s k)
  (-> string? exact-integer? exact-integer?)
  (let* ((n (string-length s))
         (pal (make-vector n)))
    ;; initialize palindrome table
    (for ([i (in-range n)])
      (vector-set! pal i (make-vector n #f)))
    ;; fill palindrome DP
    (for ([len (in-range 1 (+ n 1))])
      (for ([i (in-range 0 (+ 1 (- n len)))])
        (let* ((j (+ i len -1))
               (chars-eq? (char=? (string-ref s i) (string-ref s j)))
               (is-pal (if chars-eq?
                           (or (< (- j i) 2)
                               (vector-ref (vector-ref pal (+ i 1)) (- j 1)))
                           #f)))
          (when is-pal
            (vector-set! (vector-ref pal i) j #t)))))
    ;; dp[i] = max number for prefix ending at i
    (define dp (make-vector n -1000000))
    (for ([i (in-range n)])
      (let ((skip (if (> i 0) (vector-ref dp (- i 1)) 0)))
        (vector-set! dp i skip)
        ;; consider all palindromes ending at i with length >= k
        (for ([start (in-range 0 (+ i 1))])
          (when (and (>= (+ 1 (- i start)) k)
                     (vector-ref (vector-ref pal start) i))
            (let* ((prev (if (> start 0) (vector-ref dp (- start 1)) 0))
                   (cand (+ prev 1)))
              (when (> cand (vector-ref dp i))
                (vector-set! dp i cand)))))))
    (if (= n 0) 0 (vector-ref dp (- n 1)))))
```

## Erlang

```erlang
-module(solution).
-export([max_palindromes/2]).

-spec max_palindromes(S :: unicode:unicode_binary(), K :: integer()) -> integer().
max_palindromes(S, K) ->
    CharList = unicode:characters_to_list(S),
    N = length(CharList),
    Tuple = list_to_tuple(CharList),
    PalMap = build_map(N, Tuple, K),
    DPArray = compute_dp(N, PalMap),
    array:get(N - 1, DPArray).

%% Build a map EndIdx => [StartIdx,...] for all palindromes with length >= K
build_map(N, Tup, K) ->
    lists:foldl(fun(C, M) ->
        M1 = expand(C, C, N, Tup, K, M),               % odd length centers
        case C + 1 < N of
            true -> expand(C, C + 1, N, Tup, K, M1);   % even length centers
            false -> M1
        end
    end, #{}, lists:seq(0, N - 1)).

%% Expand around (L,R) and record qualifying palindromes
expand(L, R, N, Tup, K, Map) when L >= 0, R < N ->
    case element(L + 1, Tup) =:= element(R + 1, Tup) of
        true ->
            NewMap = if (R - L + 1) >= K -> add_start(R, L, Map); true -> Map end,
            expand(L - 1, R + 1, N, Tup, K, NewMap);
        false -> Map
    end;
expand(_, _, _, _, _, Map) ->
    Map.

add_start(EndIdx, StartIdx, Map) ->
    Prev = maps:get(EndIdx, Map, []),
    maps:put(EndIdx, [StartIdx | Prev], Map).

%% Compute DP array where dp[i] is max count for prefix ending at i
compute_dp(N, PalMap) ->
    DP0 = array:new(N, [{default, 0}]),
    dp_loop(0, N, PalMap, DP0).

dp_loop(R, N, _PalMap, DP) when R >= N ->
    DP;
dp_loop(R, N, PalMap, DP) ->
    Prev = if R > 0 -> array:get(R - 1, DP); true -> 0 end,
    Starts = maps:get(R, PalMap, []),
    MaxVal = lists:foldl(fun(L, Acc) ->
        Cand = (if L > 0 -> array:get(L - 1, DP); true -> 0 end) + 1,
        if Cand > Acc -> Cand; true -> Acc end
    end, Prev, Starts),
    DP1 = array:set(R, MaxVal, DP),
    dp_loop(R + 1, N, PalMap, DP1).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_palindromes(s :: String.t(), k :: integer) :: integer
  def max_palindromes(s, k) do
    n = String.length(s)
    chars = s |> String.to_charlist() |> List.to_tuple()
    dp0 = :array.new(n, default: 0)

    # odd length palindromes
    dp1 =
      Enum.reduce(0..(n - 1), dp0, fn i, acc ->
        expand(chars, n, k, i, i, acc)
      end)

    # even length palindromes
    dp2 =
      if n >= 2 do
        Enum.reduce(0..(n - 2), dp1, fn i, acc ->
          expand(chars, n, k, i, i + 1, acc)
        end)
      else
        dp1
      end

    # propagate maximum forward to ensure non‑overlapping selection
    dp_final =
      Enum.reduce(1..(n - 1), dp2, fn idx, acc ->
        prev = :array.get(idx - 1, acc)
        cur = :array.get(idx, acc)

        if prev > cur do
          :array.set(idx, prev, acc)
        else
          acc
        end
      end)

    :array.get(n - 1, dp_final)
  end

  defp expand(chars, n, k, l0, r0, dp) do
    do_expand(chars, n, k, l0, r0, dp)
  end

  defp do_expand(_chars, _n, _k, l, r, dp) when l < 0 or r >= _n, do: dp

  defp do_expand(chars, n, k, l, r, dp) do
    if elem(chars, l) == elem(chars, r) do
      new_dp =
        if (r - l + 1) >= k do
          prev = if l > 0, do: :array.get(l - 1, dp), else: 0
          cand = prev + 1
          cur = :array.get(r, dp)

          if cand > cur do
            :array.set(r, cand, dp)
          else
            dp
          end
        else
          dp
        end

      do_expand(chars, n, k, l - 1, r + 1, new_dp)
    else
      dp
    end
  end
end
```
