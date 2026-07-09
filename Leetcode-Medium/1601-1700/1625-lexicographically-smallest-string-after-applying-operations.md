# 1625. Lexicographically Smallest String After Applying Operations

## Cpp

```cpp
class Solution {
public:
    string findLexSmallestString(string s, int a, int b) {
        int n = s.size();
        unordered_set<string> visited;
        string best = s;
        function<void(const string&)> dfs = [&](const string& cur) {
            if (visited.count(cur)) return;
            visited.insert(cur);
            if (cur < best) best = cur;
            // operation 1: add a to all odd indices (0‑based)
            string added = cur;
            for (int i = 1; i < n; i += 2) {
                added[i] = char((added[i] - '0' + a) % 10 + '0');
            }
            dfs(added);
            // operation 2: rotate right by b
            string rotated = cur.substr(n - b) + cur.substr(0, n - b);
            dfs(rotated);
        };
        dfs(s);
        return best;
    }
};
```

## Java

```java
class Solution {
    public String findLexSmallestString(String s, int a, int b) {
        Set<String> visited = new HashSet<>();
        Deque<String> queue = new ArrayDeque<>();
        visited.add(s);
        queue.offer(s);
        String ans = s;
        while (!queue.isEmpty()) {
            String cur = queue.poll();
            if (cur.compareTo(ans) < 0) ans = cur;

            String added = add(cur, a);
            if (visited.add(added)) queue.offer(added);

            String rotated = rotate(cur, b);
            if (visited.add(rotated)) queue.offer(rotated);
        }
        return ans;
    }

    private String add(String s, int a) {
        char[] ch = s.toCharArray();
        for (int i = 1; i < ch.length; i += 2) {
            int d = ch[i] - '0';
            d = (d + a) % 10;
            ch[i] = (char) ('0' + d);
        }
        return new String(ch);
    }

    private String rotate(String s, int b) {
        int n = s.length();
        int shift = b % n;
        if (shift == 0) return s;
        return s.substring(n - shift) + s.substring(0, n - shift);
    }
}
```

## Python

```python
class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        from collections import deque

        def add_op(st):
            lst = list(st)
            for i in range(1, len(lst), 2):
                lst[i] = str((int(lst[i]) + a) % 10)
            return ''.join(lst)

        def rot_op(st):
            return st[-b:] + st[:-b]

        visited = set()
        q = deque([s])
        visited.add(s)
        best = s

        while q:
            cur = q.popleft()
            if cur < best:
                best = cur
            # operation 1: add a to odd indices
            nxt1 = add_op(cur)
            if nxt1 not in visited:
                visited.add(nxt1)
                q.append(nxt1)
            # operation 2: rotate by b
            nxt2 = rot_op(cur)
            if nxt2 not in visited:
                visited.add(nxt2)
                q.append(nxt2)

        return best
```

## Python3

```python
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        from collections import deque

        n = len(s)
        visited = set([s])
        q = deque([s])
        best = s

        while q:
            cur = q.popleft()
            if cur < best:
                best = cur

            # operation 1: add a to all odd indices (0-indexed)
            lst = list(cur)
            for i in range(1, n, 2):
                lst[i] = str((int(lst[i]) + a) % 10)
            added = ''.join(lst)
            if added not in visited:
                visited.add(added)
                q.append(added)

            # operation 2: rotate right by b positions
            rot = cur[-b:] + cur[:-b]
            if rot not in visited:
                visited.add(rot)
                q.append(rot)

        return best
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* findLexSmallestString(char* s, int a, int b) {
    int n = strlen(s);
    int capacity = 2000; // sufficient for all possible states
    char **visited = (char**)malloc(capacity * sizeof(char*));
    char **queue   = (char**)malloc(capacity * sizeof(char*));
    int visitedCnt = 0, head = 0, tail = 0;

    // helper to check if a string was already visited
    #define IS_VISITED(str) ({ \
        int _found = 0; \
        for (int _i = 0; _i < visitedCnt; ++_i) { \
            if (strcmp((str), visited[_i]) == 0) { _found = 1; break; } \
        } \
        _found; })
    
    // add initial string to structures
    char *init = (char*)malloc(n + 1);
    strcpy(init, s);
    visited[visitedCnt++] = init;
    queue[tail++] = init;

    char *best = (char*)malloc(n + 1);
    strcpy(best, s);

    while (head < tail) {
        char *cur = queue[head++];
        if (strcmp(cur, best) < 0) {
            strcpy(best, cur);
        }

        // operation 1: add a to all odd indices
        char *addStr = (char*)malloc(n + 1);
        memcpy(addStr, cur, n + 1);
        for (int i = 1; i < n; i += 2) {
            int d = addStr[i] - '0';
            d = (d + a) % 10;
            addStr[i] = (char)(d + '0');
        }
        if (!IS_VISITED(addStr)) {
            visited[visitedCnt++] = addStr;
            queue[tail++] = addStr;
        } else {
            free(addStr);
        }

        // operation 2: rotate right by b positions
        char *rotStr = (char*)malloc(n + 1);
        for (int i = 0; i < n; ++i) {
            rotStr[(i + b) % n] = cur[i];
        }
        rotStr[n] = '\0';
        if (!IS_VISITED(rotStr)) {
            visited[visitedCnt++] = rotStr;
            queue[tail++] = rotStr;
        } else {
            free(rotStr);
        }
    }

    // clean up visited strings except the best one (which we will return)
    for (int i = 0; i < visitedCnt; ++i) {
        if (visited[i] != best) free(visited[i]);
    }
    free(visited);
    free(queue);
    return best;
}
```

