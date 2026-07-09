# 3031. Minimum Time to Revert Word to Initial State II

## Cpp

```cpp
class Solution {
public:
    int minimumTimeToInitialState(string word, int k) {
        int n = word.size();
        vector<int> pi(n);
        for (int i = 1; i < n; ++i) {
            int j = pi[i - 1];
            while (j > 0 && word[i] != word[j]) j = pi[j - 1];
            if (word[i] == word[j]) ++j;
            pi[i] = j;
        }
        int ans = (n + k - 1) / k; // ceil division
        int L = pi[n - 1];
        while (L > 0) {
            if ((n - L) % k == 0) {
                ans = min(ans, (n - L) / k);
                break; // largest suitable border found
            }
            L = pi[L - 1];
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumTimeToInitialState(String word, int k) {
        int n = word.length();
        // compute prefix function (KMP)
        int[] pi = new int[n];
        for (int i = 1; i < n; i++) {
            int j = pi[i - 1];
            while (j > 0 && word.charAt(i) != word.charAt(j)) {
                j = pi[j - 1];
            }
            if (word.charAt(i) == word.charAt(j)) {
                j++;
            }
            pi[i] = j;
        }

        boolean[] goodShift = new boolean[n];
        goodShift[0] = true; // shift 0 always works
        int l = pi[n - 1];
        while (l > 0) {
            int shift = n - l; // (n - border length) % n
            if (shift == n) shift = 0;
            goodShift[shift] = true;
            l = pi[l - 1];
        }

        int g = gcd(n, k);
        int period = n / g; // number of distinct residues
        int cur = k % n;
        for (int t = 1; t <= period; t++) {
            if (goodShift[cur]) return t;
            cur += k;
            if (cur >= n) cur -= n;
        }
        // Should never reach here because shift 0 is always reachable at t=period
        return period;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int tmp = a % b;
            a = b;
            b = tmp;
        }
        return a;
    }
}
```

## Python

```python
class Solution(object):
    def minimumTimeToInitialState(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        n = len(word)
        # compute prefix function (KMP failure array)
        pi = [0] * n
        for i in range(1, n):
            j = pi[i - 1]
            while j and word[i] != word[j]:
                j = pi[j - 1]
            if word[i] == word[j]:
                j += 1
            pi[i] = j

        # mark all border lengths (including 0)
        is_border = [False] * (n + 1)
        cur = n
        while cur:
            cur = pi[cur - 1]
            is_border[cur] = True
        is_border[0] = True  # empty string is always a border

        r = 0
        for t in range(1, n + 1):
            r = (r + k) % n
            L = 0 if r == 0 else n - r
            if is_border[L]:
                return t
        # The loop should always return before reaching here
        return n // k + (1 if n % k else 0)
```

## Python3

```python
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        # compute prefix function (KMP)
        pi = [0] * n
        for i in range(1, n):
            j = pi[i - 1]
            while j > 0 and word[i] != word[j]:
                j = pi[j - 1]
            if word[i] == word[j]:
                j += 1
            pi[i] = j

        # find the longest border length L such that (n-L) % k == 0
        best_t = None
        l = pi[-1]
        while l > 0:
            if (n - l) % k == 0:
                best_t = (n - l) // k
                break
            l = pi[l - 1]

        # candidate when we need to shift completely beyond original string
        t_full = (n + k - 1) // k  # ceil(n/k)

        if best_t is None:
            return t_full
        else:
            return min(best_t, t_full)
```

## C

