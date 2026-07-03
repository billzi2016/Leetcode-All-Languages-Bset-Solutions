# 0228. Summary Ranges

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> res;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            int start = nums[i];
            while (i + 1 < n && nums[i + 1] == nums[i] + 1) {
                ++i;
            }
            int end = nums[i];
            if (start == end)
                res.push_back(to_string(start));
            else
                res.push_back(to_string(start) + "->" + to_string(end));
        }
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> result = new ArrayList<>();
        int n = nums.length;
        if (n == 0) return result;
        int start = nums[0];
        for (int i = 1; i <= n; i++) {
            // when reaching end or gap detected
            if (i == n || nums[i] != nums[i - 1] + 1) {
                int end = nums[i - 1];
                if (start == end) {
                    result.add(String.valueOf(start));
                } else {
                    result.add(start + "->" + end);
                }
                if (i < n) start = nums[i];
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        i = 0
        n = len(nums)
        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            end = nums[i]
            if start == end:
                res.append(str(start))
            else:
                res.append(f"{start}->{end}")
            i += 1
        return res
```

## Python3

```python
class Solution:
    def summaryRanges(self, nums):
        res = []
        i = 0
        n = len(nums)
        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            end = nums[i]
            if start == end:
                res.append(str(start))
            else:
                res.append(f"{start}->{end}")
            i += 1
        return res
```

## C

```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** summaryRanges(int* nums, int numsSize, int* returnSize) {
    if (numsSize == 0) {
        *returnSize = 0;
        return NULL;
    }
    
    char **result = (char **)malloc(numsSize * sizeof(char *));
    int count = 0;
    int i = 0;
    
    while (i < numsSize) {
        int start = nums[i];
        while (i + 1 < numsSize && nums[i + 1] == nums[i] + 1) {
            i++;
        }
        int end = nums[i];
        
        char buffer[50];
        int len;
        if (start == end) {
            len = snprintf(buffer, sizeof(buffer), "%d", start);
        } else {
            len = snprintf(buffer, sizeof(buffer), "%d->%d", start, end);
        }
        char *rangeStr = (char *)malloc(len + 1);
        strcpy(rangeStr, buffer);
        result[count++] = rangeStr;
        
        i++;
    }
    
    *returnSize = count;
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<string> SummaryRanges(int[] nums) {
        var res = new List<string>();
        int n = nums.Length;
        if (n == 0) return res;
        int start = nums[0];
        for (int i = 1; i <= n; i++) {
            bool endOfRange = i == n || nums[i] != nums[i - 1] + 1;
            if (endOfRange) {
                int end = nums[i - 1];
                if (start == end)
                    res.Add(start.ToString());
                else
                    res.Add($"{start}->{end}");
                if (i < n) start = nums[i];
            }
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
    const result = [];
    let i = 0;
    while (i < nums.length) {
        const start = nums[i];
        while (i + 1 < nums.length && nums[i + 1] === nums[i] + 1) {
            i++;
        }
        const end = nums[i];
        result.push(start === end ? `${start}` : `${start}->${end}`);
        i++;
    }
    return result;
};
```

## Typescript

```typescript
function summaryRanges(nums: number[]): string[] {
    const result: string[] = [];
    let i = 0;
    const n = nums.length;
    while (i < n) {
        const start = nums[i];
        while (i + 1 < n && nums[i + 1] === nums[i] + 1) {
            i++;
        }
        const end = nums[i];
        if (start === end) {
            result.push(`${start}`);
        } else {
            result.push(`${start}->${end}`);
        }
        i++;
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return String[]
     */
    function summaryRanges($nums) {
        $result = [];
        $n = count($nums);
        if ($n == 0) {
            return $result;
        }
        $start = $nums[0];
        for ($i = 0; $i < $n; $i++) {
            if ($i == $n - 1 || $nums[$i + 1] != $nums[$i] + 1) {
                $end = $nums[$i];
                if ($start == $end) {
                    $result[] = (string)$start;
                } else {
                    $result[] = $start . "->" . $end;
                }
                if ($i + 1 < $n) {
                    $start = $nums[$i + 1];
                }
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func summaryRanges(_ nums: [Int]) -> [String] {
        var res = [String]()
        var i = 0
        let n = nums.count
        while i < n {
            let start = nums[i]
            var end = start
            while i + 1 < n && nums[i + 1] == nums[i] + 1 {
                i += 1
                end = nums[i]
            }
            if start == end {
                res.append("\(start)")
            } else {
                res.append("\(start)->\(end)")
            }
            i += 1
        }
        return res
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun summaryRanges(nums: IntArray): List<String> {
        val result = mutableListOf<String>()
        var i = 0
        while (i < nums.size) {
            val start = nums[i]
            var end = start
            while (i + 1 < nums.size && nums[i + 1] == nums[i] + 1) {
                i++
                end = nums[i]
            }
            if (start == end) {
                result.add("$start")
            } else {
                result.add("$start->$end")
            }
            i++
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> summaryRanges(List<int> nums) {
    List<String> result = [];
    int n = nums.length;
    int i = 0;
    while (i < n) {
      int start = nums[i];
      while (i + 1 < n && nums[i + 1] == nums[i] + 1) {
        i++;
      }
      int end = nums[i];
      if (start == end) {
        result.add('$start');
      } else {
        result.add('$start->$end');
      }
      i++;
    }
    return result;
  }
}
```

## Golang

```go
func summaryRanges(nums []int) []string {
    n := len(nums)
    if n == 0 {
        return []string{}
    }
    res := make([]string, 0, n)
    i := 0
    for i < n {
        start := nums[i]
        for i+1 < n && nums[i+1] == nums[i]+1 {
            i++
        }
        end := nums[i]
        if start == end {
            res = append(res, fmt.Sprintf("%d", start))
        } else {
            res = append(res, fmt.Sprintf("%d->%d", start, end))
        }
        i++
    }
    return res
}
```

## Ruby

```ruby
def summary_ranges(nums)
  result = []
  i = 0
  n = nums.length
  while i < n
    start_val = nums[i]
    while i + 1 < n && nums[i + 1] == nums[i] + 1
      i += 1
    end
    end_val = nums[i]
    if start_val == end_val
      result << start_val.to_s
    else
      result << "#{start_val}->#{end_val}"
    end
    i += 1
  end
  result
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable.ListBuffer

    def summaryRanges(nums: Array[Int]): List[String] = {
        if (nums.isEmpty) return Nil
        val res = ListBuffer[String]()
        var start = nums(0)
        var prev = nums(0)

        for (i <- 1 until nums.length) {
            val cur = nums(i)
            if (cur == prev + 1) {
                // continue current range
            } else {
                if (start == prev) res += s"$start"
                else res += s"$start->$prev"
                start = cur
            }
            prev = cur
        }

        // add the final range
        if (start == prev) res += s"$start"
        else res += s"$start->$prev"

        res.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        let mut res = Vec::new();
        let n = nums.len();
        if n == 0 {
            return res;
        }
        let mut start = nums[0];
        for i in 1..=n {
            if i < n && nums[i] - nums[i - 1] == 1 {
                continue;
            } else {
                let end = nums[i - 1];
                if start == end {
                    res.push(start.to_string());
                } else {
                    res.push(format!("{}->{}", start, end));
                }
                if i < n {
                    start = nums[i];
                }
            }
        }
        res
    }
}
```

## Racket

```racket
(define (range-string a b)
  (if (= a b)
      (number->string a)
      (string-append (number->string a) "->" (number->string b))))

(define/contract (summary-ranges nums)
  (-> (listof exact-integer?) (listof string?))
  (let loop ((lst nums) (start #f) (prev #f) (acc '()))
    (cond
      [(null? lst)
       (if start
           (reverse (cons (range-string start prev) acc))
           (reverse acc))]
      [else
       (define cur (car lst))
       (if (and start (= cur (+ prev 1)))
           (loop (cdr lst) start cur acc)
           (let ((new-acc (if start
                              (cons (range-string start prev) acc)
                              acc)))
             (loop (cdr lst) cur cur new-acc)))])))
```

## Erlang

```erlang
-module(solution).
-export([summary_ranges/1]).

-spec summary_ranges(Nums :: [integer()]) -> [unicode:unicode_binary()].
summary_ranges([]) ->
    [];
summary_ranges([H|T]) ->
    lists:reverse(build(T, H, H, [])).

build([], Start, End, Acc) ->
    [format_range(Start, End) | Acc];
build([X|Rest], Start, Prev, Acc) when X =:= Prev + 1 ->
    build(Rest, Start, X, Acc);
build([X|Rest], Start, Prev, Acc) ->
    NewAcc = [format_range(Start, Prev) | Acc],
    build(Rest, X, X, NewAcc).

format_range(S, E) when S =:= E ->
    integer_to_binary(S);
format_range(S, E) ->
    << (integer_to_binary(S))/binary, "->", (integer_to_binary(E))/binary >>.
```

## Elixir

```elixir
defmodule Solution do
  @spec summary_ranges(nums :: [integer]) :: [String.t()]
  def summary_ranges([]), do: []

  def summary_ranges([head | tail]) do
    {ranges_rev, start_range, prev} =
      Enum.reduce(tail, {[], head, head}, fn num, {acc, s, p} ->
        if p + 1 == num do
          {acc, s, num}
        else
          range_str = format_range(s, p)
          {[range_str | acc], num, num}
        end
      end)

    final_range = format_range(start_range, prev)
    Enum.reverse([final_range | ranges_rev])
  end

  defp format_range(a, b) when a == b, do: Integer.to_string(a)
  defp format_range(a, b), do: "#{a}->#{b}"
end
```
