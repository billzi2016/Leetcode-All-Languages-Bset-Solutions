# 1298. Maximum Candies You Can Get from Boxes

## Cpp

```cpp
class Solution {
public:
    int maxCandies(vector<int>& status, vector<int>& candies, vector<vector<int>>& keys,
                   vector<vector<int>>& containedBoxes, vector<int>& initialBoxes) {
        int n = status.size();
        vector<bool> hasBox(n, false);
        vector<bool> canOpen(n, false);
        vector<bool> opened(n, false);
        queue<int> q;
        
        for (int b : initialBoxes) {
            if (!hasBox[b]) {
                hasBox[b] = true;
                if (status[b] == 1) {
                    canOpen[b] = true;
                    q.push(b);
                }
            } else {
                // already have the box, just ensure it's marked open if possible
                if (status[b] == 1 && !canOpen[b]) {
                    canOpen[b] = true;
                    q.push(b);
                }
            }
        }
        
        long long total = 0; // candies sum fits in int but use long long for safety
        
        while (!q.empty()) {
            int cur = q.front(); q.pop();
            if (opened[cur]) continue;
            opened[cur] = true;
            total += candies[cur];
            
            // acquire keys
            for (int k : keys[cur]) {
                if (!canOpen[k]) {
                    canOpen[k] = true;
                    if (hasBox[k] && !opened[k]) q.push(k);
                }
            }
            // acquire boxes
            for (int nb : containedBoxes[cur]) {
                if (!hasBox[nb]) {
                    hasBox[nb] = true;
                    if (canOpen[nb] && !opened[nb]) q.push(nb);
                } else {
                    // already have the box; if we just got its key earlier, it would have been queued
                }
            }
        }
        
        return (int)total;
    }
};
```

## Java

```java
class Solution {
    public int maxCandies(int[] status, int[] candies, int[][] keys, int[][] containedBoxes, int[] initialBoxes) {
        int n = status.length;
        boolean[] haveBox = new boolean[n];
        boolean[] canOpen = new boolean[n];
        boolean[] opened = new boolean[n];
        java.util.ArrayDeque<Integer> queue = new java.util.ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            if (status[i] == 1) {
                canOpen[i] = true;
            }
        }

        for (int box : initialBoxes) {
            haveBox[box] = true;
            if (canOpen[box]) {
                queue.offer(box);
            }
        }

        int totalCandies = 0;

        while (!queue.isEmpty()) {
            int cur = queue.poll();
            if (opened[cur]) continue;
            opened[cur] = true;
            totalCandies += candies[cur];

            // acquire keys
            for (int key : keys[cur]) {
                if (!canOpen[key]) {
                    canOpen[key] = true;
                    if (haveBox[key] && !opened[key]) {
                        queue.offer(key);
                    }
                }
            }

            // acquire contained boxes
            for (int b : containedBoxes[cur]) {
                if (!haveBox[b]) {
                    haveBox[b] = true;
                    if (canOpen[b] && !opened[b]) {
                        queue.offer(b);
                    }
                }
            }
        }

        return totalCandies;
    }
}
```

## Python

```python
class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        from collections import deque

        n = len(status)
        have_box = [False] * n          # whether we possess the box
        opened = [False] * n            # whether the box has been processed (opened)
        have_key = [False] * n          # whether we own a key for the box

        q = deque()
        # initialize with initial boxes
        for b in initialBoxes:
            if not have_box[b]:
                have_box[b] = True
                if status[b] == 1:
                    q.append(b)

        ans = 0
        while q:
            b = q.popleft()
            if opened[b]:
                continue
            # open the box
            opened[b] = True
            ans += candies[b]

            # acquire keys inside this box
            for k in keys[b]:
                if not have_key[k]:
                    have_key[k] = True
                    if have_box[k] and not opened[k]:
                        q.append(k)

            # acquire contained boxes
            for nb in containedBoxes[b]:
                if not have_box[nb]:
                    have_box[nb] = True
                    if status[nb] == 1 or have_key[nb]:
                        if not opened[nb]:
                            q.append(nb)
                else:
                    # already have the box, maybe we just got its key earlier
                    if have_key[nb] and not opened[nb]:
                        q.append(nb)

        return ans
```

## Python3

