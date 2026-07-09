# 2271. Maximum White Tiles Covered by a Carpet

## Cpp

```cpp
class Solution {
public:
    int maximumWhiteTiles(vector<vector<int>>& tiles, int carpetLen) {
        sort(tiles.begin(), tiles.end());
        int n = tiles.size();
        vector<long long> pref(n + 1, 0);
        vector<int> starts(n);
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i] + (long long)tiles[i][1] - tiles[i][0] + 1;
            starts[i] = tiles[i][0];
        }
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            long long limit = (long long)tiles[i][0] + carpetLen - 1;
            int idx = upper_bound(starts.begin() + i, starts.end(), limit) - starts.begin(); // first start > limit
            long long total = pref[idx] - pref[i];
            if (idx > i) {
                int last = idx - 1;
                long long over = max(0LL, (long long)tiles[last][1] - limit);
                total -= over;
            }
            ans = max(ans, (int)total);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public int maximumWhiteTiles(int[][] tiles, int carpetLen) {
        Arrays.sort(tiles, (a, b) -> Integer.compare(a[0], b[0]));
        int n = tiles.length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + (long) tiles[i][1] - tiles[i][0] + 1;
        }
        long best = 0;
        for (int i = 0; i < n; i++) {
            long start = tiles[i][0];
            long end = start + carpetLen - 1L;

            int lo = i, hi = n;
            while (lo < hi) {
                int mid = (lo + hi) >>> 1;
                if (tiles[mid][0] <= end) {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            int idx = lo; // first interval with start > end
            long covered = prefix[idx] - prefix[i];
            if (idx > i) {
                int lastIdx = idx - 1;
                long lastEnd = tiles[lastIdx][1];
                if (lastEnd > end) {
                    covered -= (lastEnd - end);
                }
            }
            if (covered > best) {
                best = covered;
            }
        }
        return (int) best;
    }
}
```

## Python

```python
class Solution(object):
    def maximumWhiteTiles(self, tiles, carpetLen):
        """
        :type tiles: List[List[int]]
        :type carpetLen: int
        :rtype: int
        """
        # Sort intervals by their start position
        tiles.sort(key=lambda x: x[0])
        n = len(tiles)
        j = 0          # right pointer
        cur = 0        # total length of fully covered intervals between i and j-1
        ans = 0

        for i in range(n):
            start = tiles[i][0]
            end = start + carpetLen - 1

            # Expand the right side while whole interval fits inside the carpet
            while j < n and tiles[j][1] <= end:
                cur += tiles[j][1] - tiles[j][0] + 1
                j += 1

            # Compute coverage including a possible partially covered interval at j
            total = cur
            if j < n and tiles[j][0] <= end:
                total += min(end, tiles[j][1]) - tiles[j][0] + 1

            ans = max(ans, total)

            # Move left pointer forward: remove its full length from cur if it was fully counted
            if i < j:
                cur -= tiles[i][1] - tiles[i][0] + 1

        return ans
```

## Python3

```python
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        # Ensure intervals are sorted by start
        tiles.sort(key=lambda x: x[0])
        n = len(tiles)
        ans = 0
        right = 0
        cur_sum = 0
        for left in range(n):
            # Expand right pointer while the whole interval fits within carpet
            limit = tiles[left][0] + carpetLen - 1
            while right < n and tiles[right][1] <= limit:
                cur_sum += tiles[right][1] - tiles[right][0] + 1
                right += 1
            # Compute total covered including possible partial interval at 'right'
            total = cur_sum
            if right < n and tiles[right][0] <= limit:
                total += min(limit, tiles[right][1]) - tiles[right][0] + 1
            ans = max(ans, total)
            # Move left pointer forward, remove its contribution from current sum
            cur_sum -= tiles[left][1] - tiles[left][0] + 1
        return ans
```

## C

