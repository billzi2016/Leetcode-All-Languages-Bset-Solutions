# 2836. Maximize Value of Function in a Ball Passing Game

## Cpp

```cpp
class Solution {
public:
    long long getMaxFunctionValue(vector<int>& receiver, long long k) {
        int n = receiver.size();
        int LOG = 0;
        while ((1LL << LOG) <= k) ++LOG;
        vector<vector<int>> nxt(LOG, vector<int>(n));
        vector<vector<long long>> sum(LOG, vector<long long>(n));
        for (int i = 0; i < n; ++i) {
            nxt[0][i] = receiver[i];
            sum[0][i] = receiver[i];
        }
        for (int j = 1; j < LOG; ++j) {
            for (int i = 0; i < n; ++i) {
                int mid = nxt[j - 1][i];
                nxt[j][i] = nxt[j - 1][mid];
                sum[j][i] = sum[j - 1][i] + sum[j - 1][mid];
            }
        }
        long long ans = 0;
        for (int start = 0; start < n; ++start) {
            long long total = start;
            int cur = start;
            long long rem = k;
            for (int j = 0; j < LOG; ++j) {
                if (rem & (1LL << j)) {
                    total += sum[j][cur];
                    cur = nxt[j][cur];
                }
            }
            ans = max(ans, total);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long getMaxFunctionValue(java.util.List<Integer> receiver, long k) {
        int n = receiver.size();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = receiver.get(i);
        }
        int LOG = 0;
        while (LOG < 60 && (1L << LOG) <= k) {
            LOG++;
        }
        int[][] nxt = new int[LOG][n];
        long[][] sum = new long[LOG][n];
        for (int i = 0; i < n; i++) {
            nxt[0][i] = arr[i];
            sum[0][i] = arr[i];
        }
        for (int p = 1; p < LOG; p++) {
            int[] prevNxt = nxt[p - 1];
            long[] prevSum = sum[p - 1];
            int[] curNxt = nxt[p];
            long[] curSum = sum[p];
            for (int i = 0; i < n; i++) {
                int mid = prevNxt[i];
                curNxt[i] = prevNxt[mid];
                curSum[i] = prevSum[i] + prevSum[mid];
            }
        }
        long ans = Long.MIN_VALUE;
        for (int start = 0; start < n; start++) {
            long curSum = 0;
            int node = start;
            long remaining = k;
            int bit = 0;
            while (remaining > 0) {
                if ((remaining & 1L) == 1L) {
                    curSum += sum[bit][node];
                    node = nxt[bit][node];
                }
                remaining >>= 1;
                bit++;
            }
            long total = start + curSum;
            if (total > ans) ans = total;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def getMaxFunctionValue(self, receiver, k):
        """
        :type receiver: List[int]
        :type k: int
        :rtype: int
        """
        n = len(receiver)
        max_pow = k.bit_length()  # enough bits to represent k
        up = [[0] * max_pow for _ in range(n)]
        sm = [[0] * max_pow for _ in range(n)]

        # j = 0 (2^0 = 1 pass)
        for i in range(n):
            nxt = receiver[i]
            up[i][0] = nxt
            sm[i][0] = nxt

        # build binary lifting tables
        for j in range(1, max_pow):
            uj = j - 1
            for i in range(n):
                mid = up[i][uj]
                up[i][j] = up[mid][uj]
                sm[i][j] = sm[i][uj] + sm[mid][uj]

        ans = 0
        for start in range(n):
            cur = start
            total = start  # include starting player
            bits = k
            j = 0
            while bits:
                if bits & 1:
                    total += sm[cur][j]
                    cur = up[cur][j]
                bits >>= 1
                j += 1
            if total > ans:
                ans = total
        return ans
```

## Python3

