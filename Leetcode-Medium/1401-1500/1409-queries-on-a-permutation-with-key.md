# 1409. Queries on a Permutation With Key

## Cpp

```cpp
class Solution {
public:
    vector<int> processQueries(vector<int>& queries, int m) {
        vector<int> perm(m);
        iota(perm.begin(), perm.end(), 1);
        vector<int> result;
        result.reserve(queries.size());
        for (int q : queries) {
            int idx = 0;
            while (perm[idx] != q) ++idx;
            result.push_back(idx);
            perm.erase(perm.begin() + idx);
            perm.insert(perm.begin(), q);
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] processQueries(int[] queries, int m) {
        List<Integer> perm = new ArrayList<>(m);
        for (int i = 1; i <= m; i++) {
            perm.add(i);
        }
        int[] result = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int q = queries[i];
            int idx = 0;
            while (perm.get(idx) != q) {
                idx++;
            }
            result[i] = idx;
            perm.remove(idx);
            perm.add(0, q);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        perm = list(range(1, m + 1))
        result = []
        for q in queries:
            idx = perm.index(q)
            result.append(idx)
            if idx != 0:
                perm.pop(idx)
                perm.insert(0, q)
        return result
```

## Python3

```python
from typing import List

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        perm = list(range(1, m + 1))
        result = []
        for q in queries:
            idx = perm.index(q)
            result.append(idx)
            # move to front
            if idx != 0:
                perm.pop(idx)
                perm.insert(0, q)
        return result
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* processQueries(int* queries, int queriesSize, int m, int* returnSize) {
    int* result = (int*)malloc(sizeof(int) * queriesSize);
    int* perm = (int*)malloc(sizeof(int) * m);
    for (int i = 0; i < m; ++i) {
        perm[i] = i + 1;
    }
    
    for (int i = 0; i < queriesSize; ++i) {
        int q = queries[i];
        int pos = 0;
        while (perm[pos] != q) {
            ++pos;
        }
        result[i] = pos;
        if (pos > 0) {
            // shift elements [0, pos-1] one step to the right
            memmove(&perm[1], &perm[0], sizeof(int) * pos);
            perm[0] = q;
        }
    }
    
    free(perm);
    *returnSize = queriesSize;
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] ProcessQueries(int[] queries, int m) {
        var perm = new List<int>(m);
        for (int i = 1; i <= m; i++) perm.Add(i);
        int n = queries.Length;
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            int q = queries[i];
            int idx = perm.IndexOf(q);
            result[i] = idx;
            if (idx > 0) {
                perm.RemoveAt(idx);
                perm.Insert(0, q);
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} queries
 * @param {number} m
 * @return {number[]}
 */
var processQueries = function(queries, m) {
    const perm = [];
    for (let i = 1; i <= m; i++) perm.push(i);
    const result = [];
    for (const q of queries) {
        const idx = perm.indexOf(q); // zero‑based position
        result.push(idx);
        perm.splice(idx, 1);
        perm.unshift(q);
    }
    return result;
};
```

## Typescript

```typescript
function processQueries(queries: number[], m: number): number[] {
    const perm = Array.from({ length: m }, (_, i) => i + 1);
    const result: number[] = [];
    for (const q of queries) {
        const idx = perm.indexOf(q); // zero‑based position
        result.push(idx);
        if (idx > 0) {
            perm.splice(idx, 1);
            perm.unshift(q);
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $queries
     * @param Integer $m
     * @return Integer[]
     */
    function processQueries($queries, $m) {
        $perm = range(1, $m);
        $result = [];

        foreach ($queries as $q) {
            $idx = array_search($q, $perm);
            $result[] = $idx;
            if ($idx > 0) {
                array_splice($perm, $idx, 1);
                array_unshift($perm, $q);
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func processQueries(_ queries: [Int], _ m: Int) -> [Int] {
        var perm = Array(1...m)
        var result = [Int]()
        for q in queries {
            if let idx = perm.firstIndex(of: q) {
                result.append(idx)
                perm.remove(at: idx)
                perm.insert(q, at: 0)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun processQueries(queries: IntArray, m: Int): IntArray {
        val permutation = MutableList(m) { it + 1 }
        val result = IntArray(queries.size)
        for (i in queries.indices) {
            val query = queries[i]
            val idx = permutation.indexOf(query)
            result[i] = idx
            permutation.removeAt(idx)
            permutation.add(0, query)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> processQueries(List<int> queries, int m) {
    List<int> perm = List.generate(m, (i) => i + 1);
    List<int> result = [];
    for (int q in queries) {
      int idx = perm.indexOf(q);
      result.add(idx);
      if (idx > 0) {
        perm.removeAt(idx);
        perm.insert(0, q);
      }
    }
    return result;
  }
}
```

