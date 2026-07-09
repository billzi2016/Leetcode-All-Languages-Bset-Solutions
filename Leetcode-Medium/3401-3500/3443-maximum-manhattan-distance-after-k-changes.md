# 3443. Maximum Manhattan Distance After K Changes

## Cpp

```cpp
class Solution {
public:
    int maxDistance(string s, int k) {
        int cntN = 0, cntS = 0, cntE = 0, cntW = 0;
        int ans = 0;
        for (int i = 0; i < (int)s.size(); ++i) {
            char ch = s[i];
            if (ch == 'N') ++cntN;
            else if (ch == 'S') ++cntS;
            else if (ch == 'E') ++cntE;
            else if (ch == 'W') ++cntW;
            
            int diff = abs(cntN - cntS) + abs(cntE - cntW);
            int minorityVert = min(cntN, cntS);
            int minorityHor  = min(cntE, cntW);
            int inc = 2 * min(k, minorityVert + minorityHor);
            int cur = diff + inc;
            if (cur > i + 1) cur = i + 1; // cannot exceed steps taken
            ans = max(ans, cur);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxDistance(String s, int k) {
        int cntN = 0, cntS = 0, cntE = 0, cntW = 0;
        int ans = 0;
        int n = s.length();
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == 'N') cntN++;
            else if (c == 'S') cntS++;
            else if (c == 'E') cntE++;
            else if (c == 'W') cntW++;
            
            int verticalDiff = Math.abs(cntN - cntS);
            int horizontalDiff = Math.abs(cntE - cntW);
            int originalDist = verticalDiff + horizontalDiff;
            
            int convertible = Math.min(cntN, cntS) + Math.min(cntE, cntW);
            int inc = 2 * Math.min(k, convertible);
            int candidate = originalDist + inc;
            if (candidate > i + 1) candidate = i + 1; // cannot exceed steps taken
            if (candidate > ans) ans = candidate;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxDistance(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cntN = cntS = cntE = cntW = 0
        ans = 0
        for i, ch in enumerate(s, 1):
            if ch == 'N':
                cntN += 1
            elif ch == 'S':
                cntS += 1
            elif ch == 'E':
                cntE += 1
            else:  # 'W'
                cntW += 1

            cur = abs(cntN - cntS) + abs(cntE - cntW)
            minorities = min(cntN, cntS) + min(cntE, cntW)
            add = 2 * min(k, minorities)
            possible = cur + add
            if possible > i:
                possible = i
            if possible > ans:
                ans = possible
        return ans
```

## Python3

```python
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        n_cnt = s_cnt = e_cnt = w_cnt = 0
        ans = 0
        for ch in s:
            if ch == 'N':
                n_cnt += 1
            elif ch == 'S':
                s_cnt += 1
            elif ch == 'E':
                e_cnt += 1
            else:  # 'W'
                w_cnt += 1

            diff_v = abs(n_cnt - s_cnt)
            diff_h = abs(e_cnt - w_cnt)

            bad_v = min(n_cnt, s_cnt)
            bad_h = min(e_cnt, w_cnt)
            total_bad = bad_v + bad_h

            inc = 2 * (k if k < total_bad else total_bad)
            cur = diff_v + diff_h + inc
            if cur > ans:
                ans = cur
        return ans
```

## C

