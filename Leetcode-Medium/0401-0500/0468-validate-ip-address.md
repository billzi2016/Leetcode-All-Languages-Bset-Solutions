# 0468. Validate IP Address

## Cpp

```cpp
class Solution {
public:
    string validIPAddress(string queryIP) {
        if (queryIP.find('.') != string::npos && queryIP.find(':') == string::npos) {
            return isIPv4(queryIP) ? "IPv4" : "Neither";
        }
        if (queryIP.find(':') != string::npos && queryIP.find('.') == string::npos) {
            return isIPv6(queryIP) ? "IPv6" : "Neither";
        }
        return "Neither";
    }

private:
    bool isIPv4(const string& ip) {
        vector<string> parts;
        string cur;
        for (char c : ip) {
            if (c == '.') {
                parts.push_back(cur);
                cur.clear();
            } else {
                if (!isdigit(c)) return false;
                cur.push_back(c);
            }
        }
        parts.push_back(cur);
        if (parts.size() != 4) return false;
        for (const string& p : parts) {
            if (p.empty() || p.size() > 3) return false;
            if (p[0] == '0' && p.size() > 1) return false; // leading zero
            int val = 0;
            for (char d : p) {
                val = val * 10 + (d - '0');
            }
            if (val < 0 || val > 255) return false;
        }
        return true;
    }

    bool isIPv6(const string& ip) {
        vector<string> parts;
        string cur;
        for (char c : ip) {
            if (c == ':') {
                parts.push_back(cur);
                cur.clear();
            } else {
                if (!isxdigit(c)) return false;
                cur.push_back(c);
            }
        }
        parts.push_back(cur);
        if (parts.size() != 8) return false;
        for (const string& p : parts) {
            if (p.empty() || p.size() > 4) return false;
            // characters already validated as hex digits
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public String validIPAddress(String queryIP) {
        if (queryIP == null || queryIP.isEmpty()) return "Neither";
        boolean hasDot = queryIP.indexOf('.') >= 0;
        boolean hasColon = queryIP.indexOf(':') >= 0;
        if (hasDot && !hasColon) {
            String[] parts = queryIP.split("\\.", -1);
            if (parts.length != 4) return "Neither";
            for (String part : parts) {
                if (!isValidIPv4Part(part)) return "Neither";
            }
            return "IPv4";
        } else if (hasColon && !hasDot) {
            String[] parts = queryIP.split(":", -1);
            if (parts.length != 8) return "Neither";
            for (String part : parts) {
                if (!isValidIPv6Part(part)) return "Neither";
            }
            return "IPv6";
        } else {
            return "Neither";
        }
    }

    private boolean isValidIPv4Part(String s) {
        if (s == null || s.isEmpty() || s.length() > 3) return false;
        // no leading zeros unless the part is exactly "0"
        if (s.charAt(0) == '0' && s.length() != 1) return false;
        for (char c : s.toCharArray()) {
            if (!Character.isDigit(c)) return false;
        }
        try {
            int val = Integer.parseInt(s);
            if (val < 0 || val > 255) return false;
        } catch (NumberFormatException e) {
            return false;
        }
        return true;
    }

    private boolean isValidIPv6Part(String s) {
        if (s == null || s.isEmpty() || s.length() > 4) return false;
        for (char c : s.toCharArray()) {
            if (Character.digit(c, 16) == -1) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        if '.' in queryIP and ':' not in queryIP:
            parts = queryIP.split('.')
            if len(parts) != 4:
                return "Neither"
            for p in parts:
                if not p or (len(p) > 1 and p[0] == '0'):
                    return "Neither"
                if not p.isdigit():
                    return "Neither"
                if int(p) < 0 or int(p) > 255:
                    return "Neither"
            return "IPv4"
        elif ':' in queryIP and '.' not in queryIP:
            parts = queryIP.split(':')
            if len(parts) != 8:
                return "Neither"
            hex_digits = set("0123456789abcdefABCDEF")
            for p in parts:
                if not (1 <= len(p) <= 4):
                    return "Neither"
                if any(c not in hex_digits for c in p):
                    return "Neither"
            return "IPv6"
        else:
            return "Neither"
```

## Python3

