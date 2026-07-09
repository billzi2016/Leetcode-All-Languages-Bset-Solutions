# 3201. Find the Maximum Length of Valid Subsequence I

## Cpp

```cpp
class Solution {
public:
    int maximumLength(vector<int>& nums) {
        auto countAll = [&](int parity)->int{
            int cnt = 0;
            for (int v : nums) if ((v & 1) == parity) ++cnt;
            return cnt;
        };
        auto countAlt = [&](int startParity)->int{
            int cnt = 0;
            int expect = startParity;
            for (int v : nums) {
                if ((v & 1) == expect) {
                    ++cnt;
                    expect ^= 1; // toggle parity
                }
            }
            return cnt;
        };
        int ans = 0;
        ans = max(ans, countAll(0));          // all even
        ans = max(ans, countAll(1));          // all odd
        ans = max(ans, countAlt(0));          // even, odd, even,...
        ans = max(ans, countAlt(1));          // odd, even, odd,...
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maximumLength(int[] nums) {
        int allEven = 0, allOdd = 0;
        for (int v : nums) {
            if ((v & 1) == 0) allEven++;
            else allOdd++;
        }
        int altStartOdd = greedy(nums, 1); // odd position -> odd, even position -> even
        int altStartEven = greedy(nums, 0); // odd position -> even, even position -> odd
        return Math.max(Math.max(allEven, allOdd), Math.max(altStartOdd, altStartEven));
    }

    private int greedy(int[] nums, int startParity) {
        int len = 0;
        int expect = startParity;
        for (int v : nums) {
            if ((v & 1) == expect) {
                len++;
                expect ^= 1; // flip parity for next position
            }
        }
        return len;
    }
}
```

## Python

```python
class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def length(first_parity, second_parity):
            cnt = 0
            for v in nums:
                expected = first_parity if (cnt & 1) == 0 else second_parity
                if (v & 1) == expected:
                    cnt += 1
            return cnt

        ans = 0
        # all even, all odd, odd-even alternating, even-odd alternating
        ans = max(ans,
                  length(0, 0),  # all even
                  length(1, 1),  # all odd
                  length(1, 0),  # odd at odd positions (0-indexed), even at even positions
                  length(0, 1))  # even at odd positions, odd at even positions
        return ans
```

## Python3

```python
class Solution:
    def maximumLength(self, nums):
        best = 0
        # pattern 0: all even
        cnt = 0
        for v in nums:
            if v % 2 == 0:
                cnt += 1
        best = max(best, cnt)
        # pattern 1: all odd
        cnt = 0
        for v in nums:
            if v % 2 == 1:
                cnt += 1
        best = max(best, cnt)
        # pattern 2: odd-indexed (1-based) -> odd, even-indexed -> even
        cnt = 0
        for v in nums:
            expected = 1 if cnt % 2 == 0 else 0  # 1 for odd, 0 for even
            if v % 2 == expected:
                cnt += 1
        best = max(best, cnt)
        # pattern 3: odd-indexed -> even, even-indexed -> odd
        cnt = 0
        for v in nums:
            expected = 0 if cnt % 2 == 0 else 1
            if v % 2 == expected:
                cnt += 1
        best = max(best, cnt)
        return best
```

## C

