# 1494. Parallel Courses II

## Cpp

```cpp
class Solution {
public:
    int minNumberOfSemesters(int n, vector<vector<int>>& relations, int k) {
        int full = (1 << n) - 1;
        vector<int> pre(n, 0);
        for (auto& r : relations) {
            int a = r[0] - 1;
            int b = r[1] - 1;
            pre[b] |= (1 << a);
        }
        const int INF = n + 5;
        vector<int> dp(1 << n, INF);
        dp[0] = 0;
        for (int mask = 0; mask <= full; ++mask) {
            if (dp[mask] == INF) continue;
            int avail = 0;
            for (int i = 0; i < n; ++i) {
                if ((mask >> i & 1) == 0 && (pre[i] & ~mask) == 0) {
                    avail |= (1 << i);
                }
            }
            if (avail == 0) continue;
            int cnt = __builtin_popcount(avail);
            if (cnt <= k) {
                int nxt = mask | avail;
                dp[nxt] = min(dp[nxt], dp[mask] + 1);
            } else {
                // enumerate subsets of size k
                for (int sub = avail; sub; sub = (sub - 1) & avail) {
                    if (__builtin_popcount(sub) == k) {
                        int nxt = mask | sub;
                        dp[nxt] = min(dp[nxt], dp[mask] + 1);
                    }
                }
            }
        }
        return dp[full];
    }
};
```

## Java

```java
class Solution {
    public int minNumberOfSemesters(int n, int[][] relations, int k) {
        int[] pre = new int[n];
        for (int[] rel : relations) {
            int prev = rel[0] - 1;
            int next = rel[1] - 1;
            pre[next] |= 1 << prev;
        }
        int totalMask = (1 << n) - 1;
        int INF = 1_000_000;
        int[] dp = new int[1 << n];
        java.util.Arrays.fill(dp, INF);
        dp[0] = 0;

        for (int mask = 0; mask <= totalMask; mask++) {
            if (dp[mask] == INF) continue;
            // compute courses that can be taken now
            int avail = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) == 0 && (pre[i] & mask) == pre[i]) {
                    avail |= 1 << i;
                }
            }
            if (avail == 0) continue;

            int cntAvail = Integer.bitCount(avail);
            if (cntAvail <= k) {
                int nextMask = mask | avail;
                dp[nextMask] = Math.min(dp[nextMask], dp[mask] + 1);
            } else {
                // enumerate subsets of avail with size up to k
                for (int sub = avail; sub > 0; sub = (sub - 1) & avail) {
                    if (Integer.bitCount(sub) <= k) {
                        int nextMask = mask | sub;
                        dp[nextMask] = Math.min(dp[nextMask], dp[mask] + 1);
                    }
                }
            }
        }
        return dp[totalMask];
    }
}
```

## Python

```python
class Solution(object):
    def minNumberOfSemesters(self, n, relations, k):
        """
        :type n: int
        :type relations: List[List[int]]
        :type k: int
        :rtype: int
        """
        # prerequisite mask for each course (0-indexed)
        prereq = [0] * n
        for u, v in relations:
            prereq[v - 1] |= 1 << (u - 1)

        full_mask = (1 << n) - 1

        # precompute popcount for all masks up to 2^n
        pc = [0] * (1 << n)
        for mask in range(1, 1 << n):
            pc[mask] = pc[mask >> 1] + (mask & 1)

        from collections import deque
        INF = n + 1
        dp = [INF] * (1 << n)
        dp[0] = 0
        q = deque([0])

        while q:
            mask = q.popleft()
            cur_sem = dp[mask]
            if mask == full_mask:
                return cur_sem

            # compute courses that can be taken now
            avail = 0
            for i in range(n):
                if not (mask >> i) & 1 and (prereq[i] & ~mask) == 0:
                    avail |= 1 << i

            if avail == 0:
                continue

            cnt_avail = pc[avail]
            # If we can take all available courses this semester
            if cnt_avail <= k:
                new_mask = mask | avail
                if dp[new_mask] > cur_sem + 1:
                    dp[new_mask] = cur_sem + 1
                    q.append(new_mask)
                continue

            # Otherwise, enumerate subsets of size exactly k
            sub = avail
            while sub:
                if pc[sub] == k:
                    new_mask = mask | sub
                    if dp[new_mask] > cur_sem + 1:
                        dp[new_mask] = cur_sem + 1
                        q.append(new_mask)
                sub = (sub - 1) & avail

        return -1
```

