# 0854. K-Similar Strings

## Cpp

```cpp
class Solution {
public:
    int kSimilarity(string s1, string s2) {
        if (s1 == s2) return 0;
        unordered_map<string, int> dist;
        queue<string> q;
        dist[s1] = 0;
        q.push(s1);
        while (!q.empty()) {
            string cur = q.front(); q.pop();
            int d = dist[cur];
            int i = 0, n = cur.size();
            while (i < n && cur[i] == s2[i]) ++i;
            for (int j = i + 1; j < n; ++j) {
                if (cur[j] == s2[i] && cur[j] != s2[j]) {
                    string nxt = cur;
                    swap(nxt[i], nxt[j]);
                    if (!dist.count(nxt)) {
                        if (nxt == s2) return d + 1;
                        dist[nxt] = d + 1;
                        q.push(move(nxt));
                    }
                }
            }
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int kSimilarity(String s1, String s2) {
        if (s1.equals(s2)) return 0;
        Queue<String> queue = new ArrayDeque<>();
        Set<String> visited = new HashSet<>();
        queue.offer(s1);
        visited.add(s1);
        int steps = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int k = 0; k < size; k++) {
                String cur = queue.poll();
                if (cur.equals(s2)) return steps;
                int i = 0;
                while (i < cur.length() && cur.charAt(i) == s2.charAt(i)) i++;
                char[] arr = cur.toCharArray();
                for (int j = i + 1; j < arr.length; j++) {
                    if (arr[j] == s2.charAt(i) && arr[j] != s2.charAt(j)) {
                        swap(arr, i, j);
                        String next = new String(arr);
                        if (!visited.contains(next)) {
                            visited.add(next);
                            queue.offer(next);
                        }
                        swap(arr, i, j); // revert
                    }
                }
            }
            steps++;
        }
        return -1; // should never reach here as s2 is an anagram of s1
    }

    private void swap(char[] arr, int i, int j) {
        char tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}
```

## Python

```python
class Solution(object):
    def kSimilarity(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        if s1 == s2:
            return 0
        from collections import deque

        n = len(s1)
        visited = set([s1])
        q = deque()
        q.append((s1, 0))

        while q:
            cur, steps = q.popleft()
            # find first mismatched position
            i = 0
            while i < n and cur[i] == s2[i]:
                i += 1
            if i == n:   # all matched
                return steps

            # try to swap with a character that matches s2[i]
            for j in range(i + 1, n):
                if cur[j] == s2[i] and cur[j] != s2[j]:
                    lst = list(cur)
                    lst[i], lst[j] = lst[j], lst[i]
                    nxt = ''.join(lst)
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps + 1))
        return -1
```

## Python3

```python
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        n = len(s1)
        from collections import deque

        visited = {s1}
        q = deque()
        q.append((s1, 0))

        while q:
            cur, steps = q.popleft()
            # find first mismatched position
            i = 0
            while i < n and cur[i] == s2[i]:
                i += 1
            if i == n:  # all matched
                return steps

            # try to swap with a character that can fix position i
            for j in range(i + 1, n):
                if cur[j] == s2[i] and cur[j] != s2[j]:
                    lst = list(cur)
                    lst[i], lst[j] = lst[j], lst[i]
                    nxt = ''.join(lst)
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps + 1))
            # If no beneficial swap found (possible with duplicates), allow any swap that puts correct char at i
            else:
                for j in range(i + 1, n):
                    if cur[j] == s2[i]:
                        lst = list(cur)
                        lst[i], lst[j] = lst[j], lst[i]
                        nxt = ''.join(lst)
                        if nxt not in visited:
                            visited.add(nxt)
                            q.append((nxt, steps + 1))
                        break
        return -1
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

int kSimilarity(char* s1c, char* s2c) {
    string start(s1c), target(s2c);
    if (start == target) return 0;
    int n = start.size();
    queue<pair<string,int>> q;
    unordered_set<string> visited;
    q.emplace(start, 0);
    visited.insert(start);
    while (!q.empty()) {
        auto [cur, steps] = q.front(); q.pop();
        if (cur == target) return steps;
        int i = 0;
        while (i < n && cur[i] == target[i]) ++i;
        bool added = false;
        for (int j = i + 1; j < n; ++j) {
            if (cur[j] == target[i] && cur[j] != target[j]) {
                string nxt = cur;
                swap(nxt[i], nxt[j]);
                if (!visited.count(nxt)) {
                    visited.insert(nxt);
                    q.emplace(nxt, steps + 1);
                }
                added = true;
            }
        }
        if (added) continue;
        for (int j = i + 1; j < n; ++j) {
            if (cur[j] == target[i]) {
                string nxt = cur;
                swap(nxt[i], nxt[j]);
                if (!visited.count(nxt)) {
                    visited.insert(nxt);
                    q.emplace(nxt, steps + 1);
                }
            }
        }
    }
    return -1; // should never reach here for valid input
}
```

