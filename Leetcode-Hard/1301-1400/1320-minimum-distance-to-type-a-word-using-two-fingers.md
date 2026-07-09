# 1320. Minimum Distance to Type a Word Using Two Fingers

## Cpp

```cpp
class Solution {
public:
    int minimumDistance(string word) {
        int n = word.size();
        if (n <= 1) return 0;
        // precompute coordinates
        vector<int> xs(26), ys(26);
        for (int i = 0; i < 26; ++i) {
            xs[i] = i % 6;
            ys[i] = i / 6;
        }
        // distance matrix
        int dist[26][26];
        for (int i = 0; i < 26; ++i)
            for (int j = 0; j < 26; ++j)
                dist[i][j] = abs(xs[i] - xs[j]) + abs(ys[i] - ys[j]);
        
        const int INF = 1e9;
        // dp[other] = min cost after processing up to current index,
        // where the active finger is on word[i-1], other finger at 'other' (26 means unused)
        vector<int> dp(27, INF);
        dp[26] = 0; // after typing first character with one finger, other finger unused
        
        for (int i = 1; i < n; ++i) {
            int cur = word[i] - 'A';
            int prev = word[i-1] - 'A';
            vector<int> ndp(27, INF);
            for (int j = 0; j <= 26; ++j) {
                if (dp[j] == INF) continue;
                // Move the finger that typed previous character
                int cost1 = dp[j] + dist[prev][cur];
                ndp[j] = min(ndp[j], cost1);
                // Use the other finger (if unused, cost 0)
                int moveCost = (j == 26) ? 0 : dist[j][cur];
                int newOther = prev; // previous active becomes the other finger
                int cost2 = dp[j] + moveCost;
                ndp[newOther] = min(ndp[newOther], cost2);
            }
            dp.swap(ndp);
        }
        
        int ans = INF;
        for (int v : dp) ans = min(ans, v);
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumDistance(String word) {
        int n = word.length();
        if (n <= 1) return 0;
        // Precompute Manhattan distances between letters
        int[][] dist = new int[26][26];
        for (int a = 0; a < 26; a++) {
            int ax = a / 6, ay = a % 6;
            for (int b = 0; b < 26; b++) {
                int bx = b / 6, by = b % 6;
                dist[a][b] = Math.abs(ax - bx) + Math.abs(ay - by);
            }
        }

        final int INF = 1_000_000;
        int[] dp = new int[26];
        // before typing first character, the other finger can be anywhere for free
        for (int i = 0; i < 26; i++) dp[i] = 0;

        int prev = word.charAt(0) - 'A';
        for (int idx = 1; idx < n; idx++) {
            int cur = word.charAt(idx) - 'A';
            int[] ndp = new int[26];
            for (int i = 0; i < 26; i++) ndp[i] = INF;

            for (int other = 0; other < 26; other++) {
                // move the finger that typed prev to cur
                ndp[other] = Math.min(ndp[other], dp[other] + dist[prev][cur]);
                // move the other finger from its position to cur, making prev stationary
                ndp[prev] = Math.min(ndp[prev], dp[other] + dist[other][cur]);
            }
            dp = ndp;
            prev = cur;
        }

        int ans = INF;
        for (int v : dp) ans = Math.min(ans, v);
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        if n <= 1:
            return 0

        # precompute Manhattan distances on the keyboard layout (6 columns per row)
        dist = [[0] * 26 for _ in range(26)]
        for i in range(26):
            x1, y1 = divmod(i, 6)
            for j in range(26):
                x2, y2 = divmod(j, 6)
                dist[i][j] = abs(x1 - x2) + abs(y1 - y2)

        prev_idx = ord(word[0]) - 65
        dp = {-1: 0}  # key: idle finger position index (or -1 if not placed), value: min cost

        for ch in word[1:]:
            cur_idx = ord(ch) - 65
            new_dp = {}
            for idle, cost in dp.items():
                # Move the active finger (currently at prev_idx) to current character
                c1 = cost + dist[prev_idx][cur_idx]
                if idle not in new_dp or c1 < new_dp[idle]:
                    new_dp[idle] = c1

                # Move the idle finger to current character (if it exists)
                move_cost = 0 if idle == -1 else dist[idle][cur_idx]
                c2 = cost + move_cost
                new_idle = prev_idx  # previous active becomes the new idle
                if new_idle not in new_dp or c2 < new_dp[new_idle]:
                    new_dp[new_idle] = c2

            dp = new_dp
            prev_idx = cur_idx

        return min(dp.values())
```

