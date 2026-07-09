# 0936. Stamping The Sequence

## Cpp

```cpp
class Solution {
public:
    vector<int> movesToStamp(string stamp, string target) {
        int m = stamp.size(), n = target.size();
        vector<vector<int>> made(n - m + 1);
        vector<int> todoCount(n - m + 1, 0);
        vector<vector<int>> posWindows(n);
        for (int i = 0; i <= n - m; ++i) {
            for (int j = 0; j < m; ++j) {
                int pos = i + j;
                if (target[pos] == stamp[j]) {
                    made[i].push_back(pos);
                } else {
                    ++todoCount[i];
                }
                posWindows[pos].push_back(i);
            }
        }

        vector<int> ans;
        queue<int> q;
        vector<bool> visitedPos(n, false);

        // windows that are already matching
        for (int i = 0; i <= n - m; ++i) {
            if (todoCount[i] == 0) {
                ans.push_back(i);
                for (int p : made[i]) {
                    if (!visitedPos[p]) {
                        visitedPos[p] = true;
                        q.push(p);
                    }
                }
                // mark as processed to avoid re‑processing
                todoCount[i] = -1;
            }
        }

        while (!q.empty()) {
            int pos = q.front(); q.pop();
            for (int w : posWindows[pos]) {
                if (todoCount[w] <= 0) continue; // already done or impossible
                --todoCount[w];
                if (todoCount[w] == 0) {
                    ans.push_back(w);
                    for (int p : made[w]) {
                        if (!visitedPos[p]) {
                            visitedPos[p] = true;
                            q.push(p);
                        }
                    }
                    // mark as processed
                    todoCount[w] = -1;
                }
            }
        }

        // check if all positions are turned to '?'
        for (bool v : visitedPos) {
            if (!v) return {};
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] movesToStamp(String stamp, String target) {
        int m = stamp.length();
        int n = target.length();
        int[] todo = new int[n - m + 1];
        @SuppressWarnings("unchecked")
        ArrayList<Integer>[] pos = new ArrayList[n];
        for (int i = 0; i < n; i++) pos[i] = new ArrayList<>();
        boolean[] visited = new boolean[n];
        Queue<Integer> queue = new LinkedList<>();
        List<Integer> ans = new ArrayList<>();

        // Initialize windows
        for (int start = 0; start <= n - m; start++) {
            int mismatches = 0;
            for (int j = 0; j < m; j++) {
                if (target.charAt(start + j) != stamp.charAt(j)) {
                    mismatches++;
                    pos[start + j].add(start);
                }
            }
            todo[start] = mismatches;
            if (mismatches == 0) {
                ans.add(start);
                for (int j = 0; j < m; j++) {
                    int idx = start + j;
                    if (!visited[idx]) {
                        visited[idx] = true;
                        queue.offer(idx);
                    }
                }
            }
        }

        // Process queue
        while (!queue.isEmpty()) {
            int idx = queue.poll();
            for (int w : pos[idx]) {
                if (todo[w] == 0) continue;
                todo[w]--;
                if (todo[w] == 0) {
                    ans.add(w);
                    for (int j = 0; j < m; j++) {
                        int i = w + j;
                        if (!visited[i]) {
                            visited[i] = true;
                            queue.offer(i);
                        }
                    }
                }
            }
        }

        // Verify all positions are covered
        for (boolean b : visited) {
            if (!b) return new int[0];
        }

        // Reverse answer to get correct order
        int[] res = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) {
            res[i] = ans.get(ans.size() - 1 - i);
        }
        return res;
    }
}
```

## Python

```python
import collections

class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        m, n = len(stamp), len(target)
        todo = []
        for i in range(n - m + 1):
            diff = set()
            for j in range(m):
                if target[i + j] != stamp[j]:
                    diff.add(i + j)
            todo.append(diff)

        queue = collections.deque()
        done = [False] * n
        visited_window = [False] * (n - m + 1)
        ans = []

        for i in range(n - m + 1):
            if not todo[i]:
                queue.append(i)
                visited_window[i] = True

        while queue:
            i = queue.popleft()
            ans.append(i)
            # turn the whole window into '?'
            for j in range(i, i + m):
                if done[j]:
                    continue
                done[j] = True
                start = max(0, j - m + 1)
                end = min(j, n - m)
                for w in range(start, end + 1):
                    if j in todo[w]:
                        todo[w].remove(j)
                        if not visited_window[w] and not todo[w]:
                            queue.append(w)
                            visited_window[w] = True

        if not all(done):
            return []
        ans.reverse()
        return ans
```

## Python3

