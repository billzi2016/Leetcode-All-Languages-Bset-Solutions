# 0914. X of a Kind in a Deck of Cards

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        if (deck.empty()) return false;
        unordered_map<int,int> cnt;
        for (int c : deck) ++cnt[c];
        int g = 0;
        for (auto &p : cnt) {
            g = std::gcd(g, p.second);
        }
        return g > 1;
    }
};
```

## Java

```java
class Solution {
    public boolean hasGroupsSizeX(int[] deck) {
        int[] count = new int[10001];
        for (int card : deck) {
            count[card]++;
        }
        int g = 0;
        for (int c : count) {
            if (c > 0) {
                g = gcd(g, c);
                if (g == 1) { // early exit
                    return false;
                }
            }
        }
        return g > 1;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int tmp = a % b;
            a = b;
            b = tmp;
        }
        return a;
    }
}
```

## Python

```python
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        from collections import Counter
        from math import gcd
        count = Counter(deck).values()
        g = 0
        for c in count:
            g = gcd(g, c)
        return g > 1
```

## Python3

```python
from typing import List
import collections
import math

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = collections.Counter(deck)
        g = 0
        for c in count.values():
            g = math.gcd(g, c)
        return g > 1
```

## C

```c
#include <stdbool.h>

static int gcd(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

bool hasGroupsSizeX(int* deck, int deckSize) {
    if (deckSize == 0) return false;

    const int MAX_VAL = 10000;
    int freq[MAX_VAL + 1] = {0};

    for (int i = 0; i < deckSize; ++i) {
        int v = deck[i];
        if (v >= 0 && v <= MAX_VAL)
            ++freq[v];
    }

    int g = 0;
    for (int i = 0; i <= MAX_VAL; ++i) {
        if (freq[i] > 0) {
            if (g == 0)
                g = freq[i];
            else
                g = gcd(g, freq[i]);
        }
    }

    return g > 1;
}
```

## Csharp

```csharp
public class Solution {
    public bool HasGroupsSizeX(int[] deck) {
        var count = new Dictionary<int, int>();
        foreach (int card in deck) {
            if (count.ContainsKey(card))
                count[card]++;
            else
                count[card] = 1;
        }

        int g = 0;
        foreach (int c in count.Values) {
            g = Gcd(g, c);
            if (g == 1) return false; // early exit, cannot satisfy X >= 2
        }
        return g > 1;
    }

    private int Gcd(int a, int b) {
        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} deck
 * @return {boolean}
 */
var hasGroupsSizeX = function(deck) {
    const freq = new Map();
    for (const card of deck) {
        freq.set(card, (freq.get(card) || 0) + 1);
    }
    
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    
    let g = 0;
    for (const count of freq.values()) {
        g = g === 0 ? count : gcd(g, count);
        if (g === 1) return false; // early exit
    }
    return g > 1;
};
```

## Typescript

```typescript
function hasGroupsSizeX(deck: number[]): boolean {
    const freq = new Map<number, number>();
    for (const card of deck) {
        freq.set(card, (freq.get(card) ?? 0) + 1);
    }

    let g = 0;
    for (const count of freq.values()) {
        g = gcd(g, count);
        if (g === 1) return false; // early exit
    }
    return g >= 2;
}

function gcd(a: number, b: number): number {
    while (b !== 0) {
        const t = a % b;
        a = b;
        b = t;
    }
    return a;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $deck
     * @return Boolean
     */
    function hasGroupsSizeX($deck) {
        $freq = [];
        foreach ($deck as $card) {
            if (!isset($freq[$card])) {
                $freq[$card] = 0;
            }
            $freq[$card]++;
        }

        $g = 0;
        foreach ($freq as $cnt) {
            $g = $this->gcd($g, $cnt);
        }

        return $g > 1;
    }

    private function gcd($a, $b) {
        while ($b != 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return $a;
    }
}
```

## Swift

```swift
class Solution {
    func hasGroupsSizeX(_ deck: [Int]) -> Bool {
        guard !deck.isEmpty else { return false }
        var freq = [Int: Int]()
        for card in deck {
            freq[card, default: 0] += 1
        }
        var currentGCD = -1
        for count in freq.values {
            if currentGCD == -1 {
                currentGCD = count
            } else {
                currentGCD = gcd(currentGCD, count)
            }
        }
        return currentGCD >= 2
    }
    
    private func gcd(_ a: Int, _ b: Int) -> Int {
        var x = a
        var y = b
        while y != 0 {
            let temp = x % y
            x = y
            y = temp
        }
        return x
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun hasGroupsSizeX(deck: IntArray): Boolean {
        if (deck.isEmpty()) return false
        val freq = HashMap<Int, Int>()
        for (card in deck) {
            freq[card] = (freq[card] ?: 0) + 1
        }
        var g = 0
        for (count in freq.values) {
            g = if (g == 0) count else gcd(g, count)
            if (g == 1) return false
        }
        return g > 1
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val tmp = x % y
            x = y
            y = tmp
        }
        return kotlin.math.abs(x)
    }
}
```

## Dart

```dart
class Solution {
  bool hasGroupsSizeX(List<int> deck) {
    final Map<int, int> freq = {};
    for (final int card in deck) {
      freq[card] = (freq[card] ?? 0) + 1;
    }

    int g = 0;
    for (final int count in freq.values) {
      g = _gcd(g, count);
    }
    return g > 1;
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      final int temp = a % b;
      a = b;
      b = temp;
    }
    return a.abs();
  }
}
```

## Golang

```go
func hasGroupsSizeX(deck []int) bool {
	if len(deck) == 0 {
		return false
	}
	freq := make(map[int]int, len(deck))
	for _, v := range deck {
		freq[v]++
	}
	g := 0
	for _, c := range freq {
		if g == 0 {
			g = c
		} else {
			g = gcd(g, c)
		}
		if g == 1 { // early exit, cannot be >1 anymore
			return false
		}
	}
	return g > 1
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	if a < 0 {
		return -a
	}
	return a
}
```

## Ruby

```ruby
def has_groups_size_x(deck)
  counts = Hash.new(0)
  deck.each { |c| counts[c] += 1 }
  gcd_val = nil
  counts.each_value do |cnt|
    gcd_val = gcd_val ? gcd_val.gcd(cnt) : cnt
  end
  gcd_val && gcd_val > 1
end
```

## Scala

```scala
object Solution {
    def hasGroupsSizeX(deck: Array[Int]): Boolean = {
        if (deck.isEmpty) return false
        val maxVal = 10000
        val freq = new Array[Int](maxVal + 1)
        for (c <- deck) {
            freq(c) += 1
        }

        def gcd(a: Int, b: Int): Int = {
            var x = a
            var y = b
            while (y != 0) {
                val tmp = x % y
                x = y
                y = tmp
            }
            math.abs(x)
        }

        var g = 0
        for (cnt <- freq if cnt > 0) {
            g = if (g == 0) cnt else gcd(g, cnt)
        }
        g >= 2
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn has_groups_size_x(deck: Vec<i32>) -> bool {
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for card in deck {
            *freq.entry(card).or_insert(0) += 1;
        }

        fn gcd(mut a: i32, mut b: i32) -> i32 {
            while b != 0 {
                let r = a % b;
                a = b;
                b = r;
            }
            a.abs()
        }

        let mut g = 0;
        for &count in freq.values() {
            if g == 0 {
                g = count;
            } else {
                g = gcd(g, count);
            }
            if g == 1 {
                return false; // early exit
            }
        }
        g > 1
    }
}
```

## Racket

```racket
(define/contract (has-groups-size-x deck)
  (-> (listof exact-integer?) boolean?)
  (let ((freq (make-hash)))
    (for ([v deck])
      (hash-update! freq v (lambda (old) (+ old 1)) 0))
    (let* ((counts (hash-values freq))
           (g (foldl gcd (car counts) (cdr counts))))
      (> g 1))))
```

## Erlang

```erlang
-module(solution).
-export([has_groups_size_x/1]).
-spec has_groups_size_x(Deck :: [integer()]) -> boolean().
has_groups_size_x(Deck) ->
    Counts = count_freq(Deck, #{}),
    Gcd = maps:fold(fun(_Key, Val, Acc) -> gcd(Acc, Val) end, 0, Counts),
    Gcd > 1.

count_freq([], Map) -> Map;
count_freq([H|T], Map) ->
    NewMap = maps:update_with(H,
                               fun(C) -> C + 1 end,
                               1,
                               Map),
    count_freq(T, NewMap).

gcd(A, 0) -> A;
gcd(0, B) -> B;
gcd(A, B) when A < B ->
    gcd(B, A);
gcd(A, B) ->
    gcd(B, A rem B).
```

## Elixir

```elixir
defmodule Solution do
  @spec has_groups_size_x(deck :: [integer]) :: boolean
  def has_groups_size_x(deck) do
    freq = Enum.reduce(deck, %{}, fn x, acc ->
      Map.update(acc, x, 1, &(&1 + 1))
    end)

    counts = Map.values(freq)

    gcd =
      Enum.reduce(counts, 0, fn count, acc ->
        Integer.gcd(count, acc)
      end)

    gcd > 1
  end
end
```
