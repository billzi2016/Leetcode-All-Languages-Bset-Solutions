# 3445. Maximum Difference Between Even and Odd Frequency II

## Cpp

```cpp
class Solution {
public:
    int maxDifference(string s, int k) {
        int n = s.size();
        vector<int> d(n);
        for (int i = 0; i < n; ++i) d[i] = s[i] - '0';
        const int INF = 1e9;
        int answer = -INF;
        for (int a = 0; a <= 4; ++a) {
            for (int b = 0; b <= 4; ++b) {
                if (a == b) continue;
                vector<int> prefA(n + 1, 0), prefB(n + 1, 0);
                for (int i = 0; i < n; ++i) {
                    prefA[i + 1] = prefA[i] + (d[i] == a);
                    prefB[i + 1] = prefB[i] + (d[i] == b);
                }
                int best[4];
                for (int t = 0; t < 4; ++t) best[t] = INF;
                int L = 0;
                for (int i = 1; i <= n; ++i) {
                    while (L <= i - k && prefB[i] - prefB[L] >= 2) {
                        int statusL = ((prefA[L] & 1) << 1) | (prefB[L] & 1);
                        int valL = prefA[L] - prefB[L];
                        if (valL < best[statusL]) best[statusL] = valL;
                        ++L;
                    }
                    int statusR = ((prefA[i] & 1) << 1) | (prefB[i] & 1);
                    int target = statusR ^ 2; // need parity difference 10b
                    if (best[target] != INF) {
                        int cand = (prefA[i] - prefB[i]) - best[target];
                        if (cand > answer) answer = cand;
                    }
                }
            }
        }
        return answer;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int maxDifference(String s, int k) {
        int n = s.length();
        int answer = -1;
        for (int a = 0; a <= 4; ++a) {
            for (int b = 0; b <= 4; ++b) {
                if (a == b) continue;
                int[] prefA = new int[n + 1];
                int[] prefB = new int[n + 1];
                for (int i = 0; i < n; ++i) {
                    char ch = s.charAt(i);
                    prefA[i + 1] = prefA[i] + ((ch - '0') == a ? 1 : 0);
                    prefB[i + 1] = prefB[i] + ((ch - '0') == b ? 1 : 0);
                }
                int[] best = new int[4];
                Arrays.fill(best, Integer.MAX_VALUE);
                int leftIdx = 0;
                for (int r = 1; r <= n; ++r) {
                    while (leftIdx <= r - k && prefB[leftIdx] <= prefB[r] - 2) {
                        int state = ((prefA[leftIdx] & 1) << 1) | (prefB[leftIdx] & 1);
                        int val = prefA[leftIdx] - prefB[leftIdx];
                        if (val < best[state]) best[state] = val;
                        leftIdx++;
                    }
                    int curState = ((prefA[r] & 1) << 1) | (prefB[r] & 1);
                    int targetState = curState ^ 0b10; // flip parity of a
                    if (best[targetState] != Integer.MAX_VALUE) {
                        int cand = (prefA[r] - prefB[r]) - best[targetState];
                        if (cand > answer) answer = cand;
                    }
                }
            }
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def maxDifference(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        digits = ['0', '1', '2', '3', '4']
        INF = 10**9
        answer = -INF

        for a in digits:
            for b in digits:
                if a == b:
                    continue
                # prefix counts for a and b
                prefA = [0] * (n + 1)
                prefB = [0] * (n + 1)
                for i, ch in enumerate(s):
                    prefA[i + 1] = prefA[i] + (ch == a)
                    prefB[i + 1] = prefB[i] + (ch == b)

                best = [INF] * 4          # minimal (prev_a - prev_b) for each status
                left_entries = []         # (prefB[left], status, value)
                ptr = 0

                for right in range(k - 1, n):
                    # add new possible left index due to length constraint
                    left_idx = right - k + 1
                    status_left = ((prefA[left_idx] & 1) << 1) | (prefB[left_idx] & 1)
                    val_left = prefA[left_idx] - prefB[left_idx]
                    left_entries.append((prefB[left_idx], status_left, val_left))

                    cur_prefB = prefB[right + 1]

                    # move pointer to include entries where b count difference >=2
                    while ptr < len(left_entries) and left_entries[ptr][0] <= cur_prefB - 2:
                        _, st, v = left_entries[ptr]
                        if v < best[st]:
                            best[st] = v
                        ptr += 1

                    cntA = prefA[right + 1]
                    cntB = prefB[right + 1]
                    status_right = ((cntA & 1) << 1) | (cntB & 1)
                    need_status = status_right ^ 2   # flip a parity only

                    if best[need_status] != INF:
                        cand = (cntA - cntB) - best[need_status]
                        if cand > answer:
                            answer = cand

        return answer
```

