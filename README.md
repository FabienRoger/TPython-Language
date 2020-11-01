# TPython-Language

## What this is

"deftree" is a new way of writing a recursing function. A code can be written in the TPython language, which is Python, but with this structure supported.

## The Syntax
```
deftree name_of_the_function(inputs_of_the_function):
	code_block_1()
	if condition:
		code_block_2()
		> x1
		> x2
	else:
		code_block_3()
		return y
merge ylist:
	code_block_4()
	return y
```
Please look at Example 1 and 2 to see exactly how this syntax works.

## How to translate a program that uses the deftree structure into a python file

- Rename the file you want to translate tree_code.tpy and copy converter.py next to this file.
- Run converter.py.\
The translated code will be found in code.py.

## The Key Idea

Contrary to a standard recursive function, the deftree function works in two steps.\
First, the recursive tree is built. Each node either creates its children with the data provided after the ">", or it is a leaf node, in which case it prepares itself to return the value after "return". This is determined by the first part of the function. After the end of this phase, every node is either a leaf node with a value which it is prepared to return, or a non-leaf node.\
Second, the recursive tree is collapsed : every non-leaf node executes the second part of the function, after "merge". The "ylist" is the list of values which the node's children return.

## Example 1: the merge code algorithm

Here, we suppose that "split" and "merge" are two functions which have already been defined.
```
deftree mergesort(x):
	if len(x) <= 1:
		return x
	y,z = split(x)
	> y
	> z
merge couple:
	a,b = couple
	return merge(a,b)
```
What it translates to in python using converter.py :
```
def mergesort(x):
	
	couple = []
	if len(x) <= 1:
		return x
	y,z = split(x)
	couple.append(mergesort(y))
	couple.append(mergesort(z))
		
	a,b = couple
	return merge(a,b)
```
## Motivation

The example clearly illustrates that writing a function using "deftree" is not that different or more difficult than writing it using standard recursive functions. However, I believe it can be easier to write and to understand some recursive functions when this code structure is used.\
Explaining to someone not used to recursive functions how merge sort works can be tricky. Some beginners might even struggle to understand how a function can be used before it has been completely defined. The deftree syntax eliminates this problem by providing a clear idea of what the merge sort algorithm is doing. Indeed, if one wants to explain how the algorithm works and how to run it by hand, it is much easier to cut the process in two steps.

Here is how I would explain how merge sort work to a beginner :\
First, split the list in two parts of similar size, then split each resulting list in two, and so one, until each list part has a length of one. Doing that, you should keep track how the cutting was made using a tree (a drawing clearly helps).\
Second, start with the bottom of the tree, merge again and again every two list with the same parent with the "merge" procedure (which is very easy to understand*) until you only have one list left : the sorted list.

Note how much easier it is to describe things that way rather than speaking of "using the method, which I haven't fully described yet, on both list" as it is usually taught.

This way of building functions can also be used to write functions which can be easily written using a for loop, thereby providing a new way (and sometimes a simpler way) of understanding some algorithm, as it is the case in the following example.

## Example 2: Dichotomic Search
```
deftree dichotomic_search(l,i=0,j=-1): 
	if j == -1:j = len(l)-1
	
	if abs(i-j) == 0:
		return i
	if l[i] > x or l[j] < x: #-1 means that x isn't in this part of the list
		return -1
		
	k = (i+j)//2
	> l,i,k
	> l,k,j
	
merge c:
	a,b = c
	return max(a,b) #if a or b is equal to -1 (but not both), this return the other value, the index at which x has been found
```

What it translates to in python using converter.py :
```
def dichotomic_search(l,i=0,j=-1):
	c = []
	if j == -1:j = len(l)-1
	
	if abs(i-j) == 0:
		return i
	if l[i] > x or l[j] < x: #-1 means that x isn't in this part of the list
		return -1
		
	k = (i+j)//2
	c.append(dichotomic_search(l,i,k))
	c.append(dichotomic_search(l,k,j))
	
	a,b = c
	return max(a,b) #if a or b is equal to -1 (but not both), this return the other value, the index at which x has been found
```
## Remark 1: Space taken in memory

Splitting the process in two is using more memory than needed : when using usual recursive function, the computer doesn't need to store the whole "recursive tree" ni memory. Note than in the way I convert the deftree function into a python function, I don't ask python to execute the execution of the function in two steps, so the program doesn't run in this issue. I "lie" to the user of the program by claiming that the process is really done in two steps when it is in fact not the case : in Example 1, check the python translation of the deftree function. Note that the "recursive tree" built to compute mergesort(y) is forgotten when computing mergesort(z), and that it is not the case that I only run the first part of the code on every node, then the second one on every non-leaf node. However, the result is exactly the same as if the process was done in two distinct steps.

## Remark 2: Flaws in the way I built the translator

1. It only supports tabs ('\t') and not triple or quadruple space
2. It does not support nested deftree
3. It would be better if one could select all the folders containing .tpy file and ask the program to convert them to .py files.
4. In most cases, it doesn't warn the user if deftree wasn't used correctly.
5. Using a variable named "ylist" (or the name used after "merge") inside the first part of the deftree function will cause the resulting program to be incorrect.

Feel free to modify converter.py to correct these flaws.
