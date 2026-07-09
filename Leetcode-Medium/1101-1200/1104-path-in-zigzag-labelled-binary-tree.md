# 1104. Path In Zigzag Labelled Binary Tree

## Cpp

```cpp
class Solution {
public:
    vector<int> pathInZigZagTree(int label) {
        // Determine depth of the label
        int depth = 0;
        for (int x = label; x > 0; x >>= 1) ++depth;
        
        vector<int> path(depth);
        int cur = label;
        for (int lvl = depth; lvl >= 1; --lvl) {
            path[lvl - 1] = cur;
            
            // Convert current label to the "normal" left‑to‑right labeling
            int start = 1 << (lvl - 1);
            int end   = (1 << lvl) - 1;
            int normal = (lvl % 2 == 0) ? start + end - cur : cur;
            
            // Parent in the normal tree
            int parentNormal = normal >> 1;
            if (lvl > 1) {
                int pStart = 1 << (lvl - 2);
                int pEnd   = (1 << (lvl - 1)) - 1;
                // Convert back to zigzag labeling for the parent level
                cur = ((lvl - 1) % 2 == 0) ? pStart + pEnd - parentNormal : parentNormal;
            }
        }
        return path;
    }
};
```

## Java

```java
class Solution {
    public java.util.List<Integer> pathInZigZagTree(int label) {
        java.util.List<Integer> path = new java.util.ArrayList<>();
        int level = 0;
        long temp = label;
        while (temp > 0) {
            temp >>= 1;
            level++;
        }
        while (level >= 1) {
            path.add(label);
            long max = (1L << level) - 1;          // maximum label at this level
            long min = 1L << (level - 1);           // minimum label at this level
            long reversed = max + min - label;     // corresponding label if the row were normal
            label = (int)(reversed / 2);            // parent in the normal tree
            level--;
        }
        java.util.Collections.reverse(path);
        return path;
    }
}
```

## Python

```python
class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        path = []
        while label:
            path.append(label)
            lvl = label.bit_length() - 1  # level of current node (root at level 0)
            if lvl == 0:
                break
            # convert current zigzag label to normal label
            start = 1 << lvl
            end = (1 << (lvl + 1)) - 1
            if lvl % 2 == 1:  # reversed row
                norm = start + end - label
            else:
                norm = label
            # parent in a normal binary tree
            parent_norm = norm // 2
            plvl = lvl - 1
            pstart = 1 << plvl
            pend = (1 << (plvl + 1)) - 1
            if plvl % 2 == 1:  # reversed row for parent
                label = pstart + pend - parent_norm
            else:
                label = parent_norm
        return path[::-1]
```

## Python3

```python
import math
from typing import List

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        path = []
        while label:
            path.append(label)
            level = label.bit_length()  # depth of current node (1-indexed)
            start = 1 << (level - 1)
            end = (1 << level) - 1
            if level % 2 == 0:          # convert to normal labeling
                label = start + end - label
            label //= 2                 # move to parent in normal tree
            level -= 1                  # now at parent level
            if level and level % 2 == 0:
                start = 1 << (level - 1)
                end = (1 << level) - 1
                label = start + end - label   # convert back to zigzag labeling
        path.reverse()
        return path
```

## C

```c
#include <stdlib.h>

int* pathInZigZagTree(int label, int* returnSize) {
    // Determine depth (level) of the node
    int depth = 0;
    for (int x = label; x > 0; x >>= 1) ++depth;

    int *path = (int *)malloc(depth * sizeof(int));
    if (!path) {
        *returnSize = 0;
        return NULL;
    }

    int curLabel = label;
    for (int level = depth; level >= 1; --level) {
        path[level - 1] = curLabel;

        // If we have reached the root, stop
        if (level == 1) break;

        // Compute the "normal" label as if the tree were left‑to‑right
        int start = 1 << (level - 1);
        int end   = (1 << level) - 1;
        int normalLabel = (level % 2 == 0) ? (start + end - curLabel) : curLabel;

        // Parent in the normal tree
        int parentNormal = normalLabel >> 1;   // divide by 2

        // Convert back to zigzag label for the parent level
        int parentLevel = level - 1;
        int pStart = 1 << (parentLevel - 1);
        int pEnd   = (1 << parentLevel) - 1;
        curLabel = (parentLevel % 2 == 0) ? (pStart + pEnd - parentNormal) : parentNormal;
    }

    *returnSize = depth;
    return path;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> PathInZigZagTree(int label) {
        List<int> path = new List<int>();
        int level = 0;
        for (int n = label; n > 0; n >>= 1) level++;

        int cur = label;
        while (true) {
            path.Add(cur);
            if (cur == 1) break;

            // range of current level in normal order
            int start = 1 << (level - 1);
            int end = (1 << level) - 1;

            // convert to normal label if this level is reversed
            int normal = cur;
            if ((level & 1) == 0) {
                normal = start + end - cur;
            }

            // parent in normal order
            int parentNormal = normal >> 1;

            level--; // move up one level

            // range of parent level in normal order
            int pStart = 1 << (level - 1);
            int pEnd = (1 << level) - 1;

            // convert back to zigzag label if parent level is reversed
            int parentLabel = parentNormal;
            if ((level & 1) == 0) {
                parentLabel = pStart + pEnd - parentNormal;
            }

            cur = parentLabel;
        }

        path.Reverse();
        return path;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} label
 * @return {number[]}
 */
var pathInZigZagTree = function(label) {
    const path = [];
    while (label >= 1) {
        path.push(label);
        if (label === 1) break;
        const level = Math.floor(Math.log2(label)) + 1;
        const start = 1 << (level - 1);
        const end = (1 << level) - 1;
        // convert current label to its "normal" left‑to‑right label
        const normal = (level % 2 === 0) ? (start + end - label) : label;
        const parentNormal = Math.floor(normal / 2);
        const parentLevel = level - 1;
        if (parentLevel === 0) {
            label = 1;
        } else {
            const startP = 1 << (parentLevel - 1);
            const endP = (1 << parentLevel) - 1;
            // convert back to zigzag labeling for the parent
            label = (parentLevel % 2 === 0) ? (startP + endP - parentNormal) : parentNormal;
        }
    }
    return path.reverse();
};
```