```c
#include <string.h>
#include <stdlib.h>

int minimumTimeToInitialState(char* word, int k) {
    int n = (int)strlen(word);
    // Compute prefix function (KMP)
    int *pi = (int*)malloc(n * sizeof(int));
    pi[0] = 0;
    for (int i = 1; i < n; ++i) {
        int j = pi[i - 1];
        while (j > 0 && word[i] != word[j]) j = pi[j - 1];
        if (word[i] == word[j]) ++j;
        pi[i] = j;
    }

    // Helper for ceil division
    int ceilDiv = (n + k - 1) / k;
    int ans = ceilDiv; // always feasible

    // Iterate over all border lengths
    int len = pi[n - 1];
    while (len > 0) {
        int diff = n - len;
        if (diff % k == 0) {
            int t = diff / k;
            if (t > 0 && t < ans) ans = t;
        }
        len = pi[len - 1];
    }

    // Also consider border length 0 when n is multiple of k
    if (n % k == 0) {
        int t = n / k;
        if (t > 0 && t < ans) ans = t;
    }

    free(pi);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumTimeToInitialState(string word, int k) {
        int n = word.Length;
        // Compute prefix function (KMP)
        int[] pi = new int[n];
        for (int i = 1; i < n; i++) {
            int j = pi[i - 1];
            while (j > 0 && word[i] != word[j]) {
                j = pi[j - 1];
            }
            if (word[i] == word[j]) j++;
            pi[i] = j;
        }

        // Traverse borders from longest to shortest
        int len = pi[n - 1]; // longest proper border
        while (len > 0) {
            if ((n - len) % k == 0) {
                return (n - len) / k;
            }
            len = pi[len - 1];
        }

        // Check the empty border (len = 0)
        if (n % k == 0) {
            return n / k;
        } else {
            // Need to shift out all original characters
            return (n + k - 1) / k; // ceil(n/k)
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @param {number} k
 * @return {number}
 */
var minimumTimeToInitialState = function(word, k) {
    const n = word.length;
    // Z-function
    const z = new Array(n).fill(0);
    for (let i = 1, l = 0, r = 0; i < n; ++i) {
        if (i <= r) z[i] = Math.min(r - i + 1, z[i - l]);
        while (i + z[i] < n && word[z[i]] === word[i + z[i]]) ++z[i];
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }

    for (let i = k; i <= n; i += k) {
        if (i === n) return i / k; // empty border always works
        const need = n - i;
        if (z[i] >= need) return i / k;
    }
    return -1;
};
```

## Typescript

```typescript
function minimumTimeToInitialState(word: string, k: number): number {
    const n = word.length;
    // Z-function
    const z = new Array<number>(n).fill(0);
    let l = 0, r = 0;
    for (let i = 1; i < n; ++i) {
        if (i <= r) z[i] = Math.min(r - i + 1, z[i - l]);
        while (i + z[i] < n && word[z[i]] === word[i + z[i]]) ++z[i];
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }

    let bestL = -1; // longest border length satisfying condition
    // consider L = 0 explicitly later
    for (let i = 1; i < n; ++i) {
        if (i + z[i] === n) { // suffix starting at i matches prefix of length n-i
            const L = n - i;
            if ((n - L) % k === 0 && L > bestL) {
                bestL = L;
            }
        }
    }
    // check L = 0 (always a border)
    if (n % k === 0 && 0 > bestL) {
        bestL = 0;
    }

    if (bestL >= 0) {
        return (n - bestL) / k;
    } else {
        return Math.ceil(n / k);
    }
}
```

## Php

```php
class Solution {

    /**
     * @param String $word
     * @param Integer $k
     * @return Integer
     */
    function minimumTimeToInitialState($word, $k) {
        $n = strlen($word);
        // build prefix function (KMP)
        $pi = array_fill(0, $n, 0);
        for ($i = 1; $i < $n; ++$i) {
            $j = $pi[$i - 1];
            while ($j > 0 && $word[$i] !== $word[$j]) {
                $j = $pi[$j - 1];
            }
            if ($word[$i] === $word[$j]) {
                ++$j;
            }
            $pi[$i] = $j;
        }

        // find the largest border length L such that (n-L) % k == 0
        $L = $pi[$n - 1];
        while ($L > 0) {
            if ((($n - $L) % $k) === 0) {
                return intdiv($n - $L, $k);
            }
            $L = $pi[$L - 1];
        }

        // check L = 0 case
        if ($n % $k === 0) {
            return intdiv($n, $k);
        }

        // otherwise need ceil(n / k) steps
        return intdiv($n + $k - 1, $k);
    }
}
```

## Swift