## Csharp

```csharp
public class Solution
{
    public string FindLexSmallestString(string s, int a, int b)
    {
        var n = s.Length;
        var visited = new HashSet<string>();
        var queue = new Queue<string>();
        queue.Enqueue(s);
        visited.Add(s);
        var best = s;

        while (queue.Count > 0)
        {
            var cur = queue.Dequeue();
            if (string.Compare(cur, best) < 0)
                best = cur;

            // operation 1: add a to digits at odd indices (0-indexed)
            char[] added = cur.ToCharArray();
            for (int i = 1; i < n; i += 2)
            {
                int d = (added[i] - '0' + a) % 10;
                added[i] = (char)('0' + d);
            }
            var addStr = new string(added);
            if (!visited.Contains(addStr))
            {
                visited.Add(addStr);
                queue.Enqueue(addStr);
            }

            // operation 2: rotate right by b positions
            int rot = b % n;
            var rotStr = cur.Substring(n - rot) + cur.Substring(0, n - rot);
            if (!visited.Contains(rotStr))
            {
                visited.Add(rotStr);
                queue.Enqueue(rotStr);
            }
        }

        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} a
 * @param {number} b
 * @return {string}
 */
var findLexSmallestString = function(s, a, b) {
    const n = s.length;
    const visited = new Set();
    let ans = s;
    const queue = [s];
    visited.add(s);
    for (let i = 0; i < queue.length; i++) {
        const cur = queue[i];
        if (cur < ans) ans = cur;

        // Operation 1: add a to digits at odd indices
        const chars = cur.split('');
        for (let j = 1; j < n; j += 2) {
            chars[j] = ((parseInt(chars[j], 10) + a) % 10).toString();
        }
        const added = chars.join('');
        if (!visited.has(added)) {
            visited.add(added);
            queue.push(added);
        }

        // Operation 2: rotate right by b positions
        const rotated = cur.slice(n - b) + cur.slice(0, n - b);
        if (!visited.has(rotated)) {
            visited.add(rotated);
            queue.push(rotated);
        }
    }
    return ans;
};
```

## Typescript

```typescript
function findLexSmallestString(s: string, a: number, b: number): string {
    const n = s.length;
    const visited = new Set<string>();
    let best = s;

    const queue: string[] = [];
    queue.push(s);
    visited.add(s);

    for (let q = 0; q < queue.length; ++q) {
        const cur = queue[q];
        if (cur < best) best = cur;

        // Operation 1: add a to all digits at odd indices (0‑based)
        const charsAdd = cur.split('');
        for (let i = 1; i < n; i += 2) {
            const d = (parseInt(charsAdd[i]) + a) % 10;
            charsAdd[i] = d.toString();
        }
        const added = charsAdd.join('');
        if (!visited.has(added)) {
            visited.add(added);
            queue.push(added);
        }

        // Operation 2: rotate right by b positions
        const rotated = cur.slice(n - b) + cur.slice(0, n - b);
        if (!visited.has(rotated)) {
            visited.add(rotated);
            queue.push(rotated);
        }
    }

    return best;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @param Integer $a
     * @param Integer $b
     * @return String
     */
    function findLexSmallestString($s, $a, $b) {
        $n = strlen($s);
        $visited = [];
        $queue = new SplQueue();
        $queue->enqueue($s);
        $visited[$s] = true;
        $best = $s;

        while (!$queue->isEmpty()) {
            $cur = $queue->dequeue();

            if (strcmp($cur, $best) < 0) {
                $best = $cur;
            }

            // Operation 1: add a to all digits at odd indices
            $chars = str_split($cur);
            for ($i = 1; $i < $n; $i += 2) {
                $digit = (int)$chars[$i];
                $digit = ($digit + $a) % 10;
                $chars[$i] = (string)$digit;
            }
            $nextAdd = implode('', $chars);
            if (!isset($visited[$nextAdd])) {
                $visited[$nextAdd] = true;
                $queue->enqueue($nextAdd);
            }

            // Operation 2: rotate right by b positions
            $bmod = $b % $n;
            $nextRotate = substr($cur, $n - $bmod) . substr($cur, 0, $n - $bmod);
            if (!isset($visited[$nextRotate])) {
                $visited[$nextRotate] = true;
                $queue->enqueue($nextRotate);
            }
        }

        return $best;
    }
}
```

