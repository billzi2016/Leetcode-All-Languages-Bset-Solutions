# 3048. Earliest Second to Mark Indices I

## Cpp

```cpp
class Solution {
public:
    bool feasible(const vector<int>& nums, const vector<int>& changeIndices, int T) {
        int n = nums.size();
        vector<int> lastPos(n, -1);
        for (int i = 0; i < T; ++i) {
            int idx = changeIndices[i] - 1;
            lastPos[idx] = i + 1; // seconds are 1-indexed
        }
        // every index must appear at least once up to T
        for (int p : lastPos) if (p == -1) return false;

        vector<pair<int,long long>> tasks;
        tasks.reserve(n);
        for (int i = 0; i < n; ++i) {
            tasks.emplace_back(lastPos[i], (long long)nums[i]);
        }
        sort(tasks.begin(), tasks.end(),
             [](const auto& a, const auto& b){ return a.first < b.first; });

        long long cur = 0;
        for (auto &pr : tasks) {
            int deadline = pr.first;
            long long need = pr.second + 1; // decrements + marking second
            cur += need;
            if (cur > deadline) return false;
        }
        return true;
    }

    int earliestSecondToMarkIndices(vector<int>& nums, vector<int>& changeIndices) {
        int m = changeIndices.size();
        int lo = 1, hi = m, ans = -1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (feasible(nums, changeIndices, mid)) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int earliestSecondToMarkIndices(int[] nums, int[] changeIndices) {
        int n = nums.length;
        int m = changeIndices.length;
        int left = 1, right = m, answer = -1;
        while (left <= right) {
            int mid = (left + right) >>> 1;
            if (canMark(nums, changeIndices, n, mid)) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return answer;
    }

    private boolean canMark(int[] nums, int[] changeIndices, int n, int limit) {
        int[] lastPos = new int[n];
        for (int i = 0; i < n; i++) lastPos[i] = -1;

        // record last occurrence within first 'limit' seconds
        for (int i = 0; i < limit; i++) {
            int idx = changeIndices[i] - 1;
            lastPos[idx] = i + 1; // store as 1‑based position
        }

        // every index must appear at least once
        for (int pos : lastPos) {
            if (pos == -1) return false;
        }

        // collect events (position, required decrements)
        Event[] ev = new Event[n];
        for (int i = 0; i < n; i++) {
            ev[i] = new Event(lastPos[i], nums[i]);
        }
        java.util.Arrays.sort(ev, (a, b) -> Integer.compare(a.pos, b.pos));

        long needed = 0;
        int marked = 0;
        for (Event e : ev) {
            needed += e.val;          // total decrements required so far
            marked++;                 // one more index will be marked at this time
            long available = (long) e.pos - marked; // seconds before this mark not used for marking
            if (needed > available) return false;
        }
        return true;
    }

    private static class Event {
        int pos;
        int val;
        Event(int p, int v) { pos = p; val = v; }
    }
}
```

## Python

```python
class Solution(object):
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        """
        :type nums: List[int]
        :type changeIndices: List[int]
        :rtype: int
        """
        n = len(nums)
        m = len(changeIndices)

        def feasible(x):
            # last occurrence (1-indexed) of each index within first x seconds
            last = [-1] * n
            for idx in range(x):
                i = changeIndices[idx] - 1
                last[i] = idx + 1
            if any(v == -1 for v in last):
                return False
            # sort by marking time
            pairs = sorted(((last[i], nums[i]) for i in range(n)), key=lambda p: p[0])
            sum_dec = 0
            marked = 0
            for pos, need in pairs:
                sum_dec += need
                marked += 1
                # seconds available for decrements up to this marking time
                if sum_dec > pos - marked:
                    return False
            return True

        # quick check if possible at all
        if not feasible(m):
            return -1

        lo, hi = 1, m
        ans = m
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n = len(nums)
        m = len(changeIndices)

        def feasible(limit: int) -> bool:
            last = [-1] * n
            for idx in range(limit):
                i = changeIndices[idx] - 1
                last[i] = idx + 1  # store 1-indexed position

            for i in range(n):
                if last[i] == -1:
                    return False

            pairs = [(last[i], nums[i]) for i in range(n)]
            pairs.sort()  # sort by marking time

            cum_need = 0
            marked = 0
            for pos, need in pairs:
                cum_need += need
                marked += 1
                if cum_need > pos - marked:
                    return False
            return True

        lo, hi = 1, m
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
```

## C

