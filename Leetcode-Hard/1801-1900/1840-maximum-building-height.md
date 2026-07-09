# 1840. Maximum Building Height

## Cpp

```cpp
class Solution {
public:
    int maxBuilding(int n, vector<vector<int>>& restrictions) {
        if (restrictions.empty()) return n - 1;
        sort(restrictions.begin(), restrictions.end());
        vector<pair<long long,long long>> v;
        v.emplace_back(1LL, 0LL); // building 1 height fixed at 0
        for (auto &r : restrictions) v.emplace_back((long long)r[0], (long long)r[1]);
        if (v.back().first != n) v.emplace_back((long long)n, (long long)4e18); // large INF
        
        int m = v.size();
        // forward pass
        for (int i = 1; i < m; ++i) {
            long long allowed = v[i-1].second + (v[i].first - v[i-1].first);
            if (v[i].second > allowed) v[i].second = allowed;
        }
        // backward pass
        for (int i = m - 2; i >= 0; --i) {
            long long allowed = v[i+1].second + (v[i+1].first - v[i].first);
            if (v[i].second > allowed) v[i].second = allowed;
        }
        
        long long ans = 0;
        for (int i = 0; i < m; ++i) ans = max(ans, v[i].second);
        // evaluate peaks between consecutive restrictions
        for (int i = 0; i < m - 1; ++i) {
            long long dist = v[i+1].first - v[i].first;
            long long diff = llabs(v[i+1].second - v[i].second);
            long long peak = max(v[i].second, v[i+1].second) + (dist - diff) / 2;
            ans = max(ans, peak);
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int maxBuilding(int n, int[][] restrictions) {
        // If there are no restrictions, the tallest building can be at height n-1
        if (restrictions == null || restrictions.length == 0) {
            return n - 1;
        }

        java.util.List<int[]> list = new java.util.ArrayList<>();
        // Building 1 is always height 0
        list.add(new int[]{1, 0});
        for (int[] r : restrictions) {
            list.add(r.clone());
        }
        // Sort by building index
        list.sort(java.util.Comparator.comparingInt(a -> a[0]));

        // Left to right pass: enforce the slope constraint
        for (int i = 1; i < list.size(); i++) {
            int dist = list.get(i)[0] - list.get(i - 1)[0];
            int maxPossible = list.get(i - 1)[1] + dist;
            if (list.get(i)[1] > maxPossible) {
                list.get(i)[1] = maxPossible;
            }
        }

        // Right to left pass: enforce the slope constraint
        for (int i = list.size() - 2; i >= 0; i--) {
            int dist = list.get(i + 1)[0] - list.get(i)[0];
            int maxPossible = list.get(i + 1)[1] + dist;
            if (list.get(i)[1] > maxPossible) {
                list.get(i)[1] = maxPossible;
            }
        }

        long answer = 0;
        // Consider heights at restricted positions
        for (int[] r : list) {
            answer = Math.max(answer, r[1]);
        }

        // Consider the maximum possible height between each pair of restrictions
        for (int i = 0; i < list.size() - 1; i++) {
            int id1 = list.get(i)[0];
            int h1 = list.get(i)[1];
            int id2 = list.get(i + 1)[0];
            int h2 = list.get(i + 1)[1];
            int d = id2 - id1;
            int diff = Math.abs(h2 - h1);
            int remaining = d - diff; // steps left after meeting the slope difference
            long peak = Math.max(h1, h2) + remaining / 2L;
            answer = Math.max(answer, peak);
        }

        // After the last restriction up to building n (if any)
        int[] last = list.get(list.size() - 1);
        if (last[0] < n) {
            long possible = last[1] + (n - last[0]);
            answer = Math.max(answer, possible);
        }

        return (int) answer;
    }
}
```

## Python