```python
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP and ':' not in queryIP:
            parts = queryIP.split('.')
            if len(parts) != 4:
                return "Neither"
            for p in parts:
                if not p or (len(p) > 1 and p[0] == '0'):
                    return "Neither"
                if not p.isdigit():
                    return "Neither"
                if int(p) > 255:
                    return "Neither"
            return "IPv4"
        elif ':' in queryIP and '.' not in queryIP:
            parts = queryIP.split(':')
            if len(parts) != 8:
                return "Neither"
            hex_digits = set("0123456789abcdefABCDEF")
            for p in parts:
                if not (1 <= len(p) <= 4):
                    return "Neither"
                if any(c not in hex_digits for c in p):
                    return "Neither"
            return "IPv6"
        else:
            return "Neither"
```

## C

```c
#include <string.h>
#include <ctype.h>

static int isIPv4(const char *ip) {
    const char *p = ip;
    int parts = 0;
    while (*p) {
        if (parts == 4) return 0;          // too many parts
        const char *start = p;
        int len = 0, val = 0;
        while (*p && *p != '.') {
            if (!isdigit((unsigned char)*p)) return 0;
            val = val * 10 + (*p - '0');
            if (val > 255) return 0;
            ++len;
            ++p;
        }
        if (len == 0) return 0;             // empty part
        if (len > 1 && start[0] == '0') return 0; // leading zero
        ++parts;
        if (*p == '.') {
            ++p;                            // skip dot
            if (!*p) return 0;              // trailing dot
        }
    }
    return parts == 4;
}

static int isIPv6(const char *ip) {
    const char *p = ip;
    int parts = 0;
    while (*p) {
        if (parts == 8) return 0;          // too many parts
        int len = 0;
        while (*p && *p != ':') {
            if (!isxdigit((unsigned char)*p)) return 0;
            ++len;
            if (len > 4) return 0;         // part too long
            ++p;
        }
        if (len == 0) return 0;             // empty part
        ++parts;
        if (*p == ':') {
            ++p;                            // skip colon
            if (!*p) return 0;              // trailing colon
        }
    }
    return parts == 8;
}

char* validIPAddress(char* queryIP) {
    if (!queryIP) return "Neither";
    int hasDot = strchr(queryIP, '.') != NULL;
    int hasColon = strchr(queryIP, ':') != NULL;

    if (hasDot && !hasColon) {
        if (isIPv4(queryIP)) return "IPv4";
    } else if (!hasDot && hasColon) {
        if (isIPv6(queryIP)) return "IPv6";
    }
    return "Neither";
}
```

## Csharp

```csharp
public class Solution
{
    public string ValidIPAddress(string queryIP)
    {
        if (queryIP.Contains('.'))
        {
            if (queryIP.Contains(':')) return "Neither";
            var parts = queryIP.Split('.');
            if (parts.Length != 4) return "Neither";

            foreach (var part in parts)
            {
                if (part.Length == 0 || part.Length > 3) return "Neither";
                // no leading zeros unless the part is exactly "0"
                if (part[0] == '0' && part.Length != 1) return "Neither";

                int val = 0;
                foreach (char c in part)
                {
                    if (!char.IsDigit(c)) return "Neither";
                    val = val * 10 + (c - '0');
                }
                if (val > 255) return "Neither";
            }
            return "IPv4";
        }
        else if (queryIP.Contains(':'))
        {
            var parts = queryIP.Split(':');
            if (parts.Length != 8) return "Neither";

            foreach (var part in parts)
            {
                if (part.Length == 0 || part.Length > 4) return "Neither";
                foreach (char c in part)
                {
                    bool isHex = (c >= '0' && c <= '9') ||
                                 (c >= 'a' && c <= 'f') ||
                                 (c >= 'A' && c <= 'F');
                    if (!isHex) return "Neither";
                }
            }
            return "IPv6";
        }
        else
        {
            return "Neither";
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string} queryIP
 * @return {string}
 */
var validIPAddress = function(queryIP) {
    const isIPv4 = (ip) => {
        const parts = ip.split('.');
        if (parts.length !== 4) return false;
        for (const p of parts) {
            if (p.length === 0 || p.length > 3) return false;
            // all digits
            for (let i = 0; i < p.length; ++i) {
                const ch = p.charCodeAt(i);
                if (ch < 48 || ch > 57) return false; // not '0'-'9'
            }
            // no leading zeros unless single zero
            if (p[0] === '0' && p.length > 1) return false;
            const num = Number(p);
            if (num < 0 || num > 255) return false;
        }
        return true;
    };
    
    const isIPv6 = (ip) => {
        const parts = ip.split(':');
        if (parts.length !== 8) return false;
        const hexRegex = /^[0-9a-fA-F]{1,4}$/;
        for (const p of parts) {
            if (!hexRegex.test(p)) return false;
        }
        return true;
    };
    
    if (queryIP.includes('.')) {
        // must not contain ':' to be IPv4
        if (queryIP.includes(':')) return "Neither";
        return isIPv4(queryIP) ? "IPv4" : "Neither";
    } else if (queryIP.includes(':')) {
        return isIPv6(queryIP) ? "IPv6" : "Neither";
    }
    return "Neither";
};
```