## Python3

```python
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        # prefix counts for digits 0..4
        pref = [[0] * (n + 1) for _ in range(5)]
        for i, ch in enumerate(s):
            d = ord(ch) - 48
            for dig in range(5):
                pref[dig][i + 1] = pref[dig][i] + (1 if dig == d else 0)

        INF = float('inf')
        ans = -10**9

        for a in range(5):
            for b in range(5):
                if a == b:
                    continue
                # lists per parity state storing (pb, pa-pb)
                lsts = [[] for _ in range(4)]
                ptr = [0] * 4
                best_active = [INF] * 4

                for r in range(n):
                    ca = pref[a][r + 1]
                    cb = pref[b][r + 1]

                    l = r - k + 1
                    if l >= 0:
                        pa = pref[a][l]
                        pb = pref[b][l]
                        state = ((pa & 1) << 1) | (pb & 1)
                        lsts[state].append((pb, pa - pb))

                    limit = cb - 2
                    if limit >= 0:
                        for st in range(4):
                            cur_lst = lsts[st]
                            p = ptr[st]
                            while p < len(cur_lst) and cur_lst[p][0] <= limit:
                                val = cur_lst[p][1]
                                if val < best_active[st]:
                                    best_active[st] = val
                                p += 1
                            ptr[st] = p

                    state_r = ((ca & 1) << 1) | (cb & 1)
                    need = state_r ^ 2  # xor with binary 10
                    if best_active[need] != INF:
                        diff = (ca - cb) - best_active[need]
                        if diff > ans:
                            ans = diff

        return ans
```

## C

