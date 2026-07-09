# 2227. Encrypt and Decrypt Strings

## Cpp

```cpp
class Encrypter {
public:
    Encrypter(std::vector<char>& keys, std::vector<std::string>& values, std::vector<std::string>& dictionary) {
        for (size_t i = 0; i < keys.size(); ++i) {
            mp_[keys[i]] = values[i];
        }
        for (const auto& w : dictionary) {
            std::string enc;
            bool ok = true;
            for (char c : w) {
                auto it = mp_.find(c);
                if (it == mp_.end()) { ok = false; break; }
                enc += it->second;
            }
            if (ok) ++encCount_[enc];
        }
    }
    
    std::string encrypt(std::string word1) {
        std::string res;
        for (char c : word1) {
            auto it = mp_.find(c);
            if (it == mp_.end()) return "";
            res += it->second;
        }
        return res;
    }
    
    int decrypt(std::string word2) {
        auto it = encCount_.find(word2);
        return it == encCount_.end() ? 0 : it->second;
    }
private:
    std::unordered_map<char, std::string> mp_;
    std::unordered_map<std::string, int> encCount_;
};

/**
 * Your Encrypter object will be instantiated and called as such:
 * Encrypter* obj = new Encrypter(keys, values, dictionary);
 * string param_1 = obj->encrypt(word1);
 * int param_2 = obj->decrypt(word2);
 */
```

## Java

```java
class Encrypter {
    private final java.util.Map<Character, String> encMap;
    private final java.util.Map<String, Integer> dictCount;

    public Encrypter(char[] keys, String[] values, String[] dictionary) {
        encMap = new java.util.HashMap<>();
        for (int i = 0; i < keys.length; ++i) {
            encMap.put(keys[i], values[i]);
        }
        dictCount = new java.util.HashMap<>();
        for (String word : dictionary) {
            String encoded = encode(word);
            if (encoded != null) {
                dictCount.put(encoded, dictCount.getOrDefault(encoded, 0) + 1);
            }
        }
    }

    public String encrypt(String word1) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < word1.length(); ++i) {
            char c = word1.charAt(i);
            String val = encMap.get(c);
            if (val == null) {
                return "";
            }
            sb.append(val);
        }
        return sb.toString();
    }

    public int decrypt(String word2) {
        return dictCount.getOrDefault(word2, 0);
    }

    private String encode(String word) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < word.length(); ++i) {
            char c = word.charAt(i);
            String val = encMap.get(c);
            if (val == null) {
                return null;
            }
            sb.append(val);
        }
        return sb.toString();
    }
}

/**
 * Your Encrypter object will be instantiated and called as such:
 * Encrypter obj = new Encrypter(keys, values, dictionary);
 * String param_1 = obj.encrypt(word1);
 * int param_2 = obj.decrypt(word2);
 */
```

## Python

```python
class Encrypter(object):
    def __init__(self, keys, values, dictionary):
        """
        :type keys: List[str]
        :type values: List[str]
        :type dictionary: List[str]
        """
        self.char_to_val = {k: v for k, v in zip(keys, values)}
        self.enc_counts = {}
        for word in dictionary:
            enc_parts = []
            valid = True
            for ch in word:
                if ch not in self.char_to_val:
                    valid = False
                    break
                enc_parts.append(self.char_to_val[ch])
            if valid:
                enc_word = ''.join(enc_parts)
                self.enc_counts[enc_word] = self.enc_counts.get(enc_word, 0) + 1

    def encrypt(self, word1):
        """
        :type word1: str
        :rtype: str
        """
        res = []
        for ch in word1:
            if ch not in self.char_to_val:
                return ""
            res.append(self.char_to_val[ch])
        return ''.join(res)

    def decrypt(self, word2):
        """
        :type word2: str
        :rtype: int
        """
        return self.enc_counts.get(word2, 0)
```

## Python3

