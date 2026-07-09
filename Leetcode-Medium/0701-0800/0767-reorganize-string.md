# 0767. Reorganize String

## Cpp

```cpp
class Solution {
public:
    string reorganizeString(string s) {
        int n = s.size();
        vector<int> cnt(26, 0);
        for (char c : s) cnt[c - 'a']++;
        int maxFreq = *max_element(cnt.begin(), cnt.end());
        if (maxFreq > (n + 1) / 2) return "";
        
        priority_queue<pair<int, char>> pq;
        for (int i = 0; i < 26; ++i) {
            if (cnt[i] > 0) pq.emplace(cnt[i], char('a' + i));
        }
        
        string result;
        while (pq.size() >= 2) {
            auto p1 = pq.top(); pq.pop();
            auto p2 = pq.top(); pq.pop();
            result.push_back(p1.second);
            result.push_back(p2.second);
            if (--p1.first > 0) pq.emplace(p1);
            if (--p2.first > 0) pq.emplace(p2);
        }
        if (!pq.empty()) {
            result.push_back(pq.top().second);
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public String reorganizeString(String s) {
        int n = s.length();
        int[] cnt = new int[26];
        for (char c : s.toCharArray()) cnt[c - 'a']++;
        for (int c : cnt) if (c > (n + 1) / 2) return "";
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[0] - a[0]); // [count, charIndex]
        for (int i = 0; i < 26; i++) {
            if (cnt[i] > 0) pq.offer(new int[]{cnt[i], i});
        }
        StringBuilder sb = new StringBuilder();
        while (pq.size() > 1) {
            int[] first = pq.poll();
            int[] second = pq.poll();
            sb.append((char) (first[1] + 'a'));
            sb.append((char) (second[1] + 'a'));
            if (--first[0] > 0) pq.offer(first);
            if (--second[0] > 0) pq.offer(second);
        }
        if (!pq.isEmpty()) {
            int[] last = pq.poll();
            sb.append((char) (last[1] + 'a'));
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        import heapq

        n = len(s)
        freq = Counter(s)
        if any(v > (n + 1) // 2 for v in freq.values()):
            return ""

        # max-heap based on counts (use negative counts)
        heap = [(-cnt, ch) for ch, cnt in freq.items()]
        heapq.heapify(heap)

        result = []
        prev_cnt, prev_ch = 0, ''
        while heap:
            cnt, ch = heapq.heappop(heap)
            result.append(ch)
            cnt += 1  # decrement the absolute count (cnt is negative)

            if prev_cnt < 0:
                heapq.heappush(heap, (prev_cnt, prev_ch))

            prev_cnt, prev_ch = cnt, ch

        return ''.join(result)
```

## Python3

