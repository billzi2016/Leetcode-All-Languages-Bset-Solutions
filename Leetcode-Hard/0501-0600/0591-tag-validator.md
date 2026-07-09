# 0591. Tag Validator

## Cpp

```cpp
class Solution {
public:
    bool isValid(string code) {
        int n = code.size();
        vector<string> stk;
        for (int i = 0; i < n;) {
            if (code[i] != '<') {
                // plain text must be inside a tag
                if (stk.empty()) return false;
                ++i;
                continue;
            }
            // now code[i] == '<'
            if (i + 1 < n && code[i + 1] == '!') { // CDATA
                if (stk.empty()) return false;
                const string cdataStart = "<![CDATA[";
                if (code.compare(i, cdataStart.size(), cdataStart) != 0) return false;
                size_t pos = code.find("]]>", i + cdataStart.size());
                if (pos == string::npos) return false;
                i = pos + 3; // move past "]]>"
            } else if (i + 1 < n && code[i + 1] == '/') { // end tag
                size_t j = code.find('>', i + 2);
                if (j == string::npos) return false;
                string tagName = code.substr(i + 2, j - (i + 2));
                if (tagName.empty() || tagName.size() > 9) return false;
                for (char c : tagName)
                    if (c < 'A' || c > 'Z') return false;
                if (stk.empty() || stk.back() != tagName) return false;
                stk.pop_back();
                i = j + 1;
                // after closing the outermost tag, nothing should follow
                if (stk.empty() && i != n) return false;
            } else { // start tag
                size_t j = code.find('>', i + 1);
                if (j == string::npos) return false;
                string tagName = code.substr(i + 1, j - (i + 1));
                if (tagName.empty() || tagName.size() > 9) return false;
                for (char c : tagName)
                    if (c < 'A' || c > 'Z') return false;
                stk.push_back(tagName);
                i = j + 1;
            }
        }
        return stk.empty();
    }
};
```

## Java

```java
class Solution {
    public boolean isValid(String code) {
        int n = code.length();
        java.util.Stack<String> stack = new java.util.Stack<>();
        int i = 0;
        while (i < n) {
            if (code.startsWith("<![CDATA[", i)) {
                // CDATA must be inside a tag
                if (stack.isEmpty()) return false;
                int j = code.indexOf("]]>", i + 9);
                if (j == -1) return false;
                i = j + 3; // skip past "]]>"
            } else if (code.startsWith("</", i)) {
                int j = code.indexOf('>', i + 2);
                if (j == -1) return false;
                String tagName = code.substring(i + 2, j);
                if (!isValidTag(tagName)) return false;
                if (stack.isEmpty() || !stack.peek().equals(tagName)) return false;
                stack.pop();
                i = j + 1;
                // after closing the outermost tag, there should be nothing left
                if (stack.isEmpty() && i != n) return false;
            } else if (code.charAt(i) == '<') {
                int j = code.indexOf('>', i + 1);
                if (j == -1) return false;
                String tagName = code.substring(i + 1, j);
                if (!isValidTag(tagName)) return false;
                stack.push(tagName);
                i = j + 1;
            } else {
                // plain text character
                if (stack.isEmpty()) return false; // text outside any tag
                if (code.charAt(i) == '>') return false; // stray '>'
                i++;
            }
        }
        return stack.isEmpty();
    }

    private boolean isValidTag(String s) {
        int len = s.length();
        if (len < 1 || len > 9) return false;
        for (int k = 0; k < len; k++) {
            char c = s.charAt(k);
            if (c < 'A' || c > 'Z') return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        n = len(code)
        stack = []
        i = 0
        while i < n:
            if code[i] == '<':
                # CDATA section
                if i + 9 <= n and code.startswith("<![CDATA[", i):
                    if not stack:
                        return False
                    end = code.find("]]>", i + 9)
                    if end == -1:
                        return False
                    i = end + 3
                # End tag
                elif i + 2 < n and code[i+1] == '/':
                    j = code.find('>', i+2)
                    if j == -1:
                        return False
                    tag = code[i+2:j]
                    if not (1 <= len(tag) <= 9 and all('A' <= c <= 'Z' for c in tag)):
                        return False
                    if not stack or stack[-1] != tag:
                        return False
                    stack.pop()
                    i = j + 1
                    # after closing root, nothing should follow
                    if not stack and i != n:
                        return False
                # Start tag
                else:
                    j = code.find('>', i+1)
                    if j == -1:
                        return False
                    tag = code[i+1:j]
                    if not (1 <= len(tag) <= 9 and all('A' <= c <= 'Z' for c in tag)):
                        return False
                    stack.append(tag)
                    i = j + 1
            else:
                # plain text, must be inside a tag
                if not stack:
                    return False
                i += 1
        return not stack
```