```python
from typing import List, Dict
from collections import defaultdict

class Encrypter:
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.char_to_val: Dict[str, str] = {}
        for k, v in zip(keys, values):
            self.char_to_val[k] = v
        # precompute encrypted forms of dictionary words
        self.enc_count: Dict[str, int] = defaultdict(int)
        for word in dictionary:
            enc = []
            valid = True
            for ch in word:
                if ch not in self.char_to_val:
                    valid = False
                    break
                enc.append(self.char_to_val[ch])
            if valid:
                encrypted_word = ''.join(enc)
                self.enc_count[encrypted_word] += 1

    def encrypt(self, word1: str) -> str:
        res = []
        for ch in word1:
            if ch not in self.char_to_val:
                return ""
            res.append(self.char_to_val[ch])
        return ''.join(res)

    def decrypt(self, word2: str) -> int:
        return self.enc_count.get(word2, 0)
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *valMap[26];      // mapping from character to its 2-char encrypted string
    char **encStr;         // unique encrypted strings from dictionary
    int *encCnt;           // counts of original words producing each encrypted string
    int encSize;           // number of unique entries
} Encrypter;

static char* encryptWord(Encrypter *obj, const char *word) {
    int n = strlen(word);
    char *res = (char *)malloc(2 * n + 1);
    for (int i = 0; i < n; ++i) {
        int idx = word[i] - 'a';
        if (!obj->valMap[idx]) {
            free(res);
            char *empty = (char *)malloc(1);
            empty[0] = '\0';
            return empty;
        }
        res[2 * i]     = obj->valMap[idx][0];
        res[2 * i + 1] = obj->valMap[idx][1];
    }
    res[2 * n] = '\0';
    return res;
}

/** Initialize your data structure here. */
Encrypter* encrypterCreate(char* keys, int keysSize, char** values, int valuesSize,
                           char** dictionary, int dictionarySize) {
    Encrypter *obj = (Encrypter *)malloc(sizeof(Encrypter));
    for (int i = 0; i < 26; ++i) obj->valMap[i] = NULL;
    for (int i = 0; i < keysSize; ++i) {
        int idx = keys[i] - 'a';
        obj->valMap[idx] = values[i];
    }

    obj->encStr = (char **)malloc(sizeof(char *) * dictionarySize);
    obj->encCnt = (int *)malloc(sizeof(int) * dictionarySize);
    obj->encSize = 0;

    for (int i = 0; i < dictionarySize; ++i) {
        char *enc = encryptWord(obj, dictionary[i]);
        if (enc[0] == '\0') { // cannot be encrypted
            free(enc);
            continue;
        }
        int found = -1;
        for (int j = 0; j < obj->encSize; ++j) {
            if (strcmp(obj->encStr[j], enc) == 0) {
                found = j;
                break;
            }
        }
        if (found != -1) {
            obj->encCnt[found] += 1;
            free(enc);
        } else {
            obj->encStr[obj->encSize] = enc;
            obj->encCnt[obj->encSize] = 1;
            obj->encSize += 1;
        }
    }

    return obj;
}

/** Encrypt a string. */
char* encrypterEncrypt(Encrypter* obj, char* word1) {
    return encryptWord(obj, word1);
}

/** Decrypt a string and return the number of possible original strings in the dictionary. */
int encrypterDecrypt(Encrypter* obj, char* word2) {
    for (int i = 0; i < obj->encSize; ++i) {
        if (strcmp(obj->encStr[i], word2) == 0) {
            return obj->encCnt[i];
        }
    }
    return 0;
}

/** Deallocate memory. */
void encrypterFree(Encrypter* obj) {
    for (int i = 0; i < obj->encSize; ++i) {
        free(obj->encStr[i]);
    }
    free(obj->encStr);
    free(obj->encCnt);
    free(obj);
}

/**
 * Your Encrypter struct will be instantiated and called as such:
 * Encrypter* obj = encrypterCreate(keys, keysSize, values, valuesSize, dictionary, dictionarySize);
 * char* param_1 = encrypterEncrypt(obj, word1);
 * int param_2 = encrypterDecrypt(obj, word2);
 * encrypterFree(obj);
 */
```

