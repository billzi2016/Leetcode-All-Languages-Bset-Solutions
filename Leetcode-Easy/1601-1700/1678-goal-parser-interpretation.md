# 1678. Goal Parser Interpretation

## Cpp

```cpp
class Solution {
public:
    string interpret(string command) {
        string res;
        for (int i = 0; i < (int)command.size(); ) {
            if (command[i] == 'G') {
                res.push_back('G');
                ++i;
            } else { // '('
                if (i + 1 < (int)command.size() && command[i+1] == ')') {
                    res.push_back('o');
                    i += 2; // skip "()"
                } else {
                    // must be "(al)"
                    res.append("al");
                    i += 4; // skip "(al)"
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
    public String interpret(String command) {
        StringBuilder sb = new StringBuilder();
        int i = 0;
        while (i < command.length()) {
            char c = command.charAt(i);
            if (c == 'G') {
                sb.append('G');
                i++;
            } else { // '('
                if (i + 1 < command.length() && command.charAt(i + 1) == ')') {
                    sb.append('o');
                    i += 2;
                } else {
                    sb.append("al");
                    i += 4; // skip "(al)"
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
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        res = []
        i = 0
        n = len(command)
        while i < n:
            if command[i] == 'G':
                res.append('G')
                i += 1
            elif command[i] == '(':
                # look ahead to determine pattern
                if i + 1 < n and command[i+1] == ')':
                    res.append('o')
                    i += 2
                else:
                    # must be "(al)"
                    res.append('al')
                    i += 4
            else:
                # should not happen with valid input
                i += 1
        return ''.join(res)
```

## Python3

```python
class Solution:
    def interpret(self, command: str) -> str:
        res = []
        i = 0
        n = len(command)
        while i < n:
            if command[i] == 'G':
                res.append('G')
                i += 1
            else:  # '('
                if i + 1 < n and command[i + 1] == ')':
                    res.append('o')
                    i += 2
                else:
                    res.append('al')
                    i += 4
        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char *interpret(char *command) {
    int n = strlen(command);
    char *res = (char *)malloc(n + 1);
    int i = 0, j = 0;
    while (i < n) {
        if (command[i] == 'G') {
            res[j++] = 'G';
            i++;
        } else if (command[i] == '(') {
            if (i + 1 < n && command[i + 1] == ')') {
                res[j++] = 'o';
                i += 2;
            } else {
                // "(al)"
                res[j++] = 'a';
                res[j++] = 'l';
                i += 4; // skip "(al)"
            }
        } else {
            i++; // safety, though input guarantees valid tokens
        }
    }
    res[j] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string Interpret(string command)
    {
        var sb = new System.Text.StringBuilder();
        int i = 0;
        while (i < command.Length)
        {
            if (command[i] == 'G')
            {
                sb.Append('G');
                i++;
            }
            else // '('
            {
                if (i + 1 < command.Length && command[i + 1] == ')')
                {
                    sb.Append('o');
                    i += 2;
                }
                else
                {
                    sb.Append("al");
                    i += 4; // skip "(al)"
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
 * @param {string} command
 * @return {string}
 */
var interpret = function(command) {
    let res = [];
    for (let i = 0; i < command.length;) {
        if (command[i] === 'G') {
            res.push('G');
            i++;
        } else if (command[i] === '(') {
            if (command[i + 1] === ')') {
                res.push('o');
                i += 2;
            } else {
                // must be "(al)"
                res.push('al');
                i += 4; // skip "(al)"
            }
        }
    }
    return res.join('');
};
```

## Typescript

```typescript
function interpret(command: string): string {
    let result = '';
    for (let i = 0; i < command.length;) {
        const ch = command[i];
        if (ch === 'G') {
            result += 'G';
            i++;
        } else { // '('
            if (command[i + 1] === ')') {
                result += 'o';
                i += 2;
            } else {
                // "(al)"
                result += 'al';
                i += 4;
            }
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $command
     * @return String
     */
    function interpret($command) {
        $n = strlen($command);
        $i = 0;
        $result = '';
        while ($i < $n) {
            if ($command[$i] === 'G') {
                $result .= 'G';
                $i++;
            } elseif ($i + 1 < $n && $command[$i] === '(' && $command[$i + 1] === ')') {
                $result .= 'o';
                $i += 2;
            } else { // must be "(al)"
                $result .= 'al';
                $i += 4; // skip "(al)"
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func interpret(_ command: String) -> String {
        let chars = Array(command)
        var i = 0
        var result = ""
        while i < chars.count {
            if chars[i] == "G" {
                result.append("G")
                i += 1
            } else if i + 1 < chars.count && chars[i] == "(" && chars[i + 1] == ")" {
                result.append("o")
                i += 2
            } else {
                // "(al)"
                result.append("al")
                i += 4
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun interpret(command: String): String {
        val sb = StringBuilder()
        var i = 0
        while (i < command.length) {
            when (command[i]) {
                'G' -> {
                    sb.append('G')
                    i++
                }
                '(' -> {
                    if (i + 1 < command.length && command[i + 1] == ')') {
                        sb.append('o')
                        i += 2
                    } else {
                        // must be "(al)"
                        sb.append("al")
                        i += 4
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
func interpret(command string) string {
	n := len(command)
	res := make([]byte, 0, n)
	for i := 0; i < n; {
		if command[i] == 'G' {
			res = append(res, 'G')
			i++
		} else { // '('
			if i+1 < n && command[i+1] == ')' {
				res = append(res, 'o')
				i += 2
			} else {
				// "(al)"
				res = append(res, 'a', 'l')
				i += 4
			}
		}
	}
	return string(res)
}
```

## Ruby

```ruby
def interpret(command)
  result = +''
  i = 0
  n = command.length
  while i < n
    case command.getbyte(i)
    when 71 # 'G'
      result << 'G'
      i += 1
    when 40 # '('
      if command.getbyte(i + 1) == 41 # ')'
        result << 'o'
        i += 2
      else
        result << 'al'
        i += 4
      end
    else
      i += 1
    end
  end
  result
end
```

## Scala

```scala
object Solution {
    def interpret(command: String): String = {
        val sb = new StringBuilder
        var i = 0
        while (i < command.length) {
            command.charAt(i) match {
                case 'G' =>
                    sb.append('G')
                    i += 1
                case '(' =>
                    if (i + 1 < command.length && command.charAt(i + 1) == ')') {
                        sb.append('o')
                        i += 2
                    } else {
                        // must be "(al)"
                        sb.append("al")
                        i += 4
                    }
                case _ =>
                    i += 1
            }
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn interpret(command: String) -> String {
        let bytes = command.as_bytes();
        let mut result = String::new();
        let mut i = 0;
        while i < bytes.len() {
            match bytes[i] as char {
                'G' => {
                    result.push('G');
                    i += 1;
                }
                '(' => {
                    if i + 1 < bytes.len() && bytes[i + 1] == b')' {
                        result.push('o');
                        i += 2;
                    } else {
                        // "(al)"
                        result.push_str("al");
                        i += 4; // skip '(', 'a', 'l', ')'
                    }
                }
                _ => {
                    i += 1; // safety, though not expected
                }
            }
        }
        result
    }
}
```