```python
import collections
from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        windows = []
        for i in range(n - m + 1):
            made = []
            todo = set()
            for k in range(m):
                if target[i + k] == stamp[k]:
                    made.append(i + k)
                else:
                    todo.add(i + k)
            windows.append({"made": made, "todo": todo})

        done = [False] * n
        visited_win = [False] * (n - m + 1)
        q = collections.deque()
        ans = []

        # initial windows with no todo
        for i, w in enumerate(windows):
            if not w["todo"]:
                visited_win[i] = True
                ans.append(i)
                for pos in w["made"]:
                    if not done[pos]:
                        done[pos] = True
                        q.append(pos)

        while q:
            pos = q.popleft()
            start = max(0, pos - m + 1)
            end = min(pos, n - m)
            for i in range(start, end + 1):
                w = windows[i]
                if pos in w["todo"]:
                    w["todo"].remove(pos)
                    if not w["todo"] and not visited_win[i]:
                        visited_win[i] = True
                        ans.append(i)
                        for p in w["made"]:
                            if not done[p]:
                                done[p] = True
                                q.append(p)

        if all(done):
            return ans[::-1]
        return []
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* movesToStamp(char* stamp, char* target, int* returnSize) {
    int m = (int)strlen(stamp);
    int n = (int)strlen(target);
    int maxW = n - m + 1;               // number of possible windows

    // Flags for original mismatches: needFlag[window][position]
    char *needFlag = calloc((size_t)maxW * n, sizeof(char));

    // Remaining mismatched count per window
    int *winCount = (int *)malloc((size_t)maxW * sizeof(int));
    memset(winCount, 0, (size_t)maxW * sizeof(int));

    // For each position, list of windows that cover it
    int *posWinSize = (int *)calloc((size_t)n, sizeof(int));
    int *pos2win = (int *)calloc((size_t)n * maxW, sizeof(int)); // flattened [pos][*]

    for (int w = 0; w < maxW; ++w) {
        for (int j = 0; j < m; ++j) {
            int p = w + j;
            // record that window w covers position p
            pos2win[p * maxW + posWinSize[p]++] = w;

            if (target[p] != stamp[j]) {
                needFlag[w * n + p] = 1;
                winCount[w]++;
            }
        }
    }

    bool *donePos = (bool *)calloc((size_t)n, sizeof(bool));
    bool *doneWindow = (bool *)calloc((size_t)maxW, sizeof(bool));

    int *queue = (int *)malloc((size_t)n * sizeof(int));
    int qhead = 0, qtail = 0;

    int *ans = (int *)malloc((size_t)n * sizeof(int));
    int ansCnt = 0;

    // Initialize with windows that already match completely
    for (int w = 0; w < maxW; ++w) {
        if (winCount[w] == 0 && !doneWindow[w]) {
            doneWindow[w] = true;
            ans[ansCnt++] = w;
            for (int p = w; p < w + m; ++p) {
                if (!donePos[p]) {
                    donePos[p] = true;
                    queue[qtail++] = p;
                }
            }
        }
    }

    // Process the queue
    while (qhead < qtail) {
        int pos = queue[qhead++];
        for (int idx = 0; idx < posWinSize[pos]; ++idx) {
            int w = pos2win[pos * maxW + idx];
            if (doneWindow[w]) continue;
            if (needFlag[w * n + pos]) {
                winCount[w]--;
            }
            if (winCount[w] == 0) {
                doneWindow[w] = true;
                ans[ansCnt++] = w;
                for (int p = w; p < w + m; ++p) {
                    if (!donePos[p]) {
                        donePos[p] = true;
                        queue[qtail++] = p;
                    }
                }
            }
        }
    }

    // Verify all positions are turned to '?'
    bool allDone = true;
    for (int i = 0; i < n; ++i) {
        if (!donePos[i]) { allDone = false; break; }
    }

    int *result;
    if (!allDone) {
        result = (int *)malloc(0);
        *returnSize = 0;
    } else {
        result = (int *)malloc((size_t)ansCnt * sizeof(int));
        for (int i = 0; i < ansCnt; ++i) {
            result[i] = ans[ansCnt - 1 - i]; // reverse order
        }
        *returnSize = ansCnt;
    }

    free(needFlag);
    free(winCount);
    free(posWinSize);
    free(pos2win);
    free(donePos);
    free(doneWindow);
    free(queue);
    free(ans);

    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] MovesToStamp(string stamp, string target) {
        int m = stamp.Length;
        int n = target.Length;
        bool[] done = new bool[n];
        var ans = new System.Collections.Generic.List<int>();
        var q = new System.Collections.Generic.Queue<int>();
        int[] todo = new int[n]; // only indices 0..n-m are used
        var made = new System.Collections.Generic.List<int>[n];
        for (int i = 0; i < n; i++) made[i] = new System.Collections.Generic.List<int>();

        for (int i = 0; i <= n - m; i++) {
            int cnt = 0;
            for (int j = 0; j < m; j++) {
                if (target[i + j] == stamp[j]) {
                    made[i].Add(i + j);
                } else {
                    cnt++;
                }
            }
            todo[i] = cnt;
            if (cnt == 0) {
                ans.Add(i);
                foreach (int pos in made[i]) {
                    if (!done[pos]) {
                        done[pos] = true;
                        q.Enqueue(pos);
                    }
                }
                todo[i] = -1; // mark as processed
            }
        }

        while (q.Count > 0) {
            int idx = q.Dequeue();
            int startLow = System.Math.Max(0, idx - m + 1);
            int startHigh = System.Math.Min(idx, n - m);
            for (int start = startLow; start <= startHigh; start++) {
                if (todo[start] == -1) continue;
                int posInStamp = idx - start;
                if (target[idx] != stamp[posInStamp]) {
                    todo[start]--;
                }
                if (todo[start] == 0) {
                    ans.Add(start);
                    foreach (int p in made[start]) {
                        if (!done[p]) {
                            done[p] = true;
                            q.Enqueue(p);
                        }
                    }
                    todo[start] = -1;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (!done[i]) return new int[0];
        }

        ans.Reverse();
        return ans.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} stamp
 * @param {string} target
 * @return {number[]}
 */
var movesToStamp = function(stamp, target) {
    const m = stamp.length;
    const n = target.length;
    if (n < m) return [];

    const visited = new Array(n).fill(false);               // positions turned to '?'
    const processed = new Array(n - m + 1).fill(false);     // windows already used
    const todoCount = new Array(n - m + 1).fill(0);         // mismatches in each window
    const posWindows = Array.from({ length: n }, () => []); // windows covering each position

    // Initialize windows and adjacency lists
    for (let i = 0; i <= n - m; i++) {
        let cnt = 0;
        for (let j = 0; j < m; j++) {
            if (stamp[j] !== target[i + j]) cnt++;
            posWindows[i + j].push(i);
        }
        todoCount[i] = cnt;
    }

    const queue = [];
    for (let i = 0; i <= n - m; i++) {
        if (todoCount[i] === 0) queue.push(i);
    }

    const result = [];

    while (queue.length) {
        const winIdx = queue.shift();
        if (processed[winIdx]) continue;
        processed[winIdx] = true;
        result.push(winIdx);

        // Turn all positions of this window into '?'
        for (let j = 0; j < m; j++) {
            const pos = winIdx + j;
            if (!visited[pos]) {
                visited[pos] = true;
                // Update neighboring windows
                for (const w of posWindows[pos]) {
                    if (!processed[w]) {
                        todoCount[w]--;
                        if (todoCount[w] === 0) queue.push(w);
                    }
                }
            }
        }
    }

    // Verify all positions are covered
    for (let i = 0; i < n; i++) {
        if (!visited[i]) return [];
    }

    result.reverse(); // reverse to get stamping order
    return result;
};
```

