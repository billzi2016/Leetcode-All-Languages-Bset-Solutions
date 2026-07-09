# 1472. Design Browser History

## Cpp

```cpp
#include <string>
#include <vector>
using namespace std;

class BrowserHistory {
public:
    BrowserHistory(string homepage) {
        history.push_back(move(homepage));
        cur = 0;
    }
    
    void visit(string url) {
        if (cur + 1 < (int)history.size()) {
            history.resize(cur + 1);
        }
        history.push_back(move(url));
        ++cur;
    }
    
    string back(int steps) {
        cur = max(0, cur - steps);
        return history[cur];
    }
    
    string forward(int steps) {
        cur = min((int)history.size() - 1, cur + steps);
        return history[cur];
    }

private:
    vector<string> history;
    int cur;
};
```

## Java

```java
class BrowserHistory {
    private java.util.ArrayList<String> history;
    private int curr;

    public BrowserHistory(String homepage) {
        history = new java.util.ArrayList<>();
        history.add(homepage);
        curr = 0;
    }

    public void visit(String url) {
        // Discard forward history
        if (curr + 1 < history.size()) {
            history.subList(curr + 1, history.size()).clear();
        }
        history.add(url);
        curr++;
    }

    public String back(int steps) {
        curr = Math.max(0, curr - steps);
        return history.get(curr);
    }

    public String forward(int steps) {
        curr = Math.min(history.size() - 1, curr + steps);
        return history.get(curr);
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */
```

## Python

```python
class BrowserHistory(object):
    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.curr = 0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        # discard forward history
        self.history = self.history[:self.curr + 1]
        self.history.append(url)
        self.curr += 1

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.curr = min(len(self.history) - 1, self.curr + steps)
        return self.history[self.curr]
```

## Python3

```python
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        # discard forward history
        self.history = self.history[:self.curr + 1]
        self.history.append(url)
        self.curr += 1

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(len(self.history) - 1, self.curr + steps)
        return self.history[self.curr]
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    char **history;
    int capacity;
    int cur;   // current index
    int last;  // last valid index in history
} BrowserHistory;

static char *copy_str(const char *s) {
    size_t len = strlen(s);
    char *p = (char *)malloc(len + 1);
    if (p) memcpy(p, s, len + 1);
    return p;
}

BrowserHistory* browserHistoryCreate(char* homepage) {
    BrowserHistory *obj = (BrowserHistory *)malloc(sizeof(BrowserHistory));
    obj->capacity = 6000; // sufficient for constraints
    obj->history = (char **)malloc(obj->capacity * sizeof(char *));
    obj->cur = 0;
    obj->last = 0;
    obj->history[0] = copy_str(homepage);
    return obj;
}

void browserHistoryVisit(BrowserHistory* obj, char* url) {
    // free forward history
    for (int i = obj->cur + 1; i <= obj->last; ++i) {
        free(obj->history[i]);
        obj->history[i] = NULL;
    }
    // move to next position
    if (obj->cur + 1 >= obj->capacity) {
        int newCap = obj->capacity * 2;
        char **newHist = (char **)realloc(obj->history, newCap * sizeof(char *));
        if (!newHist) return; // allocation failure, should not happen in LeetCode
        obj->history = newHist;
        obj->capacity = newCap;
    }
    obj->cur++;
    obj->history[obj->cur] = copy_str(url);
    obj->last = obj->cur;
}

char* browserHistoryBack(BrowserHistory* obj, int steps) {
    if (steps > obj->cur) steps = obj->cur;
    obj->cur -= steps;
    return obj->history[obj->cur];
}

char* browserHistoryForward(BrowserHistory* obj, int steps) {
    int forwardAvail = obj->last - obj->cur;
    if (steps > forwardAvail) steps = forwardAvail;
    obj->cur += steps;
    return obj->history[obj->cur];
}

void browserHistoryFree(BrowserHistory* obj) {
    for (int i = 0; i <= obj->last; ++i) {
        free(obj->history[i]);
    }
    free(obj->history);
    free(obj);
}
```

## Csharp

