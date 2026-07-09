# 1980. Find Unique Binary String

## Cpp

```cpp
class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        int n = nums.size();
        string ans;
        ans.reserve(n);
        for (int i = 0; i < n; ++i) {
            ans.push_back(nums[i][i] == '0' ? '1' : '0');
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public String findDifferentBinaryString(String[] nums) {
        int n = nums.length;
        StringBuilder sb = new StringBuilder(n);
        for (int i = 0; i < n; i++) {
            char c = nums[i].charAt(i);
            sb.append(c == '0' ? '1' : '0');
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        n = len(nums)
        ans_chars = []
        for i in range(n):
            # Flip the i-th character of the i-th string
            ans_chars.append('1' if nums[i][i] == '0' else '0')
        return ''.join(ans_chars)
```

## Python3

```python
from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        ans = []
        for i in range(n):
            ans.append('1' if nums[i][i] == '0' else '0')
        return ''.join(ans)
```

## C

```c
#include <stdlib.h>

char* findDifferentBinaryString(char** nums, int numsSize) {
    int n = numsSize;
    char *ans = (char*)malloc((n + 1) * sizeof(char));
    for (int i = 0; i < n; ++i) {
        ans[i] = (nums[i][i] == '0') ? '1' : '0';
    }
    ans[n] = '\0';
    return ans;
}
```

## Csharp

```csharp
using System.Text;

public class Solution {
    public string FindDifferentBinaryString(string[] nums) {
        int n = nums.Length;
        var sb = new StringBuilder(n);
        for (int i = 0; i < n; i++) {
            sb.Append(nums[i][i] == '0' ? '1' : '0');
        }
        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} nums
 * @return {string}
 */
var findDifferentBinaryString = function(nums) {
    const n = nums.length;
    let ans = '';
    for (let i = 0; i < n; i++) {
        ans += nums[i][i] === '0' ? '1' : '0';
    }
    return ans;
};
```

## Typescript

```typescript
function findDifferentBinaryString(nums: string[]): string {
    const n = nums.length;
    let ans = '';
    for (let i = 0; i < n; i++) {
        ans += nums[i][i] === '0' ? '1' : '0';
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $nums
     * @return String
     */
    function findDifferentBinaryString($nums) {
        $n = count($nums);
        $ans = '';
        for ($i = 0; $i < $n; $i++) {
            $c = $nums[$i][$i];
            $ans .= ($c === '0') ? '1' : '0';
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func findDifferentBinaryString(_ nums: [String]) -> String {
        let n = nums.count
        var answer = ""
        for i in 0..<n {
            let s = nums[i]
            let idx = s.index(s.startIndex, offsetBy: i)
            let ch = s[idx]
            answer.append(ch == "0" ? "1" : "0")
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findDifferentBinaryString(nums: Array<String>): String {
        val n = nums.size
        val sb = StringBuilder(n)
        for (i in 0 until n) {
            sb.append(if (nums[i][i] == '0') '1' else '0')
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String findDifferentBinaryString(List<String> nums) {
    int n = nums.length;
    StringBuffer sb = StringBuffer();
    for (int i = 0; i < n; i++) {
      sb.write(nums[i][i] == '0' ? '1' : '0');
    }
    return sb.toString();
  }
}
```

## Golang

```go
func findDifferentBinaryString(nums []string) string {
	n := len(nums)
	ans := make([]byte, n)
	for i := 0; i < n; i++ {
		if nums[i][i] == '0' {
			ans[i] = '1'
		} else {
			ans[i] = '0'
		}
	}
	return string(ans)
}
```

## Ruby

```ruby
def find_different_binary_string(nums)
  n = nums.length
  ans = []
  (0...n).each do |i|
    ans << (nums[i][i] == '0' ? '1' : '0')
  end
  ans.join
end
```

## Scala

```scala
object Solution {
    def findDifferentBinaryString(nums: Array[String]): String = {
        val n = nums.length
        val sb = new StringBuilder(n)
        var i = 0
        while (i < n) {
            sb.append(if (nums(i)(i) == '0') '1' else '0')
            i += 1
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_different_binary_string(nums: Vec<String>) -> String {
        let n = nums.len();
        let mut ans = String::with_capacity(n);
        for i in 0..n {
            let ch = nums[i].as_bytes()[i];
            if ch == b'0' {
                ans.push('1');
            } else {
                ans.push('0');
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (find-different-binary-string nums)
  (-> (listof string?) string?)
  (let* ((n (length nums))
         (chars
          (for/list ([i (in-range n)])
            (let* ((s (list-ref nums i))
                   (c (string-ref s i)))
              (if (char=? c #\0) #\1 #\0)))))
    (list->string chars)))
```

## Erlang

```erlang
-spec find_different_binary_string(Nums :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
find_different_binary_string(Nums) ->
    N = length(Nums),
    build(N, Nums, 0, []).

build(N, _Nums, I, Acc) when I == N ->
    list_to_binary(lists:reverse(Acc));
build(N, Nums, I, Acc) ->
    Bin = lists:nth(I + 1, Nums),
    Char = binary:at(Bin, I),
    NewChar = case Char of
        $0 -> $1;
        _  -> $0
    end,
    build(N, Nums, I + 1, [NewChar | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_different_binary_string(nums :: [String.t]) :: String.t
  def find_different_binary_string(nums) do
    n = length(nums)

    0..(n - 1)
    |> Enum.map(fn i ->
      s = Enum.at(nums, i)
      c = String.at(s, i)

      if c == "0", do: "1", else: "0"
    end)
    |> Enum.join()
  end
end
```
