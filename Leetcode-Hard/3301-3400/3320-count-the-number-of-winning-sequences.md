# 3320. Count The Number of Winning Sequences

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countWinningSequences(string s) {
        const int MOD = 1'000'000'007;
        int n = s.size();
        int offset = n;                     // to shift diff from [-n, n] to [0, 2n]
        vector<array<int,3>> dpPrev(2*n+1), dpCurr(2*n+1);
        auto idx = [&](char c)->int{
            if (c=='F') return 0;
            if (c=='W') return 1;
            return 2; // 'E'
        };
        auto outcome = [&](char bob, char alice)->int{
            if (bob == alice) return 0;
            if ((bob=='W' && alice=='F') ||
                (bob=='F' && alice=='E') ||
                (bob=='E' && alice=='W')) return 1; // bob wins
            return -1; // bob loses
        };
        // initialization for first round
        for (char cur : {'F','W','E'}) {
            int d = outcome(cur, s[0]);
            dpPrev[d + offset][idx(cur)] = (dpPrev[d + offset][idx(cur)] + 1) % MOD;
        }
        // process remaining rounds
        for (int i = 1; i < n; ++i) {
            for (auto &arr : dpCurr) arr.fill(0);
            for (int diff = -n; diff <= n; ++diff) {
                int pos = diff + offset;
                for (int last = 0; last < 3; ++last) {
                    int ways = dpPrev[pos][last];
                    if (!ways) continue;
                    char lastChar = (last==0?'F':(last==1?'W':'E'));
                    for (char cur : {'F','W','E'}) {
                        if (cur == lastChar) continue; // cannot repeat
                        int ndiff = diff + outcome(cur, s[i]);
                        int npos = ndiff + offset;
                        dpCurr[npos][idx(cur)] = (dpCurr[npos][idx(cur)] + ways) % MOD;
                    }
                }
            }
            dpPrev.swap(dpCurr);
        }
        long long ans = 0;
        for (int diff = 1; diff <= n; ++diff) { // only positive differences
            int pos = diff + offset;
            for (int last = 0; last < 3; ++last) {
                ans += dpPrev[pos][last];
                if (ans >= MOD) ans -= MOD;
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;

    public int countWinningSequences(String s) {
        int n = s.length();
        int offset = n;
        int size = 2 * n + 1; // indices for diff from -n .. n
        long[][][] dp = new long[2][size][3];
        int cur = 0, nxt = 1;

        // initialize first round
        char c0 = s.charAt(0);
        for (int k = 0; k < 3; k++) {
            int delta = score(k, c0);
            dp[cur][delta + offset][k] = 1;
        }

        // process remaining rounds
        for (int i = 1; i < n; i++) {
            // clear next layer
            for (int d = 0; d < size; d++) {
                Arrays.fill(dp[nxt][d], 0);
            }
            char ci = s.charAt(i);
            for (int diffIdx = 0; diffIdx < size; diffIdx++) {
                for (int prev = 0; prev < 3; prev++) {
                    long val = dp[cur][diffIdx][prev];
                    if (val == 0) continue;
                    for (int curMove = 0; curMove < 3; curMove++) {
                        if (curMove == prev) continue; // cannot repeat
                        int delta = score(curMove, ci);
                        int ndiffIdx = diffIdx + delta;
                        dp[nxt][ndiffIdx][curMove] += val;
                        if (dp[nxt][ndiffIdx][curMove] >= MOD) {
                            dp[nxt][ndiffIdx][curMove] -= MOD;
                        }
                    }
                }
            }
            // swap layers
            int temp = cur;
            cur = nxt;
            nxt = temp;
        }

        long ans = 0;
        for (int diffIdx = offset + 1; diffIdx < size; diffIdx++) { // diff > 0
            for (int k = 0; k < 3; k++) {
                ans += dp[cur][diffIdx][k];
                if (ans >= MOD) ans -= MOD;
            }
        }
        return (int) ans;
    }

    // bob move index: 0->F,1->W,2->E
    private int score(int bob, char aliceChar) {
        int a;
        switch (aliceChar) {
            case 'F': a = 0; break;
            case 'W': a = 1; break;
            default: a = 2; // 'E'
        }
        if (bob == a) return 0;                     // tie
        if (bob == (a + 1) % 3) return 1;           // bob beats alice
        return -1;                                  // bob loses
    }
}
```

## Python

```python
class Solution(object):
    def countWinningSequences(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(s)
        # map characters to indices 0:F, 1:W, 2:E
        mp = {'F': 0, 'W': 1, 'E': 2}
        a = [mp[ch] for ch in s]

        offset = n
        size = 2 * n + 1  # possible diff range [-n, n]
        dp = [[0] * 3 for _ in range(size)]

        # initialize first round
        for b in range(3):
            if b == (a[0] + 1) % 3:      # Bob wins this round
                d = 1
            elif b == (a[0] + 2) % 3:    # Bob loses this round
                d = -1
            else:                         # tie
                d = 0
            dp[d + offset][b] = 1

        for i in range(1, n):
            ndp = [[0] * 3 for _ in range(size)]
            ai = a[i]
            for diff_idx in range(size):
                for prev in range(3):
                    cnt = dp[diff_idx][prev]
                    if not cnt:
                        continue
                    for cur in range(3):
                        if cur == prev:
                            continue
                        if cur == (ai + 1) % 3:
                            delta = 1
                        elif cur == (ai + 2) % 3:
                            delta = -1
                        else:
                            delta = 0
                        ndiff_idx = diff_idx + delta
                        ndp[ndiff_idx][cur] = (ndp[ndiff_idx][cur] + cnt) % MOD
            dp = ndp

        ans = 0
        for diff_idx in range(offset + 1, size):
            for last in range(3):
                ans = (ans + dp[diff_idx][last]) % MOD
        return ans
```

## Python3

```python
class Solution:
    def countWinningSequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        offset = n
        size = 2 * n + 1

        chars = ['F', 'W', 'E']
        idx = {'F': 0, 'W': 1, 'E': 2}
        beats = {'F': 'E', 'E': 'W', 'W': 'F'}

        dp = [[0] * 3 for _ in range(size)]

        a0 = s[0]
        for c in chars:
            if c == a0:
                d = 0
            elif beats[c] == a0:
                d = 1
            else:
                d = -1
            dp[d + offset][idx[c]] = (dp[d + offset][idx[c]] + 1) % MOD

        for i in range(1, n):
            ndp = [[0] * 3 for _ in range(size)]
            a = s[i]
            for diff_idx in range(size):
                for last_idx in range(3):
                    cnt = dp[diff_idx][last_idx]
                    if not cnt:
                        continue
                    last_char = chars[last_idx]
                    for c in chars:
                        if c == last_char:
                            continue
                        if c == a:
                            delta = 0
                        elif beats[c] == a:
                            delta = 1
                        else:
                            delta = -1
                        ndiff = diff_idx - offset + delta
                        ndp[ndiff + offset][idx[c]] = (ndp[ndiff + offset][idx[c]] + cnt) % MOD
            dp = ndp

        ans = 0
        for d in range(1, n + 1):
            di = d + offset
            for k in range(3):
                ans = (ans + dp[di][k]) % MOD
        return ans
```

## C

```c
#include <stddef.h>
#include <string.h>

#define MOD 1000000007

int countWinningSequences(char* s) {
    int n = (int)strlen(s);
    int offset = n;                     // shift for negative differences
    int size = 2 * n + 1;               // range [-n, n]

    static int dp_prev[3][2005];
    static int dp_cur[3][2005];

    // mapping: F=0, W=1, E=2
    auto char_to_idx = [](char c) -> int {
        if (c == 'F') return 0;
        if (c == 'W') return 1;
        return 2; // 'E'
    };

    int beats[3] = {2, 0, 1}; // F beats E, W beats F, E beats W

    // initialization for first round
    int a0 = char_to_idx(s[0]);
    for (int bob = 0; bob < 3; ++bob) {
        int delta;
        if (bob == a0) delta = 0;
        else if (beats[bob] == a0) delta = 1;
        else delta = -1;
        dp_prev[bob][offset + delta] = (dp_prev[bob][offset + delta] + 1) % MOD;
    }

    // process remaining rounds
    for (int i = 1; i < n; ++i) {
        int a = char_to_idx(s[i]);
        // clear current dp
        for (int k = 0; k < 3; ++k)
            memset(dp_cur[k], 0, size * sizeof(int));

        for (int prevMove = 0; prevMove < 3; ++prevMove) {
            for (int dIdx = 0; dIdx < size; ++dIdx) {
                int cnt = dp_prev[prevMove][dIdx];
                if (!cnt) continue;
                int curDiff = dIdx - offset;
                for (int bob = 0; bob < 3; ++bob) {
                    if (bob == prevMove) continue; // cannot repeat
                    int delta;
                    if (bob == a) delta = 0;
                    else if (beats[bob] == a) delta = 1;
                    else delta = -1;
                    int newDiff = curDiff + delta;
                    int ndIdx = offset + newDiff;
                    int val = dp_cur[bob][ndIdx] + cnt;
                    if (val >= MOD) val -= MOD;
                    dp_cur[bob][ndIdx] = val;
                }
            }
        }

        // swap prev and cur
        for (int k = 0; k < 3; ++k) {
            memcpy(dp_prev[k], dp_cur[k], size * sizeof(int));
        }
    }

    long long ans = 0;
    for (int move = 0; move < 3; ++move) {
        for (int dIdx = offset + 1; dIdx < size; ++dIdx) { // diff > 0
            ans += dp_prev[move][dIdx];
            if (ans >= MOD) ans -= MOD;
        }
    }
    return (int)(ans % MOD);
}
```

## Csharp

```csharp
using System;

public class Solution {
    private const int MOD = 1000000007;
    
    private static int Delta(char bob, char alice) {
        if (bob == alice) return 0;
        if ((bob == 'W' && alice == 'F') ||
            (bob == 'E' && alice == 'W') ||
            (bob == 'F' && alice == 'E')) return 1;
        return -1;
    }
    
    public int CountWinningSequences(string s) {
        int n = s.Length;
        int size = 2 * n + 1;          // diff from -n .. n
        int offset = n;                // index shift
        
        int[,] prev = new int[size, 3];
        int[,] cur = new int[size, 3];
        
        char[] alice = s.ToCharArray();
        char[] moves = new char[] { 'F', 'W', 'E' };
        
        // initialization for first round
        for (int k = 0; k < 3; ++k) {
            int d = Delta(moves[k], alice[0]);
            int idx = d + offset;
            prev[idx, k] = 1;
        }
        
        for (int i = 1; i < n; ++i) {
            // clear cur
            Array.Clear(cur, 0, cur.Length);
            
            for (int diffIdx = 0; diffIdx < size; ++diffIdx) {
                for (int p = 0; p < 3; ++p) {
                    int cnt = prev[diffIdx, p];
                    if (cnt == 0) continue;
                    
                    for (int k = 0; k < 3; ++k) {
                        if (k == p) continue; // cannot repeat same move
                        int d = Delta(moves[k], alice[i]);
                        int newIdx = diffIdx + d;
                        long val = cur[newIdx, k] + (long)cnt;
                        if (val >= MOD) val -= MOD;
                        cur[newIdx, k] = (int)val;
                    }
                }
            }
            
            // swap prev and cur
            var temp = prev;
            prev = cur;
            cur = temp;
        }
        
        long ans = 0;
        for (int diffIdx = offset + 1; diffIdx < size; ++diffIdx) {
            for (int k = 0; k < 3; ++k) {
                ans += prev[diffIdx, k];
                if (ans >= MOD) ans -= MOD;
            }
        }
        
        return (int)(ans % MOD);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countWinningSequences = function(s) {
    const MOD = 1000000007;
    const n = s.length;
    const offset = n;                 // shift for negative differences
    const range = 2 * n + 1;          // possible diff values from -n .. n

    // map characters to indices: F=0, W=1, E=2
    const charMap = { 'F': 0, 'W': 1, 'E': 2 };
    const a = new Array(n);
    for (let i = 0; i < n; ++i) a[i] = charMap[s[i]];

    // outcome: +1 if bob beats alice, -1 if loses, 0 if tie
    const outcome = (bob, alice) => {
        if (bob === alice) return 0;
        return (bob === (alice + 1) % 3) ? 1 : -1;
    };

    // dp layers: each entry is an array of length 3 for last move
    let prev = new Array(range);
    for (let i = 0; i < range; ++i) prev[i] = [0, 0, 0];

    // initialization for first round
    for (let m = 0; m < 3; ++m) {
        const d = outcome(m, a[0]);
        const idx = d + offset;
        prev[idx][m] = (prev[idx][m] + 1) % MOD;
    }

    // iterate over remaining rounds
    for (let pos = 1; pos < n; ++pos) {
        let next = new Array(range);
        for (let i = 0; i < range; ++i) next[i] = [0, 0, 0];

        for (let diffIdx = 0; diffIdx < range; ++diffIdx) {
            const curArr = prev[diffIdx];
            if (!curArr[0] && !curArr[1] && !curArr[2]) continue;
            const curDiff = diffIdx - offset;

            for (let last = 0; last < 3; ++last) {
                const ways = curArr[last];
                if (!ways) continue;
                for (let m = 0; m < 3; ++m) {
                    if (m === last) continue; // cannot repeat move
                    const ndiff = curDiff + outcome(m, a[pos]);
                    const nIdx = ndiff + offset;
                    const val = next[nIdx][m] + ways;
                    next[nIdx][m] = val >= MOD ? val - MOD : val;
                }
            }
        }

        prev = next;
    }

    // sum over positive differences
    let ans = 0;
    for (let diffIdx = offset + 1; diffIdx < range; ++diffIdx) {
        const arr = prev[diffIdx];
        ans += arr[0] + arr[1] + arr[2];
        if (ans >= MOD) ans %= MOD;
    }
    return ans % MOD;
};
```

## Typescript

```typescript
function countWinningSequences(s: string): number {
    const MOD = 1000000007;
    const n = s.length;
    const offset = n; // shift for negative diffs
    const size = 2 * n + 1;
    const moves = ['F', 'W', 'E'] as const;
    const beats: { [k: string]: string } = { F: 'E', E: 'W', W: 'F' };

    function outcome(bob: string, alice: string): number {
        if (bob === alice) return 0;
        return beats[bob] === alice ? 1 : -1;
    }

    // dpPrev[moveIdx][diff+offset]
    let dpPrev = Array.from({ length: 3 }, () => new Array<number>(size).fill(0));

    for (let m = 0; m < 3; ++m) {
        const delta = outcome(moves[m], s[0]);
        dpPrev[m][delta + offset] = 1;
    }

    for (let i = 1; i < n; ++i) {
        const aChar = s[i];
        const dpCurr = Array.from({ length: 3 }, () => new Array<number>(size).fill(0));
        // previous diff range is [-i, i]
        for (let prev = 0; prev < 3; ++prev) {
            const prevArr = dpPrev[prev];
            for (let d = -i; d <= i; ++d) {
                const cnt = prevArr[d + offset];
                if (!cnt) continue;
                for (let cur = 0; cur < 3; ++cur) {
                    if (cur === prev) continue; // cannot repeat same move
                    const nd = d + outcome(moves[cur], aChar);
                    let val = dpCurr[cur][nd + offset] + cnt;
                    if (val >= MOD) val -= MOD;
                    dpCurr[cur][nd + offset] = val;
                }
            }
        }
        dpPrev = dpCurr;
    }

    let ans = 0;
    for (let m = 0; m < 3; ++m) {
        const arr = dpPrev[m];
        for (let d = 1; d <= n; ++d) {
            ans += arr[d + offset];
            if (ans >= MOD) ans -= MOD;
        }
    }
    return ans % MOD;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function countWinningSequences($s) {
        $mod = 1000000007;
        $n = strlen($s);
        $offset = $n;                     // shift for negative differences
        $size = 2 * $n + 1;               // possible diff indices: -n .. n

        // map character to integer: F=0, W=1, E=2
        $charMap = ['F'=>0,'W'=>1,'E'=>2];
        $a = [];
        for ($i = 0; $i < $n; $i++) {
            $a[$i] = $charMap[$s[$i]];
        }

        // outcome: returns +1 if bob beats alice, -1 if alice beats bob, 0 tie
        $outcome = function($bob, $alice) {
            if ($bob === $alice) return 0;
            // W beats F, F beats E, E beats W
            if (($bob == 1 && $alice == 0) ||
                ($bob == 0 && $alice == 2) ||
                ($bob == 2 && $alice == 1)) {
                return 1;
            }
            return -1;
        };

        // dp for previous position: [diffIndex][lastMove]
        $prev = array_fill(0, $size, array_fill(0, 3, 0));
        for ($move = 0; $move < 3; $move++) {
            $delta = $outcome($move, $a[0]);
            $idx = $offset + $delta;
            $prev[$idx][$move] = 1;
        }

        // iterate over positions
        for ($i = 1; $i < $n; $i++) {
            $curr = array_fill(0, $size, array_fill(0, 3, 0));
            for ($diffIdx = 0; $diffIdx < $size; $diffIdx++) {
                for ($prevMove = 0; $prevMove < 3; $prevMove++) {
                    $cnt = $prev[$diffIdx][$prevMove];
                    if ($cnt == 0) continue;
                    for ($curMove = 0; $curMove < 3; $curMove++) {
                        if ($curMove === $prevMove) continue; // cannot repeat
                        $delta = $outcome($curMove, $a[$i]);
                        $newIdx = $diffIdx + $delta;
                        if ($newIdx < 0 || $newIdx >= $size) continue;
                        $curr[$newIdx][$curMove] += $cnt;
                        if ($curr[$newIdx][$curMove] >= $mod) {
                            $curr[$newIdx][$curMove] -= $mod;
                        }
                    }
                }
            }
            $prev = $curr;
        }

        // sum over positive differences
        $ans = 0;
        for ($diffIdx = $offset + 1; $diffIdx < $size; $diffIdx++) {
            for ($move = 0; $move < 3; $move++) {
                $ans += $prev[$diffIdx][$move];
                if ($ans >= $mod) $ans -= $mod;
            }
        }
        return $ans % $mod;
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    private let MOD = 1_000_000_007
    
    func countWinningSequences(_ s: String) -> Int {
        let n = s.count
        if n == 0 { return 0 }
        // Map characters to integers: F=0, W=1, E=2
        var alice = [Int]()
        alice.reserveCapacity(n)
        for ch in s {
            switch ch {
            case "F": alice.append(0)
            case "W": alice.append(1)
            case "E": alice.append(2)
            default:  alice.append(0) // never happens
            }
        }
        
        let offset = n               // to shift diff from [-n, n] to [0, 2n]
        let size = 2 * n + 1
        
        var dpPrev = Array(repeating: Array(repeating: 0, count: 3), count: size)
        
        // Initialize for first round
        for move in 0..<3 {
            let delta = outcome(bob: move, alice: alice[0])
            let idx = offset + delta
            dpPrev[idx][move] = 1
        }
        
        if n == 1 {
            var ans = 0
            for diffIdx in (offset+1)..<size { // diff > 0
                for last in 0..<3 {
                    ans += dpPrev[diffIdx][last]
                    if ans >= MOD { ans -= MOD }
                }
            }
            return ans
        }
        
        // DP over remaining rounds
        for i in 1..<n {
            var dpCurr = Array(repeating: Array(repeating: 0, count: 3), count: size)
            let aliceMove = alice[i]
            for diffIdx in 0..<size {
                for last in 0..<3 {
                    let curVal = dpPrev[diffIdx][last]
                    if curVal == 0 { continue }
                    for nxt in 0..<3 where nxt != last {
                        let delta = outcome(bob: nxt, alice: aliceMove)
                        let newIdx = diffIdx + delta
                        // newIdx always stays within [0, size)
                        var val = dpCurr[newIdx][nxt] + curVal
                        if val >= MOD { val -= MOD }
                        dpCurr[newIdx][nxt] = val
                    }
                }
            }
            dpPrev = dpCurr
        }
        
        var answer = 0
        for diffIdx in (offset+1)..<size { // only positive differences
            for last in 0..<3 {
                answer += dpPrev[diffIdx][last]
                if answer >= MOD { answer -= MOD }
            }
        }
        return answer
    }
    
    // Returns +1 if bob beats alice, -1 if bob loses, 0 if tie.
    private func outcome(bob: Int, alice: Int) -> Int {
        if bob == alice { return 0 }
        // F(0) beats E(2), E(2) beats W(1), W(1) beats F(0)
        if (bob == 0 && alice == 2) ||
           (bob == 2 && alice == 1) ||
           (bob == 1 && alice == 0) {
            return 1
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L
    fun countWinningSequences(s: String): Int {
        val n = s.length
        val offset = n
        val size = 2 * n + 1
        val moves = charArrayOf('F', 'W', 'E')
        var cur = Array(3) { LongArray(size) }
        var nxt = Array(3) { LongArray(size) }

        fun outcome(bob: Char, alice: Char): Int {
            if (bob == alice) return 0
            return when {
                bob == 'W' && alice == 'F' -> 1
                bob == 'F' && alice == 'E' -> 1
                bob == 'E' && alice == 'W' -> 1
                else -> -1
            }
        }

        // initialize first round
        val firstAlice = s[0]
        for (k in 0..2) {
            val delta = outcome(moves[k], firstAlice)
            cur[k][offset + delta] = (cur[k][offset + delta] + 1) % MOD
        }

        // process remaining rounds
        for (i in 1 until n) {
            // reset nxt
            for (k in 0..2) {
                java.util.Arrays.fill(nxt[k], 0L)
            }
            val alice = s[i]
            for (prev in 0..2) {
                val curArr = cur[prev]
                for (idx in 0 until size) {
                    val cnt = curArr[idx]
                    if (cnt == 0L) continue
                    for (nextMove in 0..2) {
                        if (nextMove == prev) continue
                        val delta = outcome(moves[nextMove], alice)
                        val newIdx = idx + delta
                        nxt[nextMove][newIdx] = (nxt[nextMove][newIdx] + cnt) % MOD
                    }
                }
            }
            // swap cur and nxt
            val temp = cur
            cur = nxt
            nxt = temp
        }

        var ans = 0L
        for (k in 0..2) {
            for (idx in offset + 1 until size) { // diff > 0
                ans += cur[k][idx]
                if (ans >= MOD) ans -= MOD
            }
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _MOD = 1000000007;

  int countWinningSequences(String s) {
    int n = s.length;
    // Map characters to indices: F=0, W=1, E=2
    List<int> alice = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      switch (s[i]) {
        case 'F':
          alice[i] = 0;
          break;
        case 'W':
          alice[i] = 1;
          break;
        default: // 'E'
          alice[i] = 2;
      }
    }

    int offset = n; // shift for negative differences
    int diffSize = 2 * n + 1;

    // dp[diff][lastMove]
    List<List<int>> prev = List.generate(diffSize, (_) => List.filled(3, 0));
    // Initialize first round
    for (int bob = 0; bob < 3; bob++) {
      int delta = _outcome(bob, alice[0]);
      int idx = offset + delta;
      prev[idx][bob] = (prev[idx][bob] + 1) % _MOD;
    }

    // Iterate over remaining rounds
    for (int i = 1; i < n; i++) {
      List<List<int>> cur = List.generate(diffSize, (_) => List.filled(3, 0));
      int aMove = alice[i];
      for (int d = 0; d < diffSize; d++) {
        for (int last = 0; last < 3; last++) {
          int val = prev[d][last];
          if (val == 0) continue;
          for (int nb = 0; nb < 3; nb++) {
            if (nb == last) continue; // cannot repeat same move
            int delta = _outcome(nb, aMove);
            int nd = d + delta;
            cur[nd][nb] += val;
            if (cur[nd][nb] >= _MOD) cur[nd][nb] -= _MOD;
          }
        }
      }
      prev = cur;
    }

    // Sum over positive differences
    int ans = 0;
    for (int d = offset + 1; d < diffSize; d++) {
      for (int last = 0; last < 3; last++) {
        ans += prev[d][last];
        if (ans >= _MOD) ans -= _MOD;
      }
    }
    return ans;
  }

  // Returns +1 if bob beats alice, -1 if alice beats bob, 0 for tie
  int _outcome(int bob, int alice) {
    if (bob == alice) return 0;
    // F(0) beats E(2), W(1) beats F(0), E(2) beats W(1)
    if ((bob == 0 && alice == 2) ||
        (bob == 1 && alice == 0) ||
        (bob == 2 && alice == 1)) {
      return 1;
    }
    return -1;
  }
}
```

## Golang

```go
package main

import "fmt"

const MOD = 1000000007

func countWinningSequences(s string) int {
	n := len(s)
	if n == 0 {
		return 0
	}
	offset := n
	size := 2*n + 1

	// dp[diff+offset][lastMove]
	prev := make([][3]int, size)
	cur := make([][3]int, size)

	aliceIdx := func(c byte) int {
		switch c {
		case 'F':
			return 0
		case 'W':
			return 1
		case 'E':
			return 2
		}
		return -1
	}

	outcome := func(bob, alice int) int {
		if bob == alice {
			return 0
		}
		// W beats F, F beats E, E beats W
		if (bob == 1 && alice == 0) || (bob == 0 && alice == 2) || (bob == 2 && alice == 1) {
			return 1
		}
		return -1
	}

	// initialization for first round
	a0 := aliceIdx(s[0])
	for b := 0; b < 3; b++ {
		diff := outcome(b, a0)
		prev[diff+offset][b] = (prev[diff+offset][b] + 1) % MOD
	}

	// process remaining rounds
	for i := 1; i < n; i++ {
		// reset cur
		for d := 0; d < size; d++ {
			cur[d][0], cur[d][1], cur[d][2] = 0, 0, 0
		}
		ai := aliceIdx(s[i])
		for d := 0; d < size; d++ {
			for pl := 0; pl < 3; pl++ {
				val := prev[d][pl]
				if val == 0 {
					continue
				}
				for nb := 0; nb < 3; nb++ {
					if nb == pl {
						continue
					}
					newDiff := (d - offset) + outcome(nb, ai)
					idx := newDiff + offset
					cur[idx][nb] += val
					if cur[idx][nb] >= MOD {
						cur[idx][nb] -= MOD
					}
				}
			}
		}
		prev, cur = cur, prev
	}

	ans := 0
	for d := offset + 1; d < size; d++ { // diff > 0
		for k := 0; k < 3; k++ {
			ans += prev[d][k]
			if ans >= MOD {
				ans -= MOD
			}
		}
	}
	return ans % MOD
}

// The following main function is only for local testing and will be ignored on LeetCode.
func main() {
	fmt.Println(countWinningSequences("FFF"))   // expected 3
	fmt.Println(countWinningSequences("FWEFW")) // expected 18
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def count_winning_sequences(s)
  n = s.length
  shift = n
  char_to_idx = { 'F' => 0, 'W' => 1, 'E' => 2 }

  # beats[i][j] == true if move i beats move j
  beats = Array.new(3) { Array.new(3, false) }
  beats[0][2] = true   # F beats E
  beats[2][1] = true   # E beats W
  beats[1][0] = true   # W beats F

  # delta_table[move][pos] = +1 / -1 / 0 for that round
  delta_table = Array.new(3) { Array.new(n, 0) }
  n.times do |pos|
    a_idx = char_to_idx[s[pos]]
    3.times do |b|
      if b == a_idx
        delta = 0
      elsif beats[b][a_idx]
        delta = 1
      else
        delta = -1
      end
      delta_table[b][pos] = delta
    end
  end

  size = 2 * n + 1
  dp_cur = Array.new(size) { [0, 0, 0] }

  # initialize first round
  3.times do |b|
    d = delta_table[b][0]
    idx = d + shift
    dp_cur[idx][b] = (dp_cur[idx][b] + 1) % MOD
  end

  (1...n).each do |pos|
    dp_next = Array.new(size) { [0, 0, 0] }
    # possible delta range at this step is [-pos, pos]
    (-pos..pos).each do |d|
      idx = d + shift
      cnts = dp_cur[idx]
      next if cnts[0] == 0 && cnts[1] == 0 && cnts[2] == 0
      3.times do |last|
        cnt = cnts[last]
        next if cnt == 0
        3.times do |nb|
          next if nb == last
          nd = d + delta_table[nb][pos]
          nidx = nd + shift
          dp_next[nidx][nb] = (dp_next[nidx][nb] + cnt) % MOD
        end
      end
    end
    dp_cur = dp_next
  end

  ans = 0
  (1..n).each do |d|
    idx = d + shift
    ans = (ans + dp_cur[idx][0] + dp_cur[idx][1] + dp_cur[idx][2]) % MOD
  end
  ans
end
```

## Scala

```scala
object Solution {
  def countWinningSequences(s: String): Int = {
    val MOD = 1000000007L
    val n = s.length
    val offset = n
    val diffSize = 2 * n + 1

    val idxToChar = Array('F', 'W', 'E')

    def outcome(bob: Char, alice: Char): Int = {
      if (bob == alice) 0
      else if ((bob == 'F' && alice == 'E') ||
               (bob == 'E' && alice == 'W') ||
               (bob == 'W' && alice == 'F')) 1
      else -1
    }

    var prev = Array.ofDim[Long](diffSize, 3)

    // initialize for first round
    val firstAlice = s.charAt(0)
    for (mIdx <- 0 until 3) {
      val delta = outcome(idxToChar(mIdx), firstAlice)
      val dIdx = offset + delta
      prev(dIdx)(mIdx) = (prev(dIdx)(mIdx) + 1) % MOD
    }

    // process remaining rounds
    for (i <- 1 until n) {
      val cur = Array.ofDim[Long](diffSize, 3)
      val aliceChar = s.charAt(i)
      var d = 0
      while (d < diffSize) {
        var pm = 0
        while (pm < 3) {
          val cnt = prev(d)(pm)
          if (cnt != 0) {
            var nm = 0
            while (nm < 3) {
              if (nm != pm) {
                val delta = outcome(idxToChar(nm), aliceChar)
                val nd = d + delta
                if (nd >= 0 && nd < diffSize) {
                  cur(nd)(nm) = (cur(nd)(nm) + cnt) % MOD
                }
              }
              nm += 1
            }
          }
          pm += 1
        }
        d += 1
      }
      prev = cur
    }

    var ans = 0L
    var dIdx = offset + 1 // diff > 0
    while (dIdx < diffSize) {
      var m = 0
      while (m < 3) {
        ans += prev(dIdx)(m)
        if (ans >= MOD) ans -= MOD
        m += 1
      }
      dIdx += 1
    }

    ans.toInt
  }
}
```

## Rust

```rust
use std::cmp::{max, min};

impl Solution {
    pub fn count_winning_sequences(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let chars: Vec<usize> = s
            .bytes()
            .map(|b| match b {
                b'F' => 0,
                b'W' => 1,
                _ => 2, // 'E'
            })
            .collect();
        let n = chars.len();
        let offset = n as i32; // to shift diff from [-n,n] to [0,2n]
        let size = 2 * n + 1;

        // delta[bob][alice] = contribution to (Bob - Alice)
        let delta: [[i32; 3]; 3] = [
            [0, -1, 1], // bob F
            [1, 0, -1], // bob W
            [-1, 1, 0], // bob E
        ];

        // dp[diff + offset][last_char] = ways
        let mut dp: Vec<[i64; 3]> = vec![[0; 3]; size];

        // initialize for first round
        for b in 0..3 {
            let d = delta[b][chars[0]];
            let idx = (d + offset) as usize;
            dp[idx][b] = 1;
        }

        // iterate over remaining rounds
        for i in 1..n {
            let mut ndp: Vec<[i64; 3]> = vec![[0; 3]; size];
            let a = chars[i];
            for diff_idx in 0..size {
                for prev in 0..3 {
                    let cur_val = dp[diff_idx][prev];
                    if cur_val == 0 {
                        continue;
                    }
                    let cur_diff = diff_idx as i32 - offset;
                    for nb in 0..3 {
                        if nb == prev {
                            continue; // cannot repeat
                        }
                        let ndiff = cur_diff + delta[nb][a];
                        if ndiff < -(n as i32) || ndiff > n as i32 {
                            continue;
                        }
                        let nidx = (ndiff + offset) as usize;
                        ndp[nidx][nb] += cur_val;
                        if ndp[nidx][nb] >= MOD {
                            ndp[nidx][nb] -= MOD;
                        }
                    }
                }
            }
            dp = ndp;
        }

        // sum over positive diffs
        let mut ans: i64 = 0;
        for diff_idx in (offset + 1) as usize..size {
            for last in 0..3 {
                ans += dp[diff_idx][last];
                if ans >= MOD {
                    ans -= MOD;
                }
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

(: char->int (Char -> Integer))
(define (char->int ch)
  (cond [(char=? ch #\F) 0]
        [(char=? ch #\W) 1]
        [else 2]))

(: outcome (Integer Integer -> Integer))
;; returns +1 if bob beats alice, -1 if alice beats bob, 0 tie
(define (outcome bob alice)
  (cond [(= bob alice) 0]
        [(= (modulo (- bob alice) 3) 1) 1] ; bob wins
        [else -1]))

(: count-winning-sequences (String -> Integer))
(define (count-winning-sequences s)
  (let* ((n (string-length s))
         (offset n)
         (sizeDiff (+ (* 2 n) 1))
         ;; dp layers: vector of 3 vectors (for last move), each length sizeDiff
         (prev (for/vector ([i (in-range 3)]) (make-vector sizeDiff 0))))
    ;; initialize first round
    (let ((a (char->int (string-ref s 0))))
      (for ([k (in-range 3)])
        (let* ((delta (outcome k a))
               (idx (+ offset delta)))
          (vector-set! (vector-ref prev k) idx 1))))
    ;; iterate remaining rounds
    (for ([i (in-range 1 n)])
      (define cur (for/vector ([j (in-range 3)]) (make-vector sizeDiff 0)))
      (let ((a (char->int (string-ref s i))))
        (for ([prev-last (in-range 3)])
          (define prev-vec (vector-ref prev prev-last))
          (for ([diff-idx (in-range sizeDiff)])
            (define val (vector-ref prev-vec diff-idx))
            (when (not (= val 0))
              (for ([k (in-range 3)] #:when (not (= k prev-last)))
                (let* ((delta (outcome k a))
                       (new-idx (+ diff-idx delta))
                       (cur-vec (vector-ref cur k)))
                  (vector-set! cur-vec new-idx
                               (modulo (+ (vector-ref cur-vec new-idx) val) MOD))))))))
      (set! prev cur))
    ;; sum over positive differences
    (let ((ans 0))
      (for ([k (in-range 3)])
        (define vec (vector-ref prev k))
        (for ([diff-idx (in-range (add1 offset) sizeDiff)]) ; diff > 0
          (set! ans (modulo (+ ans (vector-ref vec diff-idx)) MOD))))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([count_winning_sequences/1]).

-define(MOD, 1000000007).

count_winning_sequences(S) ->
    CharList = binary:bin_to_list(S),
    Moves = [char_to_move(C) || C <- CharList],
    case Moves of
        [] -> 0;
        [FirstAlice | RestAlices] ->
            InitMap = init_map(FirstAlice),
            FinalMap = lists:foldl(fun(AliceMove, PrevMap) ->
                transition(PrevMap, AliceMove)
            end, InitMap, RestAlices),
            sum_positive(FinalMap)
    end.

char_to_move($F) -> 0;
char_to_move($W) -> 1;
char_to_move($E) -> 2.

outcome(Bob, Alice) ->
    case ((Bob - Alice + 3) rem 3) of
        1 -> 1;
        2 -> -1;
        _ -> 0
    end.

init_map(AliceMove) ->
    maps:from_list(
        [{ {Diff, Move}, 1}
         || Move <- [0,1,2],
            Diff = outcome(Move, AliceMove)]).

transition(PrevMap, AliceMove) ->
    maps:fold(fun({DiffPrev, MovePrev}, Count, Acc) ->
        lists:foldl(fun(NewMove, A2) ->
                case NewMove =:= MovePrev of
                    true -> A2;
                    false ->
                        DiffNew = DiffPrev + outcome(NewMove, AliceMove),
                        Key = {DiffNew, NewMove},
                        maps:update_with(Key,
                            fun(V) -> (V + Count) rem ?MOD end,
                            Count,
                            A2)
                end
            end, Acc, [0,1,2])
    end, maps:new(), PrevMap).

sum_positive(Map) ->
    maps:fold(fun({Diff,_}, Count, Acc) ->
        if Diff > 0 -> (Acc + Count) rem ?MOD;
           true -> Acc
        end
    end, 0, Map).
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec count_winning_sequences(s :: String.t()) :: integer
  def count_winning_sequences(s) do
    chars = String.graphemes(s) |> Enum.map(&char_to_int/1)
    n = length(chars)
    offset = n
    size = 2 * n + 1

    # dp for first position
    cur =
      Enum.reduce(0..2, :array.new(size, default: {0, 0, 0}), fn m, acc ->
        diff = outcome(m, hd(chars))
        idx = diff + offset
        {cF, cW, cE} = :array.get(idx, acc)

        new_tuple =
          case m do
            0 -> {(cF + 1) rem @mod, cW, cE}
            1 -> {cF, (cW + 1) rem @mod, cE}
            2 -> {cF, cW, (cE + 1) rem @mod}
          end

        :array.set(idx, new_tuple, acc)
      end)

    final_cur =
      Enum.reduce(1..(n - 1), cur, fn i, prev ->
        a = Enum.at(chars, i)

        next =
          Enum.reduce(0..(size - 1), :array.new(size, default: {0, 0, 0}), fn idx, nxt ->
            {cF, cW, cE} = :array.get(idx, prev)

            nxt =
              if cF > 0 do
                cnt = cF

                Enum.reduce([1, 2], nxt, fn new_move, acc ->
                  nidx = (idx - offset) + outcome(new_move, a) + offset
                  add_to(acc, nidx, new_move, cnt)
                end)
              else
                nxt
              end

            nxt =
              if cW > 0 do
                cnt = cW

                Enum.reduce([0, 2], nxt, fn new_move, acc ->
                  nidx = (idx - offset) + outcome(new_move, a) + offset
                  add_to(acc, nidx, new_move, cnt)
                end)
              else
                nxt
              end

            if cE > 0 do
              cnt = cE

              Enum.reduce([0, 1], nxt, fn new_move, acc ->
                nidx = (idx - offset) + outcome(new_move, a) + offset
                add_to(acc, nidx, new_move, cnt)
              end)
            else
              nxt
            end
          end)

        next
      end)

    Enum.reduce((offset + 1)..(size - 1), 0, fn idx, acc ->
      {cF, cW, cE} = :array.get(idx, final_cur)
      (acc + cF + cW + cE) rem @mod
    end)
  end

  defp add_to(arr, idx, move, cnt) do
    {nf, nw, ne} = :array.get(idx, arr)

    updated =
      case move do
        0 -> {(nf + cnt) rem @mod, nw, ne}
        1 -> {nf, (nw + cnt) rem @mod, ne}
        2 -> {nf, nw, (ne + cnt) rem @mod}
      end

    :array.set(idx, updated, arr)
  end

  defp char_to_int("F"), do: 0
  defp char_to_int("W"), do: 1
  defp char_to_int("E"), do: 2

  # outcome: +1 if bob beats alice, -1 if loses, 0 tie
  defp outcome(bob, alice) when bob == alice, do: 0

  defp outcome(bob, alice) do
    case {bob, alice} do
      {0, 2} -> 1   # F beats E
      {1, 0} -> 1   # W beats F
      {2, 1} -> 1   # E beats W
      _ -> -1
    end
  end
end
```
