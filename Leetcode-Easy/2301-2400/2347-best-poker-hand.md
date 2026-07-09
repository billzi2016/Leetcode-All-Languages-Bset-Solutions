# 2347. Best Poker Hand

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string bestHand(vector<int>& ranks, vector<char>& suits) {
        bool flush = true;
        for (int i = 1; i < 5; ++i) {
            if (suits[i] != suits[0]) { flush = false; break; }
        }
        if (flush) return "Flush";
        
        unordered_map<int,int> cnt;
        int mx = 0;
        for (int r : ranks) {
            mx = max(mx, ++cnt[r]);
        }
        if (mx >= 3) return "Three of a Kind";
        if (mx == 2) return "Pair";
        return "High Card";
    }
};
```

## Java

```java
class Solution {
    public String bestHand(int[] ranks, char[] suits) {
        boolean flush = true;
        for (int i = 1; i < suits.length; i++) {
            if (suits[i] != suits[0]) {
                flush = false;
                break;
            }
        }
        if (flush) return "Flush";
        int[] cnt = new int[14];
        int max = 0;
        for (int r : ranks) {
            cnt[r]++;
            if (cnt[r] > max) max = cnt[r];
        }
        if (max >= 3) return "Three of a Kind";
        if (max == 2) return "Pair";
        return "High Card";
    }
}
```

## Python

```python
class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        # Check for Flush: all suits are identical
        if len(set(suits)) == 1:
            return "Flush"
        
        # Count occurrences of each rank
        from collections import Counter
        cnt = Counter(ranks)
        most_common = max(cnt.values())
        
        if most_common >= 3:
            return "Three of a Kind"
        if most_common == 2:
            return "Pair"
        return "High Card"
```

## Python3

```python
from typing import List
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # Check for Flush: all suits are the same
        if len(set(suits)) == 1:
            return "Flush"
        # Count occurrences of each rank
        freq = {}
        for r in ranks:
            freq[r] = freq.get(r, 0) + 1
        max_cnt = max(freq.values())
        if max_cnt >= 3:
            return "Three of a Kind"
        if max_cnt == 2:
            return "Pair"
        return "High Card"
```

## C

```c
#include <stddef.h>

