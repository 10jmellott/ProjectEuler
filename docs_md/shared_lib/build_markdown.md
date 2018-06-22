<h1>Python Docstring to Markdown</h1>

<h2>Summary</h2>

<div markdown="1" style="margin-left: 30px;">

> Attempts to parse a python document and resolve a markdown file with unique formatting.  
> Assumes Google's Docstring formatting.

</div>



<h2>Classes</h2>

<div markdown="1" style="margin-left: 30px;">

```python
class DocumentDocstring
```

<div markdown="1" style="margin-left: 30px;">

<h3>Constructors</h3>

```python
DocumentDocstring(expression)
```

<h3>Methods</h3>

```python
def title()
```

```python
def body()
```

</div>

------

```python
class GoogleDocstringArgument
```

<div markdown="1" style="margin-left: 30px;">

<h3>Constructors</h3>

```python
GoogleDocstringArgument(docstring)
```

<h3>Methods</h3>

```python
def name()
```

```python
def arg_type()
```

```python
def description()
```

</div>

------

```python
class GoogleDocstringReturn
```

<div markdown="1" style="margin-left: 30px;">

<h3>Constructors</h3>

```python
GoogleDocstringReturn(docstring)
```

<h3>Methods</h3>

```python
def return_type()
```

```python
def description()
```

</div>

------

```python
class GoogleFunctionDocstring
```

<div markdown="1" style="margin-left: 30px;">

<h3>Constructors</h3>

```python
GoogleFunctionDocstring(function_def)
```

<h3>Methods</h3>

```python
def is_valid()
```

```python
def name()
```

```python
def short_description()
```

```python
def arguments()
```

```python
def return_description()
```

</div>

------

```python
class GoogleClassDocstring
```

<div markdown="1" style="margin-left: 30px;">

<h3>Constructors</h3>

```python
GoogleClassDocstring(class_def)
```

<h3>Methods</h3>

```python
def name()
```

```python
def constructors()
```

```python
def methods()
```

</div>


</div>



<h2>Intrinsic Functions</h2>
```python
def parse_file(filename)
```

------

```python
def cli()
```
