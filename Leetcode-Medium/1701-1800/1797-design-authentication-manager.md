# 1797. Design Authentication Manager

## Cpp

```cpp
class AuthenticationManager {
public:
    AuthenticationManager(int timeToLive) : ttl(timeToLive) {}
    
    void generate(std::string tokenId, int currentTime) {
        expiry[tokenId] = currentTime + ttl;
    }
    
    void renew(std::string tokenId, int currentTime) {
        auto it = expiry.find(tokenId);
        if (it != expiry.end() && it->second > currentTime) {
            it->second = currentTime + ttl;
        }
    }
    
    int countUnexpiredTokens(int currentTime) {
        int cnt = 0;
        for (const auto& p : expiry) {
            if (p.second > currentTime) ++cnt;
        }
        return cnt;
    }
private:
    int ttl;
    std::unordered_map<std::string, int> expiry;
};

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * AuthenticationManager* obj = new AuthenticationManager(timeToLive);
 * obj->generate(tokenId,currentTime);
 * obj->renew(tokenId,currentTime);
 * int param_3 = obj->countUnexpiredTokens(currentTime);
 */
```

## Java

```java
class AuthenticationManager {
    private final int timeToLive;
    private final java.util.Map<String, Integer> expiryMap;

    public AuthenticationManager(int timeToLive) {
        this.timeToLive = timeToLive;
        this.expiryMap = new java.util.HashMap<>();
    }

    public void generate(String tokenId, int currentTime) {
        expiryMap.put(tokenId, currentTime + timeToLive);
    }

    public void renew(String tokenId, int currentTime) {
        Integer exp = expiryMap.get(tokenId);
        if (exp != null && exp > currentTime) {
            expiryMap.put(tokenId, currentTime + timeToLive);
        }
    }

    public int countUnexpiredTokens(int currentTime) {
        int count = 0;
        java.util.Iterator<java.util.Map.Entry<String, Integer>> it = expiryMap.entrySet().iterator();
        while (it.hasNext()) {
            java.util.Map.Entry<String, Integer> entry = it.next();
            if (entry.getValue() > currentTime) {
                count++;
            } else {
                // clean up expired token
                it.remove();
            }
        }
        return count;
    }
}
```

## Python

```python
class AuthenticationManager(object):
    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        self.ttl = timeToLive
        self.expiry = {}  # tokenId -> expiration time

    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        self.expiry[tokenId] = currentTime + self.ttl

    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        exp = self.expiry.get(tokenId)
        if exp is not None and exp > currentTime:
            self.expiry[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """
        # Optionally clean up expired tokens to keep dict small
        cnt = 0
        for token, exp in list(self.expiry.items()):
            if exp > currentTime:
                cnt += 1
            else:
                del self.expiry[token]
        return cnt
```

## Python3

```python
class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.expiry = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.expiry[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        exp = self.expiry.get(tokenId)
        if exp is not None and exp > currentTime:
            self.expiry[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        expired = []
        for token, exp in self.expiry.items():
            if exp > currentTime:
                cnt += 1
            else:
                expired.append(token)
        for token in expired:
            del self.expiry[token]
        return cnt
```

## C

```c
typedef struct {
    char token[7];   // tokenId length <=5, plus null terminator
    int expiry;
} Node;

typedef struct {
    int ttl;
    int size;
    int capacity;
    Node *nodes;
} AuthenticationManager;

static void ensureCapacity(AuthenticationManager *obj) {
    if (obj->size >= obj->capacity) {
        obj->capacity *= 2;
        obj->nodes = (Node *)realloc(obj->nodes, obj->capacity * sizeof(Node));
    }
}

AuthenticationManager* authenticationManagerCreate(int timeToLive) {
    AuthenticationManager *obj = (AuthenticationManager *)malloc(sizeof(AuthenticationManager));
    obj->ttl = timeToLive;
    obj->size = 0;
    obj->capacity = 256;
    obj->nodes = (Node *)malloc(obj->capacity * sizeof(Node));
    return obj;
}

void authenticationManagerGenerate(AuthenticationManager* obj, char* tokenId, int currentTime) {
    ensureCapacity(obj);
    Node *node = &obj->nodes[obj->size++];
    strcpy(node->token, tokenId);
    node->expiry = currentTime + obj->ttl;
}

void authenticationManagerRenew(AuthenticationManager* obj, char* tokenId, int currentTime) {
    for (int i = 0; i < obj->size; ++i) {
        if (strcmp(obj->nodes[i].token, tokenId) == 0) {
            if (obj->nodes[i].expiry > currentTime) {
                obj->nodes[i].expiry = currentTime + obj->ttl;
            }
            break;
        }
    }
}

int authenticationManagerCountUnexpiredTokens(AuthenticationManager* obj, int currentTime) {
    int cnt = 0;
    for (int i = 0; i < obj->size; ++i) {
        if (obj->nodes[i].expiry > currentTime) {
            ++cnt;
        }
    }
    return cnt;
}

void authenticationManagerFree(AuthenticationManager* obj) {
    if (!obj) return;
    free(obj->nodes);
    free(obj);
}
```