## Csharp

```csharp
public class Solution {
    public int KSimilarity(string s1, string s2) {
        if (s1 == s2) return 0;
        var target = s2;
        var visited = new HashSet<string>();
        var queue = new Queue<string>();
        queue.Enqueue(s1);
        visited.Add(s1);
        int steps = 0;

        while (queue.Count > 0) {
            int size = queue.Count;
            for (int k = 0; k < size; k++) {
                string cur = queue.Dequeue();
                if (cur == target) return steps;

                // find first mismatched position
                int i = 0;
                while (i < cur.Length && cur[i] == target[i]) i++;
                char[] curArr = cur.ToCharArray();

                for (int j = i + 1; j < curArr.Length; j++) {
                    if (curArr[j] != target[i]) continue; // must bring correct character to position i
                    var nextArr = (char[])curArr.Clone();
                    char tmp = nextArr[i];
                    nextArr[i] = nextArr[j];
                    nextArr[j] = tmp;
                    string nextStr = new string(nextArr);
                    if (!visited.Contains(nextStr)) {
                        visited.Add(nextStr);
                        queue.Enqueue(nextStr);
                    }
                }
            }
            steps++;
        }

        return -1; // should never reach here because s2 is an anagram of s1
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {number}
 */
var kSimilarity = function(s1, s2) {
    if (s1 === s2) return 0;
    const visited = new Set();
    const queue = [];
    let head = 0;
    visited.add(s1);
    queue.push([s1, 0]);

    while (head < queue.length) {
        const [cur, step] = queue[head++];
        if (cur === s2) return step;

        // find first mismatched position
        let i = 0;
        while (i < cur.length && cur[i] === s2[i]) i++;
        if (i === cur.length) continue; // already equal, should have returned

        for (let j = i + 1; j < cur.length; j++) {
            // we only consider swaps that bring a correct character to position i
            if (cur[j] === s2[i] && cur[j] !== s2[j]) {
                const arr = cur.split('');
                [arr[i], arr[j]] = [arr[j], arr[i]];
                const nxt = arr.join('');
                if (!visited.has(nxt)) {
                    visited.add(nxt);
                    queue.push([nxt, step + 1]);
                }
            }
        }
    }

    return -1; // should never reach here for valid inputs
};
```

## Typescript

```typescript
function kSimilarity(s1: string, s2: string): number {
    if (s1 === s2) return 0;

    const visited = new Set<string>();
    const queue: string[] = [];
    let head = 0;
    queue.push(s1);
    visited.add(s1);

    let steps = 0;
    while (head < queue.length) {
        const levelSize = queue.length - head;
        for (let i = 0; i < levelSize; i++) {
            const cur = queue[head++];
            if (cur === s2) return steps;

            const arr = cur.split('');
            let idx = 0;
            while (idx < arr.length && arr[idx] === s2[idx]) idx++;

            for (let j = idx + 1; j < arr.length; j++) {
                if (arr[j] === s2[idx] && arr[j] !== s2[j]) {
                    [arr[idx], arr[j]] = [arr[j], arr[idx]];
                    const next = arr.join('');
                    if (!visited.has(next)) {
                        visited.add(next);
                        queue.push(next);
                    }
                    // revert swap for further iterations
                    [arr[idx], arr[j]] = [arr[j], arr[idx]];
                }
            }
        }
        steps++;
    }

    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @return Integer
     */
    function kSimilarity($s1, $s2) {
        if ($s1 === $s2) return 0;
        $len = strlen($s1);
        $queue = new SplQueue();
        $queue->enqueue([$s1, 0]);
        $visited = [$s1 => true];

        while (!$queue->isEmpty()) {
            [$cur, $dist] = $queue->dequeue();
            if ($cur === $s2) return $dist;

            // find first mismatched position
            $i = 0;
            while ($i < $len && $cur[$i] === $s2[$i]) {
                $i++;
            }
            if ($i >= $len) continue; // should not happen

            for ($j = $i + 1; $j < $len; $j++) {
                // only consider swaps that place correct character at position i
                if ($cur[$j] === $s2[$i] && $cur[$j] !== $s2[$j]) {
                    // perform swap
                    $arr = str_split($cur);
                    $tmp = $arr[$i];
                    $arr[$i] = $arr[$j];
                    $arr[$j] = $tmp;
                    $next = implode('', $arr);

                    if (!isset($visited[$next])) {
                        $visited[$next] = true;
                        $queue->enqueue([$next, $dist + 1]);
                    }
                }
            }
        }

        return -1; // unreachable for valid inputs
    }
}
```

