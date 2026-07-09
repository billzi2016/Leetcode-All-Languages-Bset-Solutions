# 2591. Distribute Money to Maximum Children

## Cpp

```cpp
class Solution {
public:
    int distMoney(int money, int children) {
        if (money < children) return -1;
        int maxEight = min(children, money / 8);
        for (int k = maxEight; k >= 0; --k) {
            int remMoney = money - k * 8;
            int remChildren = children - k;
            if (remMoney < remChildren) continue; // not enough for at least $1 each
            if (remChildren == 1 && remMoney == 4) continue; // the only child would get exactly $4, which is invalid
            return k;
        }
        return -1;
    }
};
```

## Java

```java
class Solution {
    public int distMoney(int money, int children) {
        // Minimum $1 per child required
        if (money < children) return -1;
        int maxEight = Math.min(money / 8, children);
        for (int k = maxEight; k >= 0; k--) {
            int remMoney = money - k * 8;
            int remChildren = children - k;
            if (remChildren == 0) {
                if (remMoney == 0) return k;
                continue;
            }
            // each remaining child needs at least $1
            if (remMoney < remChildren) continue;
            // cannot give exactly $4 to a single remaining child
            if (remChildren == 1 && remMoney == 4) continue;
            // otherwise feasible
            return k;
        }
        return -1;
    }
}
```

## Python

```python
class Solution(object):
    def distMoney(self, money, children):
        """
        :type money: int
        :type children: int
        :rtype: int
        """
        if money < children:
            return -1
        # give each child $1 first
        money -= children
        max_k = min(children, money // 7)  # each child with $8 uses extra $7
        rem = money - max_k * 7
        # avoid a child receiving exactly $4
        if rem == 3 and max_k > 0:
            max_k -= 1
        return max_k
```

## Python3

```python
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        max_k = min(children, money // 8)
        while max_k >= 0:
            rem_money = money - max_k * 8
            rem_children = children - max_k

            if rem_children == 0:
                if rem_money == 0:
                    return max_k
            else:
                # each remaining child needs at least $1
                if rem_money < rem_children:
                    pass
                elif rem_money == rem_children * 4:
                    # would force every remaining child to get exactly $4, which is not allowed
                    pass
                else:
                    return max_k
            max_k -= 1
        return -1
```

## C

```c
int distMoney(int money, int children) {
    if (money < children) return -1;
    int maxEight = money / 8;
    if (maxEight > children) maxEight = children;
    for (int k = maxEight; k >= 0; --k) {
        int remMoney = money - k * 8;
        int remChildren = children - k;
        if (remChildren == 0) return k;
        if (remMoney < remChildren) continue;
        if (remMoney == 4 && remChildren == 1) continue;
        return k;
    }
    return -1;
}
```

## Csharp

```csharp
public class Solution {
    public int DistMoney(int money, int children) {
        if (money < children) return -1;
        int maxK = Math.Min(children, money / 8);
        for (int k = maxK; k >= 0; --k) {
            int remMoney = money - 8 * k;
            int remChildren = children - k;
            if (remChildren == 0) {
                if (remMoney == 0) return k;
                continue;
            }
            if (remMoney < remChildren) continue;
            if (remMoney == 4 && remChildren == 1) continue;
            return k;
        }
        return -1;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} money
 * @param {number} children
 * @return {number}
 */
var distMoney = function(money, children) {
    // each child must receive at least $1
    if (money < children) return -1;
    
    // give each child $1 first, then each child that gets $8 needs 7 extra dollars
    let maxEight = Math.min(children, Math.floor((money - children) / 7));
    
    // remaining money and children after allocating those with $8
    let remainingMoney = money - maxEight * 8;
    let remainingChildren = children - maxEight;
    
    // if the leftover would force a child to receive exactly $4, adjust
    if (remainingChildren > 0 && remainingMoney === 4) {
        maxEight--;
    }
    
    return maxEight;
};
```

## Typescript