```python
class Solution:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        from collections import deque

        n = len(status)
        have = [False] * n          # whether we possess the box
        opened = [False] * n        # whether the box has been queued/processed

        q = deque()
        for b in initialBoxes:
            if not have[b]:
                have[b] = True
                if status[b] == 1 and not opened[b]:
                    q.append(b)
                    opened[b] = True

        total = 0
        while q:
            box = q.popleft()
            total += candies[box]

            # acquire keys
            for k in keys[box]:
                if status[k] == 0:          # we didn't have a key before
                    status[k] = 1
                    if have[k] and not opened[k]:
                        q.append(k)
                        opened[k] = True

            # acquire contained boxes
            for nb in containedBoxes[box]:
                if not have[nb]:
                    have[nb] = True
                    if status[nb] == 1 and not opened[nb]:
                        q.append(nb)
                        opened[nb] = True

        return total
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

int maxCandies(int* status, int statusSize,
               int* candies, int candiesSize,
               int** keys, int keysSize, int* keysColSize,
               int** containedBoxes, int containedBoxesSize, int* containedBoxesColSize,
               int* initialBoxes, int initialBoxesSize) {
    int n = statusSize;
    bool *hasBox = (bool*)calloc(n, sizeof(bool));
    bool *canOpen = (bool*)calloc(n, sizeof(bool));
    bool *opened = (bool*)calloc(n, sizeof(bool));

    for (int i = 0; i < n; ++i) {
        canOpen[i] = (status[i] == 1);
    }

    for (int i = 0; i < initialBoxesSize; ++i) {
        int b = initialBoxes[i];
        hasBox[b] = true;
    }

    long long total = 0;
    bool changed = true;

    while (changed) {
        changed = false;
        for (int i = 0; i < n; ++i) {
            if (!opened[i] && hasBox[i] && canOpen[i]) {
                opened[i] = true;
                total += candies[i];

                int kcnt = keysColSize[i];
                for (int j = 0; j < kcnt; ++j) {
                    int key = keys[i][j];
                    if (!canOpen[key]) {
                        canOpen[key] = true;
                    }
                }

                int bcnt = containedBoxesColSize[i];
                for (int j = 0; j < bcnt; ++j) {
                    int nb = containedBoxes[i][j];
                    if (!hasBox[nb]) {
                        hasBox[nb] = true;
                    }
                }

                changed = true;
            }
        }
    }

    free(hasBox);
    free(canOpen);
    free(opened);
    return (int)total;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxCandies(int[] status, int[] candies, int[][] keys, int[][] containedBoxes, int[] initialBoxes) {
        int n = status.Length;
        bool[] haveBox = new bool[n];
        bool[] canOpen = new bool[n];
        bool[] visited = new bool[n];

        for (int i = 0; i < n; i++) {
            if (status[i] == 1) canOpen[i] = true;
        }

        var queue = new System.Collections.Generic.Queue<int>();

        foreach (int b in initialBoxes) {
            haveBox[b] = true;
            if (canOpen[b]) {
                queue.Enqueue(b);
            }
        }

        int totalCandies = 0;

        while (queue.Count > 0) {
            int cur = queue.Dequeue();
            if (visited[cur]) continue;
            visited[cur] = true;

            totalCandies += candies[cur];

            // acquire keys
            foreach (int k in keys[cur]) {
                if (!canOpen[k]) {
                    canOpen[k] = true;
                    if (haveBox[k] && !visited[k]) {
                        queue.Enqueue(k);
                    }
                }
            }

            // acquire contained boxes
            foreach (int b in containedBoxes[cur]) {
                if (!haveBox[b]) {
                    haveBox[b] = true;
                    if (canOpen[b] && !visited[b]) {
                        queue.Enqueue(b);
                    }
                }
            }
        }

        return totalCandies;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} status
 * @param {number[]} candies
 * @param {number[][]} keys
 * @param {number[][]} containedBoxes
 * @param {number[]} initialBoxes
 * @return {number}
 */
var maxCandies = function(status, candies, keys, containedBoxes, initialBoxes) {
    const n = status.length;
    const have = new Array(n).fill(false);          // we possess the box
    const openable = status.slice();                // 1 if we can open (have key or initially open)
    const processed = new Array(n).fill(false);     // already opened and collected

    for (const b of initialBoxes) {
        have[b] = true;
    }

    const queue = [];
    let head = 0;
    for (let i = 0; i < n; ++i) {
        if (have[i] && openable[i] === 1) {
            queue.push(i);
            processed[i] = true;
        }
    }

    let total = 0;

    while (head < queue.length) {
        const cur = queue[head++];
        total += candies[cur];

        // acquire keys
        for (const k of keys[cur]) {
            if (openable[k] === 0) {
                openable[k] = 1;
                if (have[k] && !processed[k]) {
                    queue.push(k);
                    processed[k] = true;
                }
            }
        }

        // acquire contained boxes
        for (const b of containedBoxes[cur]) {
            if (!have[b]) {
                have[b] = true;
                if (openable[b] === 1 && !processed[b]) {
                    queue.push(b);
                    processed[b] = true;
                }
            } else {
                // already have the box; if we just got its key earlier, it would have been queued
                // no extra action needed here
            }
        }
    }

    return total;
};
```

