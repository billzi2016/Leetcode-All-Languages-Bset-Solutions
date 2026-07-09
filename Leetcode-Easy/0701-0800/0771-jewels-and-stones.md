# 0771. Jewels and Stones

## Cpp

```cpp
class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        bool isJewel[128] = {false};
        for (char c : jewels) {
            isJewel[(int)c] = true;
        }
        int count = 0;
        for (char s : stones) {
            if (isJewel[(int)s]) ++count;
        }
        return count;
    }
};
```

## Java

```java
class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        boolean[] isJewel = new boolean[128];
        for (int i = 0; i < jewels.length(); i++) {
            isJewel[jewels.charAt(i)] = true;
        }
        int count = 0;
        for (int i = 0; i < stones.length(); i++) {
            if (isJewel[stones.charAt(i)]) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewel_set = set(jewels)
        return sum(1 for stone in stones if stone in jewel_set)
```

## Python3

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        return sum(1 for stone in stones if stone in jewel_set)
```

## C

```c
int numJewelsInStones(char* jewels, char* stones) {
    int isJewel[128] = {0};
    for (char *p = jewels; *p != '\0'; ++p) {
        isJewel[(unsigned char)*p] = 1;
    }
    int count = 0;
    for (char *p = stones; *p != '\0'; ++p) {
        if (isJewel[(unsigned char)*p]) {
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution
{
    public int NumJewelsInStones(string jewels, string stones)
    {
        var jewelSet = new System.Collections.Generic.HashSet<char>(jewels);
        int count = 0;
        foreach (char c in stones)
        {
            if (jewelSet.Contains(c))
                count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
    const jewelSet = new Set(jewels);
    let count = 0;
    for (const ch of stones) {
        if (jewelSet.has(ch)) count++;
    }
    return count;
};
```

## Typescript

```typescript
function numJewelsInStones(jewels: string, stones: string): number {
    const jewelSet = new Set(jewels);
    let count = 0;
    for (const ch of stones) {
        if (jewelSet.has(ch)) {
            count++;
        }
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param String $jewels
     * @param String $stones
     * @return Integer
     */
    function numJewelsInStones($jewels, $stones) {
        $jewelSet = array_flip(str_split($jewels));
        $count = 0;
        foreach (str_split($stones) as $ch) {
            if (isset($jewelSet[$ch])) {
                $count++;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func numJewelsInStones(_ jewels: String, _ stones: String) -> Int {
        let jewelSet = Set(jewels)
        var count = 0
        for ch in stones {
            if jewelSet.contains(ch) {
                count += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numJewelsInStones(jewels: String, stones: String): Int {
        val jewelSet = jewels.toHashSet()
        var count = 0
        for (c in stones) {
            if (jewelSet.contains(c)) {
                count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int numJewelsInStones(String jewels, String stones) {
    final Set<String> jewelSet = jewels.split('').toSet();
    int count = 0;
    for (final ch in stones.split('')) {
      if (jewelSet.contains(ch)) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func numJewelsInStones(jewels string, stones string) int {
	set := make(map[byte]struct{}, len(jewels))
	for i := 0; i < len(jewels); i++ {
		set[jewels[i]] = struct{}{}
	}
	count := 0
	for i := 0; i < len(stones); i++ {
		if _, ok := set[stones[i]]; ok {
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
def num_jewels_in_stones(jewels, stones)
  jewel_set = {}
  jewels.each_char { |c| jewel_set[c] = true }
  count = 0
  stones.each_char { |c| count += 1 if jewel_set.key?(c) }
  count
end
```

## Scala

```scala
object Solution {
    def numJewelsInStones(jewels: String, stones: String): Int = {
        val jewelSet = jewels.toSet
        var count = 0
        for (c <- stones) {
            if (jewelSet.contains(c)) count += 1
        }
        count
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn num_jewels_in_stones(jewels: String, stones: String) -> i32 {
        let jewel_set: HashSet<char> = jewels.chars().collect();
        stones.chars().filter(|c| jewel_set.contains(c)).count() as i32
    }
}
```

## Racket

```racket
(define/contract (num-jewels-in-stones jewels stones)
  (-> string? string? exact-integer?)
  (let* ((jewel-set (make-hash))
         (jlen (string-length jewels)))
    (for ([i (in-range jlen)])
      (hash-set! jewel-set (string-ref jewels i) #t))
    (let loop ((i 0) (cnt 0))
      (if (= i (string-length stones))
          cnt
          (loop (add1 i)
                (if (hash-has-key? jewel-set (string-ref stones i))
                    (add1 cnt)
                    cnt))))) )
```

## Erlang

```erlang
-module(solution).
-export([num_jewels_in_stones/2]).

-spec num_jewels_in_stones(Jewels :: unicode:unicode_binary(),
                           Stones :: unicode:unicode_binary()) -> integer().
num_jewels_in_stones(Jewels, Stones) ->
    JewelSet = sets:from_list(unicode:characters_to_list(Jewels)),
    count(Stones, JewelSet, 0).

count(<<>>, _, Acc) -> Acc;
count(<<Char/utf8, Rest/binary>>, Set, Acc) ->
    NewAcc = case sets:is_element(Char, Set) of
        true -> Acc + 1;
        false -> Acc
    end,
    count(Rest, Set, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_jewels_in_stones(jewels :: String.t(), stones :: String.t()) :: integer()
  def num_jewels_in_stones(jewels, stones) do
    jewel_set = MapSet.new(String.graphemes(jewels))

    stones
    |> String.graphemes()
    |> Enum.count(&MapSet.member?(jewel_set, &1))
  end
end
```
