# 1405. Longest Happy String

## Cpp

```cpp
class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        priority_queue<pair<int,char>> pq;
        if (a > 0) pq.emplace(a, 'a');
        if (b > 0) pq.emplace(b, 'b');
        if (c > 0) pq.emplace(c, 'c');
        string res;
        while (!pq.empty()) {
            auto [cnt1, ch1] = pq.top(); pq.pop();
            int n = res.size();
            if (n >= 2 && res[n-1] == ch1 && res[n-2] == ch1) {
                if (pq.empty()) break;
                auto [cnt2, ch2] = pq.top(); pq.pop();
                res.push_back(ch2);
                if (--cnt2 > 0) pq.emplace(cnt2, ch2);
                pq.emplace(cnt1, ch1);
            } else {
                res.push_back(ch1);
                if (--cnt1 > 0) pq.emplace(cnt1, ch1);
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    private static class Node {
        int cnt;
        char ch;
        Node(int cnt, char ch) {
            this.cnt = cnt;
            this.ch = ch;
        }
    }

    public String longestDiverseString(int a, int b, int c) {
        java.util.PriorityQueue<Node> pq = new java.util.PriorityQueue<>(
                (x, y) -> Integer.compare(y.cnt, x.cnt));
        if (a > 0) pq.offer(new Node(a, 'a'));
        if (b > 0) pq.offer(new Node(b, 'b'));
        if (c > 0) pq.offer(new Node(c, 'c'));

        StringBuilder sb = new StringBuilder();

        while (!pq.isEmpty()) {
            Node first = pq.poll();
            int len = sb.length();
            if (len >= 2 && sb.charAt(len - 1) == first.ch && sb.charAt(len - 2) == first.ch) {
                if (pq.isEmpty()) break;
                Node second = pq.poll();
                sb.append(second.ch);
                second.cnt--;
                if (second.cnt > 0) pq.offer(second);
                // put the first node back for future use
                pq.offer(first);
            } else {
                sb.append(first.ch);
                first.cnt--;
                if (first.cnt > 0) pq.offer(first);
            }
        }

        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        import heapq
        heap = []
        if a > 0:
            heap.append((-a, 'a'))
        if b > 0:
            heap.append((-b, 'b'))
        if c > 0:
            heap.append((-c, 'c'))
        heapq.heapify(heap)

        ans = []

        while heap:
            cnt1, ch1 = heapq.heappop(heap)
            cnt1 = -cnt1
            # If adding this char would cause three consecutive same chars
            if len(ans) >= 2 and ans[-1] == ans[-2] == ch1:
                if not heap:
                    break
                cnt2, ch2 = heapq.heappop(heap)
                cnt2 = -cnt2
                ans.append(ch2)
                cnt2 -= 1
                if cnt2 > 0:
                    heapq.heappush(heap, (-cnt2, ch2))
                # push back the first character unchanged
                heapq.heappush(heap, (-cnt1, ch1))
            else:
                # Add one occurrence of ch1
                ans.append(ch1)
                cnt1 -= 1
                # Try to add a second occurrence if still allowed
                if cnt1 > 0 and not (len(ans) >= 2 and ans[-1] == ans[-2] == ch1):
                    ans.append(ch1)
                    cnt1 -= 1
                if cnt1 > 0:
                    heapq.heappush(heap, (-cnt1, ch1))

        return ''.join(ans)
```

## Python3

```python
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        import heapq
        # max-heap using negative counts
        heap = []
        for cnt, ch in ((a, 'a'), (b, 'b'), (c, 'c')):
            if cnt > 0:
                heapq.heappush(heap, (-cnt, ch))
        res = []

        while heap:
            cnt1, ch1 = heapq.heappop(heap)
            # check if adding ch1 would cause three consecutive same chars
            if len(res) >= 2 and res[-1] == res[-2] == ch1:
                if not heap:
                    break  # no alternative character
                cnt2, ch2 = heapq.heappop(heap)
                # use second most frequent character
                res.append(ch2)
                cnt2 += 1  # since cnt are negative
                if cnt2 != 0:
                    heapq.heappush(heap, (cnt2, ch2))
                # push back the first character unchanged
                heapq.heappush(heap, (cnt1, ch1))
            else:
                # we can use ch1
                res.append(ch1)
                cnt1 += 1  # decrement count (remember negative)
                if cnt1 != 0:
                    heapq.heappush(heap, (cnt1, ch1))

        return ''.join(res)
```

## C