```c
#include <stdlib.h>

typedef struct {
    int deadline;
    int idx;
} Pair;

static int cmpPair(const void *a, const void *b) {
    const Pair *pa = (const Pair *)a;
    const Pair *pb = (const Pair *)b;
    return pa->deadline - pb->deadline;
}

static int can(int x, int* nums, int n, int* changeIndices, int m) {
    int *last = (int*)calloc(n, sizeof(int));
    if (!last) return 0;

    for (int i = 0; i < x; ++i) {
        int idx = changeIndices[i] - 1;
        last[idx] = i + 1; // store 1‑based second
    }

    // check all indices appear
    for (int i = 0; i < n; ++i) {
        if (last[i] == 0) {
            free(last);
            return 0;
        }
    }

    Pair *arr = (Pair*)malloc(n * sizeof(Pair));
    if (!arr) { free(last); return 0; }

    for (int i = 0; i < n; ++i) {
        arr[i].deadline = last[i];
        arr[i].idx = i;
    }
    free(last);

    qsort(arr, n, sizeof(Pair), cmpPair);

    long long sumVals = 0;
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        cnt++;
        sumVals += (long long)nums[arr[i].idx];
        long long available = (long long)arr[i].deadline - cnt;
        if (available < sumVals) {
            free(arr);
            return 0;
        }
    }

    free(arr);
    return 1;
}

int earliestSecondToMarkIndices(int* nums, int numsSize, int* changeIndices, int changeIndicesSize){
    int lo = 1, hi = changeIndicesSize, ans = -1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (can(mid, nums, numsSize, changeIndices, changeIndicesSize)) {
            ans = mid;
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int EarliestSecondToMarkIndices(int[] nums, int[] changeIndices) {
        int n = nums.Length;
        int m = changeIndices.Length;

        bool Can(int x) {
            int[] lastPos = new int[n];
            for (int i = 0; i < n; i++) lastPos[i] = -1;
            for (int pos = 0; pos < x; pos++) {
                int idx = changeIndices[pos] - 1; // convert to 0‑based
                lastPos[idx] = pos + 1; // store as 1‑based position
            }

            var list = new List<(int pos, long need)>(n);
            for (int i = 0; i < n; i++) {
                if (lastPos[i] == -1) return false; // never appears up to x
                list.Add((lastPos[i], (long)nums[i]));
            }

            list.Sort((a, b) => a.pos.CompareTo(b.pos));

            long sum = 0;
            int cnt = 0;
            foreach (var p in list) {
                sum += p.need;
                cnt++;
                if (sum > p.pos - cnt) return false; // not enough free seconds
            }
            return true;
        }

        int lo = 1, hi = m, ans = -1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (Can(mid)) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} changeIndices
 * @return {number}
 */
var earliestSecondToMarkIndices = function(nums, changeIndices) {
    const n = nums.length;
    const m = changeIndices.length;

    // check if all indices appear at least once up to limit seconds
    const can = (limit) => {
        const lastPos = new Array(n).fill(0);
        for (let i = 0; i < limit; ++i) {
            const idx = changeIndices[i] - 1;
            lastPos[idx] = i + 1; // store 1‑based position
        }
        // every index must have a marking opportunity
        for (let i = 0; i < n; ++i) {
            if (lastPos[i] === 0) return false;
        }

        const pairs = [];
        for (let i = 0; i < n; ++i) {
            pairs.push([lastPos[i], nums[i]]);
        }
        // sort by the last occurrence position
        pairs.sort((a, b) => a[0] - b[0]);

        let sumNeed = 0;
        for (let k = 0; k < pairs.length; ++k) {
            const pos = pairs[k][0];
            const need = pairs[k][1];
            sumNeed += need;
            // after marking k+1 indices up to time 'pos',
            // only (pos - (k+1)) seconds are available for decrements
            if (sumNeed > pos - (k + 1)) return false;
        }
        return true;
    };

    let left = 1, right = m, answer = -1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (can(mid)) {
            answer = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return answer;
};
```

## Typescript