```python
class Solution:
    def getMaxFunctionValue(self, receiver, k):
        n = len(receiver)
        LOG = k.bit_length()
        nxt = [[0] * LOG for _ in range(n)]
        sm = [[0] * LOG for _ in range(n)]

        # j = 0
        for i in range(n):
            nxt[i][0] = receiver[i]
            sm[i][0] = receiver[i]

        for j in range(1, LOG):
            for i in range(n):
                mid = nxt[i][j - 1]
                nxt[i][j] = nxt[mid][j - 1]
                sm[i][j] = sm[i][j - 1] + sm[mid][j - 1]

        ans = 0
        for start in range(n):
            total = start
            cur = start
            bits = k
            j = 0
            while bits:
                if bits & 1:
                    total += sm[cur][j]
                    cur = nxt[cur][j]
                bits >>= 1
                j += 1
            if total > ans:
                ans = total
        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

long long getMaxFunctionValue(int* receiver, int receiverSize, long long k) {
    if (receiverSize == 0) return 0;
    int n = receiverSize;

    int maxLog = 0;
    while ((1LL << maxLog) <= k) ++maxLog;   // number of bits needed

    int **up = (int **)malloc(maxLog * sizeof(int *));
    long long **psum = (long long **)malloc(maxLog * sizeof(long long *));
    for (int i = 0; i < maxLog; ++i) {
        up[i] = (int *)malloc(n * sizeof(int));
        psum[i] = (long long *)malloc(n * sizeof(long long));
    }

    // level 0
    for (int v = 0; v < n; ++v) {
        up[0][v] = receiver[v];
        psum[0][v] = receiver[v];
    }

    // higher levels
    for (int lvl = 1; lvl < maxLog; ++lvl) {
        for (int v = 0; v < n; ++v) {
            int mid = up[lvl - 1][v];
            up[lvl][v] = up[lvl - 1][mid];
            psum[lvl][v] = psum[lvl - 1][v] + psum[lvl - 1][mid];
        }
    }

    long long ans = 0;
    for (int start = 0; start < n; ++start) {
        long long total = start;   // include starting player
        int cur = start;
        long long rem = k;
        int bit = 0;
        while (rem) {
            if (rem & 1LL) {
                total += psum[bit][cur];
                cur = up[bit][cur];
            }
            rem >>= 1;
            ++bit;
        }
        if (total > ans) ans = total;
    }

    // free allocated memory
    for (int i = 0; i < maxLog; ++i) {
        free(up[i]);
        free(psum[i]);
    }
    free(up);
    free(psum);

    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long GetMaxFunctionValue(IList<int> receiver, long k) {
        int n = receiver.Count;
        // Determine the number of bits needed for k
        int maxLog = 0;
        while ((1L << maxLog) <= k) maxLog++;
        // Precompute next and sum tables
        int[,] nxt = new int[maxLog, n];
        long[,] sum = new long[maxLog, n];
        for (int i = 0; i < n; i++) {
            nxt[0, i] = receiver[i];
            sum[0, i] = receiver[i];
        }
        for (int j = 1; j < maxLog; j++) {
            for (int i = 0; i < n; i++) {
                int mid = nxt[j - 1, i];
                nxt[j, i] = nxt[j - 1, mid];
                sum[j, i] = sum[j - 1, i] + sum[j - 1, mid];
            }
        }

        long best = 0;
        for (int start = 0; start < n; start++) {
            long total = 0;
            int cur = start;
            long remaining = k;
            int bit = 0;
            while (remaining > 0) {
                if ((remaining & 1L) == 1L) {
                    total += sum[bit, cur];
                    cur = nxt[bit, cur];
                }
                remaining >>= 1;
                bit++;
            }
            long candidate = start + total;
            if (candidate > best) best = candidate;
        }
        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} receiver
 * @param {number} k
 * @return {number}
 */
var getMaxFunctionValue = function(receiver, k) {
    const n = receiver.length;
    const kBig = BigInt(k);
    // determine needed number of levels for binary lifting
    let maxLog = 0;
    while ((1n << BigInt(maxLog)) <= kBig) maxLog++;
    
    const jump = Array.from({length: maxLog}, () => new Uint32Array(n));
    const sum = Array.from({length: maxLog}, () => new Float64Array(n));
    
    // level 0 (2^0 = 1 step)
    for (let i = 0; i < n; i++) {
        jump[0][i] = receiver[i];
        sum[0][i] = receiver[i];
    }
    
    // build higher levels
    for (let p = 1; p < maxLog; p++) {
        const prevJump = jump[p - 1];
        const curJump = jump[p];
        const prevSum = sum[p - 1];
        const curSum = sum[p];
        for (let i = 0; i < n; i++) {
            const mid = prevJump[i];
            curJump[i] = prevJump[mid];
            curSum[i] = prevSum[i] + prevSum[mid];
        }
    }
    
    let answer = 0;
    // evaluate each possible starting player
    for (let start = 0; start < n; start++) {
        let cur = start;
        let total = start; // include the starting player's index
        let remaining = kBig;
        let p = 0;
        while (remaining > 0n) {
            if ((remaining & 1n) === 1n) {
                total += sum[p][cur];
                cur = jump[p][cur];
            }
            remaining >>= 1n;
            p++;
        }
        if (total > answer) answer = total;
    }
    
    return answer;
};
```

