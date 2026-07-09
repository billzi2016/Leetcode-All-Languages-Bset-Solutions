# 0763. Partition Labels

## Cpp

```cpp
class Solution {
public:
    vector<int> partitionLabels(string s) {
        int n = s.size();
        vector<int> last(26, -1);
        for (int i = 0; i < n; ++i) {
            last[s[i] - 'a'] = i;
        }
        vector<int> result;
        int start = 0, end = 0;
        for (int i = 0; i < n; ++i) {
            end = max(end, last[s[i] - 'a']);
            if (i == end) {
                result.push_back(i - start + 1);
                start = i + 1;
            }
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> partitionLabels(String s) {
        int[] last = new int[26];
        for (int i = 0; i < s.length(); i++) {
            last[s.charAt(i) - 'a'] = i;
        }
        List<Integer> result = new ArrayList<>();
        int start = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {
            end = Math.max(end, last[s.charAt(i) - 'a']);
            if (i == end) {
                result.add(i - start + 1);
                start = i + 1;
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # Record last occurrence for each character
        last = [0] * 26
        for i, ch in enumerate(s):
            last[ord(ch) - ord('a')] = i

        res = []
        start = end = 0
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if last[idx] > end:
                end = last[idx]
            if i == end:
                res.append(i - start + 1)
                start = i + 1
        return res
```

## Python3

```python
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Record the last index for each character
        last = [0] * 26
        for i, ch in enumerate(s):
            last[ord(ch) - ord('a')] = i

        partitions = []
        start = end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ord(ch) - ord('a')])
            if i == end:
                partitions.append(i - start + 1)
                start = i + 1
        return partitions
```

## C

```c
#include <stdlib.h>
#include <string.h>

int* partitionLabels(char* s, int* returnSize) {
    if (!s) {
        *returnSize = 0;
        return NULL;
    }
    int len = (int)strlen(s);
    int last[26];
    for (int i = 0; i < 26; ++i) last[i] = -1;
    for (int i = 0; i < len; ++i) {
        last[s[i] - 'a'] = i;
    }
    
    int *res = (int *)malloc(len * sizeof(int));
    int cnt = 0;
    int start = 0, end = 0;
    for (int i = 0; i < len; ++i) {
        int idx = s[i] - 'a';
        if (last[idx] > end) end = last[idx];
        if (i == end) {
            res[cnt++] = i - start + 1;
            start = i + 1;
        }
    }
    *returnSize = cnt;
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<int> PartitionLabels(string s)
    {
        int[] last = new int[26];
        for (int i = 0; i < s.Length; i++)
        {
            last[s[i] - 'a'] = i;
        }

        List<int> result = new List<int>();
        int start = 0, end = 0;

        for (int i = 0; i < s.Length; i++)
        {
            int idx = s[i] - 'a';
            if (last[idx] > end)
                end = last[idx];

            if (i == end)
            {
                result.Add(i - start + 1);
                start = i + 1;
            }
        }

        return result;
    }
}
```

## Javascript

```javascript
var partitionLabels = function(s) {
    const last = new Array(26).fill(-1);
    for (let i = 0; i < s.length; i++) {
        last[s.charCodeAt(i) - 97] = i;
    }
    const result = [];
    let start = 0, end = 0;
    for (let i = 0; i < s.length; i++) {
        const idx = s.charCodeAt(i) - 97;
        if (last[idx] > end) end = last[idx];
        if (i === end) {
            result.push(end - start + 1);
            start = i + 1;
        }
    }
    return result;
};
```

## Typescript

```typescript
function partitionLabels(s: string): number[] {
    const last = new Array(26).fill(-1);
    for (let i = 0; i < s.length; i++) {
        last[s.charCodeAt(i) - 97] = i;
    }
    const result: number[] = [];
    let start = 0, end = 0;
    for (let i = 0; i < s.length; i++) {
        const idx = s.charCodeAt(i) - 97;
        if (last[idx] > end) end = last[idx];
        if (i === end) {
            result.push(end - start + 1);
            start = i + 1;
        }
    }
    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @return Integer[]
     */
    function partitionLabels($s) {
        $n = strlen($s);
        $last = array_fill(0, 26, -1);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97;
            $last[$idx] = $i;
        }
        $result = [];
        $start = 0;
        $end = 0;
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97;
            if ($last[$idx] > $end) {
                $end = $last[$idx];
            }
            if ($i == $end) {
                $result[] = $i - $start + 1;
                $start = $i + 1;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func partitionLabels(_ s: String) -> [Int] {
        let chars = Array(s)
        var last = Array(repeating: -1, count: 26)
        for (i, ch) in chars.enumerated() {
            let idx = Int(ch.unicodeScalars.first!.value - 97)
            last[idx] = i
        }
        var result: [Int] = []
        var start = 0
        var end = 0
        for (i, ch) in chars.enumerated() {
            let idx = Int(ch.unicodeScalars.first!.value - 97)
            end = max(end, last[idx])
            if i == end {
                result.append(i - start + 1)
                start = i + 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun partitionLabels(s: String): List<Int> {
        val last = IntArray(26)
        for (i in s.indices) {
            last[s[i] - 'a'] = i
        }
        val res = mutableListOf<Int>()
        var start = 0
        var end = 0
        for (i in s.indices) {
            val idx = s[i] - 'a'
            if (last[idx] > end) end = last[idx]
            if (i == end) {
                res.add(i - start + 1)
                start = i + 1
            }
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<int> partitionLabels(String s) {
    // Record the last occurrence of each character.
    List<int> last = List.filled(26, -1);
    for (int i = 0; i < s.length; i++) {
      int idx = s.codeUnitAt(i) - 97;
      last[idx] = i;
    }

    List<int> result = [];
    int start = 0;
    int end = 0;

    for (int i = 0; i < s.length; i++) {
      int idx = s.codeUnitAt(i) - 97;
      if (last[idx] > end) {
        end = last[idx];
      }
      if (i == end) {
        result.add(end - start + 1);
        start = i + 1;
      }
    }

    return result;
  }
}
```