## Typescript

```typescript
function maxCandies(status: number[], candies: number[], keys: number[][], containedBoxes: number[][], initialBoxes: number[]): number {
    const n = status.length;
    const hasBox = new Array(n).fill(false);
    const canOpen = new Array(n).fill(false);
    const opened = new Array(n).fill(false);
    const queue: number[] = [];
    let head = 0;

    for (const b of initialBoxes) {
        if (!hasBox[b]) hasBox[b] = true;
        if (status[b] === 1) {
            canOpen[b] = true;
            queue.push(b);
        }
    }

    let total = 0;
    while (head < queue.length) {
        const box = queue[head++];
        if (opened[box]) continue;
        opened[box] = true;
        total += candies[box];

        for (const k of keys[box]) {
            if (!canOpen[k]) {
                canOpen[k] = true;
                if (hasBox[k] && !opened[k]) queue.push(k);
            }
        }

        for (const nb of containedBoxes[box]) {
            if (!hasBox[nb]) {
                hasBox[nb] = true;
                if (canOpen[nb] && !opened[nb]) queue.push(nb);
            } else {
                if (canOpen[nb] && !opened[nb]) queue.push(nb);
            }
        }
    }

    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $status
     * @param Integer[] $candies
     * @param Integer[][] $keys
     * @param Integer[][] $containedBoxes
     * @param Integer[] $initialBoxes
     * @return Integer
     */
    function maxCandies($status, $candies, $keys, $containedBoxes, $initialBoxes) {
        $n = count($status);
        $hasBox = array_fill(0, $n, false);   // we possess the box
        $canOpen = array_fill(0, $n, false);  // we can open the box (open status or have key)

        foreach ($initialBoxes as $b) {
            $hasBox[$b] = true;
            if ($status[$b] == 1) {
                $canOpen[$b] = true;
            }
        }

        $queue = new SplQueue();
        for ($i = 0; $i < $n; $i++) {
            if ($hasBox[$i] && $canOpen[$i]) {
                $queue->enqueue($i);
            }
        }

        $total = 0;
        while (!$queue->isEmpty()) {
            $box = $queue->dequeue();
            $total += $candies[$box];

            // obtain keys
            foreach ($keys[$box] as $k) {
                if (!$canOpen[$k]) {
                    $canOpen[$k] = true;
                    if ($hasBox[$k]) {
                        $queue->enqueue($k);
                    }
                }
            }

            // obtain contained boxes
            foreach ($containedBoxes[$box] as $b) {
                if (!$hasBox[$b]) {
                    $hasBox[$b] = true;
                    if ($canOpen[$b]) {
                        $queue->enqueue($b);
                    }
                }
            }
        }

        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func maxCandies(_ status: [Int], _ candies: [Int], _ keys: [[Int]], _ containedBoxes: [[Int]], _ initialBoxes: [Int]) -> Int {
        let n = status.count
        var owned = [Bool](repeating: false, count: n)
        var hasKey = [Bool](repeating: false, count: n)
        var opened = [Bool](repeating: false, count: n)
        
        var queue = [Int]()
        var head = 0
        
        for b in initialBoxes {
            owned[b] = true
            if status[b] == 1 && !opened[b] {
                queue.append(b)
                opened[b] = true
            }
        }
        
        var result = 0
        
        while head < queue.count {
            let cur = queue[head]
            head += 1
            result += candies[cur]
            
            // acquire keys
            for k in keys[cur] {
                if !hasKey[k] {
                    hasKey[k] = true
                    if owned[k] && !opened[k] {
                        queue.append(k)
                        opened[k] = true
                    }
                }
            }
            
            // acquire contained boxes
            for nb in containedBoxes[cur] {
                if !owned[nb] {
                    owned[nb] = true
                    if (hasKey[nb] || status[nb] == 1) && !opened[nb] {
                        queue.append(nb)
                        opened[nb] = true
                    }
                } else {
                    // already owned; opening will be handled when key is obtained
                }
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxCandies(
        status: IntArray,
        candies: IntArray,
        keys: Array<IntArray>,
        containedBoxes: Array<IntArray>,
        initialBoxes: IntArray
    ): Int {
        val n = status.size
        val have = BooleanArray(n)
        val canOpen = BooleanArray(n)
        val visited = BooleanArray(n)
        val queue: ArrayDeque<Int> = ArrayDeque()
        var answer = 0

        // Initialize with initial boxes
        for (box in initialBoxes) {
            if (!have[box]) {
                have[box] = true
                if (status[box] == 1) {
                    canOpen[box] = true
                    queue.add(box)
                }
            }
        }

        while (queue.isNotEmpty()) {
            val box = queue.removeFirst()
            if (visited[box]) continue
            visited[box] = true
            answer += candies[box]

            // Acquire keys
            for (k in keys[box]) {
                if (!canOpen[k]) {
                    canOpen[k] = true
                    if (have[k] && !visited[k]) {
                        queue.add(k)
                    }
                }
            }

            // Acquire contained boxes
            for (nb in containedBoxes[box]) {
                if (!have[nb]) {
                    have[nb] = true
                    if (status[nb] == 1) {
                        canOpen[nb] = true
                        queue.add(nb)
                    } else if (canOpen[nb] && !visited[nb]) {
                        // already openable via a previously obtained key
                        queue.add(nb)
                    }
                } else {
                    // Already have the box; if it just became openable via status, handle here
                    if (status[nb] == 1 && !canOpen[nb]) {
                        canOpen[nb] = true
                        if (!visited[nb]) {
                            queue.add(nb)
                        }
                    }
                }
            }
        }

        return answer
    }
}
```

