# 0433. Minimum Genetic Mutation

## Cpp

```cpp
class Solution {
public:
    int minMutation(string startGene, string endGene, vector<string>& bank) {
        unordered_set<string> valid(bank.begin(), bank.end());
        if (valid.find(endGene) == valid.end()) return -1;
        if (startGene == endGene) return 0;
        
        const char chars[4] = {'A','C','G','T'};
        queue<pair<string,int>> q;
        q.push({startGene, 0});
        unordered_set<string> visited;
        visited.insert(startGene);
        
        while (!q.empty()) {
            auto [curr, steps] = q.front();
            q.pop();
            for (int i = 0; i < 8; ++i) {
                char original = curr[i];
                for (char c : chars) {
                    if (c == original) continue;
                    curr[i] = c;
                    if (curr == endGene) return steps + 1;
                    if (valid.count(curr) && !visited.count(curr)) {
                        visited.insert(curr);
                        q.push({curr, steps + 1});
                    }
                }
                curr[i] = original;
            }
        }
        return -1;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int minMutation(String startGene, String endGene, String[] bank) {
        Set<String> bankSet = new HashSet<>(Arrays.asList(bank));
        if (!bankSet.contains(endGene)) return -1;
        char[] genes = {'A', 'C', 'G', 'T'};
        Queue<String> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        queue.offer(startGene);
        visited.add(startGene);
        int steps = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String cur = queue.poll();
                if (cur.equals(endGene)) return steps;
                char[] arr = cur.toCharArray();
                for (int pos = 0; pos < 8; pos++) {
                    char original = arr[pos];
                    for (char g : genes) {
                        if (g == original) continue;
                        arr[pos] = g;
                        String next = new String(arr);
                        if (bankSet.contains(next) && !visited.contains(next)) {
                            visited.add(next);
                            queue.offer(next);
                        }
                    }
                    arr[pos] = original;
                }
            }
            steps++;
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        from collections import deque

        if startGene == endGene:
            return 0

        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        genes = ['A', 'C', 'G', 'T']
        visited = set([startGene])
        q = deque([(startGene, 0)])

        while q:
            cur, steps = q.popleft()
            for i in range(8):
                for g in genes:
                    if g == cur[i]:
                        continue
                    nxt = cur[:i] + g + cur[i+1:]
                    if nxt == endGene:
                        return steps + 1
                    if nxt in bank_set and nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps + 1))
        return -1
```

## Python3

