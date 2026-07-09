# 0385. Mini Parser

## Cpp

```cpp
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Constructor initializes an empty nested list.
 *     NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     NestedInteger(int value);
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Set this NestedInteger to hold a single integer.
 *     void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     void add(const NestedInteger &ni);
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class Solution {
public:
    NestedInteger deserialize(string s) {
        if (s.empty()) return NestedInteger();
        if (s[0] != '[') {
            return NestedInteger(stoi(s));
        }
        stack<NestedInteger> st;
        string numStr;
        for (size_t i = 0; i < s.size(); ++i) {
            char c = s[i];
            if (c == '[') {
                st.push(NestedInteger());
            } else if (c == ']' || c == ',') {
                if (!numStr.empty()) {
                    int num = stoi(numStr);
                    st.top().add(NestedInteger(num));
                    numStr.clear();
                }
                if (c == ']') {
                    NestedInteger cur = st.top(); st.pop();
                    if (st.empty()) return cur;
                    st.top().add(cur);
                }
            } else { // digit or '-'
                numStr.push_back(c);
            }
        }
        return NestedInteger(); // fallback, should never reach here
    }
};
```

## Java

```java
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     public NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     public NestedInteger(int value);
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public void add(NestedInteger ni);
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
class Solution {
    public NestedInteger deserialize(String s) {
        if (s == null || s.isEmpty()) return new NestedInteger();
        // Single integer case, no brackets.
        if (s.charAt(0) != '[') {
            return new NestedInteger(Integer.parseInt(s));
        }

        Deque<NestedInteger> stack = new ArrayDeque<>();
        StringBuilder num = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '[') {
                NestedInteger ni = new NestedInteger();
                if (!stack.isEmpty()) {
                    stack.peek().add(ni);
                }
                stack.push(ni);
            } else if (c == ']') {
                // If there is a number pending, add it before closing the list.
                if (num.length() > 0) {
                    int val = Integer.parseInt(num.toString());
                    stack.peek().add(new NestedInteger(val));
                    num.setLength(0);
                }
                NestedInteger completed = stack.pop();
                if (stack.isEmpty()) {
                    return completed;
                }
            } else if (c == ',') {
                // End of a number element.
                if (num.length() > 0) {
                    int val = Integer.parseInt(num.toString());
                    stack.peek().add(new NestedInteger(val));
                    num.setLength(0);
                }
                // commas between lists are ignored otherwise
            } else { // digit or '-'
                num.append(c);
            }
        }

        // Should never reach here for valid input.
        return new NestedInteger();
    }
}
```

## Python

```python
class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        # If the string does not start with '[', it's a single integer.
        if not s:
            return None
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = ''
        for ch in s:
            if ch == '[':
                ni = NestedInteger()
                if stack:
                    stack[-1].add(ni)
                stack.append(ni)
            elif ch == ']':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ''
                completed = stack.pop()
                if not stack:
                    return completed
            elif ch == ',':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ''
            else:  # digit or '-'
                num += ch
        # In case the entire string is a single integer (handled earlier) 
        # or malformed input, return None.
        return None
```

## Python3

