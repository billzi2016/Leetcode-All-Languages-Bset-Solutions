# 2176. Count Equal and Divisible Pairs in an Array

## Cpp

```cpp
class Solution {
public:
    int countPairs(vector<int>& nums, int k) {
        int n = nums.size();
        int res = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (nums[i] == nums[j] && ((i * j) % k == 0)) {
                    ++res;
                }
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public int countPairs(int[] nums, int k) {
        int n = nums.length;
        int res = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (nums[i] == nums[j] && ((i * j) % k == 0)) {
                    res++;
                }
            }
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    res += 1
        return res
```

## Python3

```python
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    res += 1
        return res
```

## C

```c
int countPairs(int* nums, int numsSize, int k) {
    int res = 0;
    for (int i = 0; i < numsSize; ++i) {
        for (int j = i + 1; j < numsSize; ++j) {
            if (nums[i] == nums[j]) {
                long long prod = (long long)i * j;
                if (prod % k == 0) {
                    ++res;
                }
            }
        }
    }
    return res;
}
```

## Csharp

```csharp
public class Solution {
    public int CountPairs(int[] nums, int k) {
        int n = nums.Length;
        int count = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (nums[i] == nums[j] && ((i * j) % k == 0)) {
                    count++;
                }
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countPairs = function(nums, k) {
    let n = nums.length;
    let res = 0;
    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            if (nums[i] === nums[j] && ((i * j) % k === 0)) {
                res++;
            }
        }
    }
    return res;
};
```

## Typescript

```typescript
function countPairs(nums: number[], k: number): number {
    let res = 0;
    const n = nums.length;
    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            if (nums[i] === nums[j] && ((i * j) % k === 0)) {
                res++;
            }
        }
    }
    return res;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function countPairs($nums, $k) {
        $n = count($nums);
        $res = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                if ($nums[$i] === $nums[$j] && (($i * $j) % $k) === 0) {
                    $res++;
                }
            }
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func countPairs(_ nums: [Int], _ k: Int) -> Int {
        var result = 0
        let n = nums.count
        for i in 0..<n {
            for j in (i + 1)..<n {
                if nums[i] == nums[j] && ((i * j) % k == 0) {
                    result += 1
                }
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPairs(nums: IntArray, k: Int): Int {
        var res = 0
        val n = nums.size
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                if (nums[i] == nums[j] && ((i * j) % k == 0)) {
                    res++
                }
            }
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  int countPairs(List<int> nums, int k) {
    int n = nums.length;
    int res = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        if (nums[i] == nums[j] && ((i * j) % k == 0)) {
          res++;
        }
      }
    }
    return res;
  }
}
```

## Golang

```go
func countPairs(nums []int, k int) int {
    n := len(nums)
    res := 0
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            if nums[i] == nums[j] && (i*j)%k == 0 {
                res++
            }
        }
    }
    return res
}
```

## Ruby

```ruby
def count_pairs(nums, k)
  n = nums.length
  res = 0
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      if nums[i] == nums[j] && (i * j) % k == 0
        res += 1
      end
    end
  end
  res
end
```

## Scala

```scala
object Solution {
    def countPairs(nums: Array[Int], k: Int): Int = {
        var res = 0
        val n = nums.length
        for (i <- 0 until n) {
            for (j <- i + 1 until n) {
                if (nums(i) == nums(j) && ((i * j) % k == 0)) {
                    res += 1
                }
            }
        }
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_pairs(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut res = 0;
        for i in 0..n {
            for j in (i + 1)..n {
                if nums[i] == nums[j] && ((i * j) as i32 % k == 0) {
                    res += 1;
                }
            }
        }
        res as i32
    }
}
```

## Racket

```racket
(define/contract (count-pairs nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length nums)))
    (for/fold ([cnt 0]) ([i (in-range n)])
      (let ((vi (list-ref nums i)))
        (for/fold ([cnt cnt]) ([j (in-range (add1 i) n)])
          (if (and (= vi (list-ref nums j))
                   (= (modulo (* i j) k) 0))
              (+ cnt 1)
              cnt))))))
```

## Erlang

```erlang
-spec count_pairs(Nums :: [integer()], K :: integer()) -> integer().
count_pairs(Nums, K) ->
    Indexed = lists:zip(lists:seq(0, length(Nums) - 1), Nums),
    count_pairs_loop(Indexed, K, 0).

%% Recursive loop over the list of indexed elements
count_pairs_loop([], _K, Acc) -> Acc;
count_pairs_loop([H | T], K, Acc) ->
    {I, V} = H,
    Count = count_with_rest(I, V, T, K),
    count_pairs_loop(T, K, Acc + Count).

%% Count matching pairs of the current element with the rest
count_with_rest(_I, _V, [], _K) -> 0;
count_with_rest(I, V, [{J, W} | Rest], K) ->
    Add = if V =:= W andalso (I * J) rem K =:= 0 -> 1; true -> 0 end,
    Add + count_with_rest(I, V, Rest, K).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_pairs(nums :: [integer], k :: integer) :: integer
  def count_pairs(nums, k) do
    len = length(nums)

    0..(len - 1)
    |> Enum.reduce(0, fn i, acc ->
      (i + 1)..(len - 1)
      |> Enum.reduce(acc, fn j, inner_acc ->
        if Enum.at(nums, i) == Enum.at(nums, j) and rem(i * j, k) == 0 do
          inner_acc + 1
        else
          inner_acc
        end
      end)
    end)
  end
end
```
