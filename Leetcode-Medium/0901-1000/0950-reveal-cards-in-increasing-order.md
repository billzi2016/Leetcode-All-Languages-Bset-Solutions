# 0950. Reveal Cards In Increasing Order

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        int n = deck.size();
        sort(deck.begin(), deck.end());
        queue<int> q;
        for (int i = 0; i < n; ++i) q.push(i);
        vector<int> ans(n);
        for (int card : deck) {
            int idx = q.front(); q.pop();
            ans[idx] = card;
            if (!q.empty()) {
                q.push(q.front());
                q.pop();
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        int n = deck.length;
        Arrays.sort(deck);
        Deque<Integer> indices = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            indices.addLast(i);
        }
        int[] result = new int[n];
        for (int card : deck) {
            int idx = indices.pollFirst();
            result[idx] = card;
            if (!indices.isEmpty()) {
                indices.offerLast(indices.pollFirst());
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        from collections import deque
        n = len(deck)
        deck.sort()
        q = deque(range(n))
        res = [0] * n
        for card in deck:
            idx = q.popleft()
            res[idx] = card
            if q:
                q.append(q.popleft())
        return res
```

## Python3

```python
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        from collections import deque
        n = len(deck)
        indices = deque(range(n))
        result = [0] * n
        for card in sorted(deck):
            idx = indices.popleft()
            result[idx] = card
            if indices:
                indices.append(indices.popleft())
        return result
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
static int cmp_int(const void *a, const void *b) {
    return (*(const int *)a) - (*(const int *)b);
}

int* deckRevealedIncreasing(int* deck, int deckSize, int* returnSize){
    if (deckSize == 0) {
        *returnSize = 0;
        return NULL;
    }
    
    // Sort the deck in ascending order
    qsort(deck, deckSize, sizeof(int), cmp_int);
    
    // Result array
    int *result = (int *)malloc(deckSize * sizeof(int));
    
    // Queue of indices
    int *q = (int *)malloc(deckSize * sizeof(int));
    for (int i = 0; i < deckSize; ++i) q[i] = i;
    
    int head = 0;                     // points to current front
    int tail = deckSize % deckSize;   // next insertion position (initially same as size)
    int size = deckSize;              // number of indices currently in queue
    
    for (int i = 0; i < deckSize; ++i) {
        // Take the front index to place current smallest card
        int idx = q[head];
        head = (head + 1) % deckSize;
        size--;
        result[idx] = deck[i];
        
        if (size == 0) break; // no more indices left
        
        // Move next index from front to back of the queue
        int nextIdx = q[head];
        head = (head + 1) % deckSize;
        // push to tail
        q[tail] = nextIdx;
        tail = (tail + 1) % deckSize;
        // size remains unchanged after this move (removed one, added one)
    }
    
    free(q);
    *returnSize = deckSize;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] DeckRevealedIncreasing(int[] deck)
    {
        int n = deck.Length;
        Array.Sort(deck);
        var indices = new Queue<int>();
        for (int i = 0; i < n; i++) indices.Enqueue(i);

        int[] result = new int[n];
        foreach (int card in deck)
        {
            int idx = indices.Dequeue();
            result[idx] = card;
            if (indices.Count > 0)
                indices.Enqueue(indices.Dequeue());
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} deck
 * @return {number[]}
 */
var deckRevealedIncreasing = function(deck) {
    const n = deck.length;
    deck.sort((a, b) => a - b);
    
    // initialize queue with indices 0..n-1
    const q = [];
    for (let i = 0; i < n; ++i) q.push(i);
    
    const res = new Array(n);
    
    for (let i = 0; i < n; ++i) {
        // take the front index and place current smallest card there
        const idx = q.shift();
        res[idx] = deck[i];
        // move next index to the back, if any remain
        if (q.length) {
            q.push(q.shift());
        }
    }
    
    return res;
};
```

## Typescript

```typescript
function deckRevealedIncreasing(deck: number[]): number[] {
    const n = deck.length;
    deck.sort((a, b) => a - b);
    const result = new Array<number>(n);
    const queue: number[] = [];
    for (let i = 0; i < n; i++) queue.push(i);

    let idx = 0;
    while (queue.length) {
        const pos = queue.shift()!;
        result[pos] = deck[idx++];
        if (queue.length) {
            const move = queue.shift()!;
            queue.push(move);
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $deck
     * @return Integer[]
     */
    function deckRevealedIncreasing($deck) {
        $n = count($deck);
        sort($deck); // ascending order

        $queue = new SplQueue();
        for ($i = 0; $i < $n; $i++) {
            $queue->enqueue($i);
        }

        $result = array_fill(0, $n, 0);

        foreach ($deck as $card) {
            // place the smallest remaining card at the current front index
            $idx = $queue->dequeue();
            $result[$idx] = $card;

            // move next index to the back if any remain
            if (!$queue->isEmpty()) {
                $nextIdx = $queue->dequeue();
                $queue->enqueue($nextIdx);
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func deckRevealedIncreasing(_ deck: [Int]) -> [Int] {
        let n = deck.count
        var sortedDeck = deck.sorted()
        var queue = Array(0..<n)
        var result = Array(repeating: 0, count: n)

        for card in sortedDeck {
            let idx = queue.removeFirst()
            result[idx] = card
            if !queue.isEmpty {
                let nextIdx = queue.removeFirst()
                queue.append(nextIdx)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun deckRevealedIncreasing(deck: IntArray): IntArray {
        val n = deck.size
        val sorted = deck.clone()
        java.util.Arrays.sort(sorted)
        val q = java.util.ArrayDeque<Int>()
        for (i in 0 until n) {
            q.add(i)
        }
        val result = IntArray(n)
        var idx = 0
        while (!q.isEmpty()) {
            val pos = q.pollFirst()
            result[pos] = sorted[idx++]
            if (!q.isEmpty()) {
                val move = q.pollFirst()
                q.addLast(move)
            }
        }
        return result
    }
}
```

## Dart

```dart
import 'dart:collection';

class Solution {
  List<int> deckRevealedIncreasing(List<int> deck) {
    int n = deck.length;
    deck.sort();
    Queue<int> q = Queue<int>();
    for (int i = 0; i < n; i++) {
      q.add(i);
    }
    List<int> result = List.filled(n, 0);
    for (int card in deck) {
      int idx = q.removeFirst();
      result[idx] = card;
      if (q.isNotEmpty) {
        int moveIdx = q.removeFirst();
        q.addLast(moveIdx);
      }
    }
    return result;
  }
}
```

## Golang

```go
import "sort"

func deckRevealedIncreasing(deck []int) []int {
	n := len(deck)
	sort.Ints(deck)

	res := make([]int, n)
	q := make([]int, n)
	for i := 0; i < n; i++ {
		q[i] = i
	}

	for _, card := range deck {
		idx := q[0]
		q = q[1:]
		res[idx] = card
		if len(q) > 0 {
			q = append(q, q[0])
			q = q[1:]
		}
	}
	return res
}
```

## Ruby

```ruby
def deck_revealed_increasing(deck)
  n = deck.length
  sorted = deck.sort
  indices = (0...n).to_a
  result = Array.new(n)

  sorted.each do |card|
    idx = indices.shift
    result[idx] = card
    indices.push(indices.shift) unless indices.empty?
  end

  result
end
```

## Scala

```scala
object Solution {
    def deckRevealedIncreasing(deck: Array[Int]): Array[Int] = {
        val n = deck.length
        val sorted = deck.sorted
        import scala.collection.mutable.Queue
        val q = Queue[Int]()
        for (i <- 0 until n) q.enqueue(i)
        val res = new Array[Int](n)
        var idx = 0
        while (q.nonEmpty) {
            val pos = q.dequeue()
            res(pos) = sorted(idx)
            idx += 1
            if (q.nonEmpty) {
                val move = q.dequeue()
                q.enqueue(move)
            }
        }
        res
    }
}
```

## Rust

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn deck_revealed_increasing(deck: Vec<i32>) -> Vec<i32> {
        let n = deck.len();
        if n == 0 {
            return vec![];
        }
        // Sort the cards in ascending order
        let mut sorted = deck.clone();
        sorted.sort();

        // Queue of indices representing positions in the result deck
        let mut indices: VecDeque<usize> = (0..n).collect();

        // Result array to hold the final ordering
        let mut result = vec![0; n];

        for &card in sorted.iter() {
            // Take the front index where this card will be placed
            let idx = indices.pop_front().unwrap();
            result[idx] = card;

            // Move the next index to the back of the queue, if any remain
            if let Some(next_idx) = indices.pop_front() {
                indices.push_back(next_idx);
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (deck-revealed-increasing deck)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ((n (length deck))
         (sorted (sort deck <))
         ;; generate list of indices [0 1 ... n-1]
         (indices (let rec ((i 0) (acc '()))
                    (if (= i n)
                        (reverse acc)
                        (rec (+ i 1) (cons i acc)))))
         (result (make-vector n)))
    (let loop ((cards sorted) (q indices))
      (if (null? cards)
          (vector->list result)
          (let* ((idx (car q))
                 (_ (vector-set! result idx (car cards)))
                 (q-rest (cdr q)))
            (if (null? q-rest)
                (loop (cdr cards) '())
                (let ((moved (car q-rest))
                      (new-q (append (cdr q-rest) (list moved))))
                  (loop (cdr cards) new-q))))))))
```

## Erlang

```erlang
-module(solution).
-export([deck_revealed_increasing/1]).

-spec deck_revealed_increasing(Deck :: [integer()]) -> [integer()].
deck_revealed_increasing(Deck) ->
    Sorted = lists:sort(Deck),
    N = length(Deck),
    Queue0 = build_queue(N, queue:new()),
    Arr0 = array:new(N, {default, 0}),
    FinalArr = fill(Sorted, Queue0, Arr0),
    [array:get(I, FinalArr) || I <- lists:seq(0, N - 1)].

build_queue(N, Q) ->
    build_queue_helper(0, N - 1, Q).

build_queue_helper(Cur, Max, Q) when Cur > Max ->
    Q;
build_queue_helper(Cur, Max, Q) ->
    NewQ = queue:in(Cur, Q),
    build_queue_helper(Cur + 1, Max, NewQ).

fill([], _Queue, Arr) ->
    Arr;
fill([Card | Rest], Queue, Arr) ->
    case queue:out(Queue) of
        {value, Idx, Q1} ->
            NewArr = array:set(Idx, Card, Arr),
            case queue:out(Q1) of
                {empty, _} ->
                    fill(Rest, Q1, NewArr);
                {value, NextIdx, Q2} ->
                    Q3 = queue:in(NextIdx, Q2),
                    fill(Rest, Q3, NewArr)
            end;
        {empty, _} ->
            Arr
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec deck_revealed_increasing(deck :: [integer]) :: [integer]
  def deck_revealed_increasing(deck) do
    n = length(deck)
    sorted = Enum.sort(deck)

    # Initialize a queue with indices 0..n-1
    init_queue =
      Enum.reduce(0..(n - 1), :queue.new(), fn i, acc ->
        :queue.in(i, acc)
      end)

    result = List.duplicate(0, n)

    {final_result, _} =
      Enum.reduce(sorted, {result, init_queue}, fn card, {res, q} ->
        # Take the front index where this card should be placed
        {{:value, idx}, q1} = :queue.out(q)
        res_updated = List.replace_at(res, idx, card)

        # Move the next index to the back of the queue, if any
        case :queue.out(q1) do
          {:empty, _} ->
            {res_updated, q1}

          {{:value, nxt}, q2} ->
            q3 = :queue.in(nxt, q2)
            {res_updated, q3}
        end
      end)

    final_result
  end
end
```
