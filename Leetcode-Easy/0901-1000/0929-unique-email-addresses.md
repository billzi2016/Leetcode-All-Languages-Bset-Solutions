# 0929. Unique Email Addresses

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        unordered_set<string> uniq;
        for (const string& email : emails) {
            size_t atPos = email.find('@');
            string local = email.substr(0, atPos);
            string domain = email.substr(atPos); // includes '@'
            
            string processed;
            processed.reserve(local.size());
            for (char c : local) {
                if (c == '+') break;
                if (c != '.') processed.push_back(c);
            }
            uniq.insert(processed + domain);
        }
        return static_cast<int>(uniq.size());
    }
};
```

## Java

```java
class Solution {
    public int numUniqueEmails(String[] emails) {
        java.util.Set<String> unique = new java.util.HashSet<>();
        for (String email : emails) {
            int atPos = email.indexOf('@');
            String local = email.substring(0, atPos);
            String domain = email.substring(atPos); // includes '@'
            int plusPos = local.indexOf('+');
            if (plusPos != -1) {
                local = local.substring(0, plusPos);
            }
            local = local.replace(".", "");
            unique.add(local + domain);
        }
        return unique.size();
    }
}
```

## Python

```python
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            local = local.replace('.', '')
            unique.add(local + '@' + domain)
        return len(unique)
```

## Python3

```python
from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            local = local.replace('.', '')
            unique.add(f"{local}@{domain}")
        return len(unique)
```

## C

```c
#include <string.h>
#include <stdlib.h>

static char *my_strdup(const char *s) {
    size_t len = strlen(s);
    char *p = (char *)malloc(len + 1);
    if (p) memcpy(p, s, len + 1);
    return p;
}