```c
#include <stdlib.h>

char* longestDiverseString(int a, int b, int c) {
    int cnt[3] = {a, b, c};
    const char ch[3] = {'a', 'b', 'c'};
    int total = a + b + c;
    char *res = (char *)malloc(total + 1);
    if (!res) return NULL;
    int pos = 0;

    while (1) {
        int i1 = -1, i2 = -1;
        for (int i = 0; i < 3; ++i) {
            if (cnt[i] > 0 && (i1 == -1 || cnt[i] > cnt[i1])) {
                i1 = i;
            }
        }
        if (i1 == -1) break; // no characters left

        if (pos >= 2 && res[pos - 1] == ch[i1] && res[pos - 2] == ch[i1]) {
            for (int i = 0; i < 3; ++i) {
                if (cnt[i] > 0 && i != i1 && (i2 == -1 || cnt[i] > cnt[i2])) {
                    i2 = i;
                }
            }
            if (i2 == -1) break; // cannot place any character without breaking rule
            res[pos++] = ch[i2];
            cnt[i2]--;
        } else {
            res[pos++] = ch[i1];
            cnt[i1]--;
        }
    }

    res[pos] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string LongestDiverseString(int a, int b, int c) {
        var cnt = new int[3] { a, b, c };
        var ch = new char[3] { 'a', 'b', 'c' };
        var sb = new System.Text.StringBuilder();

        while (true) {
            // find the character with maximum remaining count
            int first = -1;
            for (int i = 0; i < 3; i++) {
                if (cnt[i] > 0 && (first == -1 || cnt[i] > cnt[first])) {
                    first = i;
                }
            }
            if (first == -1) break; // no characters left

            int len = sb.Length;
            bool needAlternative = false;
            if (len >= 2 && sb[len - 1] == ch[first] && sb[len - 2] == ch[first]) {
                needAlternative = true;
            }

            if (!needAlternative) {
                sb.Append(ch[first]);
                cnt[first]--;
            } else {
                // pick the next best character
                int second = -1;
                for (int i = 0; i < 3; i++) {
                    if (i == first || cnt[i] == 0) continue;
                    if (second == -1 || cnt[i] > cnt[second]) {
                        second = i;
                    }
                }
                if (second == -1) break; // cannot add any more characters without breaking the rule
                sb.Append(ch[second]);
                cnt[second]--;
            }
        }

        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {string}
 */
var longestDiverseString = function(a, b, c) {
    let result = '';
    while (true) {
        const candidates = [];
        if (a > 0) candidates.push([a, 'a']);
        if (b > 0) candidates.push([b, 'b']);
        if (c > 0) candidates.push([c, 'c']);
        if (candidates.length === 0) break;
        // sort by remaining count descending
        candidates.sort((x, y) => y[0] - x[0]);
        let placed = false;
        for (let i = 0; i < candidates.length; i++) {
            const ch = candidates[i][1];
            if (result.length >= 2 &&
                result[result.length - 1] === ch &&
                result[result.length - 2] === ch) {
                continue; // would create three consecutive same chars
            }
            // place this character
            result += ch;
            if (ch === 'a') a--;
            else if (ch === 'b') b--;
            else c--;
            placed = true;
            break;
        }
        if (!placed) break; // no valid character can be added
    }
    return result;
};
```

## Typescript

