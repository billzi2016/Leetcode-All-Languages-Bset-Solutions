# 0331. Verify Preorder Serialization of a Binary Tree

## Cpp

```cpp
class Solution {
public:
    bool isValidSerialization(string preorder) {
        int slots = 1;
        int n = preorder.size();
        for (int i = 0; i < n;) {
            if (slots == 0) return false;
            if (preorder[i] == '#') {
                --slots;
                ++i;
            } else {
                // skip the number
                while (i < n && preorder[i] != ',') ++i;
                --slots;          // occupy a slot
                slots += 2;       // create two new slots
            }
            if (i < n && preorder[i] == ',') ++i; // move past comma
        }
        return slots == 0;
    }
};
```

## Java

```java
class Solution {
    public boolean isValidSerialization(String preorder) {
        int slots = 1;
        for (String node : preorder.split(",")) {
            if (--slots < 0) return false;
            if (!node.equals("#")) {
                slots += 2;
            }
        }
        return slots == 0;
    }
}
```

## Python

```python
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        slots = 1
        for node in preorder.split(','):
            slots -= 1
            if slots < 0:
                return False
            if node != '#':
                slots += 2
        return slots == 0
```

## Python3

```python
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        for node in preorder.split(','):
            if slots == 0:
                return False
            slots -= 1
            if node != '#':
                slots += 2
        return slots == 0
```

## C

```c
#include <stdbool.h>

bool isValidSerialization(char* preorder) {
    int slots = 1;
    char *p = preorder;
    while (*p) {
        if (slots == 0) return false;
        if (*p == '#') {
            slots--;               // consume a slot
            p++;                   // move past '#'
        } else {
            // skip the number token
            while (*p && *p != ',') p++;
            slots--;               // consume a slot for this node
            slots += 2;            // add two slots for its children
        }
        if (*p == ',') p++;         // skip delimiter
    }
    return slots == 0;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsValidSerialization(string preorder)
    {
        int slots = 1; // start with one slot for root
        foreach (var node in preorder.Split(','))
        {
            slots--; // occupy a slot
            if (slots < 0) return false;
            if (node != "#")
            {
                slots += 2; // non-null node creates two new slots
            }
        }
        return slots == 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} preorder
 * @return {boolean}
 */
var isValidSerialization = function(preorder) {
    const nodes = preorder.split(',');
    let slots = 1; // start with one slot for the root
    
    for (let i = 0; i < nodes.length; i++) {
        // occupy a slot
        slots--;
        if (slots < 0) return false;
        
        // non-null node creates two additional slots
        if (nodes[i] !== '#') {
            slots += 2;
        }
    }
    
    return slots === 0;
};
```

## Typescript

```typescript
function isValidSerialization(preorder: string): boolean {
    const nodes = preorder.split(',');
    let slots = 1; // start with one slot for the root
    for (const node of nodes) {
        slots--; // a node occupies a slot
        if (slots < 0) return false;
        if (node !== '#') {
            slots += 2; // non-null node creates two additional slots
        }
    }
    return slots === 0;
}
```

## Php

```php
class Solution {

    /**
     * @param String $preorder
     * @return Boolean
     */
    function isValidSerialization($preorder) {
        $tokens = explode(',', $preorder);
        $slots = 1;
        foreach ($tokens as $token) {
            $slots--;
            if ($slots < 0) {
                return false;
            }
            if ($token !== '#') {
                $slots += 2;
            }
        }
        return $slots === 0;
    }
}
```

## Swift

```swift
class Solution {
    func isValidSerialization(_ preorder: String) -> Bool {
        var slots = 1
        for node in preorder.split(separator: ",") {
            slots -= 1
            if slots < 0 { return false }
            if node != "#" {
                slots += 2
            }
        }
        return slots == 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isValidSerialization(preorder: String): Boolean {
        var slots = 1
        for (node in preorder.split(',')) {
            slots--
            if (slots < 0) return false
            if (node != "#") slots += 2
        }
        return slots == 0
    }
}
```

## Dart

```dart
class Solution {
  bool isValidSerialization(String preorder) {
    int diff = 1; // one slot for the root
    for (String node in preorder.split(',')) {
      diff--; // occupy a slot
      if (diff < 0) return false;
      if (node != '#') diff += 2; // non-null node creates two new slots
    }
    return diff == 0;
  }
}
```

## Golang

```go
package main

import "strings"

func isValidSerialization(preorder string) bool {
	slots := 1
	for _, token := range strings.Split(preorder, ",") {
		slots--
		if slots < 0 {
			return false
		}
		if token != "#" {
			slots += 2
		}
	}
	return slots == 0
}
```

## Ruby

```ruby
def is_valid_serialization(preorder)
  diff = 1
  preorder.split(',').each do |node|
    diff -= 1
    return false if diff < 0
    diff += 2 unless node == '#'
  end
  diff.zero?
end
```

## Scala

```scala
object Solution {
    def isValidSerialization(preorder: String): Boolean = {
        var slots = 1
        val nodes = preorder.split(',')
        for (node <- nodes) {
            slots -= 1
            if (slots < 0) return false
            if (node != "#") slots += 2
        }
        slots == 0
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_valid_serialization(preorder: String) -> bool {
        let mut slots = 1i32;
        for token in preorder.split(',') {
            slots -= 1;
            if slots < 0 {
                return false;
            }
            if token != "#" {
                slots += 2;
            }
        }
        slots == 0
    }
}
```

## Racket

```racket
#lang racket
(require racket/string)

(define/contract (is-valid-serialization preorder)
  (-> string? boolean?)
  (let loop ((tokens (string-split preorder ","))
             (slots 1))
    (cond
      [(zero? slots) #false]                     ; no slot available for next token
      [(null? tokens) (= slots 0)]               ; all tokens processed, must have exactly zero slots left
      [else
       (define token (car tokens))
       (set! slots (- slots 1))                  ; consume one slot
       (if (string=? token "#")
           (loop (cdr tokens) slots)            ; null node adds no slots
           (loop (cdr tokens) (+ slots 2)))]))) ; non‑null node adds two slots)
```

## Erlang

```erlang
-module(solution).
-export([is_valid_serialization/1]).

-spec is_valid_serialization(Preorder :: unicode:unicode_binary()) -> boolean().
is_valid_serialization(Preorder) ->
    Tokens = binary:split(Preorder, <<",">>, [global]),
    check(Tokens, 1).

check([], Slots) ->
    Slots == 0;
check(_, Slots) when Slots =< 0 ->
    false;
check([Token|Rest], Slots) ->
    NewSlots =
        case Token of
            <<"#">> -> Slots - 1;
            _ -> Slots - 1 + 2
        end,
    check(Rest, NewSlots).
```

## Elixir

```elixir
defmodule Solution do
  @spec is_valid_serialization(preorder :: String.t) :: boolean
  def is_valid_serialization(preorder) do
    tokens = String.split(preorder, ",")
    case Enum.reduce_while(tokens, 1, fn token, slots ->
           if slots <= 0 do
             {:halt, :invalid}
           else
             new_slots =
               if token == "#" do
                 slots - 1
               else
                 slots + 1
               end

             {:cont, new_slots}
           end
         end) do
      :invalid -> false
      final when is_integer(final) -> final == 0
    end
  end
end
```