## Csharp

```csharp
public class Encrypter {
    private readonly Dictionary<char, string> _charToCode;
    private readonly Dictionary<string, int> _codeCount;

    public Encrypter(char[] keys, string[] values, string[] dictionary) {
        _charToCode = new Dictionary<char, string>(keys.Length);
        for (int i = 0; i < keys.Length; i++) {
            _charToCode[keys[i]] = values[i];
        }

        _codeCount = new Dictionary<string, int>();
        foreach (var word in dictionary) {
            var encrypted = EncryptInternal(word);
            if (encrypted != null) {
                if (_codeCount.TryGetValue(encrypted, out var cnt))
                    _codeCount[encrypted] = cnt + 1;
                else
                    _codeCount[encrypted] = 1;
            }
        }
    }

    public string Encrypt(string word1) {
        var result = EncryptInternal(word1);
        return result ?? "";
    }

    private string? EncryptInternal(string word) {
        var sb = new System.Text.StringBuilder();
        foreach (var ch in word) {
            if (!_charToCode.TryGetValue(ch, out var code))
                return null;
            sb.Append(code);
        }
        return sb.ToString();
    }

    public int Decrypt(string word2) {
        return _codeCount.TryGetValue(word2, out var cnt) ? cnt : 0;
    }
}

/**
 * Your Encrypter object will be instantiated and called as such:
 * Encrypter obj = new Encrypter(keys, values, dictionary);
 * string param_1 = obj.Encrypt(word1);
 * int param_2 = obj.Decrypt(word2);
 */
```

## Javascript

```javascript
/**
 * @param {character[]} keys
 * @param {string[]} values
 * @param {string[]} dictionary
 */
var Encrypter = function(keys, values, dictionary) {
    // map from character to its encrypted pair string
    this.charToVal = new Map();
    for (let i = 0; i < keys.length; ++i) {
        this.charToVal.set(keys[i], values[i]);
    }
    
    // precompute encryption of each dictionary word and count occurrences
    this.encCount = new Map(); // encrypted string -> number of original words producing it
    for (const word of dictionary) {
        let enc = [];
        let valid = true;
        for (const ch of word) {
            if (!this.charToVal.has(ch)) { // should not happen per constraints, but guard
                valid = false;
                break;
            }
            enc.push(this.charToVal.get(ch));
        }
        if (!valid) continue;
        const encStr = enc.join('');
        this.encCount.set(encStr, (this.encCount.get(encStr) || 0) + 1);
    }
};

/** 
 * @param {string} word1
 * @return {string}
 */
Encrypter.prototype.encrypt = function(word1) {
    let res = [];
    for (const ch of word1) {
        if (!this.charToVal.has(ch)) return "";
        res.push(this.charToVal.get(ch));
    }
    return res.join('');
};

/** 
 * @param {string} word2
 * @return {number}
 */
Encrypter.prototype.decrypt = function(word2) {
    return this.encCount.get(word2) || 0;
};
```

## Typescript

```typescript
class Encrypter {
    private charToVal: Map<string, string>;
    private encryptedCount: Map<string, number>;

    constructor(keys: string[], values: string[], dictionary: string[]) {
        this.charToVal = new Map();
        for (let i = 0; i < keys.length; ++i) {
            this.charToVal.set(keys[i], values[i]);
        }

        this.encryptedCount = new Map();
        for (const word of dictionary) {
            let enc = '';
            let ok = true;
            for (const ch of word) {
                const v = this.charToVal.get(ch);
                if (v === undefined) {
                    ok = false;
                    break;
                }
                enc += v;
            }
            if (ok) {
                this.encryptedCount.set(enc, (this.encryptedCount.get(enc) ?? 0) + 1);
            }
        }
    }

    encrypt(word1: string): string {
        let res = '';
        for (const ch of word1) {
            const v = this.charToVal.get(ch);
            if (v === undefined) return "";
            res += v;
        }
        return res;
    }

    decrypt(word2: string): number {
        return this.encryptedCount.get(word2) ?? 0;
    }
}

/**
 * Your Encrypter object will be instantiated and called as such:
 * var obj = new Encrypter(keys, values, dictionary)
 * var param_1 = obj.encrypt(word1)
 * var param_2 = obj.decrypt(word2)
 */
```

