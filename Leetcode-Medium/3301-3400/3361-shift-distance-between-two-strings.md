# 3361. Shift Distance Between Two Strings

## Cpp

```cpp
class Solution {
public:
    long long shiftDistance(string s, string t, vector<int>& nextCost, vector<int>& previousCost) {
        const int ALPH = 26;
        vector<long long> prefNext(ALPH + 1, 0), prefPrev(ALPH + 1, 0);
        for (int i = 0; i < ALPH; ++i) {
            prefNext[i + 1] = prefNext[i] + nextCost[i];
            prefPrev[i + 1] = prefPrev[i] + previousCost[i];
        }
        long long totalNext = prefNext[ALPH];
        long long totalPrev = prefPrev[ALPH];
        long long ans = 0;
        int n = s.size();
        for (int i = 0; i < n; ++i) {
            int a = s[i] - 'a';
            int b = t[i] - 'a';
            if (a == b) continue;
            // forward cost using nextCost
            long long forward;
            if (a < b) forward = prefNext[b] - prefNext[a];
            else forward = totalNext - (prefNext[a] - prefNext[b]);
            // backward cost using previousCost
            long long backward;
            if (a > b) backward = prefPrev[a + 1] - prefPrev[b + 1];
            else backward = totalPrev - (prefPrev[b + 1] - prefPrev[a + 1]);
            ans += min(forward, backward);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long shiftDistance(String s, String t, int[] nextCost, int[] previousCost) {
        final int N = 26;
        long INF = Long.MAX_VALUE / 4;
        long[][] dist = new long[N][N];
        for (int i = 0; i < N; i++) {
            Arrays.fill(dist[i], INF);
            dist[i][i] = 0;
            int nxt = (i + 1) % N;
            dist[i][nxt] = Math.min(dist[i][nxt], nextCost[i]);
            int prev = (i - 1 + N) % N;
            dist[i][prev] = Math.min(dist[i][prev], previousCost[i]);
        }
        for (int k = 0; k < N; k++) {
            for (int i = 0; i < N; i++) {
                if (dist[i][k] == INF) continue;
                long dik = dist[i][k];
                for (int j = 0; j < N; j++) {
                    long nd = dik + dist[k][j];
                    if (nd < dist[i][j]) {
                        dist[i][j] = nd;
                    }
                }
            }
        }
        long total = 0;
        int len = s.length();
        for (int idx = 0; idx < len; idx++) {
            int a = s.charAt(idx) - 'a';
            int b = t.charAt(idx) - 'a';
            total += dist[a][b];
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def shiftDistance(self, s, t, nextCost, previousCost):
        """
        :type s: str
        :type t: str
        :type nextCost: List[int]
        :type previousCost: List[int]
        :rtype: int
        """
        # prefix sums for forward (next) costs
        pref_next = [0] * 27
        for i in range(26):
            pref_next[i + 1] = pref_next[i] + nextCost[i]
        total_next = pref_next[26]

        # prefix sums for backward (previous) costs
        pref_prev = [0] * 27
        for i in range(26):
            pref_prev[i + 1] = pref_prev[i] + previousCost[i]
        total_prev = pref_prev[26]

        def forward_cost(i, j):
            if i == j:
                return 0
            if i < j:
                return pref_next[j] - pref_next[i]
            # wrap around
            return total_next - (pref_next[i] - pref_next[j])

        def backward_cost(i, j):
            if i == j:
                return 0
            if i > j:
                # sum previousCost over indices (j+1 .. i)
                return pref_prev[i + 1] - pref_prev[j + 1]
            # wrap around
            return pref_prev[i + 1] + (total_prev - pref_prev[j + 1])

        ans = 0
        for a, b in zip(s, t):
            ia = ord(a) - 97
            ib = ord(b) - 97
            ans += min(forward_cost(ia, ib), backward_cost(ia, ib))
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        # prefix sums for forward (next) costs
        pref_next = [0] * 27
        for i in range(26):
            pref_next[i + 1] = pref_next[i] + nextCost[i]
        total_next = pref_next[26]

        # prefix sums for backward (previous) costs
        pref_prev = [0] * 27
        for i in range(26):
            pref_prev[i + 1] = pref_prev[i] + previousCost[i]
        total_prev = pref_prev[26]

        def forward(i: int, j: int) -> int:
            if i <= j:
                return pref_next[j] - pref_next[i]
            # wrap around
            return total_next - (pref_next[i] - pref_next[j])

        def backward(i: int, j: int) -> int:
            if i > j:
                # indices i, i-1, ..., j+1
                return pref_prev[i + 1] - pref_prev[j + 1]
            if i < j:
                # total minus the excluded segment (i+1 .. j)
                return total_prev - (pref_prev[j + 1] - pref_prev[i + 1])
            return 0

        ans = 0
        for ch_s, ch_t in zip(s, t):
            a = ord(ch_s) - 97
            b = ord(ch_t) - 97
            if a == b:
                continue
            cost_f = forward(a, b)
            cost_b = backward(a, b)
            ans += cost_f if cost_f < cost_b else cost_b
        return ans
```

