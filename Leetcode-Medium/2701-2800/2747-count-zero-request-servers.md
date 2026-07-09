# 2747. Count Zero Request Servers

## Cpp

```cpp
class Solution {
public:
    vector<int> countServers(int n, vector<vector<int>>& logs, int x, vector<int>& queries) {
        struct Log {int time; int sid;};
        vector<Log> sortedLogs;
        sortedLogs.reserve(logs.size());
        for (auto &lg : logs) {
            sortedLogs.push_back({lg[1], lg[0]});
        }
        sort(sortedLogs.begin(), sortedLogs.end(), [](const Log& a, const Log& b){
            return a.time < b.time;
        });
        
        int m = queries.size();
        vector<pair<int,int>> qlist(m);
        for (int i = 0; i < m; ++i) qlist[i] = {queries[i], i};
        sort(qlist.begin(), qlist.end());
        
        vector<int> ans(m);
        vector<int> cnt(n + 1, 0);
        int active = 0;
        size_t l = 0, r = 0;
        for (auto &qt : qlist) {
            int t = qt.first;
            // add logs with time <= t
            while (r < sortedLogs.size() && sortedLogs[r].time <= t) {
                int sid = sortedLogs[r].sid;
                if (++cnt[sid] == 1) ++active;
                ++r;
            }
            // remove logs with time < t - x
            int leftBound = t - x;
            while (l < sortedLogs.size() && sortedLogs[l].time < leftBound) {
                int sid = sortedLogs[l].sid;
                if (--cnt[sid] == 0) --active;
                ++l;
            }
            ans[qt.second] = n - active;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] countServers(int n, int[][] logs, int x, int[] queries) {
        // Sort logs by time
        java.util.Arrays.sort(logs, (a, b) -> Integer.compare(a[1], b[1]));
        int m = logs.length;

        // Prepare and sort queries with original indices
        Query[] qs = new Query[queries.length];
        for (int i = 0; i < queries.length; i++) {
            qs[i] = new Query(queries[i], i);
        }
        java.util.Arrays.sort(qs, (a, b) -> Integer.compare(a.time, b.time));

        int[] cnt = new int[n + 1]; // count of logs per server in current window
        int distinct = 0;           // number of servers with at least one log in window
        int l = 0, r = 0;           // sliding window pointers over logs

        int[] ans = new int[queries.length];

        for (Query q : qs) {
            int curTime = q.time;

            // Expand right side: include logs with time <= curTime
            while (r < m && logs[r][1] <= curTime) {
                int sid = logs[r][0];
                if (cnt[sid] == 0) distinct++;
                cnt[sid]++;
                r++;
            }

            // Shrink left side: exclude logs with time < curTime - x
            int leftBound = curTime - x;
            while (l < m && logs[l][1] < leftBound) {
                int sid = logs[l][0];
                cnt[sid]--;
                if (cnt[sid] == 0) distinct--;
                l++;
            }

            ans[q.idx] = n - distinct; // servers with zero requests in interval
        }
        return ans;
    }

    private static class Query {
        int time, idx;
        Query(int t, int i) { time = t; idx = i; }
    }
}
```

## Python

```python
class Solution(object):
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """
        # Sort logs by time
        logs.sort(key=lambda v: v[1])
        m = len(logs)

        # Pair each query with its original index and sort by query value
        q_idx = sorted([(q, i) for i, q in enumerate(queries)])

        cnt = [0] * (n + 1)          # frequency of each server id inside current window
        active = 0                   # number of servers with at least one request in window
        left = right = 0             # sliding window pointers over logs
        res = [0] * len(queries)

        for q, idx in q_idx:
            # Expand window to include logs with time <= q
            while right < m and logs[right][1] <= q:
                sid = logs[right][0]
                if cnt[sid] == 0:
                    active += 1
                cnt[sid] += 1
                right += 1

            # Shrink window to exclude logs with time < q - x (interval is inclusive)
            low = q - x
            while left < m and logs[left][1] < low:
                sid = logs[left][0]
                cnt[sid] -= 1
                if cnt[sid] == 0:
                    active -= 1
                left += 1

            # Servers with zero requests in the interval
            res[idx] = n - active

        return res
```

## Python3