## Typescript

```typescript
function validIPAddress(queryIP: string): string {
    const isIPv4 = (ip: string): boolean => {
        const parts = ip.split('.');
        if (parts.length !== 4) return false;
        for (const p of parts) {
            if (p.length === 0 || p.length > 3) return false;
            // no leading zeros unless the part is exactly "0"
            if (p[0] === '0' && p.length > 1) return false;
            for (let i = 0; i < p.length; ++i) {
                const c = p.charCodeAt(i);
                if (c < 48 || c > 57) return false; // not a digit
            }
            const num = Number(p);
            if (num < 0 || num > 255) return false;
        }
        return true;
    };

    const isIPv6 = (ip: string): boolean => {
        const parts = ip.split(':');
        if (parts.length !== 8) return false;
        const hexDigits = /^[0-9a-fA-F]{1,4}$/;
        for (const p of parts) {
            if (!hexDigits.test(p)) return false;
        }
        return true;
    };

    if (queryIP.includes('.') && !queryIP.includes(':')) {
        return isIPv4(queryIP) ? "IPv4" : "Neither";
    } else if (queryIP.includes(':') && !queryIP.includes('.')) {
        return isIPv6(queryIP) ? "IPv6" : "Neither";
    }
    return "Neither";
}
```

## Php

```php
class Solution {
    /**
     * @param String $queryIP
     * @return String
     */
    function validIPAddress($queryIP) {
        if (strpos($queryIP, '.') !== false && strpos($queryIP, ':') === false) {
            $parts = explode('.', $queryIP);
            if (count($parts) != 4) return "Neither";
            foreach ($parts as $p) {
                if ($p === '' || (strlen($p) > 1 && $p[0] === '0')) return "Neither";
                if (!ctype_digit($p)) return "Neither";
                $num = intval($p);
                if ($num < 0 || $num > 255) return "Neither";
            }
            return "IPv4";
        } elseif (strpos($queryIP, ':') !== false && strpos($queryIP, '.') === false) {
            $parts = explode(':', $queryIP);
            if (count($parts) != 8) return "Neither";
            foreach ($parts as $p) {
                $len = strlen($p);
                if ($len == 0 || $len > 4) return "Neither";
                for ($i = 0; $i < $len; $i++) {
                    $c = $p[$i];
                    $isDigit = $c >= '0' && $c <= '9';
                    $isLower = $c >= 'a' && $c <= 'f';
                    $isUpper = $c >= 'A' && $c <= 'F';
                    if (!($isDigit || $isLower || $isUpper)) return "Neither";
                }
            }
            return "IPv6";
        } else {
            return "Neither";
        }
    }
}
```

## Swift

