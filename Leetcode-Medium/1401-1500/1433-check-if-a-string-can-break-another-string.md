# 1433. Check If a String Can Break Another String

## Cpp

```cpp
class Solution {
public:
    bool checkIfCanBreak(string s1, string s2) {
        sort(s1.begin(), s1.end());
        sort(s2.begin(), s2.end());
        bool s1Breaks = true, s2Breaks = true;
        for (size_t i = 0; i < s1.size(); ++i) {
            if (s1[i] < s2[i]) s1Breaks = false;
            if (s2[i] < s1[i]) s2Breaks = false;
        }
        return s1Breaks || s2Breaks;
    }
};
```

## Java

```java
class Solution {
    public boolean checkIfCanBreak(String s1, String s2) {
        int n = s1.length();
        char[] a = s1.toCharArray();
        char[] b = s2.toCharArray();
        java.util.Arrays.sort(a);
        java.util.Arrays.sort(b);
        boolean aBreaksB = true;
        boolean bBreaksA = true;
        for (int i = 0; i < n; i++) {
            if (a[i] < b[i]) aBreaksB = false;
            if (a[i] > b[i]) bBreaksA = false;
            // early exit if both are already false
            if (!aBreaksB && !bBreaksA) return false;
        }
        return aBreaksB || bBreaksA;
    }
}
```

## Python

```python
class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        a = sorted(s1)
        b = sorted(s2)

        # Check if a can break b
        can_a_break_b = all(x >= y for x, y in zip(a, b))
        # Check if b can break a
        can_b_break_a = all(y >= x for x, y in zip(a, b))

        return can_a_break_b or can_b_break_a
```

## Python3

```python
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        a = sorted(s1)
        b = sorted(s2)
        # Check if a can break b
        can_a_break_b = all(x >= y for x, y in zip(a, b))
        # Check if b can break a
        can_b_break_a = all(y >= x for x, y in zip(a, b))
        return can_a_break_b or can_b_break_a
```

## C

```c
#include <stdbool.h>
#include <stddef.h>
#include <string.h>
#include <stdlib.h>

bool checkIfCanBreak(char* s1, char* s2) {
    size_t n = strlen(s1);
    int cnt1[26] = {0}, cnt2[26] = {0};

    for (size_t i = 0; i < n; ++i) {
        cnt1[s1[i] - 'a']++;
        cnt2[s2[i] - 'a']++;
    }

    char *sorted1 = (char *)malloc(n);
    char *sorted2 = (char *)malloc(n);
    if (!sorted1 || !sorted2) {
        free(sorted1);
        free(sorted2);
        return false;
    }

    size_t idx = 0;
    for (int c = 0; c < 26; ++c) {
        while (cnt1[c]--) {
            sorted1[idx++] = 'a' + c;
        }
    }

    idx = 0;
    for (int c = 0; c < 26; ++c) {
        while (cnt2[c]--) {
            sorted2[idx++] = 'a' + c;
        }
    }

    bool first_ge = true, second_ge = true;
    for (size_t i = 0; i < n; ++i) {
        if (sorted1[i] < sorted2[i]) first_ge = false;
        if (sorted2[i] < sorted1[i]) second_ge = false;
    }

    free(sorted1);
    free(sorted2);
    return first_ge || second_ge;
}
```

## Csharp

```csharp
public class Solution {
    public bool CheckIfCanBreak(string s1, string s2) {
        char[] a = s1.ToCharArray();
        char[] b = s2.ToCharArray();
        System.Array.Sort(a);
        System.Array.Sort(b);
        bool aCanBreakB = true;
        bool bCanBreakA = true;
        for (int i = 0; i < a.Length; i++) {
            if (a[i] < b[i]) aCanBreakB = false;
            if (b[i] < a[i]) bCanBreakA = false;
        }
        return aCanBreakB || bCanBreakA;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkIfCanBreak = function(s1, s2) {
    const a = s1.split('').sort();
    const b = s2.split('').sort();
    let canA = true;
    let canB = true;
    for (let i = 0; i < a.length; i++) {
        if (a[i] < b[i]) canA = false;
        if (b[i] < a[i]) canB = false;
    }
    return canA || canB;
};
```

## Typescript

```typescript
function checkIfCanBreak(s1: string, s2: string): boolean {
    const a = s1.split('').sort();
    const b = s2.split('').sort();
    let canABreakB = true;
    let canBBreakA = true;
    for (let i = 0; i < a.length; i++) {
        if (a[i] < b[i]) canABreakB = false;
        if (b[i] < a[i]) canBBreakA = false;
    }
    return canABreakB || canBBreakA;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @return Boolean
     */
    function checkIfCanBreak($s1, $s2) {
        $a = str_split($s1);
        $b = str_split($s2);
        sort($a);
        sort($b);
        $n = count($a);
        $canAbreakB = true;
        $canBbreakA = true;
        for ($i = 0; $i < $n; $i++) {
            if (ord($a[$i]) < ord($b[$i])) {
                $canAbreakB = false;
            }
            if (ord($a[$i]) > ord($b[$i])) {
                $canBbreakA = false;
            }
        }
        return $canAbreakB || $canBbreakA;
    }
}
```

## Swift

