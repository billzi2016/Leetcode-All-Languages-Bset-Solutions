# 0179. Largest Number

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> strs;
        strs.reserve(nums.size());
        for (int num : nums) strs.push_back(to_string(num));
        sort(strs.begin(), strs.end(),
             [](const string& a, const string& b) { return a + b > b + a; });
        string result;
        for (const string& s : strs) result += s;
        if (!result.empty() && result[0] == '0') return "0";
        return result;
    }
};
```

## Java

```java
class Solution {
    public String largestNumber(int[] nums) {
        if (nums == null || nums.length == 0) return "";
        String[] strs = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            strs[i] = String.valueOf(nums[i]);
        }
        java.util.Arrays.sort(strs, (a, b) -> (b + a).compareTo(a + b));
        if (strs[0].charAt(0) == '0') return "0";
        StringBuilder sb = new StringBuilder();
        for (String s : strs) sb.append(s);
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key
        strs = list(map(str, nums))
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        strs.sort(key=cmp_to_key(compare))
        result = ''.join(strs)
        return '0' if result and result[0] == '0' else result
```

## Python3

```python
from typing import List
import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert integers to strings for concatenation comparison
        strs = list(map(str, nums))
        
        # Comparator: order by which concatenation yields larger number
        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1  # a should come before b
            elif a + b < b + a:
                return 1   # b should come before a
            else:
                return 0
        
        strs.sort(key=functools.cmp_to_key(compare))
        