```python
from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        genes = ['A', 'C', 'G', 'T']
        visited = set([startGene])
        q = deque([(startGene, 0)])

        while q:
            cur, steps = q.popleft()
            for i in range(8):
                original = cur[i]
                for g in genes:
                    if g == original:
                        continue
                    nxt = cur[:i] + g + cur[i+1:]
                    if nxt == endGene:
                        return steps + 1
                    if nxt in bank_set and nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps + 1))
        return -1
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static int diff(const char *a, const char *b) {
    int cnt = 0;
    for (int i = 0; i < 8; ++i) {
        if (a[i] != b[i]) {
            if (++cnt > 1) return cnt;
        }
    }
    return cnt;
}

int minMutation(char* startGene, char* endGene, char** bank, int bankSize) {
    bool found = false;
    for (int i = 0; i < bankSize; ++i) {
        if (strcmp(bank[i], endGene) == 0) { found = true; break; }
    }
    if (!found) return -1;

    bool *visited = (bool *)calloc(bankSize, sizeof(bool));

    int capacity = bankSize + 2;
    char **qGene = (char **)malloc(sizeof(char *) * capacity);
    int *qStep = (int *)malloc(sizeof(int) * capacity);
    int front = 0, rear = 0;

    qGene[rear] = startGene;
    qStep[rear] = 0;
    ++rear;

    while (front < rear) {
        char *gene = qGene[front];
        int steps = qStep[front];
        ++front;

        if (strcmp(gene, endGene) == 0) {
            free(visited);
            free(qGene);
            free(qStep);
            return steps;
        }

        for (int i = 0; i < bankSize; ++i) {
            if (!visited[i] && diff(gene, bank[i]) == 1) {
                visited[i] = true;
                qGene[rear] = bank[i];
                qStep[rear] = steps + 1;
                ++rear;
            }
        }
    }

    free(visited);
    free(qGene);
    free(qStep);
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int MinMutation(string startGene, string endGene, string[] bank) {
        var bankSet = new HashSet<string>(bank);
        if (!bankSet.Contains(endGene)) return -1;

        var visited = new HashSet<string>();
        var queue = new Queue<(string gene, int steps)>();
        queue.Enqueue((startGene, 0));
        visited.Add(startGene);

        char[] nucleotides = new char[] { 'A', 'C', 'G', 'T' };

        while (queue.Count > 0) {
            var (gene, steps) = queue.Dequeue();
            if (gene == endGene) return steps;

            char[] arr = gene.ToCharArray();
            for (int i = 0; i < arr.Length; i++) {
                char original = arr[i];
                foreach (char n in nucleotides) {
                    if (n == original) continue;
                    arr[i] = n;
                    string mutated = new string(arr);
                    if (bankSet.Contains(mutated) && !visited.Contains(mutated)) {
                        visited.Add(mutated);
                        queue.Enqueue((mutated, steps + 1));
                    }
                }
                arr[i] = original;
            }
        }

        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} startGene
 * @param {string} endGene
 * @param {string[]} bank
 * @return {number}
 */
var minMutation = function(startGene, endGene, bank) {
    const bankSet = new Set(bank);
    if (!bankSet.has(endGene)) return -1;
    if (startGene === endGene) return 0;

    const chars = ['A', 'C', 'G', 'T'];
    const visited = new Set([startGene]);
    const queue = [[startGene, 0]]; // [gene, steps]

    while (queue.length) {
        const [gene, steps] = queue.shift();
        if (gene === endGene) return steps;

        for (let i = 0; i < gene.length; i++) {
            for (const c of chars) {
                if (c === gene[i]) continue;
                const mutated = gene.slice(0, i) + c + gene.slice(i + 1);
                if (bankSet.has(mutated) && !visited.has(mutated)) {
                    visited.add(mutated);
                    queue.push([mutated, steps + 1]);
                }
            }
        }
    }

    return -1;
};
```

## Typescript

```typescript
function minMutation(startGene: string, endGene: string, bank: string[]): number {
    if (startGene === endGene) return 0;
    const bankSet = new Set(bank);
    if (!bankSet.has(endGene)) return -1;

    const chars = ['A', 'C', 'G', 'T'];
    const visited = new Set<string>();
    visited.add(startGene);

    const queue: [string, number][] = [[startGene, 0]];
    let idx = 0;
    while (idx < queue.length) {
        const [gene, steps] = queue[idx++];
        for (let i = 0; i < gene.length; i++) {
            for (const c of chars) {
                if (c === gene[i]) continue;
                const mutated = gene.slice(0, i) + c + gene.slice(i + 1);
                if (!bankSet.has(mutated) || visited.has(mutated)) continue;
                if (mutated === endGene) return steps + 1;
                visited.add(mutated);
                queue.push([mutated, steps + 1]);
            }
        }
    }
    return -1;
}
```

## Php

```php
class Solution {
    /**
     * @param String $startGene
     * @param String $endGene
     * @param String[] $bank
     * @return Integer
     */
    function minMutation($startGene, $endGene, $bank) {
        if ($startGene === $endGene) {
            return 0;
        }
        $bankSet = array_flip($bank);
        if (!isset($bankSet[$endGene])) {
            return -1;
        }

        $queue = new SplQueue();
        $queue->enqueue([$startGene, 0]);
        $visited = [$startGene => true];
        $genes = ['A', 'C', 'G', 'T'];

        while (!$queue->isEmpty()) {
            [$curr, $steps] = $queue->dequeue();

            for ($i = 0; $i < 8; $i++) {
                foreach ($genes as $g) {
                    if ($curr[$i] === $g) continue;
                    $next = substr_replace($curr, $g, $i, 1);
                    if (!isset($bankSet[$next]) || isset($visited[$next])) continue;

                    if ($next === $endGene) {
                        return $steps + 1;
                    }

                    $visited[$next] = true;
                    $queue->enqueue([$next, $steps + 1]);
                }
            }
        }

        return -1;
    }
}
```