## Csharp

```csharp
public class AuthenticationManager
{
    private readonly int _timeToLive;
    private readonly Dictionary<string, int> _tokens = new Dictionary<string, int>();

    public AuthenticationManager(int timeToLive)
    {
        _timeToLive = timeToLive;
    }

    public void Generate(string tokenId, int currentTime)
    {
        _tokens[tokenId] = currentTime + _timeToLive;
    }

    public void Renew(string tokenId, int currentTime)
    {
        if (_tokens.TryGetValue(tokenId, out int expiry) && expiry > currentTime)
        {
            _tokens[tokenId] = currentTime + _timeToLive;
        }
    }

    public int CountUnexpiredTokens(int currentTime)
    {
        int count = 0;
        var keysToRemove = new List<string>();
        foreach (var kvp in _tokens)
        {
            if (kvp.Value > currentTime)
                count++;
            else
                keysToRemove.Add(kvp.Key);
        }
        // Optional cleanup of expired tokens
        foreach (var key in keysToRemove)
            _tokens.Remove(key);
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} timeToLive
 */
var AuthenticationManager = function(timeToLive) {
    this.timeToLive = timeToLive;
    this.tokens = new Map(); // tokenId -> expiryTime
};

/** 
 * @param {string} tokenId 
 * @param {number} currentTime
 * @return {void}
 */
AuthenticationManager.prototype.generate = function(tokenId, currentTime) {
    this.tokens.set(tokenId, currentTime + this.timeToLive);
};

/** 
 * @param {string} tokenId 
 * @param {number} currentTime
 * @return {void}
 */
AuthenticationManager.prototype.renew = function(tokenId, currentTime) {
    if (!this.tokens.has(tokenId)) return;
    const expiry = this.tokens.get(tokenId);
    if (expiry > currentTime) {
        this.tokens.set(tokenId, currentTime + this.timeToLive);
    } else {
        // token already expired
        this.tokens.delete(tokenId);
    }
};

/** 
 * @param {number} currentTime
 * @return {number}
 */
AuthenticationManager.prototype.countUnexpiredTokens = function(currentTime) {
    for (const [tokenId, expiry] of this.tokens.entries()) {
        if (expiry <= currentTime) {
            this.tokens.delete(tokenId);
        }
    }
    return this.tokens.size;
};
```

## Typescript

```typescript
class AuthenticationManager {
    private ttl: number;
    private tokens: Map<string, number>;

    constructor(timeToLive: number) {
        this.ttl = timeToLive;
        this.tokens = new Map();
    }

    generate(tokenId: string, currentTime: number): void {
        this.tokens.set(tokenId, currentTime + this.ttl);
    }

    renew(tokenId: string, currentTime: number): void {
        const expiry = this.tokens.get(tokenId);
        if (expiry !== undefined && expiry > currentTime) {
            this.tokens.set(tokenId, currentTime + this.ttl);
        }
    }

    countUnexpiredTokens(currentTime: number): number {
        for (const [id, expiry] of this.tokens.entries()) {
            if (expiry <= currentTime) {
                this.tokens.delete(id);
            }
        }
        return this.tokens.size;
    }
}

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * var obj = new AuthenticationManager(timeToLive)
 * obj.generate(tokenId,currentTime)
 * obj.renew(tokenId,currentTime)
 * var param_3 = obj.countUnexpiredTokens(currentTime)
 */
```

