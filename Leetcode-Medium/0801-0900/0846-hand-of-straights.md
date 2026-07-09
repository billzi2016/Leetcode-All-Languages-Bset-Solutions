# 0846. Hand of Straights

## Cpp

```cpp
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        if (hand.size() % groupSize != 0) return false;
        std::map<int,int> cnt;
        for (int x : hand) ++cnt[x];
        while (!cnt.empty()) {
            auto it = cnt.begin();
            int start = it->first;
            int need = it->second; // number of groups to open at this start
            for (int i = 0; i < groupSize; ++i) {
                int val = start + i;
                auto itr = cnt.find(val);
                if (itr == cnt.end() || itr->second < need) return false;
                itr->second -= need;
                if (itr->second == 0) cnt.erase(itr);
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        if (groupSize == 1) return true;
        if (hand.length % groupSize != 0) return false;

        java.util.TreeMap<Integer, Integer> count = new java.util.TreeMap<>();
        for (int card : hand) {
            count.put(card, count.getOrDefault(card, 0) + 1);
        }

        while (!count.isEmpty()) {
            int start = count.firstKey();
            for (int i = 0; i < groupSize; i++) {
                int cur = start + i;
                Integer c = count.get(cur);
                if (c == null) return false;
                if (c == 1) {
                    count.remove(cur);
                } else {
                    count.put(cur, c - 1);
                }
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False
        from collections import Counter
        cnt = Counter(hand)
        for x in sorted(cnt):
            cur = cnt[x]
            if cur > 0:
                for i in range(1, groupSize):
                    nxt = x + i
                    if cnt.get(nxt, 0) < cur:
                        return False
                    cnt[nxt] -= cur
        return True
```

## Python3

```python
from typing import List
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        cnt = Counter(hand)
        for x in sorted(cnt):
            c = cnt[x]
            if c > 0:
                for i in range(1, groupSize):
                    nxt = x + i
                    if cnt.get(nxt, 0) < c:
                        return False
                    cnt[nxt] -= c
        return True
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

static int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

bool isNStraightHand(int* hand, int handSize, int groupSize) {
    if (groupSize == 0) return false;
    if (handSize % groupSize != 0) return false;

    qsort(hand, handSize, sizeof(int), cmp_int);

    // Build unique values and their frequencies
    int uniqVals[handSize];
    int freq[handSize];
    int m = 0; // number of unique values

    for (int i = 0; i < handSize; ++i) {
        if (i == 0 || hand[i] != hand[i - 1]) {
            uniqVals[m] = hand[i];
            freq[m] = 1;
            ++m;
        } else {
            ++freq[m - 1];
        }
    }

    // Queue to store number of groups started at each value
    int startCounts[handSize];
    int front = 0, back = 0;
    int open = 0; // currently open groups

    for (int i = 0; i < m; ++i) {
        if (i > 0 && uniqVals[i] != uniqVals[i - 1] + 1) {
            if (open != 0) return false; // gap with unfinished groups
        }

        int cnt = freq[i];
        int newGroups = cnt - open;
        if (newGroups < 0) return false; // not enough cards to continue open groups

        startCounts[back++] = newGroups;
        open += newGroups;

        if (i >= groupSize - 1) {
            open -= startCounts[front];
            ++front;
        }
    }

    while (front < back) {
        open -= startCounts[front];
        ++front;
    }

    return open == 0;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public bool IsNStraightHand(int[] hand, int groupSize) {
        if (groupSize == 1) return true;
        if (hand.Length % groupSize != 0) return false;

        var count = new SortedDictionary<int, int>();
        foreach (var card in hand) {
            if (!count.ContainsKey(card)) count[card] = 0;
            count[card]++;
        }

        while (count.Count > 0) {
            int start = count.First().Key;
            for (int i = 0; i < groupSize; i++) {
                int cur = start + i;
                if (!count.TryGetValue(cur, out int c)) return false;
                if (c == 1) {
                    count.Remove(cur);
                } else {
                    count[cur] = c - 1;
                }
            }
        }

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} hand
 * @param {number} groupSize
 * @return {boolean}
 */
var isNStraightHand = function(hand, groupSize) {
    if (hand.length % groupSize !== 0) return false;
    
    const freq = new Map();
    for (const card of hand) {
        freq.set(card, (freq.get(card) || 0) + 1);
    }
    
    const keys = Array.from(freq.keys()).sort((a, b) => a - b);
    
    for (const start of keys) {
        const count = freq.get(start);
        if (count > 0) {
            for (let i = 0; i < groupSize; i++) {
                const cur = start + i;
                if (!freq.has(cur)) return false;
                const curCount = freq.get(cur);
                if (curCount < count) return false;
                freq.set(cur, curCount - count);
            }
        }
    }
    
    return true;
};
```

## Typescript