```swift
class Solution {
    func validIPAddress(_ queryIP: String) -> String {
        if queryIP.contains(".") && !queryIP.contains(":") {
            return isIPv4(queryIP) ? "IPv4" : "Neither"
        } else if queryIP.contains(":") && !queryIP.contains(".") {
            return isIPv6(queryIP) ? "IPv6" : "Neither"
        } else {
            return "Neither"
        }
    }
    
    private func isIPv4(_ ip: String) -> Bool {
        let parts = ip.split(separator: ".", omittingEmptySubsequences: false)
        if parts.count != 4 { return false }
        for part in parts {
            if part.isEmpty || part.count > 3 { return false }
            // leading zero check
            if part.count > 1 && part.first == "0" { return false }
            // all digits
            for ch in part {
                if !ch.isNumber { return false }
            }
            // range check
            if let val = Int(part), val >= 0 && val <= 255 {
                continue
            } else {
                return false
            }
        }
        return true
    }
    
    private func isIPv6(_ ip: String) -> Bool {
        let parts = ip.split(separator: ":", omittingEmptySubsequences: false)
        if parts.count != 8 { return false }
        for part in parts {
            if part.isEmpty || part.count > 4 { return false }
            for ch in part {
                guard let scalar = ch.unicodeScalars.first?.value else { return false }
                let isDigit = (scalar >= 48 && scalar <= 57)      // '0' - '9'
                let isUpperAtoF = (scalar >= 65 && scalar <= 70) // 'A' - 'F'
                let isLoweraTof = (scalar >= 97 && scalar <= 102)// 'a' - 'f'
                if !(isDigit || isUpperAtoF || isLoweraTof) {
                    return false
                }
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun validIPAddress(queryIP: String): String {
        if (queryIP.contains('.')) {
            if (queryIP.contains(':')) return "Neither"
            val parts = queryIP.split('.')
            if (parts.size != 4) return "Neither"
            for (p in parts) {
                if (p.isEmpty() || p.length > 3) return "Neither"
                if (p.length > 1 && p[0] == '0') return "Neither"
                var num = 0
                for (ch in p) {
                    if (!ch.isDigit()) return "Neither"
                    num = num * 10 + (ch - '0')
                }
                if (num !in 0..255) return "Neither"
            }
            return "IPv4"
        } else if (queryIP.contains(':')) {
            val parts = queryIP.split(':')
            if (parts.size != 8) return "Neither"
            for (p in parts) {
                if (p.isEmpty() || p.length > 4) return "Neither"
                for (ch in p) {
                    if (!isHexChar(ch)) return "Neither"
                }
            }
            return "IPv6"
        }
        return "Neither"
    }

    private fun isHexChar(c: Char): Boolean {
        return c.isDigit() ||
               (c >= 'a' && c <= 'f') ||
               (c >= 'A' && c <= 'F')
    }
}
```

## Dart

```dart
class Solution {
  String validIPAddress(String queryIP) {
    if (queryIP.contains('.')) {
      if (queryIP.contains(':')) return "Neither";
      List<String> parts = queryIP.split('.');
      if (parts.length != 4) return "Neither";
      final RegExp digitReg = RegExp(r'^\d+$');
      for (String part in parts) {
        if (part.isEmpty) return "Neither";
        if (!digitReg.hasMatch(part)) return "Neither";
        if (part.length > 1 && part[0] == '0') return "Neither";
        int? val = int.tryParse(part);
        if (val == null || val < 0 || val > 255) return "Neither";
      }
      return "IPv4";
    } else if (queryIP.contains(':')) {
      List<String> parts = queryIP.split(':');
      if (parts.length != 8) return "Neither";
      final RegExp hexReg = RegExp(r'^[0-9a-fA-F]{1,4}$');
      for (String part in parts) {
        if (part.isEmpty) return "Neither";
        if (!hexReg.hasMatch(part)) return "Neither";
      }
      return "IPv6";
    } else {
      return "Neither";
    }
  }
}
```

## Golang

```go
package main

import (
	"strings"
)

func validIPAddress(queryIP string) string {
	if strings.Count(queryIP, ".") == 3 && strings.Count(queryIP, ":") == 0 {
		if isIPv4(queryIP) {
			return "IPv4"
		}
	} else if strings.Count(queryIP, ":") == 7 && strings.Count(queryIP, ".") == 0 {
		if isIPv6(queryIP) {
			return "IPv6"
		}
	}
	return "Neither"
}

func isIPv4(s string) bool {
	parts := strings.Split(s, ".")
	if len(parts) != 4 {
		return false
	}
	for _, p := range parts {
		if len(p) == 0 || len(p) > 3 {
			return false
		}
		// leading zero check
		if p[0] == '0' && len(p) > 1 {
			return false
		}
		val := 0
		for i := 0; i < len(p); i++ {
			c := p[i]
			if c < '0' || c > '9' {
				return false
			}
			val = val*10 + int(c-'0')
		}
		if val > 255 {
			return false
		}
	}
	return true
}

func isIPv6(s string) bool {
	parts := strings.Split(s, ":")
	if len(parts) != 8 {
		return false
	}
	for _, p := range parts {
		if len(p) == 0 || len(p) > 4 {
			return false
		}
		for i := 0; i < len(p); i++ {
			c := p[i]
			if (c >= '0' && c <= '9') ||
				(c >= 'a' && c <= 'f') ||
				(c >= 'A' && c <= 'F') {
				continue
			}
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def valid_ip_address(query_ip)
  if query_ip.count('.') == 3 && query_ip.count(':') == 0
    parts = query_ip.split('.')
    return "Neither" unless parts.size == 4
    parts.each do |p|
      return "Neither" if p.empty? || p.length > 3
      return "Neither" if p[0] == '0' && p.length > 1
      return "Neither" unless p =~ /\A\d+\z/
      num = p.to_i
      return "Neither" if num < 0 || num > 255
    end
    return "IPv4"
  elsif query_ip.count(':') == 7 && query_ip.count('.') == 0
    parts = query_ip.split(':')
    return "Neither" unless parts.size == 8
    hex_regex = /\A[0-9a-fA-F]{1,4}\z/
    parts.each do |p|
      return "Neither" if p.empty? || !(p =~ hex_regex)
    end
    return "IPv6"
  else
    "Neither"
  end
end
```