```csharp
public class BrowserHistory
{
    private readonly List<string> _history;
    private int _curr;

    public BrowserHistory(string homepage)
    {
        _history = new List<string> { homepage };
        _curr = 0;
    }

    public void Visit(string url)
    {
        // Discard forward history
        if (_curr < _history.Count - 1)
        {
            _history.RemoveRange(_curr + 1, _history.Count - (_curr + 1));
        }
        _history.Add(url);
        _curr++;
    }

    public string Back(int steps)
    {
        _curr = Math.Max(0, _curr - steps);
        return _history[_curr];
    }

    public string Forward(int steps)
    {
        _curr = Math.Min(_history.Count - 1, _curr + steps);
        return _history[_curr];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} homepage
 */
var BrowserHistory = function(homepage) {
    this.history = [homepage];
    this.curr = 0;
};

/** 
 * @param {string} url
 * @return {void}
 */
BrowserHistory.prototype.visit = function(url) {
    // discard forward history
    this.history = this.history.slice(0, this.curr + 1);
    this.history.push(url);
    this.curr++;
};

/** 
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.back = function(steps) {
    this.curr = Math.max(0, this.curr - steps);
    return this.history[this.curr];
};

/** 
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.forward = function(steps) {
    this.curr = Math.min(this.history.length - 1, this.curr + steps);
    return this.history[this.curr];
};
```

## Typescript

```typescript
class BrowserHistory {
    private history: string[];
    private cur: number;

    constructor(homepage: string) {
        this.history = [homepage];
        this.cur = 0;
    }

    visit(url: string): void {
        // Discard forward history
        this.history = this.history.slice(0, this.cur + 1);
        this.history.push(url);
        this.cur++;
    }

    back(steps: number): string {
        this.cur = Math.max(0, this.cur - steps);
        return this.history[this.cur];
    }

    forward(steps: number): string {
        this.cur = Math.min(this.history.length - 1, this.cur + steps);
        return this.history[this.cur];
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * var obj = new BrowserHistory(homepage)
 * obj.visit(url)
 * var param_2 = obj.back(steps)
 * var param_3 = obj.forward(steps)
 */
```

## Php

```php
class BrowserHistory {
    /**
     * @var array
     */
    private $history = [];

    /**
     * @var int
     */
    private $curr = 0;

    /**
     * @param String $homepage
     */
    function __construct($homepage) {
        $this->history[] = $homepage;
        $this->curr = 0;
    }

    /**
     * @param String $url
     * @return NULL
     */
    function visit($url) {
        // Remove forward history
        array_splice($this->history, $this->curr + 1);
        // Add new page and move cursor
        $this->history[] = $url;
        $this->curr++;
    }

    /**
     * @param Integer $steps
     * @return String
     */
    function back($steps) {
        $steps = min($steps, $this->curr);
        $this->curr -= $steps;
        return $this->history[$this->curr];
    }

    /**
     * @param Integer $steps
     * @return String
     */
    function forward($steps) {
        $maxForward = count($this->history) - 1 - $this->curr;
        $steps = min($steps, $maxForward);
        $this->curr += $steps;
        return $this->history[$this->curr];
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * $obj = new BrowserHistory($homepage);
 * $obj->visit($url);
 * $ret_2 = $obj->back($steps);
 * $ret_3 = $obj->forward($steps);
 */
```

## Swift

```swift
class BrowserHistory {
    private var history: [String]
    private var currentIndex: Int

    init(_ homepage: String) {
        self.history = [homepage]
        self.currentIndex = 0
    }

    func visit(_ url: String) {
        if currentIndex < history.count - 1 {
            history.removeLast(history.count - currentIndex - 1)
        }
        history.append(url)
        currentIndex += 1
    }

    func back(_ steps: Int) -> String {
        let move = min(steps, currentIndex)
        currentIndex -= move
        return history[currentIndex]
    }

    func forward(_ steps: Int) -> String {
        let move = min(steps, history.count - 1 - currentIndex)
        currentIndex += move
        return history[currentIndex]
    }
}
```

## Kotlin

```kotlin
class BrowserHistory(homepage: String) {
    private val history = mutableListOf<String>()
    private var currentIndex = 0

    init {
        history.add(homepage)
    }

    fun visit(url: String) {
        // Discard forward history
        if (currentIndex < history.size - 1) {
            history.subList(currentIndex + 1, history.size).clear()
        }
        history.add(url)
        currentIndex = history.lastIndex
    }

    fun back(steps: Int): String {
        currentIndex = kotlin.math.max(0, currentIndex - steps)
        return history[currentIndex]
    }

    fun forward(steps: Int): String {
        currentIndex = kotlin.math.min(history.lastIndex, currentIndex + steps)
        return history[currentIndex]
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * var obj = BrowserHistory(homepage)
 * obj.visit(url)
 * var param_2 = obj.back(steps)
 * var param_3 = obj.forward(steps)
 */
```