```typescript
function earliestSecondToMarkIndices(nums: number[], changeIndices: number[]): number {
    const n = nums.length;
    const m = changeIndices.length;

    const can = (t: number): boolean => {
        const lastPos = new Array<number>(n).fill(-1);
        for (let i = 0; i < t; i++) {
            const idx = changeIndices[i] - 1; // to 0‑based
            lastPos[idx] = i + 1; // store as 1‑based position
        }
        const pairs: [number, number][] = [];
        for (let i = 0; i < n; i++) {
            if (lastPos[i] === -1) return false;
            pairs.push([lastPos[i], nums[i]]);
        }
        pairs.sort((a, b) => a[0] - b[0]);

        let marks = 0;
        let decNeeded = 0;
        for (const [pos, val] of pairs) {
            marks++;
            decNeeded += val;
            // available seconds for decrements up to 'pos' are pos - marks
            if (decNeeded > pos - marks) return false;
        }
        return true;
    };

    let left = 1, right = m, answer = -1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (can(mid)) {
            answer = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $changeIndices
     * @return Integer
     */
    function earliestSecondToMarkIndices($nums, $changeIndices) {
        $n = count($nums);
        $m = count($changeIndices);
        // binary search on answer
        $lo = 1;
        $hi = $m;
        $ans = -1;

        while ($lo <= $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($this->canMarkWithin($mid, $nums, $changeIndices, $n)) {
                $ans = $mid;
                $hi = $mid - 1;
            } else {
                $lo = $mid + 1;
            }
        }

        return $ans;
    }

    private function canMarkWithin($limit, $nums, $changeIndices, $n) {
        // last occurrence positions (1-indexed), -1 means not present
        $lastPos = array_fill(0, $n + 1, -1);
        for ($i = 0; $i < $limit; ++$i) {
            $idx = $changeIndices[$i]; // already 1-indexed in input
            $lastPos[$idx] = $i + 1;   // store as 1-indexed second
        }

        // every index must appear at least once
        for ($j = 1; $j <= $n; ++$j) {
            if ($lastPos[$j] == -1) {
                return false;
            }
        }

        // collect pairs (position, index)
        $pairs = [];
        for ($j = 1; $j <= $n; ++$j) {
            $pairs[] = [$lastPos[$j], $j];
        }
        usort($pairs, function($a, $b) {
            return $a[0] <=> $b[0];
        });

        $cntMarked = 0;
        $sumNeeded = 0; // total nums values of already marked indices

        foreach ($pairs as $pair) {
            [$pos, $idx] = $pair;
            $need = $nums[$idx - 1]; // convert to 0-index
            // available decrement slots before this second:
            // total seconds elapsed (pos) minus seconds used for previous marks (cntMarked)
            // minus decrements already spent on previous indices (sumNeeded)
            if ($pos - $cntMarked - $sumNeeded < $need) {
                return false;
            }
            $cntMarked++;
            $sumNeeded += $need;
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func earliestSecondToMarkIndices(_ nums: [Int], _ changeIndices: [Int]) -> Int {
        let n = nums.count
        let m = changeIndices.count
        
        func can(_ t: Int) -> Bool {
            var lastPos = Array(repeating: -1, count: n)
            if t > 0 {
                for s in 0..<t {
                    let idx = changeIndices[s] - 1
                    lastPos[idx] = s + 1   // store as 1‑based position
                }
            }
            var pairs: [(pos: Int, need: Int)] = []
            for i in 0..<n {
                if lastPos[i] == -1 { return false }          // index never appears up to t
                pairs.append((pos: lastPos[i], need: nums[i]))
            }
            pairs.sort { $0.pos < $1.pos }
            
            var totalNeeded = 0
            var marks = 0
            for p in pairs {
                totalNeeded += p.need
                marks += 1
                if p.pos - marks < totalNeeded {   // not enough seconds left for decrements
                    return false
                }
            }
            return true
        }
        
        if !can(m) { return -1 }
        var lo = 1, hi = m, ans = m
        while lo <= hi {
            let mid = (lo + hi) / 2
            if can(mid) {
                ans = mid
                hi = mid - 1
            } else {
                lo = mid + 1
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun earliestSecondToMarkIndices(nums: IntArray, changeIndices: IntArray): Int {
        val n = nums.size
        val m = changeIndices.size

        fun can(limit: Int): Boolean {
            val lastPos = IntArray(n) { -1 }
            for (i in 0 until limit) {
                val idx = changeIndices[i] - 1
                lastPos[idx] = i + 1 // seconds are 1-indexed
            }
            for (pos in lastPos) if (pos == -1) return false

            data class Job(val deadline: Int, val need: Long)
            val jobs = ArrayList<Job>(n)
            for (i in 0 until n) {
                jobs.add(Job(lastPos[i], nums[i].toLong()))
            }
            jobs.sortBy { it.deadline }

            var cumNeed = 0L
            for ((index, job) in jobs.withIndex()) {
                cumNeed += job.need
                val cnt = index + 1 // number of marked indices so far
                if (cumNeed + cnt > job.deadline.toLong()) return false
            }
            return true
        }

        var lo = 1
        var hi = m
        var ans = -1
        while (lo <= hi) {
            val mid = (lo + hi) ushr 1
            if (can(mid)) {
                ans = mid
                hi = mid - 1
            } else {
                lo = mid + 1
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int earliestSecondToMarkIndices(List<int> nums, List<int> changeIndices) {
    int n = nums.length;
    int m = changeIndices.length;

    bool can(int T) {
      // last occurrence (1-based) of each index within first T seconds
      List<int> lastPos = List.filled(n, -1);
      for (int s = 0; s < T; ++s) {
        int idx = changeIndices[s] - 1;
        lastPos[idx] = s + 1; // store as 1-based position
      }
      // every index must appear at least once
      for (int i = 0; i < n; ++i) {
        if (lastPos[i] == -1) return false;
      }

      // collect pairs (position, index)
      List<List<int>> pairs = [];
      for (int i = 0; i < n; ++i) {
        pairs.add([lastPos[i], i]);
      }
      pairs.sort((a, b) => a[0].compareTo(b[0]));

      int usedDecr = 0;
      int usedMark = 0;
      for (var p in pairs) {
        int pos = p[0]; // 1-based second when we will mark this index
        int idx = p[1];
        int need = nums[idx];
        int available = pos - usedDecr - usedMark;
        if (available < need) return false;
        usedDecr += need;
        usedMark += 1;
      }
      return true;
    }

    // If impossible even after all seconds
    if (!can(m)) return -1;

    int low = 1, high = m;
    while (low < high) {
      int mid = (low + high) >> 1;
      if (can(mid)) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }
    return low;
  }
}
```