```python
class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter
        import heapq

        n = len(s)
        freq = Counter(s)

        # If any character occurs more than (n+1)//2 times, impossible
        if max(freq.values()) > (n + 1) // 2:
            return ""

        # Build max-heap based on frequency
        heap = [(-cnt, ch) for ch, cnt in freq.items()]
        heapq.heapify(heap)

        result = []
        prev_cnt, prev_ch = 0, ''  # store previous character to reinsert later

        while heap:
            cnt, ch = heapq.heappop(heap)
            result.append(ch)
            # Since we used one occurrence, increase count (remember cnt is negative)
            cnt += 1  # moving towards zero

            # If there is a previously held character, push it back into heap
            if prev_cnt < 0:
                heapq.heappush(heap, (prev_cnt, prev_ch))

            # Hold current character for next round if still remaining
            prev_cnt, prev_ch = cnt, ch

        return ''.join(result)
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    char ch;
    int cnt;
} Pair;

static int cmpPair(const void *a, const void *b) {
    const Pair *p1 = (const Pair *)a;
    const Pair *p2 = (const Pair *)b;
    return p2->cnt - p1->cnt; // descending
}

char* reorganizeString(char* s) {
    int n = strlen(s);
    int freq[26] = {0};
    for (int i = 0; i < n; ++i) {
        freq[s[i] - 'a']++;
    }

    int maxCnt = 0;
    for (int i = 0; i < 26; ++i) {
        if (freq[i] > maxCnt) maxCnt = freq[i];
    }
    if (maxCnt > (n + 1) / 2) {
        char *empty = (char *)malloc(1);
        empty[0] = '\0';
        return empty;
    }

    Pair arr[26];
    int m = 0;
    for (int i = 0; i < 26; ++i) {
        if (freq[i]) {
            arr[m].ch = 'a' + i;
            arr[m].cnt = freq[i];
            ++m;
        }
    }

    qsort(arr, m, sizeof(Pair), cmpPair);

    char *res = (char *)malloc(n + 1);
    res[n] = '\0';

    int pos = 0; // even positions
    for (int i = 0; i < m; ++i) {
        while (arr[i].cnt > 0 && pos < n) {
            res[pos] = arr[i].ch;
            pos += 2;
            arr[i].cnt--;
        }
    }

    pos = 1; // odd positions
    for (int i = 0; i < m; ++i) {
        while (arr[i].cnt > 0) {
            res[pos] = arr[i].ch;
            pos += 2;
            arr[i].cnt--;
        }
    }

    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string ReorganizeString(string s) {
        int n = s.Length;
        int[] freq = new int[26];
        foreach (char c in s) freq[c - 'a']++;

        int limit = (n + 1) / 2;
        foreach (int f in freq) if (f > limit) return "";

        var sb = new System.Text.StringBuilder();

        while (sb.Length < n) {
            int first = -1;
            for (int i = 0; i < 26; i++) {
                if (freq[i] > 0 && (first == -1 || freq[i] > freq[first])) first = i;
            }
            if (first == -1) break;

            char lastChar = sb.Length > 0 ? sb[sb.Length - 1] : '\0';
            if (sb.Length > 0 && lastChar == (char)('a' + first)) {
                int second = -1;
                for (int i = 0; i < 26; i++) {
                    if (i != first && freq[i] > 0 && (second == -1 || freq[i] > freq[second])) second = i;
                }
                if (second == -1) return "";
                sb.Append((char)('a' + second));
                freq[second]--;
            } else {
                sb.Append((char)('a' + first));
                freq[first]--;
            }
        }

        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var reorganizeString = function(s) {
    const n = s.length;
    const freq = new Array(26).fill(0);
    for (let ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }
    // If any character occurs more than (n+1)/2, impossible
    if (Math.max(...freq) > Math.floor((n + 1) / 2)) return "";
    
    class MaxHeap {
        constructor() { this.heap = []; }
        size() { return this.heap.length; }
        push(node) {
            this.heap.push(node);
            this._siftUp(this.heap.length - 1);
        }
        pop() {
            if (this.heap.length === 0) return null;
            const top = this.heap[0];
            const end = this.heap.pop();
            if (this.heap.length > 0) {
                this.heap[0] = end;
                this._siftDown(0);
            }
            return top;
        }
        _siftUp(idx) {
            while (idx > 0) {
                const parent = (idx - 1) >> 1;
                if (this.heap[parent][1] >= this.heap[idx][1]) break;
                [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
                idx = parent;
            }
        }
        _siftDown(idx) {
            const length = this.heap.length;
            while (true) {
                let left = idx * 2 + 1;
                let right = idx * 2 + 2;
                let largest = idx;
                if (left < length && this.heap[left][1] > this.heap[largest][1]) largest = left;
                if (right < length && this.heap[right][1] > this.heap[largest][1]) largest = right;
                if (largest === idx) break;
                [this.heap[largest], this.heap[idx]] = [this.heap[idx], this.heap[largest]];
                idx = largest;
            }
        }
    }
    
    const heap = new MaxHeap();
    for (let i = 0; i < 26; i++) {
        if (freq[i] > 0) {
            heap.push([String.fromCharCode(97 + i), freq[i]]);
        }
    }
    
    let result = "";
    while (heap.size() > 1) {
        const [ch1, cnt1] = heap.pop();
        const [ch2, cnt2] = heap.pop();
        result += ch1 + ch2;
        if (cnt1 - 1 > 0) heap.push([ch1, cnt1 - 1]);
        if (cnt2 - 1 > 0) heap.push([ch2, cnt2 - 1]);
    }
    if (heap.size() === 1) {
        const [ch, cnt] = heap.pop();
        result += ch.repeat(cnt);
    }
    return result;
};
```

## Typescript