## C

```c
#include <stddef.h>

long long shiftDistance(char* s, char* t, int* nextCost, int nextCostSize, int* previousCost, int previousCostSize) {
    long long nextPref[27] = {0};
    long long prevPref[27] = {0};
    for (int i = 0; i < 26; ++i) {
        nextPref[i + 1] = nextPref[i] + (long long)nextCost[i];
        prevPref[i + 1] = prevPref[i] + (long long)previousCost[i];
    }
    long long totalNext = nextPref[26];
    long long totalPrev = prevPref[26];

    long long result = 0;
    for (int i = 0; s[i] != '\0'; ++i) {
        int a = s[i] - 'a';
        int b = t[i] - 'a';
        if (a == b) continue;

        // forward (next) cost
        long long fwd;
        if (a <= b) {
            fwd = nextPref[b] - nextPref[a];
        } else {
            fwd = (totalNext - nextPref[a]) + nextPref[b];
        }

        // backward (previous) cost
        long long bwd;
        if (a >= b) {
            bwd = prevPref[a + 1] - prevPref[b + 1];
        } else {
            bwd = prevPref[a + 1] + (totalPrev - prevPref[b + 1]);
        }

        result += (fwd < bwd) ? fwd : bwd;
    }
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public long ShiftDistance(string s, string t, int[] nextCost, int[] previousCost) {
        // Prefix sums for nextCost
        long[] prefNext = new long[27];
        for (int i = 0; i < 26; i++) {
            prefNext[i + 1] = prefNext[i] + nextCost[i];
        }
        long totalNext = prefNext[26];

        // Prefix sums for previousCost
        long[] prefPrev = new long[27];
        for (int i = 0; i < 26; i++) {
            prefPrev[i + 1] = prefPrev[i] + previousCost[i];
        }
        long totalPrev = prefPrev[26];

        long answer = 0;
        int n = s.Length;
        for (int idx = 0; idx < n; idx++) {
            int a = s[idx] - 'a';
            int b = t[idx] - 'a';
            if (a == b) continue;

            // forward (next) cost
            long forward;
            if (a <= b) {
                forward = prefNext[b] - prefNext[a];
            } else {
                forward = totalNext - (prefNext[a] - prefNext[b]);
            }

            // backward (previous) cost
            long backward;
            if (a >= b) {
                backward = prefPrev[a + 1] - prefPrev[b + 1];
            } else {
                backward = totalPrev - (prefPrev[b + 1] - prefPrev[a + 1]);
            }

            answer += Math.Min(forward, backward);
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @param {number[]} nextCost
 * @param {number[]} previousCost
 * @return {number}
 */
var shiftDistance = function(s, t, nextCost, previousCost) {
    const n = s.length;
    // prefix sums for forward (next) costs
    const prefNext = new Array(27).fill(0);
    for (let i = 0; i < 26; ++i) {
        prefNext[i + 1] = prefNext[i] + nextCost[i];
    }
    // prefix sums for backward (previous) costs
    const prefPrev = new Array(27).fill(0);
    for (let i = 0; i < 26; ++i) {
        prefPrev[i + 1] = prefPrev[i] + previousCost[i];
    }
    const totalNext = prefNext[26];
    const totalPrev = prefPrev[26];

    let ans = 0;
    for (let idx = 0; idx < n; ++idx) {
        const a = s.charCodeAt(idx) - 97;
        const b = t.charCodeAt(idx) - 97;
        if (a === b) continue;

        // forward cost from a to b
        let forwardCost;
        if (a < b) {
            forwardCost = prefNext[b] - prefNext[a];
        } else {
            forwardCost = (totalNext - prefNext[a]) + prefNext[b];
        }

        // backward cost from a to b
        let backwardCost;
        if (a > b) {
            // sum previousCost[b+1 .. a]
            backwardCost = prefPrev[a + 1] - prefPrev[b + 1];
        } else {
            // wrap around: sum previousCost[0..a] + sum previousCost[b+1..25]
            backwardCost = (totalPrev - prefPrev[b + 1]) + prefPrev[a + 1];
        }

        ans += forwardCost < backwardCost ? forwardCost : backwardCost;
    }
    return ans;
};
```

