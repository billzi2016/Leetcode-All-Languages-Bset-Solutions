# 0470. Implement Rand10() Using Rand7()

## Cpp

```cpp
// The rand7() API is already defined for you.
// int rand7();
// @return a random integer in the range 1 to 7

class Solution {
public:
    int rand10() {
        while (true) {
            int a = rand7();
            int b = rand7();
            int num = (a - 1) * 7 + b; // generates 1..49 uniformly
            if (num <= 40) {
                return (num - 1) % 10 + 1;
            }
        }
    }
};
```

## Java

```java
/**
 * The rand7() API is already defined in the parent class SolBase.
 * public int rand7();
 * @return a random integer in the range 1 to 7
 */
class Solution extends SolBase {
    public int rand10() {
        while (true) {
            int row = rand7();          // 1..7
            int col = rand7();          // 1..7
            int idx = (row - 1) * 7 + col; // 1..49
            if (idx <= 40) {
                return (idx - 1) % 10 + 1;
            }
        }
    }
}
```

## Python

```python
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            # Generate a uniform integer in [1, 49]
            num = (rand7() - 1) * 7 + rand7()
            if num <= 40:
                return (num - 1) % 10 + 1
```

## Python3

```python
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            # Generate a uniform integer in [1, 49]
            num = (rand7() - 1) * 7 + rand7()
            if num <= 40:
                return (num - 1) % 10 + 1
```

## C

```c
// The rand7() API is already defined for you.
// int rand7();
// @return a random integer in the range 1 to 7

int rand10() {
    while (1) {
        int a = rand7();
        int b = rand7();
        int num = (a - 1) * 7 + b; // generates uniform [1,49]
        if (num <= 40) {
            return (num - 1) % 10 + 1;
        }
    }
}
```

## Csharp

```csharp
/**
 * The Rand7() API is already defined in the parent class SolBase.
 * public int Rand7();
 * @return a random integer in the range 1 to 7
 */
public class Solution : SolBase {
    public int Rand10() {
        while (true) {
            int row = Rand7();          // 1..7
            int col = Rand7();          // 1..7
            int idx = (row - 1) * 7 + col; // 1..49
            if (idx <= 40) {
                return (idx - 1) % 10 + 1;
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * The rand7() API is already defined for you.
 * var rand7 = function() {}
 * @return {number} a random integer in the range 1 to 10
 */
var rand10 = function() {
    while (true) {
        const row = rand7();          // 1..7
        const col = rand7();          // 1..7
        const idx = (row - 1) * 7 + col; // 1..49
        if (idx <= 40) {
            return ((idx - 1) % 10) + 1;
        }
    }
};
```

## Typescript

```typescript
/**
 * The rand7() API is already defined for you.
 * function rand7(): number {}
 * @return a random integer in the range 1 to 7
 */
function rand10(): number {
    while (true) {
        const a = rand7();
        const b = rand7();
        const num = (a - 1) * 7 + b; // generates 1..49 uniformly
        if (num <= 40) {
            return ((num - 1) % 10) + 1;
        }
    }
}
```

## Php

```php
/*
 * The rand7() API is already defined for you.
 * @return a random integer in the range 1 to 7
 * function rand7();
*/

class Solution {
    /**
     * @return int
     */
    function rand10() {
        while (true) {
            $row = rand7();               // 1..7
            $col = rand7();               // 1..7
            $idx = ($row - 1) * 7 + $col; // 1..49
            if ($idx <= 40) {
                return ($idx - 1) % 10 + 1;
            }
        }
    }
}
```

## Swift

```swift
/**
 * The rand7() API is already defined in the parent class SolBase.
 * func rand7() -> Int = {}
 * @return a random integer in the range 1 to 7
 */
class Solution : SolBase {
    func rand10() -> Int {
        while true {
            let row = rand7()
            let col = rand7()
            let idx = (row - 1) * 7 + col   // generates 1..49 uniformly
            if idx <= 40 {
                return ((idx - 1) % 10) + 1
            }
        }
    }
}
```

## Kotlin

```kotlin
/**
 * The rand7() API is already defined in the parent class SolBase.
 * fun rand7(): Int {}
 * @return a random integer in the range 1 to 7
 */
class Solution : SolBase() {
    fun rand10(): Int {
        while (true) {
            val row = rand7()
            val col = rand7()
            val idx = (row - 1) * 7 + col // generates 1..49 uniformly
            if (idx <= 40) {
                return ((idx - 1) % 10) + 1
            }
        }
    }
}
```

## Golang

```go
func rand10() int {
	for {
		row := rand7()
		col := rand7()
		num := (row-1)*7 + col // 1..49
		if num <= 40 {
			return (num-1)%10 + 1
		}
	}
}
```

## Ruby

```ruby
# The rand7() API is already defined for you.
# def rand7()
# @return {Integer} a random integer in the range 1 to 7

def rand10()
  loop do
    num = (rand7 - 1) * 7 + rand7
    return ((num - 1) % 10) + 1 if num <= 40
  end
end
```

## Scala

```scala
object Solution extends SolBase {
    def rand10(): Int = {
        while (true) {
            val a = rand7()
            val b = rand7()
            val num = (a - 1) * 7 + b // generates 1..49 uniformly
            if (num <= 40) {
                return ((num - 1) % 10) + 1
            }
        }
        0 // unreachable
    }
}
```

## Rust

```rust
/** 
 * The rand7() API is already defined for you.
 * @return a random integer in the range 1 to 7
 * fn rand7() -> i32;
 */

impl Solution {
    pub fn rand10() -> i32 {
        loop {
            let row = rand7();
            let col = rand7();
            // Generate a uniform integer in [1, 49]
            let idx = (row - 1) * 7 + col;
            if idx <= 40 {
                // Map to [1,10]
                return ((idx - 1) % 10) + 1;
            }
        }
    }
}
```
