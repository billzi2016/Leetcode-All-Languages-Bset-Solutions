# 0443. String Compression

## Cpp

```cpp
class Solution {
public:
    int compress(std::vector<char>& chars) {
        int n = chars.size();
        int write = 0;
        for (int i = 0; i < n; ) {
            char cur = chars[i];
            int j = i;
            while (j < n && chars[j] == cur) ++j;
            int cnt = j - i;
            chars[write++] = cur;
            if (cnt > 1) {
                std::string s = std::to_string(cnt);
                for (char ch : s) {
                    chars[write++] = ch;
                }
            }
            i = j;
        }
        return write;
    }
};
```

## Java

```java
class Solution {
    public int compress(char[] chars) {
        int n = chars.length;
        int write = 0;
        int i = 0;
        while (i < n) {
            char c = chars[i];
            int count = 0;
            while (i < n && chars[i] == c) {
                i++;
                count++;
            }
            chars[write++] = c;
            if (count > 1) {
                String cntStr = Integer.toString(count);
                for (int k = 0; k < cntStr.length(); k++) {
                    chars[write++] = cntStr.charAt(k);
                }
            }
        }
        return write;
    }
}
```

## Python

```python
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        write = 0
        i = 0
        while i < n:
            j = i
            while j < n and chars[j] == chars[i]:
                j += 1
            count = j - i
            chars[write] = chars[i]
            write += 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
            i = j
        return write
```

## Python3

```python
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        write = 0
        i = 0
        while i < n:
            j = i
            while j < n and chars[j] == chars[i]:
                j += 1
            count = j - i
            chars[write] = chars[i]
            write += 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
            i = j
        return write
```

## C

```c
int compress(char* chars, int charsSize) {
    int i = 0, write = 0;
    while (i < charsSize) {
        char c = chars[i];
        int j = i;
        while (j < charsSize && chars[j] == c) {
            ++j;
        }
        int cnt = j - i;
        chars[write++] = c;
        if (cnt > 1) {
            char buf[12];
            int idx = 0;
            while (cnt > 0) {
                buf[idx++] = (char)('0' + (cnt % 10));
                cnt /= 10;
            }
            for (int k = idx - 1; k >= 0; --k) {
                chars[write++] = buf[k];
            }
        }
        i = j;
    }
    return write;
}
```

## Csharp

```csharp
public class Solution
{
    public int Compress(char[] chars)
    {
        int n = chars.Length;
        int write = 0;
        int i = 0;

        while (i < n)
        {
            char current = chars[i];
            int count = 0;
            while (i + count < n && chars[i + count] == current)
                count++;

            // write the character
            chars[write++] = current;

            // write the count if greater than 1
            if (count > 1)
            {
                foreach (char digit in count.ToString())
                    chars[write++] = digit;
            }

            i += count;
        }

        return write;
    }
}
```

## Javascript

```javascript
/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function(chars) {
    let n = chars.length;
    let write = 0; // position to write compressed characters
    let i = 0;
    
    while (i < n) {
        const currentChar = chars[i];
        let j = i;
        while (j < n && chars[j] === currentChar) {
            j++;
        }
        const count = j - i;
        
        // write the character
        chars[write++] = currentChar;
        
        // write the count if greater than 1
        if (count > 1) {
            const cntStr = String(count);
            for (let k = 0; k < cntStr.length; k++) {
                chars[write++] = cntStr[k];
            }
        }
        
        i = j;
    }
    
    return write;
};
```

## Typescript

```typescript
function compress(chars: string[]): number {
    let write = 0;
    let i = 0;
    const n = chars.length;
    while (i < n) {
        let j = i;
        while (j < n && chars[j] === chars[i]) {
            j++;
        }
        const count = j - i;
        chars[write++] = chars[i];
        if (count > 1) {
            const cntStr = count.toString();
            for (let k = 0; k < cntStr.length; k++) {
                chars[write++] = cntStr[k];
            }
        }
        i = j;
    }
    return write;
}
```

## Php

