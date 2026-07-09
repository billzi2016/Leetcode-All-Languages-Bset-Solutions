# 1318. Minimum Flips to Make a OR b Equal to c

## Cpp

```cpp
class Solution {
public:
    int minFlips(int a, int b, int c) {
        int flips = 0;
        for (int i = 0; i < 32; ++i) {
            int ai = (a >> i) & 1;
            int bi = (b >> i) & 1;
            int ci = (c >> i) & 1;
            if (ci == 0) {
                flips += ai + bi; // both must be 0
            } else { // ci == 1
                if (ai == 0 && bi == 0) ++flips; // need at least one 1
            }
        }
        return flips;
    }
};
```

## Java

```java
class Solution {
    public int minFlips(int a, int b, int c) {
        int flips = 0;
        for (int i = 0; i < 32; i++) {
            int bitA = (a >> i) & 1;
            int bitB = (b >> i) & 1;
            int bitC = (c >> i) & 1;
            if (bitC == 0) {
                flips += bitA + bitB; // both must be 0
            } else { // bitC == 1
                if (bitA == 0 && bitB == 0) {
                    flips++; // need at least one to be 1
                }
            }
        }
        return flips;
    }
}
```

## Python

```python
class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        flips = 0
        while a or b or c:
            a_bit = a & 1
            b_bit = b & 1
            c_bit = c & 1

            if c_bit == 0:
                # both bits must be 0
                flips += a_bit + b_bit
            else:  # c_bit == 1
                # at least one bit must be 1
                if a_bit == 0 and b_bit == 0:
                    flips += 1

            a >>= 1
            b >>= 1
            c >>= 1
        return flips
```

## Python3

```python
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            ai = a & 1
            bi = b & 1
            ci = c & 1
            if ci == 0:
                flips += ai + bi  # both must be 0
            else:  # ci == 1
                if ai == 0 and bi == 0:
                    flips += 1  # need at least one to be 1
            a >>= 1
            b >>= 1
            c >>= 1
        return flips
```

## C

```c
int minFlips(int a, int b, int c){
    int flips = 0;
    while (a || b || c) {
        int ai = a & 1;
        int bi = b & 1;
        int ci = c & 1;
        if (ci) {
            if (!ai && !bi) ++flips;
        } else {
            flips += ai + bi;
        }
        a >>= 1;
        b >>= 1;
        c >>= 1;
    }
    return flips;
}
```

## Csharp

```csharp
public class Solution {
    public int MinFlips(int a, int b, int c) {
        int flips = 0;
        for (int i = 0; i < 32; i++) {
            int ai = (a >> i) & 1;
            int bi = (b >> i) & 1;
            int ci = (c >> i) & 1;
            if (ci == 0) {
                flips += ai + bi; // both must be 0
            } else { // ci == 1
                if (ai == 0 && bi == 0) {
                    flips += 1; // need at least one to be 1
                }
            }
        }
        return flips;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var minFlips = function(a, b, c) {
    let flips = 0;
    while (a > 0 || b > 0 || c > 0) {
        const ai = a & 1;
        const bi = b & 1;
        const ci = c & 1;
        if (ci === 0) {
            flips += ai + bi; // both must be 0
        } else { // ci === 1
            if (ai === 0 && bi === 0) flips += 1; // need at least one 1
        }
        a >>>= 1;
        b >>>= 1;
        c >>>= 1;
    }
    return flips;
};
```

## Typescript

```typescript
function minFlips(a: number, b: number, c: number): number {
    let flips = 0;
    while (a > 0 || b > 0 || c > 0) {
        const ai = a & 1;
        const bi = b & 1;
        const ci = c & 1;
        if (ci === 0) {
            flips += ai + bi;
        } else {
            if (ai === 0 && bi === 0) flips++;
        }
        a >>= 1;
        b >>= 1;
        c >>= 1;
    }
    return flips;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return Integer
     */
    function minFlips($a, $b, $c) {
        $flips = 0;
        while ($a > 0 || $b > 0 || $c > 0) {
            $ai = $a & 1;
            $bi = $b & 1;
            $ci = $c & 1;
            if ($ci == 0) {
                $flips += $ai + $bi;
            } else {
                if ($ai == 0 && $bi == 0) {
                    $flips++;
                }
            }
            $a >>= 1;
            $b >>= 1;
            $c >>= 1;
        }
        return $flips;
    }
}
```

## Swift

```swift
class Solution {
    func minFlips(_ a: Int, _ b: Int, _ c: Int) -> Int {
        var flips = 0
        var aa = a
        var bb = b
        var cc = c
        while aa > 0 || bb > 0 || cc > 0 {
            let abit = aa & 1
            let bbit = bb & 1
            let cbit = cc & 1
            if cbit == 0 {
                flips += (abit) + (bbit)
            } else { // cbit == 1
                if abit == 0 && bbit == 0 {
                    flips += 1
                }
            }
            aa >>= 1
            bb >>= 1
            cc >>= 1
        }
        return flips
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minFlips(a: Int, b: Int, c: Int): Int {
        var aa = a
        var bb = b
        var cc = c
        var flips = 0
        while (aa != 0 || bb != 0 || cc != 0) {
            val ai = aa and 1
            val bi = bb and 1
            val ci = cc and 1
            if (ci == 0) {
                flips += ai + bi
            } else {
                if (ai == 0 && bi == 0) flips++
            }
            aa = aa ushr 1
            bb = bb ushr 1
            cc = cc ushr 1
        }
        return flips
    }
}
```

## Golang

```go
func minFlips(a int, b int, c int) int {
	flips := 0
	for i := 0; (a>>i)|(b>>i)|(c>>i) != 0; i++ {
		abit := (a >> i) & 1
		bbit := (b >> i) & 1
		cbit := (c >> i) & 1
		if cbit == 0 {
			flips += abit + bbit
		} else {
			if abit == 0 && bbit == 0 {
				flips++
			}
		}
	}
	return flips
}
```

## Ruby

```ruby
def min_flips(a, b, c)
  flips = 0
  while a > 0 || b > 0 || c > 0
    ai = a & 1
    bi = b & 1
    ci = c & 1
    if ci == 0
      flips += ai + bi
    else
      flips += 1 if ai == 0 && bi == 0
    end
    a >>= 1
    b >>= 1
    c >>= 1
  end
  flips
end
```

## Scala

```scala
object Solution {
    def minFlips(a: Int, b: Int, c: Int): Int = {
        var flips = 0
        for (i <- 0 until 31) {
            val mask = 1 << i
            val ai = if ((a & mask) != 0) 1 else 0
            val bi = if ((b & mask) != 0) 1 else 0
            val ci = if ((c & mask) != 0) 1 else 0
            if (ci == 0) {
                flips += ai + bi
            } else { // ci == 1
                if (ai == 0 && bi == 0) flips += 1
            }
        }
        flips
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_flips(a: i32, b: i32, c: i32) -> i32 {
        let mut flips: i32 = 0;
        for i in 0..=30 {
            let mask = 1 << i;
            let ai = (a & mask) != 0;
            let bi = (b & mask) != 0;
            let ci = (c & mask) != 0;
            if !ci {
                if ai { flips += 1; }
                if bi { flips += 1; }
            } else {
                if !ai && !bi {
                    flips += 1;
                }
            }
        }
        flips
    }
}
```