## Typescript

```typescript
function getMaxFunctionValue(receiver: number[], k: number): number {
    const n = receiver.length;
    const LOG = Math.ceil(Math.log2(k + 1));
    const nxt: number[][] = Array.from({ length: LOG }, () => new Array<number>(n));
    const sum: number[][] = Array.from({ length: LOG }, () => new Array<number>(n));

    for (let i = 0; i < n; i++) {
        nxt[0][i] = receiver[i];
        sum[0][i] = receiver[i];
    }

    for (let p = 1; p < LOG; p++) {
        const prevNxt = nxt[p - 1];
        const prevSum = sum[p - 1];
        const curNxt = nxt[p];
        const curSum = sum[p];
        for (let i = 0; i < n; i++) {
            const mid = prevNxt[i];
            curNxt[i] = prevNxt[mid];
            curSum[i] = prevSum[i] + prevSum[mid];
        }
    }

    let ans = 0;
    for (let start = 0; start < n; start++) {
        let cur = start;
        let total = start;
        let steps = k;
        let p = 0;
        while (steps > 0) {
            if (steps % 2 === 1) {
                total += sum[p][cur];
                cur = nxt[p][cur];
            }
            steps = Math.floor(steps / 2);
            p++;
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
     * @param Integer[] $receiver
     * @param Integer $k
     * @return Integer
     */
    function getMaxFunctionValue($receiver, $k) {
        $n = count($receiver);
        // determine number of bits needed for k
        $maxLog = 0;
        while ((1 << $maxLog) <= $k) {
            $maxLog++;
        }

        // binary lifting tables: up[log][node], sum[log][node]
        $up = [];
        $sum = [];

        // level 0 (2^0 = 1 step)
        $up[0] = $receiver;
        $sum[0] = $receiver;

        for ($j = 1; $j < $maxLog; $j++) {
            $up[$j] = array_fill(0, $n, 0);
            $sum[$j] = array_fill(0, $n, 0);
            for ($i = 0; $i < $n; $i++) {
                $mid = $up[$j - 1][$i];
                $up[$j][$i] = $up[$j - 1][$mid];
                $sum[$j][$i] = $sum[$j - 1][$i] + $sum[$j - 1][$mid];
            }
        }

        $ans = 0;
        for ($start = 0; $start < $n; $start++) {
            $total = $start;          // include the starting player
            $cur = $start;
            $remaining = $k;
            $bit = 0;
            while ($remaining > 0) {
                if ($remaining & 1) {
                    $total += $sum[$bit][$cur];
                    $cur = $up[$bit][$cur];
                }
                $remaining >>= 1;
                $bit++;
            }
            if ($total > $ans) {
                $ans = $total;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func getMaxFunctionValue(_ receiver: [Int], _ k: Int) -> Int {
        let n = receiver.count
        var maxLog = 0
        var pow: Int64 = 1
        while pow <= Int64(k) {
            maxLog += 1
            pow <<= 1
        }
        var nxt = Array(repeating: Array(repeating: 0, count: maxLog), count: n)
        var sums = Array(repeating: Array(repeating: Int64(0), count: maxLog), count: n)
        for i in 0..<n {
            nxt[i][0] = receiver[i]
            sums[i][0] = Int64(receiver[i])
        }
        if maxLog > 1 {
            for j in 1..<maxLog {
                for i in 0..<n {
                    let mid = nxt[i][j - 1]
                    nxt[i][j] = nxt[mid][j - 1]
                    sums[i][j] = sums[i][j - 1] + sums[mid][j - 1]
                }
            }
        }
        var answer: Int64 = 0
        for start in 0..<n {
            var cur = start
            var total: Int64 = Int64(start)
            var remaining = k
            var bit = 0
            while remaining > 0 {
                if (remaining & 1) == 1 {
                    total += sums[cur][bit]
                    cur = nxt[cur][bit]
                }
                remaining >>= 1
                bit += 1
            }
            if total > answer { answer = total }
        }
        return Int(answer)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getMaxFunctionValue(receiver: List<Int>, k: Long): Long {
        val n = receiver.size
        var LOG = 0
        var tempK = k
        while (tempK > 0) {
            LOG++
            tempK = tempK shr 1
        }
        if (LOG == 0) LOG = 1

        val nxt = Array(LOG) { IntArray(n) }
        val sum = Array(LOG) { LongArray(n) }

        for (i in 0 until n) {
            nxt[0][i] = receiver[i]
            sum[0][i] = receiver[i].toLong()
        }

        for (j in 1 until LOG) {
            for (i in 0 until n) {
                val mid = nxt[j - 1][i]
                nxt[j][i] = nxt[j - 1][mid]
                sum[j][i] = sum[j - 1][i] + sum[j - 1][mid]
            }
        }

        var ans = Long.MIN_VALUE
        for (start in 0 until n) {
            var cur = start
            var total = start.toLong()
            var remaining = k
            var bit = 0
            while (remaining > 0) {
                if ((remaining and 1L) == 1L) {
                    total += sum[bit][cur]
                    cur = nxt[bit][cur]
                }
                remaining = remaining shr 1
                bit++
            }
            if (total > ans) ans = total
        }

        return ans
    }
}
```

