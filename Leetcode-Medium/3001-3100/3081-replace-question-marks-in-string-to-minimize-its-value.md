# 3081. Replace Question Marks in String to Minimize Its Value

## Cpp

```cpp
class Solution {
public:
    string minimizeStringValue(string s) {
        const int ALPH = 26;
        vector<int> base(ALPH, 0);
        int q = 0;
        for (char ch : s) {
            if (ch == '?') ++q;
            else ++base[ch - 'a'];
        }
        struct Node {
            int freq;
            int idx;
        };
        auto cmp = [](const Node& a, const Node& b) {
            if (a.freq != b.freq) return a.freq > b.freq; // min-heap by freq
            return a.idx > b.idx;                         // then by letter
        };
        priority_queue<Node, vector<Node>, decltype(cmp)> pq(cmp);
        for (int i = 0; i < ALPH; ++i) {
            pq.push({base[i], i});
        }
        vector<int> add(ALPH, 0);
        while (q--) {
            Node cur = pq.top(); pq.pop();
            ++add[cur.idx];
            ++cur.freq;
            pq.push(cur);
        }
        string res;
        for (char ch : s) {
            if (ch != '?') {
                res.push_back(ch);
            } else {
                for (int i = 0; i < ALPH; ++i) {
                    if (add[i] > 0) {
                        res.push_back('a' + i);
                        --add[i];
                        break;
                    }
                }
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String minimizeStringValue(String s) {
        int n = s.length();
        int[] base = new int[26];
        int q = 0;
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == '?') {
                q++;
            } else {
                base[c - 'a']++;
            }
        }

        // Min-heap ordered by current total count, then by letter index
        java.util.PriorityQueue<int[]> pq = new java.util.PriorityQueue<>(
            (a, b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]
        );

        for (int i = 0; i < 26; i++) {
            pq.offer(new int[]{base[i], i}); // {current total count, letter index}
        }

        int[] added = new int[26];
        for (int i = 0; i < q; i++) {
            int[] cur = pq.poll();
            int idx = cur[1];
            added[idx]++;          // assign this '?' to letter idx
            cur[0]++;              // total count of this letter increases
            pq.offer(cur);
        }

        StringBuilder sb = new StringBuilder(n);
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c != '?') {
                sb.append(c);
            } else {
                for (int j = 0; j < 26; j++) {
                    if (added[j] > 0) {
                        sb.append((char) ('a' + j));
                        added[j]--;
                        break;
                    }
                }
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def minimizeStringValue(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = [0] * 26
        for ch in s:
            if ch != '?':
                freq[ord(ch) - 97] += 1

        orig = freq[:]

        import heapq
        heap = [(freq[i], i) for i in range(26)]
        heapq.heapify(heap)

        q_cnt = s.count('?')
        for _ in range(q_cnt):
            cnt, idx = heapq.heappop(heap)
            cnt += 1
            freq[idx] = cnt
            heapq.heappush(heap, (cnt, idx))

        extra = [freq[i] - orig[i] for i in range(26)]

        res = []
        cur = 0
        for ch in s:
            if ch != '?':
                res.append(ch)
            else:
                while cur < 26 and extra[cur] == 0:
                    cur += 1
                # cur is guaranteed to be valid because total extra equals number of '?'
                res.append(chr(cur + 97))
                extra[cur] -= 1

        return ''.join(res)
```

## Python3

