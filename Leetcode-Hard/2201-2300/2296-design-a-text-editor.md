# 2296. Design a Text Editor

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class TextEditor {
    deque<char> left, right;
    
    string getLeftString() {
        string res;
        int cnt = 0;
        for (auto it = left.rbegin(); it != left.rend() && cnt < 10; ++it, ++cnt) {
            res.push_back(*it);
        }
        reverse(res.begin(), res.end());
        return res;
    }
public:
    TextEditor() {}
    
    void addText(string text) {
        for (char c : text) left.push_back(c);
    }
    
    int deleteText(int k) {
        int cnt = 0;
        while (cnt < k && !left.empty()) {
            left.pop_back();
            ++cnt;
        }
        return cnt;
    }
    
    string cursorLeft(int k) {
        int move = min(k, (int)left.size());
        for (int i = 0; i < move; ++i) {
            char c = left.back(); left.pop_back();
            right.push_front(c);
        }
        return getLeftString();
    }
    
    string cursorRight(int k) {
        int move = min(k, (int)right.size());
        for (int i = 0; i < move; ++i) {
            char c = right.front(); right.pop_front();
            left.push_back(c);
        }
        return getLeftString();
    }
};

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor* obj = new TextEditor();
 * obj->addText(text);
 * int param_2 = obj->deleteText(k);
 * string param_3 = obj->cursorLeft(k);
 * string param_4 = obj->cursorRight(k);
 */
```

## Java

```java
class TextEditor {
    private final java.util.ArrayDeque<Character> left = new java.util.ArrayDeque<>();
    private final java.util.ArrayDeque<Character> right = new java.util.ArrayDeque<>();

    public TextEditor() { }

    public void addText(String text) {
        for (char c : text.toCharArray()) {
            left.addLast(c);
        }
    }

    public int deleteText(int k) {
        int deleted = 0;
        while (deleted < k && !left.isEmpty()) {
            left.removeLast();
            deleted++;
        }
        return deleted;
    }

    public String cursorLeft(int k) {
        int moved = 0;
        while (moved < k && !left.isEmpty()) {
            right.addFirst(left.removeLast());
            moved++;
        }
        return getLeftString();
    }

    public String cursorRight(int k) {
        int moved = 0;
        while (moved < k && !right.isEmpty()) {
            left.addLast(right.removeFirst());
            moved++;
        }
        return getLeftString();
    }

    private String getLeftString() {
        StringBuilder sb = new StringBuilder();
        java.util.Iterator<Character> it = left.descendingIterator();
        int cnt = 0;
        while (it.hasNext() && cnt < 10) {
            sb.append(it.next());
            cnt++;
        }
        return sb.reverse().toString();
    }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor obj = new TextEditor();
 * obj.addText(text);
 * int param_2 = obj.deleteText(k);
 * String param_3 = obj.cursorLeft(k);
 * String param_4 = obj.cursorRight(k);
 */
```

## Python

```python
class TextEditor(object):
    def __init__(self):
        self.left = []   # characters to the left of cursor
        self.right = []  # characters to the right of cursor (stack, top at end)

    def addText(self, text):
        """
        :type text: str
        :rtype: None
        """
        for ch in text:
            self.left.append(ch)

    def deleteText(self, k):
        """
        :type k: int
        :rtype: int
        """
        cnt = 0
        while cnt < k and self.left:
            self.left.pop()
            cnt += 1
        return cnt

    def cursorLeft(self, k):
        """
        :type k: int
        :rtype: str
        """
        move = min(k, len(self.left))
        for _ in range(move):
            self.right.append(self.left.pop())
        # return last up to 10 chars left of cursor
        start = max(0, len(self.left) - 10)
        return ''.join(self.left[start:])

    def cursorRight(self, k):
        """
        :type k: int
        :rtype: str
        """
        move = min(k, len(self.right))
        for _ in range(move):
            self.left.append(self.right.pop())
        start = max(0, len(self.left) - 10)
        return ''.join(self.left[start:])
```

## Python3

```python
class TextEditor:
    def __init__(self):
        self.left = []   # characters to the left of cursor
        self.right = []  # characters to the right of cursor (nearest at end)

