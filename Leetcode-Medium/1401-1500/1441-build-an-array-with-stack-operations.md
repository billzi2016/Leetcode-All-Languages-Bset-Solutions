# 1441. Build an Array With Stack Operations

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> ans;
        int cur = 1;
        for (int num : target) {
            while (cur < num) {
                ans.push_back("Push");
                ans.push_back("Pop");
                ++cur;
            }
            // now cur == num
            ans.push_back("Push");
            ++cur;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> ops = new ArrayList<>();
        int cur = 1;
        for (int num : target) {
            while (cur < num) {
                ops.add("Push");
                ops.add("Pop");
                cur++;
            }
            // now cur == num
            ops.add("Push");
            cur++;
        }
        return ops;
    }
}
```

## Python

```python
class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        ans = []
        i = 0  # last processed number
        for num in target:
            while i < num - 1:
                ans.append("Push")
                ans.append("Pop")
                i += 1
            ans.append("Push")
            i += 1
        return ans
```

## Python3

```python
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ops = []
        cur = 0
        for num in target:
            while cur < num - 1:
                ops.append("Push")
                ops.append("Pop")
                cur += 1
            ops.append("Push")
            cur += 1
        return ops
```

## C

```c
#include <stdlib.h>
#include <string.h>

static char *copy_str(const char *s) {
    size_t len = strlen(s);
    char *p = (char *)malloc(len + 1);
    if (p) memcpy(p, s, len + 1);
    return p;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** buildArray(int* target, int targetSize, int n, int* returnSize) {
    // Maximum possible operations is 2*n (Push+Pop for each number)
    char **ops = (char **)malloc(sizeof(char *) * 2 * n);
    int idx = 0;          // current number processed from stream
    int opCount = 0;      // total operations recorded

    for (int t = 0; t < targetSize; ++t) {
        int num = target[t];
        while (idx < num - 1) {
            ops[opCount++] = copy_str("Push");
            ops[opCount++] = copy_str("Pop");
            ++idx;
        }
        // now idx == num-1, push the needed number
        ops[opCount++] = copy_str("Push");
        ++idx;
    }

    *returnSize = opCount;
    return ops;
}
```

## Csharp

```csharp
public class Solution {
    public IList<string> BuildArray(int[] target, int n) {
        var ops = new List<string>();
        int cur = 1;
        foreach (int num in target) {
            while (cur < num) {
                ops.Add("Push");
                ops.Add("Pop");
                cur++;
            }
            ops.Add("Push");
            cur++;
        }
        return ops;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} target
 * @param {number} n
 * @return {string[]}
 */
var buildArray = function(target, n) {
    const ops = [];
    let cur = 1;
    for (const num of target) {
        while (cur < num) {
            ops.push("Push");
            ops.push("Pop");
            cur++;
        }
        // now cur === num
        ops.push("Push");
        cur++;
    }
    return ops;
};
```

## Typescript

```typescript
function buildArray(target: number[], n: number): string[] {
    const ops: string[] = [];
    let cur = 1;
    for (const num of target) {
        while (cur < num) {
            ops.push("Push");
            ops.push("Pop");
            cur++;
        }
        ops.push("Push");
        cur++;
    }
    return ops;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $target
     * @param Integer $n
     * @return String[]
     */
    function buildArray($target, $n) {
        $ans = [];
        $i = 0;
        foreach ($target as $num) {
            while ($i < $num - 1) {
                $ans[] = "Push";
                $ans[] = "Pop";
                $i++;
            }
            $ans[] = "Push";
            $i++;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func buildArray(_ target: [Int], _ n: Int) -> [String] {
        var ops = [String]()
        var current = 1
        for num in target {
            while current < num {
                ops.append("Push")
                ops.append("Pop")
                current += 1
            }
            ops.append("Push")
            current += 1
        }
        return ops
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun buildArray(target: IntArray, n: Int): List<String> {
        val ans = mutableListOf<String>()
        var i = 1
        for (num in target) {
            while (i < num) {
                ans.add("Push")
                ans.add("Pop")
                i++
            }
            // i == num
            ans.add("Push")
            i++
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<String> buildArray(List<int> target, int n) {
    List<String> ans = [];
    int cur = 1;
    for (int num in target) {
      while (cur < num) {
        ans.add('Push');
        ans.add('Pop');
        cur++;
      }
      ans.add('Push');
      cur++;
    }
    return ans;
  }
}
```

## Golang

```go
func buildArray(target []int, n int) []string {
    var res []string
    cur := 1
    for _, num := range target {
        for cur < num {
            res = append(res, "Push")
            res = append(res, "Pop")
            cur++
        }
        res = append(res, "Push")
        cur++
    }
    return res
}
```

## Ruby

```ruby
def build_array(target, n)
  ans = []
  i = 0
  target.each do |num|
    while i < num - 1
      ans << "Push"
      ans << "Pop"
      i += 1
    end
    ans << "Push"
    i += 1
  end
  ans
end
```

## Scala

```scala
object Solution {
  def buildArray(target: Array[Int], n: Int): List[String] = {
    val ops = scala.collection.mutable.ListBuffer[String]()
    var cur = 1
    for (num <- target) {
      while (cur < num) {
        ops += "Push"
        ops += "Pop"
        cur += 1
      }
      // now cur == num
      ops += "Push"
      cur += 1
    }
    ops.toList
  }
}
```

## Rust

```rust
impl Solution {
    pub fn build_array(target: Vec<i32>, _n: i32) -> Vec<String> {
        let mut ans: Vec<String> = Vec::new();
        let mut cur = 1;
        for &num in target.iter() {
            while cur < num {
                ans.push("Push".to_string());
                ans.push("Pop".to_string());
                cur += 1;
            }
            // now cur == num
            ans.push("Push".to_string());
            cur += 1;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (build-array target n)
  (-> (listof exact-integer?) exact-integer? (listof string?))
  (let ((ans '())
        (cur 0))
    (for ([num target])
      (for ([j (in-range (+ cur 1) num)])
        (set! ans (cons "Pop" (cons "Push" ans))))
      (set! ans (cons "Push" ans))
      (set! cur num))
    (reverse ans)))
```

## Erlang

```erlang
-module(solution).
-export([build_array/2]).

-spec build_array(Target :: [integer()], N :: integer()) -> [unicode:unicode_binary()].
build_array(Target, _N) ->
    lists:reverse(build_ops(Target, 0, [])).

%% Recursive processing of target list
build_ops([], _I, Acc) ->
    Acc;
build_ops([Num | Rest], I, Acc) ->
    {I1, Acc1} = discard_until(I, Num - 1, Acc),
    %% push the required number
    build_ops(Rest, I1 + 1, [<<"Push">> | Acc1]).

%% Add "Push","Pop" for numbers not in target
discard_until(I, TargetI, Acc) when I < TargetI ->
    discard_until(I + 1, TargetI, [<<"Pop">>, <<"Push">> | Acc]);
discard_until(I, _TargetI, Acc) ->
    {I, Acc}.
```

## Elixir

```elixir
defmodule Solution do
  @spec build_array(target :: [integer], n :: integer) :: [String.t]
  def build_array(target, _n) do
    {ops, _} =
      Enum.reduce(target, {[], 0}, fn num, {acc, i} ->
        acc =
          if i < num - 1 do
            missing = num - 1 - i

            extra_ops =
              Enum.flat_map(1..missing, fn _ -> ["Push", "Pop"] end)

            acc ++ extra_ops
          else
            acc
          end

        {acc ++ ["Push"], num}
      end)

    ops
  end
end
```
