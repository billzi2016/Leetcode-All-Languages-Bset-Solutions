# 2191. Sort the Jumbled Numbers

## Cpp

```cpp
class Solution {
public:
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums) {
        int n = nums.size();
        vector<pair<long long,int>> v;
        v.reserve(n);
        for (int i = 0; i < n; ++i) {
            int x = nums[i];
            long long mapped;
            if (x == 0) {
                mapped = mapping[0];
            } else {
                long long res = 0, place = 1;
                while (x > 0) {
                    int d = x % 10;
                    res += (long long)mapping[d] * place;
                    place *= 10;
                    x /= 10;
                }
                mapped = res;
            }
            v.emplace_back(mapped, i);
        }
        stable_sort(v.begin(), v.end(),
                     [](const pair<long long,int>& a, const pair<long long,int>& b) {
                         if (a.first != b.first) return a.first < b.first;
                         return a.second < b.second;
                     });
        vector<int> ans;
        ans.reserve(n);
        for (auto& p : v) ans.push_back(nums[p.second]);
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public int[] sortJumbled(int[] mapping, int[] nums) {
        int n = nums.length;
        Integer[] idx = new Integer[n];
        int[] mapped = new int[n];

        for (int i = 0; i < n; i++) {
            idx[i] = i;
            int num = nums[i];
            if (num == 0) {
                mapped[i] = mapping[0];
            } else {
                long val = 0;
                int place = 1;
                while (num > 0) {
                    int d = num % 10;
                    val += mapping[d] * place;
                    place *= 10;
                    num /= 10;
                }
                mapped[i] = (int) val;
            }
        }

        Arrays.sort(idx, (a, b) -> {
            if (mapped[a] != mapped[b]) return Integer.compare(mapped[a], mapped[b]);
            return Integer.compare(a, b);
        });

        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = nums[idx[i]];
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        def mapped_value(num):
            if num == 0:
                return mapping[0]
            res = 0
            place = 1
            while num:
                digit = num % 10
                res += mapping[digit] * place
                place *= 10
                num //= 10
            return res

        pairs = [(mapped_value(num), idx) for idx, num in enumerate(nums)]
        pairs.sort(key=lambda x: x[0])  # stable sort keeps original order for equal keys
        return [nums[idx] for _, idx in pairs]
```

## Python3

```python
from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        transformed = []
        for idx, num in enumerate(nums):
            s = str(num)
            mapped_digits = [str(mapping[ord(c) - 48]) for c in s]
            mapped_num = int(''.join(mapped_digits))
            transformed.append((mapped_num, idx))
        transformed.sort(key=lambda x: x[0])
        return [nums[i] for _, i in transformed]
```

## C