## Python3

```python
from typing import List
from collections import deque

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        prereq = [0] * n
        for u, v in relations:
            prereq[v - 1] |= 1 << (u - 1)

        full_mask = (1 << n) - 1
        dp = [n + 1] * (1 << n)
        dp[0] = 0

        q = deque([0])
        visited = [False] * (1 << n)
        visited[0] = True

        while q:
            mask = q.popleft()
            cur_sem = dp[mask]
            if mask == full_mask:
                return cur_sem

            # find courses whose prerequisites are satisfied
            avail = 0
            for i in range(n):
                if not (mask >> i) & 1 and (prereq[i] & mask) == prereq[i]:
                    avail |= 1 << i

            cnt_avail = avail.bit_count()
            if cnt_avail <= k:
                nxt = mask | avail
                if dp[nxt] > cur_sem + 1:
                    dp[nxt] = cur_sem + 1
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)
                continue

            # enumerate subsets of size exactly k
            sub = avail
            while sub:
                if sub.bit_count() == k:
                    nxt = mask | sub
                    if dp[nxt] > cur_sem + 1:
                        dp[nxt] = cur_sem + 1
                        if not visited[nxt]:
                            visited[nxt] = True
                            q.append(nxt)
                sub = (sub - 1) & avail

        return dp[full_mask]
```

## C

```c
int minNumberOfSemesters(int n, int** relations, int relationsSize, int* relationsColSize, int k) {
    int prereqMask[15] = {0};
    for (int i = 0; i < relationsSize; ++i) {
        int a = relations[i][0] - 1;
        int b = relations[i][1] - 1;
        prereqMask[b] |= (1 << a);
    }
    int fullMask = (1 << n) - 1;
    int totalStates = 1 << n;
    const int INF = 1e9;
    int *dp = (int *)malloc(sizeof(int) * totalStates);
    for (int i = 0; i < totalStates; ++i) dp[i] = INF;
    dp[0] = 0;

    for (int mask = 0; mask <= fullMask; ++mask) {
        if (dp[mask] == INF) continue;
        int avail = 0;
        for (int i = 0; i < n; ++i) {
            if ((mask >> i) & 1) continue;                     // already taken
            if ((prereqMask[i] & mask) == prereqMask[i]) {     // prerequisites satisfied
                avail |= (1 << i);
            }
        }
        int cnt = __builtin_popcount(avail);
        if (cnt <= k) {
            int nxt = mask | avail;
            if (dp[nxt] > dp[mask] + 1) dp[nxt] = dp[mask] + 1;
        } else {
            // enumerate subsets of avail with exactly k bits
            for (int sub = avail; sub; sub = (sub - 1) & avail) {
                if (__builtin_popcount(sub) == k) {
                    int nxt = mask | sub;
                    if (dp[nxt] > dp[mask] + 1) dp[nxt] = dp[mask] + 1;
                }
            }
        }
    }

    int answer = dp[fullMask];
    free(dp);
    return answer;
}
```

## Csharp