```typescript
function isNStraightHand(hand: number[], groupSize: number): boolean {
    const n = hand.length;
    if (n % groupSize !== 0) return false;
    hand.sort((a, b) => a - b);
    const cnt = new Map<number, number>();
    for (const v of hand) {
        cnt.set(v, (cnt.get(v) ?? 0) + 1);
    }
    for (const v of hand) {
        const curCount = cnt.get(v);
        if (!curCount) continue; // already used up
        for (let i = 0; i < groupSize; i++) {
            const key = v + i;
            const c = cnt.get(key);
            if (!c) return false;
            if (c === 1) cnt.delete(key);
            else cnt.set(key, c - 1);
        }
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $hand
     * @param Integer $groupSize
     * @return Boolean
     */
    function isNStraightHand($hand, $groupSize) {
        $n = count($hand);
        if ($groupSize <= 0 || $n % $groupSize !== 0) {
            return false;
        }
        sort($hand);
        $cnt = [];
        foreach ($hand as $c) {
            if (!isset($cnt[$c])) {
                $cnt[$c] = 0;
            }
            $cnt[$c]++;
        }

        foreach ($hand as $c) {
            if ($cnt[$c] === 0) {
                continue;
            }
            for ($i = 0; $i < $groupSize; $i++) {
                $val = $c + $i;
                if (!isset($cnt[$val]) || $cnt[$val] === 0) {
                    return false;
                }
                $cnt[$val]--;
            }
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func isNStraightHand(_ hand: [Int], _ groupSize: Int) -> Bool {
        if hand.count % groupSize != 0 { return false }
        var freq = [Int:Int]()
        for v in hand {
            freq[v, default: 0] += 1
        }
        let sortedKeys = freq.keys.sorted()
        for key in sortedKeys {
            guard let count = freq[key], count > 0 else { continue }
            let need = count
            for i in 0..<groupSize {
                let cur = key + i
                guard var c = freq[cur] else { return false }
                if c < need { return false }
                c -= need
                if c == 0 {
                    freq.removeValue(forKey: cur)
                } else {
                    freq[cur] = c
                }
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isNStraightHand(hand: IntArray, groupSize: Int): Boolean {
        if (hand.size % groupSize != 0) return false
        val countMap = java.util.TreeMap<Int, Int>()
        for (card in hand) {
            countMap[card] = (countMap[card] ?: 0) + 1
        }
        while (countMap.isNotEmpty()) {
            val start = countMap.firstKey()
            for (i in 0 until groupSize) {
                val key = start + i
                val cnt = countMap[key] ?: return false
                if (cnt == 1) {
                    countMap.remove(key)
                } else {
                    countMap[key] = cnt - 1
                }
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool isNStraightHand(List<int> hand, int groupSize) {
    if (hand.length % groupSize != 0) return false;
    hand.sort();
    final Map<int, int> freq = {};
    for (var card in hand) {
      freq[card] = (freq[card] ?? 0) + 1;
    }
    for (var card in hand) {
      final count = freq[card] ?? 0;
      if (count > 0) {
        for (int i = 0; i < groupSize; ++i) {
          final cur = card + i;
          final curCount = freq[cur] ?? 0;
          if (curCount < count) return false;
          freq[cur] = curCount - count;
        }
      }
    }
    return true;
  }
}
```

## Golang

```go
import "sort"

func isNStraightHand(hand []int, groupSize int) bool {
	if len(hand)%groupSize != 0 {
		return false
	}
	sort.Ints(hand)
	freq := make(map[int]int, len(hand))
	for _, v := range hand {
		freq[v]++
	}
	for _, v := range hand {
		cnt := freq[v]
		if cnt > 0 {
			for i := 0; i < groupSize; i++ {
				val := v + i
				if freq[val] < cnt {
					return false
				}
				freq[val] -= cnt
			}
		}
	}
	return true
}
```

## Ruby

```ruby
def is_n_straight_hand(hand, group_size)
  return false if hand.length % group_size != 0
  counts = Hash.new(0)
  hand.each { |c| counts[c] += 1 }
  sorted_keys = counts.keys.sort
  sorted_keys.each do |start|
    cnt = counts[start]
    next if cnt == 0
    (1...group_size).each do |i|
      nxt = start + i
      return false unless counts.key?(nxt) && counts[nxt] >= cnt
      counts[nxt] -= cnt
    end
    counts[start] = 0
  end
  true
end
```

## Scala

```scala
object Solution {
  def isNStraightHand(hand: Array[Int], groupSize: Int): Boolean = {
    if (hand.length % groupSize != 0) return false
    val count = scala.collection.mutable.TreeMap.empty[Int, Int]
    hand.foreach { c =>
      count.update(c, count.getOrElse(c, 0) + 1)
    }
    while (count.nonEmpty) {
      val start = count.firstKey
      var i = 0
      while (i < groupSize) {
        val key = start + i
        count.get(key) match {
          case None => return false
          case Some(v) =>
            if (v == 1) count -= key
            else count.update(key, v - 1)
        }
        i += 1
      }
    }
    true
  }
}
```

## Rust