    def addText(self, text: str) -> None:
        for ch in text:
            self.left.append(ch)

    def deleteText(self, k: int) -> int:
        cnt = 0
        while cnt < k and self.left:
            self.left.pop()
            cnt += 1
        return cnt

    def cursorLeft(self, k: int) -> str:
        move = min(k, len(self.left))
        for _ in range(move):
            self.right.append(self.left.pop())
        # return up to last 10 chars left of cursor
        start = max(0, len(self.left) - 10)
        return ''.join(self.left[start:])

    def cursorRight(self, k: int) -> str:
        move = min(k, len(self.right))
        for _ in range(move):
            self.left.append(self.right.pop())
        start = max(0, len(self.left) - 10)
        return ''.join(self.left[start:])
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *left;
    int leftSize;
    int leftCap;
    char *right;
    int rightSize;
    int rightCap;
} TextEditor;

static void ensureLeftCapacity(TextEditor *obj) {
    if (obj->leftSize >= obj->leftCap) {
        int newCap = obj->leftCap ? obj->leftCap * 2 : 64;
        char *newArr = (char *)realloc(obj->left, newCap);
        obj->left = newArr;
        obj->leftCap = newCap;
    }
}
static void ensureRightCapacity(TextEditor *obj) {
    if (obj->rightSize >= obj->rightCap) {
        int newCap = obj->rightCap ? obj->rightCap * 2 : 64;
        char *newArr = (char *)realloc(obj->right, newCap);
        obj->right = newArr;
        obj->rightCap = newCap;
    }
}
static void pushLeft(TextEditor *obj, char c) {
    ensureLeftCapacity(obj);
    obj->left[obj->leftSize++] = c;
}
static char popLeft(TextEditor *obj) {
    return obj->left[--obj->leftSize];
}
static void pushRight(TextEditor *obj, char c) {
    ensureRightCapacity(obj);
    obj->right[obj->rightSize++] = c;
}
static char popRight(TextEditor *obj) {
    return obj->right[--obj->rightSize];
}

/** Initialize your data structure here. */
TextEditor* textEditorCreate() {
    TextEditor *obj = (TextEditor *)malloc(sizeof(TextEditor));
    obj->left = NULL;  obj->leftSize = 0; obj->leftCap = 0;
    obj->right = NULL; obj->rightSize = 0; obj->rightCap = 0;
    return obj;
}

/** Append text to the editor. */
void textEditorAddText(TextEditor* obj, char* text) {
    for (int i = 0; text[i] != '\0'; ++i) {
        pushLeft(obj, text[i]);
    }
}

/** Delete k characters to the left of the cursor. Returns the number of characters actually deleted. */
int textEditorDeleteText(TextEditor* obj, int k) {
    int cnt = 0;
    while (cnt < k && obj->leftSize > 0) {
        popLeft(obj);
        ++cnt;
    }
    return cnt;
}

/** Move cursor left by k positions and return the last min(10, len_left) characters to the left of the cursor. */
char* textEditorCursorLeft(TextEditor* obj, int k) {
    int move = k < obj->leftSize ? k : obj->leftSize;
    for (int i = 0; i < move; ++i) {
        char c = popLeft(obj);
        pushRight(obj, c);
    }
    int len = obj->leftSize < 10 ? obj->leftSize : 10;
    char *res = (char *)malloc(len + 1);
    int start = obj->leftSize - len;
    for (int i = 0; i < len; ++i) {
        res[i] = obj->left[start + i];
    }
    res[len] = '\0';
    return res;
}

/** Move cursor right by k positions and return the last min(10, len_left) characters to the left of the cursor. */
char* textEditorCursorRight(TextEditor* obj, int k) {
    int move = k < obj->rightSize ? k : obj->rightSize;
    for (int i = 0; i < move; ++i) {
        char c = popRight(obj);
        pushLeft(obj, c);
    }
    int len = obj->leftSize < 10 ? obj->leftSize : 10;
    char *res = (char *)malloc(len + 1);
    int start = obj->leftSize - len;
    for (int i = 0; i < len; ++i) {
        res[i] = obj->left[start + i];
    }
    res[len] = '\0';
    return res;
}