int numUniqueEmails(char **emails, int emailsSize) {
    char *unique[100]; // maximum possible unique emails is emailsSize <= 100
    int uniqCount = 0;

    for (int i = 0; i < emailsSize; ++i) {
        const char *e = emails[i];
        const char *at = strchr(e, '@');
        if (!at) continue; // safety, though problem guarantees '@'

        char buf[210]; // enough for processed email
        int idx = 0;

        /* process local part */
        for (const char *p = e; p < at; ++p) {
            if (*p == '+') break;
            if (*p == '.') continue;
            buf[idx++] = *p;
        }

        /* add '@' and domain part unchanged */
        buf[idx++] = '@';
        const char *domain = at + 1;
        while (*domain) {
            buf[idx++] = *domain++;
        }
        buf[idx] = '\0';

        /* check if already seen */
        int found = 0;
        for (int j = 0; j < uniqCount; ++j) {
            if (strcmp(buf, unique[j]) == 0) {
                found = 1;
                break;
            }
        }

        if (!found) {
            unique[uniqCount++] = my_strdup(buf);
        }
    }

    /* free allocated memory */
    for (int i = 0; i < uniqCount; ++i) {
        free(unique[i]);
    }

    return uniqCount;
}
```

## Csharp

```csharp
public class Solution
{
    public int NumUniqueEmails(string[] emails)
    {
        var unique = new HashSet<string>();
        foreach (var email in emails)
        {
            int atPos = email.IndexOf('@');
            string local = email.Substring(0, atPos);
            string domain = email.Substring(atPos); // includes '@'

            var sb = new System.Text.StringBuilder();
            for (int i = 0; i < local.Length; i++)
            {
                char c = local[i];
                if (c == '+')
                    break;
                if (c != '.')
                    sb.Append(c);
            }

            unique.Add(sb.ToString() + domain);
        }
        return unique.Count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    const seen = new Set();
    for (const email of emails) {
        const [localPart, domain] = email.split('@');
        let processedLocal = localPart;
        const plusIdx = processedLocal.indexOf('+');
        if (plusIdx !== -1) {
            processedLocal = processedLocal.substring(0, plusIdx);
        }
        processedLocal = processedLocal.replace(/\./g, '');
        seen.add(`${processedLocal}@${domain}`);
    }
    return seen.size;
};
```

## Typescript

```typescript
function numUniqueEmails(emails: string[]): number {
    const unique = new Set<string>();
    for (const email of emails) {
        const [localPart, domain] = email.split('@');
        let processedLocal = localPart;
        const plusIdx = processedLocal.indexOf('+');
        if (plusIdx !== -1) {
            processedLocal = processedLocal.substring(0, plusIdx);
        }
        processedLocal = processedLocal.replace(/\./g, '');
        unique.add(`${processedLocal}@${domain}`);
    }
    return unique.size;
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param String[] $emails
     * @return Integer
     */
    function numUniqueEmails($emails) {
        $unique = [];
        foreach ($emails as $email) {
            [$local, $domain] = explode('@', $email, 2);
            $plusPos = strpos($local, '+');
            if ($plusPos !== false) {
                $local = substr($local, 0, $plusPos);
            }
            $local = str_replace('.', '', $local);
            $normalized = $local . '@' . $domain;
            $unique[$normalized] = true;
        }
        return count($unique);
    }
}
?>
```

## Swift

```swift
class Solution {
    func numUniqueEmails(_ emails: [String]) -> Int {
        var unique = Set<String>()
        for email in emails {
            let parts = email.split(separator: "@", maxSplits: 1, omittingEmptySubsequences: false)
            guard parts.count == 2 else { continue }
            var local = String(parts[0])
            let domain = String(parts[1])
            
            if let plusPos = local.firstIndex(of: "+") {
                local = String(local[..<plusPos])
            }
            local = local.replacingOccurrences(of: ".", with: "")
            
            unique.insert("\(local)@\(domain)")
        }
        return unique.count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numUniqueEmails(emails: Array<String>): Int {
        val unique = HashSet<String>()
        for (email in emails) {
            val atIdx = email.indexOf('@')
            var local = email.substring(0, atIdx)
            val domain = email.substring(atIdx + 1)
            val plusIdx = local.indexOf('+')
            if (plusIdx != -1) {
                local = local.substring(0, plusIdx)
            }
            local = local.replace(".", "")
            unique.add("$local@$domain")
        }
        return unique.size
    }
}
```

## Dart

```dart
class Solution {
  int numUniqueEmails(List<String> emails) {
    final Set<String> unique = {};
    for (var email in emails) {
      var parts = email.split('@');
      var local = parts[0];
      var domain = parts[1];

      var plusIndex = local.indexOf('+');
      if (plusIndex != -1) {
        local = local.substring(0, plusIndex);
      }
      local = local.replaceAll('.', '');

      unique.add('$local@$domain');
    }
    return unique.length;
  }
}
```

## Golang

```go
import "strings"

func numUniqueEmails(emails []string) int {
	seen := make(map[string]struct{})
	for _, e := range emails {
		at := strings.IndexByte(e, '@')
		local := e[:at]
		domain := e[at+1:]

		if p := strings.IndexByte(local, '+'); p != -1 {
			local = local[:p]
		}

		var sb strings.Builder
		for i := 0; i < len(local); i++ {
			if local[i] != '.' {
				sb.WriteByte(local[i])
			}
		}

		normalized := sb.String() + "@" + domain
		seen[normalized] = struct{}{}
	}
	return len(seen)
}
```

## Ruby

```ruby
require 'set'

def num_unique_emails(emails)
  unique = Set.new
  emails.each do |email|
    local, domain = email.split('@', 2)
    plus_index = local.index('+')
    local = plus_index ? local[0...plus_index] : local
    local.delete!('.')
    unique.add("#{local}@#{domain}")
  end
  unique.size
end
```

## Scala

```scala
object Solution {
    def numUniqueEmails(emails: Array[String]): Int = {
        val unique = scala.collection.mutable.HashSet[String]()
        for (email <- emails) {
            val parts = email.split("@", 2)
            var local = parts(0)
            val domain = parts(1)
            val plusIdx = local.indexOf('+')
            if (plusIdx != -1) local = local.substring(0, plusIdx)
            local = local.filter(_ != '.')
            unique += s"$local@$domain"
        }
        unique.size
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn num_unique_emails(emails: Vec<String>) -> i32 {
        let mut unique = HashSet::new();
        for email in emails.iter() {
            if let Some((local, domain)) = email.split_once('@') {
                let trimmed_local = match local.find('+') {
                    Some(idx) => &local[..idx],
                    None => local,
                };
                let cleaned: String = trimmed_local.chars().filter(|&c| c != '.').collect();
                unique.insert(format!("{}@{}", cleaned, domain));
            }
        }
        unique.len() as i32
    }
}
```

## Racket

```racket
#lang racket

(require racket/set
         racket/string)

(define/contract (num-unique-emails emails)
  (-> (listof string?) exact-integer?)
  (let ([unique
         (foldl
          (lambda (email acc)
            (let* ([at-pos (string-index-of email "@")]
                   [local (substring email 0 at-pos)]
                   [domain (substring email (+ at-pos 1))]
                   [plus-pos (string-index-of local "+")]
                   [local-trunc (if plus-pos
                                   (substring local 0 plus-pos)
                                   local)]
                   [clean-local
                    (list->string
                     (filter (lambda (c) (not (char=? c #\.)))
                             (string->list local-trunc)))])
              (set-add acc (string-append clean-local "@" domain))))
          (set)
          emails)])
    (set-count unique)))
```

## Erlang

```erlang
-module(solution).
-export([num_unique_emails/1]).

-spec num_unique_emails(Emails :: [unicode:unicode_binary()]) -> integer().
num_unique_emails(Emails) ->
    UniqueMap = lists:foldl(fun(Email, Acc) ->
        [LocalBin, DomainBin] = binary:split(Email, <<"@">>),
        ProcessedLocal = process_local(LocalBin),
        Normalized = <<ProcessedLocal/binary, "@", DomainBin/binary>>,
        maps:put(Normalized, true, Acc)
    end, #{}, Emails),
    map_size(UniqueMap).

process_local(Local) ->
    case binary:match(Local, <<"+">>) of
        {Pos,_} -> Local1 = binary:part(Local, 0, Pos);
        nomatch -> Local1 = Local
    end,
    binary:replace(Local1, <<".">>, <<>>, [global]).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_unique_emails(emails :: [String.t]) :: integer
  def num_unique_emails(emails) do
    emails
    |> Enum.reduce(MapSet.new(), fn email, set ->
      [local, domain] = String.split(email, "@", parts: 2)

      processed_local =
        local
        |> String.split("+", parts: 2)
        |> hd()
        |> String.replace(".", "")

      MapSet.put(set, processed_local <> "@" <> domain)
    end)
    |> MapSet.size()
  end
end
```
