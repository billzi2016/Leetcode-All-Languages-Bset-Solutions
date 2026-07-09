# 1687. Delivering Boxes from Storage to Ports

## Cpp

```cpp
class Solution {
public:
    int boxDelivering(vector<vector<int>>& boxes, int portsCount, int maxBoxes, int maxWeight) {
        int n = boxes.size();
        vector<long long> prefW(n + 1, 0);
        vector<int> prefChange(n + 1, 0); // number of port changes up to i
        for (int i = 1; i <= n; ++i) {
            prefW[i] = prefW[i - 1] + boxes[i - 1][1];
            if (i > 1 && boxes[i - 1][0] != boxes[i - 2][0])
                prefChange[i] = prefChange[i - 1] + 1;
            else
                prefChange[i] = prefChange[i - 1];
        }
        vector<int> dp(n + 1, 0);
        deque<int> dq; // store candidate start indices j
        int left = 1; // earliest box index that can be included (1‑based)
        for (int i = 1; i <= n; ++i) {
            while (i - left + 1 > maxBoxes || prefW[i] - prefW[left - 1] > maxWeight)
                ++left;
            int cand = i - 1;
            long long valCand = (long long)dp[cand] - prefChange[cand + 1];
            while (!dq.empty()) {
                int back = dq.back();
                long long valBack = (long long)dp[back] - prefChange[back + 1];
                if (valBack >= valCand)
                    dq.pop_back();
                else
                    break;
            }
            dq.push_back(cand);
            while (!dq.empty() && dq.front() < left - 1)
                dq.pop_front();
            int j = dq.front();
            dp[i] = dp[j] + (prefChange[i] - prefChange[j + 1]) + 2;
        }
        return dp[n];
    }
};
```

## Java

```java
class Solution {
    public int boxDelivering(int[][] boxes, int portsCount, int maxBoxes, int maxWeight) {
        int n = boxes.length;
        int[] dp = new int[n + 1];
        long[] prefW = new long[n + 1];
        int[] preC = new int[n + 1]; // cumulative port changes

        for (int i = 1; i <= n; i++) {
            prefW[i] = prefW[i - 1] + boxes[i - 1][1];
            if (i == 1) {
                preC[i] = 0;
            } else {
                preC[i] = preC[i - 1] + (boxes[i - 1][0] != boxes[i - 2][0] ? 1 : 0);
            }
        }

        int[] val = new int[n + 1]; // dp[l-1] - preC[l]
        java.util.ArrayDeque<Integer> deque = new java.util.ArrayDeque<>();

        int left = 1;
        val[1] = dp[0] - preC[1]; // equals 0
        deque.addLast(1);

        for (int i = 1; i <= n; i++) {
            while (i - left + 1 > maxBoxes || prefW[i] - prefW[left - 1] > maxWeight) {
                if (!deque.isEmpty() && deque.peekFirst() == left) {
                    deque.pollFirst();
                }
                left++;
            }

            dp[i] = preC[i] + 2 + val[deque.peekFirst()];

            if (i + 1 <= n) {
                val[i + 1] = dp[i] - preC[i + 1];
                while (!deque.isEmpty() && val[deque.peekLast()] >= val[i + 1]) {
                    deque.pollLast();
                }
                deque.addLast(i + 1);
            }
        }

        return dp[n];
    }
}
```

## Python

```python
import collections

class Solution(object):
    def boxDelivering(self, boxes, portsCount, maxBoxes, maxWeight):
        """
        :type boxes: List[List[int]]
        :type portsCount: int
        :type maxBoxes: int
        :type maxWeight: int
        :rtype: int
        """
        n = len(boxes)
        # prefix weight
        prefW = [0] * (n + 1)
        for i in range(1, n + 1):
            prefW[i] = prefW[i - 1] + boxes[i - 1][1]
        # prefix port changes
        prefDiff = [0] * (n + 1)
        for i in range(2, n + 1):
            prefDiff[i] = prefDiff[i - 1] + (1 if boxes[i - 1][0] != boxes[i - 2][0] else 0)

        dp = [0] * (n + 1)
        dq = collections.deque()
        # initial candidate j=0
        dq.append(0)

        left = 0
        for i in range(1, n + 1):
            # shrink window to satisfy constraints
            while i - left > maxBoxes or prefW[i] - prefW[left] > maxWeight:
                left += 1
            # remove out‑of‑window candidates
            while dq and dq[0] < left:
                dq.popleft()
            j = dq[0]
            dp[i] = (dp[j] - prefDiff[j + 1]) + prefDiff[i] + 2

            if i == n:
                break
            # value for candidate i
            val = dp[i] - prefDiff[i + 1]
            while dq and (dp[dq[-1]] - prefDiff[dq[-1] + 1]) >= val:
                dq.pop()
            dq.append(i)

        return dp[n]
```