## Dart

```dart
class Solution {
  int maxCandies(List<int> status, List<int> candies, List<List<int>> keys,
      List<List<int>> containedBoxes, List<int> initialBoxes) {
    int n = status.length;
    List<bool> haveBox = List.filled(n, false);
    List<bool> opened = List.filled(n, false);
    List<bool> visited = List.filled(n, false);

    for (int i = 0; i < n; i++) {
      if (status[i] == 1) opened[i] = true;
    }

    for (int b in initialBoxes) {
      haveBox[b] = true;
    }

    List<int> queue = [];
    for (int i = 0; i < n; i++) {
      if (haveBox[i] && opened[i]) {
        queue.add(i);
        visited[i] = true;
      }
    }

    int ans = 0;
    int idx = 0;
    while (idx < queue.length) {
      int box = queue[idx++];
      ans += candies[box];

      // Acquire keys
      for (int k in keys[box]) {
        if (!opened[k]) {
          opened[k] = true;
          if (haveBox[k] && !visited[k]) {
            queue.add(k);
            visited[k] = true;
          }
        }
      }

      // Acquire contained boxes
      for (int nb in containedBoxes[box]) {
        if (!haveBox[nb]) {
          haveBox[nb] = true;
          if (opened[nb] && !visited[nb]) {
            queue.add(nb);
            visited[nb] = true;
          }
        }
      }
    }

    return ans;
  }
}
```

## Golang