## Python3

```python
class Solution:
    def minimumDistance(self, word: str) -> int:
        # coordinates for each letter in the 6-column layout
        rows = [i // 6 for i in range(26)]
        cols = [i % 6 for i in range(26)]

        def dist(a: int, b: int) -> int:
            return abs(rows[a] - rows[b]) + abs(cols[a] - cols[b])

        INF = 10 ** 9
        SENTINEL = 26  # represents the unused finger

        n = len(word)
        if n <= 1:
            return 0

        # dp[other_finger_position] = minimal cost after typing up to current index,
        # with the active finger on word[i-1]
        dp = {SENTINEL: 0}
        prev_idx = ord(word[0]) - ord('A')

        for i in range(1, n):
            cur_idx = ord(word[i]) - ord('A')
            new_dp = [INF] * 27  # index by other finger position (0..26)
            for other_pos, cost in dp.items():
                # Option 1: use the same finger (active) to type current char
                c1 = cost + dist(prev_idx, cur_idx)
                if c1 < new_dp[other_pos]:
                    new_dp[other_pos] = c1

                # Option 2: use the other finger to type current char
                move_cost = 0 if other_pos == SENTINEL else dist(other_pos, cur_idx)
                c2 = cost + move_cost
                # after using other finger, it becomes active; previous active becomes 'other'
                new_other = prev_idx
                if c2 < new_dp[new_other]:
                    new_dp[new_other] = c2

            # compress back to dict for next iteration
            dp = {pos: val for pos, val in enumerate(new_dp) if val != INF}
            prev_idx = cur_idx

        return min(dp.values())
```

## C