## Python3

```python
class Solution:
    def boxDelivering(self, boxes, portsCount, maxBoxes, maxWeight):
        from collections import deque
        n = len(boxes)
        ports = [0] * (n + 1)
        weight = [0] * (n + 1)
        for i, (p, w) in enumerate(boxes, start=1):
            ports[i] = p
            weight[i] = w

        preChanges = [0] * (n + 1)
        for i in range(2, n + 1):
            preChanges[i] = preChanges[i - 1] + (ports[i] != ports[i - 1])

        dp = [0] * (n + 1)
        dq = deque([0])  # store indices j with increasing dp[j]-preChanges[j]

        left = 1
        curWeight = 0
        curBoxes = 0

        for i in range(1, n + 1):
            curWeight += weight[i]
            curBoxes += 1
            while curBoxes > maxBoxes or curWeight > maxWeight:
                curWeight -= weight[left]
                curBoxes -= 1
                left += 1

            while dq and dq[0] < left - 1:
                dq.popleft()

            best = dp[dq[0]] - preChanges[dq[0]]
            dp[i] = best + preChanges[i] + 2

            val = dp[i] - preChanges[i]
            while dq and (dp[dq[-1]] - preChanges[dq[-1]]) >= val:
                dq.pop()
            dq.append(i)

        return dp[n]
```

## C

```c
#include <stdlib.h>

int boxDelivering(int** boxes, int boxesSize, int* boxesColSize, int portsCount, int maxBoxes, int maxWeight) {
    int n = boxesSize;
    int *port = (int *)malloc((n + 2) * sizeof(int));
    int *weight = (int *)malloc((n + 2) * sizeof(int));
    for (int i = 1; i <= n; ++i) {
        port[i] = boxes[i - 1][0];
        weight[i] = boxes[i - 1][1];
    }

    long long *prefWeight = (long long *)malloc((n + 2) * sizeof(long long));
    int *prefDiff = (int *)malloc((n + 2) * sizeof(int));
    prefWeight[0] = 0;
    prefDiff[0] = 0;
    prefDiff[1] = 0;
    for (int i = 1; i <= n; ++i) {
        prefWeight[i] = prefWeight[i - 1] + weight[i];
        if (i >= 2)
            prefDiff[i] = prefDiff[i - 1] + (port[i] != port[i - 1] ? 1 : 0);
    }
    prefDiff[n + 1] = prefDiff[n]; // sentinel for i=n case

    int *dp = (int *)malloc((n + 2) * sizeof(int));
    dp[0] = 0;

    int *dq = (int *)malloc((n + 5) * sizeof(int));
    int front = 0, back = -1;
    dq[++back] = 0; // initial candidate j=0

    int left = 1;
    for (int i = 1; i <= n; ++i) {
        while (left <= i && ((i - left + 1) > maxBoxes ||
               (prefWeight[i] - prefWeight[left - 1]) > maxWeight)) {
            ++left;
        }
        while (front <= back && dq[front] < left - 1) {
            ++front;
        }

        int bestIdx = dq[front];
        dp[i] = 2 + prefDiff[i] + (dp[bestIdx] - prefDiff[bestIdx + 1]);

        // add current index i as future candidate
        int curVal = dp[i] - prefDiff[i + 1];
        while (front <= back) {
            int idxBack = dq[back];
            int valBack = dp[idxBack] - prefDiff[idxBack + 1];
            if (valBack <= curVal) break;
            --back;
        }
        dq[++back] = i;
    }

    int result = dp[n];

    free(port);
    free(weight);
    free(prefWeight);
    free(prefDiff);
    free(dp);
    free(dq);
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int BoxDelivering(int[][] boxes, int portsCount, int maxBoxes, int maxWeight) {
        int n = boxes.Length;
        int[] port = new int[n + 2];
        int[] w = new int[n + 2];
        for (int i = 1; i <= n; i++) {
            port[i] = boxes[i - 1][0];
            w[i] = boxes[i - 1][1];
        }

        long[] prefWeight = new long[n + 2];
        for (int i = 1; i <= n; i++) {
            prefWeight[i] = prefWeight[i - 1] + w[i];
        }

        int[] changes = new int[n + 2];
        changes[1] = 0;
        for (int i = 2; i <= n; i++) {
            changes[i] = changes[i - 1] + (port[i] != port[i - 1] ? 1 : 0);
        }
        changes[n + 1] = changes[n]; // sentinel

        int[] dp = new int[n + 1];
        dp[0] = 0;

        var dq = new System.Collections.Generic.LinkedList<int>();
        dq.AddLast(0); // initial candidate j=0

        int left = 1;
        for (int i = 1; i <= n; i++) {
            while (i - left + 1 > maxBoxes) left++;
            while (prefWeight[i] - prefWeight[left - 1] > (long)maxWeight) left++;

            // remove out‑of‑range candidates
            while (dq.First != null && dq.First.Value < left - 1) {
                dq.RemoveFirst();
            }

            int bestIdx = dq.First.Value;
            dp[i] = changes[i] + 2 + (dp[bestIdx] - changes[bestIdx + 1]);

            // prepare value for current index i
            int curVal = dp[i] - (i + 1 <= n ? changes[i + 1] : 0);

            while (dq.Last != null) {
                int idx = dq.Last.Value;
                int valIdx = dp[idx] - (idx + 1 <= n ? changes[idx + 1] : 0);
                if (valIdx <= curVal) break;
                dq.RemoveLast();
            }
            dq.AddLast(i);
        }

        return dp[n];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} boxes
 * @param {number} portsCount
 * @param {number} maxBoxes
 * @param {number} maxWeight
 * @return {number}
 */
var boxDelivering = function(boxes, portsCount, maxBoxes, maxWeight) {
    const n = boxes.length;
    const preW = new Array(n + 1).fill(0); // prefix weight
    const preC = new Array(n + 1).fill(0); // prefix port changes

    for (let i = 0; i < n; i++) {
        preW[i + 1] = preW[i] + boxes[i][1];
        if (i > 0) {
            preC[i + 1] = preC[i] + (boxes[i][0] !== boxes[i - 1][0] ? 1 : 0);
        } else {
            preC[i + 1] = 0;
        }
    }

    const dp = new Array(n + 1).fill(0);
    const deque = []; // store candidate start indices
    const getVal = (k) => dp[k] - preC[k + 1];

    deque.push(0); // initial candidate
    let left = 0;

    for (let i = 0; i < n; i++) {
        // shrink window to satisfy constraints
        while (i - left + 1 > maxBoxes || preW[i + 1] - preW[left] > maxWeight) {
            if (deque.length && deque[0] === left) deque.shift();
            left++;
        }

        const best = deque[0];
        dp[i + 1] = dp[best] + (preC[i + 1] - preC[best + 1]) + 2;

        // add current position as future candidate
        if (i + 1 < n) {
            const val = getVal(i + 1);
            while (deque.length && getVal(deque[deque.length - 1]) >= val) {
                deque.pop();
            }
            deque.push(i + 1);
        }
    }

    return dp[n];
};
```