```python
class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        # If no restrictions, height can increase by 1 each building starting from 0 at building 1
        if not restrictions:
            return n - 1

        # Add implicit restriction for building 1 with height 0
        restrictions.append([1, 0])
        # Sort by building index
        restrictions.sort(key=lambda x: x[0])

        m = len(restrictions)

        # Left to right pass: enforce distance constraint
        for i in range(1, m):
            dist = restrictions[i][0] - restrictions[i-1][0]
            max_allowed = restrictions[i-1][1] + dist
            if restrictions[i][1] > max_allowed:
                restrictions[i][1] = max_allowed

        # Right to left pass: enforce distance constraint
        for i in range(m - 2, -1, -1):
            dist = restrictions[i+1][0] - restrictions[i][0]
            max_allowed = restrictions[i+1][1] + dist
            if restrictions[i][1] > max_allowed:
                restrictions[i][1] = max_allowed

        ans = 0
        # Compute maximum possible height between each consecutive pair of restrictions
        for i in range(m - 1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i + 1]
            d = id2 - id1
            # peak achievable between them
            peak = max(h1, h2) + (d - abs(h1 - h2)) // 2
            if peak > ans:
                ans = peak

        # Consider the tail after the last restriction up to building n
        last_id, last_h = restrictions[-1]
        tail_peak = last_h + (n - last_id)
        if tail_peak > ans:
            ans = tail_peak

        return ans
```

## Python3

```python
class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        # Add building 1 with height 0
        restr = [[1, 0]]
        for r in restrictions:
            restr.append([r[0], r[1]])
        # Sort by building index
        restr.sort(key=lambda x: x[0])
        # Ensure there is a restriction at building n (use a very large height)
        if restr[-1][0] != n:
            restr.append([n, 10**18])

        # Forward pass: enforce left-to-right constraints
        for i in range(1, len(restr)):
            dist = restr[i][0] - restr[i - 1][0]
            max_allowed = restr[i - 1][1] + dist
            if restr[i][1] > max_allowed:
                restr[i][1] = max_allowed

        # Backward pass: enforce right-to-left constraints
        for i in range(len(restr) - 2, -1, -1):
            dist = restr[i + 1][0] - restr[i][0]
            max_allowed = restr[i + 1][1] + dist
            if restr[i][1] > max_allowed:
                restr[i][1] = max_allowed

        # Compute the maximum possible height between consecutive restrictions
        ans = 0
        for i in range(len(restr) - 1):
            l_id, l_h = restr[i]
            r_id, r_h = restr[i + 1]
            d = r_id - l_id
            cur = (l_h + r_h + d) // 2
            if cur > ans:
                ans = cur

        return ans
```

## C