```typescript
function longestDiverseString(a: number, b: number, c: number): string {
    const result: string[] = [];
    while (true) {
        const candidates: [number, string][] = [];
        if (a > 0) candidates.push([a, 'a']);
        if (b > 0) candidates.push([b, 'b']);
        if (c > 0) candidates.push([c, 'c']);
        if (candidates.length === 0) break;
        candidates.sort((x, y) => y[0] - x[0]); // descending by count

        let placed = false;
        for (let i = 0; i < candidates.length; i++) {
            const [cnt, ch] = candidates[i];
            const n = result.length;
            if (n >= 2 && result[n - 1] === ch && result[n - 2] === ch) continue;
            // place this character
            result.push(ch);
            if (ch === 'a') a--;
            else if (ch === 'b') b--;
            else c--;
            placed = true;
            break;
        }
        if (!placed) break; // cannot place any more characters without breaking rule
    }
    return result.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return String
     */
    function longestDiverseString($a, $b, $c) {
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_BOTH);

        if ($a > 0) $pq->insert(['a', $a], $a);
        if ($b > 0) $pq->insert(['b', $b], $b);
        if ($c > 0) $pq->insert(['c', $c], $c);

        $ans = '';

        while (!$pq->isEmpty()) {
            $first = $pq->extract();
            $char1 = $first['data'][0];
            $cnt1  = $first['data'][1];

            $len = strlen($ans);
            if ($len >= 2 && $ans[$len - 1] === $char1 && $ans[$len - 2] === $char1) {
                // need to use second most frequent character
                if ($pq->isEmpty()) {
                    break; // cannot add more characters without breaking rule
                }
                $second = $pq->extract();
                $char2 = $second['data'][0];
                $cnt2  = $second['data'][1];

                $ans .= $char2;
                $cnt2--;
                if ($cnt2 > 0) {
                    $pq->insert([$char2, $cnt2], $cnt2);
                }
                // push back the first character unchanged
                $pq->insert([$char1, $cnt1], $cnt1);
            } else {
                $ans .= $char1;
                $cnt1--;
                if ($cnt1 > 0) {
                    $pq->insert([$char1, $cnt1], $cnt1);
                }
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func longestDiverseString(_ a: Int, _ b: Int, _ c: Int) -> String {
        var heap: [(Int, Character)] = []
        if a > 0 { heap.append((a, "a")) }
        if b > 0 { heap.append((b, "b")) }
        if c > 0 { heap.append((c, "c")) }
        
        var result = ""
        var last1: Character? = nil
        var last2: Character? = nil
        
        while !heap.isEmpty {
            // sort descending by remaining count (heap size ≤ 3)
            heap.sort { $0.0 > $1.0 }
            
            let (cnt1, ch1) = heap[0]
            if let l1 = last1, let l2 = last2, l1 == ch1 && l2 == ch1 {
                // cannot use the most frequent character now
                if heap.count < 2 { break } // no alternative
                let (cnt2, ch2) = heap[1]
                
                // append second most frequent character
                result.append(ch2)
                last2 = last1
                last1 = ch2
                
                // update heap for the used character
                heap.remove(at: 1)
                if cnt2 - 1 > 0 {
                    heap.append((cnt2 - 1, ch2))
                }
            } else {
                // use most frequent character
                result.append(ch1)
                last2 = last1
                last1 = ch1
                
                heap.remove(at: 0)
                if cnt1 - 1 > 0 {
                    heap.append((cnt1 - 1, ch1))
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
    fun longestDiverseString(a: Int, b: Int, c: Int): String {
        val pq = java.util.PriorityQueue<Node> { o1, o2 -> o2.count - o1.count }
        if (a > 0) pq.offer(Node(a, 'a'))
        if (b > 0) pq.offer(Node(b, 'b'))
        if (c > 0) pq.offer(Node(c, 'c'))

        val sb = StringBuilder()
        while (!pq.isEmpty()) {
            val first = pq.poll()
            val len = sb.length
            if (len >= 2 && sb[len - 1] == first.ch && sb[len - 2] == first.ch) {
                if (pq.isEmpty()) break
                val second = pq.poll()
                sb.append(second.ch)
                second.count--
                if (second.count > 0) pq.offer(second)
                pq.offer(first)
            } else {
                sb.append(first.ch)
                first.count--
                if (first.count > 0) pq.offer(first)
            }
        }
        return sb.toString()
    }

    private data class Node(var count: Int, val ch: Char)
}
```

## Dart

```dart
class Solution {
  String longestDiverseString(int a, int b, int c) {
    var counts = [
      [a, 'a'],
      [b, 'b'],
      [c, 'c']
    ];
    var result = StringBuffer();

    while (true) {
      // sort by remaining count descending
      counts.sort((p1, p2) => (p2[0] as int) - (p1[0] as int));

      bool added = false;
      for (int i = 0; i < 3; i++) {
        int cnt = counts[i][0] as int;
        String ch = counts[i][1] as String;
        if (cnt == 0) continue;

        int len = result.length;
        if (len >= 2 &&
            result[len - 1] == ch &&
            result[len - 2] == ch) {
          // would create three consecutive same chars, try next character
          continue;
        }

        // add this character
        result.write(ch);
        counts[i][0] = cnt - 1;
        added = true;
        break;
      }

      if (!added) break; // no character can be appended without breaking the rule
    }

    return result.toString();
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type item struct {
	cnt int
	ch  byte
}

// max-heap based on cnt
type maxHeap []item

func (h maxHeap) Len() int            { return len(h) }
func (h maxHeap) Less(i, j int) bool  { return h[i].cnt > h[j].cnt } // larger count first
func (h maxHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *maxHeap) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *maxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

func longestDiverseString(a int, b int, c int) string {
	h := &maxHeap{}
	if a > 0 {
		heap.Push(h, item{a, 'a'})
	}
	if b > 0 {
		heap.Push(h, item{b, 'b'})
	}
	if c > 0 {
		heap.Push(h, item{c, 'c'})
	}

	res := make([]byte, 0, a+b+c)

	for h.Len() > 0 {
		first := heap.Pop(h).(item)
		n := len(res)
		if n >= 2 && res[n-1] == first.ch && res[n-2] == first.ch {
			// need to use the next most frequent character
			if h.Len() == 0 {
				break // cannot place any more characters
			}
			second := heap.Pop(h).(item)
			res = append(res, second.ch)
			second.cnt--
			if second.cnt > 0 {
				heap.Push(h, second)
			}
			// put the first character back for later use
			heap.Push(h, first)
		} else {
			// safe to add this character
			res = append(res, first.ch)
			first.cnt--
			if first.cnt > 0 {
				heap.Push(h, first)
			}
		}
	}

	return string(res)
}
```

