# 2525. Categorize Box According to Criteria

## Cpp

```cpp
class Solution {
public:
    string categorizeBox(int length, int width, int height, int mass) {
        bool bulky = false;
        if (length >= 10000 || width >= 10000 || height >= 10000) {
            bulky = true;
        } else {
            long long volume = 1LL * length * width * height;
            if (volume >= 1000000000LL) bulky = true;
        }
        bool heavy = mass >= 100;
        
        if (bulky && heavy) return "Both";
        if (bulky) return "Bulky";
        if (heavy) return "Heavy";
        return "Neither";
    }
};
```

## Java

```java
class Solution {
    public String categorizeBox(int length, int width, int height, int mass) {
        boolean bulky = length >= 10000 || width >= 10000 || height >= 10000;
        long volume = (long) length * width * height;
        if (volume >= 1_000_000_000L) {
            bulky = true;
        }
        boolean heavy = mass >= 100;
        if (bulky && heavy) return "Both";
        if (bulky) return "Bulky";
        if (heavy) return "Heavy";
        return "Neither";
    }
}
```

## Python

```python
class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        bulky = (length >= 10**4 or width >= 10**4 or height >= 10**4 or length * width * height >= 10**9)
        heavy = mass >= 100

        if bulky and heavy:
            return "Both"
        if bulky:
            return "Bulky"
        if heavy:
            return "Heavy"
        return "Neither"
```

## Python3

```python
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = (
            length >= 10**4
            or width >= 10**4
            or height >= 10**4
            or length * width * height >= 10**9
        )
        heavy = mass >= 100

        if bulky and heavy:
            return "Both"
        if bulky:
            return "Bulky"
        if heavy:
            return "Heavy"
        return "Neither"
```

## C

```c
char* categorizeBox(int length, int width, int height, int mass) {
    long long volume = (long long)length * width * height;
    int bulky = (length >= 10000 || width >= 10000 || height >= 10000 || volume >= 1000000000LL);
    int heavy = (mass >= 100);
    
    if (bulky && heavy) return "Both";
    if (bulky) return "Bulky";
    if (heavy) return "Heavy";
    return "Neither";
}
```

## Csharp

```csharp
public class Solution {
    public string CategorizeBox(int length, int width, int height, int mass) {
        bool bulky = length >= 10000 || width >= 10000 || height >= 10000 ||
                     (long)length * width * height >= 1000000000L;
        bool heavy = mass >= 100;
        
        if (bulky && heavy) return "Both";
        if (bulky) return "Bulky";
        if (heavy) return "Heavy";
        return "Neither";
    }
}
```

## Javascript

```javascript
/**
 * @param {number} length
 * @param {number} width
 * @param {number} height
 * @param {number} mass
 * @return {string}
 */
var categorizeBox = function(length, width, height, mass) {
    const BULKY_DIMENSION_LIMIT = 1e4;
    const BULKY_VOLUME_LIMIT = 1e9;
    const HEAVY_MASS_LIMIT = 100;

    const isBulky = length >= BULKY_DIMENSION_LIMIT ||
                    width >= BULKY_DIMENSION_LIMIT ||
                    height >= BULKY_DIMENSION_LIMIT ||
                    (length * width * height) >= BULKY_VOLUME_LIMIT;

    const isHeavy = mass >= HEAVY_MASS_LIMIT;

    if (isBulky && isHeavy) return "Both";
    if (isBulky) return "Bulky";
    if (isHeavy) return "Heavy";
    return "Neither";
};
```

## Typescript

```typescript
function categorizeBox(length: number, width: number, height: number, mass: number): string {
    const isBulky = length >= 10000 || width >= 10000 || height >= 10000 || length * width * height >= 1_000_000_000;
    const isHeavy = mass >= 100;
    if (isBulky && isHeavy) return "Both";
    if (isBulky) return "Bulky";
    if (isHeavy) return "Heavy";
    return "Neither";
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $length
     * @param Integer $width
     * @param Integer $height
     * @param Integer $mass
     * @return String
     */
    function categorizeBox($length, $width, $height, $mass) {
        $bulky = ($length >= 10000) || ($width >= 10000) || ($height >= 10000);
        if (!$bulky) {
            $volume = $length * $width;
            $volume *= $height;
            if ($volume >= 1000000000) {
                $bulky = true;
            }
        }
        $heavy = $mass >= 100;

        if ($bulky && $heavy) {
            return "Both";
        } elseif ($bulky) {
            return "Bulky";
        } elseif ($heavy) {
            return "Heavy";
        } else {
            return "Neither";
        }
    }
}
```

## Swift

