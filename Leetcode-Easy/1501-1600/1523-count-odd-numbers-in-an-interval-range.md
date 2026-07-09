# 1523. Count Odd Numbers in an Interval Range

## Cpp

```cpp
class Solution {
public:
    int countOdds(int low, int high) {
        // Number of odd numbers <= x is (x + 1) / 2
        return ((high + 1) / 2) - (low / 2);
    }
};
```

## Java

```java
class Solution {
    public int countOdds(int low, int high) {
        return ((high + 1) >> 1) - (low >> 1);
    }
}
```

## Python

```python
class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        return (high + 1) // 2 - low // 2
```

## Python3

```python
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2
```

## C

```c
int countOdds(int low, int high){
    return ((high + 1) >> 1) - (low >> 1);
}
```

## Csharp

```csharp
public class Solution {
    public int CountOdds(int low, int high) {
        return ((high + 1) / 2) - (low / 2);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countOdds = function(low, high) {
    return Math.floor((high + 1) / 2) - Math.floor(low / 2);
};
```

## Typescript

```typescript
function countOdds(low: number, high: number): number {
    const oddsUpTo = (n: number) => Math.floor((n + 1) / 2);
    return oddsUpTo(high) - oddsUpTo(low - 1);
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $low
     * @param Integer $high
     * @return Integer
     */
    function countOdds($low, $high) {
        $oddUpToHigh = intdiv($high + 1, 2);
        $oddBelowLow = intdiv($low, 2);
        return $oddUpToHigh - $oddBelowLow;
    }
}
```

## Swift

```swift
class Solution {
    func countOdds(_ low: Int, _ high: Int) -> Int {
        return (high + 1) / 2 - low / 2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countOdds(low: Int, high: Int): Int {
        return ((high + 1) / 2) - (low / 2)
    }
}
```

## Golang

```go
func countOdds(low int, high int) int {
    return ((high + 1) / 2) - (low / 2)
}
```

## Ruby

```ruby
def count_odds(low, high)
  ((high + 1) / 2) - (low / 2)
end
```

## Scala

```scala
object Solution {
    def countOdds(low: Int, high: Int): Int = {
        ((high + 1) / 2) - (low / 2)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_odds(low: i32, high: i32) -> i32 {
        ((high + 1) / 2) - (low / 2)
    }
}
```
