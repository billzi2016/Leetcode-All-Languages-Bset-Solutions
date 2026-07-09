# 1585. Check If String Is Transformable With Substring Sort Operations

## Cpp

```cpp
class Solution {
public:
    bool isTransformable(string s, string t) {
        int n = s.size();
        vector<queue<int>> pos(10);
        for (int i = 0; i < n; ++i) {
            pos[s[i] - '0'].push(i);
        }
        for (char ch : t) {
            int d = ch - '0';
            if (pos[d].empty()) return false;
            int idx = pos[d].front();
            // ensure no smaller digit appears before this index
            for (int c = 0; c < d; ++c) {
                if (!pos[c].empty() && pos[c].front() < idx) return false;
            }
            pos[d].pop();
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean isTransformable(String s, String t) {
        int n = s.length();
        int[] cnt = new int[10];
        int j = 0;
        for (int i = 0; i < n; i++) {
            int need = t.charAt(i) - '0';
            // bring characters from s until we have the needed digit
            while (j < n && cnt[need] == 0) {
                cnt[s.charAt(j) - '0']++;
                j++;
            }
            if (cnt[need] == 0) return false; // cannot obtain needed digit
            // any smaller digit present would block sorting
            for (int d = 0; d < need; d++) {
                if (cnt[d] > 0) return false;
            }
            cnt[need]--;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def isTransformable(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import deque

        # store indices of each digit in s
        idx_queues = [deque() for _ in range(10)]
        for i, ch in enumerate(s):
            idx_queues[ord(ch) - 48].append(i)

        for ch in t:
            d = ord(ch) - 48
            if not idx_queues[d]:
                return False

            cur_idx = idx_queues[d][0]  # earliest occurrence of needed digit

            # any smaller digit appearing before cur_idx blocks the move
            for smaller in range(d):
                if idx_queues[smaller] and idx_queues[smaller][0] < cur_idx:
                    return False

            idx_queues[d].popleft()   # use this character

        return True
```

## Python3

```python
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        n = len(s)
        i = j = 0
        cnt = [0] * 10
        while j < n:
            # advance in s until we find the needed character
            while i < n and s[i] != t[j]:
                cnt[ord(s[i]) - ord('0')] += 1
                i += 1
            if i == n:
                return False
            # ensure no smaller pending characters block the move
            cur = ord(t[j]) - ord('0')
            for d in range(cur):
                if cnt[d]:
                    return False
            i += 1
            j += 1
        return True
```

## C

```c
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

bool isTransformable(char* s, char* t) {
    int n = strlen(s);
    // count occurrences per digit
    int cnt[10] = {0};
    for (int i = 0; i < n; ++i) {
        cnt[s[i] - '0']++;
    }
    // allocate arrays for positions
    int* pos[10];
    for (int d = 0; d < 10; ++d) {
        if (cnt[d] > 0) {
            pos[d] = (int*)malloc(cnt[d] * sizeof(int));
        } else {
            pos[d] = NULL;
        }
        cnt[d] = 0; // reuse as fill index
    }
    // fill positions in order
    for (int i = 0; i < n; ++i) {
        int d = s[i] - '0';
        pos[d][cnt[d]++] = i;
    }
    // head pointers for each digit
    int head[10] = {0};
    // process target string
    for (int i = 0; i < n; ++i) {
        int c = t[i] - '0';
        if (head[c] >= cnt[c]) { // no remaining occurrence
            // free allocated memory before returning
            for (int d = 0; d < 10; ++d) free(pos[d]);
            return false;
        }
        int curPos = pos[c][head[c]];
        // ensure no smaller digit blocks the movement
        for (int d = 0; d < c; ++d) {
            if (head[d] < cnt[d] && pos[d][head[d]] < curPos) {
                for (int dd = 0; dd < 10; ++dd) free(pos[dd]);
                return false;
            }
        }
        head[c]++; // use this occurrence
    }
    // clean up
    for (int d = 0; d < 10; ++d) free(pos[d]);
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsTransformable(string s, string t)
    {
        int n = s.Length;
        int[] extra = new int[10];
        int i = 0;

        foreach (char ch in t)
        {
            int target = ch - '0';
            while (i < n && (s[i] - '0') != target)
            {
                extra[s[i] - '0']++;
                i++;
            }
            if (i == n) return false; // target not found

            for (int d = 0; d < target; ++d)
            {
                if (extra[d] > 0) return false;
            }

            i++; // use this character
        }

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isTransformable = function(s, t) {
    const n = s.length;
    const pos = Array.from({ length: 10 }, () => []);
    for (let i = 0; i < n; i++) {
        const d = s.charCodeAt(i) - 48;
        pos[d].push(i);
    }
    const ptr = new Array(10).fill(0);
    for (let i = 0; i < n; i++) {
        const d = t.charCodeAt(i) - 48;
        if (ptr[d] >= pos[d].length) return false;
        const idx = pos[d][ptr[d]];
        for (let k = 0; k < d; k++) {
            if (ptr[k] < pos[k].length && pos[k][ptr[k]] < idx) {
                return false;
            }
        }
        ptr[d]++;
    }
    return true;
};
```