```c
#include <stdlib.h>

struct Interval {
    int l;
    int r;
};

static int cmpInterval(const void *a, const void *b) {
    const struct Interval *ia = (const struct Interval *)a;
    const struct Interval *ib = (const struct Interval *)b;
    return ia->l - ib->l;
}

int maximumWhiteTiles(int** tiles, int tilesSize, int* tilesColSize, int carpetLen) {
    if (tilesSize == 0) return 0;

    struct Interval *arr = (struct Interval *)malloc(sizeof(struct Interval) * tilesSize);
    for (int i = 0; i < tilesSize; ++i) {
        arr[i].l = tiles[i][0];
        arr[i].r = tiles[i][1];
    }

    qsort(arr, tilesSize, sizeof(struct Interval), cmpInterval);

    long long ans = 0;
    long long total = 0;          // sum of lengths of intervals fully covered
    int j = 0;

    for (int i = 0; i < tilesSize; ++i) {
        if (j < i) {
            j = i;
            total = 0;
        }

        while (j < tilesSize && (long long)arr[j].r - arr[i].l + 1 <= carpetLen) {
            total += (long long)arr[j].r - arr[j].l + 1;
            ++j;
        }

        long long cur = total;

        if (j < tilesSize) {
            long long carpetEnd = (long long)arr[i].l + carpetLen - 1;
            if (carpetEnd >= arr[j].l) {
                long long partial = carpetEnd - arr[j].l + 1;
                long long lenj = (long long)arr[j].r - arr[j].l + 1;
                if (partial > lenj) partial = lenj;
                cur += partial;
            }
        }

        if (cur > ans) ans = cur;

        if (i < j) {
            total -= (long long)arr[i].r - arr[i].l + 1;
        }
    }

    free(arr);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumWhiteTiles(int[][] tiles, int carpetLen) {
        int n = tiles.Length;
        long best = 0;
        int right = 0;
        long fullSum = 0;
        for (int left = 0; left < n; ++left) {
            long start = tiles[left][0];
            long end = start + carpetLen - 1;

            while (right < n && tiles[right][1] <= end) {
                fullSum += (long)tiles[right][1] - tiles[right][0] + 1;
                right++;
            }

            long total = fullSum;
            if (right < n && tiles[right][0] <= end) {
                total += Math.Min(end, (long)tiles[right][1]) - tiles[right][0] + 1;
            }
            if (total > best) best = total;

            // Remove left interval from fullSum if it was fully covered
            long leftEnd = tiles[left][1];
            if (leftEnd <= end) {
                fullSum -= (long)leftEnd - tiles[left][0] + 1;
            }
        }
        return (int)best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} tiles
 * @param {number} carpetLen
 * @return {number}
 */
var maximumWhiteTiles = function(tiles, carpetLen) {
    // Sort intervals by start position
    tiles.sort((a, b) => a[0] - b[0]);
    const n = tiles.length;
    const start = new Array(n);
    const end = new Array(n);
    const len = new Array(n);
    for (let i = 0; i < n; ++i) {
        start[i] = tiles[i][0];
        end[i] = tiles[i][1];
        len[i] = end[i] - start[i] + 1;
    }
    // Prefix sums of lengths
    const pref = new Array(n + 1);
    pref[0] = 0;
    for (let i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + len[i];
    }

    let ans = 0;
    for (let i = 0; i < n; ++i) {
        const carpetEnd = start[i] + carpetLen - 1;

        // Find the last interval fully covered by the carpet
        let lo = i, hi = n - 1, pos = i - 1;
        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            if (end[mid] <= carpetEnd) {
                pos = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }

        // Total length of fully covered intervals
        let totalFull = 0;
        if (pos >= i) {
            totalFull = pref[pos + 1] - pref[i];
        }

        // Possibly partially cover the next interval
        let cur = totalFull;
        const nxt = pos + 1;
        if (nxt < n) {
            const overlap = Math.max(0, carpetEnd - start[nxt] + 1);
            cur += Math.min(overlap, len[nxt]);
        }

        if (cur > ans) ans = cur;
    }
    return ans;
};
```

## Typescript

