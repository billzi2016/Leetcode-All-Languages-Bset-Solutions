# 0984. String Without AAA or BBB

## Cpp

```cpp
class Solution {
public:
    string strWithout3a3b(int a, int b) {
        string res;
        while (a > 0 || b > 0) {
            int n = res.size();
            bool canA = a > 0 && !(n >= 2 && res[n-1] == 'a' && res[n-2] == 'a');
            bool canB = b > 0 && !(n >= 2 && res[n-1] == 'b' && res[n-2] == 'b');
            
            if (canA && (!canB || a > b)) {
                res.push_back('a');
                --a;
            } else {
                res.push_back('b');
                --b;
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String strWithout3a3b(int a, int b) {
        StringBuilder sb = new StringBuilder();
        while (a > 0 || b > 0) {
            int len = sb.length();
            boolean lastTwoA = len >= 2 && sb.charAt(len - 1) == 'a' && sb.charAt(len - 2) == 'a';
            boolean lastTwoB = len >= 2 && sb.charAt(len - 1) == 'b' && sb.charAt(len - 2) == 'b';
            if (lastTwoA) {
                // must place 'b'
                sb.append('b');
                b--;
            } else if (lastTwoB) {
                // must place 'a'
                sb.append('a');
                a--;
            } else {
                // choose the character with more remaining count
                if (a >= b) {
                    sb.append('a');
                    a--;
                } else {
                    sb.append('b');
                    b--;
                }
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def strWithout3a3b(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """
        res = []
        while a > 0 or b > 0:
            if len(res) >= 2 and res[-1] == res[-2]:
                # need to place the opposite character
                if res[-1] == 'a':
                    res.append('b')
                    b -= 1
                else:
                    res.append('a')
                    a -= 1
            else:
                # place the character with more remaining count
                if a >= b:
                    res.append('a')
                    a -= 1
                else:
                    res.append('b')
                    b -= 1
        return ''.join(res)
```

## Python3

```python
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        while a > 0 or b > 0:
            if a > b:
                cnt = min(2, a)
                res.append('a' * cnt)
                a -= cnt
                if b > 0:
                    res.append('b')
                    b -= 1
            else:
                cnt = min(2, b)
                res.append('b' * cnt)
                b -= cnt
                if a > 0:
                    res.append('a')
                    a -= 1
        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

char *strWithout3a3b(int a, int b) {
    int total = a + b;
    char *res = (char *)malloc(total + 1);
    int idx = 0;

    while (a > 0 || b > 0) {
        bool lastTwoA = false, lastTwoB = false;
        if (idx >= 2) {
            if (res[idx - 1] == 'a' && res[idx - 2] == 'a') lastTwoA = true;
            if (res[idx - 1] == 'b' && res[idx - 2] == 'b') lastTwoB = true;
        }

        if ((a > b && !lastTwoA) || (b == 0 && !lastTwoA)) {
            // place 'a'
            res[idx++] = 'a';
            a--;
        } else if ((b > a && !lastTwoB) || (a == 0 && !lastTwoB)) {
            // place 'b'
            res[idx++] = 'b';
            b--;
        } else {
            // need to place the opposite character to avoid three in a row
            if (lastTwoA) {
                res[idx++] = 'b';
                b--;
            } else { // lastTwoB must be true
                res[idx++] = 'a';
                a--;
            }
        }
    }

    res[idx] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string StrWithout3a3b(int a, int b) {
        var sb = new System.Text.StringBuilder();
        while (a > 0 || b > 0) {
            if (a > b) {
                if (a > 1) {
                    sb.Append("aa");
                    a -= 2;
                } else {
                    sb.Append('a');
                    a--;
                }
                if (b > 0) {
                    sb.Append('b');
                    b--;
                }
            } else {
                if (b > 1) {
                    sb.Append("bb");
                    b -= 2;
                } else {
                    sb.Append('b');
                    b--;
                }
                if (a > 0) {
                    sb.Append('a');
                    a--;
                }
            }
        }
        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {number} a
 * @param {number} b
 * @return {string}
 */
var strWithout3a3b = function(a, b) {
    let res = "";
    while (a > 0 || b > 0) {
        if (a > b) {
            if (res.endsWith("aa")) {
                // must place 'b' to avoid three consecutive 'a'
                res += "b";
                b--;
            } else {
                // place up to two 'a's
                const take = Math.min(2, a);
                res += "a".repeat(take);
                a -= take;
            }
        } else {
            if (res.endsWith("bb")) {
                // must place 'a' to avoid three consecutive 'b'
                res += "a";
                a--;
            } else {
                // place up to two 'b's
                const take = Math.min(2, b);
                res += "b".repeat(take);
                b -= take;
            }
        }
    }
    return res;
};
```

## Typescript

