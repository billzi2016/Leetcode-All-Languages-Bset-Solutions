# 2343. Query Kth Smallest Trimmed Number

## Cpp

```cpp
class Solution {
public:
    vector<int> smallestTrimmedNumbers(vector<string>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        int L = nums[0].size();
        vector<int> answer;
        answer.reserve(queries.size());
        for (const auto& q : queries) {
            int k = q[0];
            int trim = q[1];
            vector<pair<string,int>> v;
            v.reserve(n);
            for (int i = 0; i < n; ++i) {
                v.emplace_back(nums[i].substr(L - trim), i);
            }
            auto cmp = [&](const pair<string,int>& a, const pair<string,int>& b) {
                const string& sa = a.first;
                const string& sb = b.first;
                int ia = 0, ib = 0;
                while (ia < (int)sa.size() && sa[ia] == '0') ++ia;
                while (ib < (int)sb.size() && sb[ib] == '0') ++ib;
                int lena = (int)sa.size() - ia;
                int lenb = (int)sb.size() - ib;
                if (lena != lenb) return lena < lenb;
                for (int p = 0; p < lena; ++p) {
                    char ca = sa[ia + p];
                    char cb = sb[ib + p];
                    if (ca != cb) return ca < cb;
                }
                return a.second < b.second;
            };
            sort(v.begin(), v.end(), cmp);
            answer.push_back(v[k - 1].second);
        }
        return answer;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] smallestTrimmedNumbers(String[] nums, int[][] queries) {
        int n = nums.length;
        int len = nums[0].length();
        String[][] trimmed = new String[len + 1][n];
        for (int t = 1; t <= len; ++t) {
            int start = len - t;
            for (int i = 0; i < n; ++i) {
                trimmed[t][i] = nums[i].substring(start);
            }
        }

        int[] answer = new int[queries.length];
        Integer[] idx = new Integer[n];

        for (int q = 0; q < queries.length; ++q) {
            int k = queries[q][0];
            int tr = queries[q][1];

            for (int i = 0; i < n; ++i) idx[i] = i;

            Arrays.sort(idx, (a, b) -> {
                String sa = trimmed[tr][a];
                String sb = trimmed[tr][b];
                int cmp = sa.compareTo(sb);
                if (cmp != 0) return cmp;
                return a - b; // tie‑break by original index
            });

            answer[q] = idx[k - 1];
        }

        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = []
        for k, trim in queries:
            trimmed_with_idx = [(int(num[-trim:]), idx) for idx, num in enumerate(nums)]
            trimmed_with_idx.sort(key=lambda x: (x[0], x[1]))
            result.append(trimmed_with_idx[k - 1][1])
        return result
```

## Python3