```typescript
function maximumWhiteTiles(tiles: number[][], carpetLen: number): number {
    tiles.sort((a, b) => a[0] - b[0]);
    const n = tiles.length;
    const pref = new Array<number>(n + 1);
    pref[0] = 0;
    for (let i = 0; i < n; ++i) {
        const len = tiles[i][1] - tiles[i][0] + 1;
        pref[i + 1] = pref[i] + len;
    }
    let ans = 0;
    let j = 0;
    for (let i = 0; i < n; ++i) {
        if (j < i) j = i;
        const start = tiles[i][0];
        const endPos = start + carpetLen - 1;
        while (j < n && tiles[j][0] <= endPos) {
            ++j;
        }
        const lastIdx = j - 1;
        let total = 0;
        if (lastIdx >= i) {
            total = pref[lastIdx] - pref[i];
            const cover = Math.min(endPos, tiles[lastIdx][1]) - tiles[lastIdx][0] + 1;
            if (cover > 0) total += cover;
        }
        if (total > ans) ans = total;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $tiles
     * @param Integer $carpetLen
     * @return Integer
     */
    function maximumWhiteTiles($tiles, $carpetLen) {
        // Sort intervals by their start position
        usort($tiles, function ($a, $b) {
            return $a[0] <=> $b[0];
        });

        $n = count($tiles);
        $starts = [];
        $pref = array_fill(0, $n + 1, 0); // prefix sums of interval lengths

        for ($i = 0; $i < $n; $i++) {
            $starts[$i] = $tiles[$i][0];
            $len = $tiles[$i][1] - $tiles[$i][0] + 1;
            $pref[$i + 1] = $pref[$i] + $len;
        }

        $maxCovered = 0;

        for ($i = 0; $i < $n; $i++) {
            $carpetEnd = $tiles[$i][0] + $carpetLen - 1;

            // Binary search for first interval with start > carpetEnd
            $l = $i;
            $r = $n;
            while ($l < $r) {
                $mid = intdiv($l + $r, 2);
                if ($starts[$mid] <= $carpetEnd) {
                    $l = $mid + 1;
                } else {
                    $r = $mid;
                }
            }
            $j = $l; // intervals [i, j-1] have start <= carpetEnd

            $total = $pref[$j] - $pref[$i]; // sum of full lengths in window

            if ($j - 1 >= $i) {
                $excess = $tiles[$j - 1][1] - $carpetEnd;
                if ($excess > 0) {
                    $total -= $excess; // adjust for partial coverage of last interval
                }
            }

            if ($total > $maxCovered) {
                $maxCovered = $total;
            }
        }

        return $maxCovered;
    }
}
```

## Swift