## Typescript

```typescript
function movesToStamp(stamp: string, target: string): number[] {
    const m = stamp.length;
    const n = target.length;
    if (m > n) return [];

    const posWindows: number[][] = Array.from({ length: n }, () => []);
    const windowMade: number[][] = new Array(n - m + 1);
    const windowTodoCount: number[] = new Array(n - m + 1).fill(0);

    for (let i = 0; i <= n - m; i++) {
        const made: number[] = [];
        let todo = 0;
        for (let j = 0; j < m; j++) {
            if (target[i + j] === stamp[j]) {
                made.push(i + j);
            } else {
                todo++;
            }
            posWindows[i + j].push(i);
        }
        windowMade[i] = made;
        windowTodoCount[i] = todo;
    }

    const visited: boolean[] = new Array(n).fill(false);
    const queue: number[] = [];
    const result: number[] = [];

    // Initialize with windows that already match completely
    for (let i = 0; i <= n - m; i++) {
        if (windowTodoCount[i] === 0) {
            result.push(i);
            windowTodoCount[i] = -1; // mark as processed
            for (const p of windowMade[i]) {
                if (!visited[p]) {
                    visited[p] = true;
                    queue.push(p);
                }
            }
        }
    }

    while (queue.length) {
        const pos = queue.shift()!;
        for (const w of posWindows[pos]) {
            if (windowTodoCount[w] === -1) continue; // already done
            const stampIdx = pos - w;
            if (target[pos] !== stamp[stampIdx]) {
                windowTodoCount[w]--;
            }
            if (windowTodoCount[w] === 0) {
                result.push(w);
                windowTodoCount[w] = -1;
                for (const p of windowMade[w]) {
                    if (!visited[p]) {
                        visited[p] = true;
                        queue.push(p);
                    }
                }
            }
        }
    }

    // Verify all positions are turned into '?'
    for (let i = 0; i < n; i++) {
        if (!visited[i]) return [];
    }

    result.reverse();
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $stamp
     * @param String $target
     * @return Integer[]
     */
    function movesToStamp($stamp, $target) {
        $m = strlen($stamp);
        $n = strlen($target);
        if ($m > $n) return [];

        // For each window store made positions and todo count
        $madeList = [];
        $todoCount = [];
        $windowsAtPos = array_fill(0, $n, []);

        for ($i = 0; $i <= $n - $m; $i++) {
            $made = [];
            $todo = 0;
            for ($j = 0; $j < $m; $j++) {
                if ($target[$i + $j] === $stamp[$j]) {
                    $made[] = $i + $j;
                } else {
                    $todo++;
                }
            }
            $madeList[$i] = $made;
            $todoCount[$i] = $todo;

            // map each position to the windows that cover it
            for ($j = $i; $j < $i + $m; $j++) {
                $windowsAtPos[$j][] = $i;
            }
        }

        $queue = new SplQueue();
        $visited = array_fill(0, $n, false);
        $answer = [];

        // Enqueue windows that are already fully matching
        for ($i = 0; $i <= $n - $m; $i++) {
            if ($todoCount[$i] === 0) {
                $answer[] = $i;
                foreach ($madeList[$i] as $pos) {
                    if (!$visited[$pos]) {
                        $visited[$pos] = true;
                        $queue->enqueue($pos);
                    }
                }
            }
        }

        // Process positions that became '?'
        while (!$queue->isEmpty()) {
            $p = $queue->dequeue();
            foreach ($windowsAtPos[$p] as $w) {
                if ($todoCount[$w] === 0) continue; // already processed
                $todoCount[$w]--;
                if ($todoCount[$w] === 0) {
                    $answer[] = $w;
                    foreach ($madeList[$w] as $pos) {
                        if (!$visited[$pos]) {
                            $visited[$pos] = true;
                            $queue->enqueue($pos);
                        }
                    }
                }
            }
        }

        // Verify all positions are turned into '?'
        for ($i = 0; $i < $n; $i++) {
            if (!$visited[$i]) return [];
        }

        // Reverse to get stamping order from start to finish
        return array_reverse($answer);
    }
}
```