## Python3

```python
class Solution:
    def isValid(self, code: str) -> bool:
        n = len(code)
        stack = []
        i = 0
        while i < n:
            if code[i] != '<':
                # plain text must be inside a tag
                if not stack:
                    return False
                i += 1
                continue

            # At this point, code[i] == '<'
            if code.startswith("<![CDATA[", i):
                # CDATA section, must be inside an open tag
                if not stack:
                    return False
                end = code.find("]]>", i)
                if end == -1:
                    return False
                i = end + 3
            elif i + 1 < n and code[i + 1] == '/':
                # End tag
                j = code.find('>', i)
                if j == -1:
                    return False
                tag = code[i + 2:j]
                if not (1 <= len(tag) <= 9 and tag.isupper()):
                    return False
                if not stack or stack[-1] != tag:
                    return False
                stack.pop()
                i = j + 1
                # after closing outermost tag, there should be no more characters
                if not stack and i != n:
                    return False
            else:
                # Start tag
                j = code.find('>', i)
                if j == -1:
                    return False
                tag = code[i + 1:j]
                if not (1 <= len(tag) <= 9 and tag.isupper()):
                    return False
                stack.append(tag)
                i = j + 1

        return not stack
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

bool isValid(char* code) {
    int n = (int)strlen(code);
    if (n == 0 || code[0] != '<') return false;

    char *stack[200];
    int top = -1; // empty stack

    int i = 0;
    while (i < n) {
        if (code[i] == '<') {
            if (i + 1 < n && code[i + 1] == '/') { // end tag
                int j = i + 2;
                while (j < n && code[j] != '>') j++;
                if (j == n) return false; // no closing '>'
                int len = j - (i + 2);
                if (len < 1 || len > 9) return false;
                for (int k = i + 2; k < j; ++k)
                    if (!isupper((unsigned char)code[k])) return false;

                if (top == -1) return false;
                if ((int)strlen(stack[top]) != len ||
                    strncmp(stack[top], code + i + 2, len) != 0) {
                    return false;
                }
                free(stack[top]);
                top--;

                i = j + 1;
                if (top == -1 && i != n) return false; // extra chars after outermost tag
            } else if (i + 1 < n && code[i + 1] == '!') { // CDATA
                const char *cdataStart = "<![CDATA[";
                int startLen = 9;
                if (top == -1) return false; // must be inside a tag
                if (i + startLen > n) return false;
                if (strncmp(code + i, cdataStart, startLen) != 0) return false;

                int j = i + startLen;
                bool found = false;
                while (j + 2 < n) {
                    if (code[j] == ']' && code[j + 1] == ']' && code[j + 2] == '>') {
                        found = true;
                        break;
                    }
                    ++j;
                }
                if (!found) return false;
                i = j + 3; // move past "]]>"
            } else { // start tag
                int j = i + 1;
                while (j < n && code[j] != '>') j++;
                if (j == n) return false; // no closing '>'
                int len = j - (i + 1);
                if (len < 1 || len > 9) return false;
                for (int k = i + 1; k < j; ++k)
                    if (!isupper((unsigned char)code[k])) return false;

                // push tag name
                char *tag = (char *)malloc(len + 1);
                memcpy(tag, code + i + 1, len);
                tag[len] = '\0';
                stack[++top] = tag;

                i = j + 1;
            }
        } else {
            // plain text character must be inside a tag
            if (top == -1) return false;
            ++i;
        }
    }

    return top == -1;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsValid(string code)
    {
        int n = code.Length;
        var stack = new System.Collections.Generic.Stack<string>();
        int i = 0;

        while (i < n)
        {
            if (code[i] != '<')
            {
                // plain text must be inside a tag
                if (stack.Count == 0) return false;
                i++;
                continue;
            }

            // now code[i] == '<'
            if (i + 1 < n && code[i + 1] == '!')
            {
                // CDATA section, only valid inside an opened tag
                if (stack.Count == 0) return false;
                const string cdataStart = "<![CDATA[";
                if (i + cdataStart.Length > n || !code.Substring(i, cdataStart.Length).Equals(cdataStart))
                    return false;

                int endIdx = code.IndexOf("]]>", i + cdataStart.Length);
                if (endIdx == -1) return false;
                i = endIdx + 3; // skip past "]]>"
            }
            else if (i + 1 < n && code[i + 1] == '/')
            {
                // End tag
                int j = code.IndexOf('>', i + 2);
                if (j == -1) return false;
                string tagName = code.Substring(i + 2, j - (i + 2));
                if (!IsValidTagName(tagName)) return false;
                if (stack.Count == 0 || stack.Peek() != tagName) return false;

                stack.Pop();
                i = j + 1;

                // If all tags closed but not at end, invalid
                if (stack.Count == 0 && i != n) return false;
            }
            else
            {
                // Start tag
                int j = code.IndexOf('>', i + 1);
                if (j == -1) return false;
                string tagName = code.Substring(i + 1, j - (i + 1));
                if (!IsValidTagName(tagName)) return false;

                stack.Push(tagName);
                i = j + 1;
            }
        }

        return stack.Count == 0;
    }

    private bool IsValidTagName(string tag)
    {
        if (tag.Length < 1 || tag.Length > 9) return false;
        foreach (char c in tag)
        {
            if (c < 'A' || c > 'Z') return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} code
 * @return {boolean}
 */
var isValid = function(code) {
    const n = code.length;
    const stack = [];
    let i = 0;
    while (i < n) {
        if (code[i] === '<') {
            // CDATA section
            if (i + 1 < n && code[i + 1] === '!') {
                if (stack.length === 0) return false;
                const cdataStart = "<![CDATA[";
                if (!code.startsWith(cdataStart, i)) return false;
                const endIdx = code.indexOf("]]>", i + cdataStart.length);
                if (endIdx === -1) return false;
                i = endIdx + 3; // move past "]]>"
            }
            // End tag
            else if (i + 1 < n && code[i + 1] === '/') {
                const j = code.indexOf('>', i);
                if (j === -1) return false;
                const name = code.substring(i + 2, j);
                if (!/^[A-Z]{1,9}$/.test(name)) return false;
                if (stack.length === 0 || stack[stack.length - 1] !== name) return false;
                stack.pop();
                i = j + 1;
                // after closing outermost tag, nothing should remain
                if (stack.length === 0 && i < n) return false;
            }
            // Start tag
            else {
                const j = code.indexOf('>', i);
                if (j === -1) return false;
                const name = code.substring(i + 1, j);
                if (!/^[A-Z]{1,9}$/.test(name)) return false;
                stack.push(name);
                i = j + 1;
            }
        } else {
            // regular character must be inside a tag
            if (stack.length === 0) return false;
            i++;
        }
    }
    return stack.length === 0;
};
```