```c
#include <string.h>
#include <stdlib.h>
#include <limits.h>

int maxDifference(char* s, int k) {
    int n = (int)strlen(s);
    const int INF = INT_MAX / 2;
    int answer = -INF;

    for (int a = 0; a <= 4; ++a) {
        for (int b = 0; b <= 4; ++b) if (a != b) {
            // prefix counts
            int *prefA = (int*)malloc((n + 1) * sizeof(int));
            int *prefB = (int*)malloc((n + 1) * sizeof(int));
            prefA[0] = prefB[0] = 0;
            for (int i = 1; i <= n; ++i) {
                prefA[i] = prefA[i - 1] + ((s[i - 1] - '0') == a);
                prefB[i] = prefB[i - 1] + ((s[i - 1] - '0') == b);
            }
            int maxCntB = prefB[n];

            // exact minima for each parity state and count of b
            int **exact = (int**)malloc(4 * sizeof(int*));
            for (int st = 0; st < 4; ++st) {
                exact[st] = (int*)malloc((maxCntB + 1) * sizeof(int));
                for (int i = 0; i <= maxCntB; ++i) exact[st][i] = INF;
            }

            int curPtr[4] = {0, 0, 0, 0};
            int curMin[4];
            for (int i = 0; i < 4; ++i) curMin[i] = INF;

            // iterate over right endpoint r (prefix length)
            for (int r = k; r <= n; ++r) {
                int l = r - k; // new left index becomes eligible
                int cntA_l = prefA[l];
                int cntB_l = prefB[l];
                int D_l = cntA_l - cntB_l;
                int state_l = ((cntA_l & 1) << 1) | (cntB_l & 1);
                if (D_l < exact[state_l][cntB_l]) exact[state_l][cntB_l] = D_l;

                int cntA_r = prefA[r];
                int cntB_r = prefB[r];
                int D_r = cntA_r - cntB_r;
                int state_r = ((cntA_r & 1) << 1) | (cntB_r & 1);
                int need_state = state_r ^ 2; // xor with binary 10
                int limit = cntB_r - 2;

                if (limit >= 0) {
                    while (curPtr[need_state] <= limit && curPtr[need_state] <= maxCntB) {
                        int c = curPtr[need_state];
                        if (exact[need_state][c] < curMin[need_state])
                            curMin[need_state] = exact[need_state][c];
                        ++curPtr[need_state];
                    }
                    if (curMin[need_state] != INF) {
                        int cand = D_r - curMin[need_state];
                        if (cand > answer) answer = cand;
                    }
                }
            }

            // free memory for this pair
            for (int st = 0; st < 4; ++st) free(exact[st]);
            free(exact);
            free(prefA);
            free(prefB);
        }
    }
    return answer;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MaxDifference(string s, int k) {
        int n = s.Length;
        int[] digits = new int[n];
        for (int i = 0; i < n; i++) digits[i] = s[i] - '0';
        const int INF = 1 << 30;
        int answer = int.MinValue;

        for (int a = 0; a <= 4; a++) {
            for (int b = 0; b <= 4; b++) {
                if (a == b) continue;

                int[] prefA = new int[n + 1];
                int[] prefB = new int[n + 1];
                for (int i = 0; i < n; i++) {
                    prefA[i + 1] = prefA[i] + (digits[i] == a ? 1 : 0);
                    prefB[i + 1] = prefB[i] + (digits[i] == b ? 1 : 0);
                }

                int[] best = new int[4];
                for (int i = 0; i < 4; i++) best[i] = INF;

                int leftIdx = 0;
                for (int r = 1; r <= n; r++) {
                    int cntA = prefA[r];
                    int cntB = prefB[r];

                    while (leftIdx <= r && (r - leftIdx) >= k && (cntB - prefB[leftIdx]) >= 2) {
                        int statusLeft = ((prefA[leftIdx] & 1) << 1) | (prefB[leftIdx] & 1);
                        int val = prefA[leftIdx] - prefB[leftIdx];
                        if (val < best[statusLeft]) best[statusLeft] = val;
                        leftIdx++;
                    }

                    int statusRight = ((cntA & 1) << 1) | (cntB & 1);
                    int needStatus = statusRight ^ 2; // XOR with binary 10
                    if (best[needStatus] != INF) {
                        int cur = (cntA - cntB) - best[needStatus];
                        if (cur > answer) answer = cur;
                    }
                }
            }
        }

        return answer;
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
var maxDifference = function(s, k) {
    const n = s.length;
    const digits = [0, 1, 2, 3, 4];
    let answer = -1e9;

    for (let aIdx = 0; aIdx < 5; ++aIdx) {
        const aChar = aIdx + 48; // ASCII code
        for (let bIdx = 0; bIdx < 5; ++bIdx) {
            if (aIdx === bIdx) continue;
            const bChar = bIdx + 48;

            // prefix counts for characters a and b
            const preA = new Int32Array(n + 1);
            const preB = new Int32Array(n + 1);
            for (let i = 0; i < n; ++i) {
                preA[i + 1] = preA[i] + (s.charCodeAt(i) === aChar ? 1 : 0);
                preB[i + 1] = preB[i] + (s.charCodeAt(i) === bChar ? 1 : 0);
            }

            const INF = 1e9;
            const best = [INF, INF, INF, INF]; // for status 00,01,10,11
            let left = 0;

            for (let right = 0; right < n; ++right) {
                const cntA = preA[right + 1];
                const cntB = preB[right + 1];

                while (
                    left <= right &&
                    (right - left + 1) >= k &&
                    (cntB - preB[left]) >= 2
                ) {
                    const statusLeft = ((preA[left] & 1) << 1) | (preB[left] & 1);
                    const val = preA[left] - preB[left];
                    if (val < best[statusLeft]) best[statusLeft] = val;
                    ++left;
                }

                const statusRight = ((cntA & 1) << 1) | (cntB & 1);
                const needStatus = statusRight ^ 2; // xor with binary 10
                if (best[needStatus] !== INF) {
                    const cur = (cntA - cntB) - best[needStatus];
                    if (cur > answer) answer = cur;
                }
            }
        }
    }

    return answer;
};
```

## Typescript

