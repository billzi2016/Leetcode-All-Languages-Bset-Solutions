# 1985. Find the Kth Largest Integer in the Array

## Cpp

```cpp
class Solution {
public:
    string kthLargestNumber(vector<string>& nums, int k) {
        auto cmp = [](const string& a, const string& b) {
            if (a.size() != b.size()) return a.size() > b.size();
            return a > b;
        };
        sort(nums.begin(), nums.end(), cmp);
        return nums[k - 1];
    }
};
```

## Java

```java
class Solution {
    public String kthLargestNumber(String[] nums, int k) {
        java.util.Arrays.sort(nums, (a, b) -> {
            if (a.length() != b.length()) {
                return Integer.compare(b.length(), a.length()); // longer first
            }
            return b.compareTo(a); // lexicographically larger first
        });
        return nums[k - 1];
    }
}
```

## Python

```python
class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        # Sort by length then lexicographically (both ascending)
        nums.sort(key=lambda s: (len(s), s))
        # The k-th largest is the element at position -k
        return nums[-k]
```

## Python3

```python
from typing import List

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # Sort numbers by length and then lexicographically in descending order
        nums.sort(key=lambda x: (len(x), x), reverse=True)
        return nums[k - 1]
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int cmpDesc(const void *a, const void *b) {
    const char *s = *(const char **)a;
    const char *t = *(const char **)b;
    size_t ls = strlen(s);
    size_t lt = strlen(t);
    if (ls != lt) return (int)(lt - ls);   // longer string first
    return strcmp(t, s);                    // lexicographically larger first
}

char* kthLargestNumber(char** nums, int numsSize, int k) {
    qsort(nums, numsSize, sizeof(char *), cmpDesc);
    return nums[k - 1];
}
```

## Csharp

```csharp
public class Solution
{
    public string KthLargestNumber(string[] nums, int k)
    {
        Array.Sort(nums, (a, b) =>
        {
            if (a.Length != b.Length)
                return b.Length - a.Length; // longer number is larger
            return string.Compare(b, a, StringComparison.Ordinal); // same length: lexicographic descending
        });
        return nums[k - 1];
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} nums
 * @param {number} k
 * @return {string}
 */
var kthLargestNumber = function(nums, k) {
    nums.sort((a, b) => {
        if (a.length !== b.length) return b.length - a.length;
        if (a === b) return 0;
        return a > b ? -1 : 1; // descending lexicographic for equal length
    });
    return nums[k - 1];
};
```

## Typescript

```typescript
function kthLargestNumber(nums: string[], k: number): string {
    nums.sort((a, b) => {
        if (a.length !== b.length) return b.length - a.length;
        if (a === b) return 0;
        return b > a ? 1 : -1; // descending lexicographic
    });
    return nums[k - 1];
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $nums
     * @param Integer $k
     * @return String
     */
    function kthLargestNumber($nums, $k) {
        usort($nums, function($a, $b) {
            $lenA = strlen($a);
            $lenB = strlen($b);
            if ($lenA === $lenB) {
                if ($a === $b) return 0;
                // larger numeric string should come first
                return $a < $b ? 1 : -1;
            }
            // longer string represents larger number
            return $lenA < $lenB ? 1 : -1;
        });
        return $nums[$k - 1];
    }
}
```

## Swift

```swift
class Solution {
    func kthLargestNumber(_ nums: [String], _ k: Int) -> String {
        let sortedNums = nums.sorted { a, b in
            if a.count != b.count {
                return a.count > b.count
            } else {
                return a > b
            }
        }
        return sortedNums[k - 1]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kthLargestNumber(nums: Array<String>, k: Int): String {
        val sorted = nums.sortedWith(Comparator { a, b ->
            if (a.length != b.length) {
                b.length - a.length
            } else {
                b.compareTo(a)
            }
        })
        return sorted[k - 1]
    }
}
```

## Dart

```dart
class Solution {
  String kthLargestNumber(List<String> nums, int k) {
    int compareDesc(String a, String b) {
      if (a.length != b.length) {
        return b.length.compareTo(a.length);
      }
      return b.compareTo(a);
    }

    nums.sort(compareDesc);
    return nums[k - 1];
  }
}
```

## Golang

```go
func kthLargestNumber(nums []string, k int) string {
    sort.Slice(nums, func(i, j int) bool {
        if len(nums[i]) != len(nums[j]) {
            return len(nums[i]) > len(nums[j])
        }
        return nums[i] > nums[j]
    })
    return nums[k-1]
}
```

## Ruby

```ruby
def kth_largest_number(nums, k)
  sorted = nums.sort do |a, b|
    if a.length != b.length
      b.length <=> a.length
    else
      b <=> a
    end
  end
  sorted[k - 1]
end
```

## Scala

```scala
object Solution {
    def kthLargestNumber(nums: Array[String], k: Int): String = {
        val sorted = nums.sortWith { (a, b) =>
            if (a.length != b.length) a.length > b.length
            else a > b
        }
        sorted(k - 1)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn kth_largest_number(nums: Vec<String>, k: i32) -> String {
        let mut nums = nums;
        nums.sort_unstable_by(|a, b| {
            if a.len() != b.len() {
                b.len().cmp(&a.len())
            } else {
                b.cmp(a)
            }
        });
        nums[(k as usize) - 1].clone()
    }
}
```

## Racket

```racket
(define/contract (kth-largest-number nums k)
  (-> (listof string?) exact-integer? string?)
  (let* ((greater?
          (lambda (a b)
            (let ((la (string-length a))
                  (lb (string-length b)))
              (if (not (= la lb))
                  (> la lb)
                  (string>? a b)))))
         (sorted (sort nums greater?)))
    (list-ref sorted (- k 1))))
```

## Erlang

```erlang
-spec kth_largest_number(Nums :: [unicode:unicode_binary()], K :: integer()) -> unicode:unicode_binary().
kth_largest_number(Nums, K) ->
    Cmp = fun(A, B) ->
        LenA = byte_size(A),
        LenB = byte_size(B),
        if
            LenA > LenB -> true;
            LenA < LenB -> false;
            true -> A > B
        end
    end,
    Sorted = lists:sort(Cmp, Nums),
    lists:nth(K, Sorted).
```

## Elixir

```elixir
defmodule Solution do
  @spec kth_largest_number(nums :: [String.t()], k :: integer) :: String.t()
  def kth_largest_number(nums, k) do
    sorted =
      Enum.sort(nums, fn a, b ->
        la = byte_size(a)
        lb = byte_size(b)

        if la != lb do
          la > lb
        else
          a > b
        end
      end)

    Enum.at(sorted, k - 1)
  end
end
```