## Php

```php
class Encrypter {
    private $charToVal = [];
    private $encCount = [];

    /**
     * @param String[] $keys
     * @param String[] $values
     * @param String[] $dictionary
     */
    function __construct($keys, $values, $dictionary) {
        $n = count($keys);
        for ($i = 0; $i < $n; $i++) {
            $this->charToVal[$keys[$i]] = $values[$i];
        }

        foreach ($dictionary as $word) {
            $enc = '';
            $valid = true;
            $len = strlen($word);
            for ($j = 0; $j < $len; $j++) {
                $c = $word[$j];
                if (!isset($this->charToVal[$c])) {
                    $valid = false;
                    break;
                }
                $enc .= $this->charToVal[$c];
            }
            if ($valid) {
                if (!isset($this->encCount[$enc])) {
                    $this->encCount[$enc] = 0;
                }
                $this->encCount[$enc]++;
            }
        }
    }

    /**
     * @param String $word1
     * @return String
     */
    function encrypt($word1) {
        $res = '';
        $len = strlen($word1);
        for ($i = 0; $i < $len; $i++) {
            $c = $word1[$i];
            if (!isset($this->charToVal[$c])) {
                return "";
            }
            $res .= $this->charToVal[$c];
        }
        return $res;
    }

    /**
     * @param String $word2
     * @return Integer
     */
    function decrypt($word2) {
        return $this->encCount[$word2] ?? 0;
    }
}

/**
 * Your Encrypter object will be instantiated and called as such:
 * $obj = new Encrypter($keys, $values, $dictionary);
 * $ret_1 = $obj->encrypt($word1);
 * $ret_2 = $obj->decrypt($word2);
 */
```

## Swift

```swift
class Encrypter {
    private var charToVal: [Character: String] = [:]
    private var encryptedCount: [String: Int] = [:]

    init(_ keys: [Character], _ values: [String], _ dictionary: [String]) {
        for i in 0..<keys.count {
            charToVal[keys[i]] = values[i]
        }
        for word in dictionary {
            var enc = ""
            var valid = true
            for ch in word {
                if let val = charToVal[ch] {
                    enc.append(contentsOf: val)
                } else {
                    valid = false
                    break
                }
            }
            if valid {
                encryptedCount[enc, default: 0] += 1
            }
        }
    }

    func encrypt(_ word1: String) -> String {
        var result = ""
        for ch in word1 {
            guard let val = charToVal[ch] else { return "" }
            result.append(contentsOf: val)
        }
        return result
    }

    func decrypt(_ word2: String) -> Int {
        return encryptedCount[word2] ?? 0
    }
}
```

## Kotlin

```kotlin
class Encrypter(keys: CharArray, values: Array<String>, dictionary: Array<String>) {
    private val charToVal = HashMap<Char, String>()
    private val encryptedCount = HashMap<String, Int>()

    init {
        for (i in keys.indices) {
            charToVal[keys[i]] = values[i]
        }
        for (word in dictionary) {
            val sb = StringBuilder()
            var valid = true
            for (c in word) {
                val v = charToVal[c]
                if (v == null) {
                    valid = false
                    break
                }
                sb.append(v)
            }
            if (valid) {
                val enc = sb.toString()
                encryptedCount[enc] = (encryptedCount[enc] ?: 0) + 1
            }
        }
    }

    fun encrypt(word1: String): String {
        val sb = StringBuilder()
        for (c in word1) {
            val v = charToVal[c] ?: return ""
            sb.append(v)
        }
        return sb.toString()
    }

    fun decrypt(word2: String): Int {
        return encryptedCount[word2] ?: 0
    }
}

/**
 * Your Encrypter object will be instantiated and called as such:
 * var obj = Encrypter(keys, values, dictionary)
 * var param_1 = obj.encrypt(word1)
 * var param_2 = obj.decrypt(word2)
 */
```