## Swift

```swift
class Solution {
    func kSimilarity(_ s1: String, _ s2: String) -> Int {
        if s1 == s2 { return 0 }
        let target = Array(s2)
        var start = Array(s1)
        let n = start.count
        
        var queue: [(arr: [Character], steps: Int)] = []
        var head = 0
        queue.append((start, 0))
        var visited = Set<String>()
        visited.insert(String(start))
        
        while head < queue.count {
            let (currArr, step) = queue[head]
            head += 1
            
            // find first mismatched position
            var i = 0
            while i < n && currArr[i] == target[i] { i += 1 }
            if i == n { return step } // reached target
            
            var candidates: [Int] = []
            // Prefer swaps that also fix the other position
            for j in (i + 1)..<n {
                if currArr[j] == target[i] && currArr[j] != target[j] {
                    candidates.append(j)
                }
            }
            // If none, allow any matching character
            if candidates.isEmpty {
                for j in (i + 1)..<n {
                    if currArr[j] == target[i] {
                        candidates.append(j)
                    }
                }
            }
            
            for j in candidates {
                var newArr = currArr
                newArr.swapAt(i, j)
                let str = String(newArr)
                if !visited.contains(str) {
                    visited.insert(str)
                    queue.append((newArr, step + 1))
                }
            }
        }
        return -1 // should never reach here for valid input
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kSimilarity(s1: String, s2: String): Int {
        if (s1 == s2) return 0
        val visited = HashSet<String>()
        val queue: ArrayDeque<Pair<String, Int>> = ArrayDeque()
        queue.add(Pair(s1, 0))
        visited.add(s1)
        while (queue.isNotEmpty()) {
            val (cur, steps) = queue.removeFirst()
            if (cur == s2) return steps
            var i = 0
            while (i < cur.length && cur[i] == s2[i]) i++
            var foundBetter = false
            for (j in i + 1 until cur.length) {
                if (cur[j] == s2[i] && cur[j] != s2[j]) {
                    val sb = StringBuilder(cur)
                    val tmp = sb[i]
                    sb.setCharAt(i, sb[j])
                    sb.setCharAt(j, tmp)
                    val next = sb.toString()
                    if (visited.add(next)) {
                        queue.add(Pair(next, steps + 1))
                    }
                    foundBetter = true
                }
            }
            if (!foundBetter) {
                for (j in i + 1 until cur.length) {
                    if (cur[j] == s2[i]) {
                        val sb = StringBuilder(cur)
                        val tmp = sb[i]
                        sb.setCharAt(i, sb[j])
                        sb.setCharAt(j, tmp)
                        val next = sb.toString()
                        if (visited.add(next)) {
                            queue.add(Pair(next, steps + 1))
                        }
                    }
                }
            }
        }
        return -1
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int kSimilarity(String s1, String s2) {
    if (s1 == s2) return 0;
    final target = s2;
    final queue = Queue<String>();
    final visited = <String>{};

    queue.add(s1);
    visited.add(s1);
    int steps = 0;

    while (queue.isNotEmpty) {
      int levelSize = queue.length;
      for (int _ = 0; _ < levelSize; _++) {
        String cur = queue.removeFirst();
        if (cur == target) return steps;

        // find first mismatched position
        int i = 0;
        while (i < cur.length && cur[i] == target[i]) i++;

        List<int> candidates = [];

        // Prefer swaps that place correct character at position i and also fix j
        for (int j = i + 1; j < cur.length; j++) {
          if (cur[j] == target[i] && cur[j] != target[j]) {
            candidates.add(j);
          }
        }

        // If none, consider any position that can place correct char at i
        if (candidates.isEmpty) {
          for (int j = i + 1; j < cur.length; j++) {
            if (cur[j] == target[i]) {
              candidates.add(j);
            }
          }
        }

        for (int j in candidates) {
          // swap characters at i and j
          final sb = StringBuffer();
          for (int k = 0; k < cur.length; k++) {
            if (k == i) {
              sb.write(cur[j]);
            } else if (k == j) {
              sb.write(cur[i]);
            } else {
              sb.write(cur[k]);
            }
          }
          final next = sb.toString();
          if (!visited.contains(next)) {
            visited.add(next);
            queue.add(next);
          }
        }
      }
      steps++;
    }

    return -1; // should never reach here for valid inputs
  }
}
```