```go
func maxCandies(status []int, candies []int, keys [][]int, containedBoxes [][]int, initialBoxes []int) int {
	n := len(status)
	haveBox := make([]bool, n)
	for _, b := range initialBoxes {
		haveBox[b] = true
	}
	haveKey := make([]bool, n)
	opened := make([]bool, n)

	queue := make([]int, 0)
	for i := 0; i < n; i++ {
		if haveBox[i] && status[i] == 1 {
			queue = append(queue, i)
			opened[i] = true
		}
	}

	total := 0
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]

		total += candies[cur]

		// acquire keys
		for _, k := range keys[cur] {
			if !haveKey[k] {
				haveKey[k] = true
				if haveBox[k] && !opened[k] {
					queue = append(queue, k)
					opened[k] = true
				}
			}
		}

		// acquire boxes
		for _, b := range containedBoxes[cur] {
			if !haveBox[b] {
				haveBox[b] = true
				if (status[b] == 1 || haveKey[b]) && !opened[b] {
					queue = append(queue, b)
					opened[b] = true
				}
			} else {
				// already owned; if we just got its key earlier it would have been queued then
				if haveKey[b] && !opened[b] && (status[b] == 0) {
					queue = append(queue, b)
					opened[b] = true
				}
			}
		}
	}

	return total
}
```

## Ruby

```ruby
def max_candies(status, candies, keys, contained_boxes, initial_boxes)
  n = status.length
  have_box = Array.new(n, false)
  can_open = Array.new(n, false)
  have_key = Array.new(n, false)
  queue = []
  ans = 0

  initial_boxes.each do |b|
    next if have_box[b]
    have_box[b] = true
    if status[b] == 1
      can_open[b] = true
      queue << b
    end
  end

  front = 0
  while front < queue.length
    cur = queue[front]
    front += 1
    ans += candies[cur]

    keys[cur].each do |k|
      next if have_key[k]
      have_key[k] = true
      if have_box[k] && !can_open[k]
        can_open[k] = true
        queue << k
      end
    end

    contained_boxes[cur].each do |b|
      next if have_box[b]
      have_box[b] = true
      if status[b] == 1 || have_key[b]
        unless can_open[b]
          can_open[b] = true
          queue << b
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
    def maxCandies(status: Array[Int], candies: Array[Int], keys: Array[Array[Int]], containedBoxes: Array[Array[Int]], initialBoxes: Array[Int]): Int = {
        val n = status.length
        val have = new Array[Boolean](n)          // we possess the box
        val canOpen = new Array[Boolean](n)       // we can open it (status==1 or have key)
        val processed = new Array[Boolean](n)     // already taken from queue

        val queue = scala.collection.mutable.Queue[Int]()

        // initial boxes
        for (b <- initialBoxes) {
            have(b) = true
            if (status(b) == 1) canOpen(b) = true
        }
        for (b <- initialBoxes) {
            if (have(b) && canOpen(b) && !processed(b)) {
                queue.enqueue(b)
                processed(b) = true
            }
        }

        var total = 0

        while (queue.nonEmpty) {
            val cur = queue.dequeue()
            total += candies(cur)

            // obtain keys
            for (k <- keys(cur)) {
                if (!canOpen(k)) {
                    canOpen(k) = true
                    if (have(k) && !processed(k)) {
                        queue.enqueue(k)
                        processed(k) = true
                    }
                }
            }

            // obtain contained boxes
            for (box <- containedBoxes(cur)) {
                if (!have(box)) {
                    have(box) = true
                    if (status(box) == 1) canOpen(box) = true
                    if (canOpen(box) && !processed(box)) {
                        queue.enqueue(box)
                        processed(box) = true
                    }
                } else {
                    // already have the box; if we just got a key earlier it would have been queued then
                }
            }
        }

        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_candies(
        status: Vec<i32>,
        candies: Vec<i32>,
        keys: Vec<Vec<i32>>,
        contained_boxes: Vec<Vec<i32>>,
        initial_boxes: Vec<i32>,
    ) -> i32 {
        let n = status.len();
        let mut owned = vec![false; n];
        let mut have_key = vec![false; n];
        let mut opened = vec![false; n];
        use std::collections::VecDeque;
        let mut queue: VecDeque<usize> = VecDeque::new();

        // own initial boxes
        for &b in &initial_boxes {
            let idx = b as usize;
            owned[idx] = true;
        }
        // enqueue those that can be opened immediately
        for &b in &initial_boxes {
            let idx = b as usize;
            if status[idx] == 1 && !opened[idx] {
                queue.push_back(idx);
                opened[idx] = true;
            }
        }

        let mut ans: i32 = 0;

        while let Some(cur) = queue.pop_front() {
            ans += candies[cur];

            // obtain keys
            for &k in &keys[cur] {
                let k_idx = k as usize;
                if !have_key[k_idx] {
                    have_key[k_idx] = true;
                    if owned[k_idx] && !opened[k_idx] && (status[k_idx] == 1 || have_key[k_idx]) {
                        queue.push_back(k_idx);
                        opened[k_idx] = true;
                    }
                }
            }

            // obtain contained boxes
            for &b in &contained_boxes[cur] {
                let b_idx = b as usize;
                if !owned[b_idx] {
                    owned[b_idx] = true;
                    if (status[b_idx] == 1 || have_key[b_idx]) && !opened[b_idx] {
                        queue.push_back(b_idx);
                        opened[b_idx] = true;
                    }
                } else {
                    // already owned, maybe now we can open it because we just got it earlier
                    if (status[b_idx] == 1 || have_key[b_idx]) && !opened[b_idx] {
                        queue.push_back(b_idx);
                        opened[b_idx] = true;
                    }
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (max-candies status candies keys containedBoxes initialBoxes)
  (-> (listof exact-integer?) (listof exact-integer?) (listof (listof exact-integer?)) (listof (listof exact-integer?)) (listof exact-integer?) exact-integer?)
  (let* ((n (length status))
         (statusV (list->vector status))
         (candiesV (list->vector candies))
         (keysV (list->vector (map list->vector keys)))
         (boxesV (list->vector (map list->vector containedBoxes)))
         (hasBox (make-vector n #f))
         (canOpen (make-vector n #f))
         (opened (make-vector n #f))
         (queue '())
         (total 0))
    ;; initialize owned boxes and openable status
    (for ([b initialBoxes])
      (vector-set! hasBox b #t)
      (when (= (vector-ref statusV b) 1)
        (vector-set! canOpen b #t)))
    ;; enqueue boxes that are both owned and openable
    (for ([i (in-range n)])
      (when (and (vector-ref hasBox i) (vector-ref canOpen i))
        (set! queue (cons i queue))))
    (let loop ()
      (if (null? queue)
          total
          (begin
            (define b (car queue))
            (set! queue (cdr queue))
            (when (not (vector-ref opened b))
              (vector-set! opened b #t)
              (set! total (+ total (vector-ref candiesV b)))
              ;; use keys found in this box
              (for ([k (in-vector (vector-ref keysV b))])
                (unless (vector-ref canOpen k)
                  (vector-set! canOpen k #t)
                  (when (and (vector-ref hasBox k) (not (vector-ref opened k)))
                    (set! queue (cons k queue)))))
              ;; collect boxes found in this box
              (for ([cb (in-vector (vector-ref boxesV b))])
                (unless (vector-ref hasBox cb)
                  (vector-set! hasBox cb #t)
                  (when (and (vector-ref canOpen cb) (not (vector-ref opened cb)))
                    (set! queue (cons cb queue))))))
            (loop))))))
```

