# Day 1

## ```print()``` function

This is the function used to print an output in the terminal.

```python
print()  # Print a void line
```

## `str` Strings

To define a string is used single or double quotes. (We can use single quotes to strings not only characters)

``` python
print("Hello world!")
print('Hello world!')
```

When within a string we want to include quotes there are three principal ways to do it. 

``` python
# Define the string with a diferent type of quotes
print("He said 'hi'")
print('He said "hi"')
# Using backslash
print("He said \"hi\"")  # This is not recommended because it's difficult to read
```

Print more than one string in a line (concatenate)

``` python
print("Hello" + "world!")  # Output: Helloworld!
print("Hello", "world!")  # Output: Hello world!
```

It's better use the second way when the strings are saved in variables.

## Indentation

In Python it's important indentation, this is the way that we define what is inside a function, class, etc.

``` python
	print("Hello world!")  # This will cause an error
```

## ```input()``` function

This is the function used to input information by terminal.

```python
input()  # Wait for input
```

This function can receive a string as a parameter. This will be the text that will be printed to ask for the input. If there is no a string it simply will wait for the input.

``` python
input("How are you doing? ")  # Output: How are you doing? _______
```

It's possible to combine both functions like this:

```python
print("Hello " + input("What's your name? ") + "!")
# Output:
# What's your name? _____
# What's your name? Sebastian
# Hello Sebastian!
```

In this case, the `input()` function is inside the `print()` function. As it's not defined the input, this part of code will be executed first and then will be printed all the line.

## `#`Comments

To create a comment in Python:

```python
# This a line comment
print()  # This is a inline comment
```

It's recommended that after `#` there is a space and then the comment content. If it's a inline comment, before make the comment there should be at least two spaces.

## `len()` function

To get the length of a string is used the `len()` function. It will return the number of characters in the string.

```python
print("Hello is a str of", len("Hello"), "char(s)")  # Output: Hello is a str of 5 char(s)
```

```python
print("Your name has", len(input("What's your name? ")), "char(s)")
# Output:
# What's your name? ____
# What's your name? Sebastián
# Your name is a str of 9 char(s)
```

## Variables

In Python, to define a variable it's not necessary to specify the type of the variable.

```python
name = "Sebastián"
age = 18
```

In Python, a variable can be any type of variable. So, if previously a variable was type `int`, we can now convert it to another type, for example `str`

```python
a = 123
a = "Hello"
a = 3.14
a = ["1", "2", "3"]
```

## `type()` of a variable

To get the type of a variable is used the `type()` function. It will return the type of the variable.

```python
a = 123
print(type(a))  # Output: <class 'int'>
a = "Hello"
print(type(a))  # Output: <class 'str'>
```