```python
from typing import List

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        for k, trim in queries:
            trimmed = [(int(num[-trim:]), idx) for idx, num in enumerate(nums)]
            trimmed.sort(key=lambda x: (x[0], x[1]))
            result.append(trimmed[k - 1][1])
        return result
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int idx;
    const char *suf;
} Node;

static int cmpNode(const void *a, const void *b) {
    const Node *na = (const Node *)a;
    const Node *nb = (const Node *)b;
    int c = strcmp(na->suf, nb->suf);
    if (c != 0) return c;
    return na->idx - nb->idx;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* smallestTrimmedNumbers(char** nums, int numsSize, int** queries, int queriesSize,
                            int* queriesColSize, int* returnSize) {
    *returnSize = queriesSize;
    int *answer = (int *)malloc(sizeof(int) * queriesSize);
    if (!answer) return NULL;

    int len = strlen(nums[0]);  // all strings have same length

    for (int q = 0; q < queriesSize; ++q) {
        int k = queries[q][0];
        int trim = queries[q][1];

        Node *arr = (Node *)malloc(sizeof(Node) * numsSize);
        for (int i = 0; i < numsSize; ++i) {
            arr[i].idx = i;
            arr[i].suf = nums[i] + len - trim;
        }

        qsort(arr, numsSize, sizeof(Node), cmpNode);
        answer[q] = arr[k - 1].idx;

        free(arr);
    }
    return answer;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] SmallestTrimmedNumbers(string[] nums, int[][] queries) {
        int n = nums.Length;
        int qlen = queries.Length;
        int[] answer = new int[qlen];
        for (int qi = 0; qi < qlen; ++qi) {
            int k = queries[qi][0];
            int trim = queries[qi][1];
            var list = new List<(string stripped, int idx)>(n);
            for (int i = 0; i < n; ++i) {
                string trimmed = nums[i].Substring(nums[i].Length - trim);
                int pos = 0;
                while (pos < trimmed.Length && trimmed[pos] == '0') pos++;
                string stripped = pos == trimmed.Length ? "0" : trimmed.Substring(pos);
                list.Add((stripped, i));
            }
            list.Sort((a, b) => {
                if (a.stripped.Length != b.stripped.Length)
                    return a.stripped.Length - b.stripped.Length;
                int cmp = string.Compare(a.stripped, b.stripped, StringComparison.Ordinal);
                if (cmp != 0) return cmp;
                return a.idx - b.idx;
            });
            answer[qi] = list[k - 1].idx;
        }
        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var smallestTrimmedNumbers = function(nums, queries) {
    const n = nums.length;
    const result = [];
    for (const [k, trim] of queries) {
        const list = new Array(n);
        for (let i = 0; i < n; ++i) {
            const trimmed = nums[i].slice(-trim);
            list[i] = { trimmed, idx: i };
        }
        list.sort((a, b) => {
            if (a.trimmed < b.trimmed) return -1;
            if (a.trimmed > b.trimmed) return 1;
            return a.idx - b.idx;
        });
        result.push(list[k - 1].idx);
    }
    return result;
};
```

## Typescript

```typescript
function smallestTrimmedNumbers(nums: string[], queries: number[][]): number[] {
    const n = nums.length;
    const answer: number[] = [];
    for (const [k, trim] of queries) {
        const list: { idx: number; val: bigint }[] = [];
        for (let i = 0; i < n; ++i) {
            const trimmed = nums[i].slice(-trim);
            const val = BigInt(trimmed);
            list.push({ idx: i, val });
        }
        list.sort((a, b) => {
            if (a.val < b.val) return -1;
            if (a.val > b.val) return 1;
            return a.idx - b.idx;
        });
        answer.push(list[k - 1].idx);
    }
    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $nums
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function smallestTrimmedNumbers($nums, $queries) {
        $n = count($nums);
        $answers = [];
        foreach ($queries as $q) {
            [$k, $trim] = $q;
            $list = [];
            for ($i = 0; $i < $n; $i++) {
                $trimmed = substr($nums[$i], -$trim);
                $list[] = ['val' => $trimmed, 'idx' => $i];
            }
            usort($list, function ($a, $b) {
                $sa = ltrim($a['val'], '0');
                $sb = ltrim($b['val'], '0');
                if ($sa === '') $sa = '0';
                if ($sb === '') $sb = '0';
                $lenA = strlen($sa);
                $lenB = strlen($sb);
                if ($lenA !== $lenB) {
                    return $lenA <=> $lenB;
                }
                if ($sa !== $sb) {
                    return $sa <=> $sb;
                }
                return $a['idx'] <=> $b['idx'];
            });
            $answers[] = $list[$k - 1]['idx'];
        }
        return $answers;
    }
}
```

## Swift