## Swift

```swift
class Solution {
    func movesToStamp(_ stamp: String, _ target: String) -> [Int] {
        let s = Array(stamp)
        let t = Array(target)
        let m = s.count
        let n = t.count
        if m > n { return [] }
        
        var made = [[Int]](repeating: [], count: n - m + 1)
        var todo = [[Int]](repeating: [], count: n - m + 1)
        var queue = [Int]()
        var done = [Bool](repeating: false, count: n)
        var stamped = [Bool](repeating: false, count: n - m + 1)
        var ans = [Int]()
        
        for i in 0...(n - m) {
            for j in 0..<m {
                if t[i + j] == s[j] {
                    made[i].append(i + j)
                } else {
                    todo[i].append(i + j)
                }
            }
            if todo[i].isEmpty {
                stamped[i] = true
                ans.append(i)
                for pos in made[i] where !done[pos] {
                    done[pos] = true
                    queue.append(pos)
                }
            }
        }
        
        var qIdx = 0
        while qIdx < queue.count {
            let pos = queue[qIdx]
            qIdx += 1
            let start = max(0, pos - m + 1)
            let end = min(pos, n - m)
            if start > end { continue }
            for w in start...end {
                if stamped[w] { continue }
                if let idx = todo[w].firstIndex(of: pos) {
                    todo[w].remove(at: idx)
                    if todo[w].isEmpty {
                        stamped[w] = true
                        ans.append(w)
                        for p in made[w] where !done[p] {
                            done[p] = true
                            queue.append(p)
                        }
                    }
                }
            }
        }
        
        for i in 0..<n where !done[i] {
            return []
        }
        return ans.reversed()
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun movesToStamp(stamp: String, target: String): IntArray {
        val n = target.length
        val m = stamp.length
        if (m > n) return intArrayOf()
        val windowsMade = Array(n - m + 1) { mutableListOf<Int>() }
        val todo = IntArray(n - m + 1)
        for (i in 0..n - m) {
            var cnt = 0
            for (j in 0 until m) {
                if (target[i + j] == stamp[j]) {
                    windowsMade[i].add(i + j)
                } else {
                    cnt++
                }
            }
            todo[i] = cnt
        }

        val queue: ArrayDeque<Int> = ArrayDeque()
        val doneWindow = BooleanArray(n - m + 1)
        val changed = BooleanArray(n)

        fun enqueueWindow(pos: Int) {
            if (doneWindow[pos]) return
            doneWindow[pos] = true
            for (idx in windowsMade[pos]) {
                if (!changed[idx]) {
                    changed[idx] = true
                    queue.add(idx)
                }
            }
        }

        // initial windows with no todo
        for (i in 0..n - m) {
            if (todo[i] == 0) {
                enqueueWindow(i)
            }
        }

        val result = mutableListOf<Int>()
        while (queue.isNotEmpty()) {
            val idx = queue.removeFirst()
            // any window that covers idx
            val start = maxOf(0, idx - m + 1)
            val end = minOf(idx, n - m)
            for (w in start..end) {
                if (todo[w] == 0) continue
                // if this position was a mismatch for the window, reduce todo
                if (target[idx] != stamp[idx - w]) {
                    todo[w]--
                }
                if (todo[w] == 0) {
                    result.add(w)
                    enqueueWindow(w)
                }
            }
        }

        // check if all positions are changed to '?'
        for (c in changed) {
            if (!c) return intArrayOf()
        }

        // reverse the order to get stamping sequence
        result.reverse()
        return result.toIntArray()
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  List<int> movesToStamp(String stamp, String target) {
    int m = stamp.length;
    int n = target.length;
    int windows = n - m + 1;
    if (windows <= 0) return [];

    // For each window store all positions it covers
    List<List<int>> made = List.generate(windows, (_) => []);
    // Number of mismatched characters in each window
    List<int> todoCount = List.filled(windows, 0);

    for (int i = 0; i < windows; ++i) {
      for (int j = 0; j < m; ++j) {
        if (stamp[j] != target[i + j]) {
          todoCount[i]++;
        }
        made[i].add(i + j);
      }
    }

    Queue<int> q = ListQueue<int>();
    List<bool> doneChar = List.filled(n, false);
    List<int> ans = [];

    // Windows that are already fully matching can be stamped immediately
    for (int i = 0; i < windows; ++i) {
      if (todoCount[i] == 0) {
        ans.add(i);
        for (int pos in made[i]) {
          if (!doneChar[pos]) {
            doneChar[pos] = true;
            q.add(pos);
          }
        }
      }
    }

    while (q.isNotEmpty) {
      int idx = q.removeFirst();
      int start = idx - m + 1;
      if (start < 0) start = 0;
      int end = idx;
      if (end > windows - 1) end = windows - 1;

      for (int w = start; w <= end; ++w) {
        if (todoCount[w] == 0) continue;
        // If this position was a mismatch in window w, it is now resolved
        if (stamp[idx - w] != target[idx]) {
          todoCount[w]--;
          if (todoCount[w] == 0) {
            ans.add(w);
            for (int pos in made[w]) {
              if (!doneChar[pos]) {
                doneChar[pos] = true;
                q.add(pos);
              }
            }
          }
        }
      }
    }

    // Verify all characters have been turned into '?'
    for (bool b in doneChar) {
      if (!b) return [];
    }

    // Reverse to get the order of stamping from start to finish
    ans = ans.reversed.toList();
    return ans;
  }
}
```