```typescript
function maxDifference(s: string, k: number): number {
    const n = s.length;
    const pref: Int32Array[] = [];
    for (let d = 0; d < 5; ++d) pref.push(new Int32Array(n + 1));
    for (let i = 0; i < n; ++i) {
        const digit = s.charCodeAt(i) - 48;
        for (let d = 0; d < 5; ++d) {
            pref[d][i + 1] = pref[d][i] + (d === digit ? 1 : 0);
        }
    }

    let answer = -Infinity;

    for (let a = 0; a < 5; ++a) {
        for (let b = 0; b < 5; ++b) {
            if (a === b) continue;
            const prefA = pref[a];
            const prefB = pref[b];
            const best = [Infinity, Infinity, Infinity, Infinity];
            let left = 0;

            for (let r = 0; r < n; ++r) {
                const curA = prefA[r + 1];
                const curB = prefB[r + 1];

                while (
                    left <= r &&
                    (r - left + 1) >= k &&
                    (curB - prefB[left]) >= 2
                ) {
                    const stateLeft = ((prefA[left] & 1) << 1) | (prefB[left] & 1);
                    const diff = prefA[left] - prefB[left];
                    if (diff < best[stateLeft]) best[stateLeft] = diff;
                    left++;
                }

                const stateRight = ((curA & 1) << 1) | (curB & 1);
                const needState = stateRight ^ 2; // toggle a parity
                const minDiff = best[needState];
                if (minDiff !== Infinity) {
                    const candidate = (curA - curB) - minDiff;
                    if (candidate > answer) answer = candidate;
                }
            }
        }
    }

    return answer;
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
    function maxDifference($s, $k) {
        $n = strlen($s);
        // prefix[d][i] = count of digit d in s[0..i-1]
        $prefix = array_fill(0, 5, array_fill(0, $n + 1, 0));
        for ($i = 0; $i < $n; $i++) {
            $digit = intval($s[$i]);
            for ($d = 0; $d < 5; $d++) {
                $prefix[$d][$i + 1] = $prefix[$d][$i];
            }
            $prefix[$digit][$i + 1]++;
        }

        $ans = PHP_INT_MIN;
        for ($a = 0; $a < 5; $a++) {
            for ($b = 0; $b < 5; $b++) {
                if ($a == $b) continue;
                $best = array_fill(0, 4, PHP_INT_MAX);
                $left = 0;
                for ($right = 1; $right <= $n; $right++) {
                    $cntA = $prefix[$a][$right];
                    $cntB = $prefix[$b][$right];

                    while ($right - $left >= $k && ($cntB - $prefix[$b][$left]) >= 2) {
                        $status = (($prefix[$a][$left] % 2) << 1) | ($prefix[$b][$left] % 2);
                        $value = $prefix[$a][$left] - $prefix[$b][$left];
                        if ($value < $best[$status]) {
                            $best[$status] = $value;
                        }
                        $left++;
                    }

                    $needStatus = ((($cntA % 2) ^ 1) << 1) | ($cntB % 2);
                    if ($best[$needStatus] != PHP_INT_MAX) {
                        $candidate = ($cntA - $cntB) - $best[$needStatus];
                        if ($candidate > $ans) {
                            $ans = $candidate;
                        }
                    }
                }
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxDifference(_ s: String, _ k: Int) -> Int {
        let n = s.count
        let chars = Array(s)
        var answer = Int.min

        // Convert characters to integer values 0-4 once
        var vals = [Int](repeating: 0, count: n)
        for i in 0..<n {
            if let scalar = chars[i].unicodeScalars.first {
                vals[i] = Int(scalar.value - 48)   // '0' ascii is 48
            }
        }

        let INF = Int.max / 2

        for a in 0...4 {
            for b in 0...4 where b != a {
                var prefA = [Int](repeating: 0, count: n + 1)
                var prefB = [Int](repeating: 0, count: n + 1)

                for i in 0..<n {
                    prefA[i + 1] = prefA[i] + (vals[i] == a ? 1 : 0)
                    prefB[i + 1] = prefB[i] + (vals[i] == b ? 1 : 0)
                }

                var best = [Int](repeating: INF, count: 4)
                var addIdx = 0

                if k <= n {
                    for right in (k - 1)..<n {
                        let totalA = prefA[right + 1]
                        let totalB = prefB[right + 1]

                        // Add eligible left positions
                        while addIdx <= right - k + 1 && prefB[addIdx] <= totalB - 2 {
                            let statusLeft = ((prefA[addIdx] & 1) << 1) | (prefB[addIdx] & 1)
                            let diffPrev = prefA[addIdx] - prefB[addIdx]
                            if diffPrev < best[statusLeft] {
                                best[statusLeft] = diffPrev
                            }
                            addIdx += 1
                        }

                        let statusRight = ((totalA & 1) << 1) | (totalB & 1)
                        let neededStatus = statusRight ^ 2   // XOR with binary 10

                        if best[neededStatus] != INF {
                            let candidate = (totalA - totalB) - best[neededStatus]
                            if candidate > answer {
                                answer = candidate
                            }
                        }
                    }
                }
            }
        }

        return answer
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    fun maxDifference(s: String, k: Int): Int {
        val n = s.length
        var globalAns = Int.MIN_VALUE
        val INF = 1_000_000_000

        for (a in 0..4) {
            for (b in 0..4) {
                if (a == b) continue

                // prefix counts for a and b
                val prefA = IntArray(n + 1)
                val prefB = IntArray(n + 1)
                for (i in 0 until n) {
                    prefA[i + 1] = prefA[i] + if (s[i] - '0' == a) 1 else 0
                    prefB[i + 1] = prefB[i] + if (s[i] - '0' == b) 1 else 0
                }

                val best = IntArray(4) { INF }
                var addIdx = 0
                var ansPair = Int.MIN_VALUE

                for (r in 1..n) {
                    // add eligible left positions
                    while (addIdx <= r - k && prefB[r] - prefB[addIdx] >= 2) {
                        val status = ((prefA[addIdx] and 1) shl 1) or (prefB[addIdx] and 1)
                        val value = prefA[addIdx] - prefB[addIdx]
                        if (value < best[status]) best[status] = value
                        addIdx++
                    }

                    val statusR = ((prefA[r] and 1) shl 1) or (prefB[r] and 1)
                    val targetStatus = statusR xor 2 // flip a parity only

                    if (best[targetStatus] != INF) {
                        val cand = (prefA[r] - prefB[r]) - best[targetStatus]
                        if (cand > ansPair) ansPair = cand
                    }
                }

                if (ansPair > globalAns) globalAns = ansPair
            }
        }
        return globalAns
    }
}
```

