# 2029. Stone Game IX

## Cpp

```cpp
class Solution {
public:
    bool stoneGameIX(vector<int>& stones) {
        long long cnt[3] = {0, 0, 0};
        for (int x : stones) ++cnt[x % 3];
        if ((cnt[1] == 0 && cnt[2] == 0) || cnt[1] == 0 || cnt[2] == 0) return false;
        if (cnt[0] % 2 == 0) {
            return cnt[1] == cnt[2];
        } else {
            return llabs(cnt[1] - cnt[2]) > 1;
        }
    }
};
```

## Java

```java
class Solution {
    public boolean stoneGameIX(int[] stones) {
        int[] cnt = new int[3];
        for (int v : stones) {
            cnt[v % 3]++;
        }
        // If one of the non-zero residues is missing, Alice cannot win.
        if (cnt[1] == 0 || cnt[2] == 0) {
            return false;
        }
        // Both residues 1 and 2 are present. Alice wins iff count of zeros is even.
        return cnt[0] % 2 == 0;
    }
}
```

## Python

```python
class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        cnt = [0, 0, 0]
        for x in stones:
            cnt[x % 3] += 1
        c0, c1, c2 = cnt

        # both remainders 1 and 2 are present
        if c1 > 0 and c2 > 0:
            return c0 % 2 == 0

        # only zeros
        if c1 == 0 and c2 == 0:
            return False

        # exactly one of remainder 1 or 2 exists
        cnt_one_type = c1 if c1 else c2
        if c0 == 0:
            return False
        # Alice can win only when the count modulo 3 equals 2
        return cnt_one_type % 3 == 2
```

## Python3

```python
class Solution:
    def stoneGameIX(self, stones):
        cnt = [0, 0, 0]
        for x in stones:
            cnt[x % 3] += 1
        c0, c1, c2 = cnt[0], cnt[1], cnt[2]
        if c0 % 2 == 0:
            return (c1 > 0 and c2 > 0) or (c1 >= 3)
        else:
            return (c1 >= 2) or (c2 >= 2)
```

## C

```c
bool stoneGameIX(int* stones, int stonesSize) {
    long long cnt[3] = {0, 0, 0};
    for (int i = 0; i < stonesSize; ++i) {
        cnt[stones[i] % 3]++;
    }
    long long c0 = cnt[0], c1 = cnt[1], c2 = cnt[2];
    if (c1 > 0 && c2 > 0) {
        return (c0 % 2 == 0);
    } else if (c1 > 0) {
        return (c1 >= 3 && (c0 % 2 == 1));
    } else if (c2 > 0) {
        return (c2 >= 3 && (c0 % 2 == 1));
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool StoneGameIX(int[] stones) {
        int[] cnt = new int[3];
        foreach (int x in stones) {
            cnt[x % 3]++;
        }
        // Need at least one stone with remainder 1 and one with remainder 2
        if (cnt[1] == 0 || cnt[2] == 0) return false;
        // Alice wins only when the number of remainder-0 stones is even
        return cnt[0] % 2 == 0;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} stones
 * @return {boolean}
 */
var stoneGameIX = function(stones) {
    const cnt = [0, 0, 0];
    for (const v of stones) {
        cnt[v % 3]++;
    }
    if (cnt[0] % 2 === 0) {
        return cnt[1] > 0 && cnt[2] > 0;
    } else {
        return Math.abs(cnt[1] - cnt[2]) > 2;
    }
};
```

## Typescript

```typescript
function stoneGameIX(stones: number[]): boolean {
    const cnt = [0, 0, 0];
    for (const v of stones) cnt[v % 3]++;
    const c0 = cnt[0], c1 = cnt[1], c2 = cnt[2];

    if (c1 === 0 && c2 === 0) return false;

    if (c1 === 0) {
        // only remainder 2 stones
        if (c2 < 3) return false;
        return c0 % 2 === 1;
    }
    if (c2 === 0) {
        // only remainder 1 stones
        if (c1 < 3) return false;
        return c0 % 2 === 1;
    }

    // both remainders present
    if (Math.abs(c1 - c2) > 2) return true;
    return c0 % 2 === 0;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $stones
     * @return Boolean
     */
    function stoneGameIX($stones) {
        $c0 = $c1 = $c2 = 0;
        foreach ($stones as $v) {
            $mod = $v % 3;
            if ($mod == 0) {
                $c0++;
            } elseif ($mod == 1) {
                $c1++;
            } else {
                $c2++;
            }
        }

        // only zeros
        if ($c1 == 0 && $c2 == 0) {
            return false;
        }

        // only remainder 1 stones (and possibly zeros)
        if ($c2 == 0) {
            // any zero lets Bob force a win
            if ($c0 > 0) {
                return false;
            }
            // Alice wins iff count of remainder‑1 stones is even
            return $c1 % 2 == 0;
        }

        // only remainder 2 stones (and possibly zeros)
        if ($c1 == 0) {
            if ($c0 > 0) {
                return false;
            }
            return $c2 % 2 == 0;
        }

        // both remainder 1 and 2 are present
        $diff = abs($c1 - $c2);
        if ($diff > 1) {
            return true;
        }
        if ($diff == 1) {
            return true;
        }
        // equal counts: outcome depends on parity of zeros
        return $c0 % 2 == 0;
    }
}
```

## Swift