## Golang

```go
func movesToStamp(stamp string, target string) []int {
	m := len(stamp)
	n := len(target)
	if m > n {
		return []int{}
	}

	type window struct {
		made []int
		todo int
	}
	windows := make([]window, n-m+1)
	posWindows := make([][]int, n)

	for i := 0; i <= n-m; i++ {
		var made []int
		todo := 0
		for j := 0; j < m; j++ {
			if stamp[j] == target[i+j] {
				made = append(made, i+j)
			} else {
				todo++
			}
		}
		windows[i] = window{made: made, todo: todo}
		for p := i; p < i+m; p++ {
			posWindows[p] = append(posWindows[p], i)
		}
	}

	done := make([]bool, n)
	visitedWindow := make([]bool, n-m+1)

	queue := []int{}
	ans := []int{}

	// windows that are already fully matched
	for i := 0; i <= n-m; i++ {
		if windows[i].todo == 0 {
			visitedWindow[i] = true
			ans = append(ans, i)
			for _, p := range windows[i].made {
				if !done[p] {
					done[p] = true
					queue = append(queue, p)
				}
			}
		}
	}

	head := 0
	for head < len(queue) {
		pos := queue[head]
		head++
		for _, wIdx := range posWindows[pos] {
			if visitedWindow[wIdx] {
				continue
			}
			// if this position was a mismatch in the window, reduce todo count
			if stamp[pos-wIdx] != target[pos] {
				windows[wIdx].todo--
			}
			if windows[wIdx].todo == 0 {
				visitedWindow[wIdx] = true
				ans = append(ans, wIdx)
				for _, p := range windows[wIdx].made {
					if !done[p] {
						done[p] = true
						queue = append(queue, p)
					}
				}
			}
		}
	}

	// check if all positions are turned to '?'
	for i := 0; i < n; i++ {
		if !done[i] {
			return []int{}
		}
	}

	// reverse the answer to get forward stamping order
	for i, j := 0, len(ans)-1; i < j; i, j = i+1, j-1 {
		ans[i], ans[j] = ans[j], ans[i]
	}
	return ans
}
```

## Ruby

```ruby
def moves_to_stamp(stamp, target)
  m = stamp.length
  n = target.length
  windows = []
  visited = Array.new(n, false)
  queue = []
  ans = []

  (0..n - m).each do |i|
    made = []
    todo = 0
    (0...m).each do |j|
      if target[i + j] == stamp[j]
        made << i + j
      else
        todo += 1
      end
    end
    windows[i] = { made: made, todo: todo }
    if todo == 0
      ans << i
      (i...i + m).each do |pos|
        unless visited[pos]
          visited[pos] = true
          queue << pos
        end
      end
    end
  end

  until queue.empty?
    idx = queue.shift
    start = [0, idx - m + 1].max
    finish = [idx, n - m].min
    (start..finish).each do |i|
      w = windows[i]
      next if w[:todo] == 0
      # If this position was a mismatch for this window, it now becomes resolved.
      if target[idx] != stamp[idx - i]
        w[:todo] -= 1
        if w[:todo] == 0
          ans << i
          (i...i + m).each do |pos|
            unless visited[pos]
              visited[pos] = true
              queue << pos
            end
          end
        end
      end
    end
  end

  visited.all? ? ans.reverse : []
end
```

## Scala

