# 2806. Account Balance After Rounded Purchase

## Cpp

```cpp
class Solution {
public:
    int accountBalanceAfterPurchase(int purchaseAmount) {
        int rounded = ((purchaseAmount + 5) / 10) * 10;
        return 100 - rounded;
    }
};
```

## Java

```java
class Solution {
    public int accountBalanceAfterPurchase(int purchaseAmount) {
        int rounded = ((purchaseAmount + 5) / 10) * 10;
        return 100 - rounded;
    }
}
```

## Python

```python
class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        rounded = ((purchaseAmount + 5) // 10) * 10
        return 100 - rounded
```

## Python3

```python
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rounded = ((purchaseAmount + 5) // 10) * 10
        return 100 - rounded
```

## C

```c
int accountBalanceAfterPurchase(int purchaseAmount) {
    int rounded = ((purchaseAmount + 5) / 10) * 10;
    return 100 - rounded;
}
```

## Csharp

```csharp
public class Solution {
    public int AccountBalanceAfterPurchase(int purchaseAmount) {
        int rounded = ((purchaseAmount + 5) / 10) * 10;
        return 100 - rounded;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} purchaseAmount
 * @return {number}
 */
var accountBalanceAfterPurchase = function(purchaseAmount) {
    const rounded = Math.floor((purchaseAmount + 5) / 10) * 10;
    return 100 - rounded;
};
```

## Typescript

```typescript
function accountBalanceAfterPurchase(purchaseAmount: number): number {
    const rounded = Math.round(purchaseAmount / 10) * 10;
    return 100 - rounded;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $purchaseAmount
     * @return Integer
     */
    function accountBalanceAfterPurchase($purchaseAmount) {
        $rounded = intdiv($purchaseAmount + 5, 10) * 10;
        return 100 - $rounded;
    }
}
```

## Swift

```swift
class Solution {
    func accountBalanceAfterPurchase(_ purchaseAmount: Int) -> Int {
        let rounded = ((purchaseAmount + 5) / 10) * 10
        return 100 - rounded
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun accountBalanceAfterPurchase(purchaseAmount: Int): Int {
        val rounded = ((purchaseAmount + 5) / 10) * 10
        return 100 - rounded
    }
}
```

## Dart

```dart
class Solution {
  int accountBalanceAfterPurchase(int purchaseAmount) {
    int rounded = ((purchaseAmount + 5) ~/ 10) * 10;
    return 100 - rounded;
  }
}
```

## Golang

```go
func accountBalanceAfterPurchase(purchaseAmount int) int {
	rounded := ((purchaseAmount + 5) / 10) * 10
	return 100 - rounded
}
```

## Ruby

```ruby
def account_balance_after_purchase(purchase_amount)
  rounded = ((purchase_amount + 5) / 10) * 10
  100 - rounded
end
```

## Scala

```scala
object Solution {
    def accountBalanceAfterPurchase(purchaseAmount: Int): Int = {
        val rounded = ((purchaseAmount + 5) / 10) * 10
        100 - rounded
    }
}
```

## Rust

```rust
impl Solution {
    pub fn account_balance_after_purchase(purchase_amount: i32) -> i32 {
        let rounded = ((purchase_amount + 5) / 10) * 10;
        100 - rounded
    }
}
```

## Racket

```racket
(define/contract (account-balance-after-purchase purchaseAmount)
  (-> exact-integer? exact-integer?)
  (let* ([rounded (* (quotient (+ purchaseAmount 5) 10) 10)])
    (- 100 rounded)))
```

## Erlang

```erlang
-spec account_balance_after_purchase(PurchaseAmount :: integer()) -> integer().
account_balance_after_purchase(PurchaseAmount) ->
    Rounded = ((PurchaseAmount + 5) div 10) * 10,
    100 - Rounded.
```

## Elixir

```elixir
defmodule Solution do
  @spec account_balance_after_purchase(purchase_amount :: integer) :: integer
  def account_balance_after_purchase(purchase_amount) do
    rounded = div(purchase_amount + 5, 10) * 10
    100 - rounded
  end
end
```
