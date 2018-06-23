<h1>Python Docstring to Markdown</h1>

<h2>Summary</h2>

> Attempts to parse a python document and resolve a markdown file with unique formatting.  
> Assumes Google's Docstring formatting.

<h2>Classes</h2>

```python
class HtmlMarkdownBuilder
```

<div markdown="1" style="margin-left: 30px;">

<h4>Constructors</h4>

</div>

<div markdown="1" style="margin-left: 30px;">

```python
HtmlMarkdownBuilder()
```

</div>

<div markdown="1" style="margin-left: 30px;">

<h4>Methods</h4>

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def append(markdown, div)
```

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def append_to_block(block)
```

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def complete_block()
```

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def indent()
```

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def deindent()
```

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def build()
```

</div>

------

```python
class DocumentDocstring
```

<div markdown="1" style="margin-left: 30px;">

<h4>Constructors</h4>

</div>

<div markdown="1" style="margin-left: 30px;">

```python
DocumentDocstring(expression)
```

</div>

<div markdown="1" style="margin-left: 30px;">

<h4>Methods</h4>

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def title()
```

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def body()
```

</div>

------

```python
class GoogleDocstringArgument
```

<div markdown="1" style="margin-left: 30px;">

<h4>Constructors</h4>

</div>

<div markdown="1" style="margin-left: 30px;">

```python
GoogleDocstringArgument(docstring)
```

</div>

<div markdown="1" style="margin-left: 30px;">

<h4>Methods</h4>

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def name()
```

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def arg_type()
```

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def description()
```

</div>

------

```python
class GoogleDocstringReturn
```

<div markdown="1" style="margin-left: 30px;">

<h4>Constructors</h4>

</div>

<div markdown="1" style="margin-left: 30px;">

```python
GoogleDocstringReturn(docstring)
```

</div>

<div markdown="1" style="margin-left: 30px;">

<h4>Methods</h4>

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def return_type()
```

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def description()
```

</div>

------

```python
class GoogleFunctionDocstring
```

<div markdown="1" style="margin-left: 30px;">

<h4>Constructors</h4>

</div>

<div markdown="1" style="margin-left: 30px;">

```python
GoogleFunctionDocstring(function_def)
```

</div>

<div markdown="1" style="margin-left: 30px;">

<h4>Methods</h4>

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def is_valid()
```

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def name()
```

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def short_description()
```

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def arguments()
```

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def return_description()
```

</div>

------

```python
class GoogleClassDocstring
```

<div markdown="1" style="margin-left: 30px;">

<h4>Constructors</h4>

</div>

<div markdown="1" style="margin-left: 30px;">

```python
GoogleClassDocstring(class_def)
```

</div>

<div markdown="1" style="margin-left: 30px;">

<h4>Methods</h4>

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def name()
```

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def constructors()
```

</div>

<div markdown="1" style="margin-left: 30px;">

```python
def methods()
```

</div>

<h2>Intrinsic Functions</h2>

```python
def parse_file(filename)
```

------

```python
def cli()
```