```python
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by time
        logs.sort(key=lambda v: v[1])
        m = len(logs)
        # Pair queries with original indices and sort
        q_with_idx = sorted([(q, i) for i, q in enumerate(queries)], key=lambda p: p[0])
        ans = [0] * len(queries)

        freq = [0] * (n + 1)   # frequency of each server in current window
        active = 0             # number of servers with at least one request in window
        l = r = 0

        for q, idx in q_with_idx:
            # expand right pointer to include logs with time <= q
            while r < m and logs[r][1] <= q:
                sid = logs[r][0]
                if freq[sid] == 0:
                    active += 1
                freq[sid] += 1
                r += 1

            left_bound = q - x
            # shrink left pointer to exclude logs with time < left_bound
            while l < m and logs[l][1] < left_bound:
                sid = logs[l][0]
                freq[sid] -= 1
                if freq[sid] == 0:
                    active -= 1
                l += 1

            ans[idx] = n - active

        return ans
```

## C

```c
/****
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>
#include <string.h>

typedef struct {
    int server;
    int time;
} Log;

typedef struct {
    int time;
    int idx;
} Query;

/* Comparator for logs by time ascending */
static int cmpLog(const void *a, const void *b) {
    const Log *la = (const Log *)a;
    const Log *lb = (const Log *)b;
    return la->time - lb->time;
}

/* Comparator for queries by time ascending */
static int cmpQuery(const void *a, const void *b) {
    const Query *qa = (const Query *)a;
    const Query *qb = (const Query *)b;
    return qa->time - qb->time;
}

int* countServers(int n, int** logs, int logsSize, int* logsColSize,
                  int x, int* queries, int queriesSize, int* returnSize) {
    /* Prepare sorted logs */
    Log *logArr = (Log *)malloc(sizeof(Log) * logsSize);
    for (int i = 0; i < logsSize; ++i) {
        logArr[i].server = logs[i][0];
        logArr[i].time   = logs[i][1];
    }
    qsort(logArr, logsSize, sizeof(Log), cmpLog);

    /* Prepare sorted queries with original indices */
    Query *qArr = (Query *)malloc(sizeof(Query) * queriesSize);
    for (int i = 0; i < queriesSize; ++i) {
        qArr[i].time = queries[i];
        qArr[i].idx  = i;
    }
    qsort(qArr, queriesSize, sizeof(Query), cmpQuery);

    /* Count per server in current window */
    int *cnt = (int *)calloc(n + 1, sizeof(int));
    int distinct = 0;          // number of servers with at least one request in window
    int left = 0, right = 0;   // sliding window pointers over logArr

    int *ans = (int *)malloc(sizeof(int) * queriesSize);
    for (int i = 0; i < queriesSize; ++i) {
        int curTime = qArr[i].time;
        /* Expand window to include logs with time <= curTime */
        while (right < logsSize && logArr[right].time <= curTime) {
            int sid = logArr[right].server;
            if (++cnt[sid] == 1)
                ++distinct;
            ++right;
        }
        /* Shrink window to exclude logs with time < curTime - x */
        int lowerBound = curTime - x;
        while (left < right && logArr[left].time < lowerBound) {
            int sid = logArr[left].server;
            if (--cnt[sid] == 0)
                --distinct;
            ++left;
        }
        ans[qArr[i].idx] = n - distinct;
    }

    free(logArr);
    free(qArr);
    free(cnt);

    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int[] CountServers(int n, int[][] logs, int x, int[] queries) {
        // Sort logs by time
        Array.Sort(logs, (a, b) => a[1].CompareTo(b[1]));
        
        int m = logs.Length;
        int q = queries.Length;
        
        // Prepare sorted queries with original indices
        var qs = new Query[q];
        for (int i = 0; i < q; i++) {
            qs[i] = new Query { time = queries[i], idx = i };
        }
        Array.Sort(qs, (a, b) => a.time.CompareTo(b.time));
        
        int[] cnt = new int[n + 1];
        int active = 0;
        int left = 0, right = 0;
        int[] ans = new int[q];
        
        foreach (var cur in qs) {
            int t = cur.time;
            // Expand window to include logs with time <= t
            while (right < m && logs[right][1] <= t) {
                int id = logs[right][0];
                if (++cnt[id] == 1) active++;
                right++;
            }
            // Shrink window to exclude logs with time < t - x
            int lower = t - x;
            while (left < m && logs[left][1] < lower) {
                int id = logs[left][0];
                if (--cnt[id] == 0) active--;
                left++;
            }
            ans[cur.idx] = n - active;
        }
        
        return ans;
    }
    
    private struct Query {
        public int time;
        public int idx;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} logs
 * @param {number} x
 * @param {number[]} queries
 * @return {number[]}
 */
var countServers = function(n, logs, x, queries) {
    // Sort logs by time
    logs.sort((a, b) => a[1] - b[1]);

    // Pair each query with its original index and sort by time
    const qObjs = queries.map((t, i) => ({ time: t, idx: i }));
    qObjs.sort((a, b) => a.time - b.time);

    const cnt = new Uint32Array(n + 1); // count of logs in current window per server
    let active = 0;                     // number of servers with at least one log in window
    let left = 0, right = 0;            // sliding window pointers over logs

    const ans = new Array(queries.length);

    for (const { time: qTime, idx } of qObjs) {
        // Expand window to include logs up to qTime (inclusive)
        while (right < logs.length && logs[right][1] <= qTime) {
            const server = logs[right][0];
            if (cnt[server] === 0) active++;
            cnt[server]++;
            right++;
        }

        // Shrink window to exclude logs before (qTime - x)
        const leftBound = qTime - x;
        while (left < logs.length && logs[left][1] < leftBound) {
            const server = logs[left][0];
            cnt[server]--;
            if (cnt[server] === 0) active--;
            left++;
        }

        ans[idx] = n - active; // servers with zero requests in the interval
    }

    return ans;
};
```