## Typescript

```typescript
function isTransformable(s: string, t: string): boolean {
    const n = s.length;
    const queues: number[][] = Array.from({ length: 10 }, () => []);
    for (let i = 0; i < n; i++) {
        const d = s.charCodeAt(i) - 48;
        queues[d].push(i);
    }
    const heads = new Array(10).fill(0);
    for (let i = 0; i < n; i++) {
        const c = t.charCodeAt(i) - 48;
        if (heads[c] >= queues[c].length) return false;
        const idx = queues[c][heads[c]++];
        for (let d = 0; d < c; d++) {
            if (heads[d] < queues[d].length && queues[d][heads[d]] < idx) {
                return false;
            }
        }
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function isTransformable($s, $t) {
        $n = strlen($s);
        // queues for each digit 0-9 storing indices in s
        $queues = array_fill(0, 10, []);
        for ($i = 0; $i < $n; $i++) {
            $d = intval($s[$i]);
            $queues[$d][] = $i;
        }
        // pointers to the current front of each queue
        $ptr = array_fill(0, 10, 0);
        // precompute sizes for quick access
        $sizes = [];
        for ($d = 0; $d < 10; $d++) {
            $sizes[$d] = count($queues[$d]);
        }

        for ($i = 0; $i < $n; $i++) {
            $c = intval($t[$i]);
            if ($ptr[$c] >= $sizes[$c]) {
                return false;
            }
            $idx = $queues[$c][$ptr[$c]];
            // ensure no smaller digit appears before this index
            for ($d = 0; $d < $c; $d++) {
                if ($ptr[$d] < $sizes[$d] && $queues[$d][$ptr[$d]] < $idx) {
                    return false;
                }
            }
            $ptr[$c]++;
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func isTransformable(_ s: String, _ t: String) -> Bool {
        var positions = [[Int]](repeating: [], count: 10)
        for (i, scalar) in s.unicodeScalars.enumerated() {
            let d = Int(scalar.value - 48)
            positions[d].append(i)
        }
        var ptr = [Int](repeating: 0, count: 10)
        for scalar in t.unicodeScalars {
            let d = Int(scalar.value - 48)
            if ptr[d] >= positions[d].count { return false }
            let idx = positions[d][ptr[d]]
            // ensure no smaller digit is still before this index
            if d > 0 {
                for sd in 0..<d {
                    if ptr[sd] < positions[sd].count && positions[sd][ptr[sd]] < idx {
                        return false
                    }
                }
            }
            ptr[d] += 1
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isTransformable(s: String, t: String): Boolean {
        val n = s.length
        var i = 0
        val cnt = IntArray(10)
        for (ch in t) {
            val target = ch - '0'
            while (i < n && s[i] != ch) {
                cnt[s[i] - '0']++
                i++
            }
            if (i == n) return false
            for (d in 0 until target) {
                if (cnt[d] > 0) return false
            }
            i++ // use this character
        }
        return true
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  bool isTransformable(String s, String t) {
    int n = s.length;
    List<Queue<int>> queues = List.generate(10, (_) => Queue<int>());
    for (int i = 0; i < n; i++) {
      int d = s.codeUnitAt(i) - 48;
      queues[d].addLast(i);
    }
    for (int i = 0; i < n; i++) {
      int td = t.codeUnitAt(i) - 48;
      if (queues[td].isEmpty) return false;
      int pos = queues[td].removeFirst();
      for (int d = 0; d < td; d++) {
        if (queues[d].isNotEmpty && queues[d].first < pos) {
          return false;
        }
      }
    }
    return true;
  }
}
```