```swift
class Solution {
    func maximumWhiteTiles(_ tiles: [[Int]], _ carpetLen: Int) -> Int {
        let sorted = tiles.sorted { $0[0] < $1[0] }
        let n = sorted.count
        var starts = [Int]()
        var ends = [Int]()
        var pref = [Int64]()
        pref.append(0)
        for t in sorted {
            let l = t[0]
            let r = t[1]
            starts.append(l)
            ends.append(r)
            let len = Int64(r - l + 1)
            pref.append(pref.last! + len)
        }
        var answer: Int64 = 0
        for i in 0..<n {
            let leftStart = starts[i]
            let carpetEnd = leftStart + carpetLen - 1
            // binary search first index with start > carpetEnd
            var lo = i
            var hi = n
            while lo < hi {
                let mid = (lo + hi) / 2
                if starts[mid] <= carpetEnd {
                    lo = mid + 1
                } else {
                    hi = mid
                }
            }
            let idx = lo // first start > carpetEnd
            var total: Int64 = 0
            if idx == n {
                // all remaining intervals start within coverage
                if i < n - 1 {
                    total += pref[n - 1] - pref[i]
                }
                let overlap = max(0, min(ends[n - 1], carpetEnd) - starts[n - 1] + 1)
                total += Int64(overlap)
            } else {
                // intervals i .. idx-2 are fully covered
                if i < idx - 1 {
                    total += pref[idx - 1] - pref[i]
                }
                let lastIdx = idx - 1
                let overlap = max(0, min(ends[lastIdx], carpetEnd) - starts[lastIdx] + 1)
                total += Int64(overlap)
            }
            if total > answer {
                answer = total
            }
        }
        return Int(answer)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumWhiteTiles(tiles: Array<IntArray>, carpetLen: Int): Int {
        val sorted = tiles.sortedBy { it[0] }
        val n = sorted.size
        var left = 0
        var right = 0
        var curFull = 0L
        var ans = 0L
        while (left < n) {
            while (right < n && curFull + (sorted[right][1] - sorted[right][0] + 1).toLong() <= carpetLen.toLong()) {
                curFull += (sorted[right][1] - sorted[right][0] + 1).toLong()
                right++
            }
            var total = curFull
            if (right < n) {
                val remaining = carpetLen.toLong() - curFull
                val len = (sorted[right][1] - sorted[right][0] + 1).toLong()
                total += minOf(remaining, len)
            }
            ans = maxOf(ans, total)
            if (right > left) {
                curFull -= (sorted[left][1] - sorted[left][0] + 1).toLong()
            } else {
                right = left + 1
            }
            left++
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int maximumWhiteTiles(List<List<int>> tiles, int carpetLen) {
    // Ensure tiles are sorted by their start positions
    tiles.sort((a, b) => a[0].compareTo(b[0]));
    int n = tiles.length;

    // Prefix sums of tile lengths
    List<int> pref = List.filled(n + 1, 0);
    for (int i = 0; i < n; i++) {
      int len = tiles[i][1] - tiles[i][0] + 1;
      pref[i + 1] = pref[i] + len;
    }

    int ans = 0;

    for (int i = 0; i < n; i++) {
      int leftStart = tiles[i][0];
      int rightBound = leftStart + carpetLen - 1;

      // Binary search for first interval with start > rightBound
      int lo = i, hi = n;
      while (lo < hi) {
        int mid = (lo + hi) >> 1;
        if (tiles[mid][0] <= rightBound) {
          lo = mid + 1;
        } else {
          hi = mid;
        }
      }
      int idx = lo; // first start > rightBound
      int j = idx - 1; // last interval that starts within carpet range

      // Sum of fully covered intervals from i to j-1
      int total = pref[j] - pref[i];

      // Partial coverage on interval j
      int partial = rightBound - tiles[j][0] + 1;
      if (partial > 0) {
        int lenJ = tiles[j][1] - tiles[j][0] + 1;
        total += min(partial, lenJ);
      }

      ans = max(ans, total);
    }

    return ans;
  }
}
```

## Golang

```go
import "sort"

func maximumWhiteTiles(tiles [][]int, carpetLen int) int {
	sort.Slice(tiles, func(i, j int) bool { return tiles[i][0] < tiles[j][0] })
	n := len(tiles)
	pref := make([]int64, n+1)
	for i := 0; i < n; i++ {
		length := int64(tiles[i][1]-tiles[i][0]+1)
		pref[i+1] = pref[i] + length
	}
	var maxCover int64
	for i := 0; i < n; i++ {
		start := tiles[i][0]
		end := start + carpetLen - 1
		lo, hi := i, n
		for lo < hi {
			mid := (lo + hi) / 2
			if tiles[mid][0] > end {
				hi = mid
			} else {
				lo = mid + 1
			}
		}
		idx := lo // first tile with start > end
		total := pref[idx] - pref[i]
		if idx > i {
			lastIdx := idx - 1
			if tiles[lastIdx][1] > end {
				excess := int64(tiles[lastIdx][1] - end)
				total -= excess
			}
		}
		if total > maxCover {
			maxCover = total
		}
	}
	return int(maxCover)
}
```

## Ruby