```c
#include <string.h>

int maxDistance(char* s, int k) {
    int n = strlen(s);
    int ans = 0;
    int signs[2] = {1, -1};
    for (int si = 0; si < 2; ++si) {
        int sx = signs[si];
        for (int sj = 0; sj < 2; ++sj) {
            int sy = signs[sj];
            int cur = 0;
            int cnt1 = 0, cnt2 = 0;
            for (int i = 0; i < n; ++i) {
                char c = s[i];
                int v;
                if (c == 'N') v = sy;
                else if (c == 'S') v = -sy;
                else if (c == 'E') v = sx;
                else /* W */ v = -sx;

                cur += v;

                if (v == 0) ++cnt1;
                else if (v == -1) ++cnt2; // gain of 2

                int use2 = cnt2 < k ? cnt2 : k;
                int remaining = k - use2;
                int use1 = cnt1 < remaining ? cnt1 : remaining;
                int best_gain = use2 * 2 + use1;

                int total = cur + best_gain;
                if (total > ans) ans = total;
            }
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxDistance(string s, int k) {
        int n = s.Length;
        int best = 0;
        // Quadrant definitions: each as a pair of allowed characters
        char[][] allowed = new char[4][];
        allowed[0] = new char[] { 'N', 'E' }; // NE
        allowed[1] = new char[] { 'N', 'W' }; // NW
        allowed[2] = new char[] { 'S', 'E' }; // SE
        allowed[3] = new char[] { 'S', 'W' }; // SW

        for (int q = 0; q < 4; ++q) {
            int bad = 0;
            int i = 0;
            for (; i < n; ++i) {
                char c = s[i];
                if (c != allowed[q][0] && c != allowed[q][1]) {
                    bad++;
                    if (bad > k) break;
                }
            }
            // i is the length of longest prefix where bad <= k
            best = Math.Max(best, i);
        }

        return best;
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
var maxDistance = function(s, k) {
    const n = s.length;
    // quadrants: [signX, signY] where +1 means East/North, -1 means West/South
    const quads = [
        [1, 1],
        [1, -1],
        [-1, 1],
        [-1, -1]
    ];
    let answer = 0;
    for (const [sx, sy] of quads) {
        let curSum = 0;      // original sum up to current prefix
        let badCnt = 0;      // number of -1 contributions up to current prefix
        let best = 0;
        for (let i = 0; i < n; ++i) {
            const ch = s.charAt(i);
            let val;
            if (ch === 'N') {
                val = sy === 1 ? 1 : -1;
            } else if (ch === 'S') {
                val = sy === -1 ? 1 : -1;
            } else if (ch === 'E') {
                val = sx === 1 ? 1 : -1;
            } else { // 'W'
                val = sx === -1 ? 1 : -1;
            }
            curSum += val;
            if (val === -1) badCnt++;
            const possible = curSum + 2 * Math.min(k, badCnt);
            if (possible > best) best = possible;
        }
        // also consider distance 0 before any move
        answer = Math.max(answer, best);
    }
    return answer;
};
```

## Typescript

```typescript
function maxDistance(s: string, k: number): number {
    let north = 0, south = 0, east = 0, west = 0;
    let best = 0;
    for (const ch of s) {
        if (ch === 'N') north++;
        else if (ch === 'S') south++;
        else if (ch === 'E') east++;
        else if (ch === 'W') west++;

        const base = Math.abs(north - south) + Math.abs(east - west);
        const opposite = Math.min(north, south) + Math.min(east, west);
        const cur = base + 2 * Math.min(k, opposite);
        if (cur > best) best = cur;
    }
    return best;
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
    function maxDistance($s, $k) {
        $len = strlen($s);
        $nCnt = $sCnt = $eCnt = $wCnt = 0;
        $ans = 0;
        for ($i = 0; $i < $len; ++$i) {
            $ch = $s[$i];
            if ($ch === 'N') {
                ++$nCnt;
            } elseif ($ch === 'S') {
                ++$sCnt;
            } elseif ($ch === 'E') {
                ++$eCnt;
            } else { // 'W'
                ++$wCnt;
            }
            $vertical = abs($nCnt - $sCnt);
            $horizontal = abs($eCnt - $wCnt);
            $orig = $vertical + $horizontal;
            $beneficial = min($nCnt, $sCnt) + min($eCnt, $wCnt);
            $c = min($k, $i + 1);
            $add = 2 * min($c, $beneficial);
            $dist = $orig + $add;
            if ($dist > $ans) {
                $ans = $dist;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxDistance(_ s: String, _ k: Int) -> Int {
        var cntN = 0, cntS = 0, cntE = 0, cntW = 0
        var answer = 0
        var index = 0
        for ch in s {
            index += 1
            switch ch {
            case "N":
                cntN += 1
            case "S":
                cntS += 1
            case "E":
                cntE += 1
            case "W":
                cntW += 1
            default:
                break
            }
            let verticalLess = min(cntN, cntS)
            let horizontalLess = min(cntE, cntW)
            let lessTotal = verticalLess + horizontalLess
            let dist = abs(cntN - cntS) + abs(cntE - cntW)
            let increase = 2 * min(k, lessTotal)
            var candidate = dist + increase
            if candidate > index { candidate = index }
            if candidate > answer { answer = candidate }
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxDistance(s: String, k: Int): Int {
        var north = 0
        var south = 0
        var east = 0
        var west = 0
        var best = 0
        for (ch in s) {
            when (ch) {
                'N' -> north++
                'S' -> south++
                'E' -> east++
                'W' -> west++
            }
            val verticalDiff = kotlin.math.abs(north - south)
            val horizontalDiff = kotlin.math.abs(east - west)
            val availableChanges = kotlin.math.min(north, south) + kotlin.math.min(east, west)
            val extra = 2 * kotlin.math.min(k, availableChanges)
            val cur = verticalDiff + horizontalDiff + extra
            if (cur > best) best = cur
        }
        return best
    }
}
```