## Golang

```go
func isTransformable(s string, t string) bool {
	n := len(s)
	queues := make([][]int, 10)
	for i := 0; i < n; i++ {
		d := s[i] - '0'
		queues[d] = append(queues[d], i)
	}
	head := make([]int, 10)

	for i := 0; i < n; i++ {
		c := t[i] - '0'
		if head[c] >= len(queues[c]) {
			return false
		}
		pos := queues[c][head[c]]
		head[c]++

		for d := byte(0); d < c; d++ {
			if head[d] < len(queues[d]) && queues[d][head[d]] < pos {
				return false
			}
		}
	}
	return true
}
```

## Ruby

```ruby
def is_transformable(s, t)
  queues = Array.new(10) { [] }
  s.each_char.with_index do |ch, i|
    queues[ch.ord - 48] << i
  end

  t.each_char do |ch|
    d = ch.ord - 48
    return false if queues[d].empty?
    pos = queues[d].shift
    (0...d).each do |smaller|
      next if queues[smaller].empty?
      return false if queues[smaller][0] < pos
    end
  end
  true
end
```

## Scala

```scala
object Solution {
    def isTransformable(s: String, t: String): Boolean = {
        val n = s.length
        val cnt = new Array[Int](10)
        var i = 0
        var j = 0
        while (i < n) {
            while (j < n && s.charAt(j) != t.charAt(i)) {
                cnt(s.charAt(j) - '0') += 1
                j += 1
            }
            if (j == n) return false
            val target = t.charAt(i) - '0'
            var d = 0
            while (d < target) {
                if (cnt(d) > 0) return false
                d += 1
            }
            j += 1
            i += 1
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_transformable(s: String, t: String) -> bool {
        let n = s.len();
        let sb = s.as_bytes();
        let tb = t.as_bytes();

        let mut cnt = [0i32; 10];
        let (mut i, mut j) = (0usize, 0usize);

        while i < n {
            let d = (sb[i] - b'0') as usize;
            cnt[d] += 1;

            // try to match t as far as possible
            while j < n {
                let target = (tb[j] - b'0') as usize;
                if cnt[target] == 0 {
                    break;
                }
                // ensure no smaller digit is pending
                let mut ok = true;
                for d_small in 0..target {
                    if cnt[d_small] > 0 {
                        ok = false;
                        break;
                    }
                }
                if !ok {
                    break;
                }
                cnt[target] -= 1;
                j += 1;
            }

            i += 1;
        }

        // match any remaining characters in t
        while j < n {
            let target = (tb[j] - b'0') as usize;
            if cnt[target] == 0 {
                return false;
            }
            for d_small in 0..target {
                if cnt[d_small] > 0 {
                    return false;
                }
            }
            cnt[target] -= 1;
            j += 1;
        }

        true
    }
}
```

## Racket

```racket
(define/contract (is-transformable s t)
  (-> string? string? boolean?)
  (let* ((n (string-length s))
         (cnt (make-vector 10 0))
         (i 0))
    (let loop-j ((j 0))
      (if (= j n)
          #t
          (let ((target (- (char->integer (string-ref t j))
                           (char->integer #\0))))
            (let loop-inner ()
              (cond
                [(> (vector-ref cnt target) 0)
                 (vector-set! cnt target (- (vector-ref cnt target) 1))
                 (loop-j (+ j 1))]
                [(= i n) #f]
                [else
                 (define digit (- (char->integer (string-ref s i))
                                  (char->integer #\0)))
                 (if (< digit target)
                     #f
                     (begin
                       (vector-set! cnt digit (+ (vector-ref cnt digit) 1))
                       (set! i (+ i 1))
                       (loop-inner)))]))))))))
```