## Typescript

```typescript
function pathInZigZagTree(label: number): number[] {
    const path: number[] = [];
    while (label >= 1) {
        path.push(label);
        const level = Math.floor(Math.log2(label)) + 1;
        const start = 1 << (level - 1);
        const end = (1 << level) - 1;
        label = Math.floor((start + end - label) / 2);
    }
    return path.reverse();
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $label
     * @return Integer[]
     */
    function pathInZigZagTree($label) {
        $path = [];
        while (true) {
            $path[] = $label;
            if ($label == 1) {
                break;
            }

            // compute level of current label
            $level = 0;
            $temp = $label;
            while ($temp > 0) {
                $temp >>= 1;
                $level++;
            }

            // range for this level
            $start = 1 << ($level - 1);
            $end   = (1 << $level) - 1;

            // convert to normal label if current level is reversed
            if (($level & 1) == 0) {
                $labelNormal = $start + $end - $label;
            } else {
                $labelNormal = $label;
            }

            // parent in normal tree
            $parentNormal = intdiv($labelNormal, 2);
            $parentLevel = $level - 1;

            // range for parent level
            $startParent = 1 << ($parentLevel - 1);
            $endParent   = (1 << $parentLevel) - 1;

            // convert back to zigzag label if parent level is reversed
            if (($parentLevel & 1) == 0) {
                $label = $startParent + $endParent - $parentNormal;
            } else {
                $label = $parentNormal;
            }
        }

        return array_reverse($path);
    }
}
```

## Swift

```swift
import Foundation

class Solution {
    func pathInZigZagTree(_ label: Int) -> [Int] {
        var result = [Int]()
        var cur = label
        while true {
            result.append(cur)
            if cur == 1 { break }
            let level = Int(log2(Double(cur)))
            let start = 1 << level
            let end = (1 << (level + 1)) - 1
            cur = (start + end - cur) / 2
        }
        return result.reversed()
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun pathInZigZagTree(label: Int): List<Int> {
        var cur = label
        val res = mutableListOf<Int>()
        while (true) {
            res.add(cur)
            if (cur == 1) break
            val level = 32 - Integer.numberOfLeadingZeros(cur)
            val max = (1 shl level) - 1
            val min = 1 shl (level - 1)
            cur = (max + min - cur) / 2
        }
        res.reverse()
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<int> pathInZigZagTree(int label) {
    List<int> res = [];
    while (label >= 1) {
      res.add(label);
      if (label == 1) break;
      int level = label.bitLength;
      int start = 1 << (level - 1);
      int end = (1 << level) - 1;
      int normalLabel = (level % 2 == 0) ? (start + end - label) : label;
      int parentNormal = normalLabel >> 1;
      int parentLevel = level - 1;
      if (parentLevel == 0) {
        label = 1;
        continue;
      }
      int startParent = 1 << (parentLevel - 1);
      int endParent = (1 << parentLevel) - 1;
      int parentLabel = (parentLevel % 2 == 0)
          ? (startParent + endParent - parentNormal)
          : parentNormal;
      label = parentLabel;
    }
    return res.reversed.toList();
  }
}
```

## Golang

```go
import "math/bits"

func pathInZigZagTree(label int) []int {
	if label <= 0 {
		return nil
	}
	res := []int{}
	for label > 0 {
		res = append(res, label)
		level := bits.Len(uint(label)) - 1

		var normal int
		if level%2 == 1 {
			start := 1 << level
			end := (1 << (level + 1)) - 1
			normal = start + end - label
		} else {
			normal = label
		}

		normal = normal / 2
		if normal == 0 {
			break
		}
		level--
		if level%2 == 1 {
			start := 1 << level
			end := (1 << (level + 1)) - 1
			label = start + end - normal
		} else {
			label = normal
		}
	}
	for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
		res[i], res[j] = res[j], res[i]
	}
	return res
}
```

