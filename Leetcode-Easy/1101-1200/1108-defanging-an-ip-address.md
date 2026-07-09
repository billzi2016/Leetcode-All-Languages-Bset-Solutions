# 1108. Defanging an IP Address

## Cpp

```cpp
class Solution {
public:
    string defangIPaddr(string address) {
        string res;
        res.reserve(address.size() * 3); // worst case size
        for (char c : address) {
            if (c == '.') {
                res += "[.]";
            } else {
                res += c;
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String defangIPaddr(String address) {
        StringBuilder sb = new StringBuilder(address.length() * 3);
        for (char c : address.toCharArray()) {
            if (c == '.') {
                sb.append("[.]");
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace('.', '[.]')
```

## Python3

```python
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
```

## C

```c
#include <stdlib.h>
#include <string.h>

char *defangIPaddr(char *address) {
    int len = 0, dotCount = 0;
    while (address[len]) {
        if (address[len] == '.') dotCount++;
        len++;
    }
    int newLen = len + dotCount * 2; // each '.' becomes "[.]" (+2 chars)
    char *res = (char *)malloc(newLen + 1);
    int i = 0, j = 0;
    for (; i < len; ++i) {
        if (address[i] == '.') {
            res[j++] = '[';
            res[j++] = '.';
            res[j++] = ']';
        } else {
            res[j++] = address[i];
        }
    }
    res[newLen] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public string DefangIPaddr(string address) {
        return address.Replace(".", "[.]");
    }
}
```

## Javascript

```javascript
/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function(address) {
    return address.split('.').join('[.]');
};
```

## Typescript

```typescript
function defangIPaddr(address: string): string {
    return address.split('.').join('[.]');
}
```

## Php

```php
class Solution {

    /**
     * @param String $address
     * @return String
     */
    function defangIPaddr($address) {
        return str_replace(".", "[.]", $address);
    }
}
```

## Swift

```swift
class Solution {
    func defangIPaddr(_ address: String) -> String {
        return address.replacingOccurrences(of: ".", with: "[.]")
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun defangIPaddr(address: String): String {
        return address.replace(".", "[.]")
    }
}
```

## Golang

```go
package main

import "strings"

func defangIPaddr(address string) string {
	return strings.ReplaceAll(address, ".", "[.]")
}
```

## Ruby

```ruby
def defang_i_paddr(address)
  address.gsub(".", "[.]")
end
```

## Scala

```scala
object Solution {
    def defangIPaddr(address: String): String = {
        address.replace(".", "[.]")
    }
}
```

## Rust

```rust
impl Solution {
    pub fn defang_i_paddr(address: String) -> String {
        address.replace(".", "[.]")
    }
}
```