## Typescript

```typescript
function isValid(code: string): boolean {
    const n = code.length;
    let i = 0;
    const stack: string[] = [];

    while (i < n) {
        if (code[i] !== '<') {
            // plain text must be inside a tag
            if (stack.length === 0) return false;
            i++;
            continue;
        }

        // At this point code[i] == '<'
        if (i + 9 <= n && code.startsWith("<![CDATA[", i)) {
            // CDATA section, allowed only inside a tag
            if (stack.length === 0) return false;
            const j = code.indexOf("]]>", i + 9);
            if (j === -1) return false;
            i = j + 3; // skip past "]]>"
        } else if (i + 2 < n && code[i + 1] === '/') {
            // End tag
            const j = code.indexOf('>', i + 2);
            if (j === -1) return false;
            const tagName = code.substring(i + 2, j);
            if (!/^[A-Z]{1,9}$/.test(tagName)) return false;
            if (stack.length === 0 || stack[stack.length - 1] !== tagName) return false;
            stack.pop();
            i = j + 1;
            // After closing the outermost tag, there should be nothing left
            if (stack.length === 0 && i !== n) return false;
        } else {
            // Start tag
            const j = code.indexOf('>', i + 1);
            if (j === -1) return false;
            const tagName = code.substring(i + 1, j);
            if (!/^[A-Z]{1,9}$/.test(tagName)) return false;
            stack.push(tagName);
            i = j + 1;
        }
    }

    return stack.length === 0;
}
```

## Php