## Typescript

```typescript
function shiftDistance(s: string, t: string, nextCost: number[], previousCost: number[]): number {
    const n = s.length;
    // prefix sums for nextCost
    const prefNext = new Array(27).fill(0);
    for (let i = 0; i < 26; ++i) {
        prefNext[i + 1] = prefNext[i] + nextCost[i];
    }
    const totalNext = prefNext[26];

    // prefix sums for previousCost
    const prefPrev = new Array(27).fill(0);
    for (let i = 0; i < 26; ++i) {
        prefPrev[i + 1] = prefPrev[i] + previousCost[i];
    }
    const totalPrev = prefPrev[26];

    let ans = 0;
    for (let idx = 0; idx < n; ++idx) {
        const a = s.charCodeAt(idx) - 97;
        const b = t.charCodeAt(idx) - 97;
        if (a === b) continue;

        // forward cost using nextCost
        let forward: number;
        if (a <= b) {
            forward = prefNext[b] - prefNext[a];
        } else {
            forward = totalNext - (prefNext[a] - prefNext[b]);
        }

        // backward cost using previousCost
        let backward: number;
        if (a >= b) {
            // sum previousCost from b+1 to a inclusive
            backward = prefPrev[a + 1] - prefPrev[b + 1];
        } else {
            backward = prefPrev[a + 1] + totalPrev - prefPrev[b + 1];
        }

        ans += forward < backward ? forward : backward;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @param Integer[] $nextCost
     * @param Integer[] $previousCost
     * @return Integer
     */
    function shiftDistance($s, $t, $nextCost, $previousCost) {
        $n = strlen($s);
        // Prefix sums for nextCost
        $prefNext = array_fill(0, 27, 0);
        for ($i = 0; $i < 26; ++$i) {
            $prefNext[$i + 1] = $prefNext[$i] + $nextCost[$i];
        }
        // Prefix sums for previousCost
        $prefPrev = array_fill(0, 27, 0);
        for ($i = 0; $i < 26; ++$i) {
            $prefPrev[$i + 1] = $prefPrev[$i] + $previousCost[$i];
        }
        $totalPrev = $prefPrev[26];
        $ans = 0;
        for ($idx = 0; $idx < $n; ++$idx) {
            $a = ord($s[$idx]) - 97;
            $b = ord($t[$idx]) - 97;
            if ($a == $b) continue;

            // forward cost using nextCost
            if ($a < $b) {
                $forward = $prefNext[$b] - $prefNext[$a];
            } else {
                $forward = ($prefNext[26] - $prefNext[$a]) + $prefNext[$b];
            }

            // sum of previousCost on the forward path (a, b]
            if ($a < $b) {
                $sumFwdPrev = $prefPrev[$b + 1] - $prefPrev[$a + 1];
            } else { // a > b
                $sumFwdPrev = ($prefPrev[26] - $prefPrev[$a + 1]) + $prefPrev[$b + 1];
            }
            // backward cost using previousCost
            $backward = $totalPrev - $sumFwdPrev;

            $ans += min($forward, $backward);
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func shiftDistance(_ s: String, _ t: String, _ nextCost: [Int], _ previousCost: [Int]) -> Int {
        // Prefix sums for nextCost
        var prefNext = [Int64](repeating: 0, count: 27)
        for i in 0..<26 {
            prefNext[i + 1] = prefNext[i] + Int64(nextCost[i])
        }
        let totalNext = prefNext[26]
        
        // Prefix sums for previousCost
        var prefPrev = [Int64](repeating: 0, count: 27)
        for i in 0..<26 {
            prefPrev[i + 1] = prefPrev[i] + Int64(previousCost[i])
        }
        let totalPrev = prefPrev[26]
        
        // Helper closures
        func forward(_ from: Int, _ to: Int) -> Int64 {
            if from <= to {
                return prefNext[to] - prefNext[from]
            } else {
                return totalNext - (prefNext[from] - prefNext[to])
            }
        }
        
        func backward(_ from: Int, _ to: Int) -> Int64 {
            if from >= to {
                // sum previousCost[x] for x in (to+1)...from
                return prefPrev[from + 1] - prefPrev[to + 1]
            } else {
                // wrap around
                return prefPrev[from + 1] + totalPrev - prefPrev[to + 1]
            }
        }
        
        let sBytes = Array(s.utf8)
        let tBytes = Array(t.utf8)
        var result: Int64 = 0
        
        for i in 0..<sBytes.count {
            let a = Int(sBytes[i] - 97)   // 'a' ascii is 97
            let b = Int(tBytes[i] - 97)
            if a == b { continue }
            let costForward = forward(a, b)
            let costBackward = backward(a, b)
            result += min(costForward, costBackward)
        }
        
        return Int(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shiftDistance(s: String, t: String, nextCost: IntArray, previousCost: IntArray): Long {
        val n = s.length
        // Prefix sums for nextCost and previousCost (as Long)
        val nextPref = LongArray(27)
        val prevPref = LongArray(27)
        for (i in 0 until 26) {
            nextPref[i + 1] = nextPref[i] + nextCost[i].toLong()
            prevPref[i + 1] = prevPref[i] + previousCost[i].toLong()
        }
        val totalNext = nextPref[26]
        val totalPrev = prevPref[26]

        var result = 0L
        for (idx in 0 until n) {
            val a = s[idx] - 'a'
            val b = t[idx] - 'a'
            if (a == b) continue

            // forward cost (using nextCost)
            val forward = if (a <= b) {
                nextPref[b] - nextPref[a]
            } else {
                (totalNext - nextPref[a]) + nextPref[b]
            }

            // backward cost (using previousCost)
            val backward = if (a >= b) {
                prevPref[a + 1] - prevPref[b + 1]
            } else {
                prevPref[a + 1] + (totalPrev - prevPref[b + 1])
            }

            result += if (forward < backward) forward else backward
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int shiftDistance(String s, String t, List<int> nextCost, List<int> previousCost) {
    // Prefix sums for nextCost
    List<int> prefNext = List.filled(27, 0);
    for (int i = 0; i < 26; ++i) {
      prefNext[i + 1] = prefNext[i] + nextCost[i];
    }
    // Prefix sums for previousCost
    List<int> prefPrev = List.filled(27, 0);
    for (int i = 0; i < 26; ++i) {
      prefPrev[i + 1] = prefPrev[i] + previousCost[i];
    }

    int total = 0;
    int n = s.length;
    for (int k = 0; k < n; ++k) {
      int a = s.codeUnitAt(k) - 97;
      int b = t.codeUnitAt(k) - 97;
      if (a == b) continue;

      // forward cost using nextCost
      int forward;
      if (a < b) {
        forward = prefNext[b] - prefNext[a];
      } else {
        forward = (prefNext[26] - prefNext[a]) + prefNext[b];
      }

      // backward cost using previousCost
      int backward;
      if (a > b) {
        // sum previousCost from b+1 to a inclusive
        backward = prefPrev[a + 1] - prefPrev[b + 1];
      } else {
        // wrap around
        backward = (prefPrev[26] - prefPrev[b + 1]) + (prefPrev[a + 1] - prefPrev[0]);
      }

      total += forward < backward ? forward : backward;
    }
    return total;
  }
}
```