```swift
class Solution {
    func smallestTrimmedNumbers(_ nums: [String], _ queries: [[Int]]) -> [Int] {
        var answers = [Int]()
        let n = nums.count
        for query in queries {
            let k = query[0]
            let trim = query[1]
            var trimmedList = [(trim: String, index: Int)]()
            trimmedList.reserveCapacity(n)
            for (i, num) in nums.enumerated() {
                let start = num.index(num.endIndex, offsetBy: -trim)
                let trimmed = String(num[start...])
                trimmedList.append((trimmed, i))
            }
            trimmedList.sort { a, b in
                if a.trim == b.trim {
                    return a.index < b.index
                } else {
                    return a.trim < b.trim
                }
            }
            answers.append(trimmedList[k - 1].index)
        }
        return answers
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestTrimmedNumbers(nums: Array<String>, queries: Array<IntArray>): IntArray {
        val n = nums.size
        val len = nums[0].length
        val answer = IntArray(queries.size)
        for ((idx, q) in queries.withIndex()) {
            val k = q[0]
            val trim = q[1]
            // Build list of (trimmedString, originalIndex)
            val list = Array(n) { i ->
                Pair(nums[i].substring(len - trim), i)
            }
            list.sortWith(compareBy<Pair<String, Int>>({ it.first }, { it.second }))
            answer[idx] = list[k - 1].second
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  List<int> smallestTrimmedNumbers(List<String> nums, List<List<int>> queries) {
    int n = nums.length;
    int len = nums[0].length;
    List<int> answer = [];

    for (var query in queries) {
      int k = query[0];
      int trim = query[1];

      // Build list of pairs (original index, trimmed string)
      List<MapEntry<int, String>> paired = List.generate(
        n,
        (i) => MapEntry(i, nums[i].substring(len - trim)),
      );

      // Sort by trimmed value, then by original index
      paired.sort((a, b) {
        int cmp = a.value.compareTo(b.value);
        if (cmp != 0) return cmp;
        return a.key.compareTo(b.key);
      });

      answer.add(paired[k - 1].key);
    }

    return answer;
  }
}
```

## Golang

```go
import "sort"

func smallestTrimmedNumbers(nums []string, queries [][]int) []int {
	n := len(nums)
	ans := make([]int, len(queries))
	m := len(nums[0])

	for i, q := range queries {
		k, t := q[0], q[1]
		start := m - t

		type pair struct {
			val string
			idx int
		}
		arr := make([]pair, n)
		for j, s := range nums {
			arr[j] = pair{s[start:], j}
		}

		sort.Slice(arr, func(a, b int) bool {
			if arr[a].val != arr[b].val {
				return arr[a].val < arr[b].val
			}
			return arr[a].idx < arr[b].idx
		})

		ans[i] = arr[k-1].idx
	}

	return ans
}
```

## Ruby

```ruby
def smallest_trimmed_numbers(nums, queries)
  n = nums.length
  m = nums[0].length
  trimmed = Array.new(m + 1) { Array.new(n) }
  (1..m).each do |t|
    (0...n).each do |i|
      trimmed[t][i] = nums[i][-t, t].to_i
    end
  end

  answers = []
  queries.each do |k, t|
    order = (0...n).map { |i| [trimmed[t][i], i] }
    order.sort_by! { |val, idx| [val, idx] }
    answers << order[k - 1][1]
  end
  answers
end
```

## Scala

```scala
object Solution {
    def smallestTrimmedNumbers(nums: Array[String], queries: Array[Array[Int]]): Array[Int] = {
        val n = nums.length
        val len = if (n > 0) nums(0).length else 0
        val answers = new Array[Int](queries.length)

        for (qi <- queries.indices) {
            val k = queries(qi)(0)
            val trim = queries(qi)(1)

            // Trim each number to its last `trim` characters
            val trimmed = nums.map(s => s.substring(len - trim))

            // Indices 0 .. n-1
            val indices = (0 until n).toArray

            // Sort by trimmed value, then by original index
            val sorted = indices.sortBy(i => (trimmed(i), i))

            answers(qi) = sorted(k - 1)
        }

        answers
    }
}
```

## Rust