```swift
class Solution {
    func stoneGameIX(_ stones: [Int]) -> Bool {
        var cnt = [0, 0, 0]
        for v in stones {
            cnt[v % 3] += 1
        }
        return cnt[1] > 0 && cnt[2] > 0
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun stoneGameIX(stones: IntArray): Boolean {
        var cnt0 = 0
        var cnt1 = 0
        var cnt2 = 0
        for (s in stones) {
            when (s % 3) {
                0 -> cnt0++
                1 -> cnt1++
                else -> cnt2++
            }
        }
        return if (cnt0 % 2 == 0) {
            cnt1 > 0 && cnt2 > 0
        } else {
            kotlin.math.abs(cnt1 - cnt2) > 2
        }
    }
}
```

## Dart

```dart
class Solution {
  bool stoneGameIX(List<int> stones) {
    List<int> cnt = [0, 0, 0];
    for (int x in stones) {
      cnt[x % 3]++;
    }
    if (cnt[0] % 2 == 0) {
      return (cnt[1] > 0 && cnt[2] > 0) || (cnt[1] >= 3) || (cnt[2] >= 3);
    } else {
      return (cnt[1] > 0 && cnt[2] > 0 && (cnt[1] - cnt[2]).abs() > 2);
    }
  }
}
```

## Golang

```go
func stoneGameIX(stones []int) bool {
	var c0, c1, c2 int
	for _, v := range stones {
		switch v % 3 {
		case 0:
			c0++
		case 1:
			c1++
		case 2:
			c2++
		}
	}
	if c0%2 == 0 {
		return c1 > 0 && c2 > 0
	}
	diff := c1 - c2
	if diff < 0 {
		diff = -diff
	}
	return diff > 2
}
```

## Ruby

```ruby
def stone_game_ix(stones)
  cnt = [0, 0, 0]
  stones.each { |x| cnt[x % 3] += 1 }
  c0, c1, c2 = cnt

  # No non‑zero remainders -> Alice cannot avoid losing immediately
  return false if c1 == 0 && c2 == 0

  # Only one type of non‑zero remainder present
  if c1 == 0
    return c2 >= 3 && c0 > 0
  elsif c2 == 0
    return c1 >= 3 && c0 > 0
  end

  # Both types are present
  if c0 == 0
    true
  else
    c1 != c2
  end
end
```

## Scala

```scala
object Solution {
    def stoneGameIX(stones: Array[Int]): Boolean = {
        var c0, c1, c2 = 0
        for (v <- stones) {
            v % 3 match {
                case 0 => c0 += 1
                case 1 => c1 += 1
                case 2 => c2 += 1
            }
        }
        if (c1 == 0 && c2 == 0) false
        else if (c1 == 0 || c2 == 0) false
        else (c0 % 2 == 0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn stone_game_ix(stones: Vec<i32>) -> bool {
        let mut cnt = [0i32; 3];
        for v in stones {
            cnt[(v % 3) as usize] += 1;
        }
        let c0 = cnt[0];
        let c1 = cnt[1];
        let c2 = cnt[2];

        // no stone with remainder 1 or 2 -> Alice loses immediately
        if c1 == 0 && c2 == 0 {
            return false;
        }

        // only type 1 stones (c2 == 0)
        if c2 == 0 {
            // need at least three such stones and an odd number of zeros to flip parity
            return c1 >= 3 && c0 % 2 == 1;
        }
        // only type 2 stones (c1 == 0)
        if c1 == 0 {
            return c2 >= 3 && c0 % 2 == 1;
        }

        // both types present
        if c0 % 2 == 0 {
            // even number of zeros -> Alice can always force a win
            true
        } else {
            // odd number of zeros -> need at least three stones of one type
            (c1 >= 3 && c2 >= 1) || (c2 >= 3 && c1 >= 1)
        }
    }
}
```

## Racket

```racket
#lang racket
(require racket/match)

(define/contract (stone-game-ix stones)
  (-> (listof exact-integer?) boolean?)
  (let-values ([(c0 c1 c2)
                (foldl (lambda (x acc)
                         (match-define (list a b c) acc)
                         (case (modulo x 3)
                           [(0) (list (+ a 1) b c)]
                           [(1) (list a (+ b 1) c)]
                           [(2) (list a b (+ c 1))]))
                       (list 0 0 0)
                       stones)])
    (if (even? c0)
        (and (> c1 0) (> c2 0))
        (> (abs (- c1 c2)) 2))))
```

## Erlang

```erlang
-spec stone_game_ix(Stones :: [integer()]) -> boolean().
stone_game_ix(Stones) ->
    {_, C1, C2} = lists:foldl(
        fun(X, {C0, C1Acc, C2Acc}) ->
            case X rem 3 of
                0 -> {C0 + 1, C1Acc, C2Acc};
                1 -> {C0, C1Acc + 1, C2Acc};
                2 -> {C0, C1Acc, C2Acc + 1}
            end
        end,
        {0, 0, 0},
        Stones),
    case {C1, C2} of
        {0, _} -> false;
        {_, 0} -> false;
        _ ->
            DiffMod = (abs(C1 - C2)) rem 3,
            MinOdd = (erlang:min(C1, C2) band 1) =:= 1,
            (DiffMod =/= 0) orelse MinOdd
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec stone_game_ix(stones :: [integer]) :: boolean
  def stone_game_ix(stones) do
    {c0, c1, c2} =
      Enum.reduce(stones, {0, 0, 0}, fn x, {z, o, t} ->
        case rem(x, 3) do
          0 -> {z + 1, o, t}
          1 -> {z, o + 1, t}
          2 -> {z, o, t + 1}
        end
      end)

    cond do
      c1 == 0 and c2 == 0 ->
        false

      c1 == 0 ->
        # only remainder 2 stones
        rem(c0, 2) == 1 and c2 >= 3

      c2 == 0 ->
        # only remainder 1 stones
        rem(c0, 2) == 1 and c1 >= 3

      c1 == c2 ->
        c1 == 1

      true ->
        true
    end
  end
end
```