```typescript
function reorganizeString(s: string): string {
    const freq = new Array(26).fill(0);
    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }

    type Entry = { ch: string; cnt: number };
    const entries: Entry[] = [];
    for (let i = 0; i < 26; i++) {
        if (freq[i] > 0) {
            entries.push({ ch: String.fromCharCode(97 + i), cnt: freq[i] });
        }
    }

    let result = '';

    while (entries.length > 1) {
        // sort descending by remaining count
        entries.sort((a, b) => b.cnt - a.cnt);

        const first = entries[0];
        const second = entries[1];

        result += first.ch;
        result += second.ch;

        first.cnt--;
        second.cnt--;

        if (first.cnt === 0) entries.shift(); // remove first
        else entries[0] = first; // update

        if (second.cnt === 0) entries.splice(1, 1); // remove second
        else entries[1] = second;
    }

    if (entries.length === 1) {
        const last = entries[0];
        if (last.cnt > 1) return '';
        result += last.ch;
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function reorganizeString($s) {
        $n = strlen($s);
        $freq = array_fill(0, 26, 0);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - ord('a');
            $freq[$idx]++;
        }
        $max = max($freq);
        if ($max > intdiv($n + 1, 2)) {
            return "";
        }

        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);

        for ($i = 0; $i < 26; $i++) {
            if ($freq[$i] > 0) {
                $char = chr(ord('a') + $i);
                $pq->insert(['char' => $char, 'count' => $freq[$i]], $freq[$i]);
            }
        }

        $result = '';
        while ($pq->count() > 1) {
            $node1 = $pq->extract();
            $node2 = $pq->extract();

            $result .= $node1['char'];
            $result .= $node2['char'];

            $node1['count']--;
            $node2['count']--;

            if ($node1['count'] > 0) {
                $pq->insert($node1, $node1['count']);
            }
            if ($node2['count'] > 0) {
                $pq->insert($node2, $node2['count']);
            }
        }

        if ($pq->count() == 1) {
            $node = $pq->extract();
            if ($node['count'] > 1) {
                return "";
            }
            $result .= $node['char'];
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func reorganizeString(_ s: String) -> String {
        let n = s.count
        var freq = [Int](repeating: 0, count: 26)
        for ch in s {
            if let val = ch.asciiValue {
                let idx = Int(val - Character("a").asciiValue!)
                freq[idx] += 1
            }
        }
        // Check feasibility
        if let maxCount = freq.max(), maxCount > (n + 1) / 2 {
            return ""
        }
        // Build list of characters with counts
        var chars: [(char: Character, count: Int)] = []
        for i in 0..<26 where freq[i] > 0 {
            let ch = Character(UnicodeScalar(i + Int(Character("a").asciiValue!))!)
            chars.append((ch, freq[i]))
        }
        // Sort by descending frequency
        chars.sort { $0.count > $1.count }
        
        var result = [Character](repeating: " ", count: n)
        var index = 0
        for item in chars {
            var cnt = item.count
            let ch = item.char
            while cnt > 0 {
                if index >= n {
                    index = 1
                }
                result[index] = ch
                index += 2
                cnt -= 1
            }
        }
        return String(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun reorganizeString(s: String): String {
        val n = s.length
        val freq = IntArray(26)
        for (c in s) {
            freq[c - 'a']++
        }
        for (cnt in freq) {
            if (cnt > (n + 1) / 2) return ""
        }

        data class Node(val ch: Char, var cnt: Int)

        val pq = java.util.PriorityQueue<Node>(compareByDescending<Node> { it.cnt })
        for (i in 0 until 26) {
            if (freq[i] > 0) {
                pq.offer(Node(('a'.code + i).toChar(), freq[i]))
            }
        }

        val sb = StringBuilder()
        while (pq.size >= 2) {
            val n1 = pq.poll()
            val n2 = pq.poll()
            sb.append(n1.ch)
            sb.append(n2.ch)
            n1.cnt--
            n2.cnt--
            if (n1.cnt > 0) pq.offer(n1)
            if (n2.cnt > 0) pq.offer(n2)
        }
        if (pq.isNotEmpty()) {
            val last = pq.poll()
            if (last.cnt > 1) return ""
            sb.append(last.ch)
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String reorganizeString(String s) {
    int n = s.length;
    List<int> freq = List.filled(26, 0);
    for (int i = 0; i < n; i++) {
      freq[s.codeUnitAt(i) - 97]++;
    }

    int maxFreq = freq.reduce((a, b) => a > b ? a : b);
    if (maxFreq > (n + 1) ~/ 2) return "";

    List<List<dynamic>> heap = [];
    for (int i = 0; i < 26; i++) {
      if (freq[i] > 0) {
        heap.add([String.fromCharCode(i + 97), freq[i]]);
      }
    }

    StringBuffer sb = StringBuffer();
    String prev = '';

    while (heap.isNotEmpty) {
      // sort descending by remaining count
      heap.sort((a, b) => b[1] - a[1]);

      int idx = 0;
      if (prev.isNotEmpty && heap[0][0] == prev) {
        if (heap.length == 1) return "";
        idx = 1;
      }

      var entry = heap[idx];
      sb.write(entry[0]);
      prev = entry[0];
      entry[1]--;

      if (entry[1] == 0) {
        heap.removeAt(idx);
      }
    }

    return sb.toString();
  }
}
```

## Golang