## Typescript

```typescript
function boxDelivering(boxes: number[][], portsCount: number, maxBoxes: number, maxWeight: number): number {
    const n = boxes.length;
    const ports = new Array<number>(n + 1);
    const weight = new Array<number>(n + 1);
    for (let i = 1; i <= n; i++) {
        ports[i] = boxes[i - 1][0];
        weight[i] = boxes[i - 1][1];
    }

    // prefix sum of weights
    const wsum = new Array<number>(n + 1).fill(0);
    for (let i = 1; i <= n; i++) wsum[i] = wsum[i - 1] + weight[i];

    // prefix sum of port changes
    const diffPref = new Array<number>(n + 2).fill(0); // extra slot for i+1 access at i=n
    for (let i = 2; i <= n; i++) {
        diffPref[i] = diffPref[i - 1] + (ports[i] !== ports[i - 1] ? 1 : 0);
    }
    diffPref[n + 1] = diffPref[n];

    const dp = new Array<number>(n + 1).fill(0);

    // monotonic deque storing candidate indices
    const deque: number[] = [];
    let head = 0;
    deque.push(0); // index 0 as initial candidate

    let left = 1; // start of current feasible window (1‑based)
    for (let i = 1; i <= n; i++) {
        // shrink window to satisfy constraints
        while (
            i - left + 1 > maxBoxes ||
            wsum[i] - wsum[left - 1] > maxWeight
        ) {
            left++;
        }

        // discard indices that are out of the feasible range
        while (head < deque.length && deque[head] < left - 1) head++;

        const bestIdx = deque[head];
        dp[i] = diffPref[i] + 2 + (dp[bestIdx] - diffPref[bestIdx + 1]);

        // prepare current index as future candidate
        const curVal = dp[i] - diffPref[i + 1];
        while (deque.length > head) {
            const lastIdx = deque[deque.length - 1];
            const lastVal = dp[lastIdx] - diffPref[lastIdx + 1];
            if (lastVal >= curVal) {
                deque.pop();
            } else break;
        }
        deque.push(i);
    }

    return dp[n];
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $boxes
     * @param Integer $portsCount
     * @param Integer $maxBoxes
     * @param Integer $maxWeight
     * @return Integer
     */
    function boxDelivering($boxes, $portsCount, $maxBoxes, $maxWeight) {
        $n = count($boxes);
        $preWeight = array_fill(0, $n + 1, 0);
        $prePortChanges = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; ++$i) {
            $preWeight[$i] = $preWeight[$i - 1] + $boxes[$i - 1][1];
            $prePortChanges[$i] = $prePortChanges[$i - 1];
            if ($i > 1 && $boxes[$i - 2][0] != $boxes[$i - 1][0]) {
                $prePortChanges[$i] += 1;
            }
        }

        $dp = array_fill(0, $n + 1, PHP_INT_MAX);
        $dp[0] = 0;

        // deque implemented with simple array and head/tail pointers
        $deque = [];
        $head = 0;
        $tail = -1;

        $l = 1; // left bound of current feasible window (1-indexed)

        for ($i = 1; $i <= $n; ++$i) {
            // shrink window from the left until constraints satisfied
            while ($preWeight[$i] - $preWeight[$l - 1] > $maxWeight || $i - $l + 1 > $maxBoxes) {
                $l++;
            }

            // add candidate index (i-1) into deque
            $idx = $i - 1;
            $val = $dp[$idx] - $prePortChanges[$idx + 1];
            while ($head <= $tail) {
                $lastIdx = $deque[$tail];
                $lastVal = $dp[$lastIdx] - $prePortChanges[$lastIdx + 1];
                if ($lastVal >= $val) {
                    $tail--;
                } else {
                    break;
                }
            }
            $deque[++$tail] = $idx;

            // remove indices that are out of the current window
            while ($head <= $tail && $deque[$head] < $l - 1) {
                $head++;
            }

            // compute dp[i]
            $j = $deque[$head];
            $dp[$i] = $dp[$j] + $prePortChanges[$i] - $prePortChanges[$l] + 2;
        }

        return $dp[$n];
    }
}
```