```python
class Solution:
    def deserialize(self, s: str):
        if not s:
            return NestedInteger()
        # If it's a single integer (no brackets)
        if s[0] != '[':
            return NestedInteger(int(s))
        
        stack = []
        num = ''
        for i, ch in enumerate(s):
            if ch == '[':
                stack.append(NestedInteger())
            elif ch == ']':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ''
                cur = stack.pop()
                if not stack:
                    return cur
                stack[-1].add(cur)
            elif ch == ',':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ''
            else:  # digit or '-'
                num += ch
        # Should never reach here for valid input
        return NestedInteger()
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

/**
 * *********************************************************************
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * *********************************************************************
 *
 * // Initializes an empty nested list and return a reference to the nested integer.
 * struct NestedInteger *NestedIntegerInit();
 *
 * // Return true if this NestedInteger holds a single integer, rather than a nested list.
 * bool NestedIntegerIsInteger(struct NestedInteger *);
 *
 * // Return the single integer that this NestedInteger holds, if it holds a single integer
 * // The result is undefined if this NestedInteger holds a nested list
 * int NestedIntegerGetInteger(struct NestedInteger *);
 *
 * // Set this NestedInteger to hold a single integer.
 * void NestedIntegerSetInteger(struct NestedInteger *ni, int value);
 *
 * // Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
 * void NestedIntegerAdd(struct NestedInteger *ni, struct NestedInteger *elem);
 *
 * // Return the nested list that this NestedInteger holds, if it holds a nested list
 * // The result is undefined if this NestedInteger holds a single integer
 * struct NestedInteger **NestedIntegerGetList(struct NestedInteger *);
 *
 * // Return the nested list's size that this NestedInteger holds, if it holds a nested list
 * // The result is undefined if this NestedInteger holds a single integer
 * int NestedIntegerGetListSize(struct NestedInteger *);
 * };
 */
struct NestedInteger* deserialize(char* s) {
    int len = strlen(s);
    struct NestedInteger **stack = (struct NestedInteger **)malloc(sizeof(struct NestedInteger *) * (len + 2));
    int top = -1;
    int i = 0;

    // Single integer case
    if (s[0] != '[') {
        bool neg = false;
        if (s[i] == '-') { neg = true; i++; }
        int val = 0;
        while (i < len && isdigit(s[i])) {
            val = val * 10 + (s[i] - '0');
            i++;
        }
        if (neg) val = -val;
        struct NestedInteger *ni = NestedIntegerInit();
        NestedIntegerSetInteger(ni, val);
        free(stack);
        return ni;
    }

    while (i < len) {
        char c = s[i];
        if (c == '[') {
            struct NestedInteger *ni = NestedIntegerInit(); // empty list
            stack[++top] = ni;
            i++;
        } else if (c == ']') {
            struct NestedInteger *completed = stack[top--];
            if (top >= 0) {
                NestedIntegerAdd(stack[top], completed);
            } else {
                free(stack);
                return completed;
            }
            i++;
        } else if (c == ',') {
            i++; // skip commas
        } else { // number (digit or '-')
            bool neg = false;
            if (c == '-') { neg = true; i++; }
            int val = 0;
            while (i < len && isdigit(s[i])) {
                val = val * 10 + (s[i] - '0');
                i++;
            }
            if (neg) val = -val;
            struct NestedInteger *ni = NestedIntegerInit();
            NestedIntegerSetInteger(ni, val);
            // add to current list
            if (top >= 0) {
                NestedIntegerAdd(stack[top], ni);
            } else {
                // Should not happen for valid input
                free(stack);
                return ni;
            }
        }
    }

    // Fallback (should never reach here)
    free(stack);
    return NULL;
}
```

## Csharp

```csharp
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * interface NestedInteger {
 *
 *     // Constructor initializes an empty nested list.
 *     public NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     public NestedInteger(int value);
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool IsInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     int GetInteger();
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public void SetInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public void Add(NestedInteger ni);
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     IList<NestedInteger> GetList();
 * }
 */
public class Solution {
    public NestedInteger Deserialize(string s) {
        if (s.Length == 0) return null;
        if (s[0] != '[') {
            // Single integer case
            int val = int.Parse(s);
            return new NestedInteger(val);
        }

        Stack<NestedInteger> stack = new Stack<NestedInteger>();
        int num = 0;
        int sign = 1;
        bool hasNum = false;

        foreach (char c in s) {
            if (c == '[') {
                // Start a new list
                stack.Push(new NestedInteger());
            } else if (c == ']') {
                // Finish current number if any
                if (hasNum) {
                    var ni = new NestedInteger(sign * num);
                    stack.Peek().Add(ni);
                    hasNum = false;
                    num = 0;
                    sign = 1;
                }
                // Pop completed list
                var completed = stack.Pop();
                if (stack.Count == 0) {
                    return completed; // This is the outermost result
                } else {
                    stack.Peek().Add(completed);
                }
            } else if (c == ',') {
                if (hasNum) {
                    var ni = new NestedInteger(sign * num);
                    stack.Peek().Add(ni);
                    hasNum = false;
                    num = 0;
                    sign = 1;
                }
                // commas just separate elements
            } else if (c == '-') {
                sign = -1;
            } else if (char.IsDigit(c)) {
                num = num * 10 + (c - '0');
                hasNum = true;
            }
        }

        // Should never reach here for valid input
        return null;
    }
}
```

## Javascript