```c
int maximumLength(int* nums, int numsSize) {
    int best = 0;
    // All even
    int len = 0;
    for (int i = 0; i < numsSize; ++i) {
        if ((nums[i] & 1) == 0) ++len;
    }
    if (len > best) best = len;

    // All odd
    len = 0;
    for (int i = 0; i < numsSize; ++i) {
        if ((nums[i] & 1) == 1) ++len;
    }
    if (len > best) best = len;

    // Alternating, start with odd (odd positions -> odd, even positions -> even)
    len = 0;
    for (int i = 0; i < numsSize; ++i) {
        int expected = (len % 2 == 0) ? 1 : 0;
        if ((nums[i] & 1) == expected) ++len;
    }
    if (len > best) best = len;

    // Alternating, start with even
    len = 0;
    for (int i = 0; i < numsSize; ++i) {
        int expected = (len % 2 == 0) ? 0 : 1;
        if ((nums[i] & 1) == expected) ++len;
    }
    if (len > best) best = len;

    return best;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int MaximumLength(int[] nums) {
        int maxLen = 0;
        for (int pattern = 0; pattern < 4; pattern++) {
            int len = 0;
            foreach (int num in nums) {
                int parity = num & 1;
                int expected;
                if (pattern == 0) { // all even
                    expected = 0;
                } else if (pattern == 1) { // all odd
                    expected = 1;
                } else if (pattern == 2) { // odd positions odd, even positions even
                    int pos = len + 1; // 1-indexed position of the next element
                    expected = (pos & 1) == 1 ? 1 : 0;
                } else { // pattern == 3, odd positions even, even positions odd
                    int pos = len + 1;
                    expected = (pos & 1) == 1 ? 0 : 1;
                }
                if (parity == expected) {
                    len++;
                }
            }
            if (len > maxLen) maxLen = len;
        }
        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumLength = function(nums) {
    const patterns = [
        [0, 0], // all even
        [1, 1], // all odd
        [1, 0], // odd, even, odd, ...
        [0, 1]  // even, odd, even, ...
    ];
    let best = 0;
    for (const [p0, p1] of patterns) {
        let len = 0;
        for (let v of nums) {
            const parity = v & 1;
            if ((len % 2 === 0 && parity === p0) || (len % 2 === 1 && parity === p1)) {
                ++len;
            }
        }
        if (len > best) best = len;
    }
    return best;
};
```

## Typescript

```typescript
function maximumLength(nums: number[]): number {
    const patterns: ((pos: number) => number)[] = [
        () => 0,                                 // all even
        () => 1,                                 // all odd
        (pos) => (pos % 2 === 1 ? 1 : 0),        // odd index -> odd, even index -> even
        (pos) => (pos % 2 === 1 ? 0 : 1)         // odd index -> even, even index -> odd
    ];
    let best = 0;
    for (const getParity of patterns) {
        let len = 0;
        for (const v of nums) {
            const expected = getParity(len + 1);
            if ((v & 1) === expected) {
                ++len;
            }
        }
        if (len > best) best = len;
    }
    return best;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumLength($nums) {
        $cntEven = 0;
        $cntOdd = 0;
        foreach ($nums as $v) {
            if (($v & 1) == 0) {
                $cntEven++;
            } else {
                $cntOdd++;
            }
        }

        // Pattern: odd, even, odd, ...
        $lenOE = 0;
        $expect = 1; // expect odd first
        foreach ($nums as $v) {
            if (($v & 1) == $expect) {
                $lenOE++;
                $expect ^= 1; // toggle expectation
            }
        }

        // Pattern: even, odd, even, ...
        $lenEO = 0;
        $expect = 0; // expect even first
        foreach ($nums as $v) {
            if (($v & 1) == $expect) {
                $lenEO++;
                $expect ^= 1;
            }
        }

        return max($cntEven, $cntOdd, $lenOE, $lenEO);
    }
}
```

## Swift

```swift
class Solution {
    func maximumLength(_ nums: [Int]) -> Int {
        var countEven = 0
        var countOdd = 0
        
        for v in nums {
            if v & 1 == 0 {
                countEven += 1
            } else {
                countOdd += 1
            }
        }
        
        // Alternating starting with odd (parity 1)
        var lenAltOddStart = 0
        var expect = 1
        for v in nums {
            if (v & 1) == expect {
                lenAltOddStart += 1
                expect ^= 1
            }
        }
        
        // Alternating starting with even (parity 0)
        var lenAltEvenStart = 0
        expect = 0
        for v in nums {
            if (v & 1) == expect {
                lenAltEvenStart += 1
                expect ^= 1
            }
        }
        
        return max(countEven, countOdd, lenAltOddStart, lenAltEvenStart)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumLength(nums: IntArray): Int {
        var cntEven = 0
        var cntOdd = 0
        for (v in nums) {
            if ((v and 1) == 0) cntEven++ else cntOdd++
        }

        // Alternating starting with odd at position 1 (1-indexed)
        var lenStartOdd = 0
        var expectOdd = true
        for (v in nums) {
            val isOdd = (v and 1) != 0
            if ((expectOdd && isOdd) || (!expectOdd && !isOdd)) {
                lenStartOdd++
                expectOdd = !expectOdd
            }
        }

        // Alternating starting with even at position 1
        var lenStartEven = 0
        var expectEven = true
        for (v in nums) {
            val isOdd = (v and 1) != 0
            if ((expectEven && !isOdd) || (!expectEven && isOdd)) {
                lenStartEven++
                expectEven = !expectEven
            }
        }

        return maxOf(cntEven, cntOdd, lenStartOdd, lenStartEven)
    }
}
```