```swift
class Solution {
    func minimumTimeToInitialState(_ word: String, _ k: Int) -> Int {
        let bytes = Array(word.utf8)
        let n = bytes.count
        var z = [Int](repeating: 0, count: n)
        var l = 0, r = 0
        if n > 1 {
            for i in 1..<n {
                if i <= r {
                    z[i] = min(r - i + 1, z[i - l])
                }
                while i + z[i] < n && bytes[z[i]] == bytes[i + z[i]] {
                    z[i] += 1
                }
                if i + z[i] - 1 > r {
                    l = i
                    r = i + z[i] - 1
                }
            }
        }
        var ans = (n + k - 1) / k   // ceil division
        var t = 1
        while t * k < n {
            let d = t * k
            if z[d] >= n - d {
                ans = t
                break
            }
            t += 1
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumTimeToInitialState(word: String, k: Int): Int {
        val n = word.length
        // Compute prefix function (KMP)
        val pi = IntArray(n)
        for (i in 1 until n) {
            var j = pi[i - 1]
            while (j > 0 && word[i] != word[j]) {
                j = pi[j - 1]
            }
            if (word[i] == word[j]) j++
            pi[i] = j
        }

        // Mark all border lengths (including full length and empty)
        val isBorder = BooleanArray(n + 1)
        var len = n
        while (len > 0) {
            isBorder[len] = true
            len = pi[len - 1]
        }
        isBorder[0] = true

        var t = 1
        var mod = k % n
        while (true) {
            val remaining = n - mod   // length that must match as prefix=suffix
            if (isBorder[remaining]) return t
            t++
            mod += k
            if (mod >= n) mod %= n
        }
    }
}
```

## Dart

```dart
class Solution {
  int minimumTimeToInitialState(String word, int k) {
    int n = word.length;
    List<int> pi = List.filled(n, 0);
    List<int> chars = word.codeUnits;

    for (int i = 1; i < n; ++i) {
      int j = pi[i - 1];
      while (j > 0 && chars[i] != chars[j]) {
        j = pi[j - 1];
      }
      if (chars[i] == chars[j]) {
        ++j;
      }
      pi[i] = j;
    }

    int len = pi[n - 1];
    while (len > 0) {
      if ((n - len) % k == 0) {
        return (n - len) ~/ k;
      }
      len = pi[len - 1];
    }

    // No suitable border found; need enough steps to cover the whole string.
    return (n + k - 1) ~/ k;
  }
}
```

## Golang

```go
func minimumTimeToInitialState(word string, k int) int {
	n := len(word)
	pi := make([]int, n)
	for i := 1; i < n; i++ {
		j := pi[i-1]
		for j > 0 && word[i] != word[j] {
			j = pi[j-1]
		}
		if word[i] == word[j] {
			j++
		}
		pi[i] = j
	}

	// default answer: need enough steps to discard all original characters
	ans := (n + k - 1) / k // ceil(n/k)

	// traverse borders from longest to shortest
	L := pi[n-1]
	for L > 0 {
		if (n-L)%k == 0 {
			t := (n - L) / k
			if t > 0 && t < ans {
				ans = t
			}
			break // longest suitable border gives minimal time
		}
		L = pi[L-1]
	}
	return ans
}
```

## Ruby

```ruby
def minimum_time_to_initial_state(word, k)
  n = word.length
  pi = Array.new(n, 0)
  (1...n).each do |i|
    j = pi[i - 1]
    while j > 0 && word.getbyte(i) != word.getbyte(j)
      j = pi[j - 1]
    end
    j += 1 if word.getbyte(i) == word.getbyte(j)
    pi[i] = j
  end

  candidate = nil
  l = pi[n - 1]
  while l > 0
    if (n - l) % k == 0
      candidate = (n - l) / k
      break
    end
    l = pi[l - 1]
  end
  if candidate.nil? && n % k == 0
    candidate = n / k
  end

  rotation = n / n.gcd(k)
  candidate ? [candidate, rotation].min : rotation
end
```

## Scala