## Typescript

```typescript
function countServers(n: number, logs: number[][], x: number, queries: number[]): number[] {
    // Sort logs by time
    logs.sort((a, b) => a[1] - b[1]);

    const m = queries.length;
    const qWithIdx = queries.map((v, i) => ({ val: v, idx: i }));
    qWithIdx.sort((a, b) => a.val - b.val);

    const cnt = new Int32Array(n + 1); // request count per server in current window
    let zeroCount = n; // servers with zero requests in the window

    let l = 0, r = 0;
    const ans: number[] = new Array(m);

    for (const { val: q, idx } of qWithIdx) {
        // Expand right bound to include logs with time <= q
        while (r < logs.length && logs[r][1] <= q) {
            const sid = logs[r][0];
            if (cnt[sid] === 0) zeroCount--;
            cnt[sid]++;
            r++;
        }

        // Shrink left bound to exclude logs with time < q - x
        const leftBound = q - x;
        while (l < logs.length && logs[l][1] < leftBound) {
            const sid = logs[l][0];
            cnt[sid]--;
            if (cnt[sid] === 0) zeroCount++;
            l++;
        }

        ans[idx] = zeroCount;
    }

    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $logs
     * @param Integer $x
     * @param Integer[] $queries
     * @return Integer[]
     */
    function countServers($n, $logs, $x, $queries) {
        // Sort logs by time ascending
        usort($logs, function ($a, $b) {
            if ($a[1] == $b[1]) return 0;
            return ($a[1] < $b[1]) ? -1 : 1;
        });
        $logCount = count($logs);

        // Pair queries with original indices and sort by query time
        $qPairs = [];
        foreach ($queries as $idx => $val) {
            $qPairs[] = [$val, $idx];
        }
        usort($qPairs, function ($a, $b) {
            if ($a[0] == $b[0]) return 0;
            return ($a[0] < $b[0]) ? -1 : 1;
        });

        // Count of requests per server inside current window
        $cnt = array_fill(0, $n + 1, 0);
        $activeServers = 0; // servers with at least one request in the window

        $addIdx = 0;      // pointer to add logs into window
        $removeIdx = 0;   // pointer to remove logs from window

        $answers = array_fill(0, count($queries), 0);

        foreach ($qPairs as $pair) {
            $right = $pair[0];
            $left = $right - $x; // inclusive left bound

            // Add logs with time <= right
            while ($addIdx < $logCount && $logs[$addIdx][1] <= $right) {
                $sid = $logs[$addIdx][0];
                if ($cnt[$sid] == 0) $activeServers++;
                $cnt[$sid]++;
                $addIdx++;
            }

            // Remove logs with time < left
            while ($removeIdx < $logCount && $logs[$removeIdx][1] < $left) {
                $sid = $logs[$removeIdx][0];
                $cnt[$sid]--;
                if ($cnt[$sid] == 0) $activeServers--;
                $removeIdx++;
            }

            // Servers with zero requests in the interval
            $answers[$pair[1]] = $n - $activeServers;
        }

        return $answers;
    }
}
```