```c
#include <stdlib.h>

struct Node {
    int id;
    long long h;
};

static int cmpNode(const void *a, const void *b) {
    const struct Node *na = (const struct Node *)a;
    const struct Node *nb = (const struct Node *)b;
    return na->id - nb->id;
}

int maxBuilding(int n, int** restrictions, int restrictionsSize, int* restrictionsColSize){
    int m = restrictionsSize + 1; // include building 1
    struct Node *arr = (struct Node*)malloc(sizeof(struct Node) * m);
    if (!arr) return 0;
    
    arr[0].id = 1;
    arr[0].h = 0;
    for (int i = 0; i < restrictionsSize; ++i) {
        arr[i + 1].id = restrictions[i][0];
        arr[i + 1].h = restrictions[i][1];
    }
    
    qsort(arr, m, sizeof(struct Node), cmpNode);
    
    // forward pass
    for (int i = 1; i < m; ++i) {
        long long diff = (long long)arr[i].id - arr[i-1].id;
        if (arr[i].h > arr[i-1].h + diff)
            arr[i].h = arr[i-1].h + diff;
    }
    // backward pass
    for (int i = m - 2; i >= 0; --i) {
        long long diff = (long long)arr[i+1].id - arr[i].id;
        if (arr[i].h > arr[i+1].h + diff)
            arr[i].h = arr[i+1].h + diff;
    }
    
    long long ans = 0;
    for (int i = 0; i < m - 1; ++i) {
        long long d = (long long)arr[i+1].id - arr[i].id;
        long long possible = (arr[i].h + arr[i+1].h + d) / 2;
        if (possible > ans) ans = possible;
    }
    // segment after last restriction to building n
    long long tail = arr[m-1].h + (long long)(n - arr[m-1].id);
    if (tail > ans) ans = tail;
    
    free(arr);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxBuilding(int n, int[][] restrictions) {
        var list = new List<(long pos, long h)>();
        list.Add((1L, 0L));
        foreach (var r in restrictions) {
            list.Add(((long)r[0], (long)r[1]));
        }
        list.Sort((a, b) => a.pos.CompareTo(b.pos));

        int m = list.Count;
        var pos = new long[m];
        var h = new long[m];
        for (int i = 0; i < m; i++) {
            pos[i] = list[i].pos;
            h[i] = list[i].h;
        }

        // forward pass
        for (int i = 1; i < m; i++) {
            long diff = pos[i] - pos[i - 1];
            long maxPossible = h[i - 1] + diff;
            if (h[i] > maxPossible) h[i] = maxPossible;
        }

        // backward pass
        for (int i = m - 2; i >= 0; i--) {
            long diff = pos[i + 1] - pos[i];
            long maxPossible = h[i + 1] + diff;
            if (h[i] > maxPossible) h[i] = maxPossible;
        }

        long ans = 0;
        for (int i = 0; i < m - 1; i++) {
            long dist = pos[i + 1] - pos[i];
            long ha = h[i], hb = h[i + 1];
            long localMax = Math.Max(ha, hb) + (dist - Math.Abs(ha - hb)) / 2;
            if (localMax > ans) ans = localMax;
        }

        // tail after the last restriction
        long lastPos = pos[m - 1];
        long lastH = h[m - 1];
        if (lastPos < n) {
            long tailMax = lastH + (n - lastPos);
            if (tailMax > ans) ans = tailMax;
        }

        return (int)ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} restrictions
 * @return {number}
 */
var maxBuilding = function(n, restrictions) {
    if (restrictions.length === 0) return n - 1;
    
    // add restriction for building 1 with height 0
    restrictions.push([1, 0]);
    // sort by building index
    restrictions.sort((a, b) => a[0] - b[0]);

    // left to right pass: enforce climb limit
    for (let i = 1; i < restrictions.length; ++i) {
        const dist = restrictions[i][0] - restrictions[i - 1][0];
        const maxPossible = restrictions[i - 1][1] + dist;
        if (restrictions[i][1] > maxPossible) {
            restrictions[i][1] = maxPossible;
        }
    }

    // right to left pass: enforce descent limit
    for (let i = restrictions.length - 2; i >= 0; --i) {
        const dist = restrictions[i + 1][0] - restrictions[i][0];
        const maxPossible = restrictions[i + 1][1] + dist;
        if (restrictions[i][1] > maxPossible) {
            restrictions[i][1] = maxPossible;
        }
    }

    let ans = 0;

    // evaluate maximum height between each consecutive pair of restrictions
    for (let i = 0; i < restrictions.length - 1; ++i) {
        const posA = restrictions[i][0];
        const hA   = restrictions[i][1];
        const posB = restrictions[i + 1][0];
        const hB   = restrictions[i + 1][1];
        const d    = posB - posA;
        // highest possible peak between them
        const localMax = Math.floor((hA + hB + d) / 2);
        if (localMax > ans) ans = localMax;
    }

    // consider the stretch from the last restriction to building n
    const last = restrictions[restrictions.length - 1];
    const tailHeight = last[1] + (n - last[0]);
    if (tailHeight > ans) ans = tailHeight;

    return ans;
};
```

## Typescript