char* bestHand(int* ranks, int ranksSize, char* suits, int suitsSize) {
    // Check for Flush
    int flush = 1;
    for (int i = 1; i < suitsSize; ++i) {
        if (suits[i] != suits[0]) {
            flush = 0;
            break;
        }
    }
    if (flush) return "Flush";
    
    // Count rank frequencies
    int cnt[14] = {0};
    for (int i = 0; i < ranksSize; ++i) {
        cnt[ranks[i]]++;
    }
    
    int maxc = 0;
    for (int i = 1; i <= 13; ++i) {
        if (cnt[i] > maxc) maxc = cnt[i];
    }
    
    if (maxc >= 3) return "Three of a Kind";
    if (maxc == 2) return "Pair";
    return "High Card";
}
```

## Csharp

```csharp
public class Solution {
    public string BestHand(int[] ranks, char[] suits) {
        // Check for Flush: all suits are the same
        bool isFlush = true;
        for (int i = 1; i < suits.Length; i++) {
            if (suits[i] != suits[0]) {
                isFlush = false;
                break;
            }
        }
        if (isFlush) return "Flush";

        // Count occurrences of each rank
        var count = new Dictionary<int, int>();
        foreach (int r in ranks) {
            if (!count.ContainsKey(r)) count[r] = 0;
            count[r]++;
        }

        bool hasThree = false;
        bool hasPair = false;
        foreach (var kvp in count) {
            if (kvp.Value >= 3) {
                hasThree = true;
                break;
            }
            if (kvp.Value == 2) {
                hasPair = true;
            }
        }

        if (hasThree) return "Three of a Kind";
        if (hasPair) return "Pair";
        return "High Card";
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} ranks
 * @param {character[]} suits
 * @return {string}
 */
var bestHand = function(ranks, suits) {
    // Check Flush: all suits identical
    const firstSuit = suits[0];
    let isFlush = true;
    for (let i = 1; i < suits.length; i++) {
        if (suits[i] !== firstSuit) {
            isFlush = false;
            break;
        }
    }
    if (isFlush) return "Flush";
    
    // Count rank frequencies
    const freq = new Map();
    for (const r of ranks) {
        freq.set(r, (freq.get(r) || 0) + 1);
    }
    
    let hasThree = false;
    let hasPair = false;
    for (const cnt of freq.values()) {
        if (cnt >= 3) hasThree = true;
        else if (cnt === 2) hasPair = true;
    }
    
    if (hasThree) return "Three of a Kind";
    if (hasPair) return "Pair";
    return "High Card";
};
```

## Typescript

```typescript
function bestHand(ranks: number[], suits: string[]): string {
    // Check for Flush: all suits are the same
    const firstSuit = suits[0];
    let isFlush = true;
    for (let i = 1; i < suits.length; i++) {
        if (suits[i] !== firstSuit) {
            isFlush = false;
            break;
        }
    }
    if (isFlush) return "Flush";

    // Count rank frequencies
    const freq = new Map<number, number>();
    for (const r of ranks) {
        freq.set(r, (freq.get(r) ?? 0) + 1);
    }

    let maxCount = 0;
    for (const cnt of freq.values()) {
        if (cnt > maxCount) maxCount = cnt;
    }

    if (maxCount >= 3) return "Three of a Kind";
    if (maxCount === 2) return "Pair";
    return "High Card";
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $ranks
     * @param String[] $suits
     * @return String
     */
    function bestHand($ranks, $suits) {
        if (count(array_unique($suits)) === 1) {
            return "Flush";
        }
        $cnt = array_count_values($ranks);
        foreach ($cnt as $v) {
            if ($v >= 3) {
                return "Three of a Kind";
            }
        }
        foreach ($cnt as $v) {
            if ($v == 2) {
                return "Pair";
            }
        }
        return "High Card";
    }
}
```

## Swift

```swift
class Solution {
    func bestHand(_ ranks: [Int], _ suits: [Character]) -> String {
        // Check for Flush
        let firstSuit = suits[0]
        var isFlush = true
        for s in suits {
            if s != firstSuit {
                isFlush = false
                break
            }
        }
        if isFlush { return "Flush" }
        
        // Count rank frequencies
        var count = [Int: Int]()
        for r in ranks {
            count[r, default: 0] += 1
        }
        let maxFreq = count.values.max() ?? 0
        
        if maxFreq >= 3 {
            return "Three of a Kind"
        } else if maxFreq == 2 {
            return "Pair"
        } else {
            return "High Card"
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun bestHand(ranks: IntArray, suits: CharArray): String {
        // Check for Flush
        val firstSuit = suits[0]
        var isFlush = true
        for (s in suits) {
            if (s != firstSuit) {
                isFlush = false
                break
            }
        }
        if (isFlush) return "Flush"

        // Count rank frequencies
        val freq = HashMap<Int, Int>()
        for (r in ranks) {
            freq[r] = (freq[r] ?: 0) + 1
        }

        var maxCount = 0
        for (cnt in freq.values) {
            if (cnt > maxCount) maxCount = cnt
        }

        return when {
            maxCount >= 3 -> "Three of a Kind"
            maxCount == 2 -> "Pair"
            else -> "High Card"
        }
    }
}
```

## Dart

```dart
class Solution {
  String bestHand(List<int> ranks, List<String> suits) {
    // Check for Flush
    bool flush = true;
    for (int i = 1; i < suits.length; ++i) {
      if (suits[i] != suits[0]) {
        flush = false;
        break;
      }
    }
    if (flush) return "Flush";

    // Count rank frequencies
    final Map<int, int> freq = {};
    for (final r in ranks) {
      freq[r] = (freq[r] ?? 0) + 1;
    }

    int maxCount = 0;
    for (final count in freq.values) {
      if (count > maxCount) maxCount = count;
    }

    if (maxCount >= 3) return "Three of a Kind";
    if (maxCount == 2) return "Pair";
    return "High Card";
  }
}
```

## Golang

```go
func bestHand(ranks []int, suits []byte) string {
	// Check for Flush
	allSame := true
	for i := 1; i < len(suits); i++ {
		if suits[i] != suits[0] {
			allSame = false
			break
		}
	}
	if allSame {
		return "Flush"
	}

	// Count rank frequencies
	freq := make(map[int]int)
	maxCnt := 0
	for _, r := range ranks {
		freq[r]++
		if freq[r] > maxCnt {
			maxCnt = freq[r]
		}
	}

	switch maxCnt {
	case 3:
		return "Three of a Kind"
	case 2:
		return "Pair"
	default:
		return "High Card"
	}
}
```

## Ruby

```ruby
def best_hand(ranks, suits)
  return "Flush" if suits.uniq.size == 1

  freq = Hash.new(0)
  ranks.each { |r| freq[r] += 1 }
  max_cnt = freq.values.max

  if max_cnt >= 3
    "Three of a Kind"
  elsif max_cnt == 2
    "Pair"
  else
    "High Card"
  end
end
```

## Scala

```scala
object Solution {
    def bestHand(ranks: Array[Int], suits: Array[Char]): String = {
        if (suits.distinct.length == 1) return "Flush"
        val count = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)
        for (r <- ranks) count(r) += 1
        if (count.values.exists(_ >= 3)) "Three of a Kind"
        else if (count.values.exists(_ == 2)) "Pair"
        else "High Card"
    }
}
```

## Rust

```rust
impl Solution {
    pub fn best_hand(ranks: Vec<i32>, suits: Vec<char>) -> String {
        // Check for Flush
        let first_suit = suits[0];
        if suits.iter().all(|&s| s == first_suit) {
            return "Flush".to_string();
        }

        // Count rank frequencies
        use std::collections::HashMap;
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for r in ranks {
            *freq.entry(r).or_insert(0) += 1;
        }

        if freq.values().any(|&v| v == 3) {
            return "Three of a Kind".to_string();
        }
        if freq.values().any(|&v| v == 2) {
            return "Pair".to_string();
        }

        "High Card".to_string()
    }
}
```

## Racket

```racket
#lang racket
(require racket/hash)

(define/contract (best-hand ranks suits)
  (-> (listof exact-integer?) (listof char?) string?)
  (let* ((flush?
          (if (null? suits) #t
              (let ((first-suit (car suits)))
                (for/and ([s (cdr suits)]) (char=? s first-suit)))))
         (freq (make-hash))
         (_ (for ([r ranks]) (hash-update! freq r add1 0)))
         (maxcnt (if (hash-empty? freq) 0 (apply max (hash-values freq)))))
    (cond
      [flush? "Flush"]
      [(>= maxcnt 3) "Three of a Kind"]
      [(= maxcnt 2) "Pair"]
      [else "High Card"])))
```

## Erlang

```erlang
-module(solution).
-export([best_hand/2]).

-spec best_hand(Ranks :: [integer()], Suits :: [char()]) -> unicode:unicode_binary().
best_hand(Ranks, Suits) ->
    case lists:usort(Suits) of
        [_] -> <<"Flush">>;
        _ ->
            Freqs = rank_frequencies(Ranks),
            if
                lists:any(fun(N) -> N == 3 end, Freqs) -> <<"Three of a Kind">>;
                lists:any(fun(N) -> N == 2 end, Freqs) -> <<"Pair">>;
                true -> <<"High Card">>
            end
    end.

rank_frequencies(Ranks) ->
    maps:values(
        lists:foldl(
            fun(Rank, Acc) ->
                maps:update_with(Rank,
                                 fun(Count) -> Count + 1 end,
                                 1,
                                 Acc)
            end,
            #{},
            Ranks)).
```

## Elixir

```elixir
defmodule Solution do
  @spec best_hand(ranks :: [integer], suits :: [char]) :: String.t()
  def best_hand(ranks, suits) do
    if Enum.uniq(suits) |> length() == 1 do
      "Flush"
    else
      freq = Enum.frequencies(ranks)

      cond do
        Enum.any?(freq, fn {_k, v} -> v == 3 end) -> "Three of a Kind"
        Enum.any?(freq, fn {_k, v} -> v == 2 end) -> "Pair"
        true -> "High Card"
      end
    end
  end
end
```
