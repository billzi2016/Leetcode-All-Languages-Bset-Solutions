# 0831. Masking Personal Information

## Cpp

```cpp
class Solution {
public:
    string maskPII(string s) {
        // Check if it's an email (contains '@')
        auto atPos = s.find('@');
        if (atPos != string::npos) {
            // Email handling
            string name = s.substr(0, atPos);
            string domain = s.substr(atPos + 1);
            // convert to lowercase
            for (char &c : name) c = tolower(c);
            for (char &c : domain) c = tolower(c);
            string masked;
            masked += name.front();
            masked += "*****";
            masked += name.back();
            masked += '@';
            masked += domain;
            return masked;
        } else {
            // Phone number handling
            string digits;
            for (char c : s) {
                if (isdigit(c)) digits.push_back(c);
            }
            int n = digits.size(); // total digits
            string last4 = digits.substr(n - 4);
            string localMask = "***-***-" + last4;
            if (n == 10) return localMask;
            string countryMask = "+" + string(n - 10, '*') + "-" + localMask;
            return countryMask;
        }
    }
};
```

## Java

```java
class Solution {
    public String maskPII(String s) {
        if (s.indexOf('@') != -1) { // email
            String lower = s.toLowerCase();
            int atIdx = lower.indexOf('@');
            String name = lower.substring(0, atIdx);
            String domain = lower.substring(atIdx + 1);
            return "" + name.charAt(0) + "*****" + name.charAt(name.length() - 1) + "@" + domain;
        } else { // phone
            StringBuilder digits = new StringBuilder();
            for (char c : s.toCharArray()) {
                if (Character.isDigit(c)) {
                    digits.append(c);
                }
            }
            int n = digits.length();
            String last4 = digits.substring(n - 4);
            if (n == 10) {
                return "***-***-" + last4;
            } else {
                int ccLen = n - 10;
                StringBuilder sb = new StringBuilder();
                sb.append('+');
                for (int i = 0; i < ccLen; i++) {
                    sb.append('*');
                }
                sb.append("-***-***-");
                sb.append(last4);
                return sb.toString();
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def maskPII(self, s):
        """
        :type s: str
        :rtype: str
        """
        if '@' in s:
            local, domain = s.split('@')
            local = local.lower()
            domain = domain.lower()
            masked_local = local[0] + "*****" + local[-1]
            return masked_local + "@" + domain
        else:
            digits = [c for c in s if c.isdigit()]
            num = ''.join(digits)
            last4 = num[-4:]
            country_len = len(num) - 10
            if country_len > 0:
                return "+" + "*" * country_len + "-***-***-" + last4
            else:
                return "***-***-" + last4
```

## Python3

```python
class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            local, domain = s.split('@')
            local = local.lower()
            domain = domain.lower()
            masked_local = f"{local[0]}*****{local[-1]}"
            return f"{masked_local}@{domain}"
        else:
            digits = [c for c in s if c.isdigit()]
            n = len(digits)
            last4 = ''.join(digits[-4:])
            if n == 10:
                return f"***-***-{last4}"
            else:
                country_len = n - 10
                return f"+{'*'*country_len}-***-***-{last4}")
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char* maskPII(char* s) {
    if (!s) return NULL;
    char *at = strchr(s, '@');
    if (at) { // email
        int domain_len = strlen(at + 1);
        int total_len = 8 + domain_len; // first + ***** + last + @ + domain
        char *res = (char*)malloc(total_len + 1);
        int pos = 0;
        res[pos++] = tolower(s[0]);
        for (int i = 0; i < 5; ++i) res[pos++] = '*';
        res[pos++] = tolower(at[-1]);
        res[pos++] = '@';
        const char *domain = at + 1;
        for (int i = 0; i < domain_len; ++i)
            res[pos++] = tolower(domain[i]);
        res[pos] = '\0';
        return res;
    } else { // phone
        char digits[30];
        int n = 0;
        for (int i = 0; s[i]; ++i) {
            if (isdigit((unsigned char)s[i]))
                digits[n++] = s[i];
        }
        char last4[5] = {0};
        for (int i = 0; i < 4; ++i)
            last4[i] = digits[n - 4 + i];

        if (n == 10) {
            const char *prefix = "***-***-";
            int total_len = strlen(prefix) + 4;
            char *res = (char*)malloc(total_len + 1);
            strcpy(res, prefix);
            strcat(res, last4);
            return res;
        } else {
            int country = n - 10;
            const char *mid = "-***-***-";
            int total_len = 1 + country + strlen(mid) + 4;
            char *res = (char*)malloc(total_len + 1);
            int pos = 0;
            res[pos++] = '+';
            for (int i = 0; i < country; ++i)
                res[pos++] = '*';
            for (int i = 0; mid[i]; ++i)
                res[pos++] = mid[i];
            for (int i = 0; i < 4; ++i)
                res[pos++] = last4[i];
            res[pos] = '\0';
            return res;
        }
    }
}
```