```scala
object Solution {
    def movesToStamp(stamp: String, target: String): Array[Int] = {
        val m = stamp.length
        val n = target.length
        if (m > n) return Array.emptyIntArray

        val sArr = stamp.toCharArray
        val tArr = target.toCharArray

        val windows = n - m + 1
        val todoCount = new Array[Int](windows)

        // compute mismatches for each window
        var i = 0
        while (i < windows) {
            var cnt = 0
            var j = 0
            while (j < m) {
                if (tArr(i + j) != sArr(j)) cnt += 1
                j += 1
            }
            todoCount(i) = cnt
            i += 1
        }

        val queue = new java.util.ArrayDeque[Int]()
        var w = 0
        while (w < windows) {
            if (todoCount(w) == 0) queue.add(w)
            w += 1
        }

        val visited = new Array[Boolean](n)
        val ans = scala.collection.mutable.ArrayBuffer.empty[Int]

        while (!queue.isEmpty) {
            val start = queue.poll()
            ans += start

            var offset = 0
            while (offset < m) {
                val pos = start + offset
                if (!visited(pos)) {
                    visited(pos) = true
                    // update all windows that include this position
                    var winStart = math.max(0, pos - m + 1)
                    val winEnd = math.min(pos, n - m)
                    while (winStart <= winEnd) {
                        todoCount(winStart) -= 1
                        if (todoCount(winStart) == 0) queue.add(winStart)
                        winStart += 1
                    }
                }
                offset += 1
            }
        }

        // verify all positions are covered
        var allCovered = true
        var idx = 0
        while (idx < n && allCovered) {
            if (!visited(idx)) allCovered = false
            idx += 1
        }

        if (!allCovered) Array.emptyIntArray else ans.reverse.toArray
    }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn moves_to_stamp(stamp: String, target: String) -> Vec<i32> {
        let stamp = stamp.as_bytes();
        let target = target.as_bytes();
        let m = stamp.len();
        let n = target.len();

        if m > n {
            return vec![];
        }

        // For each window starting at i, store positions that already match
        let mut made: Vec<Vec<usize>> = vec![Vec::new(); n - m + 1];
        // Number of mismatched characters in the window
        let mut todo: Vec<i32> = vec![0; n - m + 1];

        for i in 0..=n - m {
            for j in 0..m {
                if stamp[j] == target[i + j] {
                    made[i].push(i + j);
                } else {
                    todo[i] += 1;
                }
            }
        }

        let mut queue: VecDeque<usize> = VecDeque::new();
        let mut visited_window = vec![false; n - m + 1];
        for i in 0..=n - m {
            if todo[i] == 0 {
                queue.push_back(i);
                visited_window[i] = true;
            }
        }

        let mut done_char = vec![false; n];
        let mut answer: Vec<i32> = Vec::new();

        while let Some(start) = queue.pop_front() {
            answer.push(start as i32);
            // Turn all characters in this window to '?'
            for pos in start..start + m {
                if !done_char[pos] {
                    done_char[pos] = true;
                    // Update all windows that include this position
                    let lo = if pos >= m - 1 { pos + 1 - m } else { 0 };
                    let hi = std::cmp::min(pos, n - m);
                    for w in lo..=hi {
                        if !visited_window[w] {
                            todo[w] -= 1;
                            if todo[w] == 0 {
                                visited_window[w] = true;
                                queue.push_back(w);
                            }
                        }
                    }
                }
            }
        }

        // Verify all positions are turned to '?'
        if done_char.iter().any(|&b| !b) {
            return vec![];
        }

        answer.reverse();
        answer
    }
}
```

## Racket

```racket
(define/contract (moves-to-stamp stamp target)
  (-> string? string? (listof exact-integer?))
  (let* ((n (string-length target))
         (m (string-length stamp))
         (window-count (+ (- n m) 1))
         (need (make-vector window-count #f))      ; each entry will become a vector of bools
         (cnt (make-vector window-count 0))
         (visited (make-vector n #f))
         (queue (make-vector (* n 2) -1))
         (head 0)
         (tail 0)
         (result '()))
    ;; Initialize each window: which positions still need to be matched
    (for ([i (in-range 0 window-count)])
      (let ((need-vec (make-vector m #f))
            (c 0))
        (for ([j (in-range 0 m)])
          (if (char=? (string-ref target (+ i j)) (string-ref stamp j))
              (vector-set! need-vec j #f)
              (begin
                (vector-set! need-vec j #t)
                (set! c (+ c 1)))))
        (vector-set! need i need-vec)
        (vector-set! cnt i c)
        (when (= c 0)                     ; window already matches stamp
          (for ([j (in-range 0 m)])
            (let ((pos (+ i j)))
              (unless (vector-ref visited pos)
                (vector-set! visited pos #t)
                (vector-set! queue tail pos)
                (set! tail (+ tail 1))))))))
    ;; Process positions that have become '?'
    (let loop ()
      (when (< head tail)
        (let ((pos (vector-ref queue head)))
          (set! head (+ head 1))
          (let* ((start (max 0 (- pos m -1)))   ; max(0, pos - m + 1)
                 (end   (min pos (- n m))))    ; min(pos, n-m)
            (for ([w (in-range start (+ end 1))])
              (let ((need-vec (vector-ref need w)))
                (when (and need-vec (vector-ref need-vec (- pos w))) ; this position was needed
                  (vector-set! need-vec (- pos w) #f)
                  (let ((c (- (vector-ref cnt w) 1)))
                    (vector-set! cnt w c)
                    (when (= c 0)               ; window can now be stamped
                      (set! result (cons w result))
                      (for ([j (in-range 0 m)])
                        (let ((p (+ w j)))
                          (unless (vector-ref visited p)
                            (vector-set! visited p #t)
                            (vector-set! queue tail p)
                            (set! tail (+ tail 1))))))))))))
        (loop))
    ;; Verify all characters are covered
    (let ((all-covered #t))
      (for ([i (in-range n)])
        (unless (vector-ref visited i)
          (set! all-covered #f)))
      (if all-covered
          (reverse result)
          '()))))
```