```swift
class Solution {
    func categorizeBox(_ length: Int, _ width: Int, _ height: Int, _ mass: Int) -> String {
        let bulkyDimension = length >= 10000 || width >= 10000 || height >= 10000
        let volume = Int64(length) * Int64(width) * Int64(height)
        let bulkyVolume = volume >= 1_000_000_000
        let isBulky = bulkyDimension || bulkyVolume
        let isHeavy = mass >= 100
        
        if isBulky && isHeavy {
            return "Both"
        } else if isBulky {
            return "Bulky"
        } else if isHeavy {
            return "Heavy"
        } else {
            return "Neither"
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun categorizeBox(length: Int, width: Int, height: Int, mass: Int): String {
        val bulky = length >= 10_000 || width >= 10_000 || height >= 10_000 ||
                length.toLong() * width.toLong() * height.toLong() >= 1_000_000_000L
        val heavy = mass >= 100
        return when {
            bulky && heavy -> "Both"
            bulky -> "Bulky"
            heavy -> "Heavy"
            else -> "Neither"
        }
    }
}
```

## Dart

```dart
class Solution {
  String categorizeBox(int length, int width, int height, int mass) {
    bool bulky = length >= 10000 ||
        width >= 10000 ||
        height >= 10000 ||
        (length * width * height) >= 1000000000;
    bool heavy = mass >= 100;

    if (bulky && heavy) return "Both";
    if (bulky) return "Bulky";
    if (heavy) return "Heavy";
    return "Neither";
  }
}
```

## Golang

```go
func categorizeBox(length int, width int, height int, mass int) string {
    bulky := false
    if length >= 10000 || width >= 10000 || height >= 10000 {
        bulky = true
    } else {
        volume := int64(length) * int64(width) * int64(height)
        if volume >= 1000000000 {
            bulky = true
        }
    }

    heavy := mass >= 100

    switch {
    case bulky && heavy:
        return "Both"
    case bulky:
        return "Bulky"
    case heavy:
        return "Heavy"
    default:
        return "Neither"
    }
}
```

## Ruby

```ruby
# @param {Integer} length
# @param {Integer} width
# @param {Integer} height
# @param {Integer} mass
# @return {String}
def categorize_box(length, width, height, mass)
  bulky = length >= 10_000 || width >= 10_000 || height >= 10_000 ||
          (length * width * height) >= 1_000_000_000
  heavy = mass >= 100

  if bulky && heavy
    "Both"
  elsif bulky
    "Bulky"
  elsif heavy
    "Heavy"
  else
    "Neither"
  end
end
```

## Scala

```scala
object Solution {
    def categorizeBox(length: Int, width: Int, height: Int, mass: Int): String = {
        val bulky = length >= 10000 || width >= 10000 || height >= 10000 ||
                    (length.toLong * width.toLong * height.toLong) >= 1000000000L
        val heavy = mass >= 100

        if (bulky && heavy) "Both"
        else if (bulky) "Bulky"
        else if (heavy) "Heavy"
        else "Neither"
    }
}
```

## Rust

```rust
impl Solution {
    pub fn categorize_box(length: i32, width: i32, height: i32, mass: i32) -> String {
        let bulky = length >= 10_000
            || width >= 10_000
            || height >= 10_000
            || (length as i64 * width as i64 * height as i64) >= 1_000_000_000;
        let heavy = mass >= 100;
        match (bulky, heavy) {
            (true, true) => "Both".to_string(),
            (true, false) => "Bulky".to_string(),
            (false, true) => "Heavy".to_string(),
            _ => "Neither".to_string(),
        }
    }
}
```

## Racket

```racket
(define/contract (categorize-box length width height mass)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? string?)
  (let* ((bulky (or (>= length 10000)
                    (>= width 10000)
                    (>= height 10000)
                    (>= (* length width height) 1000000000)))
         (heavy (>= mass 100)))
    (cond
      [(and bulky heavy) "Both"]
      [bulky "Bulky"]
      [heavy "Heavy"]
      [else "Neither"])))
```

## Erlang

```erlang
-spec categorize_box(Length :: integer(), Width :: integer(), Height :: integer(), Mass :: integer()) -> unicode:unicode_binary().
categorize_box(Length, Width, Height, Mass) ->
    Bulky = (Length >= 10000) orelse (Width >= 10000) orelse (Height >= 10000) orelse (Length * Width * Height >= 1000000000),
    Heavy = Mass >= 100,
    case {Bulky, Heavy} of
        {true, true} -> <<"Both">>;
        {true, false} -> <<"Bulky">>;
        {false, true} -> <<"Heavy">>;
        _ -> <<"Neither">>
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec categorize_box(length :: integer, width :: integer, height :: integer, mass :: integer) :: String.t()
  def categorize_box(length, width, height, mass) do
    bulky =
      length >= 10_000 or
        width >= 10_000 or
        height >= 10_000 or
        length * width * height >= 1_000_000_000

    heavy = mass >= 100

    cond do
      bulky and heavy -> "Both"
      bulky -> "Bulky"
      heavy -> "Heavy"
      true -> "Neither"
    end
  end
end
```