```csharp
public class Solution {
    public int MinNumberOfSemesters(int n, int[][] relations, int k) {
        int[] prereq = new int[n];
        foreach (var rel in relations) {
            int a = rel[0] - 1;
            int b = rel[1] - 1;
            prereq[b] |= 1 << a;
        }

        int fullMask = (1 << n) - 1;
        int INF = n + 1;
        int[] dp = new int[1 << n];
        for (int i = 0; i < dp.Length; i++) dp[i] = INF;
        dp[0] = 0;

        for (int mask = 0; mask <= fullMask; mask++) {
            if (dp[mask] == INF) continue;

            int available = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) == 0 && (prereq[i] & ~mask) == 0) {
                    available |= 1 << i;
                }
            }

            if (available == 0) continue;

            int cntAvail = CountBits(available);
            if (cntAvail <= k) {
                int nextMask = mask | available;
                dp[nextMask] = Math.Min(dp[nextMask], dp[mask] + 1);
            } else {
                for (int sub = available; sub > 0; sub = (sub - 1) & available) {
                    if (CountBits(sub) == k) {
                        int nextMask = mask | sub;
                        dp[nextMask] = Math.Min(dp[nextMask], dp[mask] + 1);
                    }
                }
            }
        }

        return dp[fullMask];
    }

    private int CountBits(int x) {
        int cnt = 0;
        while (x != 0) {
            x &= x - 1;
            cnt++;
        }
        return cnt;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} relations
 * @param {number} k
 * @return {number}
 */
var minNumberOfSemesters = function(n, relations, k) {
    const preMask = new Array(n).fill(0);
    for (const [a, b] of relations) {
        // convert to 0‑based index
        const u = a - 1;
        const v = b - 1;
        preMask[v] |= (1 << u);
    }
    
    const fullMask = (1 << n) - 1;
    const dp = new Array(1 << n).fill(Infinity);
    dp[0] = 0;
    
    const bitCount = (x) => {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            cnt++;
        }
        return cnt;
    };
    
    for (let mask = 0; mask <= fullMask; ++mask) {
        if (dp[mask] === Infinity) continue;
        // compute courses whose prerequisites are satisfied
        let avail = 0;
        for (let i = 0; i < n; ++i) {
            const bit = 1 << i;
            if ((mask & bit) === 0 && (preMask[i] & mask) === preMask[i]) {
                avail |= bit;
            }
        }
        if (avail === 0) continue;
        
        // if we can take all available courses this semester
        if (bitCount(avail) <= k) {
            const nxt = mask | avail;
            dp[nxt] = Math.min(dp[nxt], dp[mask] + 1);
            continue;
        }
        
        // otherwise enumerate subsets of avail with size up to k
        let sub = avail;
        while (sub) {
            if (bitCount(sub) <= k) {
                const nxt = mask | sub;
                dp[nxt] = Math.min(dp[nxt], dp[mask] + 1);
            }
            sub = (sub - 1) & avail;
        }
    }
    
    return dp[fullMask];
};
```

## Typescript