```typescript
function maxBuilding(n: number, restrictions: number[][]): number {
    // Ensure building 1 has height 0 restriction
    restrictions.push([1, 0]);
    // Sort by building index
    restrictions.sort((a, b) => a[0] - b[0]);

    // Forward pass to enforce left-to-right constraints
    for (let i = 1; i < restrictions.length; i++) {
        const dist = restrictions[i][0] - restrictions[i - 1][0];
        const maxAllowed = restrictions[i - 1][1] + dist;
        if (restrictions[i][1] > maxAllowed) {
            restrictions[i][1] = maxAllowed;
        }
    }

    // Backward pass to enforce right-to-left constraints
    for (let i = restrictions.length - 2; i >= 0; i--) {
        const dist = restrictions[i + 1][0] - restrictions[i][0];
        const maxAllowed = restrictions[i + 1][1] + dist;
        if (restrictions[i][1] > maxAllowed) {
            restrictions[i][1] = maxAllowed;
        }
    }

    let ans = 0;

    // Evaluate maximum height between consecutive restricted buildings
    for (let i = 0; i < restrictions.length - 1; i++) {
        const a = restrictions[i][0];
        const ha = restrictions[i][1];
        const b = restrictions[i + 1][0];
        const hb = restrictions[i + 1][1];
        const d = b - a;
        const candidate = Math.floor((ha + hb + d) / 2);
        if (candidate > ans) ans = candidate;
    }

    // Consider the stretch from the last restriction to building n
    const last = restrictions[restrictions.length - 1];
    const tailCandidate = last[1] + (n - last[0]);
    if (tailCandidate > ans) ans = tailCandidate;

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $restrictions
     * @return Integer
     */
    function maxBuilding($n, $restrictions) {
        if (empty($restrictions)) {
            return $n - 1;
        }

        // Add restriction for building 1 with height 0
        $restrictions[] = [1, 0];
        usort($restrictions, function ($a, $b) {
            return $a[0] <=> $b[0];
        });

        $m = count($restrictions);

        // Forward pass: enforce left-to-right constraints
        for ($i = 1; $i < $m; $i++) {
            $dist = $restrictions[$i][0] - $restrictions[$i - 1][0];
            $maxHeight = $restrictions[$i - 1][1] + $dist;
            if ($restrictions[$i][1] > $maxHeight) {
                $restrictions[$i][1] = $maxHeight;
            }
        }

        // Backward pass: enforce right-to-left constraints
        for ($i = $m - 2; $i >= 0; $i--) {
            $dist = $restrictions[$i + 1][0] - $restrictions[$i][0];
            $maxHeight = $restrictions[$i + 1][1] + $dist;
            if ($restrictions[$i][1] > $maxHeight) {
                $restrictions[$i][1] = $maxHeight;
            }
        }

        $ans = 0;

        // Consider heights at restricted positions
        foreach ($restrictions as $r) {
            if ($r[1] > $ans) {
                $ans = $r[1];
            }
        }

        // Consider peaks between consecutive restrictions
        for ($i = 0; $i < $m - 1; $i++) {
            $dist = $restrictions[$i + 1][0] - $restrictions[$i][0];
            $possible = intdiv($restrictions[$i][1] + $restrictions[$i + 1][1] + $dist, 2);
            if ($possible > $ans) {
                $ans = $possible;
            }
        }

        // Consider the tail after the last restriction up to building n
        $lastPos = $restrictions[$m - 1][0];
        $lastHeight = $restrictions[$m - 1][1];
        $tailPossible = $lastHeight + ($n - $lastPos);
        if ($tailPossible > $ans) {
            $ans = $tailPossible;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxBuilding(_ n: Int, _ restrictions: [[Int]]) -> Int {
        var arr = restrictions.map { $0 }   // each element is [index, height]
        arr.append([1, 0])                  // building 1 with height 0
        arr.sort { $0[0] < $1[0] }
        
        // Left to right pass: enforce increasing constraint
        for i in 1..<arr.count {
            let dist = arr[i][0] - arr[i - 1][0]
            if arr[i][1] > arr[i - 1][1] + dist {
                arr[i][1] = arr[i - 1][1] + dist
            }
        }
        
        // Right to left pass: enforce decreasing constraint
        if arr.count >= 2 {
            for i in stride(from: arr.count - 2, through: 0, by: -1) {
                let dist = arr[i + 1][0] - arr[i][0]
                if arr[i][1] > arr[i + 1][1] + dist {
                    arr[i][1] = arr[i + 1][1] + dist
                }
            }
        }
        
        var answer = 0
        
        // Evaluate maximum height between each pair of consecutive restrictions
        for i in 0..<(arr.count - 1) {
            let idx1 = arr[i][0], h1 = arr[i][1]
            let idx2 = arr[i + 1][0], h2 = arr[i + 1][1]
            let d = idx2 - idx1
            // Highest possible peak between them
            let candidate = (h1 + h2 + d) / 2
            if candidate > answer { answer = candidate }
        }
        
        // Consider the stretch from the last restriction to building n
        if let last = arr.last {
            let candidate = last[1] + (n - last[0])
            if candidate > answer { answer = candidate }
        }
        
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxBuilding(n: Int, restrictions: Array<IntArray>): Int {
        val list = mutableListOf<Pair<Int, Long>>()
        for (r in restrictions) {
            list.add(Pair(r[0], r[1].toLong()))
        }
        // building 1 must be height 0
        list.add(Pair(1, 0L))
        list.sortBy { it.first }

        // forward pass to enforce left-to-right constraints
        for (i in 1 until list.size) {
            val prev = list[i - 1]
            val cur = list[i]
            val d = (cur.first - prev.first).toLong()
            if (cur.second > prev.second + d) {
                list[i] = Pair(cur.first, prev.second + d)
            }
        }

        // backward pass to enforce right-to-left constraints
        for (i in list.size - 2 downTo 0) {
            val next = list[i + 1]
            val cur = list[i]
            val d = (next.first - cur.first).toLong()
            if (cur.second > next.second + d) {
                list[i] = Pair(cur.first, next.second + d)
            }
        }

        var ans = 0L
        // evaluate maximum possible height between each pair of restrictions
        for (i in 0 until list.size - 1) {
            val a = list[i]
            val b = list[i + 1]
            val dist = (b.first - a.first).toLong()
            val candidate = (a.second + b.second + dist) / 2
            if (candidate > ans) ans = candidate
        }

        // consider the stretch from the last restriction to building n
        val last = list.last()
        val tailCandidate = last.second + (n - last.first)
        if (tailCandidate > ans) ans = tailCandidate

        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maxBuilding(int n, List<List<int>> restrictions) {
    // Prepare list of restrictions including building 1 and possibly building n
    List<List<int>> arr = [];
    arr.add([1, 0]); // building 1 must be height 0

    bool hasN = false;
    for (var r in restrictions) {
      int id = r[0];
      int h = r[1];
      if (id == n) hasN = true;
      arr.add([id, h]);
    }
    if (!hasN) {
      // No restriction on building n, its height can be at most n-1
      arr.add([n, n - 1]);
    }

    // Sort by building index
    arr.sort((a, b) => a[0].compareTo(b[0]));

    // Left to right pass: enforce reachable heights from the left
    for (int i = 1; i < arr.length; ++i) {
      int dist = arr[i][0] - arr[i - 1][0];
      if (arr[i][1] > arr[i - 1][1] + dist) {
        arr[i][1] = arr[i - 1][1] + dist;
      }
    }

    // Right to left pass: enforce reachable heights from the right
    for (int i = arr.length - 2; i >= 0; --i) {
      int dist = arr[i + 1][0] - arr[i][0];
      if (arr[i][1] > arr[i + 1][1] + dist) {
        arr[i][1] = arr[i + 1][1] + dist;
      }
    }

    // Compute the maximum possible height between consecutive restrictions
    int ans = 0;
    for (int i = 0; i < arr.length - 1; ++i) {
      int a = arr[i][0];
      int ha = arr[i][1];
      int b = arr[i + 1][0];
      int hb = arr[i + 1][1];
      int d = b - a;
      int localMax = ((ha + hb + d) ~/ 2);
      if (localMax > ans) ans = localMax;
    }

    return ans;
  }
}
```