## Scala

```scala
object Solution {
  def validIPAddress(queryIP: String): String = {
    if (queryIP.contains('.') && !queryIP.contains(':')) {
      if (isIPv4(queryIP)) "IPv4" else "Neither"
    } else if (queryIP.contains(':') && !queryIP.contains('.')) {
      if (isIPv6(queryIP)) "IPv6" else "Neither"
    } else {
      "Neither"
    }
  }

  private def isIPv4(s: String): Boolean = {
    val parts = s.split("\\.", -1)
    if (parts.length != 4) return false
    for (p <- parts) {
      if (p.isEmpty || p.length > 3) return false
      if (p.length > 1 && p.charAt(0) == '0') return false
      var num = 0
      for (c <- p) {
        if (!c.isDigit) return false
        num = num * 10 + (c - '0')
      }
      if (num < 0 || num > 255) return false
    }
    true
  }

  private def isIPv6(s: String): Boolean = {
    val parts = s.split(":", -1)
    if (parts.length != 8) return false
    for (p <- parts) {
      if (p.isEmpty || p.length > 4) return false
      for (c <- p) {
        val lc = c.toLower
        if (!((lc >= '0' && lc <= '9') || (lc >= 'a' && lc <= 'f'))) return false
      }
    }
    true
  }
}
```

## Rust

```rust
impl Solution {
    pub fn valid_ip_address(query_ip: String) -> String {
        if query_ip.contains('.') && !query_ip.contains(':') {
            if Self::is_ipv4(&query_ip) {
                "IPv4".to_string()
            } else {
                "Neither".to_string()
            }
        } else if query_ip.contains(':') && !query_ip.contains('.') {
            if Self::is_ipv6(&query_ip) {
                "IPv6".to_string()
            } else {
                "Neither".to_string()
            }
        } else {
            "Neither".to_string()
        }
    }

    fn is_ipv4(s: &str) -> bool {
        let parts: Vec<&str> = s.split('.').collect();
        if parts.len() != 4 {
            return false;
        }
        for p in parts {
            if p.is_empty() || p.len() > 3 {
                return false;
            }
            // no leading zeros unless the part is exactly "0"
            if p.len() > 1 && p.as_bytes()[0] == b'0' {
                return false;
            }
            let mut val: u32 = 0;
            for &b in p.as_bytes() {
                if !b.is_ascii_digit() {
                    return false;
                }
                val = val * 10 + (b - b'0') as u32;
                if val > 255 {
                    return false;
                }
            }
        }
        true
    }

    fn is_ipv6(s: &str) -> bool {
        let parts: Vec<&str> = s.split(':').collect();
        if parts.len() != 8 {
            return false;
        }
        for p in parts {
            if p.is_empty() || p.len() > 4 {
                return false;
            }
            for &b in p.as_bytes() {
                if !b.is_ascii_hexdigit() {
                    return false;
                }
            }
        }
        true
    }
}
```

## Racket