```python
class Solution:
    def minimizeStringValue(self, s: str) -> str:
        import heapq

        freq = [0] * 26
        q_cnt = 0
        for ch in s:
            if ch == '?':
                q_cnt += 1
            else:
                freq[ord(ch) - 97] += 1

        add = [0] * 26
        heap = [(freq[i], i) for i in range(26)]
        heapq.heapify(heap)

        for _ in range(q_cnt):
            f, i = heapq.heappop(heap)
            add[i] += 1
            heapq.heappush(heap, (f + 1, i))

        res = []
        ptr = 0
        for ch in s:
            if ch != '?':
                res.append(ch)
            else:
                while ptr < 26 and add[ptr] == 0:
                    ptr += 1
                res.append(chr(97 + ptr))
                add[ptr] -= 1

        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* minimizeStringValue(char* s) {
    size_t n = strlen(s);
    char *res = (char*)malloc(n + 1);
    if (!res) return NULL;
    memcpy(res, s, n + 1);

    int cnt[26] = {0};
    int add[26] = {0};

    int q = 0;
    for (size_t i = 0; i < n; ++i) {
        if (res[i] == '?') {
            ++q;
        } else {
            ++cnt[res[i] - 'a'];
        }
    }

    // Distribute question marks to minimize total value
    for (int k = 0; k < q; ++k) {
        int best = 0;
        int bestCnt = cnt[0] + add[0];
        for (int i = 1; i < 26; ++i) {
            int cur = cnt[i] + add[i];
            if (cur < bestCnt || (cur == bestCnt && i < best)) {
                best = i;
                bestCnt = cur;
            }
        }
        ++add[best];
    }

    // Fill the string with the smallest possible letters left to right
    int rem[26];
    for (int i = 0; i < 26; ++i) rem[i] = add[i];

    for (size_t i = 0; i < n; ++i) {
        if (res[i] == '?') {
            for (int j = 0; j < 26; ++j) {
                if (rem[j] > 0) {
                    res[i] = 'a' + j;
                    --rem[j];
                    break;
                }
            }
        }
    }

    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string MinimizeStringValue(string s) {
        int n = s.Length;
        int[] freq = new int[26];
        List<int> qIndices = new List<int>();
        foreach (var (ch, i) in s.Select((c, idx) => (c, idx))) {
            if (ch == '?') {
                qIndices.Add(i);
            } else {
                freq[ch - 'a']++;
            }
        }

        int q = qIndices.Count;
        // Distribute question marks to minimize total value
        for (int k = 0; k < q; ++k) {
            int best = 0;
            for (int c = 1; c < 26; ++c) {
                if (freq[c] < freq[best] || (freq[c] == freq[best] && c < best)) {
                    best = c;
                }
            }
            freq[best]++;
        }

        // Determine how many of each letter were added
        int[] addCount = new int[26];
        foreach (int idx in qIndices) {
            // placeholder, will fill later
        }
        // Recompute initial frequencies to get added counts
        int[] initFreq = new int[26];
        foreach (var ch in s) {
            if (ch != '?') initFreq[ch - 'a']++;
        }
        for (int c = 0; c < 26; ++c) {
            addCount[c] = freq[c] - initFreq[c];
        }

        char[] res = s.ToCharArray();
        foreach (int pos in qIndices) {
            for (int c = 0; c < 26; ++c) {
                if (addCount[c] > 0) {
                    res[pos] = (char)('a' + c);
                    addCount[c]--;
                    break;
                }
            }
        }

        return new string(res);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var minimizeStringValue = function(s) {
    const n = s.length;
    const freq = new Array(26).fill(0);
    let q = 0;
    for (let i = 0; i < n; ++i) {
        const ch = s.charCodeAt(i);
        if (ch === 63) { // '?'
            ++q;
        } else {
            ++freq[ch - 97];
        }
    }

    const added = new Array(26).fill(0);
    for (let i = 0; i < q; ++i) {
        let minFreq = Infinity, idx = 0;
        for (let j = 0; j < 26; ++j) {
            if (freq[j] < minFreq) {
                minFreq = freq[j];
                idx = j;
            }
        }
        freq[idx]++;
        added[idx]++;
    }

    const need = added.slice();
    const res = [];
    for (let i = 0; i < n; ++i) {
        if (s[i] !== '?') {
            res.push(s[i]);
        } else {
            for (let j = 0; j < 26; ++j) {
                if (need[j] > 0) {
                    res.push(String.fromCharCode(97 + j));
                    --need[j];
                    break;
                }
            }
        }
    }
    return res.join('');
};
```

## Typescript

```typescript
function minimizeStringValue(s: string): string {
    const n = s.length;
    const cnt = new Array(26).fill(0);
    let questionMarks = 0;

    for (const ch of s) {
        if (ch === '?') {
            questionMarks++;
        } else {
            cnt[ch.charCodeAt(0) - 97]++;
        }
    }

    const added = new Array(26).fill(0);

    // Assign each '?' to the letter with current minimal total count
    for (let k = 0; k < questionMarks; k++) {
        let minIdx = 0;
        for (let i = 1; i < 26; i++) {
            if (cnt[i] < cnt[minIdx]) minIdx = i;
        }
        cnt[minIdx]++;
        added[minIdx]++;
    }

    const res: string[] = s.split('');
    let curLetter = 0;

    for (let i = 0; i < n; i++) {
        if (res[i] === '?') {
            while (curLetter < 26 && added[curLetter] === 0) curLetter++;
            const ch = String.fromCharCode(97 + curLetter);
            res[i] = ch;
            added[curLetter]--;
        }
    }

    return res.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function minimizeStringValue($s) {
        $n = strlen($s);
        $freq = array_fill(0, 26, 0);

        // Count existing letters
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if ($ch !== '?') {
                $idx = ord($ch) - 97;
                $freq[$idx]++;
            }
        }

        $result = [];

        // Replace '?' greedily
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if ($ch !== '?') {
                $result[] = $ch;
            } else {
                $minFreq = PHP_INT_MAX;
                $chosenIdx = 0;
                for ($c = 0; $c < 26; $c++) {
                    if ($freq[$c] < $minFreq) {
                        $minFreq = $freq[$c];
                        $chosenIdx = $c;
                    }
                }
                $freq[$chosenIdx]++;
                $result[] = chr($chosenIdx + 97);
            }
        }

        return implode('', $result);
    }
}
```