## Dart

```dart
class Encrypter {
  final Map<String, String> _charToCode = {};
  final Map<String, int> _codeCount = {};

  Encrypter(List<String> keys, List<String> values, List<String> dictionary) {
    for (int i = 0; i < keys.length; ++i) {
      _charToCode[keys[i]] = values[i];
    }
    for (final word in dictionary) {
      final enc = _encryptInternal(word);
      if (enc != null) {
        _codeCount[enc] = (_codeCount[enc] ?? 0) + 1;
      }
    }
  }

  String encrypt(String word1) {
    final enc = _encryptInternal(word1);
    return enc ?? "";
  }

  int decrypt(String word2) {
    return _codeCount[word2] ?? 0;
  }

  String? _encryptInternal(String word) {
    final sb = StringBuffer();
    for (int i = 0; i < word.length; ++i) {
      final ch = word[i];
      final code = _charToCode[ch];
      if (code == null) return null;
      sb.write(code);
    }
    return sb.toString();
  }
}

/**
 * Your Encrypter object will be instantiated and called as such:
 * Encrypter obj = Encrypter(keys, values, dictionary);
 * String param1 = obj.encrypt(word1);
 * int param2 = obj.decrypt(word2);
 */
```

## Golang

```go
type Encrypter struct {
	encMap   [26]string
	decCount map[string]int
}

func Constructor(keys []byte, values []string, dictionary []string) Encrypter {
	e := Encrypter{
		decCount: make(map[string]int),
	}
	for i, k := range keys {
		e.encMap[k-'a'] = values[i]
	}
	for _, w := range dictionary {
		var sb []byte
		ok := true
		for j := 0; j < len(w); j++ {
			val := e.encMap[w[j]-'a']
			if val == "" {
				ok = false
				break
			}
			sb = append(sb, val[0], val[1])
		}
		if ok {
			e.decCount[string(sb)]++
		}
	}
	return e
}

func (this *Encrypter) Encrypt(word1 string) string {
	var sb []byte
	for i := 0; i < len(word1); i++ {
		val := this.encMap[word1[i]-'a']
		if val == "" {
			return ""
		}
		sb = append(sb, val[0], val[1])
	}
	return string(sb)
}

func (this *Encrypter) Decrypt(word2 string) int {
	if cnt, ok := this.decCount[word2]; ok {
		return cnt
	}
	return 0
}

/**
 * Your Encrypter object will be instantiated and called as such:
 * obj := Constructor(keys, values, dictionary);
 * param_1 := obj.Encrypt(word1);
 * param_2 := obj.Decrypt(word2);
 */
```

## Ruby

```ruby
class Encrypter
  # :type keys: Character[]
  # :type values: String[]
  # :type dictionary: String[]
  def initialize(keys, values, dictionary)
    @char_to_val = {}
    keys.each_with_index { |k, i| @char_to_val[k] = values[i] }

    @enc_count = Hash.new(0)
    dictionary.each do |word|
      enc = ""
      valid = true
      word.each_char do |ch|
        val = @char_to_val[ch]
        if val.nil?
          valid = false
          break
        end
        enc << val
      end
      @enc_count[enc] += 1 if valid
    end
  end

  # :type word1: String
  # :rtype: String
  def encrypt(word1)
    result = ""
    word1.each_char do |c|
      v = @char_to_val[c]
      return "" if v.nil?
      result << v
    end
    result
  end

  # :type word2: String
  # :rtype: Integer
  def decrypt(word2)
    @enc_count[word2] || 0
  end
end
```

## Scala

