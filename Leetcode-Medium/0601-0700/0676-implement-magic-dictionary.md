# 0676. Implement Magic Dictionary

## Cpp

```cpp
class MagicDictionary {
public:
    MagicDictionary() {}
    
    void buildDict(std::vector<std::string> dictionary) {
        dict_ = std::move(dictionary);
    }
    
    bool search(std::string searchWord) {
        for (const auto& w : dict_) {
            if (w.size() != searchWord.size()) continue;
            int diff = 0;
            for (size_t i = 0; i < w.size(); ++i) {
                if (w[i] != searchWord[i]) {
                    ++diff;
                    if (diff > 1) break;
                }
            }
            if (diff == 1) return true;
        }
        return false;
    }
    
private:
    std::vector<std::string> dict_;
};

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary* obj = new MagicDictionary();
 * obj->buildDict(dictionary);
 * bool param_2 = obj->search(searchWord);
 */
```

## Java

```java
class MagicDictionary {
    private java.util.List<String> dict;

    public MagicDictionary() {
        dict = new java.util.ArrayList<>();
    }
    
    public void buildDict(String[] dictionary) {
        dict.clear();
        for (String w : dictionary) {
            dict.add(w);
        }
    }
    
    public boolean search(String searchWord) {
        int len = searchWord.length();
        for (String word : dict) {
            if (word.length() != len) continue;
            int diff = 0;
            for (int i = 0; i < len && diff <= 1; i++) {
                if (searchWord.charAt(i) != word.charAt(i)) {
                    diff++;
                }
            }
            if (diff == 1) return true;
        }
        return false;
    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.buildDict(dictionary);
 * boolean param_2 = obj.search(searchWord);
 */
```

## Python

```python
class MagicDictionary(object):
    def __init__(self):
        self.words = []

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        self.words = list(dictionary)

    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        for w in self.words:
            if len(w) != len(searchWord):
                continue
            diff = 0
            for c1, c2 in zip(w, searchWord):
                if c1 != c2:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                return True
        return False
```

## Python3

```python
from typing import List

class MagicDictionary:
    def __init__(self):
        self.words: List[str] = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = dictionary

    def search(self, searchWord: str) -> bool:
        for w in self.words:
            if len(w) != len(searchWord):
                continue
            diff = 0
            for c1, c2 in zip(w, searchWord):
                if c1 != c2:
                    diff += 1
                    if diff > 1:
                        break
            if diff == 1:
                return True
        return False
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    char **words;
    int size;
} MagicDictionary;

MagicDictionary* magicDictionaryCreate() {
    MagicDictionary *obj = (MagicDictionary *)malloc(sizeof(MagicDictionary));
    if (!obj) return NULL;
    obj->words = NULL;
    obj->size = 0;
    return obj;
}

void magicDictionaryBuildDict(MagicDictionary* obj, char** dictionary, int dictionarySize) {
    if (!obj) return;
    obj->words = (char **)malloc(sizeof(char *) * dictionarySize);
    for (int i = 0; i < dictionarySize; ++i) {
        size_t len = strlen(dictionary[i]);
        obj->words[i] = (char *)malloc(len + 1);
        strcpy(obj->words[i], dictionary[i]);
    }
    obj->size = dictionarySize;
}

bool magicDictionarySearch(MagicDictionary* obj, char* searchWord) {
    if (!obj) return false;
    size_t lenS = strlen(searchWord);
    for (int i = 0; i < obj->size; ++i) {
        char *w = obj->words[i];
        if (strlen(w) != lenS) continue;
        int diff = 0;
        for (size_t j = 0; j < lenS && diff <= 1; ++j) {
            if (searchWord[j] != w[j]) ++diff;
        }
        if (diff == 1) return true;
    }
    return false;
}

void magicDictionaryFree(MagicDictionary* obj) {
    if (!obj) return;
    for (int i = 0; i < obj->size; ++i) {
        free(obj->words[i]);
    }
    free(obj->words);
    free(obj);
}
```

## Csharp