## Swift

```swift
class Solution {
    func boxDelivering(_ boxes: [[Int]], _ portsCount: Int, _ maxBoxes: Int, _ maxWeight: Int) -> Int {
        let n = boxes.count
        var preWeight = Array(repeating: 0, count: n + 1)
        for i in 0..<n {
            preWeight[i + 1] = preWeight[i] + boxes[i][1]
        }
        var changePref = Array(repeating: 0, count: n + 1)
        if n > 1 {
            for i in 1..<n {
                if boxes[i][0] != boxes[i - 1][0] {
                    changePref[i + 1] = changePref[i] + 1
                } else {
                    changePref[i + 1] = changePref[i]
                }
            }
        }
        var dp = Array(repeating: 0, count: n + 1)
        var deque = [Int]()
        var head = 0
        deque.append(0) // start index 0
        var left = 0
        for i in 1...n {
            while i - left > maxBoxes { left += 1 }
            while preWeight[i] - preWeight[left] > maxWeight { left += 1 }
            while head < deque.count && deque[head] < left { head += 1 }
            let j = deque[head]
            let candidate = dp[j] - changePref[j + 1]
            dp[i] = changePref[i] + 2 + candidate
            if i < n {
                let val = dp[i] - changePref[i + 1]
                while head < deque.count && (dp[deque.last!] - changePref[deque.last! + 1]) >= val {
                    deque.removeLast()
                }
                deque.append(i)
            }
        }
        return dp[n]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun boxDelivering(boxes: Array<IntArray>, portsCount: Int, maxBoxes: Int, maxWeight: Int): Int {
        val n = boxes.size
        val change = IntArray(n + 1)
        for (i in 2..n) {
            change[i] = change[i - 1] + if (boxes[i - 1][0] != boxes[i - 2][0]) 1 else 0
        }
        val dp = IntArray(n + 1)
        val deque: java.util.ArrayDeque<Int> = java.util.ArrayDeque()
        var left = 0
        var weightSum = 0L
        for (i in 1..n) {
            weightSum += boxes[i - 1][1].toLong()
            while (i - left > maxBoxes || weightSum > maxWeight) {
                weightSum -= boxes[left][1].toLong()
                left++
            }
            val idx = i - 1
            val curVal = dp[idx] - change[idx]
            while (!deque.isEmpty()) {
                val last = deque.peekLast()
                if (dp[last] - change[last] >= curVal) {
                    deque.pollLast()
                } else break
            }
            deque.addLast(idx)
            while (!deque.isEmpty() && deque.peekFirst() < left) {
                deque.pollFirst()
            }
            val bestIdx = deque.peekFirst()
            dp[i] = dp[bestIdx] - change[bestIdx] + change[i] + 2
        }
        return dp[n]
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int boxDelivering(List<List<int>> boxes, int portsCount, int maxBoxes, int maxWeight) {
    int n = boxes.length;
    List<int> ports = List.filled(n, 0);
    List<int> weight = List.filled(n, 0);
    for (int i = 0; i < n; ++i) {
      ports[i] = boxes[i][0];
      weight[i] = boxes[i][1];
    }

    // trans[i]: number of port changes among first i boxes (i from 0..n)
    List<int> trans = List.filled(n + 1, 0);
    for (int i = 2; i <= n; ++i) {
      trans[i] = trans[i - 1] + (ports[i - 1] != ports[i - 2] ? 1 : 0);
    }

    List<int> dp = List.filled(n + 1, 0);
    Queue<int> dq = Queue<int>();
    dq.addLast(0); // candidate start index 0

    int left = 0;
    int weightSum = 0;

    for (int i = 1; i <= n; ++i) {
      weightSum += weight[i - 1];

      while ((i - left) > maxBoxes || weightSum > maxWeight) {
        weightSum -= weight[left];
        left++;
      }

      while (dq.isNotEmpty && dq.first < left) {
        dq.removeFirst();
      }

      int bestIdx = dq.first;
      dp[i] = dp[bestIdx] - trans[bestIdx + 1] + trans[i] + 2;

      if (i < n) {
        int curVal = dp[i] - trans[i + 1];
        while (dq.isNotEmpty) {
          int lastIdx = dq.last;
          int lastVal = dp[lastIdx] - trans[lastIdx + 1];
          if (lastVal >= curVal) {
            dq.removeLast();
          } else {
            break;
          }
        }
        dq.addLast(i);
      }
    }

    return dp[n];
  }
}
```