## Swift

```swift
class Solution {
    func minimizeStringValue(_ s: String) -> String {
        var freq = [Int](repeating: 0, count: 26)
        var questionCount = 0
        let aVal = Int(Character("a").unicodeScalars.first!.value)

        for ch in s {
            if ch == "?" {
                questionCount += 1
            } else {
                let idx = Int(ch.unicodeScalars.first!.value) - aVal
                freq[idx] += 1
            }
        }

        var extra = [Int](repeating: 0, count: 26)
        for _ in 0..<questionCount {
            var minVal = Int.max
            var idx = 0
            for i in 0..<26 {
                let cur = freq[i] + extra[i]
                if cur < minVal {
                    minVal = cur
                    idx = i
                }
            }
            extra[idx] += 1
        }

        var result: [Character] = []
        for ch in s {
            if ch == "?" {
                for i in 0..<26 where extra[i] > 0 {
                    let scalar = UnicodeScalar(UInt32(aVal + i))!
                    result.append(Character(scalar))
                    extra[i] -= 1
                    break
                }
            } else {
                result.append(ch)
            }
        }

        return String(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimizeStringValue(s: String): String {
        val freq = IntArray(26)
        var questionMarks = 0
        for (ch in s) {
            if (ch == '?') {
                questionMarks++
            } else {
                freq[ch - 'a']++
            }
        }

        val sb = StringBuilder(s.length)
        for (ch in s) {
            if (ch != '?') {
                sb.append(ch)
            } else {
                var minIdx = 0
                var minFreq = Int.MAX_VALUE
                for (i in 0 until 26) {
                    val f = freq[i]
                    if (f < minFreq || (f == minFreq && i < minIdx)) {
                        minFreq = f
                        minIdx = i
                    }
                }
                freq[minIdx]++
                sb.append(('a'.code + minIdx).toChar())
            }
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String minimizeStringValue(String s) {
    const int alphabet = 26;
    List<int> cnt = List.filled(alphabet, 0);
    int questionMarks = 0;

    for (int i = 0; i < s.length; i++) {
      int code = s.codeUnitAt(i);
      if (code == '?'.codeUnitAt(0)) {
        questionMarks++;
      } else {
        cnt[code - 'a'.codeUnitAt(0)]++;
      }
    }

    List<int> need = List.filled(alphabet, 0);

    for (int k = 0; k < questionMarks; k++) {
      int minIdx = 0;
      for (int j = 1; j < alphabet; j++) {
        if (cnt[j] < cnt[minIdx]) {
          minIdx = j;
        }
      }
      cnt[minIdx]++;
      need[minIdx]++;
    }

    StringBuffer sb = StringBuffer();
    int aCode = 'a'.codeUnitAt(0);
    for (int i = 0; i < s.length; i++) {
      int code = s.codeUnitAt(i);
      if (code != '?'.codeUnitAt(0)) {
        sb.writeCharCode(code);
      } else {
        for (int j = 0; j < alphabet; j++) {
          if (need[j] > 0) {
            sb.writeCharCode(aCode + j);
            need[j]--;
            break;
          }
        }
      }
    }

    return sb.toString();
  }
}
```

## Golang

```go
func minimizeStringValue(s string) string {
    var freq [26]int
    for i := 0; i < len(s); i++ {
        if s[i] != '?' {
            freq[s[i]-'a']++
        }
    }

    res := make([]byte, len(s))
    for i := 0; i < len(s); i++ {
        if s[i] != '?' {
            res[i] = s[i]
            continue
        }
        minFreq := int(^uint(0) >> 1)
        idx := 0
        for j := 0; j < 26; j++ {
            if freq[j] < minFreq {
                minFreq = freq[j]
                idx = j
            }
        }
        res[i] = byte('a' + idx)
        freq[idx]++
    }
    return string(res)
}
```