## Swift

```swift
class Solution {
    func countServers(_ n: Int, _ logs: [[Int]], _ x: Int, _ queries: [Int]) -> [Int] {
        // Sort logs by time
        let sortedLogs = logs.sorted { $0[1] < $1[1] }
        // Pair each query with its original index and sort by query time
        var queryPairs = [(time: Int, idx: Int)]()
        for (i, q) in queries.enumerated() {
            queryPairs.append((q, i))
        }
        queryPairs.sort { $0.time < $1.time }
        
        var countPerServer = [Int](repeating: 0, count: n + 1)
        var activeServers = 0               // servers with at least one request in current window
        var left = 0                        // index of first log inside the window
        var right = 0                       // index after last log inside the window
        let m = sortedLogs.count
        var result = [Int](repeating: 0, count: queries.count)
        
        for qp in queryPairs {
            let qTime = qp.time
            // Expand window to include logs with time <= qTime
            while right < m && sortedLogs[right][1] <= qTime {
                let serverId = sortedLogs[right][0]
                countPerServer[serverId] += 1
                if countPerServer[serverId] == 1 { activeServers += 1 }
                right += 1
            }
            // Shrink window to exclude logs with time < (qTime - x)
            let lowerBound = qTime - x
            while left < m && sortedLogs[left][1] < lowerBound {
                let serverId = sortedLogs[left][0]
                countPerServer[serverId] -= 1
                if countPerServer[serverId] == 0 { activeServers -= 1 }
                left += 1
            }
            // Servers with zero requests in the interval
            result[qp.idx] = n - activeServers
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countServers(n: Int, logs: Array<IntArray>, x: Int, queries: IntArray): IntArray {
        data class Log(val time: Int, val server: Int)

        val m = logs.size
        val logList = Array(m) { i -> Log(logs[i][1], logs[i][0]) }
        logList.sortBy { it.time }

        val q = queries.size
        val queryPairs = Array(q) { i -> Pair(queries[i], i) }
        queryPairs.sortBy { it.first }

        val cnt = IntArray(n + 1)
        var distinct = 0
        var addPtr = 0
        var removePtr = 0

        val ans = IntArray(q)

        for ((queryTime, idx) in queryPairs) {
            val left = queryTime - x
            while (addPtr < m && logList[addPtr].time <= queryTime) {
                val s = logList[addPtr].server
                if (cnt[s] == 0) distinct++
                cnt[s]++
                addPtr++
            }
            while (removePtr < addPtr && logList[removePtr].time < left) {
                val s = logList[removePtr].server
                cnt[s]--
                if (cnt[s] == 0) distinct--
                removePtr++
            }
            ans[idx] = n - distinct
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> countServers(int n, List<List<int>> logs, int x, List<int> queries) {
    // Sort logs by time
    List<List<int>> sortedLogs = List.from(logs);
    sortedLogs.sort((a, b) => a[1].compareTo(b[1]));

    // Pair each query with its original index and sort by query value
    List<List<int>> qWithIdx = List.generate(
        queries.length, (i) => [queries[i], i],
        growable: false);
    qWithIdx.sort((a, b) => a[0].compareTo(b[0]));

    // Frequency array for servers
    List<int> cnt = List.filled(n + 1, 0);
    int distinct = 0;
    int left = 0, right = 0;
    int m = sortedLogs.length;

    List<int> ans = List.filled(queries.length, 0);

    for (var pair in qWithIdx) {
      int q = pair[0];
      int idx = pair[1];

      // Expand window to include logs with time <= q
      while (right < m && sortedLogs[right][1] <= q) {
        int server = sortedLogs[right][0];
        if (++cnt[server] == 1) distinct++;
        right++;
      }

      // Shrink window to exclude logs with time < q - x
      int lower = q - x;
      while (left < m && sortedLogs[left][1] < lower) {
        int server = sortedLogs[left][0];
        if (--cnt[server] == 0) distinct--;
        left++;
      }

      ans[idx] = n - distinct;
    }

    return ans;
  }
}
```

