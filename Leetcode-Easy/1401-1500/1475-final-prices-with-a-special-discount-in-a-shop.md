# 1475. Final Prices With a Special Discount in a Shop

## Cpp

```cpp
class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        int n = prices.size();
        vector<int> result = prices;
        std::stack<int> st; // store indices
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && prices[st.top()] >= prices[i]) {
                int idx = st.top();
                st.pop();
                result[idx] = prices[idx] - prices[i];
            }
            st.push(i);
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    public int[] finalPrices(int[] prices) {
        int n = prices.length;
        int[] result = java.util.Arrays.copyOf(prices, n);
        java.util.ArrayDeque<Integer> stack = new java.util.ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && prices[stack.peek()] >= prices[i]) {
                int idx = stack.pop();
                result[idx] = prices[idx] - prices[i];
            }
            stack.push(i);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        res = prices[:]
        stack = []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                idx = stack.pop()
                res[idx] = prices[idx] - price
            stack.append(i)
        return res
```

## Python3

```python
from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices[:]
        stack = []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                idx = stack.pop()
                result[idx] = prices[idx] - price
            stack.append(i)
        return result
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* finalPrices(int* prices, int pricesSize, int* returnSize) {
    int* result = (int*)malloc(pricesSize * sizeof(int));
    if (!result) {
        *returnSize = 0;
        return NULL;
    }
    for (int i = 0; i < pricesSize; ++i) {
        result[i] = prices[i];
    }

    int* stack = (int*)malloc(pricesSize * sizeof(int));
    int top = -1;

    for (int i = 0; i < pricesSize; ++i) {
        while (top >= 0 && prices[stack[top]] >= prices[i]) {
            int idx = stack[top--];
            result[idx] = prices[idx] - prices[i];
        }
        stack[++top] = i;
    }

    free(stack);
    *returnSize = pricesSize;
    return result;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int[] FinalPrices(int[] prices) {
        int n = prices.Length;
        int[] result = new int[n];
        for (int i = 0; i < n; i++) result[i] = prices[i];

        Stack<int> stack = new Stack<int>();
        for (int i = 0; i < n; i++) {
            while (stack.Count > 0 && prices[stack.Peek()] >= prices[i]) {
                int idx = stack.Pop();
                result[idx] = prices[idx] - prices[i];
            }
            stack.Push(i);
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} prices
 * @return {number[]}
 */
var finalPrices = function(prices) {
    const n = prices.length;
    const result = [...prices];
    const stack = []; // store indices awaiting discount
    
    for (let i = 0; i < n; i++) {
        while (stack.length && prices[stack[stack.length - 1]] >= prices[i]) {
            const idx = stack.pop();
            result[idx] = prices[idx] - prices[i];
        }
        stack.push(i);
    }
    
    return result;
};
```

## Typescript

```typescript
function finalPrices(prices: number[]): number[] {
    const n = prices.length;
    const result = prices.slice();
    const stack: number[] = [];
    for (let i = 0; i < n; i++) {
        while (stack.length && prices[stack[stack.length - 1]] >= prices[i]) {
            const idx = stack.pop()!;
            result[idx] = prices[idx] - prices[i];
        }
        stack.push(i);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $prices
     * @return Integer[]
     */
    function finalPrices($prices) {
        $n = count($prices);
        $result = $prices;
        $stack = [];

        for ($i = 0; $i < $n; $i++) {
            while (!empty($stack) && $prices[end($stack)] >= $prices[$i]) {
                $idx = array_pop($stack);
                $result[$idx] = $prices[$idx] - $prices[$i];
            }
            $stack[] = $i;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func finalPrices(_ prices: [Int]) -> [Int] {
        var result = prices
        var stack = [Int]() // store indices
        
        for i in 0..<prices.count {
            while let last = stack.last, prices[last] >= prices[i] {
                let idx = stack.removeLast()
                result[idx] = prices[idx] - prices[i]
            }
            stack.append(i)
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun finalPrices(prices: IntArray): IntArray {
        val n = prices.size
        val result = prices.clone()
        val stack = java.util.ArrayDeque<Int>()
        for (i in 0 until n) {
            while (!stack.isEmpty() && prices[stack.peek()] >= prices[i]) {
                val idx = stack.pop()
                result[idx] = prices[idx] - prices[i]
            }
            stack.push(i)
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> finalPrices(List<int> prices) {
    List<int> result = List.from(prices);
    List<int> stack = [];
    for (int i = 0; i < prices.length; i++) {
      while (stack.isNotEmpty && prices[stack.last] >= prices[i]) {
        int idx = stack.removeLast();
        result[idx] = prices[idx] - prices[i];
      }
      stack.add(i);
    }
    return result;
  }
}
```