```ruby
def maximum_white_tiles(tiles, carpet_len)
  tiles.sort_by! { |a| a[0] }
  n = tiles.length
  prefix = Array.new(n + 1, 0)
  (0...n).each do |i|
    len = tiles[i][1] - tiles[i][0] + 1
    prefix[i + 1] = prefix[i] + len
  end

  ans = 0
  right = 0
  (0...n).each do |left|
    start_pos = tiles[left][0]
    limit = start_pos + carpet_len - 1
    while right < n && tiles[right][0] <= limit
      right += 1
    end

    total = prefix[right] - prefix[left]

    if right > left
      last_idx = right - 1
      if tiles[last_idx][1] > limit
        excess = tiles[last_idx][1] - limit
        total -= excess
      end
    end

    ans = total if total > ans
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maximumWhiteTiles(tiles: Array[Array[Int]], carpetLen: Int): Int = {
        val n = tiles.length
        val sorted = tiles.sortBy(_(0))
        val L = new Array[Long](n)
        val R = new Array[Long](n)
        for (i <- 0 until n) {
            L(i) = sorted(i)(0).toLong
            R(i) = sorted(i)(1).toLong
        }
        val pref = new Array[Long](n + 1)
        for (i <- 0 until n) {
            pref(i + 1) = pref(i) + (R(i) - L(i) + 1)
        }

        var ans: Long = 0L
        val len = carpetLen.toLong

        for (i <- 0 until n) {
            val start = L(i)
            val end = start + len - 1

            var lo = i
            var hi = n
            while (lo < hi) {
                val mid = (lo + hi) >>> 1
                if (R(mid) <= end) lo = mid + 1 else hi = mid
            }
            val k = lo // first index where R > end

            var total = pref(k) - pref(i)
            if (k < n && L(k) <= end) {
                total += Math.min(end, R(k)) - L(k) + 1
            }
            if (total > ans) ans = total
        }

        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_white_tiles(tiles: Vec<Vec<i32>>, carpet_len: i32) -> i32 {
        let n = tiles.len();
        if n == 0 {
            return 0;
        }
        // Convert to (start, end) pairs and sort by start.
        let mut intervals: Vec<(i64, i64)> = tiles
            .into_iter()
            .map(|v| (v[0] as i64, v[1] as i64))
            .collect();
        intervals.sort_by_key(|x| x.0);

        // Prefix sums of interval lengths.
        let mut pref: Vec<i64> = vec![0; n + 1];
        for i in 0..n {
            let len = intervals[i].1 - intervals[i].0 + 1;
            pref[i + 1] = pref[i] + len;
        }

        let mut ans: i64 = 0;
        let carpet_len_i64 = carpet_len as i64;

        for i in 0..n {
            let start = intervals[i].0;
            let end = start + carpet_len_i64 - 1;

            // Find first interval whose start > end.
            let mut lo = i;
            let mut hi = n;
            while lo < hi {
                let mid = (lo + hi) / 2;
                if intervals[mid].0 <= end {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            let idx = lo; // first start > end

            // Total tiles from i to idx-1 (inclusive).
            let mut covered = pref[idx] - pref[i];

            // Adjust if the last interval extends beyond carpet's end.
            if idx > i {
                let last = idx - 1;
                if intervals[last].1 > end {
                    covered -= intervals[last].1 - end;
                }
            }

            if covered > ans {
                ans = covered;
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (maximum-white-tiles tiles carpetLen)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((sorted (sort tiles (lambda (a b) (< (first a) (first b)))))
         (vec (list->vector sorted))
         (n (vector-length vec)))
    (let loop ((i 0) (j 0) (cur-sum 0) (ans 0))
      (if (>= i n)
          ans
          (let* ((li (first (vector-ref vec i)))
                 (end (+ li carpetLen -1)))
            ;; expand right pointer to include fully covered tiles
            (define-values (new-j new-sum)
              (let expand ((jj j) (sum cur-sum))
                (if (or (>= jj n)
                        (> (second (vector-ref vec jj)) end))
                    (values jj sum)
                    (let* ((tile (vector-ref vec jj))
                           (len (+ (- (second tile) (first tile)) 1)))
                      (expand (+ jj 1) (+ sum len))))))

            ;; possibly add a partially covered tile
            (define partial
              (if (and (< new-j n)
                       (<= (first (vector-ref vec new-j)) end))
                  (+ (- end (first (vector-ref vec new-j))) 1)
                  0))

            (define total (+ new-sum partial))
            (define ans2 (max ans total))

            ;; prepare cur-sum for next left index
            (define cur-sum-next
              (if (< i new-j)
                  (let* ((tilei (vector-ref vec i))
                         (leni (+ (- (second tilei) (first tilei)) 1)))
                    (- new-sum leni))
                  new-sum))

            (loop (+ i 1) new-j cur-sum-next ans2))))))
```