```scala
class Encrypter(_keys: Array[Char], _values: Array[String], _dictionary: Array[String]) {

  private val charToVal = {
    val m = scala.collection.mutable.HashMap[Char, String]()
    var i = 0
    while (i < _keys.length) {
      m(_keys(i)) = _values(i)
      i += 1
    }
    m.toMap
  }

  private val encCount: Map[String, Int] = {
    val cnt = scala.collection.mutable.HashMap[String, Int]().withDefaultValue(0)
    for (word <- _dictionary) {
      val sb = new StringBuilder()
      var ok = true
      var idx = 0
      while (idx < word.length && ok) {
        charToVal.get(word.charAt(idx)) match {
          case Some(v) => sb.append(v)
          case None    => ok = false
        }
        idx += 1
      }
      if (ok) {
        val enc = sb.toString()
        cnt(enc) = cnt(enc) + 1
      }
    }
    cnt.toMap
  }

  def encrypt(word1: String): String = {
    val sb = new StringBuilder()
    var i = 0
    while (i < word1.length) {
      charToVal.get(word1.charAt(i)) match {
        case Some(v) => sb.append(v)
        case None    => return ""
      }
      i += 1
    }
    sb.toString()
  }

  def decrypt(word2: String): Int = {
    encCount.getOrElse(word2, 0)
  }
}

/**
 * Your Encrypter object will be instantiated and called as such:
 * val obj = new Encrypter(keys, values, dictionary)
 * val param_1 = obj.encrypt(word1)
 * val param_2 = obj.decrypt(word2)
 */
```

## Rust

```rust
use std::collections::HashMap;

struct Encrypter {
    enc_map: HashMap<char, String>,
    dict_counts: HashMap<String, i32>,
}

impl Encrypter {
    fn new(keys: Vec<char>, values: Vec<String>, dictionary: Vec<String>) -> Self {
        let mut enc_map = HashMap::new();
        for (k, v) in keys.into_iter().zip(values.into_iter()) {
            enc_map.insert(k, v);
        }

        let mut dict_counts: HashMap<String, i32> = HashMap::new();
        for word in dictionary.iter() {
            let mut encrypted = String::new();
            let mut ok = true;
            for ch in word.chars() {
                if let Some(val) = enc_map.get(&ch) {
                    encrypted.push_str(val);
                } else {
                    ok = false;
                    break;
                }
            }
            if ok {
                *dict_counts.entry(encrypted).or_insert(0) += 1;
            }
        }

        Encrypter { enc_map, dict_counts }
    }

    fn encrypt(&self, word1: String) -> String {
        let mut res = String::new();
        for ch in word1.chars() {
            if let Some(val) = self.enc_map.get(&ch) {
                res.push_str(val);
            } else {
                return "".to_string();
            }
        }
        res
    }

    fn decrypt(&self, word2: String) -> i32 {
        *self.dict_counts.get(&word2).unwrap_or(&0)
    }
}

/**
 * Your Encrypter object will be instantiated and called as such:
 * let obj = Encrypter::new(keys, values, dictionary);
 * let ret_1: String = obj.encrypt(word1);
 * let ret_2: i32 = obj.decrypt(word2);
 */
```

## Racket

```racket
(define encrypter%
  (class object%
    (init-field keys values dictionary)
    (super-new)

    ;; private hash tables
    (define encrypt-map (make-hash))
    (define decrypt-count (make-hash))

    ;; build encryption map: char -> two‑letter string
    (for ([k keys] [v values])
      (hash-set! encrypt-map k v))

    ;; pre‑compute encrypted forms of dictionary words and count them
    (for ([word dictionary])
      (let loop ((i 0)
                 (len (string-length word))
                 (enc ""))
        (if (= i len)
            (hash-set! decrypt-count enc (+ (hash-ref decrypt-count enc 0) 1))
            (let* ([c (string-ref word i)]
                   [v (hash-ref encrypt-map c #f)])
              (if v
                  (loop (+ i 1) len (string-append enc v))
                  (void))))))

    ;; encrypt a word; return empty string if any character lacks mapping
    (define/public (encrypt word1)
      (let loop ((i 0)
                 (len (string-length word1))
                 (result ""))
        (if (= i len)
            result
            (let* ([c (string-ref word1 i)]
                   [v (hash-ref encrypt-map c #f)])
              (if v
                  (loop (+ i 1) len (string-append result v))
                  "")))))

    ;; decrypt: number of dictionary words that could produce the given encrypted string
    (define/public (decrypt word2)
      (hash-ref decrypt-count word2 0))))
```