## Golang

```go
func shiftDistance(s string, t string, nextCost []int, previousCost []int) int64 {
    n := len(s)
    var total int64
    for i := 0; i < n; i++ {
        a := s[i] - 'a'
        b := t[i] - 'a'
        if a == b {
            continue
        }
        // forward (next) cost
        var f int64
        cur := a
        for cur != b {
            f += int64(nextCost[cur])
            cur = (cur + 1) % 26
        }
        // backward (previous) cost
        var bk int64
        cur = a
        for cur != b {
            bk += int64(previousCost[cur])
            cur = (cur - 1 + 26) % 26
        }
        if f < bk {
            total += f
        } else {
            total += bk
        }
    }
    return total
}
```

## Ruby

```ruby
def shift_distance(s, t, next_cost, previous_cost)
  n = s.length
  # Prefix sums for next and previous costs
  next_prefix = Array.new(27, 0)
  prev_prefix = Array.new(27, 0)
  26.times do |i|
    next_prefix[i + 1] = next_prefix[i] + next_cost[i]
    prev_prefix[i + 1] = prev_prefix[i] + previous_cost[i]
  end
  total_next = next_prefix[26]
  total_prev = prev_prefix[26]

  ans = 0
  n.times do |idx|
    i = s.getbyte(idx) - 97
    j = t.getbyte(idx) - 97
    next if i == j

    # forward (next) cost from i to j
    forward = if i < j
                next_prefix[j] - next_prefix[i]
              else
                total_next - (next_prefix[i] - next_prefix[j])
              end

    # backward (previous) cost from i to j
    backward = if i > j
                 prev_prefix[i + 1] - prev_prefix[j + 1]
               else
                 total_prev - (prev_prefix[j + 1] - prev_prefix[i + 1])
               end

    ans += forward < backward ? forward : backward
  end
  ans
end
```