## Erlang

```erlang
-spec moves_to_stamp(Stamp :: unicode:unicode_binary(), Target :: unicode:unicode_binary()) -> [integer()].
moves_to_stamp(Stamp, Target) ->
    StampList = binary_to_list(Stamp),
    TargetList = binary_to_list(Target),
    M = length(StampList),
    N = length(TargetList),
    case M > N of
        true -> [];
        false ->
            StampArr = array:from_list(StampList),
            TargetArr = array:from_list(TargetList),
            NumWindows = N - M + 1,
            Made0 = array:new(NumWindows, {default, []}),
            Todo0 = array:new(NumWindows, {default, []}),
            PosWin0 = array:new(N, {default, []}),
            {MadeArr, TodoArr, PosWinArr} =
                build_windows(0, NumWindows, M, StampArr, TargetArr,
                              Made0, Todo0, PosWin0),
            InitQueue = init_queue(0, NumWindows, TodoArr, []),
            Visited0 = array:new(N, {default, false}),
            Processed0 = array:new(NumWindows, {default, false}),
            {VisitedFinal, _TodoFinal, _ProcessedFinal, ResRev} =
                process_queue(InitQueue, M,
                              Visited0, TodoArr, Processed0,
                              PosWinArr, []),
            case all_visited(N, VisitedFinal) of
                true -> lists:reverse(ResRev);
                false -> []
            end
    end.

%% Build window information for each possible stamp position.
build_windows(Index, NumWindows, M, StampArr, TargetArr,
              MadeAcc, TodoAcc, PosWinAcc) when Index < NumWindows ->
    {MadeList, TodoList, PosWinAcc2} = build_one_window(Index, M, StampArr, TargetArr, PosWinAcc),
    MadeAcc1 = array:set(Index, MadeList, MadeAcc),
    TodoAcc1 = array:set(Index, TodoList, TodoAcc),
    build_windows(Index + 1, NumWindows, M, StampArr, TargetArr,
                  MadeAcc1, TodoAcc1, PosWinAcc2);
build_windows(_, _, _, _, _, MadeAcc, TodoAcc, PosWinAcc) ->
    {MadeAcc, TodoAcc, PosWinAcc}.

%% Build data for a single window starting at Start.
build_one_window(Start, M, StampArr, TargetArr, PosWinAcc) ->
    build_one_window(0, M, Start, StampArr, TargetArr, [], [], PosWinAcc).

build_one_window(J, M, Start, StampArr, TargetArr, Made, Todo, PosWinAcc) when J < M ->
    Pos = Start + J,
    SChar = array:get(J, StampArr),
    TChar = array:get(Pos, TargetArr),
    {Made1, Todo1} =
        if SChar == TChar -> {[Pos | Made], Todo};
           true          -> {Made, [Pos | Todo]}
        end,
    Prev = array:get(Pos, PosWinAcc),
    PosWinAcc1 = array:set(Pos, [Start | Prev], PosWinAcc),
    build_one_window(J + 1, M, Start, StampArr, TargetArr, Made1, Todo1, PosWinAcc1);
build_one_window(_, _, _, _, _, Made, Todo, PosWinAcc) ->
    {Made, Todo, PosWinAcc}.

%% Initialize queue with windows that have no pending mismatches.
init_queue(I, NumWindows, TodoArr, Acc) when I < NumWindows ->
    case array:get(I, TodoArr) of
        [] -> init_queue(I + 1, NumWindows, TodoArr, [I | Acc]);
        _  -> init_queue(I + 1, NumWindows, TodoArr, Acc)
    end;
init_queue(_, _, _, Acc) -> Acc.

%% Process the queue of windows to stamp.
process_queue(Queue, M, Visited, TodoArr, Processed, PosWinArr, ResRev) ->
    case Queue of
        [] -> {Visited, TodoArr, Processed, ResRev};
        [W | Rest] ->
            if array:get(W, Processed) =:= true ->
                    process_queue(Rest, M, Visited, TodoArr, Processed,
                                  PosWinArr, ResRev);
               true ->
                    Processed1 = array:set(W, true, Processed),
                    {Visited1, TodoArr1, NewEnq} =
                        stamp_window(W, M, Visited, TodoArr, PosWinArr),
                    Queue1 = NewEnq ++ Rest,
                    process_queue(Queue1, M, Visited1, TodoArr1,
                                  Processed1, PosWinArr, [W | ResRev])
            end
    end.

%% Stamp a window: turn its characters into '?' and update affected windows.
stamp_window(W, M, Visited0, Todo0, PosWinArr) ->
    Offsets = lists:seq(0, M - 1),
    {Visited1, Todo1, Enq} =
        lists:foldl(
          fun(J, {VisAcc, TodoAcc, QAcc}) ->
              Pos = W + J,
              case array:get(Pos, VisAcc) of
                  true -> {VisAcc, TodoAcc, QAcc};
                  false ->
                      VisAcc2 = array:set(Pos, true, VisAcc),
                      WinList = array:get(Pos, PosWinArr),
                      {TodoAcc2, QAcc2} =
                          lists:foldl(
                            fun(Wi, {TAcc, QA}) ->
                                TodoWi = array:get(Wi, TAcc),
                                NewTodoWi = lists:delete(Pos, TodoWi),
                                TAcc3 = array:set(Wi, NewTodoWi, TAcc),
                                case NewTodoWi of
                                    [] -> {TAcc3, [Wi | QA]};
                                    _  -> {TAcc3, QA}
                                end
                            end,
                            {TodoAcc, QAcc},
                            WinList),
                      {VisAcc2, TodoAcc2, QAcc2}
              end
          end,
          {Visited0, Todo0, []},
          Offsets),
    {Visited1, Todo1, Enq}.

%% Verify all positions have been turned into '?'.
all_visited(N, VisitedArr) ->
    lists:foldl(
      fun(I, Acc) -> Acc andalso array:get(I, VisitedArr) end,
      true,
      lists:seq(0, N - 1)
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec moves_to_stamp(stamp :: String.t(), target :: String.t()) :: [integer]
  def moves_to_stamp(stamp, target) do
    m = String.length(stamp)
    n = String.length(target)

    stamp_chars = String.to_charlist(stamp)
    target_chars = String.to_charlist(target)
    target_arr = :array.from_list(target_chars)

    size_w = n - m + 1

    {windows_arr, init_queue, pos_to_windows} =
      Enum.reduce(0..size_w - 1, {:array.new(size_w, default: nil), :queue.new(), %{}}, fn i,
                                                                                       {w_arr,
                                                                                        q,
                                                                                        p_map} ->
        {made_rev, todo_set} =
          Enum.reduce(0..m - 1, {[], MapSet.new()}, fn k, {made_acc, todo_acc} ->
            pos = i + k
            t_char = :array.get(pos, target_arr)
            s_char = Enum.at(stamp_chars, k)

            if t_char == s_char do
              {[pos | made_acc], todo_acc}
            else
              {made_acc, MapSet.put(todo_acc, pos)}
            end
          end)

        win = %{made: Enum.reverse(made_rev), todo: todo_set}
        w_arr = :array.set(i, win, w_arr)

        p_map =
          Enum.reduce(0..m - 1, p_map, fn k, acc ->
            pos = i + k

            Map.update(acc, pos, [i], fn list -> [i | list] end)
          end)

        q = if MapSet.size(todo_set) == 0, do: :queue.in(i, q), else: q
        {w_arr, q, p_map}
      end)

    visited_arr = :array.new(n, default: false)
    processed_win = :array.new(size_w, default: false)

    {final_visited, answer_rev} =
      bfs(init_queue, windows_arr, visited_arr, processed_win, pos_to_windows, [])

    all_covered? =
      Enum.reduce(0..n - 1, true, fn idx, acc -> acc and :array.get(idx, final_visited) end)

    if all_covered?, do: answer_rev, else: []
  end

  defp bfs(queue, windows_arr, visited_arr, processed_win, pos_to_windows, answer) do
    case :queue.out(queue) do
      {:empty, _} ->
        {visited_arr, answer}

      {{:value, w_idx}, q2} ->
        if :array.get(w_idx, processed_win) do
          bfs(q2, windows_arr, visited_arr, processed_win, pos_to_windows, answer)
        else
          processed_win = :array.set(w_idx, true, processed_win)
          answer = [w_idx | answer]
          win = :array.get(w_idx, windows_arr)

          {q3, w_arr2, v_arr2} =
            Enum.reduce(win.made, {q2, windows_arr, visited_arr}, fn pos,
                                                                    {q_acc, w_arr_acc,
                                                                     v_arr_acc} ->
              if not :array.get(pos, v_arr_acc) do
                v_arr_acc = :array.set(pos, true, v_arr_acc)
                ws = Map.get(pos_to_windows, pos, [])

                {q_new, w_arr_new} =
                  Enum.reduce(ws, {q_acc, w_arr_acc}, fn w2,
                                                        {q_inner, w_arr_inner} ->
                    win2 = :array.get(w2, w_arr_inner)

                    if MapSet.member?(win2.todo, pos) do
                      new_todo = MapSet.delete(win2.todo, pos)
                      win2 = %{win2 | todo: new_todo}
                      w_arr_inner = :array.set(w2, win2, w_arr_inner)

                      q_inner =
                        if MapSet.size(new_todo) == 0 and not :array.get(w2,
                                                                          processed_win) do
                          :queue.in(w2, q_inner)
                        else
                          q_inner
                        end

                      {q_inner, w_arr_inner}
                    else
                      {q_inner, w_arr_inner}
                    end
                  end)

                {q_new, w_arr_new, v_arr_acc}
              else
                {q_acc, w_arr_acc, v_arr_acc}
              end
            end)

          bfs(q3, w_arr2, v_arr2, processed_win, pos_to_windows, answer)
        end
    end
  end
end
```
