# 1512. Number of Good Pairs

## Cpp

```cpp
class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int freq[101] = {0};
        for (int x : nums) ++freq[x];
        int ans = 0;
        for (int cnt : freq) {
            if (cnt > 1) ans += cnt * (cnt - 1) / 2;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int numIdenticalPairs(int[] nums) {
        int[] freq = new int[101];
        int pairs = 0;
        for (int num : nums) {
            pairs += freq[num];
            freq[num]++;
        }
        return pairs;
    }
}
```

## Python

```python
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        pairs = 0
        for num in nums:
            if num in freq:
                pairs += freq[num]
                freq[num] += 1
            else:
                freq[num] = 1
        return pairs
```

## Python3

```python
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        ans = 0
        for x in nums:
            if x in freq:
                ans += freq[x]
                freq[x] += 1
            else:
                freq[x] = 1
        return ans
```

## C

```c
int numIdenticalPairs(int* nums, int numsSize) {
    int freq[101] = {0};
    int count = 0;
    for (int i = 0; i < numsSize; ++i) {
        int v = nums[i];
        count += freq[v];
        freq[v]++;
    }
    return count;
}
```

## Csharp

```csharp
public class Solution
{
    public int NumIdenticalPairs(int[] nums)
    {
        int[] freq = new int[101];
        int result = 0;
        foreach (int x in nums)
        {
            result += freq[x];
            freq[x]++;
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    const freq = new Map();
    let pairs = 0;
    for (const x of nums) {
        const cnt = freq.get(x) || 0;
        pairs += cnt; // each previous occurrence forms a good pair with current
        freq.set(x, cnt + 1);
    }
    return pairs;
};
```

## Typescript

```typescript
function numIdenticalPairs(nums: number[]): number {
    const freq = new Map<number, number>();
    let result = 0;
    for (const v of nums) {
        const count = freq.get(v) ?? 0;
        result += count;
        freq.set(v, count + 1);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numIdenticalPairs($nums) {
        $freq = [];
        $result = 0;
        foreach ($nums as $num) {
            if (isset($freq[$num])) {
                $result += $freq[$num];
                $freq[$num]++;
            } else {
                $freq[$num] = 1;
            }
        }
        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func numIdenticalPairs(_ nums: [Int]) -> Int {
        var count = [Int:Int]()
        var result = 0
        for num in nums {
            if let c = count[num] {
                result += c
                count[num] = c + 1
            } else {
                count[num] = 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numIdenticalPairs(nums: IntArray): Int {
        val freq = IntArray(101)
        var result = 0
        for (num in nums) {
            result += freq[num]
            freq[num]++
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int numIdenticalPairs(List<int> nums) {
    final Map<int, int> freq = {};
    int result = 0;
    for (final int x in nums) {
      final int count = freq[x] ?? 0;
      result += count;
      freq[x] = count + 1;
    }
    return result;
  }
}
```

## Golang

```go
func numIdenticalPairs(nums []int) int {
    freq := make(map[int]int)
    for _, v := range nums {
        freq[v]++
    }
    count := 0
    for _, c := range freq {
        if c > 1 {
            count += c * (c - 1) / 2
        }
    }
    return count
}
```

## Ruby

```ruby
def num_identical_pairs(nums)
  freq = Hash.new(0)
  nums.each { |x| freq[x] += 1 }
  ans = 0
  freq.each_value { |c| ans += c * (c - 1) / 2 }
  ans
end
```

## Scala

```scala
object Solution {
    def numIdenticalPairs(nums: Array[Int]): Int = {
        val freq = new Array[Int](101)
        var pairs = 0
        for (num <- nums) {
            pairs += freq(num)
            freq(num) += 1
        }
        pairs
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_identical_pairs(nums: Vec<i32>) -> i32 {
        let mut freq = [0i32; 101];
        let mut ans = 0i32;
        for &v in nums.iter() {
            let idx = v as usize;
            ans += freq[idx];
            freq[idx] += 1;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (num-identical-pairs nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ([freq (make-hash)])
    (for ([x nums])
      (hash-update! freq x add1 0))
    (let loop ((keys (hash-keys freq)) (total 0))
      (if (null? keys)
          total
          (let* ([cnt (hash-ref freq (car keys))]
                 [add (/ (* cnt (- cnt 1)) 2)])
            (loop (cdr keys) (+ total add)))))))
```

## Erlang

```erlang
-spec num_identical_pairs(Nums :: [integer()]) -> integer().
num_identical_pairs(Nums) ->
    Freq = lists:foldl(
        fun(N, Acc) ->
            maps:update_with(N, fun(C) -> C + 1 end, 1, Acc)
        end,
        #{},
        Nums),
    maps:fold(
        fun(_Key, Count, Sum) ->
            Sum + (Count * (Count - 1)) div 2
        end,
        0,
        Freq).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_identical_pairs(nums :: [integer]) :: integer
  def num_identical_pairs(nums) do
    nums
    |> Enum.reduce(%{}, fn x, acc -> Map.update(acc, x, 1, &(&1 + 1)) end)
    |> Enum.reduce(0, fn {_k, v}, sum -> sum + div(v * (v - 1), 2) end)
  end
end
```
