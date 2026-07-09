# 1447. Simplified Fractions

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> simplifiedFractions(int n) {
        vector<string> res;
        for (int d = 2; d <= n; ++d) {
            for (int num = 1; num < d; ++num) {
                if (std::gcd(num, d) == 1) {
                    res.push_back(to_string(num) + "/" + to_string(d));
                }
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public List<String> simplifiedFractions(int n) {
        List<String> res = new ArrayList<>();
        for (int denom = 2; denom <= n; denom++) {
            for (int num = 1; num < denom; num++) {
                if (gcd(num, denom) == 1) {
                    res.add(num + "/" + denom);
                }
            }
        }
        return res;
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
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        from math import gcd
        res = []
        for denom in range(2, n + 1):
            for num in range(1, denom):
                if gcd(num, denom) == 1:
                    res.append(f"{num}/{denom}")
        return res
```

## Python3

```python
from typing import List
import math

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for denom in range(2, n + 1):
            for num in range(1, denom):
                if math.gcd(num, denom) == 1:
                    res.append(f"{num}/{denom}")
        return res
```

## C

```c
#include <stdlib.h>
#include <stdio.h>

static int gcd(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** simplifiedFractions(int n, int* returnSize) {
    int total = 0;
    for (int d = 2; d <= n; ++d) {
        for (int num = 1; num < d; ++num) {
            if (gcd(num, d) == 1) ++total;
        }
    }
    *returnSize = total;
    if (total == 0) return NULL;

    char **res = (char **)malloc(total * sizeof(char *));
    int idx = 0;
    for (int d = 2; d <= n; ++d) {
        for (int num = 1; num < d; ++num) {
            if (gcd(num, d) == 1) {
                int len = snprintf(NULL, 0, "%d/%d", num, d);
                char *s = (char *)malloc(len + 1);
                sprintf(s, "%d/%d", num, d);
                res[idx++] = s;
            }
        }
    }
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public IList<string> SimplifiedFractions(int n) {
        var result = new List<string>();
        for (int denominator = 2; denominator <= n; denominator++) {
            for (int numerator = 1; numerator < denominator; numerator++) {
                if (Gcd(numerator, denominator) == 1) {
                    result.Add($"{numerator}/{denominator}");
                }
            }
        }
        return result;
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
 * @param {number} n
 * @return {string[]}
 */
var simplifiedFractions = function(n) {
    const result = [];
    const gcd = (a, b) => {
        while (b !== 0) {
            const temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    };
    
    for (let denominator = 2; denominator <= n; denominator++) {
        for (let numerator = 1; numerator < denominator; numerator++) {
            if (gcd(numerator, denominator) === 1) {
                result.push(`${numerator}/${denominator}`);
            }
        }
    }
    
    return result;
};
```

## Typescript

```typescript
function simplifiedFractions(n: number): string[] {
    const res: string[] = [];
    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    for (let denom = 2; denom <= n; ++denom) {
        for (let num = 1; num < denom; ++num) {
            if (gcd(num, denom) === 1) {
                res.push(`${num}/${denom}`);
            }
        }
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return String[]
     */
    function simplifiedFractions($n) {
        $result = [];
        for ($den = 2; $den <= $n; $den++) {
            for ($num = 1; $num < $den; $num++) {
                if ($this->gcd($num, $den) === 1) {
                    $result[] = $num . '/' . $den;
                }
            }
        }
        return $result;
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
    func simplifiedFractions(_ n: Int) -> [String] {
        if n < 2 { return [] }
        var result = [String]()
        for denom in 2...n {
            for num in 1..<denom {
                if gcd(num, denom) == 1 {
                    result.append("\(num)/\(denom)")
                }
            }
        }
        return result
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
    fun simplifiedFractions(n: Int): List<String> {
        val result = mutableListOf<String>()
        for (den in 2..n) {
            for (num in 1 until den) {
                if (gcd(num, den) == 1) {
                    result.add("$num/$den")
                }
            }
        }
        return result
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val temp = x % y
            x = y
            y = temp
        }
        return x
    }
}
```

## Dart

```dart
class Solution {
  List<String> simplifiedFractions(int n) {
    List<String> res = [];
    for (int denominator = 2; denominator <= n; denominator++) {
      for (int numerator = 1; numerator < denominator; numerator++) {
        if (_gcd(numerator, denominator) == 1) {
          res.add('$numerator/$denominator');
        }
      }
    }
    return res;
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      int temp = a % b;
      a = b;
      b = temp;
    }
    return a;
  }
}
```

## Golang

```go
package main

import "strconv"

func simplifiedFractions(n int) []string {
	res := []string{}
	for d := 2; d <= n; d++ {
		for num := 1; num < d; num++ {
			if gcd(num, d) == 1 {
				res = append(res, strconv.Itoa(num)+"/"+strconv.Itoa(d))
			}
		}
	}
	return res
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
```

## Ruby

```ruby
# @param {Integer} n
# @return {String[]}
def simplified_fractions(n)
  result = []
  (2..n).each do |den|
    (1...den).each do |num|
      result << "#{num}/#{den}" if num.gcd(den) == 1
    end
  end
  result
end
```

## Scala

```scala
object Solution {
  def simplifiedFractions(n: Int): List[String] = {
    val res = scala.collection.mutable.ListBuffer[String]()
    for (b <- 2 to n) {
      for (a <- 1 until b) {
        if (gcd(a, b) == 1) res += s"$a/$b"
      }
    }
    res.toList
  }

  @annotation.tailrec
  private def gcd(x: Int, y: Int): Int = {
    if (y == 0) x else gcd(y, x % y)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn simplified_fractions(n: i32) -> Vec<String> {
        let mut res = Vec::new();
        for b in 2..=n {
            for a in 1..b {
                if Self::gcd(a, b) == 1 {
                    res.push(format!("{}/{}", a, b));
                }
            }
        }
        res
    }

    fn gcd(mut a: i32, mut b: i32) -> i32 {
        while b != 0 {
            let t = a % b;
            a = b;
            b = t;
        }
        a.abs()
    }
}
```

## Racket

```racket
(define/contract (simplified-fractions n)
  (-> exact-integer? (listof string?))
  (for*/list ([den (in-range 2 (add1 n))]
              [num (in-range 1 den)]
              #:when (= (gcd num den) 1))
    (format "~a/~a" num den)))
```

## Erlang

```erlang
-spec simplified_fractions(N :: integer()) -> [unicode:unicode_binary()].
simplified_fractions(N) ->
    [list_to_binary(io_lib:format("~p/~p", [A, B]))
     || B <- lists:seq(2, N),
        A <- lists:seq(1, B - 1),
        erlang:gcd(A, B) =:= 1].
```

## Elixir

```elixir
defmodule Solution do
  @spec simplified_fractions(n :: integer) :: [String.t()]
  def simplified_fractions(n) do
    for b <- 2..n, a <- 1..b-1, Integer.gcd(a, b) == 1, do: "#{a}/#{b}"
  end
end
```