## Golang

```go
import "sort"

func maxBuilding(n int, restrictions [][]int) int {
	type pair struct {
		pos int64
		h   int64
	}
	const INF int64 = 1 << 60

	var arr []pair
	arr = append(arr, pair{pos: 1, h: 0})
	for _, r := range restrictions {
		arr = append(arr, pair{pos: int64(r[0]), h: int64(r[1])})
	}
	arr = append(arr, pair{pos: int64(n), h: INF})

	sort.Slice(arr, func(i, j int) bool { return arr[i].pos < arr[j].pos })

	// left to right
	for i := 1; i < len(arr); i++ {
		dist := arr[i].pos - arr[i-1].pos
		maxPossible := arr[i-1].h + dist
		if arr[i].h > maxPossible {
			arr[i].h = maxPossible
		}
	}
	// right to left
	for i := len(arr) - 2; i >= 0; i-- {
		dist := arr[i+1].pos - arr[i].pos
		maxPossible := arr[i+1].h + dist
		if arr[i].h > maxPossible {
			arr[i].h = maxPossible
		}
	}

	ans := int64(0)
	for _, p := range arr {
		if p.h > ans {
			ans = p.h
		}
	}
	for i := 0; i < len(arr)-1; i++ {
		d := arr[i+1].pos - arr[i].pos
		diff := arr[i+1].h - arr[i].h
		if diff < 0 {
			diff = -diff
		}
		extra := (d - diff) / 2
		candidate := max(arr[i].h, arr[i+1].h) + extra
		if candidate > ans {
			ans = candidate
		}
	}
	return int(ans)
}

func max(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}
```