```javascript
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * function NestedInteger() {
 *
 *     Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     @return {boolean}
 *     this.isInteger = function() {
 *         ...
 *     };
 *
 *     Return the single integer that this NestedInteger holds, if it holds a single integer
 *     Return null if this NestedInteger holds a nested list
 *     @return {integer}
 *     this.getInteger = function() {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a single integer equal to value.
 *     @return {void}
 *     this.setInteger = function(value) {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
 *     @return {void}
 *     this.add = function(elem) {
 *         ...
 *     };
 *
 *     Return the nested list that this NestedInteger holds, if it holds a nested list
 *     Return null if this NestedInteger holds a single integer
 *     @return {NestedInteger[]}
 *     this.getList = function() {
 *         ...
 *     };
 * };
 */
/**
 * @param {string} s
 * @return {NestedInteger}
 */
var deserialize = function(s) {
    // Single integer case
    if (s[0] !== '[') {
        const ni = new NestedInteger();
        ni.setInteger(parseInt(s, 10));
        return ni;
    }

    const stack = [];
    let numBuffer = null; // accumulate digits for a number

    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        if (ch === '[') {
            // start a new list
            stack.push(new NestedInteger());
        } else if (ch === ']') {
            // finish any pending number before closing the list
            if (numBuffer !== null) {
                const val = parseInt(numBuffer, 10);
                const niNum = new NestedInteger();
                niNum.setInteger(val);
                stack[stack.length - 1].add(niNum);
                numBuffer = null;
            }
            // if this list is nested, pop and add to its parent
            if (stack.length > 1) {
                const completed = stack.pop();
                stack[stack.length - 1].add(completed);
            }
        } else if (ch === ',') {
            // finish a number before moving to next element
            if (numBuffer !== null) {
                const val = parseInt(numBuffer, 10);
                const niNum = new NestedInteger();
                niNum.setInteger(val);
                stack[stack.length - 1].add(niNum);
                numBuffer = null;
            }
        } else { // digit or '-'
            if (numBuffer === null) numBuffer = '';
            numBuffer += ch;
        }
    }

    return stack[0];
};
```

## Typescript

```typescript
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *     constructor(value?: number) { ... }
 *     isInteger(): boolean { ... }
 *     getInteger(): number | null { ... }
 *     setInteger(value: number): void { ... }
 *     add(elem: NestedInteger): void { ... }
 *     getList(): NestedInteger[] { ... }
 * };
 */

function deserialize(s: string): NestedInteger {
    const isDigit = (c: string) => c >= '0' && c <= '9';
    if (s[0] !== '[') {
        // pure integer
        return new NestedInteger(parseInt(s));
    }

    const stack: NestedInteger[] = [];
    let result: NestedInteger | null = null;
    let i = 0;
    const n = s.length;

    while (i < n) {
        const ch = s[i];
        if (ch === '[') {
            // start a new list
            const ni = new NestedInteger();
            stack.push(ni);
            i++;
        } else if (ch === ']') {
            // finish current list
            const completed = stack.pop()!;
            if (stack.length > 0) {
                stack[stack.length - 1].add(completed);
            } else {
                result = completed;
            }
            i++;
        } else if (ch === ',') {
            i++; // skip separator
        } else { // number (could be negative)
            let j = i;
            if (s[j] === '-') j++;
            while (j < n && isDigit(s[j])) j++;
            const num = parseInt(s.slice(i, j));
            const ni = new NestedInteger(num);
            if (stack.length > 0) {
                stack[stack.length - 1].add(ni);
            } else {
                result = ni;
            }
            i = j;
        }
    }

    // For inputs like "[]", result will be set inside the loop.
    return result!;
}
```

## Php