## Swift

```swift
class Solution {
    func minMutation(_ startGene: String, _ endGene: String, _ bank: [String]) -> Int {
        if startGene == endGene { return 0 }
        let bankSet = Set(bank)
        if !bankSet.contains(endGene) { return -1 }
        
        let chars: [Character] = ["A", "C", "G", "T"]
        var visited = Set<String>()
        var queue: [(String, Int)] = []
        var head = 0
        
        queue.append((startGene, 0))
        visited.insert(startGene)
        
        while head < queue.count {
            let (gene, steps) = queue[head]
            head += 1
            
            var arr = Array(gene)
            for i in 0..<arr.count {
                let original = arr[i]
                for c in chars where c != original {
                    arr[i] = c
                    let newGene = String(arr)
                    if bankSet.contains(newGene) && !visited.contains(newGene) {
                        if newGene == endGene { return steps + 1 }
                        visited.insert(newGene)
                        queue.append((newGene, steps + 1))
                    }
                }
                arr[i] = original
            }
        }
        
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minMutation(startGene: String, endGene: String, bank: Array<String>): Int {
        val bankSet = bank.toHashSet()
        if (!bankSet.contains(endGene)) return -1
        if (startGene == endGene) return 0

        val nucleotides = charArrayOf('A', 'C', 'G', 'T')
        val visited = HashSet<String>()
        val queue: ArrayDeque<Pair<String, Int>> = ArrayDeque()
        queue.add(Pair(startGene, 0))
        visited.add(startGene)

        while (queue.isNotEmpty()) {
            val (gene, steps) = queue.removeFirst()
            if (gene == endGene) return steps
            val chars = gene.toCharArray()
            for (i in chars.indices) {
                val original = chars[i]
                for (c in nucleotides) {
                    if (c == original) continue
                    chars[i] = c
                    val mutated = String(chars)
                    if (mutated in bankSet && mutated !in visited) {
                        visited.add(mutated)
                        queue.add(Pair(mutated, steps + 1))
                    }
                }
                chars[i] = original
            }
        }
        return -1
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  int minMutation(String startGene, String endGene, List<String> bank) {
    if (startGene == endGene) return 0;
    final Set<String> bankSet = bank.toSet();
    if (!bankSet.contains(endGene)) return -1;

    const List<String> genes = ['A', 'C', 'G', 'T'];
    final Queue<String> queue = Queue<String>();
    final Queue<int> stepsQueue = Queue<int>();
    final Set<String> visited = {startGene};

    queue.add(startGene);
    stepsQueue.add(0);

    while (queue.isNotEmpty) {
      final String current = queue.removeFirst();
      final int step = stepsQueue.removeFirst();

      if (current == endGene) return step;

      for (int i = 0; i < 8; i++) {
        for (final String g in genes) {
          if (g == current[i]) continue;
          final String next =
              current.substring(0, i) + g + current.substring(i + 1);
          if (bankSet.contains(next) && !visited.contains(next)) {
            visited.add(next);
            queue.add(next);
            stepsQueue.add(step + 1);
          }
        }
      }
    }

    return -1;
  }
}
```

## Golang

```go
func minMutation(startGene string, endGene string, bank []string) int {
	if startGene == endGene {
		return 0
	}
	bankSet := make(map[string]bool)
	for _, b := range bank {
		bankSet[b] = true
	}
	if !bankSet[endGene] {
		return -1
	}
	type node struct {
		gene string
		step int
	}
	queue := []node{{startGene, 0}}
	visited := map[string]bool{startGene: true}
	letters := []byte{'A', 'C', 'G', 'T'}

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]

		if cur.gene == endGene {
			return cur.step
		}

		gBytes := []byte(cur.gene)
		for i := 0; i < 8; i++ {
			orig := gBytes[i]
			for _, c := range letters {
				if c == orig {
					continue
				}
				gBytes[i] = c
				newGene := string(gBytes)
				if bankSet[newGene] && !visited[newGene] {
					visited[newGene] = true
					queue = append(queue, node{newGene, cur.step + 1})
				}
			}
			gBytes[i] = orig
		}
	}
	return -1
}
```