## Dart

```dart
import 'dart:math';

class BrowserHistory {
  List<String> _history;
  int _curr;

  BrowserHistory(String homepage) {
    _history = [homepage];
    _curr = 0;
  }

  void visit(String url) {
    if (_curr < _history.length - 1) {
      _history.removeRange(_curr + 1, _history.length);
    }
    _history.add(url);
    _curr++;
  }

  String back(int steps) {
    _curr = max(0, _curr - steps);
    return _history[_curr];
  }

  String forward(int steps) {
    _curr = min(_history.length - 1, _curr + steps);
    return _history[_curr];
  }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = BrowserHistory(homepage);
 * obj.visit(url);
 * String param2 = obj.back(steps);
 * String param3 = obj.forward(steps);
 */
```

## Golang

```go
type BrowserHistory struct {
	history []string
	curr    int
}

func Constructor(homepage string) BrowserHistory {
	return BrowserHistory{
		history: []string{homepage},
		curr:    0,
	}
}

func (this *BrowserHistory) Visit(url string) {
	// Discard forward history
	this.history = this.history[:this.curr+1]
	this.history = append(this.history, url)
	this.curr = len(this.history) - 1
}

func (this *BrowserHistory) Back(steps int) string {
	if steps > this.curr {
		this.curr = 0
	} else {
		this.curr -= steps
	}
	return this.history[this.curr]
}

func (this *BrowserHistory) Forward(steps int) string {
	maxForward := len(this.history) - 1 - this.curr
	if steps > maxForward {
		this.curr = len(this.history) - 1
	} else {
		this.curr += steps
	}
	return this.history[this.curr]
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * obj := Constructor(homepage);
 * obj.Visit(url);
 * param_2 := obj.Back(steps);
 * param_3 := obj.Forward(steps);
 */
```

## Ruby

```ruby
class BrowserHistory
  def initialize(homepage)
    @history = [homepage]
    @curr = 0
  end

  def visit(url)
    while @history.size > @curr + 1
      @history.pop
    end
    @history << url
    @curr += 1
  end

  def back(steps)
    @curr -= steps
    @curr = 0 if @curr < 0
    @history[@curr]
  end

  def forward(steps)
    @curr += steps
    max_idx = @history.size - 1
    @curr = max_idx if @curr > max_idx
    @history[@curr]
  end
end
```

## Scala

```scala
import scala.collection.mutable.ArrayBuffer

class BrowserHistory(_homepage: String) {
  private val history = ArrayBuffer[String](_homepage)
  private var curr = 0

  def visit(url: String): Unit = {
    if (curr < history.length - 1) {
      history.trimEnd(history.length - curr - 1)
    }
    history += url
    curr = history.length - 1
  }

  def back(steps: Int): String = {
    val move = math.min(steps, curr)
    curr -= move
    history(curr)
  }

  def forward(steps: Int): String = {
    val maxForward = history.length - 1 - curr
    val move = math.min(steps, maxForward)
    curr += move
    history(curr)
  }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * val obj = new BrowserHistory(homepage)
 * obj.visit(url)
 * val param_2 = obj.back(steps)
 * val param_3 = obj.forward(steps)
 */
```

## Rust

```rust
struct BrowserHistory {
    history: Vec<String>,
    cur: usize,
}

impl BrowserHistory {
    fn new(homepage: String) -> Self {
        BrowserHistory {
            history: vec![homepage],
            cur: 0,
        }
    }

    fn visit(&mut self, url: String) {
        // Discard forward history
        self.history.truncate(self.cur + 1);
        self.history.push(url);
        self.cur = self.history.len() - 1;
    }

    fn back(&mut self, steps: i32) -> String {
        let step = std::cmp::min(steps as usize, self.cur);
        self.cur -= step;
        self.history[self.cur].clone()
    }

    fn forward(&mut self, steps: i32) -> String {
        let max_forward = self.history.len() - 1 - self.cur;
        let step = std::cmp::min(steps as usize, max_forward);
        self.cur += step;
        self.history[self.cur].clone()
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * let mut obj = BrowserHistory::new(homepage);
 * obj.visit(url);
 * let ret_2: String = obj.back(steps);
 * let ret_3: String = obj.forward(steps);
 */
```

## Racket

