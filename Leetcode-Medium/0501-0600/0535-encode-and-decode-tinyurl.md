# 0535. Encode and Decode TinyURL

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
    unordered_map<string, string> short2long;
    unordered_map<string, string> long2short;
    const string prefix = "http://tinyurl.com/";
    const string charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    mt19937 rng{random_device{}()};
    
    string generateKey() {
        string key;
        key.reserve(6);
        uniform_int_distribution<int> dist(0, (int)charset.size() - 1);
        for (int i = 0; i < 6; ++i)
            key.push_back(charset[dist(rng)]);
        return key;
    }
public:
    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        auto it = long2short.find(longUrl);
        if (it != long2short.end()) return prefix + it->second;
        string key;
        do {
            key = generateKey();
        } while (short2long.count(key));
        short2long[key] = longUrl;
        long2short[longUrl] = key;
        return prefix + key;
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        string key = shortUrl.substr(prefix.size());
        auto it = short2long.find(key);
        if (it != short2long.end()) return it->second;
        return "";
    }
};
```

## Java

```java
import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class Codec {
    private static final String PREFIX = "http://tinyurl.com/";
    private static final String CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    private static final int CODE_LEN = 6;
    private final Map<String, String> shortToLong = new HashMap<>();
    private final Map<String, String> longToShort = new HashMap<>();
    private final Random rand = new Random();

    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        if (longToShort.containsKey(longUrl)) {
            return PREFIX + longToShort.get(longUrl);
        }
        String code;
        do {
            code = generateCode();
        } while (shortToLong.containsKey(code));
        shortToLong.put(code, longUrl);
        longToShort.put(longUrl, code);
        return PREFIX + code;
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        if (!shortUrl.startsWith(PREFIX)) {
            return "";
        }
        String code = shortUrl.substring(PREFIX.length());
        return shortToLong.getOrDefault(code, "");
    }

    private String generateCode() {
        StringBuilder sb = new StringBuilder(CODE_LEN);
        for (int i = 0; i < CODE_LEN; i++) {
            sb.append(CHARSET.charAt(rand.nextInt(CHARSET.length())));
        }
        return sb.toString();
    }
}
```

## Python

```python
class Codec:
    def __init__(self):
        self.prefix = "http://tinyurl.com/"
        self.id_counter = 1
        self.long2short = {}
        self.short2long = {}
        self.chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def _encode_id(self, n: int) -> str:
        if n == 0:
            return self.chars[0]
        base = len(self.chars)
        s = []
        while n > 0:
            n, rem = divmod(n, base)
            s.append(self.chars[rem])
        return ''.join(reversed(s))

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.long2short:
            return self.long2short[longUrl]
        # generate new short key
        key = self._encode_id(self.id_counter)
        self.id_counter += 1
        shortUrl = self.prefix + key
        self.long2short[longUrl] = shortUrl
        self.short2long[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.short2long.get(shortUrl, "")
```

## Python3

```python
import random
import string

class Codec:
    def __init__(self):
        self.prefix = "http://tinyurl.com/"
        self.long2short = {}
        self.short2long = {}

    def _generate_key(self, length=6):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl in self.long2short:
            return self.prefix + self.long2short[longUrl]
        while True:
            key = self._generate_key()
            if key not in self.short2long:
                break
        self.long2short[longUrl] = key
        self.short2long[key] = longUrl
        return self.prefix + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        key = shortUrl.replace(self.prefix, "", 1)
        return self.short2long.get(key, "")
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

static const char *PREFIX = "http://tinyurl.com/";
static char **id_to_url = NULL;
static size_t capacity = 0;
static size_t next_id = 1;

static void ensure_capacity(size_t id) {
    if (id >= capacity) {
        size_t new_cap = capacity ? capacity * 2 : 1024;
        while (new_cap <= id) new_cap <<= 1;
        char **tmp = realloc(id_to_url, new_cap * sizeof(char*));
        if (!tmp) exit(1);
        for (size_t i = capacity; i < new_cap; ++i) tmp[i] = NULL;
        id_to_url = tmp;
        capacity = new_cap;
    }
}

/** Encodes a URL to a shortened URL. */
char* encode(char* longUrl) {
    size_t id = next_id++;
    ensure_capacity(id);
    id_to_url[id] = strdup(longUrl);
    if (!id_to_url[id]) exit(1);

    // compute length of short url
    char numbuf[32];
    int numlen = snprintf(numbuf, sizeof(numbuf), "%zu", id);
    size_t total_len = strlen(PREFIX) + (size_t)numlen;
    char *shortUrl = (char*)malloc(total_len + 1);
    if (!shortUrl) exit(1);
    strcpy(shortUrl, PREFIX);
    strcat(shortUrl, numbuf);
    return shortUrl;
}

/** Decodes a shortened URL to its original URL. */
char* decode(char* shortUrl) {
    // find the last '/' character
    char *p = strrchr(shortUrl, '/');
    if (!p) return NULL;
    size_t id = (size_t)strtoul(p + 1, NULL, 10);
    if (id >= capacity || !id_to_url[id]) return NULL;
    // return a copy of the original URL
    char *orig = strdup(id_to_url[id]);
    if (!orig) exit(1);
    return orig;
}

// The functions will be called as:
// char* s = encode(url);
// char* o = decode(s);
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Codec {
    private readonly Dictionary<string, string> _map = new Dictionary<string, string>();
    private readonly Random _rand = new Random();
    private const string Alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    private const string Prefix = "http://tinyurl.com/";

    public string encode(string longUrl) {
        string key;
        do {
            char[] chars = new char[6];
            for (int i = 0; i < 6; i++) {
                chars[i] = Alphabet[_rand.Next(Alphabet.Length)];
            }
            key = new string(chars);
        } while (_map.ContainsKey(key));
        _map[key] = longUrl;
        return Prefix + key;
    }

    public string decode(string shortUrl) {
        if (!shortUrl.StartsWith(Prefix)) return "";
        string key = shortUrl.Substring(Prefix.Length);
        return _map.TryGetValue(key, out var longUrl) ? longUrl : "";
    }
}
```

## Javascript

```javascript
const base = "http://tinyurl.com/";
const longToCode = new Map();
const codeToLong = new Map();

var encode = function(longUrl) {
    if (longToCode.has(longUrl)) {
        return base + longToCode.get(longUrl);
    }
    let code;
    do {
        // generate a 6-character alphanumeric string
        code = Math.random().toString(36).substring(2, 8);
    } while (codeToLong.has(code));
    longToCode.set(longUrl, code);
    codeToLong.set(code, longUrl);
    return base + code;
};

var decode = function(shortUrl) {
    const code = shortUrl.slice(base.length);
    return codeToLong.get(code) || "";
};

/**
 * Your functions will be called as such:
 * decode(encode(url));
 */
```

## Typescript

```typescript
const PREFIX = "http://tinyurl.com/";
let counter = 1;
const shortToLong = new Map<string, string>();
const longToShort = new Map<string, string>();

function encode(longUrl: string): string {
    if (longToShort.has(longUrl)) {
        return PREFIX + longToShort.get(longUrl)!;
    }
    const key = counter.toString(36);
    counter++;
    shortToLong.set(key, longUrl);
    longToShort.set(longUrl, key);
    return PREFIX + key;
}

function decode(shortUrl: string): string {
    const key = shortUrl.slice(PREFIX.length);
    return shortToLong.get(key) ?? "";
}

/**
 * Your functions will be called as such:
 * decode(encode(strs));
 */
```

## Php

```php
class Codec {
    /**
     * @var array
     */
    private $urlMap = [];

    /**
     * @var string
     */
    private $alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';

    /**
     * Encodes a URL to a shortened URL.
     * @param String $longUrl
     * @return String
     */
    function encode($longUrl) {
        // generate a unique 6-character key
        do {
            $key = '';
            for ($i = 0; $i < 6; $i++) {
                $idx = random_int(0, 61);
                $key .= $this->alphabet[$idx];
            }
        } while (isset($this->urlMap[$key]));
        $this->urlMap[$key] = $longUrl;
        return "http://tinyurl.com/" . $key;
    }

    /**
     * Decodes a shortened URL to its original URL.
     * @param String $shortUrl
     * @return String
     */
    function decode($shortUrl) {
        $parts = explode('/', $shortUrl);
        $key = end($parts);
        return $this->urlMap[$key] ?? "";
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * $obj = new Codec();
 * $s = $obj->encode($longUrl);
 * $ans = $obj->decode($s);
 */
```

## Swift

```swift
class Codec {
    private var urlMap = [String: String]()
    private let baseURL = "http://tinyurl.com/"
    private var counter = 0
    private let charset = Array("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    
    // Encodes a URL to a shortened URL.
    func encode(_ longUrl: String) -> String {
        counter += 1
        let key = toBase62(counter)
        urlMap[key] = longUrl
        return baseURL + key
    }
    
    // Decodes a shortened URL to its original URL.
    func decode(_ shortUrl: String) -> String {
        let key = String(shortUrl.dropFirst(baseURL.count))
        return urlMap[key] ?? ""
    }
    
    private func toBase62(_ number: Int) -> String {
        var n = number
        var chars = [Character]()
        let base = charset.count
        while n > 0 {
            let rem = n % base
            chars.append(charset[rem])
            n /= base
        }
        return String(chars.reversed())
    }
}
```

## Kotlin

```kotlin
class Codec() {
    private val map = HashMap<String, String>()
    private val chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".toCharArray()
    private val base = "http://tinyurl.com/"

    fun encode(longUrl: String): String {
        var key: String
        do {
            val sb = StringBuilder()
            repeat(6) { sb.append(chars[kotlin.random.Random.nextInt(chars.size)]) }
            key = sb.toString()
        } while (map.containsKey(key))
        map[key] = longUrl
        return base + key
    }

    fun decode(shortUrl: String): String {
        val key = shortUrl.substringAfterLast('/')
        return map[key] ?: ""
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * var obj = Codec()
 * var url = obj.encode(longUrl)
 * var ans = obj.decode(url)
 */
```

## Golang

```go
import "strings"

type Codec struct {
	id int
	mp map[string]string
}

func Constructor() Codec {
	return Codec{
		id: 0,
		mp: make(map[string]string),
	}
}

const charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

func toBase62(num int) string {
	if num == 0 {
		return string(charset[0])
	}
	var sb []byte
	for num > 0 {
		rem := num % 62
		sb = append([]byte{charset[rem]}, sb...)
		num /= 62
	}
	return string(sb)
}

// Encodes a URL to a shortened URL.
func (c *Codec) encode(longUrl string) string {
	c.id++
	key := toBase62(c.id)
	c.mp[key] = longUrl
	return "http://tinyurl.com/" + key
}

// Decodes a shortened URL to its original URL.
func (c *Codec) decode(shortUrl string) string {
	idx := strings.LastIndex(shortUrl, "/")
	if idx == -1 || idx+1 >= len(shortUrl) {
		return ""
	}
	key := shortUrl[idx+1:]
	if val, ok := c.mp[key]; ok {
		return val
	}
	return ""
}

/**
 * Your Codec object will be instantiated and called as such:
 * obj := Constructor();
 * url := obj.encode(longUrl);
 * ans := obj.decode(url);
 */
```

## Ruby

```ruby
$map ||= {}
$reverse ||= {}
$counter ||= 1

def int_to_base62(num)
  chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  return chars[0] if num == 0
  s = ''
  base = 62
  while num > 0
    s << chars[num % base]
    num /= base
  end
  s.reverse
end

def encode(longUrl)
  if $reverse.key?(longUrl)
    code = $reverse[longUrl]
    return "http://tinyurl.com/#{code}"
  end
  code = int_to_base62($counter)
  $counter += 1
  $map[code] = longUrl
  $reverse[longUrl] = code
  "http://tinyurl.com/#{code}"
end

def decode(shortUrl)
  code = shortUrl.split('/').last
  $map[code]
end
```

## Scala

```scala
import scala.collection.mutable
import scala.util.Random

class Codec {
  private val urlMap = mutable.HashMap[String, String]()
  private val baseUrl = "http://tinyurl.com/"
  private val chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".toCharArray
  private val rand = new Random()

  private def generateKey(): String = {
    val sb = new StringBuilder(6)
    for (_ <- 0 until 6) {
      sb.append(chars(rand.nextInt(chars.length)))
    }
    sb.toString()
  }

  // Encodes a URL to a shortened URL.
  def encode(longURL: String): String = {
    var key = generateKey()
    while (urlMap.contains(key)) {
      key = generateKey()
    }
    urlMap.put(key, longURL)
    baseUrl + key
  }

  // Decodes a shortened URL to its original URL.
  def decode(shortURL: String): String = {
    val key = shortURL.substring(shortURL.lastIndexOf('/') + 1)
    urlMap.getOrElse(key, "")
  }
}

/**
 * Your Codec object will be instantiated and called as such:
 * var obj = new Codec()
 * val s = obj.encode(longURL)
 * val ans = obj.decode(s)
 */
```

## Rust

```rust
use std::collections::HashMap;
use std::cell::RefCell;

struct Codec {
    map: RefCell<HashMap<String, String>>,
    counter: RefCell<u64>,
}

impl Codec {
    fn new() -> Self {
        Codec {
            map: RefCell::new(HashMap::new()),
            counter: RefCell::new(1),
        }
    }

    // Encodes a URL to a shortened URL.
    fn encode(&self, longURL: String) -> String {
        let mut cnt = self.counter.borrow_mut();
        let id = *cnt;
        *cnt += 1;
        drop(cnt);
        let key = Self::to_base62(id);
        self.map.borrow_mut().insert(key.clone(), longURL);
        format!("http://tinyurl.com/{}", key)
    }

    // Decodes a shortened URL to its original URL.
    fn decode(&self, shortURL: String) -> String {
        if let Some(pos) = shortURL.rfind('/') {
            let key = &shortURL[pos + 1..];
            if let Some(url) = self.map.borrow().get(key) {
                return url.clone();
            }
        }
        String::new()
    }

    fn to_base62(mut num: u64) -> String {
        const CHARSET: &[u8] = b"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        if num == 0 {
            return "0".to_string();
        }
        let mut bytes = Vec::new();
        while num > 0 {
            let rem = (num % 62) as usize;
            bytes.push(CHARSET[rem]);
            num /= 62;
        }
        bytes.reverse();
        String::from_utf8(bytes).unwrap()
    }
}
```