## Dart

```dart
class Solution {
  int maximumLength(List<int> nums) {
    int cntEven = 0, cntOdd = 0;
    for (int v in nums) {
      if ((v & 1) == 0) {
        cntEven++;
      } else {
        cntOdd++;
      }
    }

    int lenStartOdd = _alternatingLen(nums, 1);
    int lenStartEven = _alternatingLen(nums, 0);

    int ans = cntEven;
    if (cntOdd > ans) ans = cntOdd;
    if (lenStartOdd > ans) ans = lenStartOdd;
    if (lenStartEven > ans) ans = lenStartEven;

    return ans;
  }

  int _alternatingLen(List<int> nums, int startParity) {
    int expect = startParity;
    int len = 0;
    for (int v in nums) {
      if ((v & 1) == expect) {
        len++;
        expect ^= 1;
      }
    }
    return len;
  }
}
```

## Golang

```go
func maximumLength(nums []int) int {
	maxLen := 0

	// All even
	cnt := 0
	for _, v := range nums {
		if v%2 == 0 {
			cnt++
		}
	}
	if cnt > maxLen {
		maxLen = cnt
	}

	// All odd
	cnt = 0
	for _, v := range nums {
		if v%2 != 0 {
			cnt++
		}
	}
	if cnt > maxLen {
		maxLen = cnt
	}

	// Alternating, start with odd (odd index -> odd, even index -> even)
	cnt = 0
	expect := 1 // odd
	for _, v := range nums {
		if v%2 == expect {
			cnt++
			expect ^= 1
		}
	}
	if cnt > maxLen {
		maxLen = cnt
	}

	// Alternating, start with even (odd index -> even, even index -> odd)
	cnt = 0
	expect = 0 // even
	for _, v := range nums {
		if v%2 == expect {
			cnt++
			expect ^= 1
		}
	}
	if cnt > maxLen {
		maxLen = cnt
	}

	return maxLen
}
```

## Ruby

```ruby
def maximum_length(nums)
  cnt_even = 0
  nums.each { |v| cnt_even += 1 if v.even? }
  cnt_odd = nums.length - cnt_even

  len_start_odd = 0
  expect = 1
  nums.each do |v|
    if (v & 1) == expect
      len_start_odd += 1
      expect ^= 1
    end
  end

  len_start_even = 0
  expect = 0
  nums.each do |v|
    if (v & 1) == expect
      len_start_even += 1
      expect ^= 1
    end
  end

  [cnt_even, cnt_odd, len_start_odd, len_start_even].max
end
```

## Scala