```racket
(define browser-history%
  (class object%
    (super-new)
    
    ; homepage : string?
    (init-field
      homepage)
    
    ; internal state
    (define current homepage)
    (define back-stack '())
    (define forward-stack '())
    
    ; visit : string? -> void?
    (define/public (visit url)
      (set! back-stack (cons current back-stack))
      (set! current url)
      (set! forward-stack '()))
    
    ; back : exact-integer? -> string?
    (define/public (back steps)
      (let loop ((steps steps))
        (if (or (= steps 0) (null? back-stack))
            current
            (begin
              (set! forward-stack (cons current forward-stack))
              (set! current (car back-stack))
              (set! back-stack (cdr back-stack))
              (loop (- steps 1))))))
    
    ; forward : exact-integer? -> string?
    (define/public (forward steps)
      (let loop ((steps steps))
        (if (or (= steps 0) (null? forward-stack))
            current
            (begin
              (set! back-stack (cons current back-stack))
              (set! current (car forward-stack))
              (set! forward-stack (cdr forward-stack))
              (loop (- steps 1))))))
    ))
```

## Erlang

```erlang
-module(browser_history).
-export([browser_history_init_/1,
         browser_history_visit/1,
         browser_history_back/1,
         browser_history_forward/1]).

-define(STATE_KEY, ?MODULE_state).

-spec browser_history_init_(Homepage :: unicode:unicode_binary()) -> any().
browser_history_init_(Homepage) ->
    put(?STATE_KEY, {[], Homepage, []}),
    ok.

-spec browser_history_visit(Url :: unicode:unicode_binary()) -> any().
browser_history_visit(Url) ->
    case get(?STATE_KEY) of
        undefined -> ok; % should not happen
        {Back, _Cur, _Fwd} ->
            put(?STATE_KEY, {[Url | Back] -- [Url], Url, []}),
            ok
    end.

-spec browser_history_back(Steps :: integer()) -> unicode:unicode_binary().
browser_history_back(Steps) when Steps >= 0 ->
    case get(?STATE_KEY) of
        undefined -> <<>>;
        State = {Back, Cur, Fwd} ->
            {NewState, NewCur} = back_move(State, Steps),
            put(?STATE_KEY, NewState),
            NewCur
    end.

-spec browser_history_forward(Steps :: integer()) -> unicode:unicode_binary().
browser_history_forward(Steps) when Steps >= 0 ->
    case get(?STATE_KEY) of
        undefined -> <<>>;
        State = {Back, Cur, Fwd} ->
            {NewState, NewCur} = forward_move(State, Steps),
            put(?STATE_KEY, NewState),
            NewCur
    end.

%% internal helpers

back_move({[], Cur, _Fwd}=State, _Steps) ->
    {State, Cur};
back_move({[Prev|RestBack], Cur, Fwd}, Steps) when Steps > 0 ->
    back_move({RestBack, Prev, [Cur|Fwd]}, Steps - 1);
back_move(State, _Steps) ->
    %% No more history to go back
    {State, element(2, State)}.

forward_move({_Back, Cur, []}=State, _Steps) ->
    {State, Cur};
forward_move({Back, Cur, [Next|RestFwd]}, Steps) when Steps > 0 ->
    forward_move({[Cur|Back], Next, RestFwd}, Steps - 1);
forward_move(State, _Steps) ->
    {State, element(2, State)}.
```

## Elixir

```elixir
defmodule BrowserHistory do
  @spec init_(homepage :: String.t()) :: any()
  def init_(homepage) do
    state = %{history: [homepage], cur: 0}
    Process.put(:browser_state, state)
    nil
  end

  @spec visit(url :: String.t()) :: any()
  def visit(url) do
    %{history: hist, cur: cur} = Process.get(:browser_state)
    # keep elements up to current index, then add new url
    new_history = Enum.slice(hist, 0..cur) ++ [url]
    new_state = %{history: new_history, cur: length(new_history) - 1}
    Process.put(:browser_state, new_state)
    nil
  end

  @spec back(steps :: integer()) :: String.t()
  def back(steps) do
    %{history: hist, cur: cur} = Process.get(:browser_state)
    new_cur = max(cur - steps, 0)
    new_state = %{history: hist, cur: new_cur}
    Process.put(:browser_state, new_state)
    Enum.at(hist, new_cur)
  end

  @spec forward(steps :: integer()) :: String.t()
  def forward(steps) do
    %{history: hist, cur: cur} = Process.get(:browser_state)
    max_idx = length(hist) - 1
    new_cur = min(cur + steps, max_idx)
    new_state = %{history: hist, cur: new_cur}
    Process.put(:browser_state, new_state)
    Enum.at(hist, new_cur)
  end
end
```