## Golang

```go
func countServers(n int, logs [][]int, x int, queries []int) []int {
	type Log struct{ server, t int }
	lgs := make([]Log, len(logs))
	for i, v := range logs {
		lgs[i] = Log{v[0], v[1]}
	}
	sort.Slice(lgs, func(i, j int) bool { return lgs[i].t < lgs[j].t })

	type Q struct{ time, idx int }
	qs := make([]Q, len(queries))
	for i, t := range queries {
		qs[i] = Q{t, i}
	}
	sort.Slice(qs, func(i, j int) bool { return qs[i].time < qs[j].time })

	cnt := make([]int, n+1)
	active := 0
	ans := make([]int, len(queries))
	left, right := 0, 0

	for _, q := range qs {
		L := q.time - x
		R := q.time

		for right < len(lgs) && lgs[right].t <= R {
			s := lgs[right].server
			if cnt[s] == 0 {
				active++
			}
			cnt[s]++
			right++
		}
		for left < len(lgs) && lgs[left].t < L {
			s := lgs[left].server
			cnt[s]--
			if cnt[s] == 0 {
				active--
			}
			left++
		}
		ans[q.idx] = n - active
	}
	return ans
}
```

## Ruby

```ruby
def count_servers(n, logs, x, queries)
  # Sort logs by time
  logs.sort_by! { |log| log[1] }

  # Pair each query with its original index and sort by query value
  q_with_idx = queries.each_with_index.map { |q, i| [q, i] }.sort_by { |pair| pair[0] }

  counts = Array.new(n + 1, 0)   # request count per server in current window
  active = 0                     # number of servers with at least one request in window
  res = Array.new(queries.length)

  left = 0
  right = 0
  m = logs.size

  q_with_idx.each do |q, idx|
    lower = q - x

    # Expand window to include logs with time <= q
    while right < m && logs[right][1] <= q
      server = logs[right][0]
      active += 1 if counts[server] == 0
      counts[server] += 1
      right += 1
    end

    # Shrink window to exclude logs with time < lower (outside inclusive interval)
    while left < m && logs[left][1] < lower
      server = logs[left][0]
      counts[server] -= 1
      active -= 1 if counts[server] == 0
      left += 1
    end

    res[idx] = n - active
  end

  res
end
```

## Scala