```c
#include <string.h>
#include <limits.h>

int minimumDistance(char* word) {
    int n = strlen(word);
    if (n <= 1) return 0;

    // Precompute Manhattan distances between all letters.
    int dist[26][26];
    for (int a = 0; a < 26; ++a) {
        int ra = a / 6, ca = a % 6;
        for (int b = 0; b < 26; ++b) {
            int rb = b / 6, cb = b % 6;
            dist[a][b] = abs(ra - rb) + abs(ca - cb);
        }
    }

    const int INF = INT_MAX / 2;
    int prev[27], cur[27];
    for (int i = 0; i < 27; ++i) prev[i] = INF;

    // After typing the first character, one finger is on it,
    // the other finger has not been used yet (represented by 26).
    prev[26] = 0;

    for (int i = 1; i < n; ++i) {
        int curIdx = word[i] - 'A';
        int prevIdx = word[i - 1] - 'A';
        for (int j = 0; j < 27; ++j) cur[j] = INF;

        for (int other = 0; other < 27; ++other) {
            if (prev[other] == INF) continue;

            // Use the same finger that typed previous character.
            int costSame = prev[other] + dist[prevIdx][curIdx];
            if (costSame < cur[other]) cur[other] = costSame;

            // Use the other finger.
            int moveCost = (other == 26) ? 0 : dist[other][curIdx];
            int newOther = prevIdx; // previous active finger becomes the "other" one.
            int costOther = prev[other] + moveCost;
            if (costOther < cur[newOther]) cur[newOther] = costOther;
        }

        // Prepare for next iteration.
        for (int j = 0; j < 27; ++j) prev[j] = cur[j];
    }

    int answer = INF;
    for (int i = 0; i < 27; ++i)
        if (prev[i] < answer) answer = prev[i];
    return answer;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimumDistance(string word)
    {
        int n = word.Length;
        if (n <= 1) return 0;

        int[] row = new int[26];
        int[] col = new int[26];
        for (int i = 0; i < 26; i++)
        {
            row[i] = i / 10;
            col[i] = i % 10;
        }

        int Dist(int a, int b) => Math.Abs(row[a] - row[b]) + Math.Abs(col[a] - col[b]);

        const int INF = int.MaxValue / 4;
        int[] dpPrev = new int[27];
        for (int i = 0; i < 27; i++) dpPrev[i] = INF;
        // after typing first character, the other finger is unused (index 26)
        dpPrev[26] = 0;

        for (int pos = 1; pos < n; pos++)
        {
            int prevIdx = word[pos - 1] - 'A';
            int curIdx = word[pos] - 'A';
            int[] dpCurr = new int[27];
            for (int i = 0; i < 27; i++) dpCurr[i] = INF;

            for (int j = 0; j < 27; j++)
            {
                int val = dpPrev[j];
                if (val == INF) continue;

                // Use the same finger that typed previous character
                int costSame = Dist(prevIdx, curIdx);
                if (val + costSame < dpCurr[j]) dpCurr[j] = val + costSame;

                // Use the other finger
                int costOther = (j == 26) ? 0 : Dist(j, curIdx);
                int newOther = prevIdx; // previous active finger becomes the other one
                if (val + costOther < dpCurr[newOther]) dpCurr[newOther] = val + costOther;
            }

            dpPrev = dpCurr;
        }

        int answer = INF;
        foreach (int v in dpPrev) if (v < answer) answer = v;
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var minimumDistance = function(word) {
    const n = word.length;
    if (n <= 1) return 0;

    // map letter to index 0..25
    const idx = ch => ch.charCodeAt(0) - 65;

    // precompute Manhattan distances based on layout rows of 6 columns
    const dist = Array.from({ length: 26 }, () => new Array(26).fill(0));
    for (let i = 0; i < 26; ++i) {
        const ri = Math.floor(i / 6), ci = i % 6;
        for (let j = 0; j < 26; ++j) {
            const rj = Math.floor(j / 6), cj = j % 6;
            dist[i][j] = Math.abs(ri - rj) + Math.abs(ci - cj);
        }
    }

    const INF = Number.MAX_SAFE_INTEGER;
    // dp[a][b]: min cost after processing prefix, fingers at a and b (order matters)
    let dp = Array.from({ length: 26 }, () => new Array(26).fill(INF));

    const first = idx(word[0]);
    for (let j = 0; j < 26; ++j) {
        dp[first][j] = 0;
        dp[j][first] = 0;
    }

    for (let pos = 1; pos < n; ++pos) {
        const cur = idx(word[pos]);
        const ndp = Array.from({ length: 26 }, () => new Array(26).fill(INF));
        for (let a = 0; a < 26; ++a) {
            for (let b = 0; b < 26; ++b) {
                const val = dp[a][b];
                if (val === INF) continue;
                // move finger at a
                let costA = val + dist[a][cur];
                if (costA < ndp[cur][b]) ndp[cur][b] = costA;
                // move finger at b
                let costB = val + dist[b][cur];
                if (costB < ndp[a][cur]) ndp[a][cur] = costB;
            }
        }
        dp = ndp;
    }

    let ans = INF;
    for (let a = 0; a < 26; ++a) {
        for (let b = 0; b < 26; ++b) {
            if (dp[a][b] < ans) ans = dp[a][b];
        }
    }
    return ans;
};
```

## Typescript

