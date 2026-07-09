# 1773. Count Items Matching a Rule

## Cpp

```cpp
class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        int idx = 0;
        if (ruleKey == "type") idx = 0;
        else if (ruleKey == "color") idx = 1;
        else /* name */ idx = 2;
        
        int cnt = 0;
        for (const auto& item : items) {
            if (item[idx] == ruleValue) ++cnt;
        }
        return cnt;
    }
};
```

## Java

```java
class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int idx;
        switch (ruleKey) {
            case "type":
                idx = 0;
                break;
            case "color":
                idx = 1;
                break;
            default: // "name"
                idx = 2;
                break;
        }
        int count = 0;
        for (List<String> item : items) {
            if (item.get(idx).equals(ruleValue)) {
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
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        idx = {"type": 0, "color": 1, "name": 2}[ruleKey]
        count = 0
        for item in items:
            if item[idx] == ruleValue:
                count += 1
        return count
```

## Python3

```python
from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        key_to_index = {"type": 0, "color": 1, "name": 2}
        idx = key_to_index[ruleKey]
        return sum(1 for item in items if item[idx] == ruleValue)
```

## C

```c
#include <string.h>

int countMatches(char*** items, int itemsSize, int* itemsColSize, char* ruleKey, char* ruleValue) {
    int idx;
    if (strcmp(ruleKey, "type") == 0) idx = 0;
    else if (strcmp(ruleKey, "color") == 0) idx = 1;
    else idx = 2; // name

    int count = 0;
    for (int i = 0; i < itemsSize; ++i) {
        if (strcmp(items[i][idx], ruleValue) == 0) {
            ++count;
        }
    }
    return count;
}
```

## Csharp

```csharp
public class Solution {
    public int CountMatches(IList<IList<string>> items, string ruleKey, string ruleValue) {
        int idx = ruleKey switch {
            "type" => 0,
            "color" => 1,
            _ => 2
        };
        int count = 0;
        foreach (var item in items) {
            if (item[idx] == ruleValue) count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[][]} items
 * @param {string} ruleKey
 * @param {string} ruleValue
 * @return {number}
 */
var countMatches = function(items, ruleKey, ruleValue) {
    let idx;
    if (ruleKey === "type") idx = 0;
    else if (ruleKey === "color") idx = 1;
    else idx = 2; // name

    let count = 0;
    for (const item of items) {
        if (item[idx] === ruleValue) count++;
    }
    return count;
};
```

## Typescript

```typescript
function countMatches(items: string[][], ruleKey: string, ruleValue: string): number {
    let idx: number;
    if (ruleKey === "type") idx = 0;
    else if (ruleKey === "color") idx = 1;
    else idx = 2; // name

    let count = 0;
    for (const item of items) {
        if (item[idx] === ruleValue) count++;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param String[][] $items
     * @param String $ruleKey
     * @param String $ruleValue
     * @return Integer
     */
    function countMatches($items, $ruleKey, $ruleValue) {
        $indexMap = [
            'type' => 0,
            'color' => 1,
            'name' => 2,
        ];
        $idx = $indexMap[$ruleKey];
        $count = 0;
        foreach ($items as $item) {
            if ($item[$idx] === $ruleValue) {
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
    func countMatches(_ items: [[String]], _ ruleKey: String, _ ruleValue: String) -> Int {
        let index: Int
        switch ruleKey {
        case "type":
            index = 0
        case "color":
            index = 1
        default: // "name"
            index = 2
        }
        var count = 0
        for item in items {
            if item[index] == ruleValue {
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
    fun countMatches(items: List<List<String>>, ruleKey: String, ruleValue: String): Int {
        val idx = when (ruleKey) {
            "type" -> 0
            "color" -> 1
            else -> 2
        }
        var count = 0
        for (item in items) {
            if (item[idx] == ruleValue) count++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
    int idx;
    if (ruleKey == 'type') {
      idx = 0;
    } else if (ruleKey == 'color') {
      idx = 1;
    } else { // name
      idx = 2;
    }
    int count = 0;
    for (var item in items) {
      if (item[idx] == ruleValue) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func countMatches(items [][]string, ruleKey string, ruleValue string) int {
	idx := 0
	switch ruleKey {
	case "type":
		idx = 0
	case "color":
		idx = 1
	case "name":
		idx = 2
	}
	count := 0
	for _, item := range items {
		if item[idx] == ruleValue {
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
def count_matches(items, rule_key, rule_value)
  idx = case rule_key
        when "type" then 0
        when "color" then 1
        else 2
        end
  items.count { |item| item[idx] == rule_value }
end
```

## Scala

```scala
object Solution {
    def countMatches(items: List[List[String]], ruleKey: String, ruleValue: String): Int = {
        val idx = ruleKey match {
            case "type"  => 0
            case "color" => 1
            case "name"  => 2
        }
        items.count(item => item(idx) == ruleValue)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_matches(items: Vec<Vec<String>>, rule_key: String, rule_value: String) -> i32 {
        let idx = match rule_key.as_str() {
            "type" => 0,
            "color" => 1,
            "name" => 2,
            _ => unreachable!(),
        };
        let mut count = 0;
        for item in items.iter() {
            if item[idx] == rule_value {
                count += 1;
            }
        }
        count as i32
    }
}
```

## Racket

```racket
(define/contract (count-matches items ruleKey ruleValue)
  (-> (listof (listof string?)) string? string? exact-integer?)
  (let ([idx (cond [(string=? ruleKey "type") 0]
                   [(string=? ruleKey "color") 1]
                   [else 2])])
    (for/sum ([item items])
      (if (string=? (list-ref item idx) ruleValue) 1 0))))
```

## Erlang

```erlang
-module(solution).
-export([count_matches/3]).

-spec count_matches(Items :: [[unicode:unicode_binary()]],
                    RuleKey :: unicode:unicode_binary(),
                    RuleValue :: unicode:unicode_binary()) -> integer().
count_matches(Items, RuleKey, RuleValue) ->
    Index = case RuleKey of
        <<"type">>  -> 1;
        <<"color">> -> 2;
        <<"name">>  -> 3
    end,
    count_items(Items, Index, RuleValue, 0).

count_items([], _Idx, _Val, Acc) ->
    Acc;
count_items([Item|Rest], Idx, Val, Acc) ->
    case lists:nth(Idx, Item) of
        Val -> count_items(Rest, Idx, Val, Acc + 1);
        _   -> count_items(Rest, Idx, Val, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_matches(items :: [[String.t]], rule_key :: String.t, rule_value :: String.t) :: integer
  def count_matches(items, rule_key, rule_value) do
    idx =
      case rule_key do
        "type" -> 0
        "color" -> 1
        "name" -> 2
      end

    Enum.count(items, fn item -> Enum.at(item, idx) == rule_value end)
  end
end
```