```csharp
public class MagicDictionary
{
    private List<string> dict = new List<string>();

    public MagicDictionary()
    {
    }

    public void BuildDict(string[] dictionary)
    {
        dict.Clear();
        foreach (var w in dictionary)
        {
            dict.Add(w);
        }
    }

    public bool Search(string searchWord)
    {
        foreach (var word in dict)
        {
            if (word.Length != searchWord.Length) continue;

            int diff = 0;
            for (int i = 0; i < word.Length && diff <= 1; i++)
            {
                if (word[i] != searchWord[i]) diff++;
            }
            if (diff == 1) return true;
        }
        return false;
    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.BuildDict(dictionary);
 * bool param_2 = obj.Search(searchWord);
 */
```

## Javascript

```javascript
var MagicDictionary = function() {
    this.patternMap = new Map();
    this.wordSet = new Set();
};

/** 
 * @param {string[]} dictionary
 * @return {void}
 */
MagicDictionary.prototype.buildDict = function(dictionary) {
    for (const word of dictionary) {
        this.wordSet.add(word);
        const n = word.length;
        for (let i = 0; i < n; i++) {
            const pattern = word.slice(0, i) + '*' + word.slice(i + 1);
            this.patternMap.set(pattern, (this.patternMap.get(pattern) || 0) + 1);
        }
    }
};

/** 
 * @param {string} searchWord
 * @return {boolean}
 */
MagicDictionary.prototype.search = function(searchWord) {
    const n = searchWord.length;
    for (let i = 0; i < n; i++) {
        const pattern = searchWord.slice(0, i) + '*' + searchWord.slice(i + 1);
        if (this.patternMap.has(pattern)) {
            const cnt = this.patternMap.get(pattern);
            if (!this.wordSet.has(searchWord) || cnt > 1) {
                return true;
            }
        }
    }
    return false;
};
```

## Typescript

```typescript
class MagicDictionary {
    private dict: string[];

    constructor() {
        this.dict = [];
    }

    buildDict(dictionary: string[]): void {
        this.dict = dictionary;
    }

    search(searchWord: string): boolean {
        for (const word of this.dict) {
            if (word.length !== searchWord.length) continue;
            let diff = 0;
            for (let i = 0; i < word.length && diff <= 1; i++) {
                if (word[i] !== searchWord[i]) diff++;
            }
            if (diff === 1) return true;
        }
        return false;
    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * var obj = new MagicDictionary()
 * obj.buildDict(dictionary)
 * var param_2 = obj.search(searchWord)
 */
```

## Php

```php
class MagicDictionary {
    /**
     * @var array
     */
    private $patterns = [];
    /**
     * @var array
     */
    private $wordsSet = [];

    /**
     */
    function __construct() {
        // initialization handled by property defaults
    }

    /**
     * @param String[] $dictionary
     * @return NULL
     */
    function buildDict($dictionary) {
        foreach ($dictionary as $word) {
            $this->wordsSet[$word] = true;
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) {
                $pattern = substr($word, 0, $i) . '*' . substr($word, $i + 1);
                if (!isset($this->patterns[$pattern])) {
                    $this->patterns[$pattern] = 0;
                }
                $this->patterns[$pattern]++;
            }
        }
    }

    /**
     * @param String $searchWord
     * @return Boolean
     */
    function search($searchWord) {
        $len = strlen($searchWord);
        for ($i = 0; $i < $len; $i++) {
            $pattern = substr($searchWord, 0, $i) . '*' . substr($searchWord, $i + 1);
            if (isset($this->patterns[$pattern])) {
                if (!isset($this->wordsSet[$searchWord])) {
                    return true;
                } else {
                    if ($this->patterns[$pattern] > 1) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * $obj = new MagicDictionary();
 * $obj->buildDict($dictionary);
 * $ret_2 = $obj->search($searchWord);
 */
```

## Swift

```swift
class MagicDictionary {
    private var patternMap = [String: Set<String>]()
    
    init() { }
    
    func buildDict(_ dictionary: [String]) {
        for word in dictionary {
            let length = word.count
            for i in 0..<length {
                let left = word.prefix(i)
                let right = word.suffix(length - i - 1)
                let pattern = left + "*" + right
                patternMap[pattern, default: Set<String>()].insert(word)
            }
        }
    }
    
    func search(_ searchWord: String) -> Bool {
        let length = searchWord.count
        for i in 0..<length {
            let left = searchWord.prefix(i)
            let right = searchWord.suffix(length - i - 1)
            let pattern = left + "*" + right
            if let candidates = patternMap[pattern] {
                // need at least one word different from searchWord
                for w in candidates where w != searchWord {
                    return true
                }
            }
        }
        return false
    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * let obj = MagicDictionary()
 * obj.buildDict(dictionary)
 * let ret_2: Bool = obj.search(searchWord)
 */
```