## Erlang

```erlang
-spec maximum_white_tiles(Tiles :: [[integer()]], CarpetLen :: integer()) -> integer().
maximum_white_tiles(Tiles, CarpetLen) ->
    Sorted = lists:keysort(1, Tiles),
    {StartsList, EndsList} = build_lists(Sorted, [], []),
    Starts = list_to_tuple(lists:reverse(StartsList)),
    Ends = list_to_tuple(lists:reverse(EndsList)),
    N = tuple_size(Starts),
    loop(1, N, Starts, Ends, CarpetLen, 1, 0, 0).

build_lists([], SAcc, EAcc) -> {SAcc, EAcc};
build_lists([[L,R]|Rest], SAcc, EAcc) ->
    build_lists(Rest, [L|SAcc], [R|EAcc]).

loop(L, N, _Starts, _Ends, _CarpetLen, _R, _CurFull, Max) when L > N -> Max;
loop(L, N, Starts, Ends, CarpetLen, R, CurFull, Max) ->
    StartL = element(L, Starts),
    EndCarpet = StartL + CarpetLen - 1,
    {R2, CurFull2} = expand(R, N, Starts, Ends, EndCarpet, CurFull),
    Partial =
        if
            R2 =< N, element(R2, Starts) =< EndCarpet ->
                EndCarpet - element(R2, Starts) + 1;
            true -> 0
        end,
    NewMax = erlang:max(Max, CurFull2 + Partial),
    CurFull3 =
        if
            element(L, Ends) =< EndCarpet ->
                CurFull2 - (element(L, Ends) - element(L, Starts) + 1);
            true -> CurFull2
        end,
    loop(L + 1, N, Starts, Ends, CarpetLen, R2, CurFull3, NewMax).

expand(R, N, Starts, Ends, EndCarpet, CurFull) when R =< N,
                                                    element(R, Ends) =< EndCarpet ->
    Len = element(R, Ends) - element(R, Starts) + 1,
    expand(R + 1, N, Starts, Ends, EndCarpet, CurFull + Len);
expand(R, _N, _Starts, _Ends, _EndCarpet, CurFull) -> {R, CurFull}.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_white_tiles(tiles :: [[integer]], carpet_len :: integer) :: integer
  def maximum_white_tiles(tiles, carpet_len) do
    sorted = Enum.sort_by(tiles, fn [l, _] -> l end)
    n = length(sorted)

    l_arr = List.to_tuple(Enum.map(sorted, fn [l, _] -> l end))
    r_arr = List.to_tuple(Enum.map(sorted, fn [_ , r] -> r end))
    len_arr = List.to_tuple(Enum.map(sorted, fn [l, r] -> r - l + 1 end))

    pref =
      Enum.reduce(0..(n - 1), [0], fn idx, acc ->
        prev = hd(acc)
        len = elem(len_arr, idx)
        [prev + len | acc]
      end)
      |> Enum.reverse()
      |> List.to_tuple()

    0..(n - 1)
    |> Enum.reduce(0, fn i, ans ->
      start = elem(l_arr, i)
      end_pos = start + carpet_len - 1

      idx = upper_bound(r_arr, end_pos, 0, n)

      total_full = elem(pref, idx) - elem(pref, i)

      extra =
        if idx < n do
          l_idx = elem(l_arr, idx)
          max(0, end_pos - l_idx + 1)
        else
          0
        end

      cur = total_full + extra
      if cur > ans, do: cur, else: ans
    end)
  end

  defp upper_bound(arr, target, low, high) when low < high do
    mid = div(low + high, 2)
    val = elem(arr, mid)

    if val <= target do
      upper_bound(arr, target, mid + 1, high)
    else
      upper_bound(arr, target, low, mid)
    end
  end

  defp upper_bound(_arr, _target, low, _high), do: low
end
```