```scala
object Solution {
    def maximumLength(nums: Array[Int]): Int = {
        var lenAllEven = 0
        var lenAllOdd = 0
        var lenAlt1 = 0 // odd position -> odd, even position -> even
        var lenAlt2 = 0 // odd position -> even, even position -> odd

        for (num <- nums) {
            val parity = num & 1
            if (parity == 0) lenAllEven += 1 else lenAllOdd += 1

            if ((lenAlt1 % 2 == 0 && parity == 1) || (lenAlt1 % 2 == 1 && parity == 0)) {
                lenAlt1 += 1
            }
            if ((lenAlt2 % 2 == 0 && parity == 0) || (lenAlt2 % 2 == 1 && parity == 1)) {
                lenAlt2 += 1
            }
        }

        var ans = lenAllEven
        if (lenAllOdd > ans) ans = lenAllOdd
        if (lenAlt1 > ans) ans = lenAlt1
        if (lenAlt2 > ans) ans = lenAlt2
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_length(nums: Vec<i32>) -> i32 {
        let mut best = 0;
        for pattern in 0..4 {
            let mut len: i32 = 0;
            for &x in nums.iter() {
                let p = (x & 1) as i32; // parity of current number
                let expect = match pattern {
                    0 => 0,                                   // all even
                    1 => 1,                                   // all odd
                    2 => if ((len + 1) % 2) == 1 { 1 } else { 0 }, // odd idx -> odd, even idx -> even
                    3 => if ((len + 1) % 2) == 1 { 0 } else { 1 }, // odd idx -> even, even idx -> odd
                    _ => unreachable!(),
                };
                if p == expect {
                    len += 1;
                }
            }
            if len > best {
                best = len;
            }
        }
        best
    }
}
```

## Racket

```racket
(define/contract (maximum-length nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((evens
          (foldl (lambda (x acc) (if (= (bitwise-and x 1) 0) (+ acc 1) acc)) 0 nums))
         (odds
          (foldl (lambda (x acc) (if (= (bitwise-and x 1) 1) (+ acc 1) acc)) 0 nums))
         (len-start-even
          (let loop ((lst nums) (expect 0) (len 0))
            (if (null? lst)
                len
                (let ((x (car lst)))
                  (if (= (bitwise-and x 1) expect)
                      (loop (cdr lst) (bitwise-xor expect 1) (+ len 1))
                      (loop (cdr lst) expect len))))))
         (len-start-odd
          (let loop ((lst nums) (expect 1) (len 0))
            (if (null? lst)
                len
                (let ((x (car lst)))
                  (if (= (bitwise-and x 1) expect)
                      (loop (cdr lst) (bitwise-xor expect 1) (+ len 1))
                      (loop (cdr lst) expect len))))))
         (alternating (max len-start-even len-start-odd)))
    (max evens odds alternating)))
```

## Erlang

```erlang
-module(solution).
-export([maximum_length/1]).

-spec maximum_length(Nums :: [integer()]) -> integer().
maximum_length(Nums) ->
    AllEven = count_fixed(Nums, 0, 0),
    AllOdd = count_fixed(Nums, 1, 0),
    AltOE = count_alt(Nums, 1, 0),
    AltEO = count_alt(Nums, 0, 0),
    lists:max([AllEven, AllOdd, AltOE, AltEO]).

count_fixed([], _Par, Acc) -> Acc;
count_fixed([H|T], Par, Acc) ->
    case H band 1 of
        Par -> count_fixed(T, Par, Acc + 1);
        _   -> count_fixed(T, Par, Acc)
    end.

count_alt([], _Expect, Acc) -> Acc;
count_alt([H|T], Expect, Acc) ->
    case H band 1 of
        Expect ->
            NewExpect = 1 - Expect,
            count_alt(T, NewExpect, Acc + 1);
        _ ->
            count_alt(T, Expect, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_length(nums :: [integer]) :: integer
  def maximum_length(nums) do
    {cnt_even, cnt_odd} = Enum.reduce(nums, {0, 0}, fn x, {e, o} ->
      if rem(x, 2) == 0, do: {e + 1, o}, else: {e, o + 1}
    end)

    len_start_odd = greedy(nums, 1)
    len_start_even = greedy(nums, 0)

    Enum.max([cnt_even, cnt_odd, len_start_odd, len_start_even])
  end

  defp greedy(list, start_parity) do
    {len, _} =
      Enum.reduce(list, {0, start_parity}, fn x, {len, expected} ->
        if rem(x, 2) == expected do
          {len + 1, 1 - expected}
        else
          {len, expected}
        end
      end)

    len
  end
end
```