## Golang

```go
func boxDelivering(boxes [][]int, portsCount int, maxBoxes int, maxWeight int) int {
    n := len(boxes)
    ports := make([]int, n+1)
    weight := make([]int, n+1)
    for i := 1; i <= n; i++ {
        ports[i] = boxes[i-1][0]
        weight[i] = boxes[i-1][1]
    }

    // changePref[i]: number of port changes from box 1 to i
    changePref := make([]int, n+2) // extra space for safety
    for i := 2; i <= n; i++ {
        if ports[i] != ports[i-1] {
            changePref[i] = changePref[i-1] + 1
        } else {
            changePref[i] = changePref[i-1]
        }
    }

    const INF = int(1e9)
    dp := make([]int, n+1)
    for i := 0; i <= n; i++ {
        dp[i] = INF
    }
    dp[0] = 0

    // deque storing candidate indices j
    deq := make([]int, 0, n+1)
    head := 0
    deq = append(deq, 0) // start with j=0

    left := 1
    curWeight := 0
    curCount := 0

    for i := 1; i <= n; i++ {
        curWeight += weight[i]
        curCount++

        // shrink window to satisfy constraints
        for curWeight > maxWeight || curCount > maxBoxes {
            curWeight -= weight[left]
            curCount--
            left++
        }

        minIdx := left - 1
        for len(deq)-head > 0 && deq[head] < minIdx {
            head++
        }

        bestIdx := deq[head]
        dp[i] = changePref[i] + 2 + dp[bestIdx] - changePref[bestIdx+1]

        // add current index as future candidate (if not the last)
        if i < n {
            val := dp[i] - changePref[i+1]
            for len(deq)-head > 0 {
                idx := deq[len(deq)-1]
                curVal := dp[idx] - changePref[idx+1]
                if curVal >= val {
                    deq = deq[:len(deq)-1]
                } else {
                    break
                }
            }
            deq = append(deq, i)
        }
    }

    return dp[n]
}
```

## Ruby

```ruby
def box_delivering(boxes, ports_count, max_boxes, max_weight)
  n = boxes.length
  ports = Array.new(n + 1)
  weights = Array.new(n + 1)
  (1..n).each do |i|
    ports[i] = boxes[i - 1][0]
    weights[i] = boxes[i - 1][1]
  end

  cnt = Array.new(n + 2, 0) # prefix changes
  (2..n).each do |i|
    cnt[i] = cnt[i - 1] + (ports[i] == ports[i - 1] ? 0 : 1)
  end

  dp = Array.new(n + 1, 0)

  deque = []
  head = 0
  # initial candidate j = 0
  deque << 0

  l = 1
  total_weight = 0
  box_cnt = 0

  (1..n).each do |i|
    total_weight += weights[i]
    box_cnt += 1

    while total_weight > max_weight || box_cnt > max_boxes
      total_weight -= weights[l]
      box_cnt -= 1
      l += 1
    end

    # discard indices out of window
    while head < deque.length && deque[head] < l - 1
      head += 1
    end

    best_idx = deque[head]
    dp[i] = cnt[i] + 2 + (dp[best_idx] - cnt[best_idx + 1])

    # add current index as candidate for future positions
    if i < n
      cur_val = dp[i] - cnt[i + 1]
      while deque.length > head && cur_val <= (dp[deque[-1]] - cnt[deque[-1] + 1])
        deque.pop
      end
      deque << i
    end
  end

  dp[n]
end
```