## Golang

```go
func kSimilarity(s1 string, s2 string) int {
	if s1 == s2 {
		return 0
	}
	type node struct {
		str  string
		step int
	}
	queue := []node{{s1, 0}}
	visited := map[string]bool{s1: true}

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]

		if cur.str == s2 {
			return cur.step
		}

		b := []byte(cur.str)
		var i int
		for i = 0; i < len(b); i++ {
			if b[i] != s2[i] {
				break
			}
		}

		for j := i + 1; j < len(b); j++ {
			if b[j] == s2[i] && b[j] != s2[j] {
				nb := make([]byte, len(b))
				copy(nb, b)
				nb[i], nb[j] = nb[j], nb[i]
				ns := string(nb)
				if !visited[ns] {
					visited[ns] = true
					queue = append(queue, node{ns, cur.step + 1})
				}
			}
		}
	}
	return -1
}
```

## Ruby

```ruby
require 'set'

# @param {String} s1
# @param {String} s2
# @return {Integer}
def k_similarity(s1, s2)
  return 0 if s1 == s2

  visited = Set.new([s1])
  queue = [[s1, 0]]

  while (cur, steps = queue.shift)
    # find first mismatched position
    i = 0
    while i < cur.length && cur[i] == s2[i]
      i += 1
    end
    next if i == cur.length

    cur_arr = cur.chars
    target_char = s2[i]

    candidates = []
    (i + 1...cur.length).each do |j|
      if cur_arr[j] == target_char && cur_arr[j] != s2[j]
        candidates << j
      end
    end

    # fallback: any mismatched position if no direct match found
    if candidates.empty?
      (i + 1...cur.length).each do |j|
        candidates << j if cur_arr[j] != s2[j]
      end
    end

    candidates.each do |j|
      new_arr = cur_arr.dup
      new_arr[i], new_arr[j] = new_arr[j], new_arr[i]
      new_str = new_arr.join

      return steps + 1 if new_str == s2
      unless visited.include?(new_str)
        visited.add(new_str)
        queue << [new_str, steps + 1]
      end
    end
  end

  -1
end
```

## Scala