## Golang

```go
func earliestSecondToMarkIndices(nums []int, changeIndices []int) int {
    n := len(nums)
    m := len(changeIndices)

    // Helper to check feasibility within first t seconds
    can := func(t int) bool {
        last := make([]int, n) // 1-indexed positions, 0 means not seen
        for i := 0; i < t; i++ {
            idx := changeIndices[i] - 1
            last[idx] = i + 1 // store position as 1-based
        }
        // Every index must appear at least once
        for i := 0; i < n; i++ {
            if last[i] == 0 {
                return false
            }
        }

        add := make([]int64, t+2)   // sum of required decrements whose mark is at position s
        cntMark := make([]int, t+2) // number of marks at position s

        for i := 0; i < n; i++ {
            pos := last[i]
            add[pos] += int64(nums[i])
            cntMark[pos]++
        }

        var cumReq int64
        marksSoFar := 0
        for s := 1; s <= t; s++ {
            cumReq += add[s]
            marksSoFar += cntMark[s]
            if cumReq > int64(s-marksSoFar) {
                return false
            }
        }
        return true
    }

    // If impossible even after all seconds, return -1
    if !can(m) {
        return -1
    }

    lo, hi := 1, m
    ans := m
    for lo <= hi {
        mid := (lo + hi) / 2
        if can(mid) {
            ans = mid
            hi = mid - 1
        } else {
            lo = mid + 1
        }
    }
    return ans
}
```

## Ruby