```typescript
function distMoney(money: number, children: number): number {
    if (money < children) return -1;
    const maxK = Math.min(children, Math.floor(money / 8));
    for (let k = maxK; k >= 0; --k) {
        const remMoney = money - 8 * k;
        const remKids = children - k;
        if (remKids === 0) {
            if (remMoney === 0) return k;
            continue;
        }
        if (remMoney < remKids) continue;
        if (remMoney === 4 * remKids) continue; // would force all to get exactly 4
        return k;
    }
    return -1;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $money
     * @param Integer $children
     * @return Integer
     */
    function distMoney($money, $children) {
        if ($money < $children) {
            return -1;
        }
        $maxEight = min($children, intdiv($money, 8));
        $ans = $maxEight;
        $remaining = $money - 8 * $ans;
        $leftChildren = $children - $ans;
        if ($ans > 0 && $remaining == 4 && $leftChildren > 0) {
            $ans--;
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func distMoney(_ money: Int, _ children: Int) -> Int {
        if money < children { return -1 }
        var maxEight = min(money / 8, children)
        while maxEight >= 0 {
            let remainingMoney = money - maxEight * 8
            let remainingChildren = children - maxEight
            if remainingMoney >= remainingChildren && !(remainingChildren == 1 && remainingMoney == 4) {
                return maxEight
            }
            maxEight -= 1
        }
        return -1
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun distMoney(money: Int, children: Int): Int {
        if (money < children) return -1
        var extra = money - children
        var maxEight = minOf(children, extra / 7)
        while (maxEight > 0) {
            val leftover = extra - maxEight * 7
            if (leftover == 3 && children - maxEight > 0) {
                maxEight--
            } else break
        }
        return maxEight
    }
}
```

## Dart

```dart
class Solution {
  int distMoney(int money, int children) {
    if (money < children) return -1;
    int maxKids = money ~/ 8;
    if (maxKids > children) maxKids = children;
    for (int k = maxKids; k >= 0; --k) {
      int remMoney = money - 8 * k;
      int remChildren = children - k;
      if (remChildren == 0) {
        if (remMoney == 0) return k;
        continue;
      }
      if (remMoney < remChildren) continue;
      if (remMoney == 4 && remChildren == 1) continue;
      return k;
    }
    return -1;
  }
}
```

## Golang

```go
func distMoney(money int, children int) int {
	if money < children {
		return -1
	}
	remaining := money - children
	maxKids := remaining / 7
	if maxKids > children {
		maxKids = children
	}
	remaining -= maxKids * 7
	if remaining == 3 && maxKids > 0 {
		maxKids--
	}
	return maxKids
}
```

## Ruby

```ruby
def dist_money(money, children)
  return -1 if money < children
  children.downto(0) do |k|
    r = children - k
    min_needed = 8 * k + r
    next if money < min_needed
    leftover = money - min_needed
    if r == 0
      return k if leftover == 0
    elsif r == 1 && leftover == 3
      next
    else
      return k
    end
  end
  -1
end
```

## Scala

```scala
object Solution {
    def distMoney(money: Int, children: Int): Int = {
        if (money < children) return -1
        var k = Math.min(children, money / 8)
        while (k >= 0) {
            val remMoney = money - 8 * k
            val remChildren = children - k
            if (remChildren == 0) {
                if (remMoney == 0) return k
            } else {
                if (remMoney >= remChildren && !(remChildren == 1 && remMoney == 4)) {
                    return k
                }
            }
            k -= 1
        }
        -1
    }
}
```

## Rust

```rust
impl Solution {
    pub fn dist_money(money: i32, children: i32) -> i32 {
        if money < children {
            return -1;
        }
        let mut max_k = std::cmp::min(children, (money - children) / 7);
        while max_k >= 0 {
            let remaining_money = money - 8 * max_k;
            let rem_children = children - max_k;
            if !(rem_children == 1 && remaining_money == 4) {
                return max_k;
            }
            max_k -= 1;
        }
        -1
    }
}
```

## Racket

```racket
(define/contract (dist-money money children)
  (-> exact-integer? exact-integer? exact-integer?)
  (if (< money children)
      -1
      (let* ((max-k (min children (quotient (- money children) 7)))
             (remaining (- money children (* max-k 7))))
        (if (and (= remaining 3) (> max-k 0))
            (- max-k 1)
            max-k))))
```

## Erlang

```erlang
-spec dist_money(Money :: integer(), Children :: integer()) -> integer().
dist_money(Money, Children) ->
    MaxK = erlang:min(Children, Money div 8),
    find(MaxK, Money, Children).

find(K, _Money, _Children) when K < 0 ->
    -1;
find(K, Money, Children) ->
    case feasible(K, Money, Children) of
        true -> K;
        false -> find(K-1, Money, Children)
    end.

feasible(K, Money, Children) ->
    RemMoney = Money - 8 * K,
    RemChildren = Children - K,
    case RemChildren of
        0 -> RemMoney == 0;
        _ -> RemMoney >= RemChildren andalso RemMoney =/= 4 * RemChildren
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec dist_money(money :: integer, children :: integer) :: integer
  def dist_money(money, children) do
    cond do
      money < children -> -1
      money > 8 * children -> children
      true ->
        extra = money - children
        max_k = div(extra, 7)
        rem = rem(extra, 7)

        ans =
          if max_k > children do
            children
          else
            max_k
          end

        ans =
          if rem == 3 and ans > 0 do
            ans - 1
          else
            ans
          end

        ans
    end
  end
end
```