```go
package main

import "container/heap"

type charItem struct {
	ch  byte
	cnt int
}

type maxHeap []charItem

func (h maxHeap) Len() int           { return len(h) }
func (h maxHeap) Less(i, j int) bool { return h[i].cnt > h[j].cnt } // max-heap
func (h maxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *maxHeap) Push(x interface{}) {
	*h = append(*h, x.(charItem))
}

func (h *maxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

func reorganizeString(s string) string {
	if len(s) == 0 {
		return ""
	}
	var freq [26]int
	for i := 0; i < len(s); i++ {
		freq[s[i]-'a']++
	}
	n := len(s)
	limit := (n + 1) / 2
	for _, c := range freq {
		if c > limit {
			return ""
		}
	}
	h := &maxHeap{}
	heap.Init(h)
	for i, c := range freq {
		if c > 0 {
			heap.Push(h, charItem{byte('a' + i), c})
		}
	}
	var res []byte
	for h.Len() > 1 {
		first := heap.Pop(h).(charItem)
		second := heap.Pop(h).(charItem)
		res = append(res, first.ch, second.ch)
		if first.cnt-1 > 0 {
			heap.Push(h, charItem{first.ch, first.cnt - 1})
		}
		if second.cnt-1 > 0 {
			heap.Push(h, charItem{second.ch, second.cnt - 1})
		}
	}
	if h.Len() == 1 {
		last := heap.Pop(h).(charItem)
		if last.cnt > 1 {
			return ""
		}
		res = append(res, last.ch)
	}
	return string(res)
}
```

## Ruby

```ruby
def reorganize_string(s)
  n = s.length
  freq = Hash.new(0)
  s.each_char { |c| freq[c] += 1 }
  return "" if freq.values.max > (n + 1) / 2

  sorted = freq.sort_by { |_, cnt| -cnt } # descending by count
  res = Array.new(n)
  idx = 0
  sorted.each do |ch, cnt|
    cnt.times do
      idx = 1 if idx >= n
      res[idx] = ch
      idx += 2
    end
  end
  res.join
end
```

## Scala

```scala
object Solution {
    def reorganizeString(s: String): String = {
        val n = s.length
        val counts = new Array[Int](26)
        for (c <- s) counts(c - 'a') += 1

        var maxCount = 0
        for (cnt <- counts) if (cnt > maxCount) maxCount = cnt
        if (maxCount > (n + 1) / 2) return ""

        import scala.collection.mutable.PriorityQueue
        implicit val ord: Ordering[(Int, Char)] = Ordering.by[(Int, Char), Int](_._1)
        val pq = PriorityQueue.empty[(Int, Char)]

        for (i <- 0 until 26) {
            if (counts(i) > 0) pq.enqueue((counts(i), ('a' + i).toChar))
        }

        val sb = new StringBuilder
        while (pq.size >= 2) {
            val first = pq.dequeue()
            val second = pq.dequeue()
            sb.append(first._2)
            sb.append(second._2)

            if (first._1 - 1 > 0) pq.enqueue((first._1 - 1, first._2))
            if (second._1 - 1 > 0) pq.enqueue((second._1 - 1, second._2))
        }

        if (pq.nonEmpty) sb.append(pq.dequeue()._2)

        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn reorganize_string(s: String) -> String {
        let n = s.len();
        if n == 0 {
            return String::new();
        }
        // count frequencies
        let mut cnt = [0usize; 26];
        for b in s.bytes() {
            cnt[(b - b'a') as usize] += 1;
        }
        // check feasibility
        let limit = (n + 1) / 2;
        if cnt.iter().any(|&c| c > limit) {
            return String::new();
        }
        // collect characters sorted by frequency descending
        let mut freq_chars: Vec<(usize, u8)> = Vec::new();
        for i in 0..26 {
            if cnt[i] > 0 {
                freq_chars.push((cnt[i], b'a' + i as u8));
            }
        }
        freq_chars.sort_by(|a, b| b.0.cmp(&a.0));
        // flatten into ordered list
        let mut ordered: Vec<char> = Vec::with_capacity(n);
        for (c, ch) in freq_chars {
            for _ in 0..c {
                ordered.push(ch as char);
            }
        }
        // place characters at even then odd indices
        let mut res = vec![' '; n];
        let mut idx = 0usize;
        for &ch in &ordered {
            if idx >= n {
                idx = 1;
            }
            res[idx] = ch;
            idx += 2;
        }
        res.iter().collect()
    }
}
```

## Racket