## Ruby

```ruby
# @param {Integer} a
# @param {Integer} b
# @param {Integer} c
# @return {String}
def longest_diverse_string(a, b, c)
  result = ''
  counts = [['a', a], ['b', b], ['c', c]]

  loop do
    # sort by remaining count descending
    counts.sort_by! { |_, cnt| -cnt }
    placed = false

    counts.each_with_index do |(ch, cnt), idx|
      next if cnt == 0
      # avoid three consecutive same characters
      if result.length >= 2 && result[-1] == ch && result[-2] == ch
        next
      end
      result << ch
      counts[idx][1] = cnt - 1
      placed = true
      break
    end

    break unless placed
  end

  result
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable.PriorityQueue

  def longestDiverseString(a: Int, b: Int, c: Int): String = {
    val pq = PriorityQueue.empty[(Int, Char)](Ordering.by[(Int, Char), Int](_._1))
    if (a > 0) pq.enqueue((a, 'a'))
    if (b > 0) pq.enqueue((b, 'b'))
    if (c > 0) pq.enqueue((c, 'c'))

    val sb = new StringBuilder

    while (pq.nonEmpty) {
      val top = pq.dequeue()
      val len = sb.length
      if (len >= 2 && sb.charAt(len - 1) == top._2 && sb.charAt(len - 2) == top._2) {
        if (pq.isEmpty) return sb.toString()
        val second = pq.dequeue()
        sb.append(second._2)
        if (second._1 - 1 > 0) pq.enqueue((second._1 - 1, second._2))
        pq.enqueue(top)
      } else {
        sb.append(top._2)
        if (top._1 - 1 > 0) pq.enqueue((top._1 - 1, top._2))
      }
    }

    sb.toString()
  }
}
```

## Rust

```rust
use std::collections::BinaryHeap;

impl Solution {
    pub fn longest_diverse_string(a: i32, b: i32, c: i32) -> String {
        let mut heap = BinaryHeap::new();
        if a > 0 { heap.push((a, 'a')); }
        if b > 0 { heap.push((b, 'b')); }
        if c > 0 { heap.push((c, 'c')); }

        let mut result = String::new();

        while let Some((cnt1, ch1)) = heap.pop() {
            let len = result.len();
            let need_alternate = if len >= 2 {
                let bytes = result.as_bytes();
                bytes[len - 1] as char == ch1 && bytes[len - 2] as char == ch1
            } else {
                false
            };

            if need_alternate {
                if let Some((cnt2, ch2)) = heap.pop() {
                    result.push(ch2);
                    if cnt2 > 1 {
                        heap.push((cnt2 - 1, ch2));
                    }
                    // put the first character back unchanged
                    heap.push((cnt1, ch1));
                } else {
                    break;
                }
            } else {
                result.push(ch1);
                if cnt1 > 1 {
                    heap.push((cnt1 - 1, ch1));
                }
            }
        }

        result
    }
}
```

## Racket