## Ruby

```ruby
def max_building(n, restrictions)
  return n - 1 if restrictions.empty?

  restrictions << [1, 0]
  restrictions.sort_by! { |r| r[0] }

  m = restrictions.length

  # forward pass
  (1...m).each do |i|
    dist = restrictions[i][0] - restrictions[i - 1][0]
    max_allowed = restrictions[i - 1][1] + dist
    restrictions[i][1] = [restrictions[i][1], max_allowed].min
  end

  # backward pass
  (m - 2).downto(0) do |i|
    dist = restrictions[i + 1][0] - restrictions[i][0]
    max_allowed = restrictions[i + 1][1] + dist
    restrictions[i][1] = [restrictions[i][1], max_allowed].min
  end

  ans = 0
  (0...m - 1).each do |i|
    id1, h1 = restrictions[i]
    id2, h2 = restrictions[i + 1]
    d = id2 - id1
    possible = (h1 + h2 + d) / 2
    ans = [ans, possible].max
  end

  last_id, last_h = restrictions[-1]
  ans = [ans, last_h + (n - last_id)].max

  ans
end
```

## Scala

```scala
object Solution {
    def maxBuilding(n: Int, restrictions: Array[Array[Int]]): Int = {
        import scala.collection.mutable.ArrayBuffer

        val buf = new ArrayBuffer[(Int, Long)]()
        for (r <- restrictions) {
            buf += ((r(0), r(1).toLong))
        }
        // building 1 has height 0
        buf += ((1, 0L))

        // sort by building index
        val arr = buf.sortBy(_._1).toArray

        // forward pass: enforce left-to-right constraints
        for (i <- 1 until arr.length) {
            val dist = arr(i)._1 - arr(i - 1)._1
            if (arr(i)._2 > arr(i - 1)._2 + dist) {
                arr(i) = (arr(i)._1, arr(i - 1)._2 + dist)
            }
        }

        // backward pass: enforce right-to-left constraints
        for (i <- arr.length - 2 to 0 by -1) {
            val dist = arr(i + 1)._1 - arr(i)._1
            if (arr(i)._2 > arr(i + 1)._2 + dist) {
                arr(i) = (arr(i)._1, arr(i + 1)._2 + dist)
            }
        }

        var ans: Long = 0L

        // consider heights at restricted positions
        for ((_, h) <- arr) {
            if (h > ans) ans = h
        }

        // consider maximum height between consecutive restrictions
        for (i <- 0 until arr.length - 1) {
            val idL = arr(i)._1
            val hL = arr(i)._2
            val idR = arr(i + 1)._1
            val hR = arr(i + 1)._2
            val d = idR - idL
            // peak height achievable between them
            val candidate = (hL + hR + d) / 2
            if (candidate > ans) ans = candidate
        }

        // consider the tail after the last restriction up to building n
        val lastId = arr.last._1
        val lastH = arr.last._2
        val tailHeight = lastH + (n - lastId)
        if (tailHeight > ans) ans = tailHeight

        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_building(n: i32, restrictions: Vec<Vec<i32>>) -> i32 {
        use std::cmp::{min, max};
        let n_i64 = n as i64;
        let mut v: Vec<(i64, i64)> = Vec::with_capacity(restrictions.len() + 2);
        // building 1 always height 0
        v.push((1, 0));
        for r in restrictions.iter() {
            v.push((r[0] as i64, r[1] as i64));
        }
        // ensure a restriction at n
        if !restrictions.iter().any(|r| r[0] == n) {
            v.push((n_i64, n_i64 - 1));
        }
        // sort by position
        v.sort_by_key(|&(pos, _)| pos);
        // merge duplicates keeping the minimal height
        let mut merged: Vec<(i64, i64)> = Vec::with_capacity(v.len());
        for (pos, h) in v {
            if let Some(last) = merged.last_mut() {
                if last.0 == pos {
                    if h < last.1 {
                        last.1 = h;
                    }
                    continue;
                }
            }
            merged.push((pos, h));
        }

        // forward pass
        for i in 1..merged.len() {
            let dist = merged[i].0 - merged[i - 1].0;
            let max_h = merged[i - 1].1 + dist;
            if merged[i].1 > max_h {
                merged[i].1 = max_h;
            }
        }
        // backward pass
        for i in (0..merged.len() - 1).rev() {
            let dist = merged[i + 1].0 - merged[i].0;
            let max_h = merged[i + 1].1 + dist;
            if merged[i].1 > max_h {
                merged[i].1 = max_h;
            }
        }

        // compute answer
        let mut ans: i64 = 0;
        for &(_, h) in &merged {
            ans = max(ans, h);
        }
        for i in 0..merged.len() - 1 {
            let d = merged[i + 1].0 - merged[i].0;
            let possible = (merged[i].1 + merged[i + 1].1 + d) / 2;
            ans = max(ans, possible);
        }
        ans as i32
    }
}
```