```ruby
def earliest_second_to_mark_indices(nums, change_indices)
  n = nums.length
  m = change_indices.length

  # Helper to check if all indices can be marked within first x seconds
  possible = lambda do |x|
    last = Array.new(n, -1)
    (0...x).each do |i|
      idx = change_indices[i] - 1
      last[idx] = i + 1   # store 1‑based position
    end

    # every index must appear at least once
    (0...n).each { |i| return false if last[i] == -1 }

    pairs = []
    (0...n).each { |i| pairs << [last[i], i] }
    pairs.sort_by! { |p| p[0] }

    total_needed = 0
    marks_done   = 0

    pairs.each do |pos, idx|
      total_needed += nums[idx]
      available = pos - marks_done
      return false if total_needed > available
      marks_done += 1
    end
    true
  end

  lo = 1
  hi = m
  ans = -1
  while lo <= hi
    mid = (lo + hi) / 2
    if possible.call(mid)
      ans = mid
      hi = mid - 1
    else
      lo = mid + 1
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
  def earliestSecondToMarkIndices(nums: Array[Int], changeIndices: Array[Int]): Int = {
    val n = nums.length
    val m = changeIndices.length

    def can(t: Int): Boolean = {
      val lastPos = Array.fill(n)(0)
      var i = 0
      while (i < t) {
        val idx = changeIndices(i) - 1
        lastPos(idx) = i + 1 // store 1‑based position
        i += 1
      }
      var j = 0
      while (j < n) {
        if (lastPos(j) == 0) return false
        j += 1
      }

      val pairs = new Array[(Int, Long)](n)
      j = 0
      while (j < n) {
        pairs(j) = (lastPos(j), nums(j).toLong)
        j += 1
      }
      java.util.Arrays.sort(pairs, new java.util.Comparator[(Int, Long)] {
        def compare(a: (Int, Long), b: (Int, Long)): Int = a._1 - b._1
      })

      var cum: Long = 0L
      var cnt = 0
      var k = 0
      while (k < n) {
        val (p, need) = pairs(k)
        cnt += 1
        cum += need
        val capacity = p - cnt // seconds left for decrements before this mark
        if (cum > capacity.toLong) return false
        k += 1
      }
      true
    }

    var lo = 1
    var hi = m
    var ans = -1
    while (lo <= hi) {
      val mid = (lo + hi) >>> 1
      if (can(mid)) {
        ans = mid
        hi = mid - 1
      } else {
        lo = mid + 1
      }
    }
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn earliest_second_to_mark_indices(nums: Vec<i32>, change_indices: Vec<i32>) -> i32 {
        let n = nums.len();
        let m = change_indices.len();

        // Helper closure to check feasibility up to time x (1-indexed inclusive)
        let feasible = |x: usize, nums: &Vec<i32>, change_indices: &Vec<i32>| -> bool {
            let mut last: Vec<Option<usize>> = vec![None; n];
            for s in 0..x {
                let idx = (change_indices[s] - 1) as usize;
                // store the latest occurrence (1-indexed)
                last[idx] = Some(s + 1);
            }
            // collect positions, ensure every index appears
            let mut pairs: Vec<(usize, usize)> = Vec::with_capacity(n);
            for i in 0..n {
                match last[i] {
                    Some(pos) => pairs.push((pos, i)),
                    None => return false,
                }
            }
            // sort by the time we will mark them (latest occurrence)
            pairs.sort_by_key(|k| k.0);

            let mut total_needed: i64 = 0;
            let mut marks_done: i64 = 0;
            for (pos, idx) in pairs {
                total_needed += nums[idx] as i64;
                let time = pos as i64;
                // before this second we have 'time - marks_done' slots for decrements
                if total_needed > time - marks_done {
                    return false;
                }
                marks_done += 1;
            }
            true
        };

        let mut left = 1usize;
        let mut right = m;
        let mut answer: i32 = -1;

        while left <= right {
            let mid = (left + right) / 2;
            if feasible(mid, &nums, &change_indices) {
                answer = mid as i32;
                if mid == 0 { break; }
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (earliest-second-to-mark-indices nums changeIndices)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)]
         [m (length changeIndices)]
         [numsV (list->vector nums)]
         [changeV (list->vector changeIndices)])
    ;; feasibility test for a given prefix length x (1‑based)
    (define (feasible? x)
      (let ([lastPos (make-vector n 0)])
        ;; record last occurrence up to second x
        (for ([i (in-range x)])
          (let* ([idx (- (vector-ref changeV i) 1)]) ; to 0‑based
            (vector-set! lastPos idx (+ i 1))))
        ;; every index must appear at least once
        (let loop ((i 0))
          (if (= i n)
              #t
              (if (= (vector-ref lastPos i) 0)
                  #f
                  (loop (+ i 1)))))
        ;; build list of (position value) pairs
        (define pairs '())
        (for ([i (in-range n)])
          (set! pairs (cons (list (vector-ref lastPos i)
                                  (vector-ref numsV i))
                            pairs)))
        (let ([sorted-pairs (sort pairs (lambda (a b) (< (first a) (first b))))])
          ;; simulate markings in order of increasing last position
          (let loop ((lst sorted-pairs) (cum 0) (cnt 0))
            (if (null? lst)
                #t
                (let* ([pos (first (first lst))]
                       [val (second (first lst))]
                       [need (+ cum val)]
                       [available (- pos cnt)])
                  (if (< available need)
                      #f
                      (loop (rest lst) need (+ cnt 1)))))))))
    ;; binary search for minimal feasible second
    (if (not (feasible? m))
        -1
        (let loop ((lo 1) (hi m) (ans m))
          (if (> lo hi)
              ans
              (let ([mid (quotient (+ lo hi) 2)])
                (if (feasible? mid)
                    (loop lo (- mid 1) mid)
                    (loop (+ mid 1) hi ans))))))))
```

