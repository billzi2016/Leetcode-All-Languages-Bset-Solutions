# 0398. Random Pick Index

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
    unordered_map<int, vector<int>> idxMap;
    mt19937 rng;
public:
    Solution(vector<int>& nums) : rng(random_device{}()) {
        for (int i = 0; i < (int)nums.size(); ++i) {
            idxMap[nums[i]].push_back(i);
        }
    }
    
    int pick(int target) {
        const vector<int>& v = idxMap[target];
        uniform_int_distribution<int> dist(0, (int)v.size() - 1);
        return v[dist(rng)];
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 */
```

## Java

```java
import java.util.*;

class Solution {
    private final Map<Integer, List<Integer>> indexMap;
    private final Random random;

    public Solution(int[] nums) {
        indexMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            indexMap.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }
        random = new Random();
    }

    public int pick(int target) {
        List<Integer> indices = indexMap.get(target);
        return indices.get(random.nextInt(indices.size()));
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */
```

## Python

```python
import random

class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.idx_map = {}
        for i, num in enumerate(nums):
            if num not in self.idx_map:
                self.idx_map[num] = []
            self.idx_map[num].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.idx_map[target])
```

## Python3

```python
import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        self.idx_map = {}
        for i, num in enumerate(nums):
            if num not in self.idx_map:
                self.idx_map[num] = []
            self.idx_map[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.idx_map[target])
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct {
    int *nums;
    int size;
} Solution;

Solution* solutionCreate(int* nums, int numsSize) {
    Solution* obj = (Solution*)malloc(sizeof(Solution));
    obj->size = numsSize;
    obj->nums = (int*)malloc(numsSize * sizeof(int));
    memcpy(obj->nums, nums, numsSize * sizeof(int));
    static int seeded = 0;
    if (!seeded) {
        srand((unsigned)time(NULL));
        seeded = 1;
    }
    return obj;
}

int solutionPick(Solution* obj, int target) {
    int count = 0;
    int result = -1;
    for (int i = 0; i < obj->size; ++i) {
        if (obj->nums[i] == target) {
            ++count;
            if (rand() % count == 0) {
                result = i;
            }
        }
    }
    return result;
}

void solutionFree(Solution* obj) {
    if (!obj) return;
    free(obj->nums);
    free(obj);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private readonly Dictionary<int, List<int>> _indices;
    private readonly Random _rand;

    public Solution(int[] nums) {
        _indices = new Dictionary<int, List<int>>();
        for (int i = 0; i < nums.Length; i++) {
            int val = nums[i];
            if (!_indices.TryGetValue(val, out var list)) {
                list = new List<int>();
                _indices[val] = list;
            }
            list.Add(i);
        }
        _rand = new Random();
    }

    public int Pick(int target) {
        var list = _indices[target];
        return list[_rand.Next(list.Count)];
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 */
var Solution = function(nums) {
    this.idxMap = new Map();
    for (let i = 0; i < nums.length; i++) {
        const val = nums[i];
        if (!this.idxMap.has(val)) {
            this.idxMap.set(val, []);
        }
        this.idxMap.get(val).push(i);
    }
};

/** 
 * @param {number} target
 * @return {number}
 */
Solution.prototype.pick = function(target) {
    const arr = this.idxMap.get(target);
    const randIdx = Math.floor(Math.random() * arr.length);
    return arr[randIdx];
};
```

## Typescript

```typescript
class Solution {
    private indicesMap: Map<number, number[]>;

    constructor(nums: number[]) {
        this.indicesMap = new Map();
        for (let i = 0; i < nums.length; i++) {
            const val = nums[i];
            if (!this.indicesMap.has(val)) {
                this.indicesMap.set(val, []);
            }
            this.indicesMap.get(val)!.push(i);
        }
    }

    pick(target: number): number {
        const arr = this.indicesMap.get(target)!;
        const idx = Math.floor(Math.random() * arr.length);
        return arr[idx];
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(nums)
 * var param_1 = obj.pick(target)
 */
```

## Php

```php
class Solution {
    private $map;

    /**
     * @param Integer[] $nums
     */
    function __construct($nums) {
        $this->map = [];
        foreach ($nums as $i => $num) {
            if (!isset($this->map[$num])) {
                $this->map[$num] = [];
            }
            $this->map[$num][] = $i;
        }
    }

    /**
     * @param Integer $target
     * @return Integer
     */
    function pick($target) {
        $list = $this->map[$target];
        $randIdx = mt_rand(0, count($list) - 1);
        return $list[$randIdx];
    }
}
```

## Swift

```swift
class Solution {
    private var indicesMap: [Int: [Int]] = [:]

    init(_ nums: [Int]) {
        for (i, num) in nums.enumerated() {
            indicesMap[num, default: []].append(i)
        }
    }

    func pick(_ target: Int) -> Int {
        let arr = indicesMap[target]!
        let randomIdx = Int.random(in: 0..<arr.count)
        return arr[randomIdx]
    }
}
```

## Kotlin

```kotlin
import java.util.concurrent.ThreadLocalRandom

class Solution(nums: IntArray) {
    private val idxMap = HashMap<Int, IntArray>()

    init {
        val temp = HashMap<Int, MutableList<Int>>()
        for (i in nums.indices) {
            temp.computeIfAbsent(nums[i]) { mutableListOf() }.add(i)
        }
        for ((k, v) in temp) {
            idxMap[k] = v.toIntArray()
        }
    }

    fun pick(target: Int): Int {
        val arr = idxMap[target]!!
        return arr[ThreadLocalRandom.current().nextInt(arr.size)]
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = Solution(nums)
 * var param_1 = obj.pick(target)
 */
```

## Dart

```dart
import 'dart:math';

class Solution {
  final Map<int, List<int>> _indices = {};
  final Random _rand = Random();

  Solution(List<int> nums) {
    for (int i = 0; i < nums.length; i++) {
      _indices.putIfAbsent(nums[i], () => []).add(i);
    }
  }

  int pick(int target) {
    List<int> list = _indices[target]!;
    return list[_rand.nextInt(list.length)];
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = Solution(nums);
 * int param1 = obj.pick(target);
 */
```

## Golang

```go
import (
	"math/rand"
	"time"
)

type Solution struct {
	idxMap map[int][]int
}

func Constructor(nums []int) Solution {
	m := make(map[int][]int)
	for i, v := range nums {
		m[v] = append(m[v], i)
	}
	rand.Seed(time.Now().UnixNano())
	return Solution{idxMap: m}
}

func (this *Solution) Pick(target int) int {
	indices := this.idxMap[target]
	return indices[rand.Intn(len(indices))]
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.Pick(target);
 */
```

## Ruby

```ruby
class Solution
  def initialize(nums)
    @indices = Hash.new { |h, k| h[k] = [] }
    nums.each_with_index do |num, i|
      @indices[num] << i
    end
  end

  def pick(target)
    arr = @indices[target]
    arr[rand(arr.length)]
  end
end
```

## Scala

```scala
import scala.collection.mutable.{Map, ArrayBuffer}
import scala.util.Random

class Solution(_nums: Array[Int]) {
  private val idxMap: Map[Int, ArrayBuffer[Int]] = Map()
  _nums.zipWithIndex.foreach { case (num, i) =>
    idxMap.getOrElseUpdate(num, ArrayBuffer()).append(i)
  }
  private val rand = new Random()

  def pick(target: Int): Int = {
    val indices = idxMap(target)
    indices(rand.nextInt(indices.length))
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * val obj = new Solution(nums)
 * val param_1 = obj.pick(target)
 */
```

## Rust

```rust
use std::collections::HashMap;
use rand::Rng;

struct Solution {
    map: HashMap<i32, Vec<usize>>,
}

impl Solution {
    fn new(nums: Vec<i32>) -> Self {
        let mut map = HashMap::new();
        for (i, v) in nums.iter().enumerate() {
            map.entry(*v).or_insert_with(Vec::new).push(i);
        }
        Solution { map }
    }

    fn pick(&self, target: i32) -> i32 {
        let indices = self.map.get(&target).unwrap();
        let mut rng = rand::thread_rng();
        let idx = rng.gen_range(0..indices.len());
        indices[idx] as i32
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(nums);
 * let ret_1: i32 = obj.pick(target);
 */
```

## Racket

```racket
(define solution%
  (class object%
    (super-new)
    
    ; nums : (listof exact-integer?)
    (init-field
      nums)
    
    ; internal map from value to list of indices
    (define map (make-hash))
    
    ; build the map when the object is created
    (let loop ([i 0] [len (length nums)])
      (when (< i len)
        (let* ([v (list-ref nums i)]
               [old (hash-ref map v null)])
          (hash-set! map v (cons i old))
          (loop (+ i 1) len))))
    
    ; pick : exact-integer? -> exact-integer?
    (define/public (pick target)
      (let* ([indices (hash-ref map target)]
             [n (length indices)]
             [rand-idx (random n)])
        (list-ref indices rand-idx)))))
```

## Erlang

```erlang
-module(solution).
-export([solution_init_/1, solution_pick/1]).

-spec solution_init_(Nums :: [integer()]) -> any().
solution_init_(Nums) ->
    put(nums, Nums),
    ok.

-spec solution_pick(Target :: integer()) -> integer().
solution_pick(Target) ->
    List = get(nums),
    {_, Index} = lists:foldl(
        fun({Val, Idx}, {Count, Res}) ->
            if Val == Target ->
                    NewCount = Count + 1,
                    case rand:uniform(NewCount) of
                        1 -> {NewCount, Idx};
                        _ -> {NewCount, Res}
                    end;
               true ->
                    {Count, Res}
            end
        end,
        {0, -1},
        lists:zip(List, lists:seq(0, length(List) - 1))
    ),
    Index.
```

## Elixir

```elixir
defmodule Solution do
  @spec init_(nums :: [integer]) :: any
  def init_(nums) do
    Process.put(:random_pick_nums, nums)
  end

  @spec pick(target :: integer) :: integer
  def pick(target) do
    nums = Process.get(:random_pick_nums)

    indices =
      for {value, idx} <- Enum.with_index(nums), value == target, do: idx

    random_idx = :rand.uniform(length(indices)) - 1
    Enum.at(indices, random_idx)
  end
end
```