## Swift

```swift
class Solution {
    func findLexSmallestString(_ s: String, _ a: Int, _ b: Int) -> String {
        var visited = Set<String>()
        var queue = [String]()
        visited.insert(s)
        queue.append(s)
        var best = s
        var idx = 0
        while idx < queue.count {
            let cur = queue[idx]
            idx += 1
            if cur < best { best = cur }
            
            // Operation 1: add a to digits at odd indices (0‑based)
            var chars = Array(cur)
            for i in stride(from: 1, to: chars.count, by: 2) {
                if let val = chars[i].wholeNumberValue {
                    let newVal = (val + a) % 10
                    chars[i] = Character("\(newVal)")
                }
            }
            let added = String(chars)
            if !visited.contains(added) {
                visited.insert(added)
                queue.append(added)
            }
            
            // Operation 2: rotate right by b positions
            let n = cur.count
            let rotated = String(cur.suffix(b)) + String(cur.prefix(n - b))
            if !visited.contains(rotated) {
                visited.insert(rotated)
                queue.append(rotated)
            }
        }
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findLexSmallestString(s: String, a: Int, b: Int): String {
        val n = s.length
        val visited = HashSet<String>()
        val queue: ArrayDeque<String> = ArrayDeque()
        visited.add(s)
        queue.add(s)
        var answer = s

        while (queue.isNotEmpty()) {
            val cur = queue.removeFirst()
            if (cur < answer) answer = cur

            // Operation 1: add a to all odd indices
            val sbAdd = StringBuilder(cur)
            for (i in cur.indices) {
                if (i % 2 == 1) {
                    val newDigit = ((cur[i] - '0' + a) % 10) + '0'.code
                    sbAdd.setCharAt(i, newDigit.toChar())
                }
            }
            val added = sbAdd.toString()
            if (added !in visited) {
                visited.add(added)
                queue.add(added)
            }

            // Operation 2: rotate right by b positions
            val shift = b % n
            val rotated = if (shift == 0) cur else cur.substring(n - shift) + cur.substring(0, n - shift)
            if (rotated !in visited) {
                visited.add(rotated)
                queue.add(rotated)
            }
        }

        return answer
    }
}
```

## Dart

```dart
class Solution {
  String findLexSmallestString(String s, int a, int b) {
    final n = s.length;
    final Set<String> visited = {s};
    final List<String> queue = [s];
    String best = s;

    for (int idx = 0; idx < queue.length; idx++) {
      final cur = queue[idx];
      if (cur.compareTo(best) < 0) best = cur;

      // Operation 1: add a to digits at odd indices (0‑based)
      final List<int> addedChars = List.filled(n, 0);
      for (int i = 0; i < n; i++) {
        int d = cur.codeUnitAt(i) - 48;
        if (i.isOdd) d = (d + a) % 10;
        addedChars[i] = d + 48;
      }
      final String added = String.fromCharCodes(addedChars);
      if (!visited.contains(added)) {
        visited.add(added);
        queue.add(added);
      }

      // Operation 2: rotate right by b positions
      final int rot = b % n;
      final String rotated = cur.substring(n - rot) + cur.substring(0, n - rot);
      if (!visited.contains(rotated)) {
        visited.add(rotated);
        queue.add(rotated);
      }
    }

    return best;
  }
}
```

## Golang