## Kotlin

```kotlin
class MagicDictionary() {
    private val dict = mutableListOf<String>()

    fun buildDict(dictionary: Array<String>) {
        dict.clear()
        dict.addAll(dictionary)
    }

    fun search(searchWord: String): Boolean {
        for (word in dict) {
            if (word.length != searchWord.length) continue
            var diff = 0
            for (i in word.indices) {
                if (word[i] != searchWord[i]) {
                    diff++
                    if (diff > 1) break
                }
            }
            if (diff == 1) return true
        }
        return false
    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * var obj = MagicDictionary()
 * obj.buildDict(dictionary)
 * var param_2 = obj.search(searchWord)
 */
```

## Dart

```dart
class MagicDictionary {
  List<String> _dict = [];

  MagicDictionary() {
    // Constructor
  }

  void buildDict(List<String> dictionary) {
    _dict = List.from(dictionary);
  }

  bool search(String searchWord) {
    for (var word in _dict) {
      if (word.length != searchWord.length) continue;
      int diff = 0;
      for (int i = 0; i < word.length; i++) {
        if (word.codeUnitAt(i) != searchWord.codeUnitAt(i)) {
          diff++;
          if (diff > 1) break;
        }
      }
      if (diff == 1) return true;
    }
    return false;
  }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = MagicDictionary();
 * obj.buildDict(dictionary);
 * bool param2 = obj.search(searchWord);
 */
```

## Golang

```go
type MagicDictionary struct {
	dict []string
}

func Constructor() MagicDictionary {
	return MagicDictionary{}
}

func (this *MagicDictionary) BuildDict(dictionary []string) {
	this.dict = make([]string, len(dictionary))
	copy(this.dict, dictionary)
}

func (this *MagicDictionary) Search(searchWord string) bool {
	for _, w := range this.dict {
		if len(w) != len(searchWord) {
			continue
		}
		diff := 0
		for i := 0; i < len(w); i++ {
			if w[i] != searchWord[i] {
				diff++
				if diff > 1 {
					break
				}
			}
		}
		if diff == 1 {
			return true
		}
	}
	return false
}
```

## Ruby

```ruby
class MagicDictionary
    def initialize()
        @dict_by_len = Hash.new { |h, k| h[k] = [] }
    end

=begin
    :type dictionary: String[]
    :rtype: Void
=end
    def build_dict(dictionary)
        dictionary.each do |word|
            @dict_by_len[word.length] << word
        end
    end

=begin
    :type search_word: String
    :rtype: Boolean
=end
    def search(search_word)
        candidates = @dict_by_len[search_word.length]
        candidates.each do |w|
            diff = 0
            w.length.times do |i|
                diff += 1 if w[i] != search_word[i]
                break if diff > 1
            end
            return true if diff == 1
        end
        false
    end
end
```

## Scala

```scala
class MagicDictionary() {

  import scala.collection.mutable

  private val patternCount = mutable.Map[String, Int]()
  private var dictSet: Set[String] = Set.empty

  def buildDict(dictionary: Array[String]): Unit = {
    patternCount.clear()
    dictSet = dictionary.toSet
    for (word <- dictionary) {
      val len = word.length
      for (i <- 0 until len) {
        val pattern = word.substring(0, i) + '*' + word.substring(i + 1)
        patternCount(pattern) = patternCount.getOrElse(pattern, 0) + 1
      }
    }
  }

  def search(searchWord: String): Boolean = {
    val len = searchWord.length
    for (i <- 0 until len) {
      val pattern = searchWord.substring(0, i) + '*' + searchWord.substring(i + 1)
      patternCount.get(pattern) match {
        case Some(cnt) =>
          if (cnt > 1 || !dictSet.contains(searchWord)) return true
        case None => // do nothing
      }
    }
    false
  }

}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * val obj = new MagicDictionary()
 * obj.buildDict(dictionary)
 * val param_2 = obj.search(searchWord)
 */
```

## Rust