```scala
object Solution {
    def minimumTimeToInitialState(word: String, k: Int): Int = {
        val n = word.length
        // prefix function (KMP)
        val pi = new Array[Int](n)
        for (i <- 1 until n) {
            var j = pi(i - 1)
            while (j > 0 && word.charAt(i) != word.charAt(j)) {
                j = pi(j - 1)
            }
            if (word.charAt(i) == word.charAt(j)) j += 1
            pi(i) = j
        }

        // collect all border lengths (including 0)
        val borders = scala.collection.mutable.ArrayBuffer[Int]()
        var len = pi(n - 1)
        while (len > 0) {
            borders += len
            len = pi(len - 1)
        }
        borders += 0

        val g = gcd(k, n)
        val kDiv = k / g
        val nDiv = n / g
        val invK = modInv(kDiv, nDiv) // inverse of kDiv modulo nDiv (coprime)

        var ans = Int.MaxValue
        for (L <- borders) {
            var d = n - L
            if (d == n) d = 0               // shift amount modulo n
            if (d % g != 0) {
                // not reachable, skip
            } else {
                val dDiv = d / g
                var t = ((dDiv.toLong * invK) % nDiv).toInt
                if (t == 0) t = nDiv          // smallest positive solution
                if (t < ans) ans = t
            }
        }
        ans
    }

    private def gcd(a: Int, b: Int): Int = {
        var x = a
        var y = b
        while (y != 0) {
            val tmp = x % y
            x = y
            y = tmp
        }
        math.abs(x)
    }

    // extended Euclidean algorithm
    private def egcd(a: Int, b: Int): (Int, Long, Long) = {
        if (b == 0) (a, 1L, 0L)
        else {
            val (g, x1, y1) = egcd(b, a % b)
            (g, y1, x1 - (a / b).toLong * y1)
        }
    }

    private def modInv(a: Int, m: Int): Int = {
        val (_, x, _) = egcd(a, m)
        ((x % m + m) % m).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_time_to_initial_state(word: String, k: i32) -> i32 {
        let s = word.as_bytes();
        let n = s.len();
        let k_usize = k as usize;

        // compute prefix function (KMP pi array)
        let mut pi = vec![0usize; n];
        for i in 1..n {
            let mut j = pi[i - 1];
            while j > 0 && s[i] != s[j] {
                j = pi[j - 1];
            }
            if s[i] == s[j] {
                j += 1;
            }
            pi[i] = j;
        }

        // mark all border lengths
        let mut is_border = vec![false; n + 1];
        is_border[0] = true;
        let mut len = if n > 0 { pi[n - 1] } else { 0 };
        while len > 0 {
            is_border[len] = true;
            len = pi[len - 1];
        }

        // iterate over possible times
        let max_t = (n + k_usize - 1) / k_usize; // ceil(n/k)
        for t in 1..=max_t {
            let removed = t * k_usize;
            if removed > n {
                break;
            }
            let l = n - removed; // remaining original prefix length
            if is_border[l] {
                return t as i32;
            }
        }

        // fallback (should not reach because L=0 is always a border)
        max_t as i32
    }
}
```

## Racket