## Dart

```dart
class Solution {
  int getMaxFunctionValue(List<int> receiver, int k) {
    int n = receiver.length;
    int LOG = 0;
    while ((1 << LOG) <= k) LOG++;

    List<List<int>> up = List.generate(LOG, (_) => List.filled(n, 0));
    List<List<int>> sum = List.generate(LOG, (_) => List.filled(n, 0));

    for (int i = 0; i < n; ++i) {
      up[0][i] = receiver[i];
      sum[0][i] = receiver[i];
    }

    for (int j = 1; j < LOG; ++j) {
      for (int i = 0; i < n; ++i) {
        int mid = up[j - 1][i];
        up[j][i] = up[j - 1][mid];
        sum[j][i] = sum[j - 1][i] + sum[j - 1][mid];
      }
    }

    int ans = 0;
    for (int start = 0; start < n; ++start) {
      int cur = start;
      int total = start;
      int remaining = k;
      int bit = 0;
      while (remaining > 0) {
        if ((remaining & 1) == 1) {
          total += sum[bit][cur];
          cur = up[bit][cur];
        }
        remaining >>= 1;
        bit++;
      }
      if (total > ans) ans = total;
    }

    return ans;
  }
}
```

## Golang

```go
func getMaxFunctionValue(receiver []int, k int64) int64 {
    n := len(receiver)
    // Determine number of levels needed for binary lifting
    LOG := 0
    for (int64(1) << LOG) <= k {
        LOG++
    }
    // nxt[level][node] = node after 2^level steps
    // sumVals[level][node] = sum of visited nodes during those steps (excluding the starting node)
    nxt := make([][]int, LOG)
    sumVals := make([][]int64, LOG)
    for i := 0; i < LOG; i++ {
        nxt[i] = make([]int, n)
        sumVals[i] = make([]int64, n)
    }
    // level 0 (1 step)
    for v := 0; v < n; v++ {
        nxt[0][v] = receiver[v]
        sumVals[0][v] = int64(receiver[v])
    }
    // build higher levels
    for lvl := 1; lvl < LOG; lvl++ {
        for v := 0; v < n; v++ {
            mid := nxt[lvl-1][v]
            nxt[lvl][v] = nxt[lvl-1][mid]
            sumVals[lvl][v] = sumVals[lvl-1][v] + sumVals[lvl-1][mid]
        }
    }

    var ans int64
    for start := 0; start < n; start++ {
        cur := start
        total := int64(start)
        remaining := k
        lvl := 0
        for remaining > 0 {
            if (remaining & 1) == 1 {
                total += sumVals[lvl][cur]
                cur = nxt[lvl][cur]
            }
            remaining >>= 1
            lvl++
        }
        if total > ans {
            ans = total
        }
    }
    return ans
}
```

