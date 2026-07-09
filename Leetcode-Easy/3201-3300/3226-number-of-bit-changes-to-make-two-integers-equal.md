# 3226. Number of Bit Changes to Make Two Integers Equal

## Cpp

```cpp
class Solution {
public:
    int minChanges(int n, int k) {
        // If k has a bit set that n does not have, it's impossible
        if ((k & ~n) != 0) return -1;
        // Count bits that are 1 in n and 0 in k
        return __builtin_popcount(n & ~k);
    }
};
```

## Java

```java
class Solution {
    public int minChanges(int n, int k) {
        // If k has a 1 where n has 0, impossible
        if ((k & ~n) != 0) return -1;
        // Count bits that are 1 in n and 0 in k
        return Integer.bitCount(n & ~k);
    }
}
```

## Python

```python
class Solution(object):
    def minChanges(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # If there exists a bit that is 0 in n and 1 in k, impossible.
        if k & ~n:
            return -1
        # Count bits that are 1 in n but 0 in k.
        return bin(n & ~k).count('1')
```

## Python3

```python
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        # If any bit required by k is not present in n, impossible
        if (n & k) != k:
            return -1
        # Bits to turn off are those set in n but not in k
        return (n & ~k).bit_count()
```

## C

```c
int minChanges(int n, int k) {
    if ((~n) & k) return -1;
    int diff = n & ~k;
    return __builtin_popcount(diff);
}
```

## Csharp

```csharp
public class Solution {
    public int MinChanges(int n, int k) {
        // If there is a bit that is 0 in n but 1 in k, impossible.
        if ((k & ~n) != 0) return -1;
        int diff = n & ~k; // bits that need to be turned from 1 to 0
        int cnt = 0;
        while (diff != 0) {
            cnt += diff & 1;
            diff >>= 1;
        }
        return cnt;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var minChanges = function(n, k) {
    // If there is any bit that is 0 in n but 1 in k, impossible.
    if ((k & (~n)) !== 0) return -1;
    
    // Bits that are 1 in n and need to become 0 (where k has 0).
    let diff = n & (~k);
    
    // Count set bits in diff.
    let cnt = 0;
    while (diff) {
        diff &= diff - 1; // clear lowest set bit
        cnt++;
    }
    return cnt;
};
```

## Typescript

```typescript
function minChanges(n: number, k: number): number {
    // If any bit is 1 in k but 0 in n, impossible
    if ((n & k) !== k) return -1;
    let diff = n ^ k; // bits that differ (only where n has 1 and k has 0)
    let cnt = 0;
    while (diff) {
        cnt += diff & 1;
        diff >>>= 1;
    }
    return cnt;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function minChanges($n, $k) {
        // If k has a bit that n doesn't have, impossible
        if ( ($n & $k) != $k ) {
            return -1;
        }
        $diff = $n ^ $k; // bits that differ; all are 1 in n and 0 in k
        $cnt = 0;
        while ($diff > 0) {
            $cnt += $diff & 1;
            $diff >>= 1;
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func minChanges(_ n: Int, _ k: Int) -> Int {
        // If k has a 1 where n has 0, it's impossible
        if (k & ~n) != 0 {
            return -1
        }
        // Count bits that are 1 in n and 0 in k
        let changes = (n & ~k).nonzeroBitCount
        return changes
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minChanges(n: Int, k: Int): Int {
        // All bits set in k must also be set in n; otherwise impossible
        if ((n and k) != k) return -1
        // Count the bits that are 1 in n but 0 in k
        return Integer.bitCount(n xor k)
    }
}
```

## Dart

```dart
class Solution {
  int minChanges(int n, int k) {
    // If there is any bit that is 1 in k but 0 in n, impossible.
    if ((n & k) != k) return -1;
    int diff = n & ~k;
    int cnt = 0;
    while (diff > 0) {
      cnt += diff & 1;
      diff >>= 1;
    }
    return cnt;
  }
}
```

## Golang

```go
func minChanges(n int, k int) int {
	if (k & ^n) != 0 {
		return -1
	}
	diff := n & ^k
	return bits.OnesCount(uint(diff))
}
```

## Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def min_changes(n, k)
  return -1 if (n & k) != k
  n.to_s(2).count('1') - k.to_s(2).count('1')
end
```

## Scala

```scala
object Solution {
    def minChanges(n: Int, k: Int): Int = {
        if ((k | n) != n) -1
        else Integer.bitCount(n ^ k)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_changes(n: i32, k: i32) -> i32 {
        let n_u = n as u32;
        let k_u = k as u32;
        if (n_u & k_u) != k_u {
            return -1;
        }
        (n_u ^ k_u).count_ones() as i32
    }
}
```

## Racket

```racket
(require racket/bitwise)

(define (popcnt x)
  (let loop ((y x) (c 0))
    (if (zero? y)
        c
        (loop (bitwise-and y (- y 1)) (+ c 1)))))

(define/contract (min-changes n k)
  (-> exact-integer? exact-integer? exact-integer?)
  (if (= (bitwise-and n k) k)
      (popcnt (bitwise-xor n k))
      -1))
```

## Erlang

```erlang
-spec min_changes(N :: integer(), K :: integer()) -> integer().
min_changes(N, K) ->
    case (K band bnot(N)) of
        0 -> count_ones(N band bnot(K));
        _ -> -1
    end.

count_ones(0) -> 0;
count_ones(X) -> count_ones(X, 0).

count_ones(0, Acc) -> Acc;
count_ones(X, Acc) ->
    count_ones(X bsr 1, Acc + (X band 1)).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec min_changes(n :: integer, k :: integer) :: integer
  def min_changes(n, k) do
    if (k &&& bnot(n)) != 0 do
      -1
    else
      diff = n &&& bnot(k)
      count_bits(diff)
    end
  end

  defp count_bits(0), do: 0
  defp count_bits(x) do
    count_bits(x &&& (x - 1)) + 1
  end
end
```