## Csharp

```csharp
public class Solution
{
    public string MaskPII(string s)
    {
        if (s.Contains("@"))
        {
            var parts = s.Split('@');
            string name = parts[0].ToLower();
            string domain = parts[1].ToLower();
            char first = name[0];
            char last = name[name.Length - 1];
            return $"{first}*****{last}@{domain}";
        }
        else
        {
            var digitsBuilder = new System.Text.StringBuilder();
            foreach (char c in s)
            {
                if (char.IsDigit(c))
                    digitsBuilder.Append(c);
            }

            string digits = digitsBuilder.ToString();
            string last4 = digits.Substring(digits.Length - 4);
            int countryLen = digits.Length - 10;

            string prefix = "";
            if (countryLen > 0)
                prefix = "+" + new string('*', countryLen) + "-";

            return $"{prefix}***-***-{last4}";
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var maskPII = function(s) {
    if (s.includes('@')) {
        const [name, domain] = s.split('@');
        const lowerName = name.toLowerCase();
        const lowerDomain = domain.toLowerCase();
        return lowerName[0] + '*****' + lowerName[lowerName.length - 1] + '@' + lowerDomain;
    } else {
        const digits = s.replace(/\D/g, '');
        const n = digits.length;
        const last4 = digits.slice(-4);
        if (n === 10) {
            return `***-***-${last4}`;
        } else {
            const countryStars = '*'.repeat(n - 10);
            return `+${countryStars}-***-***-${last4}`;
        }
    }
};
```

## Typescript

```typescript
function maskPII(s: string): string {
    if (s.indexOf('@') !== -1) {
        const [local, domain] = s.split('@');
        const lowerLocal = local.toLowerCase();
        const lowerDomain = domain.toLowerCase();
        return (
            lowerLocal[0] +
            '*****' +
            lowerLocal[lowerLocal.length - 1] +
            '@' +
            lowerDomain
        );
    } else {
        // phone number
        const digits = s.replace(/\D/g, '');
        const n = digits.length;
        const last4 = digits.slice(-4);
        if (n === 10) {
            return `***-***-${last4}`;
        } else {
            const countryMask = '*'.repeat(n - 10);
            return `+${countryMask}-***-***-${last4}`;
        }
    }
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function maskPII($s) {
        if (strpos($s, '@') !== false) {
            // Email case
            $parts = explode('@', $s);
            $name = strtolower($parts[0]);
            $domain = strtolower($parts[1]);
            $maskedName = $name[0] . '*****' . $name[strlen($name) - 1];
            return $maskedName . '@' . $domain;
        } else {
            // Phone number case
            $digits = preg_replace('/\D/', '', $s);
            $len = strlen($digits);
            $last4 = substr($digits, -4);
            if ($len == 10) {
                return "***-***-" . $last4;
            } else {
                $countryLen = $len - 10;
                $prefix = '+' . str_repeat('*', $countryLen) . '-';
                return $prefix . '***-***-' . $last4;
            }
        }
    }
}
```