```php
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *
 *     // if value is not specified, initializes an empty list.
 *     // Otherwise initializes a single integer equal to value.
 *     function __construct($value = null)
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     function isInteger() : bool
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     function getInteger()
 *
 *     // Set this NestedInteger to hold a single integer.
 *     function setInteger($i) : void
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     function add($ni) : void
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     function getList() : array
 * }
 */
class Solution {

    /**
     * @param String $s
     * @return NestedInteger
     */
    function deserialize($s) {
        // If the string does not start with '[', it's a single integer.
        if ($s[0] !== '[') {
            return new NestedInteger(intval($s));
        }

        $stack = [];
        $num = '';
        $len = strlen($s);

        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];

            if ($ch === '[') {
                // Start a new list.
                array_push($stack, new NestedInteger());
            } elseif ($ch === ']') {
                // If there is a pending number, add it before closing the list.
                if ($num !== '') {
                    $topIdx = count($stack) - 1;
                    $stack[$topIdx]->add(new NestedInteger(intval($num)));
                    $num = '';
                }
                // Pop completed NestedInteger.
                $completed = array_pop($stack);
                if (!empty($stack)) {
                    $topIdx = count($stack) - 1;
                    $stack[$topIdx]->add($completed);
                } else {
                    // This is the outermost list.
                    return $completed;
                }
            } elseif ($ch === ',') {
                // If there is a pending number, add it to current list.
                if ($num !== '') {
                    $topIdx = count($stack) - 1;
                    $stack[$topIdx]->add(new NestedInteger(intval($num)));
                    $num = '';
                }
            } else { // digit or '-'
                $num .= $ch;
            }
        }

        // Should never reach here for valid input.
        return null;
    }
}
```

## Swift

```swift
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public func isInteger() -> Bool
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     public func getInteger() -> Int
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public func setInteger(value: Int)
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public func add(elem: NestedInteger)
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     public func getList() -> [NestedInteger]
 * }
 */
class Solution {
    func deserialize(_ s: String) -> NestedInteger {
        // Single integer case
        if !s.hasPrefix("[") {
            let ni = NestedInteger()
            ni.setInteger(value: Int(s)!)
            return ni
        }

        var stack = [NestedInteger]()
        var numberBuffer = ""

        for ch in s {
            switch ch {
            case "[":
                // Start a new list
                let ni = NestedInteger()
                stack.append(ni)
            case "]", ",":
                if !numberBuffer.isEmpty {
                    // Flush the pending number into current list
                    let value = Int(numberBuffer)!
                    let numNI = NestedInteger()
                    numNI.setInteger(value: value)
                    stack[stack.count - 1].add(elem: numNI)
                    numberBuffer.removeAll()
                }
                if ch == "]" {
                    // Close current list and attach to previous one if exists
                    if stack.count > 1 {
                        let completed = stack.removeLast()
                        stack[stack.count - 1].add(elem: completed)
                    }
                }
            default:
                // Digit or '-'
                numberBuffer.append(ch)
            }
        }

        // The remaining element on the stack is the result
        return stack.first!
    }
}
```

## Kotlin

```kotlin
/ **
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     constructor()
 *
 *     // Constructor initializes a single integer.
 *     constructor(value: Int)
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     fun isInteger(): Boolean
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     fun getInteger(): Int?
 *
 *     // Set this NestedInteger to hold a single integer.
 *     fun setInteger(value: Int): Unit
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     fun add(ni: NestedInteger): Unit
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     fun getList(): List<NestedInteger>?
 * }
 */
class Solution {
    fun deserialize(s: String): NestedInteger {
        if (s.isEmpty()) return NestedInteger()
        if (s[0] != '[') {
            return NestedInteger(s.toInt())
        }

        val stack = mutableListOf<NestedInteger>()
        var num = 0
        var negative = false
        var haveNum = false

        for (ch in s) {
            when (ch) {
                '[' -> {
                    stack.add(NestedInteger())
                }
                ']', ',' -> {
                    if (haveNum) {
                        val value = if (negative) -num else num
                        stack.last().add(NestedInteger(value))
                        haveNum = false
                        num = 0
                        negative = false
                    }
                    if (ch == ']') {
                        val completed = stack.removeAt(stack.size - 1)
                        if (stack.isNotEmpty()) {
                            stack.last().add(completed)
                        } else {
                            return completed
                        }
                    }
                }
                '-' -> {
                    negative = true
                }
                else -> { // digit
                    haveNum = true
                    num = num * 10 + (ch - '0')
                }
            }
        }

        // Should never reach here for valid input.
        return NestedInteger()
    }
}
```

## Dart