```typescript
function minNumberOfSemesters(n: number, relations: number[][], k: number): number {
    const prereq = new Array<number>(n).fill(0);
    for (const [uRaw, vRaw] of relations) {
        const u = uRaw - 1;
        const v = vRaw - 1;
        prereq[v] |= (1 << u);
    }
    const fullMask = (1 << n) - 1;
    const visited = new Uint8Array(1 << n);
    let queue: number[] = [0];
    visited[0] = 1;
    let semesters = 0;

    const popcount = (x: number): number => {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            cnt++;
        }
        return cnt;
    };

    while (queue.length) {
        const nextQueue: number[] = [];
        for (const mask of queue) {
            if (mask === fullMask) return semesters;

            let avail = 0;
            for (let i = 0; i < n; i++) {
                if (((mask >> i) & 1) === 0 && (prereq[i] & mask) === prereq[i]) {
                    avail |= (1 << i);
                }
            }

            const cntAvail = popcount(avail);
            if (cntAvail === 0) continue;

            if (cntAvail <= k) {
                const nextMask = mask | avail;
                if (!visited[nextMask]) {
                    visited[nextMask] = 1;
                    nextQueue.push(nextMask);
                }
            } else {
                for (let sub = avail; sub; sub = (sub - 1) & avail) {
                    if (popcount(sub) === k) {
                        const nextMask = mask | sub;
                        if (!visited[nextMask]) {
                            visited[nextMask] = 1;
                            nextQueue.push(nextMask);
                        }
                    }
                }
            }
        }
        queue = nextQueue;
        semesters++;
    }

    return semesters;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $relations
     * @param Integer $k
     * @return Integer
     */
    function minNumberOfSemesters($n, $relations, $k) {
        $fullMask = (1 << $n) - 1;
        // prerequisite mask for each course
        $pre = array_fill(0, $n, 0);
        foreach ($relations as $rel) {
            [$a, $b] = $rel;
            $a--; $b--;
            $pre[$b] |= (1 << $a);
        }

        // precompute popcount for all masks
        $size = 1 << $n;
        $popcnt = array_fill(0, $size, 0);
        for ($i = 1; $i < $size; $i++) {
            $popcnt[$i] = $popcnt[$i >> 1] + ($i & 1);
        }

        $INF = PHP_INT_MAX;
        $dp = array_fill(0, $size, $INF);
        $dp[0] = 0;

        for ($mask = 0; $mask < $size; $mask++) {
            if ($dp[$mask] === $INF) continue;

            // find courses that can be taken now
            $available = 0;
            for ($i = 0; $i < $n; $i++) {
                if ((($mask >> $i) & 1) == 0 && (($pre[$i] & ~$mask) == 0)) {
                    $available |= (1 << $i);
                }
            }

            if ($available == 0) continue;

            $cntAvail = $popcnt[$available];
            if ($cntAvail <= $k) {
                $nextMask = $mask | $available;
                if ($dp[$nextMask] > $dp[$mask] + 1) {
                    $dp[$nextMask] = $dp[$mask] + 1;
                }
            } else {
                // enumerate subsets of available with size <= k
                for ($sub = $available; $sub > 0; $sub = ($sub - 1) & $available) {
                    if ($popcnt[$sub] <= $k) {
                        $nextMask = $mask | $sub;
                        if ($dp[$nextMask] > $dp[$mask] + 1) {
                            $dp[$nextMask] = $dp[$mask] + 1;
                        }
                    }
                }
            }
        }

        return $dp[$fullMask];
    }
}
```

## Swift

```swift
class Solution {
    func minNumberOfSemesters(_ n: Int, _ relations: [[Int]], _ k: Int) -> Int {
        let fullMask = (1 << n) - 1
        var prereq = [Int](repeating: 0, count: n)
        for rel in relations {
            let a = rel[0] - 1
            let b = rel[1] - 1
            prereq[b] |= 1 << a
        }
        let INF = Int.max / 2
        var dp = [Int](repeating: INF, count: 1 << n)
        dp[0] = 0
        
        for mask in 0...fullMask {
            if dp[mask] == INF { continue }
            // compute available courses
            var avail = 0
            for i in 0..<n {
                let bit = 1 << i
                if (mask & bit) == 0 && (prereq[i] & mask) == prereq[i] {
                    avail |= bit
                }
            }
            if avail == 0 { continue }
            let cntAvail = avail.nonzeroBitCount
            if cntAvail <= k {
                let nextMask = mask | avail
                if dp[nextMask] > dp[mask] + 1 {
                    dp[nextMask] = dp[mask] + 1
                }
            } else {
                // enumerate subsets of size k
                var sub = avail
                while sub > 0 {
                    if sub.nonzeroBitCount == k {
                        let nextMask = mask | sub
                        if dp[nextMask] > dp[mask] + 1 {
                            dp[nextMask] = dp[mask] + 1
                        }
                    }
                    sub = (sub - 1) & avail
                }
            }
        }
        return dp[fullMask]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minNumberOfSemesters(n: Int, relations: Array<IntArray>, k: Int): Int {
        val prereq = IntArray(n)
        for (rel in relations) {
            val prev = rel[0] - 1
            val next = rel[1] - 1
            prereq[next] = prereq[next] or (1 shl prev)
        }
        val totalMask = (1 shl n) - 1
        val INF = Int.MAX_VALUE / 2
        val dp = IntArray(1 shl n) { INF }
        dp[0] = 0

        for (mask in 0..totalMask) {
            if (dp[mask] == INF) continue
            // compute available courses
            var avail = 0
            for (i in 0 until n) {
                val bit = 1 shl i
                if ((mask and bit) == 0 && (prereq[i] and mask) == prereq[i]) {
                    avail = avail or bit
                }
            }
            if (avail == 0) continue
            val cntAvail = Integer.bitCount(avail)
            if (cntAvail <= k) {
                val nextMask = mask or avail
                if (dp[nextMask] > dp[mask] + 1) dp[nextMask] = dp[mask] + 1
            } else {
                var sub = avail
                while (sub > 0) {
                    if (Integer.bitCount(sub) == k) {
                        val nextMask = mask or sub
                        if (dp[nextMask] > dp[mask] + 1) dp[nextMask] = dp[mask] + 1
                    }
                    sub = (sub - 1) and avail
                }
            }
        }
        return dp[totalMask]
    }
}
```