```swift
class Solution {
    func checkIfCanBreak(_ s1: String, _ s2: String) -> Bool {
        let arr1 = s1.sorted()
        let arr2 = s2.sorted()
        var canFirstBreakSecond = true
        var canSecondBreakFirst = true
        
        for i in 0..<arr1.count {
            if arr1[i] < arr2[i] {
                canFirstBreakSecond = false
            }
            if arr2[i] < arr1[i] {
                canSecondBreakFirst = false
            }
        }
        return canFirstBreakSecond || canSecondBreakFirst
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkIfCanBreak(s1: String, s2: String): Boolean {
        val a = s1.toCharArray()
        val b = s2.toCharArray()
        a.sort()
        b.sort()
        var canAStrictlyBreakB = true
        var canBStrictlyBreakA = true
        for (i in a.indices) {
            if (a[i] < b[i]) canAStrictlyBreakB = false
            if (a[i] > b[i]) canBStrictlyBreakA = false
        }
        return canAStrictlyBreakB || canBStrictlyBreakA
    }
}
```

## Dart

```dart
class Solution {
  bool checkIfCanBreak(String s1, String s2) {
    List<int> a = s1.codeUnits..sort();
    List<int> b = s2.codeUnits..sort();

    bool aBreaksB = true;
    bool bBreaksA = true;

    for (int i = 0; i < a.length; i++) {
      if (a[i] < b[i]) aBreaksB = false;
      if (b[i] < a[i]) bBreaksA = false;
    }

    return aBreaksB || bBreaksA;
  }
}
```

## Golang

```go
package main

import "sort"

func checkIfCanBreak(s1 string, s2 string) bool {
	b1 := []byte(s1)
	b2 := []byte(s2)

	sort.Slice(b1, func(i, j int) bool { return b1[i] < b1[j] })
	sort.Slice(b2, func(i, j int) bool { return b2[i] < b2[j] })

	can1 := true
	for i := 0; i < len(b1); i++ {
		if b1[i] < b2[i] {
			can1 = false
			break
		}
	}
	if can1 {
		return true
	}

	can2 := true
	for i := 0; i < len(b1); i++ {
		if b2[i] < b1[i] {
			can2 = false
			break
		}
	}
	return can2
}
```

## Ruby

```ruby
def check_if_can_break(s1, s2)
  a = s1.chars.sort
  b = s2.chars.sort
  can_a_break_b = true
  can_b_break_a = true

  a.each_index do |i|
    if a[i] < b[i]
      can_a_break_b = false
    elsif a[i] > b[i]
      can_b_break_a = false
    end
  end

  can_a_break_b || can_b_break_a
end
```

## Scala

```scala
object Solution {
    def checkIfCanBreak(s1: String, s2: String): Boolean = {
        val arr1 = s1.toCharArray
        java.util.Arrays.sort(arr1)
        val arr2 = s2.toCharArray
        java.util.Arrays.sort(arr2)

        var can1 = true // arr1 can break arr2
        var can2 = true // arr2 can break arr1

        var i = 0
        while (i < arr1.length) {
            if (arr1(i) < arr2(i)) can1 = false
            if (arr2(i) < arr1(i)) can2 = false
            i += 1
        }
        can1 || can2
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_if_can_break(s1: String, s2: String) -> bool {
        let mut a = s1.into_bytes();
        let mut b = s2.into_bytes();
        a.sort_unstable();
        b.sort_unstable();

        let mut a_ge_b = true;
        let mut b_ge_a = true;

        for i in 0..a.len() {
            if a[i] < b[i] {
                a_ge_b = false;
            }
            if b[i] < a[i] {
                b_ge_a = false;
            }
            if !a_ge_b && !b_ge_a {
                return false;
            }
        }

        a_ge_b || b_ge_a
    }
}
```

## Racket

```racket
(define/contract (check-if-can-break s1 s2)
  (-> string? string? boolean?)
  (let* ((sorted1 (sort (string->list s1) char<?))
         (sorted2 (sort (string->list s2) char<?)))
    (define (can-break? a b)
      (let loop ((as a) (bs b))
        (cond [(null? as) #t]
              [(char<=? (car bs) (car as)) (loop (cdr as) (cdr bs))]
              [else #f])))
    (or (can-break? sorted1 sorted2)
        (can-break? sorted2 sorted1))))
```

## Erlang

```erlang
-module(solution).
-export([check_if_can_break/2]).

-spec check_if_can_break(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> boolean().
check_if_can_break(S1, S2) ->
    Sorted1 = lists:sort(binary_to_list(S1)),
    Sorted2 = lists:sort(binary_to_list(S2)),
    case can_break(Sorted1, Sorted2) of
        true -> true;
        false -> can_break(Sorted2, Sorted1)
    end.

can_break([], []) -> true;
can_break([H1|T1], [H2|T2]) when H1 >= H2 ->
    can_break(T1, T2);
can_break(_, _) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_if_can_break(s1 :: String.t(), s2 :: String.t()) :: boolean()
  def check_if_can_break(s1, s2) do
    a = :binary.bin_to_list(s1) |> Enum.sort()
    b = :binary.bin_to_list(s2) |> Enum.sort()

    can_break?(a, b) or can_break?(b, a)
  end

  defp can_break?(list1, list2) do
    Enum.zip(list1, list2)
    |> Enum.reduce_while(true, fn {x, y}, _acc ->
      if x >= y, do: {:cont, true}, else: {:halt, false}
    end)
  end
end
```