## Ruby

```ruby
require 'set'

def min_mutation(start_gene, end_gene, bank)
  return 0 if start_gene == end_gene
  bank_set = Set.new(bank)
  return -1 unless bank_set.include?(end_gene)

  chars = ['A', 'C', 'G', 'T']
  visited = Set.new([start_gene])
  queue = [[start_gene, 0]]

  until queue.empty?
    gene, steps = queue.shift
    return steps if gene == end_gene

    (0...gene.length).each do |i|
      original = gene[i]
      chars.each do |c|
        next if c == original
        mutated = gene.dup
        mutated[i] = c
        if bank_set.include?(mutated) && !visited.include?(mutated)
          visited.add(mutated)
          queue << [mutated, steps + 1]
        end
      end
    end
  end

  -1
end
```

## Scala

```scala
object Solution {
    def minMutation(startGene: String, endGene: String, bank: Array[String]): Int = {
        val bankSet = bank.toSet
        if (!bankSet.contains(endGene)) return -1
        if (startGene == endGene) return 0

        val visited = scala.collection.mutable.Set[String]()
        val queue = scala.collection.mutable.Queue[(String, Int)]()
        queue.enqueue((startGene, 0))
        visited.add(startGene)

        val genes = Array('A', 'C', 'G', 'T')

        while (queue.nonEmpty) {
            val (curr, steps) = queue.dequeue()
            if (curr == endGene) return steps

            for (i <- 0 until 8) {
                val prefix = curr.substring(0, i)
                val suffix = curr.substring(i + 1)
                for (g <- genes) {
                    if (curr.charAt(i) != g) {
                        val next = prefix + g + suffix
                        if (bankSet.contains(next) && !visited.contains(next)) {
                            visited.add(next)
                            queue.enqueue((next, steps + 1))
                        }
                    }
                }
            }
        }

        -1
    }
}
```

## Rust

```rust
use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn min_mutation(start_gene: String, end_gene: String, bank: Vec<String>) -> i32 {
        if start_gene == end_gene {
            return 0;
        }

        let bank_set: HashSet<String> = bank.into_iter().collect();
        if !bank_set.contains(&end_gene) {
            return -1;
        }

        let mut visited: HashSet<String> = HashSet::new();
        let mut queue: VecDeque<(String, i32)> = VecDeque::new();

        visited.insert(start_gene.clone());
        queue.push_back((start_gene, 0));

        let genes = ['A', 'C', 'G', 'T'];

        while let Some((curr, steps)) = queue.pop_front() {
            if curr == end_gene {
                return steps;
            }
            let chars: Vec<char> = curr.chars().collect();
            for i in 0..8 {
                for &g in genes.iter() {
                    if g == chars[i] {
                        continue;
                    }
                    let mut new_chars = chars.clone();
                    new_chars[i] = g;
                    let new_gene: String = new_chars.iter().collect();
                    if bank_set.contains(&new_gene) && !visited.contains(&new_gene) {
                        visited.insert(new_gene.clone());
                        queue.push_back((new_gene, steps + 1));
                    }
                }
            }
        }

        -1
    }
}
```

## Racket

```racket
#lang racket

(require racket/set)

(define/contract (min-mutation startGene endGene bank)
  (-> string? string? (listof string?) exact-integer?)
  (cond
    [(string=? startGene endGene) 0]
    [(not (member endGene bank)) -1]
    [else
     (let* ((bank-set (list->set bank))
            (diff-count
              (lambda (s1 s2)
                (let loop ((i 0) (cnt 0))
                  (if (= i (string-length s1))
                      cnt
                      (loop (+ i 1)
                            (if (char=? (string-ref s1 i) (string-ref s2 i))
                                cnt
                                (+ cnt 1))))))))
       (let bfs ((queue (list (cons startGene 0)))
                 (visited (set startGene)))
         (cond
           [(empty? queue) -1]
           [else
            (define cur (first queue))
            (define rest (rest queue))
            (define gene (car cur))
            (define steps (cdr cur))
            (if (string=? gene endGene)
                steps
                (let* ((neighbors
                         (filter (lambda (g)
                                   (and (not (set-member? visited g))
                                        (= (diff-count gene g) 1)))
                                 bank))
                       (new-visited (foldl set-add visited neighbors))
                       (new-queue (append rest (map (lambda (g) (cons g (+ steps 1))) neighbors))))
                  (bfs new-queue new-visited))))))])))))
```