## Ruby

```ruby
def minimize_string_value(s)
  freq = Array.new(26, 0)
  orig = Array.new(26, 0)
  q = 0

  s.each_char do |ch|
    if ch == '?'
      q += 1
    else
      idx = ch.ord - 97
      freq[idx] += 1
      orig[idx] += 1
    end
  end

  q.times do
    min_idx = 0
    min_val = freq[0]
    (1...26).each do |i|
      if freq[i] < min_val || (freq[i] == min_val && i < min_idx)
        min_val = freq[i]
        min_idx = i
      end
    end
    freq[min_idx] += 1
  end

  remain = Array.new(26, 0)
  26.times { |i| remain[i] = freq[i] - orig[i] }

  result = []
  s.each_char do |ch|
    if ch != '?'
      result << ch
    else
      i = 0
      i += 1 while i < 26 && remain[i] == 0
      result << (97 + i).chr
      remain[i] -= 1
    end
  end

  result.join
end
```

## Scala

```scala
object Solution {
    def minimizeStringValue(s: String): String = {
        val cnt = Array.fill(26)(0)
        for (ch <- s) {
            if (ch != '?') cnt(ch - 'a') += 1
        }
        val sb = new StringBuilder(s.length)
        for (ch <- s) {
            if (ch != '?') {
                sb.append(ch)
            } else {
                var bestIdx = 0
                var bestCnt = Int.MaxValue
                var i = 0
                while (i < 26) {
                    val cur = cnt(i)
                    if (cur < bestCnt) {
                        bestCnt = cur
                        bestIdx = i
                    }
                    i += 1
                }
                cnt(bestIdx) += 1
                sb.append((('a'.toInt + bestIdx).toChar))
            }
        }
        sb.toString()
    }
}
```

## Rust

```rust
use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn minimize_string_value(s: String) -> String {
        let mut counts = [0usize; 26];
        for ch in s.chars() {
            if ch != '?' {
                let idx = (ch as u8 - b'a') as usize;
                counts[idx] += 1;
            }
        }

        let mut heap: BinaryHeap<Reverse<(usize, u8)>> = BinaryHeap::new();
        for i in 0..26 {
            heap.push(Reverse((counts[i], i as u8)));
        }

        let mut result = String::with_capacity(s.len());
        for ch in s.chars() {
            if ch != '?' {
                result.push(ch);
            } else {
                let Reverse((cnt, idx)) = heap.pop().unwrap();
                let letter = (b'a' + idx) as char;
                result.push(letter);
                heap.push(Reverse((cnt + 1, idx)));
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (minimize-string-value s)
  (-> string? string?)
  (let* ([n (string-length s)]
         [freq (make-vector 26 0)]
         [orig-freq (make-vector 26 0)]
         [question-count
          (let loop ((i 0) (cnt 0))
            (if (= i n)
                cnt
                (let ((c (string-ref s i)))
                  (if (char=? c #\?)
                      (loop (+ i 1) (+ cnt 1))
                      (let* ((idx (- (char->integer c) (char->integer #\a)))
                             (new (+ (vector-ref freq idx) 1)))
                        (vector-set! freq idx new)
                        (vector-set! orig-freq idx new)
                        (loop (+ i 1) cnt))))))])
    ;; Distribute question marks to minimize cost
    (let loop ((k question-count))
      (when (> k 0)
        (let* ((min-idx 0)
               (min-val (vector-ref freq 0)))
          (do ([i 1 (+ i 1)])
              ((= i 26))
            (let ((v (vector-ref freq i)))
              (when (< v min-val)
                (set! min-val v)
                (set! min-idx i))))
          (vector-set! freq min-idx (+ (vector-ref freq min-idx) 1))
          (loop (- k 1)))))
    ;; Compute how many of each letter were added
    (let ([add-counts (make-vector 26 0)])
      (do ([i 0 (+ i 1)]) ((= i 26))
        (vector-set! add-counts i
                     (- (vector-ref freq i) (vector-ref orig-freq i))))
      ;; Build result string
      (let* ([res (make-string n)]
             [cur-idx 0])
        (define (advance-pointer!)
          (when (and (< cur-idx 26)
                     (= (vector-ref add-counts cur-idx) 0))
            (set! cur-idx (+ cur-idx 1))
            (advance-pointer!)))
        (do ([i 0 (+ i 1)]) ((= i n))
          (let ((c (string-ref s i)))
            (if (char=? c #\?)
                (begin
                  (advance-pointer!)
                  (let ((ch (integer->char
                             (+ (char->integer #\a) cur-idx))))
                    (string-set! res i ch)
                    (vector-set! add-counts cur-idx
                                 (- (vector-ref add-counts cur-idx) 1))))
                (string-set! res i c))))
        res))))
```