## Scala

```scala
object Solution {
  def boxDelivering(boxes: Array[Array[Int]], portsCount: Int, maxBoxes: Int, maxWeight: Int): Int = {
    val n = boxes.length
    val port = new Array[Int](n + 1)
    val weight = new Array[Int](n + 1)
    var i = 0
    while (i < n) {
      port(i + 1) = boxes(i)(0)
      weight(i + 1) = boxes(i)(1)
      i += 1
    }

    // diff[i]: number of port changes in first i boxes (1-indexed)
    val diff = new Array[Int](n + 2)
    var idx = 2
    while (idx <= n) {
      diff(idx) = diff(idx - 1) + (if (port(idx) != port(idx - 1)) 1 else 0)
      idx += 1
    }

    val dp = new Array[Int](n + 1)
    dp(0) = 0

    import scala.collection.mutable.ArrayDeque
    val deque = new ArrayDeque[Int]()
    // store indices; value for index j is dp[j] - diff(j+1)
    deque.append(0)

    var left = 1
    var curWeight: Long = 0L
    var curBoxes = 0

    var r = 1
    while (r <= n) {
      curWeight += weight(r).toLong
      curBoxes += 1
      while (curWeight > maxWeight || curBoxes > maxBoxes) {
        curWeight -= weight(left).toLong
        curBoxes -= 1
        left += 1
      }

      // remove indices that are out of the current window
      while (deque.nonEmpty && deque.head < left - 1) {
        deque.removeHead()
      }

      val bestIdx = deque.head
      dp(r) = diff(r) + 2 + (dp(bestIdx) - diff(bestIdx + 1))

      // prepare value for index r to be used later
      val valueR = dp(r) - (if (r + 1 <= n) diff(r + 1) else 0)

      while (deque.nonEmpty && (dp(deque.last) - diff(deque.last + 1)) >= valueR) {
        deque.removeLast()
      }
      deque.append(r)

      r += 1
    }

    dp(n)
  }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn box_delivering(
        boxes: Vec<Vec<i32>>,
        ports_count: i32,
        max_boxes: i32,
        max_weight: i32,
    ) -> i32 {
        let n = boxes.len();
        if n == 0 {
            return 0;
        }
        // prefix of port changes
        let mut change = vec![0i32; n];
        for i in 1..n {
            change[i] = change[i - 1]
                + if boxes[i][0] != boxes[i - 1][0] { 1 } else { 0 };
        }

        let max_boxes_usize = max_boxes as usize;
        let max_weight_i64 = max_weight as i64;

        let mut dp = vec![0i32; n + 1];
        let mut deq: VecDeque<usize> = VecDeque::new();

        let mut l: usize = 0;
        let mut cur_weight: i64 = 0;

        for i in 1..=n {
            // add current box weight
            cur_weight += boxes[i - 1][1] as i64;

            // shrink window to satisfy constraints
            while (i - l) > max_boxes_usize || cur_weight > max_weight_i64 {
                if let Some(&front) = deq.front() {
                    if front == l {
                        deq.pop_front();
                    }
                }
                cur_weight -= boxes[l][1] as i64;
                l += 1;
            }

            // add candidate start index (i-1)
            let idx = i - 1;
            let val = dp[idx] - change[idx];
            while let Some(&back) = deq.back() {
                if dp[back] - change[back] >= val {
                    deq.pop_back();
                } else {
                    break;
                }
            }
            deq.push_back(idx);

            // compute dp[i]
            let best_idx = *deq.front().unwrap();
            dp[i] = (change[i - 1] + 2) + (dp[best_idx] - change[best_idx]);
        }

        dp[n]
    }
}
```

## Racket