```c
#include <stdlib.h>

typedef struct {
    int val;      // original number
    int mapped;   // mapped value
    int idx;      // original index
} Pair;

static int mapNumber(int num, const int *mapping) {
    if (num == 0) return mapping[0];
    long long res = 0;
    long long place = 1;
    while (num > 0) {
        int digit = num % 10;
        int mappedDigit = mapping[digit];
        res += (long long)mappedDigit * place;
        place *= 10;
        num /= 10;
    }
    return (int)res;
}

static int cmpPairs(const void *a, const void *b) {
    const Pair *p = (const Pair *)a;
    const Pair *q = (const Pair *)b;
    if (p->mapped != q->mapped)
        return p->mapped - q->mapped;
    return p->idx - q->idx;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortJumbled(int* mapping, int mappingSize, int* nums, int numsSize, int* returnSize) {
    (void)mappingSize; // unused
    Pair *arr = (Pair *)malloc(numsSize * sizeof(Pair));
    for (int i = 0; i < numsSize; ++i) {
        arr[i].val = nums[i];
        arr[i].mapped = mapNumber(nums[i], mapping);
        arr[i].idx = i;
    }

    qsort(arr, numsSize, sizeof(Pair), cmpPairs);

    int *result = (int *)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        result[i] = arr[i].val;
    }
    free(arr);
    *returnSize = numsSize;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] SortJumbled(int[] mapping, int[] nums)
    {
        int n = nums.Length;
        var pairs = new Tuple<int, int>[n];
        for (int i = 0; i < n; i++)
        {
            int mapped = MapNumber(nums[i], mapping);
            pairs[i] = Tuple.Create(mapped, i);
        }

        Array.Sort(pairs, (a, b) =>
        {
            int cmp = a.Item1.CompareTo(b.Item1);
            if (cmp != 0) return cmp;
            return a.Item2.CompareTo(b.Item2);
        });

        var result = new int[n];
        for (int i = 0; i < n; i++)
        {
            result[i] = nums[pairs[i].Item2];
        }
        return result;
    }

    private int MapNumber(int num, int[] mapping)
    {
        if (num == 0) return mapping[0];

        int res = 0;
        int place = 1;
        while (num > 0)
        {
            int digit = num % 10;
            int mappedDigit = mapping[digit];
            res += mappedDigit * place;
            place *= 10;
            num /= 10;
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} mapping
 * @param {number[]} nums
 * @return {number[]}
 */
var sortJumbled = function(mapping, nums) {
    const getMapped = (num) => {
        if (num === 0) return mapping[0];
        let mapped = 0;
        let place = 1;
        while (num > 0) {
            const digit = num % 10;
            mapped += mapping[digit] * place;
            place *= 10;
            num = Math.floor(num / 10);
        }
        return mapped;
    };
    
    const paired = nums.map((val, idx) => ({
        mapped: getMapped(val),
        idx: idx
    }));
    
    paired.sort((a, b) => {
        if (a.mapped !== b.mapped) return a.mapped - b.mapped;
        return a.idx - b.idx;
    });
    
    const result = new Array(nums.length);
    for (let i = 0; i < paired.length; ++i) {
        result[i] = nums[paired[i].idx];
    }
    return result;
};
```

## Typescript

```typescript
function sortJumbled(mapping: number[], nums: number[]): number[] {
    const transformed = nums.map((val, idx) => {
        const str = String(val);
        let mappedStr = '';
        for (let ch of str) {
            mappedStr += mapping[+ch];
        }
        const mappedVal = Number(mappedStr);
        return { mapped: mappedVal, idx, val };
    });

    transformed.sort((a, b) => {
        if (a.mapped !== b.mapped) return a.mapped - b.mapped;
        return a.idx - b.idx;
    });

    return transformed.map(item => item.val);
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $mapping
     * @param Integer[] $nums
     * @return Integer[]
     */
    function sortJumbled($mapping, $nums) {
        $pairs = [];
        foreach ($nums as $idx => $num) {
            $mapped = $this->mapValue($num, $mapping);
            $pairs[] = ['mapped' => $mapped, 'idx' => $idx];
        }
        usort($pairs, function($a, $b) {
            if ($a['mapped'] == $b['mapped']) {
                return $a['idx'] <=> $b['idx'];
            }
            return $a['mapped'] <=> $b['mapped'];
        });
        $result = [];
        foreach ($pairs as $p) {
            $result[] = $nums[$p['idx']];
        }
        return $result;
    }

    private function mapValue($num, $mapping) {
        $s = strval($num);
        $mappedStr = '';
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $digit = intval($s[$i]);
            $mappedStr .= $mapping[$digit];
        }
        return intval($mappedStr);
    }
}
```

## Swift