## Dart

```dart
class Solution {
  int maxDistance(String s, int k) {
    int nCount = 0, sCount = 0, eCount = 0, wCount = 0;
    int ans = 0;
    for (int i = 0; i < s.length; i++) {
      switch (s[i]) {
        case 'N':
          nCount++;
          break;
        case 'S':
          sCount++;
          break;
        case 'E':
          eCount++;
          break;
        case 'W':
          wCount++;
          break;
      }
      // (+x,+y)
      int base = (nCount - sCount) + (eCount - wCount);
      int bad = sCount + wCount;
      int dist = base + 2 * (k < bad ? k : bad);
      if (dist > ans) ans = dist;

      // (+x,-y)
      base = (sCount - nCount) + (eCount - wCount);
      bad = nCount + wCount;
      dist = base + 2 * (k < bad ? k : bad);
      if (dist > ans) ans = dist;

      // (-x,+y)
      base = (nCount - sCount) + (wCount - eCount);
      bad = sCount + eCount;
      dist = base + 2 * (k < bad ? k : bad);
      if (dist > ans) ans = dist;

      // (-x,-y)
      base = (sCount - nCount) + (wCount - eCount);
      bad = nCount + eCount;
      dist = base + 2 * (k < bad ? k : bad);
      if (dist > ans) ans = dist;
    }
    return ans;
  }
}
```

## Golang

```go
func maxDistance(s string, k int) int {
    n := len(s)
    cntN, cntS, cntE, cntW := 0, 0, 0, 0
    ans := 0

    max := func(a, b int) int {
        if a > b {
            return a
        }
        return b
    }

    for i, ch := range s {
        switch ch {
        case 'N':
            cntN++
        case 'S':
            cntS++
        case 'E':
            cntE++
        case 'W':
            cntW++
        }
        idx := i + 1 // current prefix length

        oppNE := cntS + cntW
        d := idx - 2*max(0, oppNE-k)
        if d > ans {
            ans = d
        }

        oppNW := cntS + cntE
        d = idx - 2*max(0, oppNW-k)
        if d > ans {
            ans = d
        }

        oppSE := cntN + cntW
        d = idx - 2*max(0, oppSE-k)
        if d > ans {
            ans = d
        }

        oppSW := cntN + cntE
        d = idx - 2*max(0, oppSW-k)
        if d > ans {
            ans = d
        }
    }
    return ans
}
```

## Ruby

```ruby
def max_distance(s, k)
  cnt_n = cnt_s = cnt_e = cnt_w = 0
  best = 0
  i = 0
  s.each_char do |ch|
    i += 1
    case ch
    when 'N' then cnt_n += 1
    when 'S' then cnt_s += 1
    when 'E' then cnt_e += 1
    when 'W' then cnt_w += 1
    end

    vertical = (cnt_n - cnt_s).abs
    horizontal = (cnt_e - cnt_w).abs
    cur = vertical + horizontal

    less = [cnt_n, cnt_s].min + [cnt_e, cnt_w].min
    add = 2 * (k <= less ? k : less)

    possible = cur + add
    cand = i < possible ? i : possible
    best = cand if cand > best
  end
  best
end
```

## Scala