## Dart

```dart
class Solution {
  int minNumberOfSemesters(int n, List<List<int>> relations, int k) {
    List<int> pre = List.filled(n, 0);
    for (var rel in relations) {
      int a = rel[0] - 1;
      int b = rel[1] - 1;
      pre[b] |= (1 << a);
    }
    int fullMask = (1 << n) - 1;
    const int INF = 1 << 30;
    List<int> dp = List.filled(1 << n, INF);
    List<int> queue = [];
    int head = 0;
    dp[0] = 0;
    queue.add(0);

    while (head < queue.length) {
      int mask = queue[head++];
      if (mask == fullMask) return dp[mask];

      int avail = 0;
      for (int i = 0; i < n; i++) {
        if ((mask >> i & 1) == 0 && (pre[i] & mask) == pre[i]) {
          avail |= (1 << i);
        }
      }

      int cnt = _bitCount(avail);
      if (cnt == 0) continue;

      if (cnt <= k) {
        int nextMask = mask | avail;
        if (dp[nextMask] > dp[mask] + 1) {
          dp[nextMask] = dp[mask] + 1;
          queue.add(nextMask);
        }
      } else {
        for (int sub = avail; sub > 0; sub = (sub - 1) & avail) {
          if (_bitCount(sub) == k) {
            int nextMask = mask | sub;
            if (dp[nextMask] > dp[mask] + 1) {
              dp[nextMask] = dp[mask] + 1;
              queue.add(nextMask);
            }
          }
        }
      }
    }

    return dp[fullMask];
  }

  int _bitCount(int x) {
    int cnt = 0;
    while (x != 0) {
      x &= x - 1;
      cnt++;
    }
    return cnt;
  }
}
```

## Golang

```go
func minNumberOfSemesters(n int, relations [][]int, k int) int {
	type void struct{}
	_ = void{}
	total := 1 << n
	prereq := make([]int, n)
	for _, r := range relations {
		u, v := r[0]-1, r[1]-1
		prereq[v] |= 1 << u
	}
	const inf = int(1e9)
	dp := make([]int, total)
	for i := range dp {
		dp[i] = inf
	}
	dp[0] = 0
	fullMask := total - 1

	for mask := 0; mask < total; mask++ {
		if dp[mask] == inf {
			continue
		}
		// compute available courses
		avail := 0
		for i := 0; i < n; i++ {
			if (mask>>i)&1 == 0 && (prereq[i]&mask) == prereq[i] {
				avail |= 1 << i
			}
		}
		if avail == 0 {
			continue
		}
		cnt := bits.OnesCount(uint(avail))
		if cnt <= k {
			next := mask | avail
			if dp[next] > dp[mask]+1 {
				dp[next] = dp[mask] + 1
			}
			continue
		}
		// enumerate subsets of avail with size up to k
		sub := avail
		for sub > 0 {
			if bits.OnesCount(uint(sub)) <= k {
				next := mask | sub
				if dp[next] > dp[mask]+1 {
					dp[next] = dp[mask] + 1
				}
			}
			sub = (sub - 1) & avail
		}
	}
	return dp[fullMask]
}
```