```scala
object Solution {
    def countServers(n: Int, logs: Array[Array[Int]], x: Int, queries: Array[Int]): Array[Int] = {
        val sortedLogs = logs.sortBy(_(1))
        val qWithIdx = queries.zipWithIndex.sortBy(_._1)
        val cnt = new Array[Int](n + 1)
        var active = 0
        var left = 0
        var right = 0
        val m = sortedLogs.length
        val res = new Array[Int](queries.length)

        for ((q, idx) <- qWithIdx) {
            val start = q - x
            while (left < m && sortedLogs(left)(1) < start) {
                val sid = sortedLogs(left)(0)
                cnt(sid) -= 1
                if (cnt(sid) == 0) active -= 1
                left += 1
            }
            while (right < m && sortedLogs(right)(1) <= q) {
                val sid = sortedLogs(right)(0)
                cnt(sid) += 1
                if (cnt(sid) == 1) active += 1
                right += 1
            }
            res(idx) = n - active
        }

        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_servers(n: i32, logs: Vec<Vec<i32>>, x: i32, queries: Vec<i32>) -> Vec<i32> {
        let n_usize = n as usize;
        // (time, server_id)
        let mut log_vec: Vec<(i32, i32)> = logs
            .into_iter()
            .map(|v| (v[1], v[0]))
            .collect();
        log_vec.sort_by_key(|&(t, _)| t);

        // (query_value, original_index)
        let mut query_pairs: Vec<(i32, usize)> = queries
            .iter()
            .enumerate()
            .map(|(i, &q)| (q, i))
            .collect();
        query_pairs.sort_by_key(|&(q, _)| q);

        let mut freq = vec![0i32; n_usize + 1];
        let mut distinct: i32 = 0;
        let mut ans = vec![0i32; queries.len()];

        let mut left: usize = 0;
        let mut right: usize = 0;

        for &(q, idx) in &query_pairs {
            // add logs with time <= q
            while right < log_vec.len() && log_vec[right].0 <= q {
                let server = log_vec[right].1 as usize;
                if freq[server] == 0 {
                    distinct += 1;
                }
                freq[server] += 1;
                right += 1;
            }

            // remove logs with time < q - x
            let low = q - x;
            while left < log_vec.len() && log_vec[left].0 < low {
                let server = log_vec[left].1 as usize;
                freq[server] -= 1;
                if freq[server] == 0 {
                    distinct -= 1;
                }
                left += 1;
            }

            ans[idx] = n - distinct;
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (count-servers n logs x queries)
  (-> exact-integer?
      (listof (listof exact-integer?))
      exact-integer?
      (listof exact-integer?)
      (listof exact-integer?))
  (let* ((sorted-logs (sort logs (lambda (a b) (< (cadr a) (cadr b)))))
         (m (length sorted-logs))
         (log-vec (list->vector sorted-logs))
         ;; pair each query with its original index
         (q-with-idx
          (let loop ((i 0) (lst queries) (acc '()))
            (if (null? lst)
                (reverse acc)
                (loop (+ i 1) (cdr lst) (cons (list (car lst) i) acc)))))
         (sorted-q (sort q-with-idx (lambda (a b) (< (first a) (first b)))))
         (freq (make-vector (+ n 1) 0))
         (answers (make-vector (length queries) 0))
         (left 0)
         (right 0)
         (distinct 0))
    (for ([q-pair sorted-q])
      (define q (first q-pair))
      (define idx (second q-pair))
      (define start (- q x))
      ;; expand right pointer to include logs with time <= q
      (let loop-right ()
        (when (< right m)
          (define log (vector-ref log-vec right))
          (define time (cadr log))
          (when (<= time q)
            (define server (car log))
            (vector-set! freq server (+ 1 (vector-ref freq server)))
            (when (= (vector-ref freq server) 1)
              (set! distinct (+ distinct 1)))
            (set! right (+ right 1))
            (loop-right)))))
      ;; shrink left pointer to exclude logs with time < start
      (let loop-left ()
        (when (< left right)
          (define log (vector-ref log-vec left))
          (define time (cadr log))
          (when (< time start)
            (define server (car log))
            (vector-set! freq server (- (vector-ref freq server) 1))
            (when (= (vector-ref freq server) 0)
              (set! distinct (- distinct 1)))
            (set! left (+ left 1))
            (loop-left)))))
      ;; answer for this query
      (vector-set! answers idx (- n distinct)))
    (vector->list answers)))
```

## Erlang