## Erlang

```erlang
-module(solution).
-export([min_mutation/3]).

-spec min_mutation(binary(), binary(), [binary()]) -> integer().
min_mutation(StartGene, EndGene, Bank) ->
    case lists:member(EndGene, Bank) of
        false -> -1;
        true ->
            BankMap = maps_from_list(Bank),
            bfs([{StartGene, 0}], #{}, BankMap, EndGene)
    end.

maps_from_list(List) ->
    lists:foldl(fun(G, M) -> maps:put(G, true, M) end, #{}, List).

bfs([], _Visited, _BankSet, _End) ->
    -1;
bfs([{Gene, Steps} | Rest], Visited, BankSet, End) ->
    if Gene =:= End ->
            Steps;
       true ->
            NewNeighbors = neighbors(Gene, BankSet, Visited),
            NewVisited = add_to_visited(NewNeighbors, Visited),
            NewQueue = Rest ++ [{N, Steps + 1} || N <- NewNeighbors],
            bfs(NewQueue, NewVisited, BankSet, End)
    end.

add_to_visited([], Vis) -> Vis;
add_to_visited([G | Gs], Vis) ->
    add_to_visited(Gs, maps:put(G, true, Vis)).

neighbors(Gene, BankSet, Visited) ->
    Genes = binary_to_list(Gene),
    CharList = "ACGT",
    lists:foldl(fun(Pos, Acc) ->
        OrigChar = lists:nth(Pos + 1, Genes),
        lists:foldl(fun(C, A2) ->
            if C =/= OrigChar ->
                    NewList = replace_nth(Genes, Pos, C),
                    NewGene = list_to_binary(NewList),
                    case maps:is_key(NewGene, BankSet) andalso not maps:is_key(NewGene, Visited) of
                        true -> [NewGene | A2];
                        false -> A2
                    end;
               true ->
                    A2
            end
        end, Acc, CharList)
    end, [], lists:seq(0, 7)).

replace_nth(List, Index, NewChar) ->
    {Left, [_ | Right]} = lists:split(Index, List),
    Left ++ [NewChar] ++ Right.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_mutation(start_gene :: String.t, end_gene :: String.t, bank :: [String.t]) :: integer
  def min_mutation(start_gene, end_gene, bank) do
    cond do
      start_gene == end_gene ->
        0

      not Enum.member?(bank, end_gene) ->
        -1

      true ->
        bank_set = MapSet.new(bank)
        bfs(:queue.from_list([{start_gene, 0}]), MapSet.new([start_gene]), bank_set, end_gene)
    end
  end

  defp bfs(queue, visited, bank_set, target) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{:value, {gene, steps}}, q} ->
        if gene == target do
          steps
        else
          neighbors = get_neighbors(gene, bank_set)

          {new_queue, new_visited} =
            Enum.reduce(neighbors, {q, visited}, fn nb, {acc_q, acc_vis} ->
              if MapSet.member?(acc_vis, nb) do
                {acc_q, acc_vis}
              else
                {:queue.in({nb, steps + 1}, acc_q), MapSet.put(acc_vis, nb)}
              end
            end)

          bfs(new_queue, new_visited, bank_set, target)
        end
    end
  end

  defp get_neighbors(gene, bank_set) do
    chars = [?A, ?C, ?G, ?T]
    gene_chars = String.to_charlist(gene)

    for i <- 0..7,
        c <- chars,
        c != Enum.at(gene_chars, i),
        mutated = List.replace_at(gene_chars, i, c) |> to_string(),
        MapSet.member?(bank_set, mutated) do
      mutated
    end
  end
end
```