```rust
use std::cmp::Ordering;

impl Solution {
    pub fn smallest_trimmed_numbers(nums: Vec<String>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len();
        let mut answers = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let k = q[0] as usize;
            let trim = q[1] as usize;
            let mut arr: Vec<(usize, String)> = (0..n)
                .map(|i| {
                    let s = &nums[i];
                    let trimmed = if trim >= s.len() {
                        s.clone()
                    } else {
                        s[s.len() - trim..].to_string()
                    };
                    (i, trimmed)
                })
                .collect();
            arr.sort_by(|a, b| {
                let ord = Self::numeric_cmp(&a.1, &b.1);
                if ord != Ordering::Equal {
                    ord
                } else {
                    a.0.cmp(&b.0)
                }
            });
            answers.push(arr[k - 1].0 as i32);
        }
        answers
    }

    fn numeric_cmp(a: &str, b: &str) -> Ordering {
        let a_trim = a.trim_start_matches('0');
        let b_trim = b.trim_start_matches('0');
        match a_trim.len().cmp(&b_trim.len()) {
            Ordering::Equal => {
                let ord = a_trim.cmp(b_trim);
                if ord == Ordering::Equal { Ordering::Equal } else { ord }
            }
            other => other,
        }
    }
}
```

## Racket

```racket
#lang racket
(require racket/list)

(define/contract (smallest-trimmed-numbers nums queries)
  (-> (listof string?) (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([len (string-length (first nums))])
    (map
     (lambda (q)
       (define k (first q))
       (define trim (second q))
       (define pairs
         (map-indexed
          (lambda (i s)
            (define sub (substring s (- len trim) len))
            (list (string->number sub) i))
          nums))
       (define sorted
         (sort pairs
               (lambda (a b)
                 (let ([va (first a)] [vb (first b)]
                       [ia (second a)] [ib (second b)])
                   (if (< va vb) #t
                       (if (= va vb) (< ia ib) #f))))))
       (second (list-ref sorted (- k 1))))
     queries)))
```

## Erlang

```erlang
-module(solution).
-export([smallest_trimmed_numbers/2]).

-spec smallest_trimmed_numbers(Nums :: [unicode:unicode_binary()], Queries :: [[integer()]]) -> [integer()].
smallest_trimmed_numbers(Nums, Queries) ->
    lists:map(
        fun([K, Trim]) ->
            Sorted = sort_by_trim(Nums, Trim),
            {_, Index} = lists:nth(K, Sorted),
            Index
        end,
        Queries).

%% Build and sort list of {TrimmedValue, OriginalIndex}
-spec sort_by_trim([unicode:unicode_binary()], integer()) -> [{integer(), integer()}].
sort_by_trim(Nums, Trim) ->
    List = build_list(Nums, Trim, 0, []),
    lists:sort(
        fun({V1, I1}, {V2, I2}) ->
            if
                V1 == V2 -> I1 < I2;
                true     -> V1 < V2
            end
        end,
        List).

-spec build_list([unicode:unicode_binary()], integer(), integer(), [{integer(), integer()}]) -> [{integer(), integer()}].
build_list([], _Trim, _Idx, Acc) ->
    Acc;
build_list([Num | Rest], Trim, Idx, Acc) ->
    Size = byte_size(Num),
    Start = Size - Trim,
    <<_:Start/binary, Suffix:Trim/binary>> = Num,
    Value = binary_to_integer(Suffix),
    build_list(Rest, Trim, Idx + 1, [{Value, Idx} | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_trimmed_numbers(nums :: [String.t()], queries :: [[integer]]) :: [integer]
  def smallest_trimmed_numbers(nums, queries) do
    Enum.map(queries, fn [k, trim] ->
      trimmed =
        nums
        |> Enum.with_index()
        |> Enum.map(fn {s, idx} ->
          sub = String.slice(s, -trim, trim)
          val = String.to_integer(sub)
          {val, idx}
        end)

      sorted = Enum.sort_by(trimmed, fn {val, idx} -> {val, idx} end)
      {_val, ans_idx} = Enum.at(sorted, k - 1)
      ans_idx
    end)
  end
end
```