## Dart

```dart
class Solution {
  int maxDifference(String s, int k) {
    const int INF = 1 << 60;
    int n = s.length;
    int globalAns = -INF;

    for (int a = 0; a < 5; ++a) {
      for (int b = 0; b < 5; ++b) {
        if (a == b) continue;

        // prefix counts for characters a and b
        List<int> prefA = List.filled(n + 1, 0);
        List<int> prefB = List.filled(n + 1, 0);
        for (int i = 0; i < n; ++i) {
          int digit = s.codeUnitAt(i) - 48;
          prefA[i + 1] = prefA[i] + (digit == a ? 1 : 0);
          prefB[i + 1] = prefB[i] + (digit == b ? 1 : 0);
        }

        List<int> best = List.filled(4, INF);
        int left = 0;

        for (int right = 0; right < n; ++right) {
          // advance left while the current window satisfies length and even count constraints
          while (left <= right &&
              (right - left + 1) >= k &&
              (prefB[right + 1] - prefB[left]) >= 2) {
            int statusLeft = ((prefA[left] & 1) << 1) | (prefB[left] & 1);
            int val = prefA[left] - prefB[left];
            if (val < best[statusLeft]) best[statusLeft] = val;
            left++;
          }

          int statusRight = ((prefA[right + 1] & 1) << 1) | (prefB[right + 1] & 1);
          int need = statusRight ^ 2; // toggle parity of a
          if (best[need] != INF) {
            int diff = (prefA[right + 1] - prefB[right + 1]) - best[need];
            if (diff > globalAns) globalAns = diff;
          }
        }
      }
    }

    return globalAns;
  }
}
```

## Golang

```go
package main

import (
	"math"
)

type pair struct {
	state int
	diff  int
}

func maxDifference(s string, k int) int {
	n := len(s)
	const INF = math.MaxInt32
	ans := -INF
	found := false

	for a := byte('0'); a <= '4'; a++ {
		for b := byte('0'); b <= '4'; b++ {
			if a == b {
				continue
			}
			// prefix counts
			aPref := make([]int, n+1)
			bPref := make([]int, n+1)
			for i := 0; i < n; i++ {
				aPref[i+1] = aPref[i]
				bPref[i+1] = bPref[i]
				if s[i] == a {
					aPref[i+1]++
				}
				if s[i] == b {
					bPref[i+1]++
				}
			}

			best := [4]int{INF, INF, INF, INF}
			buckets := make([][]pair, n+1)

			for pr := 1; pr <= n; pr++ {
				pl := pr - k
				if pl >= 0 {
					state := ((aPref[pl] % 2) << 1) | (bPref[pl] % 2)
					diff := aPref[pl] - bPref[pl]
					bcnt := bPref[pl]
					buckets[bcnt] = append(buckets[bcnt], pair{state, diff})
				}

				curB := bPref[pr]
				if curB-2 >= 0 {
					idx := curB - 2
					for _, p := range buckets[idx] {
						if p.diff < best[p.state] {
							best[p.state] = p.diff
						}
					}
					buckets[idx] = nil
				}

				statusR := ((aPref[pr] % 2) << 1) | (bPref[pr] % 2)
				need := statusR ^ 2 // binary 10
				if best[need] != INF {
					cand := (aPref[pr] - bPref[pr]) - best[need]
					if !found || cand > ans {
						ans = cand
						found = true
					}
				}
			}
		}
	}

	if !found {
		return -1
	}
	return ans
}
```

## Ruby