## Ruby

```ruby
def get_max_function_value(receiver, k)
  n = receiver.length
  # Determine number of bits needed for k
  max_pow = 0
  while (1 << max_pow) <= k
    max_pow += 1
  end

  jump = Array.new(max_pow) { Array.new(n) }
  sum = Array.new(max_pow) { Array.new(n) }

  # level 0 (2^0 = 1 step)
  n.times do |i|
    jump[0][i] = receiver[i]
    sum[0][i] = receiver[i]
  end

  # build binary lifting tables
  (1...max_pow).each do |p|
    n.times do |i|
      prev = jump[p - 1][i]
      jump[p][i] = jump[p - 1][prev]
      sum[p][i] = sum[p - 1][i] + sum[p - 1][prev]
    end
  end

  max_score = 0

  n.times do |start|
    cur = start
    total = start
    remaining = k
    bit = 0
    while remaining > 0
      if (remaining & 1) == 1
        total += sum[bit][cur]
        cur = jump[bit][cur]
      end
      remaining >>= 1
      bit += 1
    end
    max_score = total if total > max_score
  end

  max_score
end
```

## Scala

```scala
object Solution {
  def getMaxFunctionValue(receiver: List[Int], k: Long): Long = {
    val n = receiver.length
    // Determine number of bits needed for k
    var maxLog = 0
    var tempK = k
    while (tempK > 0) {
      maxLog += 1
      tempK >>= 1
    }
    if (maxLog == 0) maxLog = 1

    val nxt = Array.ofDim[Int](maxLog, n)
    val sum = Array.ofDim[Long](maxLog, n)

    // j = 0 (2^0 = 1 step)
    for (i <- 0 until n) {
      nxt(0)(i) = receiver(i)
      sum(0)(i) = receiver(i).toLong
    }

    // Build binary lifting tables
    var j = 1
    while (j < maxLog) {
      var i = 0
      while (i < n) {
        val mid = nxt(j - 1)(i)
        nxt(j)(i) = nxt(j - 1)(mid)
        sum(j)(i) = sum(j - 1)(i) + sum(j - 1)(mid)
        i += 1
      }
      j += 1
    }

    var answer: Long = Long.MinValue

    // Evaluate each starting player
    for (start <- 0 until n) {
      var cur = start
      var total: Long = 0L
      var bitsIdx = 0
      var remaining = k
      while (remaining > 0) {
        if ((remaining & 1L) == 1L) {
          total += sum(bitsIdx)(cur)
          cur = nxt(bitsIdx)(cur)
        }
        remaining >>= 1
        bitsIdx += 1
      }
      val score = start.toLong + total
      if (score > answer) answer = score
    }

    answer
  }
}
```

## Rust

