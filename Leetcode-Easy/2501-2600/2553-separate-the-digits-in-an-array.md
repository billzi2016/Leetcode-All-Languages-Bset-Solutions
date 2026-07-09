# 2553. Separate the Digits in an Array

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> separateDigits(vector<int>& nums) {
        vector<int> answer;
        answer.reserve(nums.size() * 6); // max digits per number is up to 6 (since 10^5)
        for (int num : nums) {
            string s = to_string(num);
            for (char c : s) {
                answer.push_back(c - '0');
            }
        }
        return answer;
    }
};
```

## Java

```java
class Solution {
    public int[] separateDigits(int[] nums) {
        java.util.List<Integer> list = new java.util.ArrayList<>();
        for (int num : nums) {
            char[] chars = Integer.toString(num).toCharArray();
            for (char c : chars) {
                list.add(c - '0');
            }
        }
        int[] result = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            result[i] = list.get(i);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums:
            for ch in str(num):
                ans.append(int(ch))
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            for ch in str(num):
                ans.append(int(ch))
        return ans
```

## C

```c
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* separateDigits(int* nums, int numsSize, int* returnSize) {
    int total = 0;
    for (int i = 0; i < numsSize; ++i) {
        int x = nums[i];
        if (x == 0) {
            total += 1;
        } else {
            while (x > 0) {
                total++;
                x /= 10;
            }
        }
    }

    int* result = (int*)malloc(total * sizeof(int));
    *returnSize = total;

    int idx = 0;
    for (int i = 0; i < numsSize; ++i) {
        int digits[12];
        int cnt = 0;
        int x = nums[i];
        if (x == 0) {
            digits[cnt++] = 0;
        } else {
            while (x > 0) {
                digits[cnt++] = x % 10;
                x /= 10;
            }
        }
        for (int j = cnt - 1; j >= 0; --j) {
            result[idx++] = digits[j];
        }
    }

    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int[] SeparateDigits(int[] nums) {
        var result = new List<int>();
        foreach (var num in nums) {
            foreach (var ch in num.ToString()) {
                result.Add(ch - '0');
            }
        }
        return result.ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var separateDigits = function(nums) {
    const ans = [];
    for (const num of nums) {
        const digits = String(num).split('');
        for (const d of digits) {
            ans.push(d.charCodeAt(0) - 48); // faster than Number(d)
        }
    }
    return ans;
};
```

## Typescript

```typescript
function separateDigits(nums: number[]): number[] {
    const result: number[] = [];
    for (const num of nums) {
        const str = num.toString();
        for (let i = 0; i < str.length; i++) {
            result.push(str.charCodeAt(i) - 48);
        }
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function separateDigits($nums) {
        $answer = [];
        foreach ($nums as $num) {
            foreach (str_split((string)$num) as $ch) {
                $answer[] = intval($ch);
            }
        }
        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func separateDigits(_ nums: [Int]) -> [Int] {
        var result = [Int]()
        for num in nums {
            for ch in String(num) {
                if let digit = ch.wholeNumberValue {
                    result.append(digit)
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
    fun separateDigits(nums: IntArray): IntArray {
        val totalSize = nums.sumOf { it.toString().length }
        val result = IntArray(totalSize)
        var idx = 0
        for (num in nums) {
            val s = num.toString()
            for (ch in s) {
                result[idx++] = ch - '0'
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> separateDigits(List<int> nums) {
    List<int> answer = [];
    for (int num in nums) {
      String s = num.toString();
      for (int i = 0; i < s.length; i++) {
        answer.add(int.parse(s[i]));
      }
    }
    return answer;
  }
}
```

## Golang

```go
package main

import "strconv"

func separateDigits(nums []int) []int {
	var ans []int
	for _, num := range nums {
		s := strconv.Itoa(num)
		for i := 0; i < len(s); i++ {
			ans = append(ans, int(s[i]-'0'))
		}
	}
	return ans
}
```

## Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def separate_digits(nums)
  nums.flat_map { |num| num.to_s.chars.map(&:to_i) }
end
```

## Scala

```scala
object Solution {
    def separateDigits(nums: Array[Int]): Array[Int] = {
        nums.flatMap(num => num.toString.map(_.asDigit))
    }
}
```

## Rust

```rust
impl Solution {
    pub fn separate_digits(nums: Vec<i32>) -> Vec<i32> {
        let mut answer = Vec::new();
        for num in nums {
            for ch in num.to_string().chars() {
                answer.push(ch.to_digit(10).unwrap() as i32);
            }
        }
        answer
    }
}
```

## Racket

```racket
(define/contract (separate-digits nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (apply append
         (map (lambda (n)
                (map (lambda (c)
                       (- (char->integer c) (char->integer #\0)))
                     (string->list (number->string n))))
              nums)))
```

## Erlang

```erlang
-spec separate_digits(Nums :: [integer()]) -> [integer()].
separate_digits(Nums) ->
    lists:flatmap(
        fun(N) ->
            [C - $0 || C <- integer_to_list(N)]
        end,
        Nums
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec separate_digits(nums :: [integer]) :: [integer]
  def separate_digits(nums) do
    Enum.flat_map(nums, &Integer.digits/1)
  end
end
```