```ruby
def max_difference(s, k)
  digits = ['0', '1', '2', '3', '4']
  n = s.length
  ans = - (1 << 60)

  digits.each do |a|
    digits.each do |b|
      next if a == b

      pref_a = Array.new(n, 0)
      pref_b = Array.new(n, 0)
      cnt_a = 0
      cnt_b = 0
      (0...n).each do |i|
        cnt_a += 1 if s[i] == a
        cnt_b += 1 if s[i] == b
        pref_a[i] = cnt_a
        pref_b[i] = cnt_b
      end

      inf = 1 << 60
      best = Array.new(4, inf)
      best[0] = 0   # empty prefix state
      left = 0

      (0...n).each do |right|
        cur_a = pref_a[right]
        cur_b = pref_b[right]

        while left <= right && (right - left + 1) >= k
          sub_b = cur_b - (left > 0 ? pref_b[left - 1] : 0)
          break unless sub_b >= 2 && (sub_b & 1).zero?

          prev_a = left > 0 ? pref_a[left - 1] : 0
          prev_b = left > 0 ? pref_b[left - 1] : 0
          status_left = ((prev_a % 2) << 1) | (prev_b % 2)
          val = prev_a - prev_b
          best[status_left] = val if val < best[status_left]
          left += 1
        end

        status_right = ((cur_a % 2) << 1) | (cur_b % 2)
        target = status_right ^ 2   # XOR with binary 10
        if best[target] != inf
          cand = (cur_a - cur_b) - best[target]
          ans = cand if cand > ans
        end
      end
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maxDifference(s: String, k: Int): Int = {
        val n = s.length
        val digits = s.map(c => c - '0')
        var globalAns = Int.MinValue

        for (a <- 0 to 4) {
            for (b <- 0 to 4 if b != a) {
                val prefA = new Array[Int](n + 1)
                val prefB = new Array[Int](n + 1)
                val posB = scala.collection.mutable.ArrayBuffer.empty[Int]

                var i = 0
                while (i < n) {
                    val d = digits(i)
                    prefA(i + 1) = prefA(i) + (if (d == a) 1 else 0)
                    prefB(i + 1) = prefB(i) + (if (d == b) 1 else 0)
                    if (d == b) posB += i
                    i += 1
                }

                val INF = Int.MaxValue / 2
                val best = Array.fill(4)(INF)
                var addPtr = 0
                var ans = Int.MinValue

                var r = 0
                while (r < n) {
                    val cntBUpToR = prefB(r + 1)
                    var maxLeft = -1
                    if (cntBUpToR >= 2) {
                        val secondLastPos = posB(cntBUpToR - 2)
                        maxLeft = math.min(r - k + 1, secondLastPos)
                    }

                    while (addPtr <= maxLeft && addPtr <= n) {
                        val statusL = ((prefA(addPtr) & 1) << 1) | (prefB(addPtr) & 1)
                        val diffVal = prefA(addPtr) - prefB(addPtr)
                        if (diffVal < best(statusL)) best(statusL) = diffVal
                        addPtr += 1
                    }

                    val statusR = ((prefA(r + 1) & 1) << 1) | (prefB(r + 1) & 1)
                    val desired = statusR ^ 2 // toggle a parity bit
                    if (best(desired) != INF) {
                        val cand = (prefA(r + 1) - prefB(r + 1)) - best(desired)
                        if (cand > ans) ans = cand
                    }

                    r += 1
                }

                if (ans > globalAns) globalAns = ans
            }
        }

        if (globalAns == Int.MinValue) -1 else globalAns
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_difference(s: String, k: i32) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut answer = i32::MIN;
        for a in 0..5 {
            for b in 0..5 {
                if a == b { continue; }
                // prefix sums for characters a and b
                let mut pref_a = vec![0i32; n + 1];
                let mut pref_b = vec![0i32; n + 1];
                for i in 0..n {
                    pref_a[i + 1] = pref_a[i]
                        + if bytes[i] == b'0' + a as u8 { 1 } else { 0 };
                    pref_b[i + 1] = pref_b[i]
                        + if bytes[i] == b'0' + b as u8 { 1 } else { 0 };
                }
                // candidates per status: (pref_b, diff)
                let mut cand: Vec<Vec<(i32, i32)>> = vec![Vec::new(); 4];
                let mut idx = [0usize; 4];
                let mut best = [i32::MAX / 2; 4];
                let mut add_left = 0usize;
                for end in (k as usize)..=n {
                    // add new left positions that become allowed by length
                    while add_left + k as usize <= end {
                        let status = ((pref_a[add_left] % 2) << 1 | (pref_b[add_left] % 2)) as usize;
                        let diff = pref_a[add_left] - pref_b[add_left];
                        cand[status].push((pref_b[add_left], diff));
                        add_left += 1;
                    }
                    let cnt_a = pref_a[end];
                    let cnt_b = pref_b[end];
                    // update best for statuses where b count condition satisfied
                    if cnt_b >= 2 {
                        let thresh = cnt_b - 2;
                        for st in 0..4 {
                            while idx[st] < cand[st].len()
                                && cand[st][idx[st]].0 <= thresh
                            {
                                let diff = cand[st][idx[st]].1;
                                if diff < best[st] {
                                    best[st] = diff;
                                }
                                idx[st] += 1;
                            }
                        }
                    }
                    // compute candidate answer
                    let status_right =
                        ((cnt_a % 2) << 1 | (cnt_b % 2)) as usize;
                    let need = status_right ^ 2; // xor with binary 10
                    if best[need] < i32::MAX / 2 {
                        let cand_ans = (cnt_a - cnt_b) - best[need];
                        if cand_ans > answer {
                            answer = cand_ans;
                        }
                    }
                }
            }
        }
        answer
    }
}
```