```rust
impl Solution {
    pub fn get_max_function_value(receiver: Vec<i32>, k: i64) -> i64 {
        let n = receiver.len();
        // Determine needed number of levels for binary lifting
        let mut log = 0usize;
        while (1i64 << log) <= k {
            log += 1;
        }
        // up[x][j] = node reached from x after 2^j steps
        // sum[x][j] = sum of node indices visited during those 2^j steps
        let mut up: Vec<Vec<usize>> = vec![vec![0; log]; n];
        let mut sum: Vec<Vec<i64>> = vec![vec![0; log]; n];

        for i in 0..n {
            let nxt = receiver[i] as usize;
            up[i][0] = nxt;
            sum[i][0] = nxt as i64;
        }

        for j in 1..log {
            for i in 0..n {
                let mid = up[i][j - 1];
                up[i][j] = up[mid][j - 1];
                sum[i][j] = sum[i][j - 1] + sum[mid][j - 1];
            }
        }

        let mut answer: i64 = 0;
        for start in 0..n {
            let mut cur = start;
            let mut total = start as i64; // include starting player
            let mut remaining = k;
            let mut bit = 0usize;
            while remaining > 0 {
                if (remaining & 1) == 1 {
                    total += sum[cur][bit];
                    cur = up[cur][bit];
                }
                remaining >>= 1;
                bit += 1;
            }
            if total > answer {
                answer = total;
            }
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (get-max-function-value receiver k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length receiver))
         (vec-receiver (list->vector receiver))
         (LOG (max 1 (integer-length k))) ; at least one level
         (next (make-vector LOG))
         (sumv (make-vector LOG)))
    ;; level 0 initialization
    (let ((lvl-next (make-vector n))
          (lvl-sum (make-vector n)))
      (for ([i (in-range n)])
        (define nxt (vector-ref vec-receiver i))
        (vector-set! lvl-next i nxt)
        (vector-set! lvl-sum i nxt))
      (vector-set! next 0 lvl-next)
      (vector-set! sumv 0 lvl-sum))
    ;; build higher levels
    (for ([lvl (in-range 1 LOG)])
      (define prev-next (vector-ref next (- lvl 1)))
      (define prev-sum (vector-ref sumv (- lvl 1)))
      (define cur-next (make-vector n))
      (define cur-sum (make-vector n))
      (for ([i (in-range n)])
        (define mid (vector-ref prev-next i))
        (vector-set! cur-next i (vector-ref prev-next mid))
        (vector-set! cur-sum i (+ (vector-ref prev-sum i)
                                 (vector-ref prev-sum mid))))
      (vector-set! next lvl cur-next)
      (vector-set! sumv lvl cur-sum))
    ;; compute maximum score
    (define max-score -1)
    (for ([i (in-range n)])
      (define total i)          ; include starting player
      (define cur i)
      (define remaining k)
      (define bit 0)
      (let loop ()
        (when (> remaining 0)
          (when (odd? remaining)
            (set! total (+ total (vector-ref (vector-ref sumv bit) cur)))
            (set! cur   (vector-ref (vector-ref next bit) cur)))
          (set! remaining (arithmetic-shift remaining -1))
          (set! bit (+ bit 1))
          (loop)))
      (when (> total max-score)
        (set! max-score total)))
    max-score))
```

## Erlang