## Ruby

```ruby
def min_number_of_semesters(n, relations, k)
  prereq = Array.new(n, 0)
  relations.each do |pre, nxt|
    pre -= 1
    nxt -= 1
    prereq[nxt] |= (1 << pre)
  end

  total = 1 << n
  INF = n + 1
  dp = Array.new(total, INF)
  dp[0] = 0

  popcnt = Array.new(total, 0)
  (1...total).each { |i| popcnt[i] = popcnt[i >> 1] + (i & 1) }

  (0...total).each do |mask|
    cur = dp[mask]
    next if cur == INF

    avail = 0
    n.times do |i|
      next if (mask >> i) & 1 == 1
      avail |= (1 << i) if (prereq[i] & mask) == prereq[i]
    end

    next if avail == 0

    if popcnt[avail] <= k
      nxt = mask | avail
      dp[nxt] = cur + 1 if dp[nxt] > cur + 1
    else
      sub = avail
      while sub > 0
        if popcnt[sub] <= k
          nxt = mask | sub
          dp[nxt] = cur + 1 if dp[nxt] > cur + 1
        end
        sub = (sub - 1) & avail
      end
    end
  end

  dp[total - 1]
end
```

## Scala

```scala
object Solution {
    def minNumberOfSemesters(n: Int, relations: Array[Array[Int]], k: Int): Int = {
        val prereq = Array.fill(n)(0)
        for (rel <- relations) {
            val prev = rel(0) - 1
            val next = rel(1) - 1
            prereq(next) |= 1 << prev
        }
        val total = 1 << n
        val INF = Int.MaxValue / 2
        val dp = Array.fill(total)(INF)
        dp(0) = 0

        for (mask <- 0 until total) {
            val cur = dp(mask)
            if (cur < INF) {
                var avail = 0
                var i = 0
                while (i < n) {
                    if ((mask & (1 << i)) == 0 && (prereq(i) & mask) == prereq(i)) {
                        avail |= 1 << i
                    }
                    i += 1
                }

                if (Integer.bitCount(avail) <= k) {
                    val nextMask = mask | avail
                    if (dp(nextMask) > cur + 1) dp(nextMask) = cur + 1
                } else {
                    var sub = avail
                    while (sub > 0) {
                        if (Integer.bitCount(sub) <= k) {
                            val nextMask = mask | sub
                            if (dp(nextMask) > cur + 1) dp(nextMask) = cur + 1
                        }
                        sub = (sub - 1) & avail
                    }
                }
            }
        }

        dp(total - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_number_of_semesters(n: i32, relations: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = n as usize;
        let k = k as i32;
        // prerequisite bitmask for each course
        let mut prereq = vec![0u16; n];
        for rel in relations {
            let a = (rel[0] - 1) as usize;
            let b = (rel[1] - 1) as usize;
            prereq[b] |= 1 << a;
        }

        let max_mask = 1usize << n;
        let mut dp = vec![i32::MAX; max_mask];
        dp[0] = 0;

        for mask in 0..max_mask {
            let cur = dp[mask];
            if cur == i32::MAX {
                continue;
            }
            // compute courses that can be taken now
            let mut avail: u16 = 0;
            for i in 0..n {
                if (mask >> i) & 1 == 0 {
                    let pre = prereq[i] as usize;
                    if (pre & mask) == pre {
                        avail |= 1 << i;
                    }
                }
            }

            let cnt = avail.count_ones() as i32;
            if cnt <= k {
                let new_mask = mask | (avail as usize);
                if dp[new_mask] > cur + 1 {
                    dp[new_mask] = cur + 1;
                }
            } else {
                // enumerate subsets of avail with exactly k bits
                let mut sub = avail;
                while sub > 0 {
                    if sub.count_ones() as i32 == k {
                        let new_mask = mask | (sub as usize);
                        if dp[new_mask] > cur + 1 {
                            dp[new_mask] = cur + 1;
                        }
                    }
                    sub = (sub - 1) & avail;
                }
            }
        }

        dp[max_mask - 1]
    }
}
```

