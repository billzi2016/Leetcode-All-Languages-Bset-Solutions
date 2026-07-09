# 1672. Richest Customer Wealth

## Cpp

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int maxWealth = 0;
        for (const auto& customer : accounts) {
            int wealth = 0;
            for (int money : customer) {
                wealth += money;
            }
            if (wealth > maxWealth) {
                maxWealth = wealth;
            }
        }
        return maxWealth;
    }
};
```

## Java

```java
class Solution {
    public int maximumWealth(int[][] accounts) {
        int maxWealth = 0;
        for (int[] customer : accounts) {
            int sum = 0;
            for (int money : customer) {
                sum += money;
            }
            if (sum > maxWealth) {
                maxWealth = sum;
            }
        }
        return maxWealth;
    }
}
```

## Python

```python
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
        for customer in accounts:
            wealth = sum(customer)
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth
```

## Python3

```python
from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))
```

## C

```c
int maximumWealth(int** accounts, int accountsSize, int* accountsColSize) {
    int max = 0;
    for (int i = 0; i < accountsSize; ++i) {
        int sum = 0;
        for (int j = 0; j < accountsColSize[i]; ++j) {
            sum += accounts[i][j];
        }
        if (sum > max) {
            max = sum;
        }
    }
    return max;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumWealth(int[][] accounts) {
        int maxWealth = 0;
        foreach (var customer in accounts) {
            int wealth = 0;
            foreach (int money in customer) {
                wealth += money;
            }
            if (wealth > maxWealth) {
                maxWealth = wealth;
            }
        }
        return maxWealth;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let maxWealth = 0;
    for (const customer of accounts) {
        let wealth = 0;
        for (const money of customer) {
            wealth += money;
        }
        if (wealth > maxWealth) maxWealth = wealth;
    }
    return maxWealth;
};
```

## Typescript

```typescript
function maximumWealth(accounts: number[][]): number {
    let maxWealth = 0;
    for (const customer of accounts) {
        const wealth = customer.reduce((sum, money) => sum + money, 0);
        if (wealth > maxWealth) {
            maxWealth = wealth;
        }
    }
    return maxWealth;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $accounts
     * @return Integer
     */
    function maximumWealth($accounts) {
        $max = 0;
        foreach ($accounts as $customer) {
            $sum = array_sum($customer);
            if ($sum > $max) {
                $max = $sum;
            }
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func maximumWealth(_ accounts: [[Int]]) -> Int {
        var maxWealth = 0
        for customer in accounts {
            let wealth = customer.reduce(0, +)
            if wealth > maxWealth {
                maxWealth = wealth
            }
        }
        return maxWealth
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumWealth(accounts: Array<IntArray>): Int {
        var maxWealth = 0
        for (customer in accounts) {
            var wealth = 0
            for (money in customer) {
                wealth += money
            }
            if (wealth > maxWealth) {
                maxWealth = wealth
            }
        }
        return maxWealth
    }
}
```

## Dart

```dart
class Solution {
  int maximumWealth(List<List<int>> accounts) {
    int maxWealth = 0;
    for (var customer in accounts) {
      int wealth = 0;
      for (var money in customer) {
        wealth += money;
      }
      if (wealth > maxWealth) {
        maxWealth = wealth;
      }
    }
    return maxWealth;
  }
}
```

## Golang

```go
func maximumWealth(accounts [][]int) int {
	maxWealth := 0
	for _, customer := range accounts {
		sum := 0
		for _, money := range customer {
			sum += money
		}
		if sum > maxWealth {
			maxWealth = sum
		}
	}
	return maxWealth
}
```

## Ruby

```ruby
def maximum_wealth(accounts)
  max = 0
  accounts.each do |row|
    wealth = 0
    row.each { |v| wealth += v }
    max = wealth if wealth > max
  end
  max
end
```

## Scala

```scala
object Solution {
    def maximumWealth(accounts: Array[Array[Int]]): Int = {
        var maxWealth = 0
        for (row <- accounts) {
            var sum = 0
            var i = 0
            while (i < row.length) {
                sum += row(i)
                i += 1
            }
            if (sum > maxWealth) maxWealth = sum
        }
        maxWealth
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_wealth(accounts: Vec<Vec<i32>>) -> i32 {
        let mut max_wealth = 0;
        for customer in accounts.iter() {
            let wealth: i32 = customer.iter().sum();
            if wealth > max_wealth {
                max_wealth = wealth;
            }
        }
        max_wealth
    }
}
```

## Racket

```racket
(define/contract (maximum-wealth accounts)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((sums (map (lambda (row) (apply + row)) accounts))
         (max-sum (apply max sums)))
    max-sum))
```

## Erlang

```erlang
-spec maximum_wealth(Accounts :: [[integer()]]) -> integer().
maximum_wealth(Accounts) ->
    Wealths = [lists:sum(Cust) || Cust <- Accounts],
    lists:max(Wealths).
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_wealth(accounts :: [[integer]]) :: integer
  def maximum_wealth(accounts) do
    accounts
    |> Enum.map(&Enum.sum/1)
    |> Enum.max()
  end
end
```