```dart
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   // If [integer] is an int, constructor initializes a single integer.
 *   // Otherwise it initializes an empty nested list.
 *   NestedInteger([int? integer]);
 *
 *   // Returns true if this NestedInteger holds a single integer, rather than a nested list.
 *   bool isInteger();
 *
 *   // Returns the single integer that this NestedInteger holds, if it holds a single integer.
 *   // Returns null if this NestedInteger holds a nested list.
 *   int getInteger();
 *
 *   // Sets this NestedInteger to hold a single integer.
 *   void setInteger(int value);
 *
 *   // Sets this NestedInteger to hold a nested list and adds a nested integer to it.
 *   void add(NestedInteger ni);
 *
 *   // Returns the nested list that this NestedInteger holds, if it holds a nested list.
 *   // Returns empty list if this NestedInteger holds a single integer.
 *   List<NestedInteger> getList();
 * }
 */
class Solution {
  NestedInteger deserialize(String s) {
    if (s.isEmpty) return NestedInteger();

    // Single integer case
    if (s[0] != '[') {
      return NestedInteger(int.parse(s));
    }

    List<NestedInteger> stack = [];
    int i = 0;
    while (i < s.length) {
      String ch = s[i];
      if (ch == '[') {
        // Start a new list
        stack.add(NestedInteger());
        i++;
      } else if (ch == ']') {
        // End current list
        NestedInteger completed = stack.removeLast();
        if (stack.isEmpty) {
          return completed;
        }
        stack.last.add(completed);
        i++;
      } else if (ch == ',') {
        i++; // skip separator
      } else {
        // Parse number (could be negative)
        int start = i;
        while (i < s.length &&
            (s[i] == '-' ||
                (s.codeUnitAt(i) >= '0'.codeUnitAt(0) && s.codeUnitAt(i) <= '9'.codeUnitAt(0)))) {
          i++;
        }
        int num = int.parse(s.substring(start, i));
        NestedInteger ni = NestedInteger(num);
        if (stack.isNotEmpty) {
          stack.last.add(ni);
        } else {
          return ni;
        }
      }
    }

    // Fallback (should not reach here)
    return NestedInteger();
  }
}
```

## Golang

```go
import "strconv"

func deserialize(s string) *NestedInteger {
	if len(s) == 0 {
		return nil
	}
	// Single integer case, no surrounding brackets.
	if s[0] != '[' {
		val, _ := strconv.Atoi(s)
		ni := &NestedInteger{}
		ni.SetInteger(val)
		return ni
	}

	stack := []*NestedInteger{}
	num := 0
	sign := 1
	hasNum := false

	for i := 0; i < len(s); i++ {
		c := s[i]
		switch c {
		case '[':
			// Start a new list.
			ni := &NestedInteger{}
			stack = append(stack, ni)
		case ']':
			if hasNum {
				val := sign * num
				child := &NestedInteger{}
				child.SetInteger(val)
				top := stack[len(stack)-1]
				top.Add(*child)
				num = 0
				sign = 1
				hasNum = false
			}
			// Close current list.
			if len(stack) > 1 {
				child := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				parent := stack[len(stack)-1]
				parent.Add(*child)
			} else {
				return stack[0]
			}
		case ',':
			if hasNum {
				val := sign * num
				child := &NestedInteger{}
				child.SetInteger(val)
				top := stack[len(stack)-1]
				top.Add(*child)
				num = 0
				sign = 1
				hasNum = false
			}
		case '-':
			sign = -1
		default: // digit
			if c >= '0' && c <= '9' {
				hasNum = true
				num = num*10 + int(c-'0')
			}
		}
	}
	return nil
}
```

## Ruby

```ruby
def deserialize(s)
  # Single integer case
  unless s[0] == '['
    ni = NestedInteger.new
    ni.set_integer(s.to_i)
    return ni
  end

  stack = []
  num = nil

  s.each_char do |ch|
    case ch
    when '['
      stack << NestedInteger.new
    when ']'
      if !num.nil?
        integer_ni = NestedInteger.new
        integer_ni.set_integer(num.to_i)
        stack[-1].add(integer_ni)
        num = nil
      end
      completed = stack.pop
      return completed if stack.empty?
      stack[-1].add(completed)
    when ','
      if !num.nil?
        integer_ni = NestedInteger.new
        integer_ni.set_integer(num.to_i)
        stack[-1].add(integer_ni)
        num = nil
      end
    else # digit or '-'
      num = '' if num.nil?
      num << ch
    end
  end

  stack.pop unless stack.empty?
end
```

## Scala