## Golang

```go
func finalPrices(prices []int) []int {
    n := len(prices)
    res := make([]int, n)
    copy(res, prices)

    stack := make([]int, 0, n)
    for i, price := range prices {
        for len(stack) > 0 && prices[stack[len(stack)-1]] >= price {
            idx := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            res[idx] = prices[idx] - price
        }
        stack = append(stack, i)
    }
    return res
}
```

## Ruby

```ruby
# @param {Integer[]} prices
# @return {Integer[]}
def final_prices(prices)
  n = prices.length
  result = prices.clone
  stack = []
  (0...n).each do |i|
    while !stack.empty? && prices[i] <= prices[stack[-1]]
      idx = stack.pop
      result[idx] = prices[idx] - prices[i]
    end
    stack << i
  end
  result
end
```

## Scala

```scala
object Solution {
    def finalPrices(prices: Array[Int]): Array[Int] = {
        val n = prices.length
        val result = prices.clone()
        val stack = new scala.collection.mutable.Stack[Int]()
        var i = 0
        while (i < n) {
            while (stack.nonEmpty && prices(i) <= prices(stack.top)) {
                val idx = stack.pop()
                result(idx) = prices(idx) - prices(i)
            }
            stack.push(i)
            i += 1
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn final_prices(prices: Vec<i32>) -> Vec<i32> {
        let n = prices.len();
        let mut result = prices.clone();
        let mut stack: Vec<usize> = Vec::new();

        for i in 0..n {
            while let Some(&last) = stack.last() {
                if prices[i] <= prices[last] {
                    result[last] = prices[last] - prices[i];
                    stack.pop();
                } else {
                    break;
                }
            }
            stack.push(i);
        }

        result
    }
}
```

## Racket

```racket
(define/contract (final-prices prices)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ([n (length prices)]
         [vec (list->vector prices)]
         [res (make-vector n)])
    ;; copy original prices into result vector
    (for ([i (in-range n)])
      (vector-set! res i (vector-ref vec i)))
    (let ((stack '()))
      (for ([i (in-range n)])
        (define current (vector-ref vec i))
        (let loop ()
          (when (and (not (null? stack))
                     (<= current (vector-ref vec (car stack))))
            (define idx (car stack))
            (set! stack (cdr stack))
            (vector-set! res idx (- (vector-ref vec idx) current))
            (loop)))
        (set! stack (cons i stack)))
      (vector->list res))))
```

## Erlang

```erlang
-spec final_prices(Prices :: [integer()]) -> [integer()].
final_prices([]) -> [];
final_prices([H|T]) ->
    Discount = find_discount(T, H),
    [H - Discount | final_prices(T)].

find_discount([], _Curr) -> 0;
find_discount([X|_], Curr) when X =< Curr -> X;
find_discount([_|Xs], Curr) -> find_discount(Xs, Curr).
```

## Elixir

```elixir
defmodule Solution do
  @spec final_prices(prices :: [integer]) :: [integer]
  def final_prices(prices) do
    arr = :array.from_list(prices)

    {final_arr, _stack} =
      Enum.reduce(Enum.with_index(prices), {arr, []}, fn {price, idx},
                                                        {acc_arr, stack} ->
        {new_stack, new_arr} = pop_and_apply(stack, price, acc_arr)
        {new_arr, [{price, idx} | new_stack]}
      end)

    :array.to_list(final_arr)
  end

  defp pop_and_apply([], _price, arr), do: {[], arr}

  defp pop_and_apply([{prev_price, prev_idx} = head | rest], price, arr) when prev_price >= price do
    new_arr = :array.set(prev_idx, prev_price - price, arr)
    pop_and_apply(rest, price, new_arr)
  end

  defp pop_and_apply(stack, _price, arr), do: {stack, arr}
end
```