```racket
(require racket/string)

(define (hex-char? c)
  (or (char-numeric? c)
      (let ([lc (char-downcase c)])
        (and (>= lc #\a) (<= lc #\f)))))

(define (ipv4-part? part)
  (and (> (string-length part) 0)
       (<= (string-length part) 3)
       (let loop ((i 0))
         (or (= i (string-length part))
             (and (char-numeric? (string-ref part i))
                  (loop (+ i 1)))))
       (not (and (> (string-length part) 1)
                 (eq? (string-ref part 0) #\0)))
       (let ([num (string->number part)])
         (and num (<= num 255)))))

(define (ipv4? s)
  (let ([parts (string-split s ".")])
    (and (= (length parts) 4)
         (for/all ([p parts]) (ipv4-part? p)))))

(define (ipv6-part? part)
  (and (> (string-length part) 0)
       (<= (string-length part) 4)
       (let loop ((i 0))
         (or (= i (string-length part))
             (and (hex-char? (string-ref part i))
                  (loop (+ i 1)))))))

(define (ipv6? s)
  (let ([parts (string-split s ":")])
    (and (= (length parts) 8)
         (for/all ([p parts]) (ipv6-part? p)))))

(define/contract (valid-ip-address queryIP)
  (-> string? string?)
  (cond
    [(and (string-contains? queryIP ".")
          (not (string-contains? queryIP ":")))
     (if (ipv4? queryIP) "IPv4" "Neither")]
    [(and (string-contains? queryIP ":")
          (not (string-contains? queryIP ".")))
     (if (ipv6? queryIP) "IPv6" "Neither")]
    [else "Neither"]))
```

## Erlang

```erlang
-module(solution).
-export([valid_ip_address/1]).

-spec valid_ip_address(QueryIP :: unicode:unicode_binary()) -> unicode:unicode_binary().
valid_ip_address(QueryIP) ->
    case {binary:match(QueryIP, <<".">>), binary:match(QueryIP, <<":">>)} of
        {nomatch, nomatch} ->
            <<"Neither">>;
        {{_,_}, {_,_}} ->
            <<"Neither">>;
        {{_,_}, nomatch} ->
            case validate_ipv4(binary_to_list(QueryIP)) of
                true -> <<"IPv4">>;
                false -> <<"Neither">>
            end;
        {nomatch, {_,_}} ->
            case validate_ipv6(binary_to_list(QueryIP)) of
                true -> <<"IPv6">>;
                false -> <<"Neither">>
            end
    end.

validate_ipv4(Str) ->
    Parts = string:tokens(Str, "."),
    length(Parts) == 4 andalso lists:all(fun is_valid_ipv4_part/1, Parts).

is_valid_ipv4_part(Part) ->
    Len = length(Part),
    Len > 0 andalso
    lists:all(fun(C) -> C >= $0 andalso C =< $9 end, Part) andalso
    (Len == 1 orelse hd(Part) =/= $0) andalso
    begin
        N = list_to_integer(Part),
        N >= 0 andalso N =< 255
    end.

validate_ipv6(Str) ->
    Parts = string:tokens(Str, ":"),
    length(Parts) == 8 andalso lists:all(fun is_valid_ipv6_part/1, Parts).

is_valid_ipv6_part(Part) ->
    Len = length(Part),
    Len >= 1 andalso Len =< 4 andalso
    lists:all(
        fun(C) ->
            (C >= $0 andalso C =< $9) orelse
            (C >= $a andalso C =< $f) orelse
            (C >= $A andalso C =< $F)
        end,
        Part).
```

## Elixir

```elixir
defmodule Solution do
  @spec valid_ip_address(query_ip :: String.t()) :: String.t()
  def valid_ip_address(query_ip) do
    cond do
      String.contains?(query_ip, ".") && !String.contains?(query_ip, ":") ->
        if ipv4?(query_ip), do: "IPv4", else: "Neither"

      String.contains?(query_ip, ":") && !String.contains?(query_ip, ".") ->
        if ipv6?(query_ip), do: "IPv6", else: "Neither"

      true ->
        "Neither"
    end
  end

  defp ipv4?(ip) do
    parts = String.split(ip, ".", trim: false)
    length(parts) == 4 and Enum.all?(parts, &valid_ipv4_part?/1)
  end

  defp valid_ipv4_part?(part) do
    len = byte_size(part)

    cond do
      len == 0 or len > 3 ->
        false

      len > 1 and String.at(part, 0) == "0" ->
        false

      true ->
        case Integer.parse(part) do
          {num, ""} when num >= 0 and num <= 255 -> true
          _ -> false
        end
    end
  end

  defp ipv6?(ip) do
    parts = String.split(ip, ":", trim: false)
    length(parts) == 8 and Enum.all?(parts, &valid_ipv6_part?/1)
  end

  defp valid_ipv6_part?(part) do
    len = byte_size(part)

    if len == 0 or len > 4 do
      false
    else
      String.match?(part, ~r/^[0-9a-fA-F]{1,4}$/)
    end
  end
end
```