```typescript
function minimumDistance(word: string): number {
    const n = word.length;
    if (n <= 1) return 0;

    const row = new Array(26);
    const col = new Array(26);
    for (let i = 0; i < 26; i++) {
        row[i] = Math.floor(i / 6);
        col[i] = i % 6;
    }
    const dist = (a: number, b: number): number => {
        return Math.abs(row[a] - row[b]) + Math.abs(col[a] - col[b]);
    };

    const INF = 1e9;
    let dp = new Array(26).fill(0); // after first character, other finger can be anywhere for free

    for (let i = 1; i < n; i++) {
        const cur = word.charCodeAt(i) - 65;
        const prev = word.charCodeAt(i - 1) - 65;
        const ndp = new Array(26).fill(INF);
        for (let other = 0; other < 26; other++) {
            const curCost = dp[other];
            if (curCost === INF) continue;

            // Move the finger that typed prev to cur
            const cost1 = curCost + dist(prev, cur);
            if (cost1 < ndp[other]) ndp[other] = cost1;

            // Move the other finger to cur; now prev becomes the "other" finger position
            const cost2 = curCost + dist(other, cur);
            if (cost2 < ndp[prev]) ndp[prev] = cost2;
        }
        dp = ndp;
    }

    let ans = INF;
    for (const v of dp) {
        if (v < ans) ans = v;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function minimumDistance($word) {
        $n = strlen($word);
        // Precompute Manhattan distances between all letters.
        $dist = array_fill(0, 26, array_fill(0, 26, 0));
        for ($i = 0; $i < 26; $i++) {
            $xi = intdiv($i, 6);
            $yi = $i % 6;
            for ($j = 0; $j < 26; $j++) {
                $xj = intdiv($j, 6);
                $yj = $j % 6;
                $dist[$i][$j] = abs($xi - $xj) + abs($yi - $yj);
            }
        }

        $INF = PHP_INT_MAX;
        // dp[other] = minimal cost after typing up to current position,
        // where one finger is on the last typed character and the other finger
        // is at 'other' (0..25). 26 represents "unused/undefined".
        $dp = array_fill(0, 27, $INF);
        $dp[26] = 0; // after first character, other finger not placed yet

        for ($i = 1; $i < $n; $i++) {
            $curIdx  = ord($word[$i]) - 65;
            $prevIdx = ord($word[$i - 1]) - 65;
            $newdp = array_fill(0, 27, $INF);
            for ($o = 0; $o < 27; $o++) {
                if ($dp[$o] === $INF) continue;

                // Move the finger that typed previous character.
                $cost1 = $dp[$o] + $dist[$prevIdx][$curIdx];
                if ($cost1 < $newdp[$o]) {
                    $newdp[$o] = $cost1;
                }

                // Use the other finger to type current character.
                $moveDist = ($o == 26) ? 0 : $dist[$o][$curIdx];
                $cost2 = $dp[$o] + $moveDist;
                if ($cost2 < $newdp[$prevIdx]) {
                    $newdp[$prevIdx] = $cost2;
                }
            }
            $dp = $newdp;
        }

        // Minimum over all possible positions of the unused finger.
        $ans = $INF;
        foreach ($dp as $val) {
            if ($val < $ans) $ans = $val;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimumDistance(_ word: String) -> Int {
        // Convert characters to indices 0..25
        var letters = [Int]()
        for scalar in word.unicodeScalars {
            let idx = Int(scalar.value - 65) // 'A' ASCII is 65
            letters.append(idx)
        }
        let n = letters.count
        if n <= 1 { return 0 }
        
        // Distance between two letters based on 6-column layout
        func dist(_ a: Int, _ b: Int) -> Int {
            let ra = a / 6
            let ca = a % 6
            let rb = b / 6
            let cb = b % 6
            return abs(ra - rb) + abs(ca - cb)
        }
        
        // dp[other] = minimal cost after processing up to current position,
        // where the finger that typed the last character is at letters[i],
        // and the other finger is at 'other'.
        var dp = Array(repeating: 0, count: 26) // after first character, cost zero for any other position
        
        for i in 1..<n {
            let cur = letters[i]
            let prev = letters[i - 1]
            var newDp = Array(repeating: Int.max / 2, count: 26)
            for other in 0..<26 {
                let currentCost = dp[other]
                
                // Move the same finger (which is at 'prev') to 'cur'
                let costSame = currentCost + dist(prev, cur)
                if costSame < newDp[other] {
                    newDp[other] = costSame
                }
                
                // Use the other finger to type 'cur'
                let costOther = currentCost + dist(other, cur)
                if costOther < newDp[prev] {
                    newDp[prev] = costOther
                }
            }
            dp = newDp
        }
        
        return dp.min() ?? 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumDistance(word: String): Int {
        if (word.isEmpty()) return 0
        val INF = 1_000_000_000
        // distance between two letters, index 26 means "unused" with zero cost
        fun dist(a: Int, b: Int): Int {
            if (a == 26 || b == 26) return 0
            val ax = a / 6
            val ay = a % 6
            val bx = b / 6
            val by = b % 6
            return kotlin.math.abs(ax - bx) + kotlin.math.abs(ay - by)
        }

        var dp = Array(27) { IntArray(27) { INF } }
        val first = word[0] - 'A'
        dp[first][26] = 0  // place first finger on the first character, other finger unused

        for (pos in 1 until word.length) {
            val nxt = word[pos] - 'A'
            val ndp = Array(27) { IntArray(27) { INF } }
            for (i in 0..26) {
                for (j in 0..26) {
                    val cur = dp[i][j]
                    if (cur == INF) continue
                    // move the finger that typed previous character (at i)
                    val cost1 = cur + dist(i, nxt)
                    if (cost1 < ndp[nxt][j]) ndp[nxt][j] = cost1
                    // move the other finger (at j)
                    val cost2 = cur + dist(j, nxt)
                    if (cost2 < ndp[nxt][i]) ndp[nxt][i] = cost2
                }
            }
            dp = ndp
        }

        var ans = INF
        for (i in 0..26) {
            for (j in 0..26) {
                if (dp[i][j] < ans) ans = dp[i][j]
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minimumDistance(String word) {
    if (word.length <= 1) return 0;
    List<int> w = word.codeUnits.map((c) => c - 65).toList();
    const int INF = 1 << 30;
    List<int> dp = List.filled(26, 0); // after first char, other finger can be anywhere with zero cost
    for (int i = 1; i < w.length; i++) {
      int cur = w[i];
      int prev = w[i - 1];
      List<int> ndp = List.filled(26, INF);
      for (int other = 0; other < 26; other++) {
        int base = dp[other];
        if (base == INF) continue;
        // move finger that was on prev to cur
        int cost1 = base + _dist(prev, cur);
        if (cost1 < ndp[other]) ndp[other] = cost1;
        // move the other finger to cur
        int cost2 = base + _dist(other, cur);
        if (cost2 < ndp[prev]) ndp[prev] = cost2;
      }
      dp = ndp;
    }
    int ans = INF;
    for (int v in dp) {
      if (v < ans) ans = v;
    }
    return ans;
  }

  int _dist(int a, int b) {
    int ra = a ~/ 6, ca = a % 6;
    int rb = b ~/ 6, cb = b % 6;
    return (ra - rb).abs() + (ca - cb).abs();
  }
}
```