## Golang

```go
func partitionLabels(s string) []int {
	last := [26]int{}
	for i, ch := range s {
		last[ch-'a'] = i
	}
	var result []int
	start, end := 0, 0
	for i, ch := range s {
		if last[ch-'a'] > end {
			end = last[ch-'a']
		}
		if i == end {
			result = append(result, i-start+1)
			start = i + 1
		}
	}
	return result
}
```

## Ruby

```ruby
def partition_labels(s)
  last = Array.new(26, 0)
  s.each_char.with_index { |ch, i| last[ch.ord - 97] = i }
  res = []
  start_idx = 0
  end_idx = 0
  s.each_char.with_index do |ch, i|
    idx = ch.ord - 97
    end_idx = [end_idx, last[idx]].max
    if i == end_idx
      res << (i - start_idx + 1)
      start_idx = i + 1
    end
  end
  res
end
```

## Scala

```scala
object Solution {
    def partitionLabels(s: String): List[Int] = {
        val last = Array.fill(26)(-1)
        for (i <- s.indices) {
            last(s.charAt(i) - 'a') = i
        }
        var start = 0
        var end = 0
        val res = scala.collection.mutable.ListBuffer[Int]()
        for (i <- s.indices) {
            val idx = s.charAt(i) - 'a'
            if (last(idx) > end) end = last(idx)
            if (i == end) {
                res += (end - start + 1)
                start = i + 1
            }
        }
        res.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn partition_labels(s: String) -> Vec<i32> {
        let bytes = s.as_bytes();
        let mut last = [0usize; 26];
        for (i, &b) in bytes.iter().enumerate() {
            last[(b - b'a') as usize] = i;
        }

        let mut res: Vec<i32> = Vec::new();
        let mut start = 0usize;
        let mut end = 0usize;

        for (i, &b) in bytes.iter().enumerate() {
            let idx = (b - b'a') as usize;
            if last[idx] > end {
                end = last[idx];
            }
            if i == end {
                res.push((end - start + 1) as i32);
                start = i + 1;
            }
        }

        res
    }
}
```

## Racket

```racket
(define/contract (partition-labels s)
  (-> string? (listof exact-integer?))
  (let* ((n (string-length s))
         (last (make-vector 26 -1)))
    ;; Record last occurrence of each character
    (for ([i (in-range n)])
      (let* ((c (string-ref s i))
             (idx (- (char->integer c) (char->integer #\a))))
        (vector-set! last idx i)))
    ;; Build partitions greedily
    (let loop ((i 0) (start 0) (end 0) (acc '()))
      (if (= i n)
          (reverse acc)
          (let* ((c (string-ref s i))
                 (idx (- (char->integer c) (char->integer #\a)))
                 (lastIdx (vector-ref last idx))
                 (newEnd (max end lastIdx)))
            (if (= i newEnd)
                (loop (+ i 1) (+ i 1) (+ i 1)
                      (cons (+ 1 (- i start)) acc))
                (loop (+ i 1) start newEnd acc)))))))
```

## Erlang

```erlang
-module(solution).
-export([partition_labels/1]).

-spec partition_label(binary()) -> [integer()] .
partition_label(_S) ->
    [].

-spec partition_labels(binary()) -> [integer()].
partition_labels(S) when is_binary(S) ->
    LastMap = build_last(S),
    go(S, 0, 0, 0, LastMap, []).

build_last(Bin) -> build_last(Bin, 0, #{}).

build_last(<<>>, _Idx, Acc) -> Acc;
build_last(<<Byte, Rest/binary>>, Idx, Acc) ->
    Char = Byte - $a,
    NewAcc = maps:put(Char, Idx, Acc),
    build_last(Rest, Idx + 1, NewAcc).

go(<<>>, _I, _Start, _End, _LastMap, Acc) -> lists:reverse(Acc);
go(<<Byte, Rest/binary>>, I, Start, End, LastMap, Acc) ->
    Char = Byte - $a,
    LastPos = maps:get(Char, LastMap),
    NewEnd = if
        LastPos > End -> LastPos;
        true -> End
    end,
    case I of
        NewEnd when I == NewEnd ->
            Size = NewEnd - Start + 1,
            go(Rest, I + 1, I + 1, I + 1, LastMap, [Size | Acc]);
        _ ->
            go(Rest, I + 1, Start, NewEnd, LastMap, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec partition_labels(s :: String.t()) :: [integer]
  def partition_labels(s) do
    chars = String.graphemes(s)

    last_map =
      Enum.with_index(chars, fn ch, idx -> {ch, idx} end)
      |> Enum.reduce(%{}, fn {ch, idx}, acc -> Map.put(acc, ch, idx) end)

    {result, _, _} =
      Enum.reduce(Enum.with_index(chars), {[], 0, 0},
        fn {ch, idx}, {res, start_idx, cur_end} ->
          new_end = max(cur_end, Map.get(last_map, ch))

          if idx == new_end do
            size = idx - start_idx + 1
            {[size | res], idx + 1, new_end}
          else
            {res, start_idx, new_end}
          end
        end)

    Enum.reverse(result)
  end
end
```