```php
class Solution {

    /**
     * @param String $code
     * @return Boolean
     */
    function isValid($code) {
        $n = strlen($code);
        $i = 0;
        $stack = [];

        while ($i < $n) {
            if ($code[$i] === '<') {
                // CDATA section
                if ($i + 9 <= $n && substr($code, $i, 9) === '<![CDATA[') {
                    if (empty($stack)) return false;
                    $closePos = strpos($code, ']]>', $i + 9);
                    if ($closePos === false) return false;
                    $i = $closePos + 3;
                }
                // End tag
                elseif ($i + 2 < $n && $code[$i + 1] === '/') {
                    $gtPos = strpos($code, '>', $i + 2);
                    if ($gtPos === false) return false;
                    $tagName = substr($code, $i + 2, $gtPos - ($i + 2));
                    if (!$this->validTagName($tagName)) return false;
                    if (empty($stack) || array_pop($stack) !== $tagName) return false;
                    $i = $gtPos + 1;
                    // After closing the outermost tag, there should be no more characters
                    if (empty($stack) && $i != $n) return false;
                }
                // Start tag
                else {
                    $gtPos = strpos($code, '>', $i + 1);
                    if ($gtPos === false) return false;
                    $tagName = substr($code, $i + 1, $gtPos - ($i + 1));
                    if (!$this->validTagName($tagName)) return false;
                    array_push($stack, $tagName);
                    $i = $gtPos + 1;
                }
            } else {
                // Plain text character
                if (empty($stack)) return false;
                $i++;
            }
        }

        return empty($stack);
    }

    private function validTagName($tag) {
        $len = strlen($tag);
        if ($len < 1 || $len > 9) return false;
        for ($i = 0; $i < $len; $i++) {
            $c = $tag[$i];
            if ($c < 'A' || $c > 'Z') return false;
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func isValid(_ code: String) -> Bool {
        var stack = [String]()
        let chars = Array(code)
        let n = chars.count
        var i = 0
        
        func isUppercaseLetter(_ c: Character) -> Bool {
            guard let v = c.unicodeScalars.first?.value else { return false }
            return v >= 65 && v <= 90 // 'A' to 'Z'
        }
        
        while i < n {
            if chars[i] == "<" {
                if i + 1 >= n { return false }
                
                // CDATA section
                if chars[i + 1] == "!" {
                    if stack.isEmpty { return false }
                    let cdataStart = Array("<![CDATA[")
                    if i + cdataStart.count > n { return false }
                    var match = true
                    for k in 0..<cdataStart.count {
                        if chars[i + k] != cdataStart[k] {
                            match = false
                            break
                        }
                    }
                    if !match { return false }
                    i += cdataStart.count
                    var foundEnd = false
                    while i + 2 < n {
                        if chars[i] == "]" && chars[i + 1] == "]" && chars[i + 2] == ">" {
                            foundEnd = true
                            i += 3
                            break
                        }
                        i += 1
                    }
                    if !foundEnd { return false }
                }
                // End tag
                else if chars[i + 1] == "/" {
                    var j = i + 2
                    var tagName = ""
                    while j < n && chars[j] != ">" {
                        let c = chars[j]
                        if !isUppercaseLetter(c) { return false }
                        tagName.append(c)
                        j += 1
                    }
                    if j == n || chars[j] != ">" { return false }
                    if tagName.isEmpty || tagName.count > 9 { return false }
                    if stack.isEmpty || stack.last! != tagName { return false }
                    stack.removeLast()
                    i = j + 1
                    // No characters allowed after the outermost closing tag
                    if stack.isEmpty && i != n {
                        return false
                    }
                }
                // Start tag
                else {
                    var j = i + 1
                    var tagName = ""
                    while j < n && chars[j] != ">" {
                        let c = chars[j]
                        if !isUppercaseLetter(c) { return false }
                        tagName.append(c)
                        j += 1
                    }
                    if j == n || chars[j] != ">" { return false }
                    if tagName.isEmpty || tagName.count > 9 { return false }
                    stack.append(tagName)
                    i = j + 1
                }
            } else {
                // Plain text character; must be inside a tag
                if stack.isEmpty { return false }
                i += 1
            }
        }
        return stack.isEmpty
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isValid(code: String): Boolean {
        val n = code.length
        var i = 0
        val stack = ArrayDeque<String>()
        while (i < n) {
            if (code[i] != '<') {
                if (stack.isEmpty()) return false
                i++
                continue
            }
            // now at '<'
            if (i + 1 < n && code[i + 1] == '!') {
                // CDATA section
                if (stack.isEmpty()) return false
                val cdataStart = "<![CDATA["
                if (!code.startsWith(cdataStart, i)) return false
                val j = code.indexOf("]]>", i + cdataStart.length)
                if (j == -1) return false
                i = j + 3
            } else if (i + 1 < n && code[i + 1] == '/') {
                // end tag
                val j = code.indexOf('>', i + 2)
                if (j == -1) return false
                val tagName = code.substring(i + 2, j)
                if (!isValidTag(tagName)) return false
                if (stack.isEmpty() || stack.peekLast() != tagName) return false
                stack.removeLast()
                i = j + 1
                // after closing the outermost tag, nothing should remain
                if (stack.isEmpty() && i != n) return false
            } else {
                // start tag
                val j = code.indexOf('>', i + 1)
                if (j == -1) return false
                val tagName = code.substring(i + 1, j)
                if (!isValidTag(tagName)) return false
                stack.addLast(tagName)
                i = j + 1
            }
        }
        return stack.isEmpty()
    }

    private fun isValidTag(s: String): Boolean {
        if (s.length < 1 || s.length > 9) return false
        for (ch in s) {
            if (ch !in 'A'..'Z') return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool isValid(String code) {
    int n = code.length;
    List<String> stack = [];
    int i = 0;

    while (i < n) {
      if (code[i] == '<') {
        // CDATA
        if (i + 1 < n && code[i + 1] == '!') {
          if (stack.isEmpty) return false;
          const String cdataStart = "<![CDATA[";
          if (!code.startsWith(cdataStart, i)) return false;
          int endIdx = code.indexOf("]]>", i + cdataStart.length);
          if (endIdx == -1) return false;
          i = endIdx + 3;
        }
        // Closing tag
        else if (i + 1 < n && code[i + 1] == '/') {
          int j = code.indexOf('>', i + 2);
          if (j == -1) return false;
          String tagName = code.substring(i + 2, j);
          if (!_isValidTag(tagName)) return false;
          if (stack.isEmpty || stack.last != tagName) return false;
          stack.removeLast();
          i = j + 1;
          // after closing outermost tag, nothing should remain
          if (stack.isEmpty && i != n) return false;
        }
        // Opening tag
        else {
          int j = code.indexOf('>', i + 1);
          if (j == -1) return false;
          String tagName = code.substring(i + 1, j);
          if (!_isValidTag(tagName)) return false;
          stack.add(tagName);
          i = j + 1;
        }
      } else {
        // Text character
        if (stack.isEmpty) return false;
        i++;
      }
    }

    return stack.isEmpty;
  }

  bool _isValidTag(String tag) {
    if (tag.length < 1 || tag.length > 9) return false;
    for (int i = 0; i < tag.length; i++) {
      int codeUnit = tag.codeUnitAt(i);
      if (codeUnit < 65 || codeUnit > 90) return false; // not 'A'-'Z'
    }
    return true;
  }
}
```