```swift
class Solution {
    func sortJumbled(_ mapping: [Int], _ nums: [Int]) -> [Int] {
        func mapNumber(_ num: Int) -> Int {
            if num == 0 { return mapping[0] }
            var n = num
            var result = 0
            var place = 1
            while n > 0 {
                let digit = n % 10
                result += mapping[digit] * place
                place *= 10
                n /= 10
            }
            return result
        }

        var paired: [(mapped: Int, idx: Int, original: Int)] = []
        paired.reserveCapacity(nums.count)
        for (i, num) in nums.enumerated() {
            let m = mapNumber(num)
            paired.append((mapped: m, idx: i, original: num))
        }

        paired.sort { a, b in
            if a.mapped != b.mapped {
                return a.mapped < b.mapped
            } else {
                return a.idx < b.idx
            }
        }

        var result = [Int]()
        result.reserveCapacity(paired.count)
        for p in paired {
            result.append(p.original)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun sortJumbled(mapping: IntArray, nums: IntArray): IntArray {
        val n = nums.size
        data class PairVal(val mapped: Int, val idx: Int)
        val arr = Array(n) { i -> PairVal(mapNumber(nums[i], mapping), i) }
        java.util.Arrays.sort(arr) { a, b ->
            if (a.mapped != b.mapped) a.mapped - b.mapped
            else a.idx - b.idx
        }
        val res = IntArray(n)
        for (i in 0 until n) {
            res[i] = nums[arr[i].idx]
        }
        return res
    }

    private fun mapNumber(num: Int, mapping: IntArray): Int {
        if (num == 0) return mapping[0]
        var n = num
        var place = 1
        var mapped = 0
        while (n > 0) {
            val d = n % 10
            mapped += mapping[d] * place
            place *= 10
            n /= 10
        }
        return mapped
    }
}
```

## Dart

```dart
class Solution {
  List<int> sortJumbled(List<int> mapping, List<int> nums) {
    int n = nums.length;
    List<_Item> items = List.generate(n, (i) {
      int mapped = _mapNumber(nums[i], mapping);
      return _Item(mapped, i, nums[i]);
    });
    items.sort((a, b) {
      if (a.mapped != b.mapped) return a.mapped.compareTo(b.mapped);
      return a.index.compareTo(b.index);
    });
    return items.map((e) => e.original).toList();
  }

  int _mapNumber(int num, List<int> mapping) {
    if (num == 0) {
      return mapping[0];
    }
    String s = num.toString();
    StringBuffer sb = StringBuffer();
    for (int i = 0; i < s.length; i++) {
      int digit = s.codeUnitAt(i) - 48;
      sb.write(mapping[digit]);
    }
    return int.parse(sb.toString());
  }
}

class _Item {
  final int mapped;
  final int index;
  final int original;

  _Item(this.mapped, this.index, this.original);
}
```

## Golang

```go
import "sort"

func sortJumbled(mapping []int, nums []int) []int {
	type pair struct {
		mapped int
		idx    int
	}
	pairs := make([]pair, len(nums))
	for i, v := range nums {
		pairs[i] = pair{mapNum(v, mapping), i}
	}
	sort.SliceStable(pairs, func(i, j int) bool {
		return pairs[i].mapped < pairs[j].mapped
	})
	res := make([]int, len(nums))
	for i, p := range pairs {
		res[i] = nums[p.idx]
	}
	return res
}

func mapNum(num int, mapping []int) int {
	if num == 0 {
		return mapping[0]
	}
	mapped := 0
	place := 1
	for num > 0 {
		d := num % 10
		mapped += mapping[d] * place
		place *= 10
		num /= 10
	}
	return mapped
}
```

## Ruby

```ruby
# @param {Integer[]} mapping
# @param {Integer[]} nums
# @return {Integer[]}
def sort_jumbled(mapping, nums)
  pairs = nums.each_with_index.map do |num, idx|
    if num == 0
      mapped = mapping[0]
    else
      temp = num
      place = 1
      mapped = 0
      while temp > 0
        digit = temp % 10
        mapped += mapping[digit] * place
        place *= 10
        temp /= 10
      end
    end
    [mapped, idx, num]
  end

  pairs.sort_by! { |m, i, _| [m, i] }
  pairs.map { |_, _, original| original }
end
```

## Scala