```erlang
-spec get_max_function_value(Receiver :: [integer()], K :: integer()) -> integer().
get_max_function_value(Receiver, K) ->
    N = length(Receiver),
    RecArr = array:from_list(Receiver),
    Log = trunc(math:log(K) / math:log(2)) + 1,
    {NextList, SumList} = build_tables(RecArr, N, Log),
    NextTuple = list_to_tuple(NextList),
    SumTuple = list_to_tuple(SumList),
    compute_max(N, K, NextTuple, SumTuple).

%% Build binary lifting tables up to LOG levels.
build_tables(RecArr, N, Log) ->
    build_tables(0, Log, RecArr, RecArr, [], []).

build_tables(Level, Log, PrevNext, PrevSum, AccNext, AccSum) when Level < Log ->
    NewAccNext = [PrevNext | AccNext],
    NewAccSum  = [PrevSum  | AccSum],
    case Level + 1 of
        Log -> {lists:reverse(NewAccNext), lists:reverse(NewAccSum)};
        _   ->
            {CurrNext, CurrSum} = build_level(PrevNext, PrevSum, N),
            build_tables(Level + 1, Log, CurrNext, CurrSum, NewAccNext, NewAccSum)
    end.

%% Compute next and sum arrays for one higher power of two.
build_level(PrevNext, PrevSum, N) ->
    build_level(0, N, PrevNext, PrevSum,
                array:new(N, [{default, 0}]),
                array:new(N, [{default, 0}])).

build_level(I, N, PrevNext, PrevSum, AccNext, AccSum) when I < N ->
    Mid = array:get(PrevNext, I),
    NextNode = array:get(PrevNext, Mid),
    SumVal   = array:get(PrevSum, I) + array:get(PrevSum, Mid),
    NewAccNext = array:set(I, NextNode, AccNext),
    NewAccSum  = array:set(I, SumVal,   AccSum),
    build_level(I + 1, N, PrevNext, PrevSum, NewAccNext, NewAccSum);
build_level(_, _, _, _, AccNext, AccSum) ->
    {AccNext, AccSum}.

%% Compute the maximum score over all starting players.
compute_max(N, K, NextTuple, SumTuple) ->
    compute_max(0, N - 1, K, NextTuple, SumTuple, -1).

compute_max(I, MaxIdx, _K, _NextTuple, _SumTuple, MaxScore) when I > MaxIdx ->
    MaxScore;
compute_max(I, MaxIdx, K, NextTuple, SumTuple, MaxScore) ->
    Total0 = I,
    Cur0   = I,
    {Total, _} = compute_score(K, 0, Cur0, Total0, NextTuple, SumTuple),
    NewMax = if Total > MaxScore -> Total; true -> MaxScore end,
    compute_max(I + 1, MaxIdx, K, NextTuple, SumTuple, NewMax).

%% Apply binary lifting according to bits of K.
compute_score(0, _BitIdx, Cur, Total, _NextTuple, _SumTuple) ->
    {Total, Cur};
compute_score(K, BitIdx, Cur, Total, NextTuple, SumTuple) ->
    case (K band 1) of
        1 ->
            SumArr = element(BitIdx + 1, SumTuple),
            NextArr = element(BitIdx + 1, NextTuple),
            Add   = array:get(SumArr, Cur),
            NewCur = array:get(NextArr, Cur),
            compute_score(K bsr 1, BitIdx + 1, NewCur, Total + Add, NextTuple, SumTuple);
        0 ->
            compute_score(K bsr 1, BitIdx + 1, Cur, Total, NextTuple, SumTuple)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_max_function_value(receiver :: [integer], k :: integer) :: integer
  def get_max_function_value(receiver, k) do
    n = length(receiver)

    max_log =
      if k == 0 do
        0
      else
        :math.log2(k) |> trunc() |> Kernel.+(1)
      end

    # level 0 arrays
    arr0 = :array.from_list(receiver)

    {next_levels, sum_levels} =
      build_levels(arr0, arr0, max_log, 1, [arr0], [arr0])

    require Bitwise

    Enum.reduce(0..n - 1, 0, fn start, best ->
      total = walk(start, start, k, 0, next_levels, sum_levels)
      if total > best, do: total, else: best
    end)
  end

  defp build_levels(_prev_next, _prev_sum, max_log, i, next_acc, sum_acc) when i == max_log do
    {Enum.reverse(next_acc), Enum.reverse(sum_acc)}
  end

  defp build_levels(prev_next, prev_sum, max_log, i, next_acc, sum_acc) do
    n = :array.size(prev_next)

    new_next_list =
      for idx <- 0..n - 1 do
        mid = :array.get(idx, prev_next)
        :array.get(mid, prev_next)
      end

    new_sum_list =
      for idx <- 0..n - 1 do
        mid = :array.get(idx, prev_next)
        :array.get(idx, prev_sum) + :array.get(mid, prev_sum)
      end

    new_next_arr = :array.from_list(new_next_list)
    new_sum_arr = :array.from_list(new_sum_list)

    build_levels(
      new_next_arr,
      new_sum_arr,
      max_log,
      i + 1,
      [new_next_arr | next_acc],
      [new_sum_arr | sum_acc]
    )
  end

  defp walk(total, _cur, 0, _bit, _next_levels, _sum_levels), do: total

  defp walk(total, cur, rem_k, bit, next_levels, sum_levels) do
    require Bitwise

    if (rem_k &&& 1) == 1 do
      sum_arr = Enum.at(sum_levels, bit)
      next_arr = Enum.at(next_levels, bit)

      total2 = total + :array.get(cur, sum_arr)
      cur2 = :array.get(cur, next_arr)

      walk(total2, cur2, Bitwise.bsr(rem_k, 1), bit + 1, next_levels, sum_levels)
    else
      walk(total, cur, Bitwise.bsr(rem_k, 1), bit + 1, next_levels, sum_levels)
    end
  end
end
```