## Golang

```go
package main

import "math"

func minimumDistance(word string) int {
	if len(word) <= 1 {
		return 0
	}

	// Precompute positions of each letter on the keyboard.
	var posX, posY [26]int
	rows := []string{
		"ABCDE",
		"FGHIJ",
		"KLMNO",
		"PQRST",
		"UVWXY",
		"Z",
	}
	for r, row := range rows {
		for c, ch := range row {
			idx := int(ch - 'A')
			posX[idx] = r
			posY[idx] = c
		}
	}
	dist := func(a, b int) int {
		return int(math.Abs(float64(posX[a]-posX[b]))) + int(math.Abs(float64(posY[a]-posY[b])))
	}

	const INF = 1 << 30
	dp := make([]int, 26)
	for i := 0; i < 26; i++ {
		dp[i] = 0 // after typing first character, other finger can be anywhere for free
	}
	prev := int(word[0] - 'A')

	for i := 1; i < len(word); i++ {
		cur := int(word[i] - 'A')
		ndp := make([]int, 26)
		for j := 0; j < 26; j++ {
			ndp[j] = INF
		}
		for other := 0; other < 26; other++ {
			if dp[other] == INF {
				continue
			}
			// Use the finger that typed prev to type cur.
			cost1 := dp[other] + dist(prev, cur)
			if cost1 < ndp[other] {
				ndp[other] = cost1
			}
			// Use the other finger (at position 'other') to type cur.
			cost2 := dp[other] + dist(other, cur)
			if cost2 < ndp[prev] {
				ndp[prev] = cost2
			}
		}
		dp = ndp
		prev = cur
	}

	ans := INF
	for i := 0; i < 26; i++ {
		if dp[i] < ans {
			ans = dp[i]
		}
	}
	return ans
}
```

## Ruby

```ruby
# @param {String} word
# @return {Integer}
def minimum_distance(word)
  n = word.length
  return 0 if n <= 1

  idxs = word.bytes.map { |b| b - 65 } # 'A' => 0

  # precompute Manhattan distances on the 6x5 grid (last row has only Z)
  dist = Array.new(26) { Array.new(26, 0) }
  (0...26).each do |i|
    ri = i / 6
    ci = i % 6
    (0...26).each do |j|
      rj = j / 6
      cj = j % 6
      dist[i][j] = (ri - rj).abs + (ci - cj).abs
    end
  end

  INF = 1 << 60
  dp = Array.new(27, INF) # index 26 represents "unused" other finger
  dp[26] = 0

  (1...n).each do |pos|
    cur = idxs[pos - 1]
    nxt = idxs[pos]
    new_dp = Array.new(27, INF)

    (0..26).each do |other|
      cost = dp[other]
      next if cost >= INF

      # Use the same finger that typed previous character
      c1 = cost + dist[cur][nxt]
      new_dp[other] = c1 if c1 < new_dp[other]

      # Use the other finger to type current character
      move_cost = (other == 26) ? 0 : dist[other][nxt]
      new_other = cur
      c2 = cost + move_cost
      new_dp[new_other] = c2 if c2 < new_dp[new_other]
    end

    dp = new_dp
  end

  dp.min
end
```