## Golang

```go
import "strings"

func isValid(code string) bool {
	n := len(code)
	var stack []string
	i := 0
	for i < n {
		if code[i] != '<' {
			if len(stack) == 0 {
				return false
			}
			i++
			continue
		}
		// CDATA section
		if strings.HasPrefix(code[i:], "<![CDATA[") {
			if len(stack) == 0 {
				return false
			}
			end := strings.Index(code[i+9:], "]]>")
			if end == -1 {
				return false
			}
			i = i + 9 + end + 3
			continue
		}
		// End tag
		if i+1 < n && code[i+1] == '/' {
			j := strings.IndexByte(code[i+2:], '>')
			if j == -1 {
				return false
			}
			tag := code[i+2 : i+2+j]
			if len(tag) < 1 || len(tag) > 9 {
				return false
			}
			for _, ch := range tag {
				if ch < 'A' || ch > 'Z' {
					return false
				}
			}
			if len(stack) == 0 || stack[len(stack)-1] != tag {
				return false
			}
			stack = stack[:len(stack)-1]
			i = i + 2 + j + 1
			if len(stack) == 0 && i != n {
				return false
			}
			continue
		}
		// Start tag
		j := strings.IndexByte(code[i+1:], '>')
		if j == -1 {
			return false
		}
		tag := code[i+1 : i+1+j]
		if len(tag) < 1 || len(tag) > 9 {
			return false
		}
		for _, ch := range tag {
			if ch < 'A' || ch > 'Z' {
				return false
			}
		}
		stack = append(stack, tag)
		i = i + 1 + j + 1
	}
	return len(stack) == 0
}
```