## Golang

```go
func processQueries(queries []int, m int) []int {
	perm := make([]int, m)
	for i := 0; i < m; i++ {
		perm[i] = i + 1
	}
	result := make([]int, len(queries))
	for i, q := range queries {
		pos := 0
		for ; pos < m; pos++ {
			if perm[pos] == q {
				break
			}
		}
		result[i] = pos
		val := perm[pos]
		for j := pos; j > 0; j-- {
			perm[j] = perm[j-1]
		}
		perm[0] = val
	}
	return result
}
```

## Ruby

```ruby
def process_queries(queries, m)
  perm = (1..m).to_a
  result = []
  queries.each do |q|
    idx = perm.index(q)
    result << idx
    perm.delete_at(idx)
    perm.unshift(q)
  end
  result
end
```

## Scala

```scala
object Solution {
    def processQueries(queries: Array[Int], m: Int): Array[Int] = {
        val perm = scala.collection.mutable.ArrayBuffer[Int]()
        for (i <- 1 to m) perm += i
        val result = new Array[Int](queries.length)
        for (i <- queries.indices) {
            val q = queries(i)
            val idx = perm.indexOf(q) // zero‑based position
            result(i) = idx
            perm.remove(idx)
            perm.insert(0, q)
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn process_queries(queries: Vec<i32>, m: i32) -> Vec<i32> {
        let mut perm: Vec<i32> = (1..=m).collect();
        let mut ans = Vec::with_capacity(queries.len());
        for q in queries {
            let pos = perm.iter().position(|&x| x == q).unwrap() as i32;
            ans.push(pos);
            if pos != 0 {
                perm.remove(pos as usize);
                perm.insert(0, q);
            }
        }
        ans
    }
}
```

## Racket

```racket
#lang racket

(require rackunit) ; optional, can be omitted in submission

(define/contract (process-queries queries m)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (letrec
      ((find-index
        (lambda (lst val idx)
          (cond [(null? lst) -1] ; should never happen per constraints
                [(= (car lst) val) idx]
                [else (find-index (cdr lst) val (+ idx 1))])))
       
       (remove-first
        (lambda (lst val)
          (cond [(null? lst) '()]
                [(= (car lst) val) (cdr lst)]
                [else (cons (car lst) (remove-first (cdr lst) val))]))))
    
    (let loop ((qs queries)
               (perm (for/list ([i (in-range 1 (+ m 1))]) i))
               (acc '()))
      (if (null? qs)
          (reverse acc)
          (let* ((q (car qs))
                 (idx (find-index perm q 0))
                 (new-perm (cons q (remove-first perm q))))
            (loop (cdr qs) new-perm (cons idx acc)))))))
```

## Erlang

```erlang
-module(solution).
-export([process_queries/2]).
-spec process_queries(Queries :: [integer()], M :: integer()) -> [integer()].
process_queries(Queries, M) ->
    Perm0 = lists:seq(1, M),
    {ResRev, _} = lists:foldl(fun(Q, {Acc, Perm}) ->
        {Idx, NewPerm} = move_to_front(Q, Perm),
        {[Idx | Acc], NewPerm}
    end, {[], Perm0}, Queries),
    lists:reverse(ResRev).

move_to_front(Q, List) ->
    move_to_front(Q, List, 0, []).

move_to_front(Q, [Q|Rest], Index, PrefixRev) ->
    Prefix = lists:reverse(PrefixRev),
    NewList = [Q | Prefix ++ Rest],
    {Index, NewList};
move_to_front(Q, [H|T], Index, PrefixRev) ->
    move_to_front(Q, T, Index + 1, [H|PrefixRev]).
```

## Elixir

```elixir
defmodule Solution do
  @spec process_queries(queries :: [integer], m :: integer) :: [integer]
  def process_queries(queries, m) do
    perm = Enum.to_list(1..m)

    {rev_res, _} =
      Enum.reduce(queries, {[], perm}, fn q, {acc_rev, p} ->
        idx = Enum.find_index(p, &(&1 == q))
        new_p = [q] ++ List.delete_at(p, idx)
        {[idx | acc_rev], new_p}
      end)

    Enum.reverse(rev_res)
  end
end
```