## Racket

```racket
(define (max-difference s k)
  (let* ((n (string-length s))
         (arr (make-vector n)))
    (for ([i (in-range n)])
      (vector-set! arr i (- (char->integer (string-ref s i))
                            (char->integer #\0))))
    (define INF 1000000000)
    (define ans -INF)
    (for ([a (in-range 5)])
      (for ([b (in-range 5)])
        (when (not (= a b))
          (let ((left 0) (cnt-a 0) (cnt-b 0) (prev-a 0) (prev-b 0)
                (best (make-vector 4 INF)))
            (for ([right (in-range n)])
              (define ch (vector-ref arr right))
              (when (= ch a) (set! cnt-a (+ cnt-a 1)))
              (when (= ch b) (set! cnt-b (+ cnt-b 1)))
              ;; advance left while constraints are satisfied
              (let loop ()
                (when (and (>= (- right left + 1) k)
                           (>= (- cnt-b prev-b) 2))
                  (define status-left (+ (* (mod prev-a 2) 2) (mod prev-b 2)))
                  (vector-set! best status-left
                               (min (vector-ref best status-left)
                                    (- prev-a prev-b)))
                  (let ((c (vector-ref arr left)))
                    (when (= c a) (set! prev-a (- prev-a 1)))
                    (when (= c b) (set! prev-b (- prev-b 1))))
                  (set! left (+ left 1))
                  (loop)))
              ;; compute candidate answer
              (define status-right (+ (* (mod cnt-a 2) 2) (mod cnt-b 2)))
              (define need-state (bitwise-xor status-right 2)) ; binary 10 = 2
              (when (< (vector-ref best need-state) INF)
                (set! ans (max ans (- (- cnt-a cnt-b) (vector-ref best need-state)))))))))
    ans)))
```

## Erlang