```scala
object Solution {
  def sortJumbled(mapping: Array[Int], nums: Array[Int]): Array[Int] = {
    def mappedValue(num: Int): Long = {
      if (num == 0) return mapping(0).toLong
      var n = num
      var res: Long = 0L
      var place: Long = 1L
      while (n > 0) {
        val d = n % 10
        val md = mapping(d)
        res += md * place
        place *= 10
        n /= 10
      }
      res
    }

    val indexed = nums.zipWithIndex
    val sorted = indexed.sortBy { case (value, idx) => (mappedValue(value), idx) }
    sorted.map(_._1)
  }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn sort_jumbled(mapping: Vec<i32>, nums: Vec<i32>) -> Vec<i32> {
        fn map_num(num: i32, mapping: &Vec<i32>) -> i64 {
            if num == 0 {
                return mapping[0] as i64;
            }
            let mut n = num;
            let mut place = 1i64;
            let mut res = 0i64;
            while n > 0 {
                let digit = (n % 10) as usize;
                let mapped_digit = mapping[digit] as i64;
                res += mapped_digit * place;
                place *= 10;
                n /= 10;
            }
            res
        }

        let mut pairs: Vec<(i64, usize)> = nums
            .iter()
            .enumerate()
            .map(|(i, &num)| (map_num(num, &mapping), i))
            .collect();

        pairs.sort_unstable_by(|a, b| {
            if a.0 == b.0 {
                a.1.cmp(&b.1)
            } else {
                a.0.cmp(&b.0)
            }
        });

        let mut result = Vec::with_capacity(nums.len());
        for (_, idx) in pairs {
            result.push(nums[idx]);
        }
        result
    }
}
```

## Racket

```racket
(define/contract (sort-jumbled mapping nums)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let ((mapping-vec (list->vector mapping)))
    (define (map-num n)
      (let* ((s (number->string n))
             (mapped-str
              (list->string
               (map (lambda (c)
                      (let* ((digit (- (char->integer c) (char->integer #\0)))
                             (m (vector-ref mapping-vec digit)))
                        (integer->char (+ (char->integer #\0) m))))
                    (string->list s)))))
        (string->number mapped-str)))
    (define pairs
      (let loop ((lst nums) (idx 0) (acc '()))
        (if (null? lst)
            (reverse acc)
            (let* ((num (car lst))
                   (mapped (map-num num))
                   (pair (list mapped idx num)))
              (loop (cdr lst) (add1 idx) (cons pair acc))))))
    (define sorted
      (sort pairs
            (lambda (a b)
              (let ((ma (first a))
                    (mb (first b))
                    (ia (second a))
                    (ib (second b)))
                (if (< ma mb) #t
                    (if (> ma mb) #f
                        (< ia ib)))))))
    (map third sorted)))
```

## Erlang

```erlang
-spec sort_jumbled([integer()], [integer()]) -> [integer()].
sort_jumbled(Mapping, Nums) ->
    MappingTuple = list_to_tuple(Mapping),
    Indexed = lists:zip(Nums, lists:seq(0, length(Nums) - 1)),
    Tuples = [
        begin
            {Num, Idx} = Pair,
            Mapped = map_number(Num, MappingTuple),
            {Mapped, Idx, Num}
        end
     || Pair <- Indexed],
    Sorted = lists:keysort(1, Tuples),
    [Num || {_, _, Num} <- Sorted].

map_number(N, Tuple) ->
    Digits = integer_to_list(N),
    MappedChars = [$0 + element(Char - $0 + 1, Tuple) || Char <- Digits],
    list_to_integer(MappedChars).
```

## Elixir

```elixir
defmodule Solution do
  @spec sort_jumbled(mapping :: [integer], nums :: [integer]) :: [integer]
  def sort_jumbled(mapping, nums) do
    digit_map = mapping |> Enum.with_index() |> Enum.map(fn {v, i} -> {i, v} end) |> Map.new()

    transformed =
      nums
      |> Enum.with_index()
      |> Enum.map(fn {num, idx} ->
        mapped = map_number(num, digit_map)
        {mapped, idx, num}
      end)

    transformed
    |> Enum.sort_by(fn {mapped, idx, _} -> {mapped, idx} end)
    |> Enum.map(fn {_m, _i, original} -> original end)
  end

  defp map_number(0, digit_map), do: Map.fetch!(digit_map, 0)

  defp map_number(num, digit_map) when num > 0 do
    do_map(num, digit_map, 0, 1)
  end

  defp do_map(0, _digit_map, acc, _place), do: acc

  defp do_map(n, digit_map, acc, place) do
    digit = rem(n, 10)
    mapped_digit = Map.fetch!(digit_map, digit)
    new_acc = acc + mapped_digit * place
    do_map(div(n, 10), digit_map, new_acc, place * 10)
  end
end
```