## Php

```php
class AuthenticationManager {
    private $ttl;
    private $tokens;

    /**
     * @param Integer $timeToLive
     */
    function __construct($timeToLive) {
        $this->ttl = $timeToLive;
        $this->tokens = [];
    }

    /**
     * @param String $tokenId
     * @param Integer $currentTime
     * @return NULL
     */
    function generate($tokenId, $currentTime) {
        $this->tokens[$tokenId] = $currentTime + $this->ttl;
    }

    /**
     * @param String $tokenId
     * @param Integer $currentTime
     * @return NULL
     */
    function renew($tokenId, $currentTime) {
        if (isset($this->tokens[$tokenId]) && $this->tokens[$tokenId] > $currentTime) {
            $this->tokens[$tokenId] = $currentTime + $this->ttl;
        }
    }

    /**
     * @param Integer $currentTime
     * @return Integer
     */
    function countUnexpiredTokens($currentTime) {
        $count = 0;
        foreach ($this->tokens as $id => $expiry) {
            if ($expiry > $currentTime) {
                $count++;
            } else {
                unset($this->tokens[$id]);
            }
        }
        return $count;
    }
}

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * $obj = new AuthenticationManager($timeToLive);
 * $obj->generate($tokenId, $currentTime);
 * $obj->renew($tokenId, $currentTime);
 * $ret_3 = $obj->countUnexpiredTokens($currentTime);
 */
```

## Swift

```swift
class AuthenticationManager {
    private let timeToLive: Int
    private var expiryMap: [String: Int]

    init(_ timeToLive: Int) {
        self.timeToLive = timeToLive
        self.expiryMap = [:]
    }

    func generate(_ tokenId: String, _ currentTime: Int) {
        expiryMap[tokenId] = currentTime + timeToLive
    }

    func renew(_ tokenId: String, _ currentTime: Int) {
        if let exp = expiryMap[tokenId], exp > currentTime {
            expiryMap[tokenId] = currentTime + timeToLive
        } else {
            // If expired or not present, ensure it's removed.
            expiryMap.removeValue(forKey: tokenId)
        }
    }

    func countUnexpiredTokens(_ currentTime: Int) -> Int {
        var count = 0
        var toRemove: [String] = []
        for (token, exp) in expiryMap {
            if exp > currentTime {
                count += 1
            } else {
                toRemove.append(token)
            }
        }
        for token in toRemove {
            expiryMap.removeValue(forKey: token)
        }
        return count
    }
}
```

## Kotlin

```kotlin
class AuthenticationManager(private val timeToLive: Int) {
    private val expiryMap = HashMap<String, Int>()
    private val pq = java.util.PriorityQueue<Pair<Int, String>>(compareBy { it.first })

    fun generate(tokenId: String, currentTime: Int) {
        clean(currentTime)
        val expireAt = currentTime + timeToLive
        expiryMap[tokenId] = expireAt
        pq.offer(Pair(expireAt, tokenId))
    }

    fun renew(tokenId: String, currentTime: Int) {
        clean(currentTime)
        val oldExpire = expiryMap[tokenId] ?: return
        if (oldExpire > currentTime) {
            val newExpire = currentTime + timeToLive
            expiryMap[tokenId] = newExpire
            pq.offer(Pair(newExpire, tokenId))
        }
    }

    fun countUnexpiredTokens(currentTime: Int): Int {
        clean(currentTime)
        return expiryMap.size
    }

    private fun clean(currentTime: Int) {
        while (pq.isNotEmpty()) {
            val (expireAt, id) = pq.peek()
            if (expireAt <= currentTime) {
                pq.poll()
                val cur = expiryMap[id]
                if (cur != null && cur == expireAt) {
                    expiryMap.remove(id)
                }
            } else break
        }
    }
}
```

## Dart

