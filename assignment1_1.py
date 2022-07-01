
1) what is python and its features?

>>python is dynamic,high level,free open source and interpreted programming
    language.it supports object oriented programming as well as procedural
    oriented programming

2) Differentiate between lists and tuples.
    The major difference is that a list is mutable, but a tuple is immutable. Examples:

>>> mylist=[1,3,3]
>>> mylist[1]=2
>>> mytuple=(1,3,3)
>>> mytuple[1]=

3)  How long can an identifier be in Python?
    According to the official Python documentation, an identifier can be of any length. However, PEP 8 suggests that you should limit all lines to a maximum of 79 characters. Also, PEP 20 says ‘readability counts’. So, a very long identifier will violate PEP-8 and PEP-20.

Apart from that, there are certain rules we must follow to name one:

It can only begin with an underscore or a character from A-Z or a-z.
The rest of it can contain anything from the following: A-Z/a-z/_/0-9.
Python is case-sensitive, as we discussed in the previous question.
Keywords cannot be used as identifiers. Python has the following keywords:
and	def	False	import	not	True
as	del	finally	in	or	try
assert	elif	for	is	pass	while
break	else	from	lambda	print	with
class	except	global	None	raise	yield
continue	exec	if	nonlocal	return

4)  What is slicing?
    Slicing is a technique that allows us to retrieve only a part of a list, tuple, or string. For this, we use the slicing operator [].
>>> (1,2,3,4,5)[2:4]
(3, 4)

>>> [7,6,8,5,9][2:]
[8, 5, 9]

>>> 'Hello'[:-1]
‘Hell’

5)  How would you declare a comment in Python?
    Unlike languages like C++, Python does not have multiline comments. All it has is octothorpe (#). Anything following a hash is considered a comment, and the interpreter ignores it.

>>> #line 1 of comment
>>> #line 2 of comment

6)  How do you insert an object at a given index in Python?
    Let’s build a list first.
>>> a=[1,2,4]
Now, we use the method insert. The first argument is the index at which to insert, the second is the value to insert.

>>> a.insert(2,3)
>>> a
[1, 2, 3, 4]

7)  And how do you reverse a list?
Using the reverse() method.

>>> a.reverse()
>>> a
[4, 3, 2, 1]
You can also do it via slicing from right to left:

>>> a[::-1]
>>> a
[1, 2, 3, 4]
This gives us the original list because we already reversed it once. However, this does not modify the original list to reverse it

8) How would you define a block in Python?
For any kind of statements, we possibly need to define a block of code under them. 
However, Python does not support curly braces. This means we must end such statements 
with colons and then indent the blocks under those with the same amount.
>>> if 3>1:
print("Hello")
print("Goodbye")
Hello
Goodbye

9)  Why do we need break and continue in Python?
    Both break and continue are statements that control flow in Python loops.   
    break stops the current loop from executing further and transfers the control to the next
    block.continue jumps to the next iteration of the loop without exhausting it.

10) What is Python good for?

Python is a jack of many trades, check out Applications of Python to find out more.
Meanwhile, we’ll say we can use it for:
Web and Internet Development
Desktop GUI
Scientific and Numeric Applications
Software Development Applications
Applications in Education
Applications in Business
Database Access
Network Programming
Games, 3D Graphics
Other Python Applications

11) Can you name ten built-in functions in Python and explain each in brief?
Ten Built-in Functions, you say? Okay, here you go.
complex()- Creates a complex number.

>>> complex(3.5,4)
(3.5+4j)
eval()- Parses a string as an expression.

>>> eval('print(max(22,22.0)-min(2,3))')
20

filter()- Filters in items for which the condition is true.

>>> list(filter(lambda x:x%2==0,[1,2,0,False]))
[2, 0, False]

format()- Lets us format a string.

>>> print("a={0} but b={1}".format(a,b))
a=2 but b=3

hash()- Returns the hash value of an object.
>>> hash(3.7)
644245917
hex()- Converts an integer to a hexadecimal.
>>> hex(14)
‘0xe’

input()- Reads and returns a line of string.
>>> input('Enter a number')
Enter a number7
‘7’

len()- Returns the length of an object.
>>> len('Ayushi')
6
locals()- Returns a dictionary of the current local symbol table.
>>> locals()
{‘__name__’: ‘__main__’, ‘__doc__’: None, ‘__package__’: None, ‘__loader__’: <class ‘_frozen_importlib.BuiltinImporter’>, ‘__spec__’: None, ‘__annotations__’: {}, ‘__builtins__’: <module ‘builtins’ (built-in)>, ‘a’: 2, ‘b’: 3}
open()- Opens a file.
>>> file=open('tabs.txt')

12) What will the following code output?

>>> word=’abcdefghij’
>>> word[:3]+word[3:]
The output is ‘abcdefghij’. The first slice gives us ‘abc’, the next gives us ‘defghij’

13)  How will you convert a list into a string?
We will use the join() method for this.
>>> nums=['one','two','three','four','five','six','seven']
>>> s=' '.join(nums)
>>> s
‘one two three four five six seven’

14) How will you remove a duplicate element from a list?
We can turn it into a set to do that.
>>> list=[1,2,1,3,4,2]
>>> set(list)
{1, 2, 3, 4}

15) What is a function?
When we want to execute a sequence of statements, we can give it a name. Let’s define a function to take two numbers and return the greater number.
>>> def greater(a,b):
return a is a>b else b
>>> greater(3,3.5)

16)  How do you calculate the length of a string?
This is simple. We call the function len() on the string we want to calculate the length of.
>>> len('Ayushi Sharma')
13

17) Write code to print everything in the string except the spaces.

>>> for i in s:
if i==' ': continue
print(i,end='')

18) What is a control flow statement?
A Python program usually starts to execute from the first line. From there, it moves through each statement just once and as soon as it’s done with the last statement, 
it transactions the program. However, sometimes, we may want to take a more twisted path through the code. 
Control flow statements let us disturb the normal execution flow of a program and bend it to our will.

19)  How do we execute Python?
Python files first compile to bytecode. Then, the host executes them.
Revise the concept of Python Compiler

20)   How would you work with numbers other than those in the decimal number system?
With Python, it is possible to type numbers in binary, octal, and hexadecimal.
Binary numbers are made of 0 and 1. To type in binary, we use the prefix 0b or 0B.
>>> int(0b1010) 
10
To convert a number into its binary form, we use bin().
>>> bin(0xf)
‘0b1111’
Octal numbers may have digits from 0 to 7. We use the prefix 0o or 0O.
>>> oct(8)
‘0o10’
Hexadecimal numbers may have digits from 0 to 15. We use the prefix 0x or 0X.
>>> hex(16)
‘0x10’
>>> hex(15)
‘0xf’

DataFlair’s latest article on Python Numbers with Examples