```scala
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * trait NestedInteger {
 *
 *   // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *   def isInteger: Boolean
 *
 *   // Return the single integer that this NestedInteger holds, if it holds a single integer.
 *   def getInteger: Int
 *
 *   // Set this NestedInteger to hold a single integer.
 *   def setInteger(i: Int): Unit
 *
 *   // Return the nested list that this NestedInteger holds, if it holds a nested list.
 *   def getList: Array[NestedInteger]
 *
 *   // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *   def add(ni: NestedInteger): Unit
 * }
 */
object Solution {
  import scala.collection.mutable.Stack

  def deserialize(s: String): NestedInteger = {
    if (s.isEmpty) return null
    // Single integer case
    if (s.charAt(0) != '[') {
      val ni = new NestedInteger()
      ni.setInteger(s.toInt)
      return ni
    }

    val stack = Stack[NestedInteger]()
    val numBuilder = new StringBuilder

    for (c <- s) {
      c match {
        case '[' =>
          // start a new list
          stack.push(new NestedInteger())
        case ']' | ',' =>
          if (numBuilder.nonEmpty) {
            val num = numBuilder.toString().toInt
            val niNum = new NestedInteger()
            niNum.setInteger(num)
            stack.top.add(niNum)
            numBuilder.clear()
          }
          if (c == ']') {
            // finish current list
            val completed = stack.pop()
            if (stack.isEmpty) {
              return completed
            } else {
              stack.top.add(completed)
            }
          }
        case ch =>
          // digit or '-'
          numBuilder.append(ch)
      }
    }
    null
  }
}
```

## Rust

```rust
#[derive(Debug, PartialEq, Eq)]
pub enum NestedInteger {
    Int(i32),
    List(Vec<NestedInteger>),
}

impl Solution {
    pub fn deserialize(s: String) -> NestedInteger {
        let bytes = s.as_bytes();
        let n = bytes.len();
        if n == 0 {
            return NestedInteger::List(vec![]);
        }
        // If the string does not start with '[', it's a single integer.
        if bytes[0] != b'[' {
            let mut i = 0;
            let mut sign = 1i32;
            if bytes[i] == b'-' {
                sign = -1;
                i += 1;
            }
            let mut num = 0i32;
            while i < n && (bytes[i] as char).is_ascii_digit() {
                num = num * 10 + (bytes[i] - b'0') as i32;
                i += 1;
            }
            return NestedInteger::Int(sign * num);
        }

        let mut stack: Vec<Vec<NestedInteger>> = Vec::new();
        let mut i = 0usize;

        while i < n {
            match bytes[i] {
                b'[' => {
                    stack.push(Vec::new());
                    i += 1;
                }
                b']' => {
                    let list_vec = stack.pop().unwrap();
                    let ni = NestedInteger::List(list_vec);
                    if let Some(prev) = stack.last_mut() {
                        prev.push(ni);
                    } else {
                        return ni; // final result
                    }
                    i += 1;
                }
                b',' => {
                    i += 1;
                }
                _ => {
                    // parse number (could be negative)
                    let mut sign = 1i32;
                    if bytes[i] == b'-' {
                        sign = -1;
                        i += 1;
                    }
                    let mut num = 0i32;
                    while i < n && (bytes[i] as char).is_ascii_digit() {
                        num = num * 10 + (bytes[i] - b'0') as i32;
                        i += 1;
                    }
                    let val = sign * num;
                    if let Some(prev) = stack.last_mut() {
                        prev.push(NestedInteger::Int(val));
                    } else {
                        // Should not happen for valid input
                        return NestedInteger::Int(val);
                    }
                }
            }
        }

        // In case the entire string was a single integer without brackets (handled earlier)
        panic!("Invalid serialization");
    }
}
```

## Racket