```dart
class AuthenticationManager {
  final int _timeToLive;
  final Map<String, int> _expiry = {};

  AuthenticationManager(int timeToLive) : _timeToLive = timeToLive;

  void generate(String tokenId, int currentTime) {
    _expiry[tokenId] = currentTime + _timeToLive;
  }

  void renew(String tokenId, int currentTime) {
    final exp = _expiry[tokenId];
    if (exp != null && exp > currentTime) {
      _expiry[tokenId] = currentTime + _timeToLive;
    }
  }

  int countUnexpiredTokens(int currentTime) {
    int count = 0;
    final List<String> toRemove = [];
    _expiry.forEach((token, exp) {
      if (exp > currentTime) {
        count++;
      } else {
        toRemove.add(token);
      }
    });
    for (final token in toRemove) {
      _expiry.remove(token);
    }
    return count;
  }
}

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * AuthenticationManager obj = AuthenticationManager(timeToLive);
 * obj.generate(tokenId,currentTime);
 * obj.renew(tokenId,currentTime);
 * int param3 = obj.countUnexpiredTokens(currentTime);
 */
```

## Golang

```go
type AuthenticationManager struct {
	ttl    int
	tokens map[string]int
}

func Constructor(timeToLive int) AuthenticationManager {
	return AuthenticationManager{
		ttl:    timeToLive,
		tokens: make(map[string]int),
	}
}

func (this *AuthenticationManager) Generate(tokenId string, currentTime int) {
	this.tokens[tokenId] = currentTime + this.ttl
}

func (this *AuthenticationManager) Renew(tokenId string, currentTime int) {
	if exp, ok := this.tokens[tokenId]; ok && exp > currentTime {
		this.tokens[tokenId] = currentTime + this.ttl
	}
}

func (this *AuthenticationManager) CountUnexpiredTokens(currentTime int) int {
	count := 0
	for id, exp := range this.tokens {
		if exp > currentTime {
			count++
		} else {
			delete(this.tokens, id)
		}
	}
	return count
}

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * obj := Constructor(timeToLive);
 * obj.Generate(tokenId,currentTime);
 * obj.Renew(tokenId,currentTime);
 * param_3 := obj.CountUnexpiredTokens(currentTime);
 */
```

## Ruby

```ruby
class AuthenticationManager
  def initialize(time_to_live)
    @ttl = time_to_live
    @tokens = {}
  end

  def generate(token_id, current_time)
    @tokens[token_id] = current_time + @ttl
  end

  def renew(token_id, current_time)
    expiry = @tokens[token_id]
    if expiry && expiry > current_time
      @tokens[token_id] = current_time + @ttl
    else
      @tokens.delete(token_id) if expiry && expiry <= current_time
    end
  end

  def count_unexpired_tokens(current_time)
    @tokens.delete_if { |_, exp| exp <= current_time }
    @tokens.size
  end
end
```

## Scala

```scala
import scala.collection.mutable
import java.util.PriorityQueue

class AuthenticationManager(_timeToLive: Int) {

  private val ttl = _timeToLive
  private val tokenExp = mutable.Map[String, Int]()
  private val pq = new PriorityQueue[(Int, String)]((a, b) => Integer.compare(a._1, b._1))

  private def clean(currentTime: Int): Unit = {
    while (!pq.isEmpty && pq.peek()._1 <= currentTime) {
      val (exp, id) = pq.poll()
      tokenExp.get(id) match {
        case Some(e) if e == exp => tokenExp -= id
        case _ => // stale entry, ignore
      }
    }
  }

  def generate(tokenId: String, currentTime: Int): Unit = {
    val exp = currentTime + ttl
    tokenExp(tokenId) = exp
    pq.offer((exp, tokenId))
  }

  def renew(tokenId: String, currentTime: Int): Unit = {
    clean(currentTime)
    tokenExp.get(tokenId) match {
      case Some(exp) if exp > currentTime =>
        val newExp = currentTime + ttl
        tokenExp(tokenId) = newExp
        pq.offer((newExp, tokenId))
      case _ => // do nothing
    }
  }

  def countUnexpiredTokens(currentTime: Int): Int = {
    clean(currentTime)
    tokenExp.size
  }
}

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * val obj = new AuthenticationManager(timeToLive)
 * obj.generate(tokenId,currentTime)
 * obj.renew(tokenId,currentTime)
 * val param_3 = obj.countUnexpiredTokens(currentTime)
 */
```

## Rust