## Scala

```scala
object Solution {
    def minimumDistance(word: String): Int = {
        val rows = Array.ofDim[Int](26)
        val cols = Array.ofDim[Int](26)
        for (i <- 0 until 26) {
            rows(i) = i / 5
            cols(i) = i % 5
        }
        def dist(a: Int, b: Int): Int =
            Math.abs(rows(a) - rows(b)) + Math.abs(cols(a) - cols(b))

        val INF = 1 << 30
        var dp = Array.fill(26)(0) // after first character, other finger can be anywhere with zero cost

        val chars = word.map(c => c - 'A')
        for (idx <- 0 until chars.length - 1) {
            val cur = chars(idx)
            val nxt = chars(idx + 1)
            val newDp = Array.fill(26)(INF)
            for (j <- 0 until 26) {
                val cost = dp(j)
                // same finger types next
                var c1 = cost + dist(cur, nxt)
                if (c1 < newDp(j)) newDp(j) = c1
                // other finger types next
                var c2 = cost + dist(j, nxt)
                if (c2 < newDp(cur)) newDp(cur) = c2
            }
            dp = newDp
        }
        dp.min
    }
}
```

## Rust

```rust
fn distance(a: usize, b: usize) -> i32 {
    let ra = a / 6;
    let ca = a % 6;
    let rb = b / 6;
    let cb = b % 6;
    ((ra as i32 - rb as i32).abs() + (ca as i32 - cb as i32).abs())
}

impl Solution {
    pub fn minimum_distance(word: String) -> i32 {
        let bytes = word.as_bytes();
        let n = bytes.len();
        if n <= 1 {
            return 0;
        }
        let chars: Vec<usize> = bytes.iter().map(|&b| (b - b'A') as usize).collect();

        const INF: i32 = 1_000_000_000;
        // dp[j] = min cost where the other finger is at letter j (0..25) or unused (26)
        let mut dp = vec![INF; 27];
        dp[26] = 0;

        for i in 1..n {
            let prev = chars[i - 1];
            let cur = chars[i];
            let mut ndp = vec![INF; 27];
            for j in 0..27 {
                let val = dp[j];
                if val == INF {
                    continue;
                }
                // Use the same finger that typed previous character
                let cost_same = distance(prev, cur);
                let new_val = val + cost_same;
                if new_val < ndp[j] {
                    ndp[j] = new_val;
                }

                // Use the other finger
                let cost_other = if j == 26 { 0 } else { distance(j, cur) };
                let new_j = prev; // now the other finger is at previous character
                let new_val2 = val + cost_other;
                if new_val2 < ndp[new_j] {
                    ndp[new_j] = new_val2;
                }
            }
            dp = ndp;
        }

        *dp.iter().min().unwrap()
    }
}
```

## Racket