```racket
#lang racket

(provide minimum-time-to-initial-state)

(define/contract (minimum-time-to-initial-state word k)
  (-> string? exact-integer? exact-integer?)
  (let* ([n (string-length word)]
         [z (make-vector n 0)])
    ;; Z-function
    (let ([l 0] [r 0])
      (for ([i (in-range 1 n)])
        (define zi
          (if (<= i r)
              (min (+ (- r i) 1) (vector-ref z (- i l)))
              0))
        ;; extend match
        (let loop ((zval zi))
          (if (and (< (+ i zval) n)
                   (char=? (string-ref word zval)
                           (string-ref word (+ i zval))))
              (loop (+ zval 1))
              (begin
                (vector-set! z i zval)
                (when (> (+ i zval -1) r)
                  (set! l i)
                  (set! r (+ i zval -1)))))))))
    ;; minimal multiple of k satisfying border condition
    (let* ([ceil-mult (quotient (+ n k -1) k)])
      (let search ((i k))
        (cond [(>= i n) ceil-mult]
              [(>= (vector-ref z i) (- n i)) (quotient i k)]
              [else (search (+ i k))])))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_time_to_initial_state/2]).

-include_lib("kernel/include/array.hrl").

minimum_time_to_initial_state(Word, K) ->
    CharList = binary_to_list(Word),
    CharTuple = list_to_tuple(CharList),
    N = tuple_size(CharTuple),

    %% Build prefix function (pi) using array for O(1) access
    Pi0 = array:new(N, [{default, 0}]),
    PiArray = build_pi(1, 0, N, CharTuple, Pi0),

    %% Find the minimal t using borders chain
    MinT = find_min_t(N, K, PiArray),
    MinT.

build_pi(I, J, N, CharTuple, PiArr) when I < N ->
    CharI = element(I + 1, CharTuple),
    CharJ = element(J + 1, CharTuple),
    NewJ = case {J > 0, CharI =:= CharJ} of
        {true, false} ->
            %% fallback using previously computed pi values
            build_fallback(J, CharI, CharTuple, PiArr);
        _ ->
            J
    end,
    FinalJ = if CharI =:= element(NewJ + 1, CharTuple) -> NewJ + 1; true -> NewJ end,
    PiArr2 = array:set(I, FinalJ, PiArr),
    build_pi(I + 1, FinalJ, N, CharTuple, PiArr2);
build_pi(_, _, _, _, PiArr) ->
    PiArr.

%% Fallback loop to find proper border length when mismatch occurs
build_fallback(J, CharI, CharTuple, PiArr) ->
    case J of
        0 -> 0;
        _ ->
            PrevJ = array:get(J - 1, PiArr),
            CharPrevJ = element(PrevJ + 1, CharTuple),
            if CharI =:= CharPrevJ ->
                    PrevJ;
               true ->
                    build_fallback(PrevJ, CharI, CharTuple, PiArr)
            end
    end.

find_min_t(N, K, PiArr) ->
    %% Start from the longest proper border
    L0 = array:get(N - 1, PiArr),
    find_min_t_loop(N, K, PiArr, L0, undefined).

find_min_t_loop(_N, _K, _PiArr, 0, undefined) ->
    %% No suitable border found except empty; compute using L=0
    ( _N div _K ) + (if (_N rem _K) =:= 0 -> 0; true -> 1 end);
find_min_t_loop(N, K, PiArr, L, Best) when L >= 0 ->
    case ((N - L) rem K) of
        0 ->
            T = (N - L) div K,
            NewBest = case Best of
                undefined -> T;
                _ when T < Best -> T;
                _ -> Best
            end,
            NextL = if L == 0 -> 0; true -> array:get(L - 1, PiArr) end,
            find_min_t_loop(N, K, PiArr, NextL, NewBest);
        _ ->
            NextL = if L == 0 -> 0; true -> array:get(L - 1, PiArr) end,
            find_min_t_loop(N, K, PiArr, NextL, Best)
    end;
find_min_t_loop(_N, _K, _PiArr, 0, Best) ->
    %% Include the empty border case
    case Best of
        undefined -> ( _N div _K ) + (if (_N rem _K) =:= 0 -> 0; true -> 1 end);
        _ -> Best
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_time_to_initial_state(word :: String.t(), k :: integer) :: integer
  def minimum_time_to_initial_state(word, k) do
    chars = String.to_charlist(word)
    n = length(chars)
    tup = List.to_tuple(chars)

    pi = build_pi(tup, n)

    # collect all border lengths
    borders = collect_borders(pi, n - 1, [])

    # check if can revert in one second (border length == n - k)
    if Enum.any?(borders, fn l -> l == n - k end) do
      1
    else
      max_multiple =
        borders
        |> Enum.filter(fn l -> rem(l, k) == 0 end)
        |> Enum.max(fn -> 0 end)

      div((n - max_multiple + k - 1), k)
    end
  end

  defp build_pi(tup, n) do
    # initialize array with zeros
    pi = :array.new(n, default: 0)

    {_, pi_final} =
      Enum.reduce(1..(n - 1), {0, pi}, fn i, {j, arr} ->
        j = reduce_j(j, tup, i, arr)
        if elem(tup, i) == elem(tup, j) do
          j = j + 1
        end

        arr2 = :array.set(i, j, arr)
        {j, arr2}
      end)

    pi_final
  end

  defp reduce_j(j, tup, i, arr) when j > 0 and elem(tup, i) != elem(tup, j) do
    prev = :array.get(j - 1, arr)
    reduce_j(prev, tup, i, arr)
  end

  defp reduce_j(j, _tup, _i, _arr), do: j

  defp collect_borders(_pi, -1, acc), do: acc
  defp collect_borders(pi, idx, acc) when idx >= 0 do
    l = :array.get(idx, pi)
    if l > 0 do
      collect_borders(pi, l - 1, [l | acc])
    else
      acc
    end
  end
end
```