## Erlang

```erlang
-module(solution).
-export([is_transformable/2]).

-spec is_transformable(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> boolean().
is_transformable(S, T) ->
    SList = binary_to_list(S),
    TList = binary_to_list(T),
    Queues = build_queues(SList),
    process(TList, Queues).

%% Build queues of positions for each digit (0..9), earliest index first.
build_queues(SList) ->
    EmptyQueues = {[], [], [], [], [], [], [], [], [], []},
    RevQueues = build_queues(0, SList, EmptyQueues),
    % reverse each list to get ascending order
    {
        lists:reverse(element(1, RevQueues)),
        lists:reverse(element(2, RevQueues)),
        lists:reverse(element(3, RevQueues)),
        lists:reverse(element(4, RevQueues)),
        lists:reverse(element(5, RevQueues)),
        lists:reverse(element(6, RevQueues)),
        lists:reverse(element(7, RevQueues)),
        lists:reverse(element(8, RevQueues)),
        lists:reverse(element(9, RevQueues)),
        lists:reverse(element(10, RevQueues))
    }.

build_queues(_Idx, [], Queues) ->
    Queues;
build_queues(Idx, [H|Rest], Queues) ->
    D = H - $0,
    OldQ = element(D + 1, Queues),
    NewQ = [Idx | OldQ],
    NewQueues = setelement(D + 1, Queues, NewQ),
    build_queues(Idx + 1, Rest, NewQueues).

%% Process target string using the queues.
process([], _Queues) ->
    true;
process([H|RestT], Queues) ->
    D = H - $0,
    Qd = element(D + 1, Queues),
    case Qd of
        [] -> false;                     % no such digit left in source
        [Idx | QdRest] ->
            UpdatedQueues = setelement(D + 1, Queues, QdRest),
            case check_smaller(0, D - 1, Idx, UpdatedQueues) of
                true -> process(RestT, UpdatedQueues);
                false -> false
            end
    end.

%% Verify that no smaller digit has an earlier unused position.
check_smaller(Cur, Max, _Idx, _Queues) when Cur > Max ->
    true;
check_smaller(Cur, Max, Idx, Queues) ->
    Q = element(Cur + 1, Queues),
    case Q of
        [] -> check_smaller(Cur + 1, Max, Idx, Queues);
        [Front | _] when Front < Idx -> false;
        [_ | _] -> check_smaller(Cur + 1, Max, Idx, Queues)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_transformable(s :: String.t(), t :: String.t()) :: boolean()
  def is_transformable(s, t) do
    # Build queues of indices for each digit in s (ascending order)
    init_queues = Tuple.duplicate([], 10)

    queues_rev =
      Enum.reduce(Enum.with_index(String.graphemes(s)), init_queues, fn {ch, idx}, qs ->
        d = String.to_integer(ch)
        list = elem(qs, d)
        put_elem(qs, d, [idx | list])
      end)

    queues =
      0..9
      |> Enum.map(fn i -> List.reverse(elem(queues_rev, i)) end)
      |> List.to_tuple()

    t_chars = String.graphemes(t)

    result =
      Enum.reduce_while(Enum.with_index(t_chars), queues, fn {ch, _i}, qs ->
        d = String.to_integer(ch)
        list_d = elem(qs, d)

        case list_d do
          [] ->
            {:halt, false}

          [idx | rest] ->
            # Check if any smaller digit has an earlier unused index
            impossible =
              Enum.any?(0..(d - 1), fn c ->
                l = elem(qs, c)

                case l do
                  [] -> false
                  [h | _] -> h < idx
                end
              end)

            if impossible do
              {:halt, false}
            else
              new_qs = put_elem(qs, d, rest)
              {:cont, new_qs}
            end
        end
      end)

    result != false
  end
end
```