## Erlang

```erlang
-module(solution).
-export([minimize_string_value/1]).

-spec minimize_string_value(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
minimize_string_value(S) ->
    CharList = unicode:characters_to_list(S),
    {ExistingCounts, Q} = count_chars(CharList, erlang:make_tuple(26, 0), 0),
    FinalCounts = allocate_counts(ExistingCounts, Q),
    Needed = needed_counts(FinalCounts, ExistingCounts),
    ResultChars = build_string(CharList, Needed, []),
    unicode:characters_to_binary(lists:reverse(ResultChars)).

%% Count existing letters and number of '?'.
count_chars([], Counts, Q) ->
    {Counts, Q};
count_chars([C | Rest], Counts, Q) ->
    case C of
        $? ->
            count_chars(Rest, Counts, Q + 1);
        _ when C >= $a, C =< $z ->
            Idx = C - $a + 1,
            Old = element(Idx, Counts),
            NewCounts = setelement(Idx, Counts, Old + 1),
            count_chars(Rest, NewCounts, Q)
    end.

%% Allocate extra letters to minimize value.
allocate_counts(Counts, 0) ->
    Counts;
allocate_counts(Counts, Q) ->
    MinIdx = find_min_idx(Counts, 1, 26, 1, element(1, Counts)),
    Old = element(MinIdx, Counts),
    NewCounts = setelement(MinIdx, Counts, Old + 1),
    allocate_counts(NewCounts, Q - 1).

find_min_idx(_Counts, I, Max, BestIdx, _BestVal) when I > Max ->
    BestIdx;
find_min_idx(Counts, I, Max, BestIdx, BestVal) ->
    Val = element(I, Counts),
    {NewBestIdx, NewBestVal} =
        if
            Val < BestVal -> {I, Val};
            true -> {BestIdx, BestVal}
        end,
    find_min_idx(Counts, I + 1, Max, NewBestIdx, NewBestVal).

%% Compute how many of each letter still need to be placed.
needed_counts(Final, Existing) ->
    needed_counts(Final, Existing, 1, erlang:make_tuple(26, 0)).

needed_counts(_Final, _Existing, I, Acc) when I > 26 ->
    Acc;
needed_counts(Final, Existing, I, Acc) ->
    Need = element(I, Final) - element(I, Existing),
    NewAcc = setelement(I, Acc, Need),
    needed_counts(Final, Existing, I + 1, NewAcc).

%% Build final string, filling '?' with smallest possible needed letters.
build_string([], _Needed, Acc) ->
    Acc;
build_string([C | Rest], Needed, Acc) ->
    case C of
        $? ->
            {LetterIdx, UpdatedNeeded} = pick_letter(Needed, 1),
            LetterChar = $a + LetterIdx - 1,
            build_string(Rest, UpdatedNeeded, [LetterChar | Acc]);
        _ ->
            build_string(Rest, Needed, [C | Acc])
    end.

pick_letter(Needed, I) when I =< 26 ->
    Need = element(I, Needed),
    if
        Need > 0 ->
            NewNeeded = setelement(I, Needed, Need - 1),
            {I, NewNeeded};
        true ->
            pick_letter(Needed, I + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimize_string_value(s :: String.t()) :: String.t()
  def minimize_string_value(s) do
    chars = String.to_charlist(s)

    init_counts =
      Enum.reduce(chars, List.duplicate(0, 26), fn
        ??, acc -> acc
        c, acc ->
          idx = c - ?a
          List.update_at(acc, idx, &(&1 + 1))
      end)

    result_rev = process(chars, init_counts, [])
    List.to_string(Enum.reverse(result_rev))
  end

  defp process([], _counts, acc), do: acc

  defp process([h | t], counts, acc) when h != ?? do
    process(t, counts, [h | acc])
  end

  defp process([?? | t], counts, acc) do
    {_, min_idx} =
      Enum.with_index(counts)
      |> Enum.min_by(fn {cnt, idx} -> {cnt, idx} end)

    new_counts = List.update_at(counts, min_idx, &(&1 + 1))
    char = ?a + min_idx
    process(t, new_counts, [char | acc])
  end
end
```