## Racket

```racket
(define/contract (min-number-of-semesters n relations k)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((pre (make-vector n 0))
         (maxMask (arithmetic-shift 1 n)))
    ;; build prerequisite masks
    (for ([rel relations])
      (define prev (- (first rel) 1))
      (define nxt (- (second rel) 1))
      (vector-set! pre nxt
                   (bitwise-ior (vector-ref pre nxt)
                                (arithmetic-shift 1 prev))))
    (define dp (make-vector maxMask (+ n 1))) ; large initial value
    (vector-set! dp 0 0)
    ;; iterate over all masks
    (for ([mask (in-range maxMask)])
      (define cur (vector-ref dp mask))
      (when (< cur (+ n 1))               ; reachable state
        ;; compute courses that can be taken now
        (let loop-available ((i 0) (avail 0))
          (if (= i n)
              (let ((sub avail))
                (let inner-loop ((s sub))
                  (when (> s 0)
                    (when (<= (bitwise-bit-count s) k)
                      (define newmask (bitwise-ior mask s))
                      (define old (vector-ref dp newmask))
                      (when (< (+ cur 1) old)
                        (vector-set! dp newmask (+ cur 1))))
                    (inner-loop (bitwise-and (sub1 s) avail)))))
              (let ((taken? (positive? (bitwise-and mask (arithmetic-shift 1 i)))))
                (if taken?
                    (loop-available (add1 i) avail)
                    (let ((prereq (vector-ref pre i)))
                      (if (= (bitwise-and prereq (bitwise-not mask)) 0)
                          (loop-available (add1 i)
                                          (bitwise-ior avail (arithmetic-shift 1 i)))
                          (loop-available (add1 i) avail)))))))))
    (vector-ref dp (sub1 maxMask))))
```

## Erlang

```erlang
-spec min_number_of_semesters(N :: integer(), Relations :: [[integer()]], K :: integer()) -> integer().
min_number_of_semesters(N, Relations, K) ->
    MaxMask = (1 bsl N) - 1,
    PreMaskArr = build_pre_mask(N, Relations),
    Queue0 = queue:new(),
    Queue1 = queue:in(0, Queue0),
    DistMap0 = #{0 => 0},
    bfs(DistMap0, Queue1, PreMaskArr, N, K, MaxMask).

build_pre_mask(N, Relations) ->
    Empty = array:new(N, {default, 0}),
    lists:foldl(fun([A, B], Arr) ->
        IndexB = B - 1,
        Old = array:get(IndexB, Arr),
        NewMask = Old bor (1 bsl (A - 1)),
        array:set(IndexB, NewMask, Arr)
    end, Empty, Relations).

bfs(DistMap, Queue, PreMaskArr, N, K, MaxMask) ->
    case queue:out(Queue) of
        {empty, _} -> -1;
        {{value, Mask}, QRest} ->
            D = maps:get(Mask, DistMap),
            if Mask == MaxMask ->
                    D;
               true ->
                    AvailMask = compute_available(Mask, PreMaskArr, N),
                    {NewQ, NewDistMap} =
                        case popcount(AvailMask) =< K of
                            true ->
                                NewMask = Mask bor AvailMask,
                                maybe_enqueue_queue(NewMask, D + 1, DistMap, QRest);
                            false ->
                                enqueue_subsets_queue(Mask, AvailMask, K, D, DistMap, QRest)
                        end,
                    bfs(NewDistMap, NewQ, PreMaskArr, N, K, MaxMask)
            end
    end.

compute_available(Mask, PreMaskArr, N) ->
    compute_available(0, Mask, 0, PreMaskArr, N).

compute_available(I, _Mask, Acc, _Arr, N) when I == N -> Acc;
compute_available(I, Mask, Acc, Arr, N) ->
    Bit = 1 bsl I,
    case (Mask band Bit) of
        0 ->
            Pre = array:get(I, Arr),
            if (Pre band Mask) == Pre ->
                    compute_available(I + 1, Mask, Acc bor Bit, Arr, N);
               true ->
                    compute_available(I + 1, Mask, Acc, Arr, N)
            end;
        _ ->
            compute_available(I + 1, Mask, Acc, Arr, N)
    end.

popcount(0) -> 0;
popcount(X) -> (X band 1) + popcount(X bsr 1).

maybe_enqueue_queue(NewMask, NewDist, DistMap, Queue) ->
    case maps:is_key(NewMask, DistMap) of
        true -> {Queue, DistMap};
        false -> {queue:in(NewMask, Queue), maps:put(NewMask, NewDist, DistMap)}
    end.

enqueue_subsets_queue(Mask, AvailMask, K, D, DistMap, Queue) ->
    enqueue_subsets_loop(AvailMask, AvailMask, Mask, K, D, DistMap, Queue).

enqueue_subsets_loop(0, _AvailMask, _Mask, _K, _D, DistMap, Queue) ->
    {Queue, DistMap};
enqueue_subsets_loop(Sub, AvailMask, Mask, K, D, DistMap, Queue) ->
    {TmpQ, TmpM} =
        if popcount(Sub) =< K ->
                NewMask = Mask bor Sub,
                maybe_enqueue_queue(NewMask, D + 1, DistMap, Queue);
           true -> {Queue, DistMap}
        end,
    NextSub = (Sub - 1) band AvailMask,
    enqueue_subsets_loop(NextSub, AvailMask, Mask, K, D, TmpM, TmpQ).
```

