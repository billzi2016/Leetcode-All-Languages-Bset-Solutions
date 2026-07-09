# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings

## Cpp

```cpp
class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
        vector<int> ans;
        ans.reserve(seq.size());
        int depth = 0;
        for (char c : seq) {
            if (c == '(') {
                depth++;
                ans.push_back(depth % 2);
            } else { // ')'
                ans.push_back(depth % 2);
                depth--;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] maxDepthAfterSplit(String seq) {
        int n = seq.length();
        int[] ans = new int[n];
        int depth = 0;
        for (int i = 0; i < n; i++) {
            char c = seq.charAt(i);
            if (c == '(') {
                depth++;
                ans[i] = depth % 2;
            } else { // ')'
                ans[i] = depth % 2;
                depth--;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        ans = []
        depth = 0
        for ch in seq:
            if ch == '(':
                depth += 1
                ans.append(depth % 2)
            else:  # ')'
                ans.append(depth % 2)
                depth -= 1
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = []
        depth = 0
        for ch in seq:
            if ch == '(':
                depth += 1
                ans.append(depth % 2)
            else:
                ans.append(depth % 2)
                depth -= 1
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxDepthAfterSplit(char* seq, int* returnSize) {
    int n = (int)strlen(seq);
    int *ans = (int*)malloc(n * sizeof(int));
    int depth = 0;
    for (int i = 0; i < n; ++i) {
        if (seq[i] == '(') {
            depth++;
            ans[i] = depth % 2;
        } else { // ')'
            ans[i] = depth % 2;
            depth--;
        }
    }
    *returnSize = n;
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] MaxDepthAfterSplit(string seq) {
        int n = seq.Length;
        int[] answer = new int[n];
        int depth = 0;
        for (int i = 0; i < n; i++) {
            if (seq[i] == '(') {
                answer[i] = depth % 2;
                depth++;
            } else { // ')'
                depth--;
                answer[i] = depth % 2;
            }
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} seq
 * @return {number[]}
 */
var maxDepthAfterSplit = function(seq) {
    const ans = new Array(seq.length);
    let depth = 0;
    for (let i = 0; i < seq.length; i++) {
        if (seq[i] === '(') {
            ans[i] = depth % 2;
            depth++;
        } else { // ')'
            depth--;
            ans[i] = depth % 2;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function maxDepthAfterSplit(seq: string): number[] {
    const ans: number[] = new Array(seq.length);
    let depth = 0;
    for (let i = 0; i < seq.length; i++) {
        if (seq[i] === '(') {
            ans[i] = depth % 2;
            depth++;
        } else { // ')'
            depth--;
            ans[i] = depth % 2;
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $seq
     * @return Integer[]
     */
    function maxDepthAfterSplit($seq) {
        $depth = 0;
        $ans = [];
        $n = strlen($seq);
        for ($i = 0; $i < $n; $i++) {
            if ($seq[$i] === '(') {
                $group = $depth % 2;
                $ans[] = $group;
                $depth++;
            } else { // ')'
                $depth--;
                $group = $depth % 2;
                $ans[] = $group;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func maxDepthAfterSplit(_ seq: String) -> [Int] {
        var depth = 0
        var ans = [Int]()
        ans.reserveCapacity(seq.count)
        for ch in seq {
            if ch == "(" {
                depth += 1
                ans.append(depth % 2)
            } else { // ')'
                ans.append(depth % 2)
                depth -= 1
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxDepthAfterSplit(seq: String): IntArray {
        val n = seq.length
        val ans = IntArray(n)
        var depth = 0
        for (i in 0 until n) {
            if (seq[i] == '(') {
                depth++
                ans[i] = depth % 2
            } else {
                ans[i] = depth % 2
                depth--
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> maxDepthAfterSplit(String seq) {
    int depth = 0;
    List<int> ans = List.filled(seq.length, 0);
    for (int i = 0; i < seq.length; i++) {
      if (seq[i] == '(') {
        depth++;
        ans[i] = depth % 2;
      } else {
        ans[i] = depth % 2;
        depth--;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func maxDepthAfterSplit(seq string) []int {
    n := len(seq)
    ans := make([]int, n)
    depth := 0
    for i := 0; i < n; i++ {
        if seq[i] == '(' {
            ans[i] = depth % 2
            depth++
        } else { // ')'
            depth--
            ans[i] = depth % 2
        }
    }
    return ans
}
```

## Ruby

```ruby
def max_depth_after_split(seq)
  result = []
  depth = 0
  seq.each_char do |ch|
    if ch == '('
      depth += 1
      result << (depth % 2)
    else
      result << (depth % 2)
      depth -= 1
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def maxDepthAfterSplit(seq: String): Array[Int] = {
        val n = seq.length
        val ans = new Array[Int](n)
        var depth = 0
        for (i <- 0 until n) {
            if (seq(i) == '(') {
                depth += 1
                ans(i) = depth % 2
            } else {
                ans(i) = depth % 2
                depth -= 1
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_depth_after_split(seq: String) -> Vec<i32> {
        let mut ans = Vec::with_capacity(seq.len());
        let mut depth = 0;
        for ch in seq.chars() {
            if ch == '(' {
                depth += 1;
                ans.push((depth % 2) as i32);
            } else { // ')'
                ans.push((depth % 2) as i32);
                depth -= 1;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (max-depth-after-split seq)
  (-> string? (listof exact-integer?))
  (let* ((n (string-length seq))
         (res (make-vector n)))
    (let loop ((i 0) (depth 0))
      (if (= i n)
          (vector->list res)
          (let ((ch (string-ref seq i)))
            (cond
              [(char=? ch #\()
               (set! depth (+ depth 1))
               (vector-set! res i (modulo depth 2))
               (loop (+ i 1) depth)]
              [(char=? ch #\))
               (vector-set! res i (modulo depth 2))
               (set! depth (- depth 1))
               (loop (+ i 1) depth)]))))))
```

## Erlang

```erlang
-module(solution).
-export([max_depth_after_split/1]).

-spec max_depth_after_split(Seq :: unicode:unicode_binary()) -> [integer()].
max_depth_after_split(Seq) ->
    List = binary_to_list(Seq),
    RevRes = split(List, 0, []),
    lists:reverse(RevRes).

split([], _Depth, Acc) ->
    Acc;
split([$( | Rest], Depth, Acc) ->
    NewDepth = Depth + 1,
    Assign = NewDepth rem 2,
    split(Rest, NewDepth, [Assign | Acc]);
split([$) | Rest], Depth, Acc) ->
    Assign = Depth rem 2,
    NewDepth = Depth - 1,
    split(Rest, NewDepth, [Assign | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec max_depth_after_split(seq :: String.t) :: [integer]
  def max_depth_after_split(seq) do
    {_, rev_res} =
      seq
      |> String.graphemes()
      |> Enum.reduce({0, []}, fn ch, {depth, acc} ->
        case ch do
          "(" ->
            new_depth = depth + 1
            assign = rem(new_depth, 2)
            {new_depth, [assign | acc]}

          ")" ->
            assign = rem(depth, 2)
            new_depth = depth - 1
            {new_depth, [assign | acc]}
        end
      end)

    Enum.reverse(rev_res)
  end
end
```