## Racket

```racket
#lang racket
(require racket/list)

(define/contract (max-building n restrictions)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ([sorted (sort restrictions < #:key (lambda (pair) (first pair)))]
         [with-start (cons (list 1 0) sorted)])
    (let* ([m (length with-start)]
           [id-vec (make-vector m)]
           [h-vec (make-vector m)])
      ;; fill vectors
      (for ([i (in-range m)]
            [pair (in-list with-start)])
        (vector-set! id-vec i (first pair))
        (vector-set! h-vec i (second pair)))
      ;; forward pass
      (for ([i (in-range 1 m)])
        (let* ([dist (- (vector-ref id-vec i) (vector-ref id-vec (- i 1)))]
               [allowed (+ (vector-ref h-vec (- i 1)) dist)])
          (when (> (vector-ref h-vec i) allowed)
            (vector-set! h-vec i allowed))))
      ;; backward pass
      (for ([i (in-range (- m 2) -1 -1)])
        (let* ([dist (- (vector-ref id-vec (+ i 1)) (vector-ref id-vec i))]
               [allowed (+ (vector-ref h-vec (+ i 1)) dist)])
          (when (> (vector-ref h-vec i) allowed)
            (vector-set! h-vec i allowed))))
      ;; compute answer
      (let loop ([i 0] [ans 0])
        (if (>= i (- m 1))
            (let* ([last-id (vector-ref id-vec (- m 1))]
                   [last-h (vector-ref h-vec (- m 1))])
              (max ans (+ last-h (- n last-id))))
            (let* ([id1 (vector-ref id-vec i)]
                   [h1 (vector-ref h-vec i)]
                   [id2 (vector-ref id-vec (+ i 1))]
                   [h2 (vector-ref h-vec (+ i 1))]
                   [d (- id2 id1)]
                   [candidate (quotient (+ h1 h2 d) 2)])
              (loop (+ i 1) (max ans candidate)))))))))
```