/** Free all allocated memory. */
void textEditorFree(TextEditor* obj) {
    if (!obj) return;
    free(obj->left);
    free(obj->right);
    free(obj);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Text;

public class TextEditor
{
    private Stack<char> left = new Stack<char>();
    private Stack<char> right = new Stack<char>();

    public TextEditor()
    {
    }

    public void AddText(string text)
    {
        foreach (char c in text)
            left.Push(c);
    }

    public int DeleteText(int k)
    {
        int deleted = 0;
        while (deleted < k && left.Count > 0)
        {
            left.Pop();
            deleted++;
        }
        return deleted;
    }

    public string CursorLeft(int k)
    {
        int move = Math.Min(k, left.Count);
        for (int i = 0; i < move; i++)
            right.Push(left.Pop());
        return GetLeftString();
    }

    public string CursorRight(int k)
    {
        int move = Math.Min(k, right.Count);
        for (int i = 0; i < move; i++)
            left.Push(right.Pop());
        return GetLeftString();
    }

    private string GetLeftString()
    {
        int cnt = Math.Min(10, left.Count);
        if (cnt == 0) return "";
        char[] arr = left.ToArray(); // top to bottom
        StringBuilder sb = new StringBuilder(cnt);
        for (int i = cnt - 1; i >= 0; i--)
            sb.Append(arr[i]);
        return sb.ToString();
    }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor obj = new TextEditor();
 * obj.AddText(text);
 * int param_2 = obj.DeleteText(k);
 * string param_3 = obj.CursorLeft(k);
 * string param_4 = obj.CursorRight(k);
 */
```

## Javascript

```javascript
var TextEditor = function() {
    this.left = [];   // characters to the left of cursor
    this.right = [];  // characters to the right of cursor
};

/** 
 * @param {string} text
 * @return {void}
 */
TextEditor.prototype.addText = function(text) {
    for (let ch of text) {
        this.left.push(ch);
    }
};

/** 
 * @param {number} k
 * @return {number}
 */
TextEditor.prototype.deleteText = function(k) {
    let deleted = 0;
    while (k > 0 && this.left.length > 0) {
        this.left.pop();
        k--;
        deleted++;
    }
    return deleted;
};

/** 
 * @param {number} k
 * @return {string}
 */
TextEditor.prototype.cursorLeft = function(k) {
    while (k > 0 && this.left.length > 0) {
        this.right.push(this.left.pop());
        k--;
    }
    const start = Math.max(0, this.left.length - 10);
    return this.left.slice(start).join('');
};

/** 
 * @param {number} k
 * @return {string}
 */
TextEditor.prototype.cursorRight = function(k) {
    while (k > 0 && this.right.length > 0) {
        this.left.push(this.right.pop());
        k--;
    }
    const start = Math.max(0, this.left.length - 10);
    return this.left.slice(start).join('');
};
```

## Typescript

```typescript
class TextEditor {
    private left: string[];
    private right: string[];

    constructor() {
        this.left = [];
        this.right = [];
    }

    addText(text: string): void {
        for (const ch of text) {
            this.left.push(ch);
        }
    }

    deleteText(k: number): number {
        let cnt = 0;
        while (cnt < k && this.left.length > 0) {
            this.left.pop();
            cnt++;
        }
        return cnt;
    }

    cursorLeft(k: number): string {
        const moves = Math.min(k, this.left.length);
        for (let i = 0; i < moves; i++) {
            const ch = this.left.pop()!;
            this.right.push(ch);
        }
        return this.getLast10();
    }

    cursorRight(k: number): string {
        const moves = Math.min(k, this.right.length);
        for (let i = 0; i < moves; i++) {
            const ch = this.right.pop()!;
            this.left.push(ch);
        }
        return this.getLast10();
    }

    private getLast10(): string {
        const start = Math.max(0, this.left.length - 10);
        return this.left.slice(start).join('');
    }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * var obj = new TextEditor()
 * obj.addText(text)
 * var param_2 = obj.deleteText(k)
 * var param_3 = obj.cursorLeft(k)
 * var param_4 = obj.cursorRight(k)
 */
```

## Php

```php
class TextEditor {
    private $left = [];
    private $right = [];

    function __construct() {
        // Initialize empty editor with cursor at start.
    }

    /**
     * @param String $text
     * @return NULL
     */
    function addText($text) {
        $n = strlen($text);
        for ($i = 0; $i < $n; $i++) {
            $this->left[] = $text[$i];
        }
    }

    /**
     * @param Integer $k
     * @return Integer
     */
    function deleteText($k) {
        $deleted = 0;
        while ($deleted < $k && !empty($this->left)) {
            array_pop($this->left);
            $deleted++;
        }
        return $deleted;
    }

    /**
     * @param Integer $k
     * @return String
     */
    function cursorLeft($k) {
        $move = min($k, count($this->left));
        for ($i = 0; $i < $move; $i++) {
            $ch = array_pop($this->left);
            $this->right[] = $ch;
        }
        $len = min(10, count($this->left));
        if ($len == 0) return "";
        return implode('', array_slice($this->left, -$len));
    }

    /**
     * @param Integer $k
     * @return String
     */
    function cursorRight($k) {
        $move = min($k, count($this->right));
        for ($i = 0; $i < $move; $i++) {
            $ch = array_pop($this->right);
            $this->left[] = $ch;
        }
        $len = min(10, count($this->left));
        if ($len == 0) return "";
        return implode('', array_slice($this->left, -$len));
    }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * $obj = new TextEditor();
 * $obj->addText($text);
 * $ret_2 = $obj->deleteText($k);
 * $ret_3 = $obj->cursorLeft($k);
 * $ret_4 = $obj->cursorRight($k);
 */
```

## Swift

```swift
class TextEditor {
    private var left: [Character] = []
    private var right: [Character] = []

    init() {}

    func addText(_ text: String) {
        for ch in text {
            left.append(ch)
        }
    }

    func deleteText(_ k: Int) -> Int {
        let del = min(k, left.count)
        if del > 0 {
            left.removeLast(del)
        }
        return del
    }

    func cursorLeft(_ k: Int) -> String {
        var move = min(k, left.count)
        while move > 0 {
            right.append(left.removeLast())
            move -= 1
        }
        let start = max(0, left.count - 10)
        let slice = left[start..<left.count]
        return String(slice)
    }

    func cursorRight(_ k: Int) -> String {
        var move = min(k, right.count)
        while move > 0 {
            left.append(right.removeLast())
            move -= 1
        }
        let start = max(0, left.count - 10)
        let slice = left[start..<left.count]
        return String(slice)
    }
}
```

## Kotlin

```kotlin
class TextEditor() {

    private val left = java.util.ArrayDeque<Char>()
    private val right = java.util.ArrayDeque<Char>()

    fun addText(text: String) {
        for (c in text) {
            left.addLast(c)
        }
    }

    fun deleteText(k: Int): Int {
        var cnt = 0
        var remaining = k
        while (remaining > 0 && left.isNotEmpty()) {
            left.removeLast()
            cnt++
            remaining--
        }
        return cnt
    }

    private fun getLeftString(): String {
        val sb = StringBuilder()
        var cnt = 0
        val it = left.descendingIterator()
        while (it.hasNext() && cnt < 10) {
            sb.append(it.next())
            cnt++
        }
        return sb.reverse().toString()
    }

    fun cursorLeft(k: Int): String {
        var remaining = k
        while (remaining > 0 && left.isNotEmpty()) {
            val c = left.removeLast()
            right.addFirst(c)
            remaining--
        }
        return getLeftString()
    }

    fun cursorRight(k: Int): String {
        var remaining = k
        while (remaining > 0 && right.isNotEmpty()) {
            val c = right.removeFirst()
            left.addLast(c)
            remaining--
        }
        return getLeftString()
    }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * var obj = TextEditor()
 * obj.addText(text)
 * var param_2 = obj.deleteText(k)
 * var param_3 = obj.cursorLeft(k)
 * var param_4 = obj.cursorRight(k)
 */
```

## Dart

```dart
class TextEditor {
  List<String> _left = [];
  List<String> _right = [];

  TextEditor() {}

  void addText(String text) {
    for (int i = 0; i < text.length; i++) {
      _left.add(text[i]);
    }
  }

  int deleteText(int k) {
    int deleted = 0;
    while (deleted < k && _left.isNotEmpty) {
      _left.removeLast();
      deleted++;
    }
    return deleted;
  }

  String cursorLeft(int k) {
    int moves = k;
    while (moves > 0 && _left.isNotEmpty) {
      _right.add(_left.removeLast());
      moves--;
    }
    int start = _left.length - 10;
    if (start < 0) start = 0;
    return _left.sublist(start).join();
  }

  String cursorRight(int k) {
    int moves = k;
    while (moves > 0 && _right.isNotEmpty) {
      _left.add(_right.removeLast());
      moves--;
    }
    int start = _left.length - 10;
    if (start < 0) start = 0;
    return _left.sublist(start).join();
  }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor obj = TextEditor();
 * obj.addText(text);
 * int param2 = obj.deleteText(k);
 * String param3 = obj.cursorLeft(k);
 * String param4 = obj.cursorRight(k);
 */
```

## Golang

```go
type TextEditor struct {
	left  []byte
	right []byte
}

func Constructor() TextEditor {
	return TextEditor{
		left:  make([]byte, 0),
		right: make([]byte, 0),
	}
}

func (this *TextEditor) AddText(text string) {
	for i := 0; i < len(text); i++ {
		this.left = append(this.left, text[i])
	}
}

func (this *TextEditor) DeleteText(k int) int {
	deleted := 0
	for k > 0 && len(this.left) > 0 {
		this.left = this.left[:len(this.left)-1]
		k--
		deleted++
	}
	return deleted
}

func (this *TextEditor) CursorLeft(k int) string {
	move := k
	if move > len(this.left) {
		move = len(this.left)
	}
	for i := 0; i < move; i++ {
		ch := this.left[len(this.left)-1]
		this.left = this.left[:len(this.left)-1]
		this.right = append(this.right, ch)
	}
	return lastTen(this.left)
}

func (this *TextEditor) CursorRight(k int) string {
	move := k
	if move > len(this.right) {
		move = len(this.right)
	}
	for i := 0; i < move; i++ {
		ch := this.right[len(this.right)-1]
		this.right = this.right[:len(this.right)-1]
		this.left = append(this.left, ch)
	}
	return lastTen(this.left)
}

func lastTen(arr []byte) string {
	n := len(arr)
	start := n - 10
	if start < 0 {
		start = 0
	}
	return string(arr[start:])
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddText(text);
 * param_2 := obj.DeleteText(k);
 * param_3 := obj.CursorLeft(k);
 * param_4 := obj.CursorRight(k);
 */
```

## Ruby

```ruby
class TextEditor
  def initialize()
    @left = []   # characters to the left of the cursor
    @right = []  # characters to the right of the cursor
  end

=begin
    :type text: String
    :rtype: Void
=end
  def add_text(text)
    text.each_char { |ch| @left << ch }
  end

=begin
    :type k: Integer
    :rtype: Integer
=end
  def delete_text(k)
    cnt = 0
    while cnt < k && !@left.empty?
      @left.pop
      cnt += 1
    end
    cnt
  end

=begin
    :type k: Integer
    :rtype: String
=end
  def cursor_left(k)
    move = [k, @left.size].min
    move.times { @right << @left.pop }
    @left.last(10).join
  end

=begin
    :type k: Integer
    :rtype: String
=end
  def cursor_right(k)
    move = [k, @right.size].min
    move.times { @left << @right.pop }
    @left.last(10).join
  end
end
```

## Scala

```scala
class TextEditor() {
  private val left = new scala.collection.mutable.ArrayDeque[Char]()
  private val right = new scala.collection.mutable.ArrayDeque[Char]()

  def addText(text: String): Unit = {
    for (c <- text) left.append(c)
  }

  def deleteText(k: Int): Int = {
    var cnt = 0
    var remaining = k
    while (remaining > 0 && left.nonEmpty) {
      left.removeLast()
      cnt += 1
      remaining -= 1
    }
    cnt
  }

  private def getLeftString(): String = {
    val sz = left.length
    val start = math.max(0, sz - 10)
    val sb = new java.lang.StringBuilder()
    var i = start
    while (i < sz) {
      sb.append(left(i))
      i += 1
    }
    sb.toString
  }

  def cursorLeft(k: Int): String = {
    var remaining = k
    while (remaining > 0 && left.nonEmpty) {
      val c = left.removeLast()
      right.prepend(c)
      remaining -= 1
    }
    getLeftString()
  }

  def cursorRight(k: Int): String = {
    var remaining = k
    while (remaining > 0 && right.nonEmpty) {
      val c = right.removeFirst()
      left.append(c)
      remaining -= 1
    }
    getLeftString()
  }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * val obj = new TextEditor()
 * obj.addText(text)
 * val param_2 = obj.deleteText(k)
 * val param_3 = obj.cursorLeft(k)
 * val param_4 = obj.cursorRight(k)
 */
```

## Rust

```rust
struct TextEditor {
    left: Vec<char>,
    right: Vec<char>,
}

impl TextEditor {
    fn new() -> Self {
        Self {
            left: Vec::new(),
            right: Vec::new(),
        }
    }

    fn add_text(&mut self, text: String) {
        for ch in text.chars() {
            self.left.push(ch);
        }
    }

    fn delete_text(&mut self, k: i32) -> i32 {
        let mut cnt = 0;
        while cnt < k && !self.left.is_empty() {
            self.left.pop();
            cnt += 1;
        }
        cnt
    }

    fn cursor_left(&mut self, k: i32) -> String {
        let mut moved = 0;
        while moved < k && !self.left.is_empty() {
            if let Some(ch) = self.left.pop() {
                self.right.push(ch);
            }
            moved += 1;
        }
        let len = self.left.len();
        let start = if len >= 10 { len - 10 } else { 0 };
        self.left[start..].iter().collect()
    }

    fn cursor_right(&mut self, k: i32) -> String {
        let mut moved = 0;
        while moved < k && !self.right.is_empty() {
            if let Some(ch) = self.right.pop() {
                self.left.push(ch);
            }
            moved += 1;
        }
        let len = self.left.len();
        let start = if len >= 10 { len - 10 } else { 0 };
        self.left[start..].iter().collect()
    }
}

/**
 * Your TextEditor object will be instantiated and called as such:
 * let obj = TextEditor::new();
 * obj.add_text(text);
 * let ret_2: i32 = obj.delete_text(k);
 * let ret_3: String = obj.cursor_left(k);
 * let ret_4: String = obj.cursor_right(k);
 */
```

## Racket

```racket
#lang racket
(require racket/list)

(define text-editor%
  (class object%
    (super-new)
    
    (define left '())
    (define right '())
    
    ; add-text : string? -> void?
    (define/public (add-text txt)
      (for ([i (in-range (string-length txt))])
        (set! left (cons (string-ref txt i) left))))
    
    ; delete-text : exact-integer? -> exact-integer?
    (define/public (delete-text k)
      (let loop ((cnt 0) (rem k))
        (if (or (= rem 0) (null? left))
            cnt
            (begin
              (set! left (cdr left))
              (loop (+ cnt 1) (- rem 1))))))
    
    ; helper to get suffix string of left up to 10 chars
    (define (left-suffix)
      (let* ([taken (take left 10)]
             [rev (reverse taken)])
        (list->string rev)))
    
    ; cursor-left : exact-integer? -> string?
    (define/public (cursor-left k)
      (let loop ((rem k))
        (if (or (= rem 0) (null? left))
            (void)
            (begin
              (set! right (cons (car left) right))
              (set! left (cdr left))
              (loop (- rem 1)))))
      (left-suffix))
    
    ; cursor-right : exact-integer? -> string?
    (define/public (cursor-right k)
      (let loop ((rem k))
        (if (or (= rem 0) (null? right))
            (void)
            (begin
              (set! left (cons (car right) left))
              (set! right (cdr right))
              (loop (- rem 1)))))
      (left-suffix))
    ))
```

## Erlang

```erlang
-spec text_editor_init_() -> any().
text_editor_init_() ->
    put(left, []),
    put(right, []).

-spec text_editor_add_text(Text :: unicode:unicode_binary()) -> any().
text_editor_add_text(Text) ->
    Chars = unicode:characters_to_list(Text),
    Left0 = get(left),
    NewLeft = lists:foldl(fun(C, Acc) -> [C | Acc] end, Left0, Chars),
    put(left, NewLeft).

-spec text_editor_delete_text(K :: integer()) -> integer().
text_editor_delete_text(K) ->
    Left0 = get(left),
    {Deleted, Rest} = delete_k(Left0, K, 0),
    put(left, Rest),
    Deleted.

-spec text_editor_cursor_left(K :: integer()) -> unicode:unicode_binary().
text_editor_cursor_left(K) ->
    move_left(K),
    last_ten().

-spec text_editor_cursor_right(K :: integer()) -> unicode:unicode_binary().
text_editor_cursor_right(K) ->
    move_right(K),
    last_ten().

%% internal helpers
delete_k([], _K, Count) ->
    {Count, []};
delete_k(List, 0, Count) ->
    {Count, List};
delete_k([_C | Rest], K, Count) when K > 0 ->
    delete_k(Rest, K - 1, Count + 1).

move_left(0) -> ok;
move_left(K) when K > 0 ->
    case get(left) of
        [] -> ok;
        [C | Rest] ->
            put(left, Rest),
            Right = get(right),
            put(right, [C | Right]),
            move_left(K - 1)
    end.

move_right(0) -> ok;
move_right(K) when K > 0 ->
    case get(right) of
        [] -> ok;
        [C | Rest] ->
            put(right, Rest),
            Left = get(left),
            put(left, [C | Left]),
            move_right(K - 1)
    end.

last_ten() ->
    Left = get(left),
    Take = lists:sublist(Left, 10),
    Rev = lists:reverse(Take),
    unicode:characters_to_binary(Rev).
```

## Elixir

```elixir
defmodule TextEditor do
  @spec init_() :: any
  def init_() do
    :erlang.put(:left, [])
    :erlang.put(:right, [])
    :ok
  end

  @spec add_text(text :: String.t) :: any
  def add_text(text) do
    left = :erlang.get(:left)
    # prepend characters so that the stack is reversed (head = nearest to cursor)
    new_left =
      text
      |> String.to_charlist()
      |> Enum.reduce(left, fn c, acc -> [c | acc] end)

    :erlang.put(:left, new_left)
    :ok
  end

  @spec delete_text(k :: integer) :: integer
  def delete_text(k) do
    left = :erlang.get(:left)
    {deleted, rest} = Enum.split(left, k)
    :erlang.put(:left, rest)
    length(deleted)
  end

  @spec cursor_left(k :: integer) :: String.t
  def cursor_left(k) do
    left = :erlang.get(:left)
    right = :erlang.get(:right)

    move = Enum.take(left, k)
    moved_len = length(move)
    new_left = Enum.drop(left, moved_len)
    # reverse to maintain correct order when moving to the right side
    new_right = Enum.reverse(move) ++ right

    :erlang.put(:left, new_left)
    :erlang.put(:right, new_right)

    get_last_ten(new_left)
  end

  @spec cursor_right(k :: integer) :: String.t
  def cursor_right(k) do
    left = :erlang.get(:left)
    right = :erlang.get(:right)

    move = Enum.take(right, k)
    moved_len = length(move)
    new_right = Enum.drop(right, moved_len)

    # push moved characters onto the left stack preserving order
    new_left =
      Enum.reduce(move, left, fn c, acc -> [c | acc] end)

    :erlang.put(:left, new_left)
    :erlang.put(:right, new_right)

    get_last_ten(new_left)
  end

  defp get_last_ten(left_stack) do
    len = min(10, length(left_stack))
    left_stack
    |> Enum.take(len)
    |> Enum.reverse()
    |> List.to_string()
  end
end
```