```erlang
-spec count_servers(N :: integer(), Logs :: [[integer()]], X :: integer(), Queries :: [integer()]) -> [integer()].
count_servers(N, Logs, X, Queries) ->
    SortedLogs = lists:sort(fun(A, B) -> element(2, A) < element(2, B) end, Logs),
    IdxList = lists:seq(0, length(Queries) - 1),
    QIdx = lists:zip(Queries, IdxList),
    SortedQueries = lists:keysort(1, QIdx),
    {_, _, _, Answers} = process_queries(SortedQueries, SortedLogs, X, N,
                                        queue:new(), #{}, 0, []),
    SortedAns = lists:keysort(1, Answers),
    [Ans || {_Idx, Ans} <- SortedAns].

%% Process all queries recursively
process_queries([], _LogsRest, _X, _N, WindowQ, CountMap, Active, Acc) ->
    {WindowQ, CountMap, Active, Acc};
process_queries([{Q, Idx} | RestQs], LogsRest, X, N, WindowQ, CountMap, Active, Acc) ->
    Start = Q - X,
    {NewLogsRest, NewWindowQ, NewCountMap, NewActive} =
        add_logs(LogsRest, WindowQ, CountMap, Active, Q),
    {FinalWindowQ, FinalCountMap, FinalActive} =
        remove_old(NewWindowQ, Start, NewCountMap, NewActive),
    Answer = N - FinalActive,
    process_queries(RestQs, NewLogsRest, X, N,
                    FinalWindowQ, FinalCountMap, FinalActive,
                    [{Idx, Answer} | Acc]).

%% Add logs with time <= QueryTime into the window
add_logs([], WindowQ, CountMap, Active, _QueryTime) ->
    {[], WindowQ, CountMap, Active};
add_logs([{Server, Time} = Log | Rest], WindowQ, CountMap, Active, QueryTime) when Time =< QueryTime ->
    Prev = maps:get(Server, CountMap, 0),
    NewCount = Prev + 1,
    UpdatedMap = maps:put(Server, NewCount, CountMap),
    UpdatedActive = if Prev == 0 -> Active + 1; true -> Active end,
    add_logs(Rest, queue:in(Log, WindowQ), UpdatedMap, UpdatedActive, QueryTime);
add_logs(LogsRest, WindowQ, CountMap, Active, _QueryTime) ->
    {LogsRest, WindowQ, CountMap, Active}.

%% Remove logs with time < Start from the window
remove_old(WindowQ, Start, CountMap, Active) ->
    case queue:peek(WindowQ) of
        empty ->
            {WindowQ, CountMap, Active};
        {value, {_Server, Time}} when Time < Start ->
            {{value, {Srv, _T}}, Q1} = queue:out(WindowQ),
            Prev = maps:get(Srv, CountMap),
            NewCount = Prev - 1,
            UpdatedMap = if NewCount == 0 -> maps:remove(Srv, CountMap); true -> maps:put(Srv, NewCount, CountMap) end,
            UpdatedActive = if NewCount == 0 -> Active - 1; true -> Active end,
            remove_old(Q1, Start, UpdatedMap, UpdatedActive);
        _ ->
            {WindowQ, CountMap, Active}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_servers(n :: integer, logs :: [[integer]], x :: integer, queries :: [integer]) :: [integer]
  def count_servers(n, logs, x, queries) do
    sorted_logs =
      logs
      |> Enum.sort_by(fn [_sid, t] -> t end)
      |> Enum.map(fn [sid, t] -> {sid, t} end)
      |> List.to_tuple()

    q_with_idx = Enum.with_index(queries)
    sorted_q = Enum.sort_by(q_with_idx, fn {q, _i} -> q end)

    res_map =
      process(
        sorted_logs,
        sorted_q,
        n,
        x,
        0,
        0,
        %{},
        0,
        %{}
      )

    max_idx = length(queries) - 1

    Enum.map(0..max_idx, fn i -> Map.fetch!(res_map, i) end)
  end

  defp process(_logs, [], _n, _x, _l, _r, _freq, _distinct, res), do: res

  defp process(logs, [{q, idx} | rest_q], n, x, l, r, freq, distinct, res) do
    {r2, freq1, distinct1} = expand_right(logs, r, q, freq, distinct)
    bound = q - x
    {l2, freq2, distinct2} = shrink_left(logs, l, bound, freq1, distinct1)

    res2 = Map.put(res, idx, n - distinct2)
    process(logs, rest_q, n, x, l2, r2, freq2, distinct2, res2)
  end

  defp expand_right(logs, r, q, freq, distinct) do
    len = tuple_size(logs)

    if r < len do
      {sid, time} = elem(logs, r)

      if time <= q do
        cnt = Map.get(freq, sid, 0)
        distinct = if cnt == 0, do: distinct + 1, else: distinct
        freq = Map.put(freq, sid, cnt + 1)
        expand_right(logs, r + 1, q, freq, distinct)
      else
        {r, freq, distinct}
      end
    else
      {r, freq, distinct}
    end
  end

  defp shrink_left(logs, l, bound, freq, distinct) do
    len = tuple_size(logs)

    if l < len do
      {sid, time} = elem(logs, l)

      if time < bound do
        cnt = Map.get(freq, sid)

        if cnt == 1 do
          freq = Map.delete(freq, sid)
          distinct = distinct - 1
        else
          freq = Map.put(freq, sid, cnt - 1)
        end

        shrink_left(logs, l + 1, bound, freq, distinct)
      else
        {l, freq, distinct}
      end
    else
      {l, freq, distinct}
    end
  end
end
```