```go
func findLexSmallestString(s string, a int, b int) string {
	n := len(s)
	visited := make(map[string]bool)
	queue := []string{s}
	visited[s] = true
	ans := s

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]

		if cur < ans {
			ans = cur
		}

		// Operation 1: add a to all digits at odd indices (0‑based)
		bs := []byte(cur)
		for i := 1; i < n; i += 2 {
			d := (int(bs[i]-'0') + a) % 10
			bs[i] = byte(d) + '0'
		}
		nextAdd := string(bs)
		if !visited[nextAdd] {
			visited[nextAdd] = true
			queue = append(queue, nextAdd)
		}

		// Operation 2: rotate right by b positions
		rotated := cur[n-b:] + cur[:n-b]
		if !visited[rotated] {
			visited[rotated] = true
			queue = append(queue, rotated)
		}
	}
	return ans
}
```

## Ruby

```ruby
def find_lex_smallest_string(s, a, b)
  visited = {}
  queue = [s]
  visited[s] = true
  min_str = s

  while (cur = queue.shift)
    min_str = cur if cur < min_str

    # Operation 1: add 'a' to every digit at odd indices (0‑based)
    chars = cur.chars
    i = 1
    while i < chars.length
      digits = chars[i].ord - 48
      chars[i] = ((digits + a) % 10).to_s
      i += 2
    end
    added = chars.join
    unless visited[added]
      visited[added] = true
      queue << added
    end

    # Operation 2: rotate right by 'b' positions
    rotated = cur[-b, b] + cur[0...-b]
    unless visited[rotated]
      visited[rotated] = true
      queue << rotated
    end
  end

  min_str
end
```

## Scala

```scala
object Solution {
  def findLexSmallestString(s: String, a: Int, b: Int): String = {
    val n = s.length
    val visited = scala.collection.mutable.HashSet[String]()
    val queue = scala.collection.mutable.Queue[String]()
    visited += s
    queue.enqueue(s)
    var best = s

    while (queue.nonEmpty) {
      val cur = queue.dequeue()
      if (cur < best) best = cur

      // Operation 1: add a to digits at odd indices
      val sbAdd = new StringBuilder(cur)
      for (i <- 0 until n if i % 2 == 1) {
        val d = ((cur.charAt(i) - '0' + a) % 10).toInt
        sbAdd.setCharAt(i, (d + '0').toChar)
      }
      val added = sbAdd.toString()
      if (!visited.contains(added)) {
        visited += added
        queue.enqueue(added)
      }

      // Operation 2: rotate right by b positions
      val k = b % n
      val rotated = cur.substring(n - k) + cur.substring(0, n - k)
      if (!visited.contains(rotated)) {
        visited += rotated
        queue.enqueue(rotated)
      }
    }

    best
  }
}
```

## Rust

```rust
use std::collections::{HashSet, VecDeque};

pub struct Solution;

impl Solution {
    pub fn find_lex_smallest_string(s: String, a: i32, b: i32) -> String {
        let len = s.len();
        let rot = b as usize % len;
        let mut visited: HashSet<String> = HashSet::new();
        let mut queue: VecDeque<String> = VecDeque::new();
        queue.push_back(s.clone());
        let mut best = s;

        while let Some(cur) = queue.pop_front() {
            if !visited.insert(cur.clone()) {
                continue;
            }
            if cur < best {
                best = cur.clone();
            }

            // Operation 1: add a to all digits at odd indices (0‑based)
            let mut bytes: Vec<u8> = cur.bytes().collect();
            for i in (1..len).step_by(2) {
                let d = bytes[i] - b'0';
                let nd = ((d as i32 + a) % 10) as u8;
                bytes[i] = b'0' + nd;
            }
            let added = String::from_utf8(bytes).unwrap();
            if !visited.contains(&added) {
                queue.push_back(added);
            }

            // Operation 2: rotate right by b positions
            let split = len - rot;
            let rotated = format!("{}{}", &cur[split..], &cur[..split]);
            if !visited.contains(&rotated) {
                queue.push_back(rotated);
            }
        }

        best
    }
}
```

## Racket

