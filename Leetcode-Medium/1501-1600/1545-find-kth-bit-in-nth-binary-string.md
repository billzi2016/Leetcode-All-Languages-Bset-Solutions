# 1545. Find Kth Bit in Nth Binary String

## Cpp

```cpp
class Solution {
public:
    char findKthBit(int n, int k) {
        return helper(n, k);
    }
private:
    char helper(int n, int k) {
        if (n == 1) return '0';
        int mid = 1 << (n - 1); // middle position
        if (k == mid) return '1';
        if (k < mid) return helper(n - 1, k);
        // k > mid: mirror to the left part and invert
        char c = helper(n - 1, (1 << n) - k);
        return c == '0' ? '1' : '0';
    }
};
```

## Java

```java
class Solution {
    public char findKthBit(int n, int k) {
        return kthBit(n, k);
    }
    
    private char kthBit(int n, int k) {
        if (n == 1) {
            return '0';
        }
        int len = (1 << n) - 1;          // length of S_n
        int mid = (len + 1) / 2;         // middle position = 2^{n-1}
        if (k == mid) {
            return '1';
        } else if (k < mid) {
            return kthBit(n - 1, k);
        } else {
            char mirrored = kthBit(n - 1, len - k + 1); // mirror to first half
            return mirrored == '0' ? '1' : '0';         // invert
        }
    }
}
```

## Python

```python
class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 1:
            return "0"
        length = (1 << n) - 1          # total length of S_n
        mid = (length // 2) + 1        # position of the middle '1'
        if k == mid:
            return "1"
        if k < mid:
            return self.findKthBit(n - 1, k)
        # k > mid: map to mirrored position in S_{n-1} and invert
        mirror = length - k + 1
        bit = self.findKthBit(n - 1, mirror)
        return "0" if bit == "1" else "1"
```

## Python3

```python
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n: int, k: int) -> int:
            if n == 1:
                return 0
            length = (1 << n) - 1
            mid = 1 << (n - 1)
            if k == mid:
                return 1
            if k < mid:
                return helper(n - 1, k)
            # second half: mirror and invert
            mirrored_k = length - k + 1
            bit = helper(n - 1, mirrored_k)
            return 1 - bit

        return str(helper(n, k))
```

## C

```c
char findKthBit(int n, int k) {
    if (n == 1) return '0';
    int len = (1 << n) - 1;          // length of S_n
    int mid = (len + 1) >> 1;        // middle position = 2^{n-1}
    if (k == mid) return '1';
    if (k < mid) return findKthBit(n - 1, k);
    char c = findKthBit(n - 1, len - k + 1); // mirror to first half
    return c == '0' ? '1' : '0';   // invert
}
```

## Csharp

```csharp
public class Solution
{
    public char FindKthBit(int n, int k)
    {
        return GetBit(n, k);
    }

    private char GetBit(int n, int k)
    {
        if (n == 1) return '0';

        int mid = 1 << (n - 1); // position of the middle '1' in S_n
        if (k == mid) return '1';
        if (k < mid) return GetBit(n - 1, k);

        // k is in the right part: mirror to left part and invert
        int mirroredPos = (1 << n) - k; // 2^n - k
        char c = GetBit(n - 1, mirroredPos);
        return c == '0' ? '1' : '0';
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {character}
 */
var findKthBit = function(n, k) {
    const dfs = (n, k) => {
        if (n === 1) return '0';
        const mid = 1 << (n - 1); // middle position = 2^{n-1}
        if (k === mid) return '1';
        if (k < mid) {
            return dfs(n - 1, k);
        } else {
            // mirrored index in the left part
            const mirrored = (1 << n) - k; // 2^n - k
            const bit = dfs(n - 1, mirrored);
            return bit === '0' ? '1' : '0';
        }
    };
    return dfs(n, k);
};
```

## Typescript

```typescript
function findKthBit(n: number, k: number): string {
    const helper = (n: number, k: number): string => {
        if (n === 1) return '0';
        const mid = 1 << (n - 1); // position of the middle '1'
        if (k === mid) return '1';
        if (k < mid) {
            return helper(n - 1, k);
        } else {
            const len = (1 << n) - 1;
            const mirroredK = len - k + 1; // position in the left part
            const bit = helper(n - 1, mirroredK);
            return bit === '0' ? '1' : '0';
        }
    };
    return helper(n, k);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer $k
     * @return String
     */
    function findKthBit($n, $k) {
        if ($n == 1) {
            return '0';
        }
        $mid = 1 << ($n - 1);
        if ($k == $mid) {
            return '1';
        } elseif ($k < $mid) {
            return $this->findKthBit($n - 1, $k);
        } else {
            $len = (1 << $n) - 1;
            $mirror = $len - $k + 1;
            $bit = $this->findKthBit($n - 1, $mirror);
            return $bit === '0' ? '1' : '0';
        }
    }
}
```

## Swift