## Scala

```scala
object Solution {
    def shiftDistance(s: String, t: String, nextCost: Array[Int], previousCost: Array[Int]): Long = {
        val f = new Array[Long](27)
        var i = 0
        while (i < 26) {
            f(i + 1) = f(i) + nextCost(i).toLong
            i += 1
        }
        val totalF = f(26)

        val p = new Array[Long](27)
        i = 0
        while (i < 26) {
            p(i + 1) = p(i) + previousCost(i).toLong
            i += 1
        }
        val totalP = p(26)

        var ans: Long = 0L
        var idx = 0
        val n = s.length
        while (idx < n) {
            val a = s.charAt(idx) - 'a'
            val b = t.charAt(idx) - 'a'
            if (a != b) {
                val forwardCost: Long =
                    if (a <= b) f(b) - f(a)
                    else totalF + f(b) - f(a)

                val backwardCost: Long =
                    if (a >= b) p(a + 1) - p(b + 1)
                    else totalP + p(a + 1) - p(b + 1)

                ans += math.min(forwardCost, backwardCost)
            }
            idx += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn shift_distance(s: String, t: String, next_cost: Vec<i32>, previous_cost: Vec<i32>) -> i64 {
        // Prefix sums for forward (next) costs
        let mut pref_next = vec![0i64; 27];
        for i in 0..26 {
            pref_next[i + 1] = pref_next[i] + next_cost[i] as i64;
        }
        // Prefix sums for backward (previous) costs
        let mut pref_prev = vec![0i64; 27];
        for i in 0..26 {
            pref_prev[i + 1] = pref_prev[i] + previous_cost[i] as i64;
        }
        let total_prev = pref_prev[26];

        let s_bytes = s.as_bytes();
        let t_bytes = t.as_bytes();
        let n = s_bytes.len();

        let mut ans: i64 = 0;
        for idx in 0..n {
            let a = (s_bytes[idx] - b'a') as usize;
            let b = (t_bytes[idx] - b'a') as usize;
            if a == b {
                continue;
            }
            // forward cost (using next_cost)
            let forward = if a < b {
                pref_next[b] - pref_next[a]
            } else {
                pref_next[26] - pref_next[a] + pref_next[b]
            };
            // backward cost (using previous_cost)
            let backward = if a > b {
                pref_prev[a + 1] - pref_prev[b + 1]
            } else {
                (total_prev - pref_prev[b + 1]) + pref_prev[a + 1]
            };
            ans += forward.min(backward);
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (shift-distance s t nextCost previousCost)
  (-> string? string? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((n (string-length s))
         ;; distance matrix 26 x 26
         (dist (make-vector 26)))
    ;; initialize rows
    (for ([i (in-range 26)])
      (vector-set! dist i (make-vector 26)))
    ;; helper to compute forward cost from i to j
    (define (forward-cost i j)
      (let loop ((k i) (sum 0))
        (if (= k j)
            sum
            (loop (modulo (+ k 1) 26)
                  (+ sum (list-ref nextCost k))))))
    ;; helper to compute backward cost from i to j
    (define (backward-cost i j)
      (let loop ((k i) (sum 0))
        (if (= k j)
            sum
            (loop (modulo (- k 1) 26)
                  (+ sum (list-ref previousCost k))))))
    ;; fill distance matrix with minimal costs
    (for ([i (in-range 26)])
      (for ([j (in-range 26)])
        (let* ((f (forward-cost i j))
               (b (backward-cost i j))
               (c (if (< f b) f b)))
          (vector-set! (vector-ref dist i) j c))))
    ;; accumulate total cost over all positions
    (let ((total 0))
      (for ([idx (in-range n)])
        (define a-index (- (char->integer (string-ref s idx))
                           (char->integer #\a)))
        (define b-index (- (char->integer (string-ref t idx))
                           (char->integer #\a)))
        (set! total (+ total
                       (vector-ref (vector-ref dist a-index) b-index))))
      total)))
```