## Swift

```swift
class Solution {
    func maskPII(_ s: String) -> String {
        if s.contains("@") {
            let lower = s.lowercased()
            let parts = lower.split(separator: "@", maxSplits: 1, omittingEmptySubsequences: false)
            let name = String(parts[0])
            let domain = String(parts[1])
            let first = name.first!
            let last = name.last!
            return "\(first)*****\(last)@\(domain)"
        } else {
            var digits = ""
            for ch in s {
                if ch.isNumber {
                    digits.append(ch)
                }
            }
            let n = digits.count
            let last4 = String(digits.suffix(4))
            if n == 10 {
                return "***-***-\(last4)"
            } else {
                let country = n - 10
                let prefix = "+" + String(repeating: "*", count: country)
                return "\(prefix)-***-***-\(last4)"
            }
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maskPII(s: String): String {
        return if (s.contains('@')) {
            val parts = s.split("@")
            val name = parts[0].lowercase()
            val domain = parts[1].lowercase()
            "${name.first()}*****${name.last()}@$domain"
        } else {
            val digits = s.filter { it.isDigit() }
            val n = digits.length
            val last4 = digits.substring(n - 4)
            if (n == 10) {
                "***-***-$last4"
            } else {
                "+" + "*".repeat(n - 10) + "-***-***-$last4"
            }
        }
    }
}
```

## Dart

```dart
class Solution {
  String maskPII(String s) {
    if (s.contains('@')) {
      var parts = s.split('@');
      var name = parts[0];
      var domain = parts[1].toLowerCase();
      var first = name[0].toLowerCase();
      var last = name[name.length - 1].toLowerCase();
      return '$first*****$last@$domain';
    } else {
      var digits = s.replaceAll(RegExp(r'\D'), '');
      int n = digits.length;
      String lastFour = digits.substring(n - 4);
      String maskedLocal = '***-***-$lastFour';
      if (n == 10) {
        return maskedLocal;
      }
      int countryLen = n - 10;
      String countryMask = '+' + List.filled(countryLen, '*').join() + '-';
      return countryMask + maskedLocal;
    }
  }
}
```

## Golang

```go
import "strings"

func maskPII(s string) string {
	if strings.Contains(s, "@") {
		lower := strings.ToLower(s)
		parts := strings.SplitN(lower, "@", 2)
		name := parts[0]
		domain := parts[1]
		maskedName := string(name[0]) + "*****" + string(name[len(name)-1])
		return maskedName + "@" + domain
	}
	digits := make([]rune, 0, len(s))
	for _, ch := range s {
		if ch >= '0' && ch <= '9' {
			digits = append(digits, ch)
		}
	}
	n := len(digits)
	last4 := string(digits[n-4:])
	var sb strings.Builder
	if n == 10 {
		sb.WriteString("***-***-")
		sb.WriteString(last4)
	} else {
		sb.WriteByte('+')
		sb.WriteString(strings.Repeat("*", n-10))
		sb.WriteString("-***-***-")
		sb.WriteString(last4)
	}
	return sb.String()
}
```

## Ruby

```ruby
def mask_pii(s)
  if s.include?('@')
    local, domain = s.split('@')
    masked_local = "#{local[0].downcase}*****#{local[-1].downcase}"
    "#{masked_local}@#{domain.downcase}"
  else
    digits = s.scan(/\d/).join
    n = digits.length
    last4 = digits[-4, 4]
    if n == 10
      "***-***-#{last4}"
    else
      country_len = n - 10
      "+" + "*" * country_len + "-***-***-#{last4}"
    end
  end
end
```

## Scala