```rust
use std::collections::BTreeMap;

impl Solution {
    pub fn is_n_straight_hand(hand: Vec<i32>, group_size: i32) -> bool {
        let n = hand.len();
        if group_size <= 0 {
            return false;
        }
        let k = group_size as usize;
        if n % k != 0 {
            return false;
        }

        // Count occurrences of each card
        let mut cnt: BTreeMap<i32, usize> = BTreeMap::new();
        for &card in &hand {
            *cnt.entry(card).or_insert(0) += 1;
        }

        while let Some((&first, &c)) = cnt.iter().next() {
            // Try to build a group starting from 'first'
            let mut zeros = Vec::with_capacity(k);
            for i in 0..k as i32 {
                let key = first + i;
                match cnt.get_mut(&key) {
                    Some(v) => {
                        if *v < c {
                            return false;
                        }
                        *v -= c;
                        if *v == 0 {
                            zeros.push(key);
                        }
                    }
                    None => return false,
                }
            }
            // Remove entries that reached zero
            for key in zeros {
                cnt.remove(&key);
            }
        }

        true
    }
}
```

## Racket

```racket
(define/contract (is-n-straight-hand hand groupSize)
  (-> (listof exact-integer?) exact-integer? boolean?)
  (if (not (= (modulo (length hand) groupSize) 0))
      #false
      (let ((cnt (make-hash)))
        ;; count occurrences
        (for ([x hand])
          (hash-update! cnt x (lambda (v) (+ v 1)) 1))
        (define keys (sort (hash-keys cnt) <))
        (let loop ((ks keys))
          (cond [(null? ks) #true]
                [else
                 (define cur (car ks))
                 (define c (hash-ref cnt cur 0))
                 (if (= c 0)
                     (loop (cdr ks))
                     (begin
                       ;; verify we have enough cards for the whole group
                       (define ok #t)
                       (for ([i (in-range groupSize)])
                         (define val (+ cur i))
                         (define vcnt (hash-ref cnt val 0))
                         (when (< vcnt c) (set! ok #f)))
                       (if (not ok)
                           #false
                           (begin
                             ;; subtract used cards
                             (for ([i (in-range groupSize)])
                               (define val (+ cur i))
                               (hash-set! cnt val (- (hash-ref cnt val) c)))
                             (loop (cdr ks))))))])))))
```

## Erlang

```erlang
-spec is_n_straight_hand(Hand :: [integer()], GroupSize :: integer()) -> boolean().
is_n_straight_hand(Hand, GroupSize) ->
    case length(Hand) rem GroupSize of
        0 ->
            Tree = build_tree(Hand, gb_trees:empty()),
            process(Tree, GroupSize);
        _ -> false
    end.

build_tree([], Tree) -> Tree;
build_tree([H|T], Tree) ->
    case gb_trees:lookup(H, Tree) of
        {value, C} -> NewTree = gb_trees:update(H, C + 1, Tree);
        error      -> NewTree = gb_trees:enter(H, 1, Tree)
    end,
    build_tree(T, NewTree).

process(Tree, _GroupSize) when gb_trees:is_empty(Tree) ->
    true;
process(Tree, GroupSize) ->
    {Start, Count} = gb_trees:smallest(Tree),
    case decrement(Tree, Start, GroupSize, Count) of
        {ok, NewTree} -> process(NewTree, GroupSize);
        error         -> false
    end.

decrement(Tree, Start, GroupSize, Needed) ->
    dec_offset(0, Start, GroupSize, Needed, Tree).

dec_offset(Offset, _Start, GroupSize, _Needed, CurTree) when Offset == GroupSize ->
    {ok, CurTree};
dec_offset(Offset, Start, GroupSize, Needed, CurTree) ->
    Val = Start + Offset,
    case gb_trees:lookup(Val, CurTree) of
        {value, C} when C >= Needed ->
            NewTree = if C == Needed -> gb_trees:delete(Val, CurTree);
                         true       -> gb_trees:update(Val, C - Needed, CurTree)
                     end,
            dec_offset(Offset + 1, Start, GroupSize, Needed, NewTree);
        _ -> error
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_n_straight_hand(hand :: [integer], group_size :: integer) :: boolean
  def is_n_straight_hand(hand, group_size) do
    n = length(hand)

    if rem(n, group_size) != 0 do
      false
    else
      freq =
        Enum.reduce(hand, %{}, fn x, acc ->
          Map.update(acc, x, 1, &(&1 + 1))
        end)

      keys = Map.keys(freq) |> Enum.sort()
      process(keys, freq, group_size)
    end
  end

  defp process([], _freq, _group_size), do: true

  defp process([k | ks], freq, group_size) do
    count = Map.get(freq, k, 0)

    if count == 0 do
      process(ks, freq, group_size)
    else
      {new_map, ok} =
        Enum.reduce_while(0..(group_size - 1), {freq, true}, fn offset, {m, _} ->
          val = k + offset
          cur = Map.get(m, val, 0)

          if cur < count do
            {:halt, {m, false}}
          else
            {:cont, {Map.put(m, val, cur - count), true}}
          end
        end)

      if ok do
        process(ks, new_map, group_size)
      else
        false
      end
    end
  end
end
```