```swift
class Solution {
    func findKthBit(_ n: Int, _ k: Int) -> Character {
        return helper(n, k)
    }
    
    private func helper(_ n: Int, _ k: Int) -> Character {
        if n == 1 { return "0" }
        let mid = 1 << (n - 1)          // middle position
        if k == mid {
            return "1"
        } else if k < mid {
            return helper(n - 1, k)
        } else {
            let newK = (1 << n) - k     // mirrored position in the left half
            let ch = helper(n - 1, newK)
            return ch == "0" ? "1" : "0"
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findKthBit(n: Int, k: Int): Char {
        return helper(n, k)
    }

    private fun helper(n: Int, k: Int): Char {
        if (n == 1) return '0'
        val mid = 1 shl (n - 1) // position of the middle '1'
        return when {
            k == mid -> '1'
            k < mid -> helper(n - 1, k)
            else -> {
                val mirrored = (1 shl n) - k
                val bit = helper(n - 1, mirrored)
                if (bit == '0') '1' else '0'
            }
        }
    }
}
```

## Dart

```dart
class Solution {
  String findKthBit(int n, int k) {
    int helper(int n, int k) {
      if (n == 1) return 0;
      int mid = 1 << (n - 1);
      if (k == mid) return 1;
      if (k < mid) return helper(n - 1, k);
      // second half: mirror position and invert
      int mirrored = (1 << n) - k; // 2^n - k
      int bit = helper(n - 1, mirrored);
      return bit ^ 1;
    }

    return helper(n, k).toString();
  }
}
```

## Golang

```go
func findKthBit(n int, k int) byte {
	var dfs func(int, int) byte
	dfs = func(n, k int) byte {
		if n == 1 {
			return '0'
		}
		length := (1 << n) - 1          // total length of S_n
		mid := (length + 1) >> 1        // position of the middle '1', equals 2^(n-1)
		if k == mid {
			return '1'
		}
		if k < mid {
			return dfs(n-1, k)
		}
		// k > mid: mirror to first half and invert
		newK := length + 1 - k
		b := dfs(n-1, newK)
		if b == '0' {
			return '1'
		}
		return '0'
	}
	return dfs(n, k)
}
```

## Ruby

```ruby
def find_kth_bit(n, k)
  return '0' if n == 1
  len = (1 << n) - 1
  mid = (len + 1) / 2
  if k == mid
    '1'
  elsif k < mid
    find_kth_bit(n - 1, k)
  else
    idx = len - k + 1
    bit = find_kth_bit(n - 1, idx)
    bit == '0' ? '1' : '0'
  end
end
```

## Scala

```scala
object Solution {
    def findKthBit(n: Int, k: Int): Char = {
        def helper(level: Int, pos: Int): Char = {
            if (level == 1) return '0'
            val len = (1 << level) - 1
            val mid = 1 << (level - 1)
            if (pos == mid) '1'
            else if (pos < mid) helper(level - 1, pos)
            else {
                val mirrored = len - pos + 1
                val bit = helper(level - 1, mirrored)
                if (bit == '0') '1' else '0'
            }
        }
        helper(n, k)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_kth_bit(n: i32, k: i32) -> char {
        fn helper(n: i32, k: i32) -> i32 {
            if n == 1 {
                return 0;
            }
            let mid = 1 << (n - 1);
            if k == mid {
                1
            } else if k < mid {
                helper(n - 1, k)
            } else {
                // mirrored position in the left half
                let mirrored = (1 << n) - k;
                1 - helper(n - 1, mirrored)
            }
        }

        match helper(n, k) {
            0 => '0',
            _ => '1',
        }
    }
}
```

## Racket

```racket
(define/contract (find-kth-bit n k)
  (-> exact-integer? exact-integer? char?)
  (letrec ((helper
            (lambda (n k invert?)
              (if (= n 1)
                  (if invert? #\1 #\0)
                  (let* ((len (- (arithmetic-shift 1 n) 1))
                         (mid (arithmetic-shift 1 (- n 1))))
                    (cond
                      [(= k mid) (if invert? #\0 #\1)]
                      [(< k mid) (helper (- n 1) k invert?)]
                      [else (helper (- n 1)
                                    (+ (- len k) 1)
                                    (not invert?))]))))))
    (helper n k #f)))
```

## Erlang

```erlang
-module(solution).
-export([find_kth_bit/2]).

-spec find_kth_bit(N :: integer(), K :: integer()) -> char().
find_kth_bit(N, K) ->
    find(N, K).

find(1, _) ->
    $0;
find(N, K) ->
    Len = (1 bsl N) - 1,
    Mid = (Len div 2) + 1,
    case K of
        _ when K == Mid -> $1;
        _ when K < Mid   -> find(N - 1, K);
        _                ->
            NewK = Len - K + 1,
            invert(find(N - 1, NewK))
    end.

invert($0) -> $1;
invert($1) -> $0.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_kth_bit(n :: integer, k :: integer) :: char
  def find_kth_bit(n, k) do
    helper(n, k)
  end

  defp helper(1, _k), do: "0"

  defp helper(n, k) do
    mid = 1 <<< (n - 1)

    cond do
      k == mid ->
        "1"

      k < mid ->
        helper(n - 1, k)

      true ->
        # Mirror position in the first half and invert the result
        new_k = (1 <<< n) - k
        invert(helper(n - 1, new_k))
    end
  end

  defp invert("0"), do: "1"
  defp invert("1"), do: "0"
end
```
