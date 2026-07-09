# 0384. Shuffle an Array

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
    vector<int> original;
    mt19937 rng;
public:
    Solution(vector<int>& nums) : original(nums), rng(random_device{}()) {}
    
    vector<int> reset() {
        return original;
    }
    
    vector<int> shuffle() {
        vector<int> arr = original;
        int n = arr.size();
        for (int i = n - 1; i > 0; --i) {
            uniform_int_distribution<int> dist(0, i);
            int j = dist(rng);
            swap(arr[i], arr[j]);
        }
        return arr;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */
```

## Java

```java
class Solution {
    private final int[] original;
    private final java.util.Random rand;

    public Solution(int[] nums) {
        this.original = nums.clone();
        this.rand = new java.util.Random();
    }

    public int[] reset() {
        return original.clone();
    }

    public int[] shuffle() {
        int[] arr = original.clone();
        for (int i = 0; i < arr.length; i++) {
            int j = i + rand.nextInt(arr.length - i);
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        return arr;
    }
}
```

## Python

```python
import random

class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = list(nums)

    def reset(self):
        """
        :rtype: List[int]
        """
        return list(self.original)

    def shuffle(self):
        """
        :rtype: List[int]
        """
        arr = list(self.original)
        n = len(arr)
        for i in range(n):
            j = random.randint(i, n - 1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
```

## Python3

```python
import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        self.original = nums[:]

    def reset(self) -> List[int]:
        return self.original[:]

    def shuffle(self) -> List[int]:
        arr = self.original[:]
        n = len(arr)
        for i in range(n):
            j = random.randint(i, n - 1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct {
    int *original;
    int *array;
    int size;
} Solution;

Solution* solutionCreate(int* nums, int numsSize) {
    Solution *obj = (Solution *)malloc(sizeof(Solution));
    obj->size = numsSize;
    obj->original = (int *)malloc(numsSize * sizeof(int));
    memcpy(obj->original, nums, numsSize * sizeof(int));
    obj->array = (int *)malloc(numsSize * sizeof(int));
    memcpy(obj->array, nums, numsSize * sizeof(int));
    srand((unsigned)time(NULL));
    return obj;
}

int* solutionReset(Solution* obj, int* retSize) {
    *retSize = obj->size;
    memcpy(obj->array, obj->original, obj->size * sizeof(int));
    int *res = (int *)malloc(obj->size * sizeof(int));
    memcpy(res, obj->original, obj->size * sizeof(int));
    return res;
}

int* solutionShuffle(Solution* obj, int* retSize) {
    *retSize = obj->size;
    int *res = (int *)malloc(obj->size * sizeof(int));
    memcpy(res, obj->original, obj->size * sizeof(int));
    for (int i = 0; i < obj->size; ++i) {
        int j = i + rand() % (obj->size - i);
        int tmp = res[i];
        res[i] = res[j];
        res[j] = tmp;
    }
    memcpy(obj->array, res, obj->size * sizeof(int));
    return res;
}

void solutionFree(Solution* obj) {
    if (!obj) return;
    free(obj->original);
    free(obj->array);
    free(obj);
}
```

## Csharp

```csharp
public class Solution {
    private readonly int[] _original;
    private readonly Random _rand;

    public Solution(int[] nums) {
        _original = (int[])nums.Clone();
        _rand = new Random();
    }

    public int[] Reset() {
        return (int[])_original.Clone();
    }

    public int[] Shuffle() {
        int n = _original.Length;
        int[] shuffled = (int[])_original.Clone();
        for (int i = 0; i < n; i++) {
            int j = _rand.Next(i, n);
            int temp = shuffled[i];
            shuffled[i] = shuffled[j];
            shuffled[j] = temp;
        }
        return shuffled;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 */
var Solution = function(nums) {
    // Store a copy of the original array for reset and shuffling.
    this.original = nums.slice();
};

/**
 * @return {number[]}
 */
Solution.prototype.reset = function() {
    // Return a fresh copy of the original configuration.
    return this.original.slice();
};

/**
 * @return {number[]}
 */
Solution.prototype.shuffle = function() {
    const arr = this.original.slice(); // work on a copy
    for (let i = 0; i < arr.length; i++) {
        // Pick a random index from i (inclusive) to end (exclusive)
        const j = i + Math.floor(Math.random() * (arr.length - i));
        // Swap elements at indices i and j
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(nums)
 * var param_1 = obj.reset()
 * var param_2 = obj.shuffle()
 */
```

## Typescript

```typescript
class Solution {
    private original: number[];
    constructor(nums: number[]) {
        this.original = nums.slice();
    }

    reset(): number[] {
        return this.original.slice();
    }

    shuffle(): number[] {
        const arr = this.original.slice();
        for (let i = 0; i < arr.length; i++) {
            const j = i + Math.floor(Math.random() * (arr.length - i));
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
        return arr;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(nums)
 * var param_1 = obj.reset()
 * var param_2 = obj.shuffle()
 */
```

## Php

```php
class Solution {
    /**
     * @var int[]
     */
    private $original = [];

    /**
     * @param int[] $nums
     */
    function __construct($nums) {
        $this->original = $nums;
    }

    /**
     * @return int[]
     */
    function reset() {
        // Return a copy of the original array
        return $this->original;
    }

    /**
     * @return int[]
     */
    function shuffle() {
        $arr = $this->original;
        $n = count($arr);
        for ($i = 0; $i < $n; $i++) {
            // mt_rand is inclusive on both ends
            $j = mt_rand($i, $n - 1);
            $tmp = $arr[$i];
            $arr[$i] = $arr[$j];
            $arr[$j] = $tmp;
        }
        return $arr;
    }
}
```

## Swift

```swift
class Solution {
    private let original: [Int]
    
    init(_ nums: [Int]) {
        self.original = nums
    }
    
    func reset() -> [Int] {
        return original
    }
    
    func shuffle() -> [Int] {
        var shuffled = original
        let n = shuffled.count
        for i in 0..<n {
            let j = Int.random(in: i..<n)
            if i != j {
                shuffled.swapAt(i, j)
            }
        }
        return shuffled
    }
}
```

## Kotlin

```kotlin
class Solution(nums: IntArray) {
    private val original = nums.clone()
    private val rand = java.util.Random()

    fun reset(): IntArray {
        return original.clone()
    }

    fun shuffle(): IntArray {
        val arr = original.clone()
        for (i in arr.indices) {
            val j = i + rand.nextInt(arr.size - i)
            val tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
        }
        return arr
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  final List<int> _original;
  final Random _rand = Random();

  Solution(List<int> nums) : _original = List.from(nums);

  List<int> reset() {
    return List.from(_original);
  }

  List<int> shuffle() {
    List<int> arr = List.from(_original);
    for (int i = arr.length - 1; i > 0; i--) {
      int j = _rand.nextInt(i + 1);
      int temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;
    }
    return arr;
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = Solution(nums);
 * List<int> param1 = obj.reset();
 * List<int> param2 = obj.shuffle();
 */
```

## Golang

```go
package main

import (
	"math/rand"
	"time"
)

func init() {
	rand.Seed(time.Now().UnixNano())
}

type Solution struct {
	original []int
	shuffled []int
}

func Constructor(nums []int) Solution {
	orig := make([]int, len(nums))
	copy(orig, nums)
	shuf := make([]int, len(nums))
	copy(shuf, nums)
	return Solution{original: orig, shuffled: shuf}
}

func (this *Solution) Reset() []int {
	this.shuffled = make([]int, len(this.original))
	copy(this.shuffled, this.original)
	return this.shuffled
}

func (this *Solution) Shuffle() []int {
	n := len(this.original)
	shuffled := make([]int, n)
	copy(shuffled, this.original)
	for i := n - 1; i > 0; i-- {
		j := rand.Intn(i + 1)
		shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
	}
	this.shuffled = shuffled
	return shuffled
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.Reset();
 * param_2 := obj.Shuffle();
 */
```

## Ruby

```ruby
class Solution
  # @param {Integer[]} nums
  def initialize(nums)
    @original = nums.clone
  end

  # @return {Integer[]}
  def reset
    @original.clone
  end

  # @return {Integer[]}
  def shuffle
    arr = @original.clone
    n = arr.length
    (0...n).each do |i|
      j = rand(i...n)
      arr[i], arr[j] = arr[j], arr[i]
    end
    arr
  end
end
```

## Scala

```scala
class Solution(_nums: Array[Int]) {
  private val original: Array[Int] = _nums.clone()
  private val rand = new scala.util.Random()

  def reset(): Array[Int] = original.clone()

  def shuffle(): Array[Int] = {
    val arr = original.clone()
    for (i <- arr.length - 1 to 1 by -1) {
      val j = rand.nextInt(i + 1)
      val tmp = arr(i)
      arr(i) = arr(j)
      arr(j) = tmp
    }
    arr
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * val obj = new Solution(nums)
 * val param_1 = obj.reset()
 * val param_2 = obj.shuffle()
 */
```

## Rust

```rust
use rand::Rng;

struct Solution {
    original: Vec<i32>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Solution {

    fn new(nums: Vec<i32>) -> Self {
        Solution { original: nums }
    }
    
    fn reset(&self) -> Vec<i32> {
        self.original.clone()
    }
    
    fn shuffle(&self) -> Vec<i32> {
        let mut rng = rand::thread_rng();
        let mut arr = self.original.clone();
        let n = arr.len();
        for i in 0..n {
            let j = rng.gen_range(i..n);
            arr.swap(i, j);
        }
        arr
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(nums);
 * let ret_1: Vec<i32> = obj.reset();
 * let ret_2: Vec<i32> = obj.shuffle();
 */
```

## Racket

```racket
(define solution%
  (class object%
    (init-field nums)
    (super-new)

    (define orig (list->vector nums))
    (define cur (make-vector (vector-length orig)))

    (define/public (reset)
      (let ([len (vector-length orig)])
        (for ([i (in-range len)])
          (vector-set! cur i (vector-ref orig i))))
      (vector->list cur))

    (define/public (shuffle)
      (let* ([len (vector-length orig)]
             [v (make-vector len)])
        (for ([i (in-range len)])
          (vector-set! v i (vector-ref orig i)))
        (for ([i (in-range (sub1 len) 0 -1)])
          (let* ([j (+ i (random (- len i)))])
            (let ([temp (vector-ref v i)])
              (vector-set! v i (vector-ref v j))
              (vector-set! v j temp))))
        (vector->list v)))))
```

## Erlang

```erlang
-spec solution_init_(Nums :: [integer()]) -> any().
solution_init_(Nums) ->
    Seed = {erlang:monotonic_time(), erlang:unique_integer([positive]), erlang:self()},
    rand:seed(exsplus, Seed),
    put(original, Nums),
    put(current, Nums).

-spec solution_reset() -> [integer()].
solution_reset() ->
    Orig = get(original),
    put(current, Orig),
    Orig.

-spec solution_shuffle() -> [integer()].
solution_shuffle() ->
    Curr = get(current),
    Shuffled = fisher_yates(Curr),
    put(current, Shuffled),
    Shuffled.

fisher_yates(List) when is_list(List) ->
    Tuple = list_to_tuple(List),
    Len = tuple_size(Tuple),
    ShuffledTuple = shuffle_tuple(Tuple, Len),
    tuple_to_list(ShuffledTuple).

shuffle_tuple(Tuple, I) when I =< 1 -> Tuple;
shuffle_tuple(Tuple, I) ->
    J = rand:uniform(I),
    NewTuple =
        if
            I == J -> Tuple;
            true ->
                ElemI = element(I, Tuple),
                ElemJ = element(J, Tuple),
                T1 = setelement(I, Tuple, ElemJ),
                setelement(J, T1, ElemI)
        end,
    shuffle_tuple(NewTuple, I - 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec init_(nums :: [integer]) :: any
  def init_(nums) do
    Process.put(:solution_original, nums)
    :ok
  end

  @spec reset() :: [integer]
  def reset() do
    Process.get(:solution_original)
  end

  @spec shuffle() :: [integer]
  def shuffle() do
    original = Process.get(:solution_original) || []
    list = Enum.to_list(original)
    n = length(list)

    arr =
      :array.from_list(list)

    shuffled_arr =
      Enum.reduce(0..(n - 1), arr, fn i, acc ->
        j = :rand.uniform(n - i) - 1 + i
        vi = :array.get(i, acc)
        vj = :array.get(j, acc)
        acc |> :array.set(i, vj) |> :array.set(j, vi)
      end)

    :array.to_list(shuffled_arr)
  end
end
```