```scala
object Solution {
    def kSimilarity(s1: String, s2: String): Int = {
        if (s1 == s2) return 0
        val visited = scala.collection.mutable.HashSet[String]()
        val queue = scala.collection.mutable.ArrayDeque[(String, Int)]()
        visited.add(s1)
        queue.append((s1, 0))
        while (queue.nonEmpty) {
            val (cur, steps) = queue.removeHead()
            if (cur == s2) return steps
            val curArr = cur.toCharArray
            var i = 0
            while (i < curArr.length && curArr(i) == s2.charAt(i)) i += 1
            var j = i + 1
            while (j < curArr.length) {
                if (curArr(j) != s2.charAt(j) && curArr(j) == s2.charAt(i)) {
                    val nextArr = curArr.clone()
                    val tmp = nextArr(i)
                    nextArr(i) = nextArr(j)
                    nextArr(j) = tmp
                    val nextStr = new String(nextArr)
                    if (!visited.contains(nextStr)) {
                        visited.add(nextStr)
                        queue.append((nextStr, steps + 1))
                    }
                }
                j += 1
            }
        }
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn k_similarity(s1: String, s2: String) -> i32 {
        fn dfs(cur: &mut Vec<char>, idx: usize, swaps: i32, target: &[char], best: &mut i32) {
            let n = cur.len();
            // skip already matched prefix
            let mut i = idx;
            while i < n && cur[i] == target[i] {
                i += 1;
            }
            if i == n {
                if swaps < *best {
                    *best = swaps;
                }
                return;
            }

            // heuristic lower bound: at least (mismatches+1)/2 more swaps needed
            let mut mism = 0;
            for k in i..n {
                if cur[k] != target[k] {
                    mism += 1;
                }
            }
            let lb = ((mism as i32) + 1) / 2;
            if swaps + lb >= *best {
                return;
            }

            // try beneficial swaps that place correct character at position i
            let mut found = false;
            for j in (i + 1)..n {
                if cur[j] == target[i] && cur[j] != target[j] {
                    found = true;
                    cur.swap(i, j);
                    dfs(cur, i + 1, swaps + 1, target, best);
                    cur.swap(i, j);
                }
            }

            // fallback: swap with any mismatched position if no beneficial swap
            if !found {
                for j in (i + 1)..n {
                    if cur[j] != target[j] {
                        cur.swap(i, j);
                        dfs(cur, i + 1, swaps + 1, target, best);
                        cur.swap(i, j);
                    }
                }
            }
        }

        let mut cur: Vec<char> = s1.chars().collect();
        let target: Vec<char> = s2.chars().collect();
        let mut best = i32::MAX;
        dfs(&mut cur, 0, 0, &target, &mut best);
        best
    }
}
```

## Racket

```racket
(require racket/queue)

(define (swap-str s i j)
  (let* ((v (string->vector s))
         (tmp (vector-ref v i)))
    (vector-set! v i (vector-ref v j))
    (vector-set! v j tmp)
    (vector->string v)))

(define/contract (k-similarity s1 s2)
  (-> string? string? exact-integer?)
  (let* ((n (string-length s1))
         (target s2)
         (visited (make-hash))
         (q (make-queue)))
    (hash-set! visited s1 0)
    (enqueue! q s1)
    (let bfs ()
      (if (queue-empty? q)
          -1 ; should never happen
          (let* ((cur (dequeue! q))
                 (dist (hash-ref visited cur)))
            (if (string=? cur target)
                dist
                (begin
                  ;; find first mismatched index
                  (define i
                    (let loop ((idx 0))
                      (cond [(= idx n) #f]
                            [(char=? (string-ref cur idx) (string-ref target idx)) (loop (+ idx 1))]
                            [else idx])))
                  (when i
                    (for ([j (in-range (+ i 1) n)])
                      (let* ((c-j (string-ref cur j))
                             (need (string-ref target i)))
                        (when (and (char=? c-j need)
                                   (not (char=? c-j (string-ref target j))))
                          (let ((next (swap-str cur i j)))
                            (unless (hash-has-key? visited next)
                              (hash-set! visited next (+ dist 1))
                              (enqueue! q next)))))))
                  (bfs)))))))))
```

## Erlang