```racket
(define/contract (box-delivering boxes portsCount maxBoxes maxWeight)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ((n (length boxes))
         (portV   (make-vector (+ n 2) 0))
         (weightV (make-vector (+ n 2) 0))
         (prefW   (make-vector (+ n 2) 0))
         (prefD   (make-vector (+ n 2) 0))
         (dp      (make-vector (+ n 2) 0)))
    ;; fill port and weight vectors (1‑based)
    (let loop ((i 1) (lst boxes))
      (when (not (null? lst))
        (define p (car (car lst)))
        (define w (cadr (car lst)))
        (vector-set! portV i p)
        (vector-set! weightV i w)
        (loop (+ i 1) (cdr lst))))
    ;; prefix sums for weight and port changes
    (let loop ((i 1))
      (when (<= i n)
        (vector-set! prefW i (+ (vector-ref prefW (- i 1)) (vector-ref weightV i)))
        (if (= i 1)
            (vector-set! prefD i 0)
            (let ((chg (if (= (vector-ref portV i) (vector-ref portV (- i 1))) 0 1)))
              (vector-set! prefD i (+ (vector-ref prefD (- i 1)) chg))))
        (loop (+ i 1))))
    ;; extra entry for prefD[n+1] to avoid bounds checks
    (vector-set! prefD (+ n 1) (vector-ref prefD n))
    ;; deque implementation using vector, front and back indices
    (let ((deq (make-vector (+ n 2) 0))
          (front 0)
          (back -1))
      ;; push initial index 0
      (set! back (+ back 1))
      (vector-set! deq back 0)
      ;; DP iteration
      (let loop-i ((i 1))
        (when (<= i n)
          ;; remove infeasible front indices
          (let rec-remove ()
            (when (and (<= front back)
                       (or (> (- i (vector-ref deq front)) maxBoxes)
                           (> (- (vector-ref prefW i) (vector-ref prefW (vector-ref deq front))) maxWeight)))
              (set! front (+ front 1))
              (rec-remove)))
          ;; compute dp[i] using best front index
          (let* ((j (vector-ref deq front))
                 (val (- (vector-ref dp j) (vector-ref prefD (+ j 1)))))
            (vector-set! dp i (+ val (vector-ref prefD i) 2)))
          ;; prepare value for current i to be inserted into deque
          (let ((curVal (- (vector-ref dp i) (vector-ref prefD (+ i 1)))))
            ;; maintain monotonicity: remove back while not better
            (let rec-pop ()
              (when (and (<= front back)
                         (>= (- (vector-ref dp (vector-ref deq back))
                                (vector-ref prefD (+ (vector-ref deq back) 1)))
                              curVal))
                (set! back (- back 1))
                (rec-pop))))
          ;; push i
          (set! back (+ back 1))
          (vector-set! deq back i)
          ;; next i
          (loop-i (+ i 1)))))
      ;; answer is dp[n]
      (vector-ref dp n)))
```

## Erlang