## Ruby

```ruby
def is_valid(code)
  n = code.length
  stack = []
  i = 0
  valid_name = ->(name) { name.length.between?(1, 9) && name =~ /\A[A-Z]+\z/ }

  while i < n
    if code[i] == '<'
      if i + 1 < n && code[i + 1] == '!'
        # CDATA section
        return false if stack.empty?
        cdata_start = "<![CDATA["
        return false unless code[i, cdata_start.length] == cdata_start

        close_idx = code.index("]]>", i + cdata_start.length)
        return false if close_idx.nil?

        i = close_idx + 3
      elsif i + 1 < n && code[i + 1] == '/'
        # End tag
        j = code.index('>', i + 2)
        return false if j.nil?

        name = code[(i + 2)...j]
        return false unless valid_name.call(name)
        return false if stack.empty? || stack[-1] != name

        stack.pop
        i = j + 1
        # after closing the outermost tag, nothing should remain
        return false if stack.empty? && i != n
      else
        # Start tag
        j = code.index('>', i + 1)
        return false if j.nil?

        name = code[(i + 1)...j]
        return false unless valid_name.call(name)

        stack << name
        i = j + 1
      end
    else
      # Text character, must be inside a tag
      return false if stack.empty?
      i += 1
    end
  end

  stack.empty?
end
```

## Scala

```scala
object Solution {
  def isValid(code: String): Boolean = {
    val n = code.length
    var i = 0
    val stack = new scala.collection.mutable.Stack[String]()
    while (i < n) {
      if (code.charAt(i) == '<') {
        if (i + 1 >= n) return false
        if (code.startsWith("<![CDATA[", i)) {
          // CDATA must be inside a tag
          if (stack.isEmpty) return false
          val end = code.indexOf("]]>", i + 9)
          if (end == -1) return false
          i = end + 3
        } else if (code.startsWith("</", i)) {
          // End tag
          val j = code.indexOf('>', i + 2)
          if (j == -1) return false
          val name = code.substring(i + 2, j)
          if (!validTagName(name)) return false
          if (stack.isEmpty || stack.top != name) return false
          stack.pop()
          i = j + 1
          // after closing outermost tag, nothing should remain
          if (stack.isEmpty && i < n) return false
        } else {
          // Start tag
          val j = code.indexOf('>', i + 1)
          if (j == -1) return false
          val name = code.substring(i + 1, j)
          if (!validTagName(name)) return false
          // first tag must start at position 0
          if (stack.isEmpty && i != 0) return false
          stack.push(name)
          i = j + 1
        }
      } else {
        i += 1
      }
    }
    stack.isEmpty
  }

  private def validTagName(s: String): Boolean = {
    if (s.length < 1 || s.length > 9) return false
    for (c <- s) {
      if (c < 'A' || c > 'Z') return false
    }
    true
  }
}
```

## Rust

```rust
impl Solution {
    pub fn is_valid(code: String) -> bool {
        let bytes = code.as_bytes();
        let n = bytes.len();
        let mut i = 0usize;
        let mut stack: Vec<String> = Vec::new();

        while i < n {
            if bytes[i] != b'<' {
                // plain text must be inside a tag
                if stack.is_empty() {
                    return false;
                }
                i += 1;
                continue;
            }

            // CDATA section
            if i + 9 <= n && &bytes[i..i + 9] == b"<![CDATA[" {
                if stack.is_empty() {
                    return false;
                }
                let mut j = i + 9;
                let mut found = false;
                while j + 3 <= n {
                    if &bytes[j..j + 3] == b"]]>".as_ref() {
                        found = true;
                        break;
                    }
                    j += 1;
                }
                if !found {
                    return false;
                }
                i = j + 3; // move past "]]>"
                continue;
            }

            // Tag (start or end)
            let is_end = i + 1 < n && bytes[i + 1] == b'/';
            let name_start = if is_end { i + 2 } else { i + 1 };
            let mut j = name_start;
            while j < n && bytes[j] != b'>' {
                j += 1;
            }
            if j == n {
                return false; // no closing '>'
            }

            let name_bytes = &bytes[name_start..j];
            // validate tag name
            if name_bytes.is_empty() || name_bytes.len() > 9 {
                return false;
            }
            for &c in name_bytes {
                if c < b'A' || c > b'Z' {
                    return false;
                }
            }
            let name = unsafe { std::str::from_utf8_unchecked(name_bytes) }.to_string();

            if is_end {
                // end tag
                if stack.is_empty() || *stack.last().unwrap() != name {
                    return false;
                }
                stack.pop();
                i = j + 1;
                // after closing the outermost tag, nothing should remain
                if stack.is_empty() && i != n {
                    return false;
                }
            } else {
                // start tag
                stack.push(name);
                i = j + 1;
            }
        }

        stack.is_empty()
    }
}
```