```rust
use std::cell::RefCell;
use std::collections::HashMap;

struct MagicDictionary {
    dict: RefCell<HashMap<usize, Vec<String>>>,
}

impl MagicDictionary {
    fn new() -> Self {
        MagicDictionary {
            dict: RefCell::new(HashMap::new()),
        }
    }

    fn build_dict(&self, dictionary: Vec<String>) {
        let mut map: HashMap<usize, Vec<String>> = HashMap::new();
        for word in dictionary {
            map.entry(word.len()).or_insert_with(Vec::new).push(word);
        }
        *self.dict.borrow_mut() = map;
    }

    fn search(&self, search_word: String) -> bool {
        let len = search_word.len();
        if let Some(candidates) = self.dict.borrow().get(&len) {
            for cand in candidates {
                let mut diff = 0;
                let a = cand.as_bytes();
                let b = search_word.as_bytes();
                for i in 0..len {
                    if a[i] != b[i] {
                        diff += 1;
                        if diff > 1 {
                            break;
                        }
                    }
                }
                if diff == 1 {
                    return true;
                }
            }
        }
        false
    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * let obj = MagicDictionary::new();
 * obj.build_dict(dictionary);
 * let ret_2: bool = obj.search(searchWord);
 */
```

## Racket

```racket
(define magic-dictionary%
  (class object%
    (super-new)

    ;; store the words of the dictionary
    (define dict '())

    ;; build-dict : (listof string?) -> void?
    (define/public (build-dict dictionary)
      (set! dict dictionary))

    ;; helper: true if two strings differ by exactly one character
    (define (diff-one? w1 w2)
      (let ([len (string-length w1)])
        (let loop ([i 0] [cnt 0])
          (cond
            [(= i len) (= cnt 1)]
            [else
             (let* ([c1 (string-ref w1 i)]
                    [c2 (string-ref w2 i)]
                    [new-cnt (+ cnt (if (char=? c1 c2) 0 1))])
               (if (> new-cnt 1)
                   #f
                   (loop (+ i 1) new-cnt)))]))))

    ;; search : string? -> boolean?
    (define/public (search search-word)
      (let loop ((lst dict))
        (cond
          [(null? lst) #f]
          [else
           (let ([w (car lst)])
             (if (= (string-length w) (string-length search-word))
                 (if (diff-one? w search-word)
                     #t
                     (loop (cdr lst)))
                 (loop (cdr lst))))])))))
```

## Erlang

```erlang
-export([magic_dictionary_init_/0,
          magic_dictionary_build_dict/1,
          magic_dictionary_search/1]).

magic_dictionary_init_() ->
    put(magic_dict, []).

magic_dictionary_build_dict(Dictionary) ->
    put(magic_dict, Dictionary).

magic_dictionary_search(SearchWord) ->
    Dict = get(magic_dict),
    lists:any(fun(W) -> exactly_one_diff(W, SearchWord) end, Dict).

exactly_one_diff(Bin1, Bin2) when byte_size(Bin1) =:= byte_size(Bin2) ->
    diff_one(binary_to_list(Bin1), binary_to_list(Bin2), 0);
exactly_one_diff(_, _) -> false.

diff_one([], [], 1) -> true;
diff_one([], [], _) -> false;
diff_one([H|T1], [H|T2], Count) ->
    diff_one(T1, T2, Count);
diff_one([_|T1], [_|T2], Count) ->
    New = Count + 1,
    if New > 1 -> false; true -> diff_one(T1, T2, New) end.
```

## Elixir

```elixir
defmodule MagicDictionary do
  @spec init_() :: any
  def init_() do
    Process.put(:magic_dict, [])
  end

  @spec build_dict(dictionary :: [String.t]) :: any
  def build_dict(dictionary) do
    Process.put(:magic_dict, dictionary)
  end

  @spec search(search_word :: String.t) :: boolean
  def search(search_word) do
    dict = Process.get(:magic_dict, [])
    Enum.any?(dict, fn word ->
      if String.length(word) != String.length(search_word) do
        false
      else
        mismatches =
          word
          |> String.graphemes()
          |> Enum.zip(String.graphemes(search_word))
          |> Enum.count(fn {c1, c2} -> c1 != c2 end)

        mismatches == 1
      end
    end)
  end
end
```