```racket
(define/contract (find-lex-smallest-string s a b)
  (-> string? exact-integer? exact-integer? string?)
  (let* ((n (string-length s))
         (bmod (remainder b n)))
    (define (rotate str)
      (if (= bmod 0)
          str
          (let ((part1 (substring str (- n bmod) n))
                (part2 (substring str 0 (- n bmod))))
            (string-append part1 part2))))
    (define (add-op str)
      (let loop ((i 0) (acc '()))
        (if (= i n)
            (list->string (reverse acc))
            (let* ((ch (string-ref str i))
                   (digit (- (char->integer ch) (char->integer #\0)))
                   (new-digit (if (odd? i)
                                  (remainder (+ digit a) 10)
                                  digit))
                   (new-ch (integer->char (+ new-digit (char->integer #\0)))))
              (loop (add1 i) (cons new-ch acc))))))
    (define visited (make-hash))
    (define best (box s))
    (define (update-best str)
      (when (string<? str (unbox best))
        (set-box! best str)))
    (letrec ((dfs
              (lambda (cur)
                (unless (hash-has-key? visited cur)
                  (hash-set! visited cur #t)
                  (update-best cur)
                  (dfs (rotate cur))
                  (dfs (add-op cur))))))
      (dfs s)
      (unbox best))))
```

## Erlang

```erlang
-spec find_lex_smallest_string(S :: unicode:unicode_binary(), A :: integer(), B :: integer()) -> unicode:unicode_binary().
find_lex_smallest_string(S, A, B) ->
    bfs([S], maps:from_list([{S,true}]), S, A, B).

bfs([], _Visited, MinStr, _A, _B) ->
    MinStr;
bfs([Curr|RestQueue], Visited, MinStr, A, B) ->
    Rot = rotate(Curr, B),
    Add = add_op(Curr, A),

    {Visited1, Queue1} = maybe_enqueue(Rot, Visited, RestQueue),
    {Visited2, Queue2} = maybe_enqueue(Add, Visited1, Queue1),

    NewMin = case binary:compare(Rot, MinStr) of
                less -> Rot;
                _ ->
                    case binary:compare(Add, MinStr) of
                        less -> Add;
                        _ -> MinStr
                    end
            end,
    bfs(Queue2, Visited2, NewMin, A, B).

maybe_enqueue(Str, Visited, Queue) ->
    case maps:is_key(Str, Visited) of
        true -> {Visited, Queue};
        false -> {maps:put(Str, true, Visited), Queue ++ [Str]}
    end.

rotate(S, B) ->
    L = byte_size(S),
    Bmod = B rem L,
    if Bmod == 0 ->
            S;
       true ->
            PrefixLen = L - Bmod,
            Prefix = binary:part(S, 0, PrefixLen),
            Suffix = binary:part(S, PrefixLen, Bmod),
            <<Suffix/binary, Prefix/binary>>
    end.

add_op(S, A) ->
    List = binary_to_list(S),
    NewListRev = add_op_list(List, A, 0, []),
    list_to_binary(lists:reverse(NewListRev)).

add_op_list([], _A, _Idx, Acc) ->
    Acc;
add_op_list([D|Rest], A, Idx, Acc) ->
    NewD = if
               (Idx rem 2) == 1 ->
                   ((D - $0 + A) rem 10) + $0;
               true ->
                   D
           end,
    add_op_list(Rest, A, Idx + 1, [NewD|Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_lex_smallest_string(s :: String.t(), a :: integer, b :: integer) :: String.t()
  def find_lex_smallest_string(s, a, b) do
    visited = MapSet.new([s])
    queue = :queue.in(s, :queue.new())
    bfs(queue, visited, a, b, s)
  end

  defp bfs(queue, visited, a, b, min_str) do
    case :queue.out(queue) do
      {:empty, _} ->
        min_str

      {{:value, cur}, q} ->
        new_min = if cur < min_str, do: cur, else: min_str

        added = add_op(cur, a)
        {q1, visited1} =
          if MapSet.member?(visited, added) do
            {q, visited}
          else
            {:queue.in(added, q), MapSet.put(visited, added)}
          end

        rotated = rot_op(cur, b)

        {q2, visited2} =
          if MapSet.member?(visited1, rotated) do
            {q1, visited1}
          else
            {:queue.in(rotated, q1), MapSet.put(visited1, rotated)}
          end

        bfs(q2, visited2, a, b, new_min)
    end
  end

  defp add_op(str, a) do
    str
    |> String.graphemes()
    |> Enum.with_index()
    |> Enum.map(fn {ch, idx} ->
      if rem(idx, 2) == 1 do
        ((String.to_integer(ch) + a) rem 10)
        |> Integer.to_string()
      else
        ch
      end
    end)
    |> Enum.join()
  end

  defp rot_op(str, b) do
    len = String.length(str)
    shift = rem(b, len)

    if shift == 0 do
      str
    else
      {head, tail} = String.split_at(str, len - shift)
      tail <> head
    end
  end
end
```