```erlang
-module(solution).
-export([k_similarity/2]).

-spec k_similarity(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> integer().
k_similarity(S1, S2) ->
    L1 = unicode:characters_to_list(S1),
    L2 = unicode:characters_to_list(S2),
    case L1 == L2 of
        true -> 0;
        false ->
            Q0 = queue:new(),
            Q1 = queue:in({L1, 0}, Q0),
            Visited0 = maps:put(L1, true, #{}),
            bfs(Q1, Visited0, L2)
    end.

%% BFS loop
bfs(Queue, Visited, Target) ->
    case queue:out(Queue) of
        {empty, _} -> -1; % should never happen for valid inputs
        {{State, Dist}, RestQueue} ->
            case State == Target of
                true -> Dist;
                false ->
                    Neighbors = gen_neighbors(State, Target),
                    {NewQueue, NewVisited} = enqueue_new(Neighbors, Dist + 1, RestQueue, Visited),
                    bfs(NewQueue, NewVisited, Target)
            end
    end.

%% Enqueue unseen neighbor states
enqueue_new([], _Dist, Queue, Visited) ->
    {Queue, Visited};
enqueue_new([N | Ns], Dist, Queue, Visited) ->
    case maps:is_key(N, Visited) of
        true ->
            enqueue_new(Ns, Dist, Queue, Visited);
        false ->
            Q1 = queue:in({N, Dist}, Queue),
            V1 = maps:put(N, true, Visited),
            enqueue_new(Ns, Dist, Q1, V1)
    end.

%% Generate neighbor states by swapping the first mismatched position with a suitable later one
gen_neighbors(State, Target) ->
    case first_mismatch(State, Target, 0) of
        undefined -> [];
        I ->
            Char = lists:nth(I + 1, Target),
            gen_swaps(State, Target, I, Char, [])
    end.

%% Find first index where two lists differ (0‑based)
first_mismatch([], [], _Idx) ->
    undefined;
first_mismatch([H | T], [HT | TT], Idx) ->
    case H =:= HT of
        true -> first_mismatch(T, TT, Idx + 1);
        false -> Idx
    end.

%% Generate all swaps fixing position I
gen_swaps(State, Target, I, Char, Acc) ->
    gen_swaps_helper(State, Target, I, Char, 0, Acc).

gen_swaps_helper([], _Target, _I, _Char, _Pos, Acc) ->
    lists:reverse(Acc);
gen_swaps_helper([H | T], Target, I, Char, Pos, Acc) ->
    NewAcc =
        if
            Pos > I,
            H =:= Char,
            (lists:nth(Pos + 1, Target)) =/= Char ->
                Swapped = swap(State, I, Pos),
                [Swapped | Acc];
            true -> Acc
        end,
    gen_swaps_helper(T, Target, I, Char, Pos + 1, NewAcc).

%% Swap elements at positions I and J (0‑based) in a list
swap(List, I, J) ->
    ElemI = lists:nth(I + 1, List),
    ElemJ = lists:nth(J + 1, List),
    swap_helper(List, 0, I, J, ElemI, ElemJ).

swap_helper([], _Pos, _I, _J, _EI, _EJ) ->
    [];
swap_helper([H | T], Pos, I, J, EI, EJ) ->
    NewElem =
        case Pos of
            I -> EJ;
            J -> EI;
            _ -> H
        end,
    [NewElem | swap_helper(T, Pos + 1, I, J, EI, EJ)].
```

## Elixir

```elixir
defmodule Solution do
  @spec k_similarity(String.t(), String.t()) :: integer
  def k_similarity(s1, s2) do
    if s1 == s2, do: 0, else bfs(s1, s2)
  end

  defp bfs(start, target) do
    queue = :queue.new() |> :queue.in({start, 0})
    visited = MapSet.new([start])
    bfs_loop(queue, visited, target)
  end

  defp bfs_loop(queue, visited, target) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{state, steps}, q} ->
        if state == target do
          steps
        else
          neigh = neighbors(state, target)

          {new_queue, new_visited} =
            Enum.reduce(neigh, {q, visited}, fn nb, {q_acc, vis_acc} ->
              if MapSet.member?(vis_acc, nb) do
                {q_acc, vis_acc}
              else
                {:queue.in({nb, steps + 1}, q_acc), MapSet.put(vis_acc, nb)}
              end
            end)

          bfs_loop(new_queue, new_visited, target)
        end
    end
  end

  defp neighbors(state, target) do
    s = String.to_charlist(state)
    t = String.to_charlist(target)
    len = length(s)

    i = find_mismatch_index(s, t, 0, len)

    if i == nil do
      []
    else
      Enum.reduce((i + 1)..(len - 1), [], fn j, acc ->
        cond do
          :lists.nth(j + 1, s) == :lists.nth(i + 1, t) and
              :lists.nth(j + 1, s) != :lists.nth(j + 1, t) ->
            new_s = swap(s, i, j)
            [List.to_string(new_s) | acc]

          true ->
            acc
        end
      end)
    end
  end

  defp find_mismatch_index(_s, _t, idx, len) when idx >= len, do: nil

  defp find_mismatch_index(s, t, idx, len) do
    if :lists.nth(idx + 1, s) != :lists.nth(idx + 1, t) do
      idx
    else
      find_mismatch_index(s, t, idx + 1, len)
    end
  end

  defp swap(list, i, j) do
    vi = :lists.nth(i + 1, list)
    vj = :lists.nth(j + 1, list)

    list
    |> List.replace_at(i, vj)
    |> List.replace_at(j, vi)
  end
end
```