## Erlang

```erlang
-module(solution).
-export([earliest_second_to_mark_indices/2]).

earliest_second_to_mark_indices(Nums, ChangeIndices) ->
    NumsTuple = list_to_tuple(Nums),
    ChangeTuple = list_to_tuple(ChangeIndices),
    N = tuple_size(NumsTuple),
    M = tuple_size(ChangeTuple),

    case feasible(M, N, NumsTuple, ChangeTuple) of
        false -> -1;
        true  -> binary_search(1, M, M, N, NumsTuple, ChangeTuple)
    end.

feasible(T, N, NumsT, ChangeT) ->
    Last = make_last(1, T, erlang:make_tuple(N, 0), ChangeT),
    case has_zero(1, N, Last) of
        true -> false;
        false ->
            Pairs = build_pairs(1, N, Last, NumsT, []),
            Sorted = lists:keysort(1, Pairs),
            check_cum(Sorted, 0)
    end.

make_last(Pos, T, Last, _ChangeT) when Pos > T -> Last;
make_last(Pos, T, Last, ChangeT) ->
    Idx = element(Pos, ChangeT) - 1,
    NewLast = setelement(Idx + 1, Last, Pos),
    make_last(Pos + 1, T, NewLast, ChangeT).

has_zero(I, N, _Last) when I > N -> false;
has_zero(I, N, Last) ->
    case element(I, Last) of
        0 -> true;
        _ -> has_zero(I + 1, N, Last)
    end.

build_pairs(I, N, Last, NumsT, Acc) when I > N -> Acc;
build_pairs(I, N, Last, NumsT, Acc) ->
    D = element(I, Last),
    Work = element(I, NumsT) + 1,
    build_pairs(I + 1, N, Last, NumsT, [{D, Work} | Acc]).

check_cum([], _Cum) -> true;
check_cum([{Deadline, Work} | Rest], Cum) ->
    NewCum = Cum + Work,
    if
        NewCum > Deadline -> false;
        true -> check_cum(Rest, NewCum)
    end.

binary_search(Low, High, Ans, N, NumsT, ChangeT) when Low =< High ->
    Mid = (Low + High) div 2,
    case feasible(Mid, N, NumsT, ChangeT) of
        true -> binary_search(Low, Mid - 1, Mid, N, NumsT, ChangeT);
        false -> binary_search(Mid + 1, High, Ans, N, NumsT, ChangeT)
    end;
binary_search(_, _, Ans, _N, _NumsT, _ChangeT) -> Ans.
```

## Elixir

```elixir
defmodule Solution do
  @spec earliest_second_to_mark_indices(nums :: [integer], change_indices :: [integer]) :: integer
  def earliest_second_to_mark_indices(nums, change_indices) do
    n = length(nums)
    m = length(change_indices)

    binary_search(1, m, nums, change_indices, -1)
  end

  # Binary search for minimal feasible time
  defp binary_search(lo, hi, _nums, _change_indices, ans) when lo > hi do
    ans
  end

  defp binary_search(lo, hi, nums, change_indices, _ans) do
    mid = div(lo + hi, 2)

    if feasible?(mid, nums, change_indices) do
      binary_search(lo, mid - 1, nums, change_indices, mid)
    else
      binary_search(mid + 1, hi, nums, change_indices, -1)
    end
  end

  # Check if all indices can be marked within first t seconds
  defp feasible?(t, nums, change_indices) do
    n = length(nums)

    # Build map of last occurrence for each index within first t seconds
    last_map =
      Enum.reduce(1..t, %{}, fn sec, acc ->
        idx = Enum.at(change_indices, sec - 1)
        Map.put(acc, idx, sec)
      end)

    # Gather (position, required_decrements) pairs; fail if any index missing
    pairs =
      Enum.map(1..n, fn i ->
        pos = Map.get(last_map, i, 0)

        if pos == 0 do
          :missing
        else
          {pos, Enum.at(nums, i - 1)}
        end
      end)

    if :missing in pairs do
      false
    else
      sorted = Enum.sort_by(pairs, fn {pos, _} -> pos end)
      check_order(sorted, 0, 0)
    end
  end

  # Verify cumulative condition cum_need + cnt <= position for each prefix
  defp check_order([], _cum, _cnt), do: true

  defp check_order([{pos, val} | rest], cum, cnt) do
    cum2 = cum + val
    cnt2 = cnt + 1

    if cum2 + cnt2 > pos do
      false
    else
      check_order(rest, cum2, cnt2)
    end
  end
end
```