```php
class Solution {
    /**
     * @param String[] $chars
     * @return Integer
     */
    function compress(&$chars) {
        $n = count($chars);
        $write = 0;
        $i = 0;
        while ($i < $n) {
            $j = $i;
            while ($j < $n && $chars[$j] === $chars[$i]) {
                $j++;
            }
            $count = $j - $i;
            // write the character
            $chars[$write++] = $chars[$i];
            if ($count > 1) {
                foreach (str_split((string)$count) as $c) {
                    $chars[$write++] = $c;
                }
            }
            $i = $j;
        }
        // Trim the array to the new length (optional, not required by LeetCode)
        // for ($k = $write; $k < $n; $k++) {
        //     unset($chars[$k]);
        // }
        return $write;
    }
}
```

## Swift

```swift
class Solution {
    func compress(_ chars: inout [Character]) -> Int {
        var i = 0
        var write = 0
        let n = chars.count
        while i < n {
            let currentChar = chars[i]
            var j = i
            while j < n && chars[j] == currentChar {
                j += 1
            }
            let count = j - i
            chars[write] = currentChar
            write += 1
            if count > 1 {
                for digit in String(count) {
                    chars[write] = digit
                    write += 1
                }
            }
            i = j
        }
        return write
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun compress(chars: CharArray): Int {
        var i = 0
        var write = 0
        val n = chars.size
        while (i < n) {
            val ch = chars[i]
            var count = 0
            while (i + count < n && chars[i + count] == ch) {
                count++
            }
            chars[write++] = ch
            if (count > 1) {
                for (c in count.toString()) {
                    chars[write++] = c
                }
            }
            i += count
        }
        return write
    }
}
```

## Dart

```dart
class Solution {
  int compress(List<String> chars) {
    int i = 0, res = 0;
    while (i < chars.length) {
      int j = i;
      while (j < chars.length && chars[j] == chars[i]) {
        j++;
      }
      int count = j - i;
      chars[res++] = chars[i];
      if (count > 1) {
        for (var ch in count.toString().split('')) {
          chars[res++] = ch;
        }
      }
      i = j;
    }
    return res;
  }
}
```

## Golang

```go
import "strconv"

func compress(chars []byte) int {
	n := len(chars)
	write, i := 0, 0
	for i < n {
		j := i
		for j < n && chars[j] == chars[i] {
			j++
		}
		count := j - i
		chars[write] = chars[i]
		write++
		if count > 1 {
			s := strconv.Itoa(count)
			for k := 0; k < len(s); k++ {
				chars[write] = s[k]
				write++
			}
		}
		i = j
	}
	return write
}
```

## Ruby

```ruby
def compress(chars)
  n = chars.length
  i = 0
  write = 0
  while i < n
    j = i
    j += 1 while j < n && chars[j] == chars[i]
    count = j - i
    chars[write] = chars[i]
    write += 1
    if count > 1
      count.to_s.each_char do |ch|
        chars[write] = ch
        write += 1
      end
    end
    i = j
  end
  write
end
```

## Scala

```scala
object Solution {
    def compress(chars: Array[Char]): Int = {
        var read = 0
        var write = 0
        val n = chars.length
        while (read < n) {
            val current = chars(read)
            var count = 0
            while (read < n && chars(read) == current) {
                read += 1
                count += 1
            }
            chars(write) = current
            write += 1
            if (count > 1) {
                val cntStr = count.toString
                var k = 0
                while (k < cntStr.length) {
                    chars(write) = cntStr.charAt(k)
                    write += 1
                    k += 1
                }
            }
        }
        write
    }
}
```

## Rust

```rust
impl Solution {
    pub fn compress(chars: &mut Vec<char>) -> i32 {
        let n = chars.len();
        let mut read = 0usize;
        let mut write = 0usize;

        while read < n {
            let current = chars[read];
            let mut count = 0usize;
            while read + count < n && chars[read + count] == current {
                count += 1;
            }

            // write the character
            chars[write] = current;
            write += 1;

            if count > 1 {
                for c in count.to_string().chars() {
                    chars[write] = c;
                    write += 1;
                }
            }

            read += count;
        }

        write as i32
    }
}
```