```typescript
function strWithout3a3b(a: number, b: number): string {
    let res = "";
    while (a > 0 || b > 0) {
        if (res.endsWith("aa")) {
            const cnt = Math.min(2, b);
            res += "b".repeat(cnt);
            b -= cnt;
        } else if (res.endsWith("bb")) {
            const cnt = Math.min(2, a);
            res += "a".repeat(cnt);
            a -= cnt;
        } else {
            if (a >= b) {
                const cnt = Math.min(2, a);
                res += "a".repeat(cnt);
                a -= cnt;
            } else {
                const cnt = Math.min(2, b);
                res += "b".repeat(cnt);
                b -= cnt;
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
     * @param Integer $a
     * @param Integer $b
     * @return String
     */
    function strWithout3a3b($a, $b) {
        $res = '';
        while ($a > 0 || $b > 0) {
            $len = strlen($res);
            $last1 = $len >= 1 ? $res[$len - 1] : '';
            $last2 = $len >= 2 ? $res[$len - 2] : '';

            // If the last two characters are the same, we must add the opposite character
            if ($last1 !== '' && $last1 === $last2) {
                if ($last1 === 'a') {
                    $res .= 'b';
                    $b--;
                } else {
                    $res .= 'a';
                    $a--;
                }
            } else {
                // Otherwise, add the character with the larger remaining count
                if ($a >= $b) {
                    $res .= 'a';
                    $a--;
                } else {
                    $res .= 'b';
                    $b--;
                }
            }
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func strWithout3a3b(_ a: Int, _ b: Int) -> String {
        var a = a
        var b = b
        var result = [Character]()
        
        while a > 0 || b > 0 {
            if a >= b {
                // try to place 'a' if it doesn't create three consecutive 'a's
                if a > 0 && (result.count < 2 ||
                    !(result[result.count - 1] == "a" && result[result.count - 2] == "a")) {
                    result.append("a")
                    a -= 1
                } else {
                    // place 'b' instead
                    result.append("b")
                    b -= 1
                }
            } else {
                // try to place 'b' if it doesn't create three consecutive 'b's
                if b > 0 && (result.count < 2 ||
                    !(result[result.count - 1] == "b" && result[result.count - 2] == "b")) {
                    result.append("b")
                    b -= 1
                } else {
                    // place 'a' instead
                    result.append("a")
                    a -= 1
                }
            }
        }
        
        return String(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun strWithout3a3b(a: Int, b: Int): String {
        var A = a
        var B = b
        val sb = StringBuilder()
        while (A > 0 || B > 0) {
            val len = sb.length
            val last1 = if (len >= 1) sb[len - 1] else ' '
            val last2 = if (len >= 2) sb[len - 2] else ' '
            when {
                A > B -> {
                    if (last1 == 'a' && last2 == 'a') {
                        sb.append('b')
                        B--
                    } else {
                        sb.append('a')
                        A--
                    }
                }
                B > A -> {
                    if (last1 == 'b' && last2 == 'b') {
                        sb.append('a')
                        A--
                    } else {
                        sb.append('b')
                        B--
                    }
                }
                else -> { // A == B
                    if (last1 == 'a' && last2 == 'a') {
                        sb.append('b')
                        B--
                    } else if (last1 == 'b' && last2 == 'b') {
                        sb.append('a')
                        A--
                    } else {
                        // arbitrary choice when no restriction
                        sb.append('a')
                        A--
                    }
                }
            }
        }
        return sb.toString()
    }
}
```

## Golang

```go
package main

import "strings"

func strWithout3a3b(a int, b int) string {
	var sb strings.Builder
	for a > 0 || b > 0 {
		if a > b {
			// place up to two 'a's
			if a >= 2 {
				sb.WriteString("aa")
				a -= 2
			} else {
				sb.WriteByte('a')
				a--
			}
			// then one 'b' if any left
			if b > 0 {
				sb.WriteByte('b')
				b--
			}
		} else if b > a {
			// place up to two 'b's
			if b >= 2 {
				sb.WriteString("bb")
				b -= 2
			} else {
				sb.WriteByte('b')
				b--
			}
			// then one 'a' if any left
			if a > 0 {
				sb.WriteByte('a')
				a--
			}
		} else { // a == b
			if a > 0 && b > 0 {
				sb.WriteString("ab")
				a--
				b--
			}
		}
	}
	return sb.String()
}
```

## Ruby

```ruby
def str_without3a3b(a, b)
  result = ''
  while a > 0 || b > 0
    if a > b
      if result[-2..-1] == 'aa'
        result << 'b'
        b -= 1
      else
        result << 'a'
        a -= 1
      end
    else
      if result[-2..-1] == 'bb'
        result << 'a'
        a -= 1
      else
        result << 'b'
        b -= 1
      end
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def strWithout3a3b(a: Int, b: Int): String = {
        val sb = new StringBuilder
        var A = a
        var B = b
        var consecA = 0
        var consecB = 0
        while (A > 0 || B > 0) {
            if ((A > B && consecA < 2) || consecB == 2) {
                sb.append('a')
                A -= 1
                consecA += 1
                consecB = 0
            } else {
                sb.append('b')
                B -= 1
                consecB += 1
                consecA = 0
            }
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn str_without3a3b(a: i32, b: i32) -> String {
        let mut a = a;
        let mut b = b;
        let mut res = String::new();
        while a > 0 || b > 0 {
            let n = res.len();
            if n >= 2 {
                let bytes = res.as_bytes();
                if bytes[n - 2] == b'a' && bytes[n - 1] == b'a' {
                    // last two are 'a', must place 'b'
                    if b > 0 {
                        res.push('b');
                        b -= 1;
                    } else {
                        // fallback (should not happen per problem guarantee)
                        res.push('a');
                        a -= 1;
                    }
                    continue;
                }
                if bytes[n - 2] == b'b' && bytes[n - 1] == b'b' {
                    // last two are 'b', must place 'a'
                    if a > 0 {
                        res.push('a');
                        a -= 1;
                    } else {
                        // fallback (should not happen per problem guarantee)
                        res.push('b');
                        b -= 1;
                    }
                    continue;
                }
            }
            // otherwise, place the character with larger remaining count
            if a >= b && a > 0 {
                res.push('a');
                a -= 1;
            } else if b > 0 {
                res.push('b');
                b -= 1;
            }
        }
        res
    }
}
```