## Ruby

```ruby
def path_in_zig_zag_tree(label)
  path = []
  while label > 0
    path << label
    level = label.bit_length
    if level.even?
      max = (1 << level) - 1
      min = 1 << (level - 1)
      label = (max + min - label) / 2
    else
      label /= 2
    end
  end
  path.reverse!
end
```

## Scala

```scala
object Solution {
    def pathInZigZagTree(label: Int): List[Int] = {
        var cur = label
        val buf = scala.collection.mutable.ListBuffer[Int]()
        while (cur > 0) {
            buf += cur
            val level = 31 - Integer.numberOfLeadingZeros(cur)
            cur = (( (1 << (level + 1)) - 1) + (1 << level) - cur) / 2
        }
        buf.reverse.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn path_in_zig_zag_tree(label: i32) -> Vec<i32> {
        let mut res = Vec::new();
        let mut cur = label as i64;

        // compute initial level (depth)
        let mut level = 0;
        let mut temp = cur;
        while temp > 0 {
            level += 1;
            temp >>= 1;
        }

        while cur >= 1 {
            res.push(cur as i32);
            if cur == 1 {
                break;
            }
            // convert current label to its "normal" (left‑to‑right) value
            let start = 1i64 << (level - 1);
            let end = (1i64 << level) - 1;
            let normal = if level % 2 == 0 {
                start + end - cur
            } else {
                cur
            };
            // parent in the normal tree
            let parent_normal = normal / 2;

            // move up one level
            level -= 1;
            let p_start = 1i64 << (level - 1);
            let p_end = (1i64 << level) - 1;
            cur = if level % 2 == 0 {
                p_start + p_end - parent_normal
            } else {
                parent_normal
            };
        }

        res.reverse();
        res
    }
}
```

## Racket

```racket
(define/contract (path-in-zig-zag-tree label)
  (-> exact-integer? (listof exact-integer?))
  (let loop ((lbl label) (acc '()))
    (if (< lbl 1)
        (reverse acc)
        (let* ((lvl (sub1 (integer-length lbl)))               ; floor(log2(lbl))
               (start (arithmetic-shift 1 lvl))                ; 2^lvl
               (end (sub1 (arithmetic-shift 1 (+ lvl 1))))    ; 2^(lvl+1)-1
               (mirror (+ start (- end lbl)))                 ; mirrored label in normal order
               (parent (quotient mirror 2)))                  ; move to parent
          (loop parent (cons lbl acc))))))
```

## Erlang

```erlang
-module(solution).
-export([path_in_zig_zag_tree/1]).

-spec path_in_zig_zag_tree(Label :: integer()) -> [integer()].
path_in_zig_zag_tree(Label) ->
    build_path(Label, []).

build_path(0, Acc) ->
    lists:reverse(Acc);
build_path(Label, Acc) ->
    Level = bit_len(Label),
    Min = 1 bsl (Level - 1),
    Max = (1 bsl Level) - 1,
    Normal = if
        Level rem 2 == 0 -> Max + Min - Label;
        true -> Label
    end,
    ParentNormal = Normal div 2,
    NextLevel = Level - 1,
    ParentZigzag = case NextLevel of
        0 -> 0;
        _ ->
            MinP = 1 bsl (NextLevel - 1),
            MaxP = (1 bsl NextLevel) - 1,
            if
                NextLevel rem 2 == 0 -> MaxP + MinP - ParentNormal;
                true -> ParentNormal
            end
    end,
    build_path(ParentZigzag, [Label | Acc]).

bit_len(N) when N > 0 ->
    bit_len(N, 0).
bit_len(0, Acc) ->
    Acc;
bit_len(N, Acc) ->
    bit_len(N bsr 1, Acc + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec path_in_zig_zag_tree(label :: integer) :: [integer]
  def path_in_zig_zag_tree(label) do
    build_path(label, [])
  end

  defp build_path(1, acc), do: [1 | acc]

  defp build_path(label, acc) do
    level = (:math.log2(label) |> :math.floor() |> trunc()) + 1

    start = 1 <<< (level - 1)
    finish = (1 <<< level) - 1

    norm_label =
      if rem(level, 2) == 0 do
        start + finish - label
      else
        label
      end

    norm_parent = div(norm_label, 2)

    parent_level = level - 1

    p_start = 1 <<< (parent_level - 1)
    p_finish = (1 <<< parent_level) - 1

    parent_label =
      if rem(parent_level, 2) == 0 do
        p_start + p_finish - norm_parent
      else
        norm_parent
      end

    build_path(parent_label, [label | acc])
  end
end
```