## Erlang

```erlang
max_candies(Status, Candies, Keys, ContainedBoxes, InitialBoxes) ->
    Owned0 = maps:from_list([{B,true} || B <- InitialBoxes]),
    Queue0 = [B || B <- InitialBoxes, lists:nth(B+1, Status) == 1],
    process(Queue0, Owned0, #{}, #{}, 0, Status, Candies, Keys, ContainedBoxes).

process([], _Owned, _KeySet, _Processed, Total, _Status, _Candies, _KeysArr, _BoxesArr) ->
    Total;
process([Box|Rest], Owned, KeySet, Processed, Total,
        Status, Candies, KeysArr, BoxesArr) ->
    case maps:is_key(Box, Processed) of
        true ->
            process(Rest, Owned, KeySet, Processed, Total,
                    Status, Candies, KeysArr, BoxesArr);
        false ->
            Cand = lists:nth(Box+1, Candies),
            NewTotal = Total + Cand,
            BoxList = lists:nth(Box+1, BoxesArr),
            {Owned2, QueueAfterBoxes} =
                add_boxes(BoxList, Rest, Owned, KeySet, Processed, Status),
            KeyList = lists:nth(Box+1, KeysArr),
            {KeySet2, QueueAfterKeys} =
                add_keys(KeyList, QueueAfterBoxes, Owned2, KeySet, Processed),
            Processed2 = maps:put(Box, true, Processed),
            process(QueueAfterKeys, Owned2, KeySet2, Processed2,
                    NewTotal, Status, Candies, KeysArr, BoxesArr)
    end.

add_boxes([], Queue, Owned, _KeySet, _Processed, _Status) ->
    {Owned, Queue};
add_boxes([B|Rest], Queue, Owned, KeySet, Processed, Status) ->
    case maps:is_key(B, Owned) of
        true ->
            add_boxes(Rest, Queue, Owned, KeySet, Processed, Status);
        false ->
            NewOwned = maps:put(B, true, Owned),
            StatusB = lists:nth(B+1, Status),
            CanOpen = (StatusB == 1) orelse maps:is_key(B, KeySet),
            NewQueue = case CanOpen of
                           true -> Queue ++ [B];
                           false -> Queue
                       end,
            add_boxes(Rest, NewQueue, NewOwned, KeySet, Processed, Status)
    end.

add_keys([], Queue, Owned, KeySet, _Processed) ->
    {KeySet, Queue};
add_keys([K|Rest], Queue, Owned, KeySet, Processed) ->
    case maps:is_key(K, KeySet) of
        true ->
            add_keys(Rest, Queue, Owned, KeySet, Processed);
        false ->
            NewKeySet = maps:put(K, true, KeySet),
            NewQueue = case maps:is_key(K, Owned) of
                           true ->
                               case maps:is_key(K, Processed) of
                                   true -> Queue;
                                   false -> Queue ++ [K]
                               end;
                           false -> Queue
                       end,
            add_keys(Rest, NewQueue, Owned, NewKeySet, Processed)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_candies(
          status :: [integer],
          candies :: [integer],
          keys :: [[integer]],
          contained_boxes :: [[integer]],
          initial_boxes :: [integer]
        ) :: integer
  def max_candies(status, candies, keys, contained_boxes, initial_boxes) do
    n = length(status)

    status_t = List.to_tuple(status)
    candies_t = List.to_tuple(candies)
    keys_t = Enum.map(keys, &List.to_tuple/1) |> List.to_tuple()
    boxes_t = Enum.map(contained_boxes, &List.to_tuple/1) |> List.to_tuple()

    owned = MapSet.new(initial_boxes)
    have_key = MapSet.new()
    opened = MapSet.new()

    {queue, opened} =
      Enum.reduce(initial_boxes, {:queue.new(), opened}, fn box, {q, op} ->
        if :erlang.element(box + 1, status_t) == 1 do
          { :queue.in(box, q), MapSet.put(op, box) }
        else
          { q, op }
        end
      end)

    bfs(
      queue,
      owned,
      have_key,
      opened,
      status_t,
      candies_t,
      keys_t,
      boxes_t,
      0
    )
  end

  defp bfs(queue, owned, have_key, opened, status_t, candies_t, keys_t, boxes_t, total) do
    case :queue.out(queue) do
      {:empty, _} ->
        total

      {{:value, box}, q2} ->
        total1 = total + :erlang.element(box + 1, candies_t)

        # Process contained boxes
        {owned1, opened1, q3} =
          Enum.reduce(
            Tuple.to_list(:erlang.element(box + 1, boxes_t)),
            {owned, opened, q2},
            fn new_box, {own, op, qq} ->
              if MapSet.member?(own, new_box) do
                {own, op, qq}
              else
                own = MapSet.put(own, new_box)

                cond do
                  (:erlang.element(new_box + 1, status_t) == 1 or
                     MapSet.member?(have_key, new_box)) and not MapSet.member?(op, new_box) ->
                    {own, MapSet.put(op, new_box), :queue.in(new_box, qq)}

                  true ->
                    {own, op, qq}
                end
              end
            end
          )

        # Process keys
        {have_key2, opened2, q4} =
          Enum.reduce(
            Tuple.to_list(:erlang.element(box + 1, keys_t)),
            {have_key, opened1, q3},
            fn key_box, {hk, op, qq} ->
              if MapSet.member?(hk, key_box) do
                {hk, op, qq}
              else
                hk = MapSet.put(hk, key_box)

                if MapSet.member?(owned1, key_box) and not MapSet.member?(op, key_box) do
                  {hk, MapSet.put(op, key_box), :queue.in(key_box, qq)}
                else
                  {hk, op, qq}
                end
              end
            end
          )

        bfs(q4, owned1, have_key2, opened2, status_t, candies_t, keys_t, boxes_t, total1)
    end
  end
end
```