## Erlang

```erlang
-module(solution).
-export([max_building/2]).

-spec max_building(N :: integer(), Restrictions :: [[integer()]]) -> integer().
max_building(N, Restrictions) ->
    Base = [[1,0]|Restrictions],
    HasN = lists:any(fun([Id,_]) -> Id == N end, Base),
    Full = if
        HasN -> Base;
        true -> [[N,1000000000]|Base]
    end,
    Sorted = lists:keysort(1, Full),
    Tuples = [{Pos,Height} || [Pos,Height] <- Sorted],
    LeftAdj = left_pass(Tuples),
    Adjusted = right_pass(LeftAdj),
    compute_max_height(Adjusted).

%% left to right pass
left_pass([First|Rest]) ->
    left_pass(Rest, [First]).
left_pass([], Acc) ->
    lists:reverse(Acc);
left_pass([{Pos,H}|Tail], [{PrevPos,PrevH}|_]=AccRev) ->
    Dist = Pos - PrevPos,
    NewH = erlang:min(H, PrevH + Dist),
    left_pass(Tail, [{Pos,NewH}|AccRev]).

%% right to left pass (reuse left_pass on reversed list)
right_pass(List) ->
    Rev = lists:reverse(List),
    RevAdj = left_pass(Rev),
    lists:reverse(RevAdj).

%% compute maximum possible height
compute_max_height(List) ->
    compute_max_pairwise(List, 0).

compute_max_pairwise([], Max) -> Max;
compute_max_pairwise([_], Max) -> Max;
compute_max_pairwise([{Pos1,H1},{Pos2,H2}|Rest], Max) ->
    Dist = Pos2 - Pos1,
    Candidate = (H1 + H2 + Dist) div 2,
    NewMax = erlang:max(Max, erlang:max(H1, erlang:max(H2, Candidate))),
    compute_max_pairwise([{Pos2,H2}|Rest], NewMax).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_building(n :: integer, restrictions :: [[integer]]) :: integer
  def max_building(n, restrictions) do
    # Convert to list of {position, height}
    rs = Enum.map(restrictions, fn [p, h] -> {p, h} end)
    # Add building 1 with height 0
    rs = [{1, 0} | rs]
    # Sort by position
    rs = Enum.sort_by(rs, fn {p, _} -> p end)

    inf = 1_000_000_000_000_000_000

    # Ensure building n is present with a very large height
    rs =
      case List.last(rs) do
        {pos, _} when pos == n -> rs
        _ -> rs ++ [{n, inf}]
      end

    # Forward pass: enforce left-to-right constraints
    forward =
      Enum.reduce(Enum.with_index(rs), [], fn {{pos, h}, idx}, acc ->
        if idx == 0 do
          [{pos, h}]
        else
          {prev_pos, prev_h} = List.last(acc)
          max_h = min(h, prev_h + (pos - prev_pos))
          acc ++ [{pos, max_h}]
        end
      end)

    # Backward pass: enforce right-to-left constraints
    backward =
      Enum.reduce(Enum.reverse(forward), [], fn {pos, h}, acc ->
        if acc == [] do
          [{pos, h}]
        else
          [{next_pos, next_h} | _] = acc
          max_h = min(h, next_h + (next_pos - pos))
          [{pos, max_h} | acc]
        end
      end)

    # Compute the maximum possible height
    {max_height, _} =
      Enum.reduce(backward, {0, nil}, fn {pos, h}, {ans, prev} ->
        ans = if h > ans, do: h, else: ans

        ans =
          case prev do
            nil -> ans
            {p_prev, h_prev} ->
              d = pos - p_prev
              peak = div(h_prev + h + d, 2)
              max(ans, peak)
          end

        {ans, {pos, h}}
      end)

    max_height
  end
end
```