```scala
object Solution {
    def maskPII(s: String): String = {
        if (s.contains("@")) {
            val parts = s.split("@")
            val name = parts(0).toLowerCase
            val domain = parts(1).toLowerCase
            val first = name.head
            val last = name.last
            s"${first}*****${last}@${domain}"
        } else {
            val digits = s.filter(_.isDigit)
            val n = digits.length
            val maskedLocal = "***-***-" + digits.substring(n - 4)
            if (n == 10) maskedLocal
            else {
                val countryStars = "*" * (n - 10)
                "+" + countryStars + "-" + maskedLocal
            }
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn mask_pii(s: String) -> String {
        if s.contains('@') {
            let lower = s.to_ascii_lowercase();
            let mut parts = lower.splitn(2, '@');
            let name = parts.next().unwrap();
            let domain = parts.next().unwrap();
            let first = name.chars().next().unwrap();
            let last = name.chars().last().unwrap();
            format!("{}*****{}@{}", first, last, domain)
        } else {
            let digits: String = s.chars().filter(|c| c.is_ascii_digit()).collect();
            let n = digits.len();
            let last4 = &digits[n - 4..];
            if n == 10 {
                format!("***-***-{}", last4)
            } else {
                let country_len = n - 10;
                let mut prefix = String::from("+");
                for _ in 0..country_len {
                    prefix.push('*');
                }
                prefix.push('-');
                format!("{}***-***-{}", prefix, last4)
            }
        }
    }
}
```

## Racket

```racket
#lang racket

(require racket/string)

(define/contract (mask-pii s)
  (-> string? string?)
  (if (string-contains? s "@")
      (let* ((lower (string-downcase s))
             (at (string-index-of lower "@"))
             (name (substring lower 0 at))
             (domain (substring lower (+ at 1)))
             (first (substring name 0 1))
             (last (substring name (- (string-length name) 1))))
        (string-append first "*****" last "@" domain))
      (let* ((digits (list->string (filter char-numeric? (string->list s))))
             (n (string-length digits))
             (last4 (substring digits (- n 4)))
             (masked
               (if (= n 10)
                   (string-append "***-***-" last4)
                   (let ((prefix (make-string (- n 10) #\*)))
                     (string-append "+" prefix "-***-***-" last4)))))
        masked)))
```

## Erlang

```erlang
-module(solution).
-export([mask_pii/1]).

-spec mask_pii(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
mask_pii(S) ->
    Str = unicode:characters_to_list(S),
    case lists:any(fun(C) -> C =:= $@ end, Str) of
        true  -> mask_email(Str);
        false -> mask_phone(Str)
    end.

mask_email(Str) ->
    Lower = string:to_lower(Str),
    [Name, Domain] = string:split(Lower, "@", all),
    First = hd(Name),
    Last = lists:last(Name),
    Masked = [First] ++ "*****" ++ [Last] ++ "@" ++ Domain,
    unicode:characters_to_binary(Masked).

mask_phone(Str) ->
    Digits = [C || C <- Str, $0 =< C, C =< $9],
    Len = length(Digits),
    CountryLen = Len - 10,
    Last4Start = Len - 3,
    Last4 = lists:sublist(Digits, Last4Start, 4),
    CCPart = case CountryLen of
        0 -> "";
        N -> "+" ++ lists:duplicate(N, $*) ++ "-"
    end,
    Result = CCPart ++ "***-***-" ++ Last4,
    unicode:characters_to_binary(Result).
```

## Elixir

```elixir
defmodule Solution do
  @spec mask_pii(s :: String.t) :: String.t
  def mask_pii(s) do
    if String.contains?(s, "@") do
      [local, domain] = String.split(s, "@", parts: 2)
      local_down = String.downcase(local)
      domain_down = String.downcase(domain)

      first = String.at(local_down, 0)
      last = String.at(local_down, -1)

      "#{first}*****#{last}@#{domain_down}"
    else
      digits =
        s
        |> String.graphemes()
        |> Enum.filter(&(&1 =~ ~r/^\d$/))
        |> Enum.join()

      total = String.length(digits)
      last4 = String.slice(digits, -4, 4)

      if total == 10 do
        "***-***-" <> last4
      else
        country_len = total - 10
        "+" <> String.duplicate("*", country_len) <> "-***-***-" <> last4
      end
    end
  end
end
```