```racket
(require racket/list)

(define/contract (longest-diverse-string a b c)
  (-> exact-integer? exact-integer? exact-integer? string?)
  (letrec
      ((can-add?
        (lambda (lst ch)
          (if (< (length lst) 2)
              #t
              (let ([c1 (first lst)]
                    [c2 (second lst)])
                (not (and (char=? c1 ch) (char=? c2 ch)))))))
       (loop
        (lambda (counts result)
          (define nonzero
            (filter (lambda (p) (> (car p) 0)) counts))
          (if (null? nonzero)
              (list->string (reverse result))
              (let* ((sorted (sort nonzero > #:key car))
                     (first-pair (car sorted))
                     (char1 (cdr first-pair)))
                (if (can-add? result char1)
                    ;; use the most frequent character
                    (loop
                     (map (lambda (p)
                            (if (char=? (cdr p) char1)
                                (cons (sub1 (car p)) (cdr p))
                                p))
                          sorted)
                     (cons char1 result))
                    ;; need to try the second most frequent
                    (if (null? (cdr sorted))
                        (list->string (reverse result))
                        (let* ((second-pair (cadr sorted))
                               (char2 (cdr second-pair)))
                          (if (can-add? result char2)
                              (loop
                               (map (lambda (p)
                                      (if (char=? (cdr p) char2)
                                          (cons (sub1 (car p)) (cdr p))
                                          p))
                                    sorted)
                               (cons char2 result))
                              (list->string (reverse result))))))))))
    (loop (list (cons a #\a) (cons b #\b) (cons c #\c)) '())))))
```

## Erlang

```erlang
-spec longest_diverse_string(A :: integer(), B :: integer(), C :: integer()) -> unicode:unicode_binary().
longest_diverse_string(A, B, C) ->
    Counts0 = maybe_put(A, $a, maybe_put(B, $b, maybe_put(C, $c, []))),
    Result = build(Counts0, []),
    unicode:characters_to_binary(Result).

%% Build the longest happy string.
build([], Rev) -> lists:reverse(Rev);
build(Counts, Rev) ->
    Sorted = lists:sort(fun({C1,_},{C2,_}) -> C1 > C2 end, Counts),
    case Sorted of
        [] -> lists:reverse(Rev);
        [{Cnt1, Ch1}|Rest] ->
            case can_add(Ch1, Rev) of
                true ->
                    NewCounts = maybe_put(Cnt1-1, Ch1, Rest),
                    build(NewCounts, [Ch1|Rev]);
                false ->
                    case Rest of
                        [] -> lists:reverse(Rev);
                        [{Cnt2, Ch2}|Rest2] ->
                            case can_add(Ch2, Rev) of
                                true ->
                                    NewCounts = maybe_put(Cnt1, Ch1,
                                                          maybe_put(Cnt2-1, Ch2, Rest2)),
                                    build(NewCounts, [Ch2|Rev]);
                                false ->
                                    lists:reverse(Rev)
                            end
                    end
            end
    end.

%% Check if adding Char would create three consecutive identical chars.
can_add(Char, Rev) ->
    case Rev of
        [Char, Char | _] -> false;
        _ -> true
    end.

%% Insert a character with Count > 0 into the list.
maybe_put(Count, _, List) when Count =< 0 -> List;
maybe_put(Count, Char, List) -> [{Count, Char} | List].
```

## Elixir

```elixir
defmodule Solution do
  @spec longest_diverse_string(a :: integer, b :: integer, c :: integer) :: String.t()
  def longest_diverse_string(a, b, c) do
    counts = %{a: a, b: b, c: c}
    build(counts, [])
  end

  defp build(counts, acc) do
    sorted =
      counts
      |> Enum.filter(fn {_k, v} -> v > 0 end)
      |> Enum.sort_by(fn {_k, v} -> -v end)

    case sorted do
      [] ->
        acc
        |> Enum.reverse()
        |> Enum.map(&Atom.to_string/1)
        |> Enum.join()

      [{ch, _cnt} | rest] ->
        if can_use?(acc, ch) do
          new_counts = Map.update!(counts, ch, &(&1 - 1))
          build(new_counts, [ch | acc])
        else
          case rest do
            [] ->
              acc
              |> Enum.reverse()
              |> Enum.map(&Atom.to_string/1)
              |> Enum.join()

            [{ch2, _cnt2} | _] ->
              if can_use?(acc, ch2) do
                new_counts = Map.update!(counts, ch2, &(&1 - 1))
                build(new_counts, [ch2 | acc])
              else
                acc
                |> Enum.reverse()
                |> Enum.map(&Atom.to_string/1)
                |> Enum.join()
              end
          end
        end
    end
  end

  defp can_use?(acc, ch) do
    case acc do
      [c1, c2 | _] when c1 == ch and c2 == ch -> false
      _ -> true
    end
  end
end
```