```racket
#lang racket

(define/contract (reorganize-string s)
  (-> string? string?)
  (let* ((n (string-length s))
         (cnts (make-vector 26 0))
         (base (char->integer #\a)))
    ;; count frequencies
    (for ([ch (in-string s)])
      (let* ((idx (- (char->integer ch) base))
             (old (vector-ref cnts idx)))
        (vector-set! cnts idx (+ old 1))))
    ;; feasibility check
    (define max-count
      (for/fold ([m 0]) ([i (in-range 26)])
        (max m (vector-ref cnts i))))
    (if (> max-count (quotient (+ n 1) 2))
        ""
        (let loop ((counts (vector-copy cnts)) (result '()))
          (define pairs
            (for/list ([i (in-range 26)]
                       #:when (> (vector-ref counts i) 0))
              (list i (vector-ref counts i))))
          (cond
            [(empty? pairs)
             (list->string (reverse result))]
            [(= (length pairs) 1)
             (define idx (first (first pairs)))
             (define cnt (second (first pairs)))
             (if (= cnt 1)
                 (list->string (reverse (cons (integer->char (+ base idx)) result)))
                 "")]
            [else
             (define sorted (sort pairs (lambda (a b) (> (second a) (second b)))))
             (define first-pair (first sorted))
             (define second-pair (second sorted))
             (define idx1 (first first-pair))
             (define cnt1 (second first-pair))
             (define idx2 (first second-pair))
             (define cnt2 (second second-pair))
             (vector-set! counts idx1 (- cnt1 1))
             (vector-set! counts idx2 (- cnt2 1))
             (loop counts
                   (cons (integer->char (+ base idx2))
                         (cons (integer->char (+ base idx1)) result))))])))))
```

## Erlang

```erlang
-module(solution).
-export([reorganize_string/1]).
-spec reorganize_string(unicode:unicode_binary()) -> unicode:unicode_binary().
reorganize_string(S) ->
    CharList = binary_to_list(S),
    FreqMap = count_chars(CharList, #{}),
    Heap0 = [{Count, Ch} || {Ch, Count} <- maps:to_list(FreqMap), Count > 0],
    SortedHeap = lists:sort(fun({C1,_},{C2,_}) -> C1 > C2 end, Heap0),
    case loop(SortedHeap, []) of
        impossible -> <<>>;
        {ok, ResList} -> list_to_binary(ResList)
    end.

count_chars([], Map) ->
    Map;
count_chars([C|Rest], Map) ->
    Count = maps:get(C, Map, 0),
    NewMap = maps:put(C, Count + 1, Map),
    count_chars(Rest, NewMap).

loop([], RevRes) ->
    {ok, lists:reverse(RevRes)};
loop([{Cnt1, Ch1}|Rest], RevRes) ->
    case RevRes of
        [Prev|_] when Prev =:= Ch1 ->
            case Rest of
                [] -> impossible;
                [{Cnt2, Ch2}|Rest2] ->
                    NewHeap = rebuild(Rest2, [{Cnt1, Ch1}, {Cnt2 - 1, Ch2}]),
                    loop(NewHeap, [Ch2|RevRes])
            end;
        _ ->
            NewHeap = rebuild(Rest, [{Cnt1 - 1, Ch1}]),
            loop(NewHeap, [Ch1|RevRes])
    end.

rebuild(Rest, Updates) ->
    Combined = Rest ++ Updates,
    Filtered = [ {C, Ch} || {C, Ch} <- Combined, C > 0 ],
    lists:sort(fun({C1,_},{C2,_}) -> C1 > C2 end, Filtered).
```

## Elixir

```elixir
defmodule Solution do
  @spec reorganize_string(s :: String.t) :: String.t
  def reorganize_string(s) do
    n = String.length(s)

    counts =
      s
      |> String.graphemes()
      |> Enum.reduce(%{}, fn ch, acc ->
        Map.update(acc, ch, 1, &(&1 + 1))
      end)

    max_freq =
      counts
      |> Map.values()
      |> Enum.max(fn -> 0 end)

    if max_freq > div(n + 1, 2) do
      ""
    else
      sorted =
        counts
        |> Enum.to_list()
        |> Enum.sort_by(fn {_c, cnt} -> -cnt end)

      chars = Enum.flat_map(sorted, fn {c, cnt} -> List.duplicate(c, cnt) end)

      result = List.duplicate("", n)

      {final_res, _} =
        Enum.reduce(chars, {result, 0}, fn ch, {res, idx} ->
          if idx >= n do
            new_idx = 1
            {List.replace_at(res, new_idx, ch), new_idx + 2}
          else
            {List.replace_at(res, idx, ch), idx + 2}
          end
        end)

      Enum.join(final_res)
    end
  end
end
```
