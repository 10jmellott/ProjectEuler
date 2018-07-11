<h1>Fibonacci's Algorithms</h1>

<h2>Intrinsic Functions</h2>

```python
def trial_division(n)
```

<div markdown="1" style="margin-left: 30px;">

[Trial Division](https://en.wikipedia.org/wiki/Trial_division)

Arguments:
    n (Integer): Number to factor


</div>

<div markdown="1" style="margin-left: 30px;">

Returns *Array*: List of factors of n

</div>

------

```python
def factors_to_dictionary(factors)
```

<div markdown="1" style="margin-left: 30px;">

Transforms a list of factors into a dictionary


</div>

<div markdown="1" style="margin-left: 30px;">

Args:

</div>

<div markdown="1" style="margin-left: 30px;">

* **factors** *list*: List of factors

</div>

<div markdown="1" style="margin-left: 30px;">

Returns *dict*: Dictionary of factors to count

</div>

------

```python
def fib_basic(n)
```

<div markdown="1" style="margin-left: 30px;">

Simple fibonacci sequence implementation

Arguments:
    n (Integer): Index of the fibonacci number


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

Implemented as recursion. Use fib_loop for large n.

Arguments:
    n (Integer): Index of the fibonacci number


</div>

<div markdown="1" style="margin-left: 30px;">

Returns *Integer*: Value of the fibonacci sequence at the provided index

</div>

------

```python
def fib_memo(n, memoization)
```

<div markdown="1" style="margin-left: 30px;">

Recursive fibonacci sequence implementation utilizing memoization


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

------

```python
def fib_loop(n)
```

<div markdown="1" style="margin-left: 30px;">

Optimized fibonacci sequence implementation utilizing memoization.

Implemented as a loop. Use for large n.

Arguments:
    n (Integer): Index of the fibonacci number


</div>

<div markdown="1" style="margin-left: 30px;">

Returns *Integer*: Value of the fibonacci sequence at the provided index

</div>

------

```python
def fib_memo_loop(n, memo)
```

<div markdown="1" style="margin-left: 30px;">

Looping recursive fibonacci sequence implementation utilizing memoization.

Use for large n.


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