## Racket

```racket
(define (find-substring s sub start)
  (let ((len-s (string-length s))
        (len-sub (string-length sub)))
    (let loop ((i start))
      (if (> (+ i len-sub) len-s)
          #f
          (if (string=? (substring s i (+ i len-sub)) sub)
              i
              (loop (+ i 1)))))))

(define (find-char s ch start)
  (let ((len (string-length s)))
    (let loop ((i start))
      (if (>= i len)
          #f
          (if (char=? (string-ref s i) ch)
              i
              (loop (+ i 1)))))))

(define (valid-tag-name? name)
  (let ((len (string-length name)))
    (and (>= len 1) (<= len 9)
         (let loop ((i 0))
           (if (= i len)
               #t
               (let ((c (string-ref name i)))
                 (and (char>=? c #\A) (char<=? c #\Z)
                      (loop (+ i 1)))))))))

(define/contract (is-valid code)
  (-> string? boolean?)
  (let ((n (string-length code)))
    (let loop ((i 0) (stack '()))
      (cond
        [(= i n) (null? stack)]
        [else
         (cond
           ;; CDATA
           [(and (<= (+ i 9) n)
                 (string=? (substring code i (+ i 9)) "<![CDATA["))
            (if (null? stack)
                #f
                (let ((end (find-substring code "]]>" (+ i 9))))
                  (if (not end)
                      #f
                      (loop (+ end 3) stack))))]
           ;; End tag
           [(and (< i n) (char=? (string-ref code i) #\<)
                 (< (+ i 1) n) (char=? (string-ref code (+ i 1)) #\/))
            (let ((gt (find-char code #\> (+ i 2))))
              (if (not gt)
                  #f
                  (let ((name (substring code (+ i 2) gt)))
                    (if (and (valid-tag-name? name)
                             (pair? stack)
                             (string=? (car stack) name))
                        (let ((new-stack (cdr stack))
                              (new-i (+ gt 1)))
                          (if (and (null? new-stack) (< new-i n))
                              #f
                              (loop new-i new-stack)))
                        #f))))]
           ;; Start tag
           [(char=? (string-ref code i) #\<)
            (let ((gt (find-char code #\> (+ i 1))))
              (if (not gt)
                  #f
                  (let ((name (substring code (+ i 1) gt)))
                    (if (valid-tag-name? name)
                        (loop (+ gt 1) (cons name stack))
                        #f))))]
           ;; Text character
           [else
            (if (null? stack)
                #f
                (loop (+ i 1) stack))]))))))
```

## Erlang

