<h1>Fibonacci's Algorithms</h1>

<h2>Intrinsic Functions</h2>

```python
def trial_division(n)
```

<div markdown="1" style="margin-left: 30px;">

[Trial Division](https://en.wikipedia.org/wiki/Trial_division)

</div>

<div markdown="1" style="margin-left: 30px;">

Returns *Array*: List of factors of n

</div>

------

```python
def fib_basic(n)
```

<div markdown="1" style="margin-left: 30px;">

Simple fibonacci sequence implementation

</div>

<div markdown="1" style="margin-left: 30px;">

Returns *Integer*: Value of the fibonacci sequence at the provided index

</div>

------

```python
def fib(n)
```

<div markdown="1" style="margin-left: 30px;">

Optimized fibonacci sequence implementation utilizing memoization

</div>

<div markdown="1" style="margin-left: 30px;">

Returns *Integer*: Value of the fibonacci sequence at the provided index

</div>

------

```python
def _fib(n, memoization)
```

<div markdown="1" style="margin-left: 30px;">

[Internal] Recursive fibonacci sequence implementation utilizing memoization

</div>

<div markdown="1" style="margin-left: 30px;">

Args:

</div>

<div markdown="1" style="margin-left: 30px;">

* **n** *Integer*: Index of the fibonacci number
* **memoization** *Dictionary*: Non-Null dictionary with prior memoized values

</div>

<div markdown="1" style="margin-left: 30px;">

Returns *Integer*: Value of the fibonacci sequence at the provided index

</div>