```erlang
-module(solution).
-export([max_difference/2]).

-define(INF, 1000000000).

-spec max_difference(S :: unicode:unicode_binary(), K :: integer()) -> integer().
max_difference(S, K) ->
    Digits = [C - $0 || <<C>> <- binary_to_list(S)],
    N = length(Digits),
    compute_max(Digits, N, K).

%% Compute maximum over all ordered pairs (a,b), a != b
compute_max(Digits, N, K) ->
    All = lists:seq(0, 4),
    lists:foldl(fun(A, AccA) ->
        lists:foldl(fun(B, AccB) ->
            case B =:= A of
                true -> AccB;
                false ->
                    PairAns = process_pair(A, B, Digits, N, K),
                    erlang:max(AccB, PairAns)
            end
        end, AccA, All)
    end, -?INF, All).

%% Process a specific ordered pair (a,b)
process_pair(A, B, Digits, N, K) ->
    {PrefA, PrefB} = build_prefixes(Digits, A, B),
    loop(0, 0, {?INF, ?INF, ?INF, ?INF}, -?INF, N, K, PrefA, PrefB).

%% Build prefix count arrays for characters a and b
build_prefixes(Digits, A, B) ->
    N = length(Digits),
    PA0 = array:new(N + 1, {default, 0}),
    PB0 = array:new(N + 1, {default, 0}),
    build_pref(0, 0, 0, Digits, A, B, PA0, PB0).

build_pref(_Idx, _CntA, _CntB, [], _A, _B, PrefA, PrefB) ->
    {PrefA, PrefB};
build_pref(Idx, CntA, CntB, [D | Rest], A, B, PrefA, PrefB) ->
    NewCntA = CntA + (if D == A -> 1; true -> 0 end),
    NewCntB = CntB + (if D == B -> 1; true -> 0 end),
    PA2 = array:set(Idx + 1, NewCntA, PrefA),
    PB2 = array:set(Idx + 1, NewCntB, PrefB),
    build_pref(Idx + 1, NewCntA, NewCntB, Rest, A, B, PA2, PB2).

%% Main sliding window loop
loop(Right, Left, Best, Ans, N, K, PrefA, PrefB) when Right < N ->
    I = Right + 1,
    CntA = array:get(I, PrefA),
    CntB = array:get(I, PrefB),
    {NewLeft, NewBest} = move_left(Left, CntA, CntB, K, PrefA, PrefB, Best, Right),
    StatusRight = ((CntA band 1) bsl 1) bor (CntB band 1),
    Needed = StatusRight bxor 2,
    Val = element(Needed + 1, NewBest),
    UpdatedAns =
        if
            Val == ?INF -> Ans;
            true ->
                Diff = (CntA - CntB) - Val,
                erlang:max(Ans, Diff)
        end,
    loop(Right + 1, NewLeft, NewBest, UpdatedAns, N, K, PrefA, PrefB);
loop(_, _, _, Ans, _, _, _, _) -> Ans.

%% Move left pointer and update best table
move_left(Left, CntA_R, CntB_R, K, PrefA, PrefB, Best, Right) ->
    if
        Left =< Right,
        (Right - Left + 1) >= K,
        (CntB_R - array:get(Left, PrefB)) >= 2 ->
            PA = array:get(Left, PrefA),
            PB = array:get(Left, PrefB),
            StatusL = ((PA band 1) bsl 1) bor (PB band 1),
            ValL = PA - PB,
            Old = element(StatusL + 1, Best),
            NewBest = setelement(StatusL + 1, Best, erlang:min(Old, ValL)),
            move_left(Left + 1, CntA_R, CntB_R, K, PrefA, PrefB, NewBest, Right);
        true -> {Left, Best}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_difference(String.t(), integer()) :: integer()
  def max_difference(s, k) do
    import Bitwise

    digits = String.to_charlist(s) |> Enum.map(&(&1 - ?0))
    n = length(digits)
    inf = 1 <<< 60
    ans_initial = -(1 <<< 60)

    ans =
      for a <- 0..4, b <- 0..4, a != b, reduce: ans_initial do
        acc_ans ->
          # build prefix sums for characters a and b
          pref_a0 = :array.new(n + 1, default: 0)
          pref_b0 = :array.new(n + 1, default: 0)

          {pref_a, pref_b} =
            Enum.with_index(digits)
            |> Enum.reduce({pref_a0, pref_b0}, fn {val, i}, {pa, pb} ->
              prev_a = :array.get(i, pa)
              prev_b = :array.get(i, pb)

              new_a = if val == a, do: prev_a + 1, else: prev_a
              new_b = if val == b, do: prev_b + 1, else: prev_b

              { :array.set(i + 1, new_a, pa), :array.set(i + 1, new_b, pb) }
            end)

          best0 = List.duplicate(inf, 4)

          {_final_l, _best, pair_max} =
            Enum.reduce(0..(n - 1), {0, best0, acc_ans}, fn r, {l, best, cur_best} ->
              cnt_a = :array.get(r + 1, pref_a)
              cnt_b = :array.get(r + 1, pref_b)

              {l2, best2} = advance_left(r, l, cnt_b, pref_a, pref_b, best, k)

              status_right = ((cnt_a &&& 1) <<< 1) ||| (cnt_b &&& 1)
              need = Bitwise.bxor(status_right, 2)

              cur_best =
                case Enum.at(best2, need) do
                  v when v < inf ->
                    diff = (cnt_a - cnt_b) - v
                    if diff > cur_best, do: diff, else: cur_best

                  _ -> cur_best
                end

              {l2, best2, cur_best}
            end)

          if pair_max > acc_ans, do: pair_max, else: acc_ans
      end

    ans
  end

  defp advance_left(r, l, cnt_b, pref_a, pref_b, best, k) do
    import Bitwise

    if l <= r and (r - l + 1) >= k and (cnt_b - :array.get(l, pref_b)) >= 2 do
      state = ((:array.get(l, pref_a) &&& 1) <<< 1) ||| (:array.get(l, pref_b) &&& 1)
      diff = :array.get(l, pref_a) - :array.get(l, pref_b)

      best_updated =
        List.update_at(best, state, fn cur -> if diff < cur, do: diff, else: cur end)

      advance_left(r, l + 1, cnt_b, pref_a, pref_b, best_updated, k)
    else
      {l, best}
    end
  end
end
```