```scala
object Solution {
    def maxDistance(s: String, k: Int): Int = {
        var cntN = 0
        var cntS = 0
        var cntE = 0
        var cntW = 0
        var ans = 0
        val kk = k
        var i = 0
        while (i < s.length) {
            s.charAt(i) match {
                case 'N' => cntN += 1
                case 'S' => cntS += 1
                case 'E' => cntE += 1
                case 'W' => cntW += 1
                case _   =>
            }
            val idx = i + 1
            val verticalDiff = math.abs(cntN - cntS)
            val horizDiff = math.abs(cntE - cntW)
            val origDist = verticalDiff + horizDiff
            val lessV = math.min(cntN, cntS)
            val lessH = math.min(cntE, cntW)
            val totalLess = lessV + lessH
            val inc = 2 * math.min(kk, totalLess)
            var cur = origDist + inc
            if (cur > idx) cur = idx
            if (cur > ans) ans = cur
            i += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_distance(s: String, k: i32) -> i32 {
        let mut n = 0i32;
        let mut s_cnt = 0i32;
        let mut e = 0i32;
        let mut w = 0i32;
        let mut ans: i64 = 0;
        let kk = k as i64;

        for ch in s.bytes() {
            match ch {
                b'N' => n += 1,
                b'S' => s_cnt += 1,
                b'E' => e += 1,
                b'W' => w += 1,
                _ => {}
            }
            let diff = (n - s_cnt).abs() as i64 + (e - w).abs() as i64;
            let minority = std::cmp::min(n, s_cnt) as i64 + std::cmp::min(e, w) as i64;
            let add = 2 * std::cmp::min(kk, minority);
            let cur = diff + add;
            if cur > ans {
                ans = cur;
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (max-distance s k)
  (-> string? exact-integer? exact-integer?)
  (let* ((len (string-length s))
         (n 0)          ; count of 'N'
         (sCnt 0)       ; count of 'S'
         (e 0)          ; count of 'E'
         (w 0)          ; count of 'W'
         (rem k)
         (maxd 0))
    (for ([i (in-range len)])
      (define ch (string-ref s i))
      (cond
        [(char=? ch #\N)
         (if (and (> rem 0) (> sCnt n))
             (begin (set! sCnt (+ sCnt 1)) (set! rem (- rem 1)))
             (set! n (+ n 1)))]
        [(char=? ch #\S)
         (if (and (> rem 0) (> n sCnt))
             (begin (set! n (+ n 1)) (set! rem (- rem 1))) ; flip to 'N'
             (set! sCnt (+ sCnt 1)))]
        [(char=? ch #\E)
         (if (and (> rem 0) (> w e))
             (begin (set! w (+ w 1)) (set! rem (- rem 1)))
             (set! e (+ e 1)))]
        [(char=? ch #\W)
         (if (and (> rem 0) (> e w))
             (begin (set! e (+ e 1)) (set! rem (- rem 1))) ; flip to 'E'
             (set! w (+ w 1)))])
      (define dist (+ (abs (- n sCnt)) (abs (- e w))))
      (when (> dist maxd) (set! maxd dist)))
    maxd))
```

## Erlang

```erlang
-module(solution).
-export([max_distance/2]).

-spec max_distance(S :: unicode:unicode_binary(), K :: integer()) -> integer().
max_distance(S, K) ->
    max_distance_loop(S, K, 0, 0, 0, 0).

max_distance_loop(<<>>, _K, _I, _X, _Y, Max) ->
    Max;
max_distance_loop(<<Char, Rest/binary>>, K, I, X, Y, Max) ->
    {NX, NY} =
        case Char of
            $N -> {X, Y + 1};
            $S -> {X, Y - 1};
            $E -> {X + 1, Y};
            $W -> {X - 1, Y}
        end,
    NewI = I + 1,
    Base = erlang:abs(NX) + erlang:abs(NY),
    Cand = erlang:min(NewI, Base + 2 * K),
    NewMax = erlang:max(Max, Cand),
    max_distance_loop(Rest, K, NewI, NX, NY, NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_distance(String.t(), integer) :: integer
  def max_distance(s, k) do
    {max_len, _} =
      s
      |> String.graphemes()
      |> Enum.with_index(1)
      |> Enum.reduce({0, %{n: 0, s: 0, e: 0, w: 0}}, fn {ch, idx}, {best, cnts} ->
        cnts = update_counts(cnts, ch)

        incompatibles =
          [
            cnts.w + cnts.s,
            cnts.w + cnts.n,
            cnts.e + cnts.s,
            cnts.e + cnts.n
          ]
          |> Enum.min()

        new_best = if incompatibles <= k, do: idx, else: best
        {new_best, cnts}
      end)

    max_len
  end

  defp update_counts(cnts, "N"), do: %{cnts | n: cnts.n + 1}
  defp update_counts(cnts, "S"), do: %{cnts | s: cnts.s + 1}
  defp update_counts(cnts, "E"), do: %{cnts | e: cnts.e + 1}
  defp update_counts(cnts, "W"), do: %{cnts | w: cnts.w + 1}
end
```