## Erlang

```erlang
-export([encrypter_init_/3, encrypter_encrypt/1, encrypter_decrypt/1]).

-spec encrypter_init_(Keys :: [unicode:unicode_binary()], Values :: [unicode:unicode_binary()], Dictionary :: [unicode:unicode_binary()]) -> any().
encrypter_init_(Keys, Values, Dictionary) ->
    CharMap = maps:from_list(lists:zip(Keys, Values)),
    put(char_map, CharMap),
    EncCount = build_enc_count(CharMap, Dictionary),
    put(enc_count, EncCount).

-spec encrypter_encrypt(Word1 :: unicode:unicode_binary()) -> unicode:unicode_binary().
encrypter_encrypt(Word1) ->
    case get(char_map) of
        undefined -> <<>>;
        CharMap ->
            Bytes = binary_to_list(Word1),
            case encrypt_word(Bytes, CharMap) of
                {error, _} -> <<>>;
                {ok, RevIolist} -> iolist_to_binary(lists:reverse(RevIolist))
            end
    end.

-spec encrypter_decrypt(Word2 :: unicode:unicode_binary()) -> integer().
encrypter_decrypt(Word2) ->
    case get(enc_count) of
        undefined -> 0;
        EncCount -> maps:get(Word2, EncCount, 0)
    end.

%% internal helpers

build_enc_count(CharMap, Dictionary) ->
    lists:foldl(fun(Word, Acc) ->
        case encrypt_binary(Word, CharMap) of
            error -> Acc;
            {ok, Enc} ->
                maps:update_with(Enc,
                    fun(C) -> C + 1 end,
                    1,
                    Acc)
        end
    end, #{}, Dictionary).

encrypt_binary(WordBin, CharMap) ->
    Bytes = binary_to_list(WordBin),
    case encrypt_word(Bytes, CharMap) of
        {error, _} -> error;
        {ok, RevIolist} -> {ok, iolist_to_binary(lists:reverse(RevIolist))}
    end.

encrypt_word([], _) ->
    {ok, []};
encrypt_word([Code | Rest], CharMap) ->
    CharBin = <<Code>>,
    case maps:get(CharBin, CharMap, undefined) of
        undefined -> {error, []};
        Val ->
            case encrypt_word(Rest, CharMap) of
                {error, _}=Err -> Err;
                {ok, Acc} -> {ok, [Val | Acc]}
            end
    end.
```

## Elixir

```elixir
defmodule Encrypter do
  @spec init_([String.t()], [String.t()], [String.t()]) :: :ok
  def init_(keys, values, dictionary) do
    key_to_val = Enum.zip(keys, values) |> Map.new()

    encrypted_counts =
      Enum.reduce(dictionary, %{}, fn word, acc ->
        case encrypt_word(word, key_to_val) do
          nil -> acc
          enc -> Map.update(acc, enc, 1, &(&1 + 1))
        end
      end)

    Process.put(:encrypter_state, %{key_to_val: key_to_val, encrypted_counts: encrypted_counts})
    :ok
  end

  @spec encrypt(String.t()) :: String.t()
  def encrypt(word) do
    state = Process.get(:encrypter_state)
    case encrypt_word(word, state.key_to_val) do
      nil -> ""
      enc -> enc
    end
  end

  @spec decrypt(String.t()) :: integer
  def decrypt(enc_word) do
    state = Process.get(:encrypter_state)
    Map.get(state.encrypted_counts, enc_word, 0)
  end

  defp encrypt_word(word, map) do
    Enum.reduce_while(String.graphemes(word), "", fn ch, acc ->
      case Map.fetch(map, ch) do
        {:ok, val} -> {:cont, acc <> val}
        :error -> {:halt, nil}
      end
    end)
  end
end
```