## Elixir

```elixir
defmodule Solution do
  @spec min_number_of_semesters(n :: integer, relations :: [[integer]], k :: integer) :: integer
  def min_number_of_semesters(n, relations, k) do
    # prerequisite mask for each course (0-indexed)
    prereq_list =
      Enum.reduce(relations, List.duplicate(0, n), fn [prev, nxt], acc ->
        prev_idx = prev - 1
        nxt_idx = nxt - 1
        List.update_at(acc, nxt_idx, &(&1 ||| (1 <<< prev_idx)))
      end)

    prereq = List.to_tuple(prereq_list)
    full_mask = (1 <<< n) - 1

    visited = MapSet.new([0])
    queue = :queue.from_list([{0, 0}])

    bfs(queue, visited, prereq, k, full_mask)
  end

  defp bfs(queue, visited, prereq, k, full_mask) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{:value, {mask, dist}}, q_rest} ->
        if mask == full_mask do
          dist
        else
          available = compute_available(mask, prereq)

          next_masks =
            if bit_count(available) <= k do
              [mask ||| available]
            else
              subsets_of_limit(available, k)
            end

          {new_queue, new_visited} =
            Enum.reduce(next_masks, {q_rest, visited}, fn nxt, {q_acc, v_acc} ->
              if MapSet.member?(v_acc, nxt) do
                {q_acc, v_acc}
              else
                {
                  :queue.in({nxt, dist + 1}, q_acc),
                  MapSet.put(v_acc, nxt)
                }
              end
            end)

          bfs(new_queue, new_visited, prereq, k, full_mask)
        end
    end
  end

  defp compute_available(mask, prereq) do
    n = tuple_size(prereq)

    Enum.reduce(0..(n - 1), 0, fn i, acc ->
      course_bit = 1 <<< i

      if (mask &&& course_bit) == 0 and ((elem(prereq, i) &&& mask) == elem(prereq, i)) do
        acc ||| course_bit
      else
        acc
      end
    end)
  end

  defp subsets_of_limit(available, k) do
    collect_subsets(available, available, k, [])
  end

  defp collect_subsets(0, _orig, _k, acc), do: acc

  defp collect_subsets(sub, orig, k, acc) do
    new_acc = if bit_count(sub) <= k, do: [sub | acc], else: acc
    next = (sub - 1) &&& orig
    collect_subsets(next, orig, k, new_acc)
  end

  defp bit_count(0), do: 0
  defp bit_count(x), do: 1 + bit_count(x &&& (x - 1))
end
```