## Erlang

```erlang
-module(solution).
-export([shift_distance/4]).

shift_distance(S, T, NextCost, PreviousCost) ->
    PrefNext = list_to_tuple(prefix(NextCost)),
    PrefPrev = list_to_tuple(prefix(PreviousCost)),
    Slist = binary_to_list(S),
    Tlist = binary_to_list(T),
    calc(Slist, Tlist, 0, PrefNext, PrefPrev).

calc([], [], Acc, _PrefNext, _PrefPrev) ->
    Acc;
calc([Sc|Ss], [Tc|Ts], Acc, PrefNext, PrefPrev) ->
    I = Sc - $a,
    J = Tc - $a,
    F = forward_cost(I, J, PrefNext),
    B = backward_cost(I, J, PrefPrev),
    Cost = if F < B -> F; true -> B end,
    calc(Ss, Ts, Acc + Cost, PrefNext, PrefPrev).

forward_cost(I, J, Pref) ->
    case I == J of
        true -> 0;
        false ->
            case I < J of
                true ->
                    element(J+1, Pref) - element(I+1, Pref);
                false ->
                    Total = element(27, Pref),
                    (Total - element(I+1, Pref)) + element(J+1, Pref)
            end
    end.

backward_cost(I, J, Pref) ->
    case I == J of
        true -> 0;
        false ->
            case I > J of
                true ->
                    element(I+1, Pref) - element(J+1, Pref);
                false ->
                    Total = element(27, Pref),
                    (Total - element(J+1, Pref)) + element(I+1, Pref)
            end
    end.

prefix(Costs) -> prefix(Costs, 0, []).

prefix([], Acc, AccList) ->
    lists:reverse([Acc | AccList]);
prefix([H|T], Acc, AccList) ->
    NewAcc = Acc + H,
    prefix(T, NewAcc, [Acc | AccList]).
```

## Elixir

```elixir
defmodule Solution do
  @spec shift_distance(String.t(), String.t(), [integer()], [integer()]) :: integer()
  def shift_distance(s, t, next_cost, previous_cost) do
    # prefix sums for nextCost (forward direction)
    nxt_ps = [0 | Enum.scan(next_cost, 0, fn x, acc -> acc + x end)]
    total_next = List.last(nxt_ps)
    nxt_ps = List.to_tuple(nxt_ps)

    # prefix sums for previousCost (backward direction)
    prev_ps = [0 | Enum.scan(previous_cost, 0, fn x, acc -> acc + x end)]
    total_prev = List.last(prev_ps)
    prev_ps = List.to_tuple(prev_ps)

    s_codes = String.to_charlist(s)
    t_codes = String.to_charlist(t)

    Enum.zip(s_codes, t_codes)
    |> Enum.reduce(0, fn {sc, tc}, acc ->
      i = sc - ?a
      j = tc - ?a

      forward =
        if i <= j do
          elem(nxt_ps, j) - elem(nxt_ps, i)
        else
          total_next - (elem(nxt_ps, i) - elem(nxt_ps, j))
        end

      backward =
        if i >= j do
          elem(prev_ps, i + 1) - elem(prev_ps, j + 1)
        else
          (elem(prev_ps, i + 1) - elem(prev_ps, 0)) +
            (total_prev - elem(prev_ps, j + 1))
        end

      acc + min(forward, backward)
    end)
  end
end
```
