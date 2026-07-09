# 1237. Find Positive Integer Solution for a Given Equation

## Cpp

```cpp
/*
 * // This is the custom function interface.
 * // You should not implement it, or speculate about its implementation
 * class CustomFunction {
 * public:
 *     // Returns f(x, y) for any given positive integers x and y.
 *     // Note that f(x, y) is increasing with respect to both x and y.
 *     // i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
 *     int f(int x, int y);
 * };
 */

class Solution {
public:
    vector<vector<int>> findSolution(CustomFunction& customfunction, int z) {
        const int MAX = 1000;
        vector<vector<int>> ans;
        int x = 1, y = MAX;
        while (x <= MAX && y >= 1) {
            int val = customfunction.f(x, y);
            if (val == z) {
                ans.push_back({x, y});
                ++x;
                --y;
            } else if (val < z) {
                ++x;
            } else { // val > z
                --y;
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> findSolution(CustomFunction customfunction, int z) {
        List<List<Integer>> result = new ArrayList<>();
        int x = 1;
        int y = 1000; // maximum possible per constraints
        while (x <= 1000 && y >= 1) {
            int val = customfunction.f(x, y);
            if (val == z) {
                result.add(Arrays.asList(x, y));
                x++;
                y--;
            } else if (val < z) {
                x++; // need larger value
            } else { // val > z
                y--; // need smaller value
            }
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type customfunction: CustomFunction
        :type z: int
        :rtype: List[List[int]]
        """
        res = []
        x, y = 1, 1000
        while x <= 1000 and y >= 1:
            val = customfunction.f(x, y)
            if val == z:
                res.append([x, y])
                x += 1
                y -= 1
            elif val < z:
                x += 1
            else:  # val > z
                y -= 1
        return res
```

## Python3

```python
from typing import List

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        x, y = 1, 1000
        while x <= 1000 and y >= 1:
            val = customfunction.f(x, y)
            if val == z:
                res.append([x, y])
                x += 1
                y -= 1
            elif val < z:
                x += 1
            else:  # val > z
                y -= 1
        return res
```

## C

```c
#include <stdlib.h>

/*
 * // This is the definition for customFunction API.
 * // You should not implement it, or speculate about its implementation
 *
 * // Returns f(x, y) for any given positive integers x and y.
 * // Note that f(x, y) is increasing with respect to both x and y.
 * // i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
 */

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** findSolution(int (*customFunction)(int, int), int z, int* returnSize, int*** returnColumnSizes) {
    const int MAX_VAL = 1000;
    int x = 1, y = MAX_VAL;
    int capacity = 1024;
    int **result = (int **)malloc(capacity * sizeof(int *));
    int count = 0;

    while (x <= MAX_VAL && y >= 1) {
        int val = customFunction(x, y);
        if (val == z) {
            if (count == capacity) {
                capacity <<= 1;
                result = (int **)realloc(result, capacity * sizeof(int *));
            }
            result[count] = (int *)malloc(2 * sizeof(int));
            result[count][0] = x;
            result[count][1] = y;
            ++count;
            ++x;
            --y;
        } else if (val < z) {
            ++x;
        } else { // val > z
            --y;
        }
    }

    *returnSize = count;
    *returnColumnSizes = (int **)malloc(count * sizeof(int *));
    for (int i = 0; i < count; ++i) {
        (*returnColumnSizes)[i] = (int *)malloc(sizeof(int));
        (*returnColumnSizes)[i][0] = 2;
    }

    return result;
}
```

## Csharp

```csharp
/*
 * // This is the custom function interface.
 * // You should not implement it, or speculate about its implementation
 * public class CustomFunction {
 *     // Returns f(x, y) for any given positive integers x and y.
 *     // Note that f(x, y) is increasing with respect to both x and y.
 *     // i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
 *     public int f(int x, int y);
 * };
 */

public class Solution {
    public IList<IList<int>> FindSolution(CustomFunction customfunction, int z) {
        var result = new List<IList<int>>();
        int x = 1;
        int y = 1000; // upper bound per problem constraints
        while (x <= 1000 && y >= 1) {
            int val = customfunction.f(x, y);
            if (val == z) {
                result.Add(new List<int> { x, y });
                x++;
                y--;
            } else if (val < z) {
                x++; // need larger value
            } else {
                y--; // need smaller value
            }
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {CustomFunction} customfunction
 * @param {integer} z
 * @return {integer[][]}
 */
var findSolution = function(customfunction, z) {
    const result = [];
    let x = 1;
    let y = 1000; // upper bound as per constraints
    
    while (x <= 1000 && y >= 1) {
        const val = customfunction.f(x, y);
        if (val === z) {
            result.push([x, y]);
            x++;
            y--;
        } else if (val < z) {
            x++;
        } else { // val > z
            y--;
        }
    }
    
    return result;
};
```

## Typescript

```typescript
/**
 * // This is the CustomFunction's API interface.
 * // You should not implement it, or speculate about its implementation
 * class CustomFunction {
 *     f(x: number, y: number): number {}
 * }
 */

function findSolution(customfunction: CustomFunction, z: number): number[][] {
    const result: number[][] = [];
    let x = 1;
    let y = 1000; // upper bound as per constraints

    while (x <= 1000 && y >= 1) {
        const val = customfunction.f(x, y);
        if (val === z) {
            result.push([x, y]);
            x++;
            y--;
        } else if (val < z) {
            x++;
        } else { // val > z
            y--;
        }
    }

    return result;
}
```