```erlang
-module(solution).
-export([is_valid/1]).

-spec is_valid(Code :: unicode:unicode_binary()) -> boolean().
is_valid(Code) ->
    List = unicode:characters_to_list(Code),
    go(List, []).

%% Main parser
go([], []) -> true;
go([], _) -> false;
go([$< | Rest], Stack) ->
    case Rest of
        [$!,$[,$C,$D,$A,$T,$A,$[ | AfterCdata] ] ->
            case Stack of
                [] -> false;
                _  -> skip_cdata(AfterCdata, Stack)
            end;
        [$/ | AfterSlash] ->
            parse_end_tag(AfterSlash, Stack);
        _ ->
            parse_start_tag(Rest, Stack)
    end;
go([_Char | Rest], []) -> false;   % text outside any tag
go([_Char | Rest], Stack) -> go(Rest, Stack).

%% Skip CDATA section, assumes it starts after "<![CDATA["
skip_cdata(List, Stack) ->
    case find_cdata_end(List) of
        {ok, After} -> go(After, Stack);
        error       -> false
    end.

find_cdata_end([]) -> error;
find_cdata_end([ $], $], $> | Rest]) -> {ok, Rest};
find_cdata_end([_ | Tail]) -> find_cdata_end(Tail).

%% Parse a start tag: assumes we are after '<'
parse_start_tag(Chars, Stack) ->
    case read_until_gt(Chars, []) of
        {ok, Name, After} ->
            go(After, [Name | Stack]);
        false -> false
    end.

%% Parse an end tag: assumes we are after "</"
parse_end_tag(Chars, Stack) ->
    case read_until_gt(Chars, []) of
        {ok, Name, After} ->
            case Stack of
                [Top | RestStack] when Top =:= Name ->
                    case RestStack of
                        [] -> % root tag closed
                            case After of
                                [] -> true;
                                _  -> false
                            end;
                        _  -> go(After, RestStack)
                    end;
                _ -> false
            end;
        false -> false
    end.

%% Read characters until '>', collecting name characters.
read_until_gt([], _) -> false; % no closing '>'
read_until_gt([ $> | Rest], Acc) ->
    Name = lists:reverse(Acc),
    case valid_tag_name(Name) of
        true  -> {ok, Name, Rest};
        false -> false
    end;
read_until_gt([C | Rest], Acc) when C >= $A, C =< $Z ->
    read_until_gt(Rest, [C | Acc]);
read_until_gt(_, _) -> false. % invalid character in tag name

%% Validate tag name length (1 to 9). Characters are already uppercase.
valid_tag_name(Name) ->
    Len = length(Name),
    Len >= 1 andalso Len =< 9.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_valid(code :: String.t) :: boolean
  def is_valid(code) do
    parse(code, 0, [])
  end

  # Main parsing function
  defp parse(code, i, stack) do
    len = byte_size(code)

    cond do
      i == len ->
        stack == []

      true ->
        <<_::binary-size(i), c::utf8, _rest::binary>> = code

        if c == ?< do
          # Ensure there is a next character
          if i + 1 >= len do
            false
          else
            <<_::binary-size(i + 1), nxt::utf8, _::binary>> = code

            cond do
              nxt == ?! ->
                # CDATA section, must be inside a tag
                if stack == [] do
                  false
                else
                  if String.slice(code, i, 9) != "<![CDATA[" do
                    false
                  else
                    end_idx = find_substring(code, i + 9, "]]>")
                    if end_idx == -1 do
                      false
                    else
                      parse(code, end_idx + 3, stack)
                    end
                  end
                end

              nxt == ?/ ->
                # End tag
                close_idx = find_char(code, i + 2, ?>)
                if close_idx == -1 do
                  false
                else
                  name = String.slice(code, i + 2, close_idx - (i + 2))

                  cond do
                    not valid_tag_name?(name) ->
                      false

                    stack == [] or hd(stack) != name ->
                      false

                    true ->
                      new_stack = tl(stack)
                      new_i = close_idx + 1

                      if new_stack == [] and new_i != len do
                        false
                      else
                        parse(code, new_i, new_stack)
                      end
                  end
                end

              true ->
                # Start tag
                close_idx = find_char(code, i + 1, ?>)

                if close_idx == -1 do
                  false
                else
                  name = String.slice(code, i + 1, close_idx - (i + 1))

                  if valid_tag_name?(name) do
                    parse(code, close_idx + 1, [name | stack])
                  else
                    false
                  end
                end
            end
          end
        else
          # Regular character; must be inside a tag
          if stack == [] do
            false
          else
            parse(code, i + 1, stack)
          end
        end
    end
  end

  # Find the index of a single character starting from `start`
  defp find_char(code, start, char) do
    sub = String.slice(code, start, byte_size(code) - start)

    case String.index(sub, <<char>>) do
      nil -> -1
      idx -> start + idx
    end
  end

  # Find the index of a substring starting from `start`
  defp find_substring(code, start, pat) do
    sub = String.slice(code, start, byte_size(code) - start)

    case String.index(sub, pat) do
      nil -> -1
      idx -> start + idx
    end
  end

  # Validate tag name: length 1..9 and all uppercase letters
  defp valid_tag_name?(name) do
    len = byte_size(name)

    if len < 1 or len > 9 do
      false
    else
      name
      |> :binary.bin_to_list()
      |> Enum.all?(fn c -> c >= ?A and c <= ?Z end)
    end
  end
end
```