```racket
(define/contract (minimum-distance word)
  (-> string? exact-integer?)
  (let* ((n (string-length word))
         (chars
          (for/vector ([i (in-range n)])
            (- (char->integer (string-ref word i))
               (char->integer #\A)))))
    (if (= n 1)
        0
        (let* ((INF 1000000000)
               (dp (make-vector 26 INF)))
          ;; after typing first character, cost is zero regardless of other finger position
          (for ([pos (in-range 26)]) (vector-set! dp pos 0))
          (define (dist a b)
            (let* ((ax (modulo a 6)) (ay (quotient a 6))
                   (bx (modulo b 6)) (by (quotient b 6)))
              (+ (abs (- ax bx)) (abs (- ay by)))))
          (let recur ((i 1) (prev (vector-ref chars 0)) (dp dp))
            (if (= i n)
                (apply min (vector->list dp))
                (let* ((cur (vector-ref chars i))
                       (newdp (make-vector 26 INF)))
                  (for ([other (in-range 26)])
                    (define curcost (vector-ref dp other))
                    (when (< curcost INF)
                      ;; move the finger that typed previous character
                      (let ((c1 (+ curcost (dist prev cur))))
                        (when (< c1 (vector-ref newdp other))
                          (vector-set! newdp other c1)))
                      ;; move the other finger to type current character
                      (let ((c2 (+ curcost (dist other cur))))
                        (when (< c2 (vector-ref newdp prev))
                          (vector-set! newdp prev c2)))))
                  (recur (+ i 1) cur newdp)))))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_distance/1]).
-spec minimum_distance(Word :: unicode:unicode_binary()) -> integer().
minimum_distance(Word) ->
    CharList = unicode:characters_to_list(Word),
    case CharList of
        [] -> 0;
        [_] -> 0;
        [First|Rest] ->
            FirstIdx = First - $A,
            DP0 = erlang:make_tuple(26, 0),
            process(Rest, FirstIdx, DP0)
    end.

process([], _PrevIdx, DP) ->
    min_in_tuple(DP);
process([CurChar|Tail], PrevIdx, DP) ->
    CurIdx = CurChar - $A,
    NewDP = update_dp(DP, PrevIdx, CurIdx),
    process(Tail, CurIdx, NewDP).

update_dp(DP, PrevIdx, CurIdx) ->
    INF = 1 bsl 30,
    Empty = erlang:make_tuple(26, INF),
    update_loop(0, DP, PrevIdx, CurIdx, Empty).

update_loop(26, _DP, _PrevIdx, _CurIdx, NewDP) ->
    NewDP;
update_loop(AIdx, DP, PrevIdx, CurIdx, NewDP) ->
    Pos = AIdx + 1,
    DPVal = element(Pos, DP),

    %% keep same finger
    SameOld = element(Pos, NewDP),
    NewDP1 = if DPVal < SameOld -> setelement(Pos, NewDP, DPVal); true -> NewDP end,

    %% move other finger from AIdx to CurIdx
    Dist = manhattan(AIdx, CurIdx),
    Cost = DPVal + Dist,
    PrevPos = PrevIdx + 1,
    PrevOld = element(PrevPos, NewDP1),
    NewDP2 = if Cost < PrevOld -> setelement(PrevPos, NewDP1, Cost); true -> NewDP1 end,

    update_loop(AIdx + 1, DP, PrevIdx, CurIdx, NewDP2).

manhattan(I1, I2) ->
    {X1, Y1} = pos(I1),
    {X2, Y2} = pos(I2),
    abs(X1 - X2) + abs(Y1 - Y2).

pos(Index) ->
    Row = Index div 5,
    Col = Index rem 5,
    {Col, Row}.

min_in_tuple(Tuple) ->
    Min0 = element(1, Tuple),
    lists:foldl(fun(I, Acc) ->
        Val = element(I, Tuple),
        if Val < Acc -> Val; true -> Acc end
    end, Min0, lists:seq(2, 26)).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_distance(word :: String.t()) :: integer()
  def minimum_distance(word) do
    chars = String.to_charlist(word) |> Enum.map(&(&1 - ?A))
    sentinel = 26

    manhattan = fn
      (a, _) when a == sentinel -> 0
      (_, b) when b == sentinel -> 0
      (a, b) ->
        row_a = div(a, 6)
        col_a = rem(a, 6)
        row_b = div(b, 6)
        col_b = rem(b, 6)
        abs(row_a - row_b) + abs(col_a - col_b)
    end

    [first | rest] = chars
    dp = %{sentinel => 0}
    prev = first

    Enum.reduce(rest, {dp, prev}, fn cur, {dp_acc, prev_char} ->
      new_dp = %{}
      Enum.each(dp_acc, fn {k, val} ->
        # Use the same finger that typed previous character
        cost1 = val + manhattan.(prev_char, cur)
        new_dp =
          case Map.get(new_dp, k) do
            nil -> Map.put(new_dp, k, cost1)
            existing when cost1 < existing -> Map.put(new_dp, k, cost1)
            _ -> new_dp
          end

        # Use the other finger (idle finger)
        cost2 = val + manhattan.(k, cur)
        new_dp =
          case Map.get(new_dp, prev_char) do
            nil -> Map.put(new_dp, prev_char, cost2)
            existing when cost2 < existing -> Map.put(new_dp, prev_char, cost2)
            _ -> new_dp
          end
      end)

      {new_dp, cur}
    end)
    |> (fn {final_dp, _} ->
      final_dp
      |> Map.values()
      |> Enum.min()
    end)
  end
end
```