```rust
use std::collections::HashMap;

struct AuthenticationManager {
    ttl: i32,
    tokens: HashMap<String, i32>,
}

impl AuthenticationManager {
    fn new(time_to_live: i32) -> Self {
        AuthenticationManager {
            ttl: time_to_live,
            tokens: HashMap::new(),
        }
    }

    fn generate(&mut self, token_id: String, current_time: i32) {
        self.tokens.insert(token_id, current_time + self.ttl);
    }

    fn renew(&mut self, token_id: String, current_time: i32) {
        if let Some(expiry) = self.tokens.get_mut(&token_id) {
            if *expiry > current_time {
                *expiry = current_time + self.ttl;
            }
        }
    }

    fn count_unexpired_tokens(&self, current_time: i32) -> i32 {
        self.tokens.values().filter(|&&exp| exp > current_time).count() as i32
    }
}
```

## Racket

```racket
(define authentication-manager%
  (class object%
    (init-field time-to-live)
    (super-new)

    ;; token-id -> expiry-time
    (field [tokens (make-hash)])

    (define/public (generate token-id current-time)
      (hash-set! tokens token-id (+ current-time time-to-live)))

    (define/public (renew token-id current-time)
      (let ([exp (hash-ref tokens token-id #f)])
        (when (and exp (> exp current-time))
          (hash-set! tokens token-id (+ current-time time-to-live)))))

    (define/public (count-unexpired-tokens current-time)
      (for/sum ([exp (in-hash-values tokens)])
        (if (> exp current-time) 1 0)))) )
```

## Erlang

```erlang
-spec authentication_manager_init_(TimeToLive :: integer()) -> any().
authentication_manager_init_(TimeToLive) ->
    put(ttl, TimeToLive),
    put(tokens, #{}).

-spec authentication_manager_generate(TokenId :: unicode:unicode_binary(), CurrentTime :: integer()) -> any().
authentication_manager_generate(TokenId, CurrentTime) ->
    TTL = get(ttl),
    Expiry = CurrentTime + TTL,
    Tokens = get(tokens),
    NewTokens = maps:put(TokenId, Expiry, Tokens),
    put(tokens, NewTokens).

-spec authentication_manager_renew(TokenId :: unicode:unicode_binary(), CurrentTime :: integer()) -> any().
authentication_manager_renew(TokenId, CurrentTime) ->
    Tokens = get(tokens),
    case maps:find(TokenId, Tokens) of
        {ok, Expiry} when Expiry > CurrentTime ->
            TTL = get(ttl),
            NewExpiry = CurrentTime + TTL,
            NewTokens = maps:put(TokenId, NewExpiry, Tokens),
            put(tokens, NewTokens);
        _ -> ok
    end.

-spec authentication_manager_count_unexpired_tokens(CurrentTime :: integer()) -> integer().
authentication_manager_count_unexpired_tokens(CurrentTime) ->
    Tokens = get(tokens),
    maps:fold(
        fun(_Key, Expiry, Acc) ->
            if Expiry > CurrentTime -> Acc + 1; true -> Acc end
        end,
        0,
        Tokens).
```

## Elixir

```elixir
defmodule AuthenticationManager do
  @spec init_(time_to_live :: integer) :: any
  def init_(time_to_live) do
    Process.put(:auth_manager_state, %{ttl: time_to_live, tokens: %{}})
    nil
  end

  @spec generate(token_id :: String.t(), current_time :: integer) :: any
  def generate(token_id, current_time) do
    state = Process.get(:auth_manager_state)
    new_tokens = Map.put(state.tokens, token_id, current_time + state.ttl)
    Process.put(:auth_manager_state, %{state | tokens: new_tokens})
    nil
  end

  @spec renew(token_id :: String.t(), current_time :: integer) :: any
  def renew(token_id, current_time) do
    state = Process.get(:auth_manager_state)

    case Map.fetch(state.tokens, token_id) do
      {:ok, expiry} when expiry > current_time ->
        new_tokens = Map.put(state.tokens, token_id, current_time + state.ttl)
        Process.put(:auth_manager_state, %{state | tokens: new_tokens})
      _ -> :ok
    end

    nil
  end

  @spec count_unexpired_tokens(current_time :: integer) :: integer
  def count_unexpired_tokens(current_time) do
    state = Process.get(:auth_manager_state)
    Enum.count(state.tokens, fn {_id, exp} -> exp > current_time end)
  end
end
```