```racket
#lang racket
(require racket/contract)

;; The NestedInteger class is provided by the platform.
;; It has methods: is-integer, get-integer, set-integer, add, get-list.

(define/contract (deserialize s)
  (-> string? (is-a?/c nested-integer%))
  (let ((len (string-length s)))
    (if (and (> len 0) (not (char=? (string-ref s 0) #\[])))
        ;; The whole string is a single integer.
        (let ((ni (new nested-integer%)))
          (send ni set-integer (string->number s))
          ni)
        ;; Parse a list representation.
        (let loop ((i 0) (stack '()))
          (if (= i len)
              (error "invalid input")
              (let ((ch (string-ref s i)))
                (cond
                  [(char=? ch #\[)
                   (define new-ni (new nested-integer%))
                   (loop (+ i 1) (cons new-ni stack))]
                  [(char=? ch #\])
                   (define completed (car stack))
                   (define rest (cdr stack))
                   (if (null? rest)
                       completed
                       (begin
                         (send (car rest) add completed)
                         (loop (+ i 1) rest)))]
                  [(char=? ch #\,)
                   (loop (+ i 1) stack)]
                  [else ; start of a number (digit or '-')
                   (define start i)
                   (let parse ((j i))
                     (if (or (= j len)
                             (let ((c (string-ref s j)))
                               (or (char=? c #\,) (char=? c #\])))
                         )
                         (let* ((num-str (substring s start j))
                                (num (string->number num-str))
                                (ni (new nested-integer%)))
                           (send ni set-integer num)
                           (send (car stack) add ni)
                           (loop j stack))
                         (parse (+ j 1))))])))))))
```

## Erlang

```erlang
-module(solution).
-export([deserialize/1]).

-spec deserialize(unicode:unicode_binary()) -> nested_integer:nested_integer().
deserialize(S) ->
    Chars = binary_to_list(S),
    parse(Chars, []).

%% Parsing functions
parse([], [Result]) ->
    Result;
parse([], []) ->
    undefined; % should not happen for valid input

%% Skip commas
parse([$, | Rest], Stack) ->
    parse(Rest, Stack);

%% Opening bracket: start a new list
parse([$[ | Rest], Stack) ->
    Empty = nested_integer:new(),
    parse(Rest, [Empty | Stack]);

%% Closing bracket: finish current list and attach to parent if exists
parse([$] | Rest], [Curr | Prev]) ->
    case Prev of
        [] ->
            % This is the outermost list
            parse(Rest, [Curr]);
        [Parent | RestPrev] ->
            UpdatedParent = nested_integer:add(Parent, Curr),
            parse(Rest, [UpdatedParent | RestPrev])
    end;

%% Number (including negative)
parse([C | _] = Chars, Stack) when C == $- orelse (C >= $0 andalso C =< $9) ->
    {Num, RestAfter} = take_number(Chars, []),
    NI = nested_integer:new(Num),
    case Stack of
        [] ->
            parse(RestAfter, [NI]);
        [Top | RestStack] ->
            UpdatedTop = nested_integer:add(Top, NI),
            parse(RestAfter, [UpdatedTop | RestStack])
    end.

%% Helper to read an integer from the character list
take_number([C | Cs], []) when C == $- ->
    take_number(Cs, [C]);
take_number([C | Cs], Acc) when C >= $0, C =< $9 ->
    take_number(Cs, [C | Acc]);
take_number(Rest, Acc) ->
    NumberStr = lists:reverse(Acc),
    {list_to_integer(NumberStr), Rest}.
```

## Elixir

```elixir
defmodule Solution do
  @spec deserialize(s :: String.t) :: :nested_integer.nested_integer
  def deserialize(s) do
    if String.first(s) != "[" do
      :nested_integer.new(String.to_integer(s))
    else
      chars = String.graphemes(s)

      {stack, _} =
        Enum.reduce(chars, {[], ""}, fn ch, {stack, num_buf} ->
          cond do
            ch == "[" ->
              {[ :nested_integer.new() | stack ], ""}

            (ch >= "0" and ch <= "9") or ch == "-" ->
              {stack, num_buf <> ch}

            ch == "," or ch == "]" ->
              # add pending number if any
              {stack2, _} =
                if num_buf != "" do
                  val = String.to_integer(num_buf)
                  elem_ni = :nested_integer.new(val)

                  [top | rest] = stack
                  new_top = :nested_integer.add(top, elem_ni)
                  {[new_top | rest], ""}
                else
                  {stack, ""}
                end

              if ch == "]" do
                # pop completed list and attach to previous if exists
                case stack2 do
                  [completed | rest] ->
                    if rest == [] do
                      {[completed], ""}
                    else
                      [prev | rest2] = rest
                      new_prev = :nested_integer.add(prev, completed)
                      {[new_prev | rest2], ""}
                    end
                end
              else
                {stack2, ""}
              end

            true ->
              {stack, num_buf}
          end
        end)

      [result] = stack
      result
    end
  end
end
```