```erlang
-spec box_delivering(Boxes :: [[integer()]], PortsCount :: integer(), MaxBoxes :: integer(), MaxWeight :: integer()) -> integer().
box_delivering(Boxes, _PortsCount, MaxBoxes, MaxWeight) ->
    {PortsT, WeightsT, PrefDiffT} = build_tuples(Boxes),
    N = tuple_size(PortsT),
    DP0 = array:new(N + 1, [{default, 0}]),
    Q0 = queue:in({0, 0}, queue:new()),
    loop(1, 1, 0, MaxBoxes, MaxWeight, N,
         PortsT, WeightsT, PrefDiffT,
         DP0, Q0).

%% Build tuples: ports, weights, prefDiff (number of port changes up to i)
build_tuples(Boxes) ->
    build_tuples(Boxes, 0, [], [], [], 0).

build_tuples([], _PrevPort, PortsAcc, WeightsAcc, PrefDiffAcc, _CurrDiff) ->
    {list_to_tuple(lists:reverse(PortsAcc)),
     list_to_tuple(lists:reverse(WeightsAcc)),
     list_to_tuple(lists:reverse(PrefDiffAcc))};
build_tuples([{Port, Weight} | Rest], PrevPort,
             PortsAcc, WeightsAcc, PrefDiffAcc, CurrDiff) ->
    Diff = case PrevPort of
               0 -> 0;
               _ -> if Port =/= PrevPort -> CurrDiff + 1; true -> CurrDiff end
           end,
    build_tuples(Rest, Port,
                 [Port | PortsAcc],
                 [Weight | WeightsAcc],
                 [Diff | PrefDiffAcc],
                 Diff).

%% Main DP loop
loop(I, Start, WeightSum, MaxBoxes, MaxWeight, N,
     PortsT, WeightsT, PrefDiffT,
     DP, Queue) when I =< N ->
    Wi = element(I, WeightsT),
    NewWeightSum = WeightSum + Wi,
    {NewStart, AdjWeight} = adjust_start(Start, NewWeightSum, MaxBoxes, MaxWeight, I, WeightsT),
    MinIdx = NewStart - 1,
    Q1 = clean_front(Queue, MinIdx),

    case queue:peek(Q1) of
        {value, {_Idx, BestVal}} ->
            PrefDiffI = element(I, PrefDiffT),
            DPi = PrefDiffI + 2 + BestVal,
            DP1 = array:set(I, DPi, DP),

            if I < N ->
                PrefDiffNext = element(I + 1, PrefDiffT),
                ValI = DPi - PrefDiffNext,
                Q2 = push_monotonic(Q1, {I, ValI}),
                loop(I + 1, NewStart, AdjWeight, MaxBoxes, MaxWeight, N,
                     PortsT, WeightsT, PrefDiffT,
                     DP1, Q2);
               true ->
                DPi
            end;
        _ -> 0
    end;
loop(_I, _Start, _WeightSum, _MaxBoxes, _MaxWeight, N,
     _PortsT, _WeightsT, _PrefDiffT,
     DP, _Queue) ->
    array:get(N, DP).

%% Adjust start index to satisfy constraints
adjust_start(Start, WeightSum, MaxBoxes, MaxWeight, I, WeightsT) ->
    case (I - Start + 1 > MaxBoxes) orelse (WeightSum > MaxWeight) of
        true ->
            WStart = element(Start, WeightsT),
            adjust_start(Start + 1, WeightSum - WStart, MaxBoxes, MaxWeight, I, WeightsT);
        false -> {Start, WeightSum}
    end.

%% Remove indices out of window from front
clean_front(Q, MinIdx) ->
    case queue:peek(Q) of
        {value, {Idx, _}} when Idx < MinIdx ->
            clean_front(queue:drop(Q), MinIdx);
        _ -> Q
    end.

%% Insert while maintaining monotonic increasing values (by Val)
push_monotonic(Q, {Idx, Val}) ->
    case queue:out_r(Q) of
        {{value, {_BIdx, BVal}}, Rest} when BVal >= Val ->
            push_monotonic(Rest, {Idx, Val});
        _ -> queue:in({Idx, Val}, Q)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec box_delivering(boxes :: [[integer]], ports_count :: integer, max_boxes :: integer, max_weight :: integer) :: integer
  def box_delivering(boxes, _ports_count, max_boxes, max_weight) do
    n = length(boxes)

    ports_list = Enum.map(boxes, fn [p, _] -> p end)
    weights_list = Enum.map(boxes, fn [_, w] -> w end)

    ports_arr = :array.from_list([0 | ports_list])
    weights_arr = :array.from_list([0 | weights_list])

    # prefix of port changes
    pref_arr =
      1..n
      |> Enum.reduce(:array.set(0, 0, :array.new(n + 1)), fn i, acc ->
        change =
          if i == 1 do
            0
          else
            if :array.get(i, ports_arr) != :array.get(i - 1, ports_arr), do: 1, else: 0
          end

        val = :array.get(i - 1, acc) + change
        :array.set(i, val, acc)
      end)

    dp_arr = :array.set(0, 0, :array.new(n + 1))

    # deque of {index, value = dp[idx] - pref[idx+1]}, monotonic increasing by value
    init_val = 0 - :array.get(1, pref_arr)
    deque = :queue.in_r({0, init_val}, :queue.new())

    left = 1
    weight_sum = 0

    {dp_arr, _deque, _left, _weight_sum} =
      Enum.reduce(1..n, {dp_arr, deque, left, weight_sum}, fn i,
                                                             {dp_acc, deq, l, wsum} ->
        wsum = wsum + :array.get(i, weights_arr)

        # shrink window to satisfy constraints
        {l, wsum} = shrink_window(l, wsum, max_boxes, max_weight, i, weights_arr)

        # remove candidates whose index < l-1
        deq = clean_front(deq, l - 1)

        # minimal value at front
        min_val =
          case :queue.peek(deq) do
            {:value, {_idx, v}} -> v
          end

        pref_i = :array.get(i, pref_arr)
        dp_i = 2 + pref_i + min_val
        dp_acc = :array.set(i, dp_i, dp_acc)

        # add candidate for j = i (if not last)
        deq =
          if i < n do
            new_val = dp_i - :array.get(i + 1, pref_arr)
            deq = pop_back_while(deq, fn {_idx, v} -> v >= new_val end)
            :queue.in_r({i, new_val}, deq)
          else
            deq
          end

        {dp_acc, deq, l, wsum}
      end)

    :array.get(n, dp_arr)
  end

  defp shrink_window(left, wsum, max_boxes, max_weight, i, weights_arr) do
    cond do
      wsum > max_weight or (i - left + 1) > max_boxes ->
        wsum = wsum - :array.get(left, weights_arr)
        shrink_window(left + 1, wsum, max_boxes, max_weight, i, weights_arr)

      true ->
        {left, wsum}
    end
  end

  defp clean_front(deq, min_idx) do
    case :queue.peek(deq) do
      {:value, {idx, _}} when idx < min_idx ->
        {{:value, _}, deq2} = :queue.out(deq)
        clean_front(deq2, min_idx)

      _ ->
        deq
    end
  end

  defp pop_back_while(deq, cond_fun) do
    case :queue.peek_r(deq) do
      {:value, elem} = peek when cond_fun.(elem) ->
        {{:value, _}, deq2} = :queue.out_r(deq)
        pop_back_while(deq2, cond_fun)

      _ ->
        deq
    end
  end
end
```