        # Edge case: if the highest number is '0', all numbers are zero
        if strs and strs[0] == "0":
            return "0"
        return "".join(strs)
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

static int cmp(const void *p1, const void *p2) {
    const char *s1 = *(const char **)p1;
    const char *s2 = *(const char **)p2;
    char ab[22], ba[22];
    sprintf(ab, "%s%s", s1, s2);
    sprintf(ba, "%s%s", s2, s1);
    return strcmp(ba, ab); // descending order based on concatenation
}

char* largestNumber(int* nums, int numsSize) {
    if (numsSize == 0) {
        char *empty = malloc(1);
        empty[0] = '\0';
        return empty;
    }

    char **arr = (char **)malloc(numsSize * sizeof(char *));
    int total_len = 0;

    for (int i = 0; i < numsSize; ++i) {
        char buf[12];
        sprintf(buf, "%d", nums[i]);
        int len = strlen(buf);
        arr[i] = (char *)malloc(len + 1);
        strcpy(arr[i], buf);
        total_len += len;
    }

    qsort(arr, numsSize, sizeof(char *), cmp);

    if (arr[0][0] == '0') {
        for (int i = 0; i < numsSize; ++i) free(arr[i]);
        free(arr);
        char *zero = (char *)malloc(2);
        zero[0] = '0';
        zero[1] = '\0';
        return zero;
    }

    char *result = (char *)malloc(total_len + 1);
    result[0] = '\0';
    for (int i = 0; i < numsSize; ++i) {
        strcat(result, arr[i]);
        free(arr[i]);
    }
    free(arr);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public string LargestNumber(int[] nums)
    {
        string[] strNums = new string[nums.Length];
        for (int i = 0; i < nums.Length; i++)
            strNums[i] = nums[i].ToString();

        Array.Sort(strNums, (a, b) => (b + a).CompareTo(a + b));

        if (strNums.Length == 0 || strNums[0] == "0")
            return "0";

        var sb = new System.Text.StringBuilder();
        foreach (var s in strNums)
            sb.Append(s);
        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    const strs = nums.map(String);
    strs.sort((a, b) => {
        const ab = a + b;
        const ba = b + a;
        if (ba > ab) return 1;
        if (ba < ab) return -1;
        return 0;
    });
    const result = strs.join('');
    return result[0] === '0' ? '0' : result;
};
```

## Typescript

```typescript
function largestNumber(nums: number[]): string {
    const strs = nums.map(String);
    strs.sort((a, b) => {
        const order1 = a + b;
        const order2 = b + a;
        if (order1 === order2) return 0;
        return order1 > order2 ? -1 : 1;
    });
    const result = strs.join('');
    return result[0] === '0' ? '0' : result;
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param Integer[] $nums
     * @return String
     */
    function largestNumber($nums) {
        $strs = array_map('strval', $nums);
        usort($strs, function($a, $b) {
            return strcmp($b . $a, $a . $b);
        });
        if ($strs[0] === "0") {
            return "0";
        }
        return implode('', $strs);
    }
}
?>
```

## Swift

```swift
class Solution {
    func largestNumber(_ nums: [Int]) -> String {
        let strs = nums.map { String($0) }
        let sorted = strs.sorted { $0 + $1 > $1 + $0 }
        let result = sorted.joined()
        if result.first == "0" {
            return "0"
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun largestNumber(nums: IntArray): String {
        val strs = nums.map { it.toString() }.sortedWith(Comparator { a, b ->
            (b + a).compareTo(a + b)
        })
        if (strs.isNotEmpty() && strs[0] == "0") return "0"
        return strs.joinToString("")
    }
}
```

## Dart

```dart
class Solution {
  String largestNumber(List<int> nums) {
    List<String> strs = nums.map((e) => e.toString()).toList();
    strs.sort((a, b) {
      int cmp = (b + a).compareTo(a + b);
      // We want descending order based on concatenation.
      // If a+b > b+a, a should come before b -> return -1.
      if (cmp == 0) return 0;
      return cmp;
    });
    if (strs.isNotEmpty && strs[0] == '0') {
      return '0';
    }
    return strs.join();
  }
}
```

## Golang

```go
package main

import (
	"sort"
	"strconv"
	"strings"
)

func largestNumber(nums []int) string {
	strs := make([]string, len(nums))
	for i, v := range nums {
		strs[i] = strconv.Itoa(v)
	}
	sort.Slice(strs, func(i, j int) bool {
		return strs[i]+strs[j] > strs[j]+strs[i]
	})
	if len(strs) == 0 || strs[0] == "0" {
		return "0"
	}
	var sb strings.Builder
	for _, s := range strs {
		sb.WriteString(s)
	}
	return sb.String()
}
```

## Ruby

```ruby
def largest_number(nums)
  strs = nums.map(&:to_s)
  strs.sort! { |a, b| (b + a) <=> (a + b) }
  result = strs.join
  result[0] == '0' ? '0' : result
end
```

## Scala

```scala
object Solution {
    def largestNumber(nums: Array[Int]): String = {
        val strs = nums.map(_.toString)
        val sorted = strs.sortWith { (a, b) => (a + b) > (b + a) }
        val result = sorted.mkString
        if (result.nonEmpty && result.charAt(0) == '0') "0" else result
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn largest_number(nums: Vec<i32>) -> String {
        let mut strs: Vec<String> = nums.iter().map(|&x| x.to_string()).collect();
        strs.sort_by(|a, b| {
            let ab = a.clone() + b;
            let ba = b.clone() + a;
            ba.cmp(&ab)
        });
        if let Some(first) = strs.first() {
            if first == "0" {
                return "0".to_string();
            }
        }
        strs.concat()
    }
}
```

## Racket

```racket
(define/contract (largest-number nums)
  (-> (listof exact-integer?) string?)
  (let* ([strs   (map number->string nums)]
         [sorted (sort strs
                       (lambda (a b)
                         (string>? (string-append a b)
                                    (string-append b a))))])
    (if (and (pair? sorted) (string=? (first sorted) "0"))
        "0"
        (apply string-append sorted))))
```

## Erlang

```erlang
-module(solution).
-export([largest_number/1]).

-spec largest_number(Nums :: [integer()]) -> unicode:unicode_binary().
largest_number(Nums) ->
    Strs = [integer_to_list(N) || N <- Nums],
    Sorted = lists:sort(fun(A, B) -> (A ++ B) > (B ++ A) end, Strs),
    case Sorted of
        [] -> <<"">>;
        ["0"|_] -> <<"0">>;
        _ ->
            ResultList = lists:foldl(fun(S, Acc) -> Acc ++ S end, [], Sorted),
            list_to_binary(ResultList)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec largest_number(nums :: [integer]) :: String.t()
  def largest_number(nums) do
    strs = Enum.map(nums, &Integer.to_string/1)

    sorted =
      Enum.sort(strs, fn a, b ->
        a <> b > b <> a
      end)

    case List.first(sorted) do
      "0" -> "0"
      _ -> Enum.join(sorted)
    end
  end
end
```