## Php

```php
/*
 * // This is the custom function interface.
 * // You should not implement it, or speculate about its implementation
 * class CustomFunction {
 *     // Returns f(x, y) for any given positive integers x and y.
 *     // Note that f(x, y) is increasing with respect to both x and y.
 *     // i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
 *     public function f($x, $y){}
 * };
 */

class Solution {
    /**
     * @param CustomFunction $customfunction
     * @param Integer $n
     * @return Integer[][]
     */
    function findSolution($customfunction, $n) {
        $result = [];
        $x = 1;
        $y = 1000; // maximum possible value per constraints
        
        while ($x <= 1000 && $y >= 1) {
            $val = $customfunction->f($x, $y);
            if ($val == $n) {
                $result[] = [$x, $y];
                $x++;
                $y--;
            } elseif ($val < $n) {
                $x++;
            } else { // $val > $n
                $y--;
            }
        }
        
        return $result;
    }
}
```

## Swift

```swift
/*
 * // This is the custom function interface.
 * // You should not implement it, or speculate about its implementation
 * class CustomFunction {
 *     // Returns f(x, y) for any given positive integers x and y.
 *     // Note that f(x, y) is increasing with respect to both x and y.
 *     // i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
 *     func f(_ x: Int, _ y: Int) -> Int {}
 * }
 */

class Solution {
    func findSolution(_ customfunction: CustomFunction, _ z: Int) -> [[Int]] {
        var result = [[Int]]()
        var x = 1
        var y = 1000
        while x <= 1000 && y >= 1 {
            let value = customfunction.f(x, y)
            if value == z {
                result.append([x, y])
                x += 1
                y -= 1
            } else if value < z {
                x += 1
            } else { // value > z
                y -= 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
/*
 * // This is the custom function interface.
 * // You should not implement it, or speculate about its implementation
 * class CustomFunction {
 *     // Returns f(x, y) for any given positive integers x and y.
 *     // Note that f(x, y) is increasing with respect to both x and y.
 *     // i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
 *     fun f(x:Int, y:Int):Int {}
 * };
 */

class Solution {
    fun findSolution(customfunction: CustomFunction, z: Int): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        var x = 1
        var y = 1000
        while (x <= 1000 && y >= 1) {
            val value = customfunction.f(x, y)
            when {
                value == z -> {
                    result.add(listOf(x, y))
                    x++
                    y--
                }
                value < z -> x++
                else -> y--
            }
        }
        return result
    }
}
```

## Golang

```go
/**
 * This is the declaration of customFunction API.
 * @param  x    int
 * @param  y    int
 * @return      Returns f(x, y) for any given positive integers x and y.
 *              Note that f(x, y) is increasing with respect to both x and y.
 *              i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
 */
func findSolution(customFunction func(int, int) int, z int) [][]int {
    const limit = 1000
    res := make([][]int, 0)
    x, y := 1, limit
    for x <= limit && y >= 1 {
        val := customFunction(x, y)
        if val == z {
            res = append(res, []int{x, y})
            x++
            y--
        } else if val < z {
            x++
        } else { // val > z
            y--
        }
    }
    return res
}
```

## Ruby

```ruby
def findSolution(customfunction, z)
  result = []
  x = 1
  y = 1000
  while x <= 1000 && y >= 1
    val = customfunction.f(x, y)
    if val == z
      result << [x, y]
      x += 1
      y -= 1
    elsif val < z
      x += 1
    else
      y -= 1
    end
  end
  result
end
```

## Scala

```scala
/*
 * // This is the custom function interface.
 * // You should not implement it, or speculate about its implementation
 * class CustomFunction {
 *     // Returns f(x, y) for any given positive integers x and y.
 *     // Note that f(x, y) is increasing with respect to both x and y.
 *     // i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
 *     def f(x: Int, y: Int): Int = {}
 * };
 */

object Solution {
    def findSolution(customfunction: CustomFunction, z: Int): List[List[Int]] = {
        var y = 1000
        val res = scala.collection.mutable.ListBuffer[List[Int]]()
        for (x <- 1 to 1000) {
            while (y >= 1 && customfunction.f(x, y) > z) {
                y -= 1
            }
            if (y >= 1 && customfunction.f(x, y) == z) {
                res += List(x, y)
            }
        }
        res.toList
    }
}
```

## Rust

```rust
/*
 * // This is the custom function interface.
 * // You should not implement it, or speculate about its implementation
 * struct CustomFunction;
 * impl CustomFunction {
 *    pub fn f(&self, x: i32, y: i32) -> i32 {}
 * }
 */

impl Solution {
    pub fn find_solution(customfunction: &CustomFunction, z: i32) -> Vec<Vec<i32>> {
        let mut result = Vec::new();
        let mut x = 1i32;
        let mut y = 1000i32; // upper bound from constraints

        while x <= 1000 && y >= 1 {
            let val = customfunction.f(x, y);
            if val == z {
                result.push(vec![x, y]);
                x += 1;
                y -= 1;
            } else if val < z {
                x += 1;
            } else {
                y -= 1;
            }
        }

        result
    }
}
```
