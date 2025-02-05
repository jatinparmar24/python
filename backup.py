# topics

# 1=keyward=35
# softkward=4
# special symbol=32

# 2=punctation

# 3=identifiers         (line = 186)

# 4=operators            (line = 235)

# a = arithmatic operators===   [    +,-,*,/,%,//=floor,**=power  ]  ==arithmatic operators return value
# b = comparasion operators====    (== , != , > ,< , <=, >=)  ==  return boolean
# c = assingment operators === [= , += , -= , *= , /= , %= , //= , **= ]  == assingment operators return value 
                                                                      
# d = logical operators === [and , or , not]   // not makes true into false     and false into true
# e = identity operators  ===  [is , is not]   is = compare memory address,refrence of object
# f = membership operators   ====  [in , not in]  == checks if present or not 
# g = bitwise operators     ====  [& , | , ~ , ^ , >> , <<]  [and , or , not ,x-or , right-shift , left-sift]

# number system = collection of digit---
#  1a= Binary=(0,1)  == length or base =2
#  1b= Octal=(0,1,2,3,4,5,6,7)  ==  length or base =8
#  1c=Decimal=(0,1,2,3,4,5,6,7,8,9)  ==  length or base =10
#  1d= Hexadecimal=([0,1,2,3,4,5,6,7,8,9]+[A,B,C,D,E,F]||[a,b,c,d,e,f]) =  length or base =16

# 5=literals   [The value asigned to a constant variable is called literals]           
# literals types===  [numeric, string, boolen, list, tuple, dict , (set,frozenset)]  set and frozenset are not used in web development
# and these types are called data types

# 5A=numeric ===
# a=integer==>2,4,5,7,etc
# b=float==3.4,1.2,5.4,etc
# c=complex== x+yj             x is real number  and y is imaginary number

# 5B =string  ==    collection of characters     
# represented by==
# ''=single quote     ====     used for single line string   
#    ""=double quote   ====    used for single line string
#   '''=triple quote   ==== used for multiline string

# 5C = boolean  == True or False

# 5D =   list      ===   collection of objects
# represent by [] with comma(,)seperated objects

# 5E =   Tuple      ===   collection of objects
# represent by () with comma(,)seperated objects
# ordered collection , indexing supported  , immutable in nature , slicing supported

# 5F = dict   === collection of 'key':'value' pair      === 'key':'value' = 1 object
# represent by {} with comma(,)seperated objects

# 5G = set ===  collection of unique object
# represent by {} with comma(,)seperated objects
# duplicate value not allowed
# order not fixed \\ provide random order

# 5H = frozenset  === collection of unique object
# represent by {} with comma(,)seperated objects
# duplicate value not allowed
# order not fixed \\ provide random order


# 6 (                                         (line = 62)

#  pythom is not a call by value language    (not)

# but it is a call by refrence language     (yes)
x=10
y=10
print(id(x))
print(id(y))
# x and y hold the memory address of 10 thats why it is call by reference

# python object type =
# mutable = (address or object can be changed) = list , set , dict

# list
l1=[1,2,3,'jat']
l2=[1,2,3,'jat']
print(id(l1))
print(id(l2))

# dist
d1={'name':'jatin','age':23}
d2={'name':'jatin','age':23}
print(id(d1))
print(id(d2))

# set
s1={1,4,6,'jatin'}
s2={1,4,6,'jatin'}
print(id(s1))
print(id(s2))


# immutable = (address or object can not be changed) =  int , str , tuple , frozenset
# int
x=10
y=10
print(id(x))
print(id(y))

# str
x='jatin'
y='jatin'
print(id(x))
print(id(y))

# tuple
x=(1,2,3,'jat')
y=(1,2,3,'jat')
print(id(x))
print(id(y))


# exception case  == frozenset = it's nature is immutable but works as mutable 

s1=frozenset({1,4,6,'jatin'})
s2=frozenset({1,4,6,'jatin'})
print(id(s1))
print(id(s2))

# Thus python is a call by object refrence language   (yes)

# and if object refrence language option is not available then we can say it is a call by refrence language

# )



# 7 = indexing                                                 
# pyhton support positive indexing = points
# a = start from 0
# b = read direction = left to right
# c = write direction =  left to right
# d = stop point = end -1
# e =  use to find first object

# pyhton support negetive indexing = points
# a = start from -1
# b = read direction = left to right or right to left
# c =  write direction =  left to right
#  d = stop point = end +1
# e = use to find last object

# indexing syntax
# a = collection.index('obj')
# b = collection.index('obj' , start , stop)               internal 

# indexing works on ordered collection = like == string , list , tuple
# unordered collection = set and frozenset    here indexing not work

# 8 = slicing

# slicing works on ordered collection = like == string , list , tuple
# syntax   =    collecton[start : stop : step/jump/direction]
#  (stop-1) for +ve indexing
#  (stop+1) for -ve indexing

# some rules:-
# a = check direction of step   = a1==if direction is empty then it is by default one(1) == +ve direction
# a2 == +ve no.  == (+ve direction)
# a3 == -ve no.  == (-ve direction)

# b = check start and stop direction
# c = if both directions are matched then we get output otherwise we get empty output



# 9 = data-types   ===   


# 9a = numeric === (integer ,float , complex)

# 9b = string === (type,max,min id , etc)   
#  and methods ===  lower()  ,upper() ,title() ,capitalize() ,swapcase() ,find() ,index() ,count() , ( join() , split() ) = imp methods

# 9c = list  ===  collection of object =
#  a= homogeneous (same data type)        b = hetrogenous (diff data type)

# ordered collection  ,  indexing supported  , slicing supported  , mutable in nature , represented by [square bracket] and object is (,) seperated
# mutable in nature=
#  x=[10]
# y=[10]
# print(id(x))
# print(id(y))
# diffrent memory addresses

# inbuilt function of python for list====
# min(),max(),sum()    =  to used that function we have to make list homogeneous(means same data)
# len(),id(),type()

# methods of list ===
# append() = add one object at last position
# extend() = add multiple object at last position
# sort() = arrange data in ascending order
# insert() = add one object at required position
# remove() = remove one object at required position
# pop() = remove one object from last position
# reverse() = arrange list in reverse order
# clear() = remove all object from list                         and we get an empty list in result
# count() = frequency
# index() = object position
# copy() = create another object with same content
# l1=[22,23]
# x=print(id(l1.copy()))     ans = 2521131361152
# print(id(x))               ans = 140713179185648


# extra method of list for decending
l1=[22,23,2,5,3]
l1.sort(reverse=True)
print(l1)
# ans  [23, 22, 5, 3, 2]


# 9d tuple      ===   collection of objects
# represent by () with comma(,)seperated objects
# ordered collection , indexing supported  , immutable in nature , slicing supported 
# fast as compared to list beacuse takes less space or memeory   and also immutable
# fix memeory allocation

# import sys

# x=10
# print(sys.getsizeof(x))   = 28

# y=''
# print(sys.getsizeof(y))   = 41

# z="jatin"
# print(sys.getsizeof(z))   = 46

# a=()            tuple     = 40
# print(sys.getsizeof(a))

# b=[]            list      = 56
# print(sys.getsizeof(b))


#  9e = dict 

# collection of key value pair.
# represent by {} with comma(,)seperated objects
# indexing and slicing not supported
# squential collection but not ordered
# key must be unique          and value  may be duplicate
# mutbale in nature
# syntax   d1={ 'key':''value','key':''value','key':''value',}
#                ^  1-element    ^  2-element   ^ 3-element

# in-built function of list
# max() , min()   on the basis of largest alphabet
# len() , type()  , id()

# methods for dict
# clear() , copy() , fromkeys() , get() , items() , key() , pop() , popitem() , setdefault() , update() , values()


# 9f = set

# collection of unique elements
# unordered colletion  ,  indexing or slicing not supported      , mutable in nature
# represent by {} with comma(,)seperated objects

# inbuilt functions
# max() , min() , type() , id() , len() , sum()

# methods for set
# copy() , clear() , add() , update() , pop() , remove() , discard()

# special mathematical operations for set
# union() = target all element
# intersection = target common element
# difference = return new set   minus the element of B from A
# difference_update = change permamnet which we target
# symmetric_difference = leaves common element
# symmetric_difference_update = 
# isdisjoint() 
# issubset() 
#  issubsuperset()


# 9g = frozenset

# collection of unique elements
# unordered colletion  ,  indexing or slicing not supported      , immutable in nature

# method  = only copy()
# inbuilt methods =  max() , min() , len()   (and some more)

# mathematical operations =   union() , intersection() , difference() , symmetric_difference() , isdisjoint() , issubset() , issubsuperset()


# 10 = control statement
# python is a squential + conditional statement
# 
# 10a = conditional statement = if , if-else , if-elif , if-elif-else
# 10b =  iterative statement  = while , for
# while   =  1 = initialization      2 = condition check   = (a) If True = execute block of code  (b) Increase/Decrease (c) If condition False = break/terminate loop
# syntax  =  initialization(i)  ,  while(condition check) , block of code  , i=i+1 / i=i-1

# for    =  
# syntax  =  for i in collection 
#          collections are = list , string , tuple , dict

# 10c =            statement    = continue , break , pass








# range(start,stop,step)          step(from where u have to go)   
# it return collection

x=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
x=range(-1,-11)
print(list(x))
# empty list

x=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
x=range(-1,-11,-1)
print(list(x))
# ans [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

# even number
n=50
x=range(2,51,2)
print(list(x))
# ans [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]


# even number in runtime
n=int(input("Enter number"))
x=range(2,n+1,2)
print(list(x))


# odd number in runtime
n=int(input("Enter number"))
x=range(1,n+1,2)
print(list(x))











# imp = ============================

# print("Hello")
# print("Hii")
# output = hello
# output = Hii

# if we want to print in one line so

# print("Hello", end=',')
# print("Hii")
# output = Hello,Hii

# imp ==============================

#  char to ascii==ord()
#  ascii to char == chr()

















print("Enter Two Numbers")
print(int(input("Enter First Number"))+int(input("Enter Second Number")))

print(input("Enter Your Name:"))     

# import for keyword from kwlist == kwlist

import keyword

x = keyword.kwlist

y = keyword.softkwlist

print(x)
print(y)

print(len(x))
print(len(y))

# import for string == punctuation

import string

x = string.punctuation

print(x)
print(len(x))

# identifiers is a name that can be used to indentify the object. examply= (variable,module,packages,libraray)
# identifiers does not have datatype but its value has:

x=12
print(x)

_y=45
print(_y)

# 5=124     not valid if declared as number
# print(5)

xyz=343
print(xyz)

# case-senstive 

x=12
# print(X) wrong
print(x)

#  combination of digit,alphabet and underscore
# we can use digit after underscore or alphabet

_1x2y=3534
print(_1x2y)

#  can't use space in declaration

# wrong
x y =12
print(x y)

# right
x_y=12
print(x_y)

jatin_parmar=43
print(jatin_parmar)

name='Jatin Parmar'
print(name)

print("Hello =",name)

# to find memory address 
# and that (name) might be declared also
print(id(name))

# comparasion operators

# x=10
# y=20
# print(x==y)
# print(x!=y)
# print(x>y)
# print(x>=y)
# print(x<y)
# print(x<=y)

# x=[10]
# y=[10]
# print(x==y)
# print(x!=y)
# print(x>y)
# print(x>=y)
# print(x<y)
# print(x<=y)

# x=10
# y=10
# print(x==y)
# print(x!=y)
# print(x>y)
# print(x>=y)
# print(x<y)
# print(x<=y)

# assingment operators
x=5
x=x+2
print(x) 
# ans=7

#  logical operators   (and)

x=10
y=12
z=13

print(x<y and y<z)
# ans True
print(x<y and y>z)
# ans False

#  logical operators   (or)

x=10
y=12
z=13

print(x<y or y<z)
# ans True
print(x<y or y>z)
# ans True

#  logical operators   (not)

x=10
y=12
z=13

print(not(x<y or y<z))
# ans False
print(not(x<y or y>z))
# ans False

#  membership operators
str1='jatin'
print('a' in str1)
# true

print('a' not in str1)
# false

# identity operators

x=10
y=20
print(x is y)
# False

x=10
y=10
print(x is y)
# True

x=[10]
y=[10]
print(x is y)
# False  beacuse of diffrent memory storage  \\ example at 198-201

x=10
y=10
print(x == y)
# True

# example
x=10
print(id(x))
y=10
print(id(y))
print(x is y)

x=[10]
print(id(x))
y=[10]
print(id(y))
print(x is y)
print(x==y)
# examples

# bitwise operators

# &   (and operator)
x=10
y=20
print(x & y)
# ans = 0

#  |  (or),(pipe operator)
x=10
y=20
print(x | y)
#  ans = 30

# ~  (not),(tilt)
x=10
print(~x)
#  ans = -11

#  ^ (x-or)
x=10
y=20
print(x ^ y)
#  ans = 30

# << (left sift)
# (x << 2)   2 is the number that says how many bit u have to move to left
# multiply the number by 2's power how many digit u move
x=10
print(x << 2)
#  ans 40

x=10
print(x << 1)
# ans 20

# >> (right shift)
# divide the number by 2's power how many digit u move
# remove the digit comes after decimal
x=10
print(x >> 1)
# ans 5

x=10
print(x >> 2)
#  ans 2


#   literals
# numeric

# complex
x=5+3j
print(type(x))

# integer
x=5
print(type(x))

# float
x=5.6
print(type(x))


# string
# single,double and triple

x='n'
print(type(x))
# ans = str

x='jatin"parmar"'
print((x))
# ans = jatin"parmar"

x="n"
print(type(x))
# ans = str

x="jatin'parmar'"
print((x))
# jatin'parmar'

x='''n'''
print(type(x))
# ans = str

x='''
        *
       ***
      *****
     *******
          '''
print((x))


# boolean

x=True
print(x)
# True  
print(type(x))
# <class 'bool'>


# list

x=[12,2,45,38,"yat"]
# can't use list in place of x or any other variable
print(x)  
print(type(x))
# ans <class 'list'>

# tuple
x=(12,2,45,38,"yat")
print(x)  
print(type(x))
# ans <class tuple>

# dict
x={'name':'jatin','age':23,"city":'sehore'}
print(x)  
print(type(x))
# can't use same key twice
# ans <class 'dict'>

# set
x={12,23,4,56,12}
print(x)  
print(type(x))
# ans   {56, 12, 4, 23}
#  ans    <class 'set'>

# frozenset
x=frozenset({12,23,4,56,12})
print(x)  
print(type(x))
# frozenset({56, 12, 4, 23})
# ans <class 'frozenset'>


# indexing questions  ?
# indexing works on ordered collection = like == string , list , tuple

# to search
str1='python'
print(str1.index('p'))
# ans = 0
print(str1.index('p',1))
# error      because starts from 1 indexing
print(str1.index('t',1))
# ans = 2
print(str1.index('p',0,1))
#  ans = 0
print(str1.index('t',0,1))
# error

str1='python'
print(str1.index('python'))
# ans = 0

# get object
# indexing location
# first object
str1='python'
print(str1[0])
# ans = p

# last object
str1='python'
print(str1[-1])
# ans = n

# with list
li1=[12,23,3,45]
print(li1.index(23))
# ans = 1

li2=[10,23,10,23,76]
print(li2.index(10,1))
# ans = 2

# with tuple
tu1=(12,23,3,45)
print(tu1.index(3))
# ans = 2

# 8 = slicing questions 

str1='python'
print(str1[: : 1])
# ans = python

str1='python'
print(str1[: : -1])
# ans = nohtyp









# datatypes         ===================

# integer === 
# 1 = numeric
x=10
y=20
print(type(x))
# ans = <class 'int'>
print(type(y))
# ans = <class 'int'>

z=x+y
print(type(z))
# ans = <class 'int'>

z=x-y
print(type(z))
# ans = <class 'int'>

z=x*y
print(type(z))
# ans = <class 'int'>


# float
z=x/y
print(type(z))
# ans = <class 'float'>


x=10.3
y=1.1
print(type(x))
# ans = <class 'float'>
print(type(y))
# ans = <class 'float'>

z=x+y
print(type(z))
# ans = <class 'float'>

# complex
x=10.1+3j
y=20.2+2j
z=x+y
print(type(z))
# ans = <class 'complex'>

x=10+3j
y=20+2j
z=x+y
print(type(z))
# ans = <class 'complex'>

# 2 = string    ======================
str1="pyhton"
print(type(str1))
# ans <class 'str'>

x=input("Enter name")
print(type(x))
# ans Enter namejatin
# <class 'str'>
print(id(x))
# /ans 1733566770336


str1 = "python"
print(max(str1))
# ans y             finds the highest aschi value of letter 

str1 = "pyhton"
print(min(str1))
# ans h

str1 = "pyhton"
print(len(str1))
# ans 6

# methods of string


str1 = " I Love Python"
print(str1.lower())
#  i love python

str1 = " I Love Python"
print(str1.upper())
#  I LOVE PYTHON

str1 = " I Love Python"
print(str1.title())
#  I Love Python

str1 = " I Love Python"
print(str1.capitalize())
#  i love python

str1 = " I Love Python"
print(str1.swapcase())
#  i lOVE pYTHON

str1 = " I Love Python"
print(str1.find('P'))
# 8

str1 = " I Love Python"
print(str1.find('z'))
# -1                      if not finf then -1 is by default value

str1 = " I Love Python"
print(str1.index('z'))
# error


str1 = " I Love Python"
print(str1.split())
# ['I', 'Love', 'Python']        by default split through space i f value not given

str1 = " I Love Python"
print(str1.split('o'))
# [' I L', 've Pyth', 'n']

str1 = " I Love Python"
print(str1.split('o',1))
# [' I L', 've Python']      if passs 1 then object return 2   ,   if passs 2 then object return 3    and so on   



# output of join is = single output
la=['shir','jatin','parmar']

print(','.join(la))
# shir,jatin,parmar          ',' is yhe point from where u want to join

print(''.join(la))
# shirjatinparmar

print(' '.join(la))
# shir jatin parmar

la="i love python"
print(la.count('o'))
# 2

# 3 = list ============

li1=["jatin",23,"jay",12.1]
print(type(li1))
# ans <class 'list'>

# methods of list
# 1 = append()     = add one object at last
l1=[22,23,"jatin",2]
x=(10,23,57)
l1.append(x)
print(l1)
# ans  [22, 23, 'jatin', 2, (10, 23, 57)]

l1=[22,23,"jatin",2]
x=(10)
l1.append(x)
print(l1)
# ans [22, 23, 'jatin', 2, 10]


# 2 = extend == add multiple object at last
l1=[22,23,"jatin",2]
x=(10,23,57)
l1.extend(x)
print(l1)
# ans [22, 23, 'jatin', 2, 10, 23, 57]

l1=[22,23,"jatin",2]
x=("parmar")
l1.extend(x)
print(l1)
# ans [22, 23, 'jatin', 2, 10, 23, 57]

# 3 = insert ==
l1=[22,23,"jatin",2]
l1.insert(0,"shri")    
print(l1)
# 0 is position and "shri" is object to add at 0 position
# ans ['shri', 22, 23, 'jatin', 2]

# 4 = sort ==    data type must be same
l1=[22,23,2]
l1.sort()
print(l1)
# ans [2, 22, 23]

# 5 = reverse ==
l1=[22,23,2,5,3]
l1.reverse()
print(l1)
# ans [3, 5, 2, 23, 22]

#  6 = pop ==         remove last object
l1=[22,23,2,5,3]
l1.pop()
print(l1)
# ans [22, 23, 2, 5]

#  7 = remove ==           id duplicate object in array then remove first of list
l1=[22,23,2,5,3]
l1.remove(5)
print(l1)
# ans [22, 23, 2, 3]

# 8 = clear == clear object from list and leave empty list
l1=[22,23,2,5,3]
l1.clear()
print(l1)
# ans []

# 9 = copy  ==      diffrent  memeory address
l1=[22,23,2,5,3]
l2=l1.copy()
print(l1,l2)
#  ans [22, 23, 2, 5, 3] [22, 23, 2, 5, 3]
print(id(l1),id(l2))
# ans 1923298320704 1923298468800

# 10 = count ==   give number how many times it comes in object
l1=[22,23,2,5,3,23]
print(l1.count(23))
# ans 2

# 11 = index  ==       indexing number
l1=[22,23,2,5,3,23]
print(l1.count(2))
# ans 1

# 4 tuple

t1=(1,2,3,4,5,6,7)
print(t1)
# ans (1, 2, 3, 4, 5, 6, 7)
print(type(t1))
# ans <class 'tuple'>

# in-built function of tuple
t1=(1,2,3,4,5,6,7)
print(max(t1))
# 7

print(min(t1))
# 1

print(sum(t1))
# 28

print(len(t1))
# 7

print(id(t1))
# 1800699082688

print(type(t1))
# <class 'tuple'>

# methods of tuple

t1=(1,2,3,4,5,6,7)

print(t1.index(4))
# 3

print(t1.count(5))
# 1

#  5 = dict
# inbuilt functions

d1={'name':'jatin','age':24,'city':'sehore','qualification':'MA'}

print(max(d1))
# qualification

print(min(d1))
# age

print(len(d1))
# 4

print(type(d1))
# <class 'dict'>

print(id(d1))
# 1985547804032

# methods of dict

#  clear()
d1={'name':'jatin','age':24,'city':'sehore','qualification':'MA'}
d1.clear()
print(d1)
# {}

print(id(d1))
# 1787535236480

# coyp()
d1={'name':'jatin','age':24,'city':'sehore','qualification':'MA'}
d2=d1.copy()
print(d2)
# {'name': 'jatin', 'age': 24, 'city': 'sehore', 'qualification': 'MA'}

print(id(d1),id(d2))
# 1954606816640 1954607210560            diffrent memory address

# fromkeys()
d1={'name','age','city','qualification'}
d2=dict.fromkeys(d1)
print(d2)
# {'age': None, 'qualification': None, 'name': None, 'city': None}              ==  none is by default

d1={'name','age','city','qualification'}
d2=dict.fromkeys(d1,100)
print(d2)
# {'qualification': 100, 'city': 100, 'name': 100, 'age': 100}

# get()
d1={'name':'jatin','age':24,'city':'sehore','qualification':'MA'}
# print(d1.get('key'))
print(d1.get('age'))
# 24

# items()   return key : value pair
d1={'name':'jatin','age':24,'city':'sehore','qualification':'MA'}
print(d1.items())
# dict_items([('name', 'jatin'), ('age', 24), ('city', 'sehore'), ('qualification', 'MA')])            return ans in tuple formate

# keys() 
d1={'name':'jatin','age':24,'city':'sehore','qualification':'MA'}
print(d1.keys())
# dict_keys(['name', 'age', 'city', 'qualification'])

# values()
d1={'name':'jatin','age':24,'city':'sehore','qualification':'MA'}
print(d1.values())
# dict_values(['jatin', 24, 'sehore', 'MA'])


# popitem()
d1={'name':'jatin','age':24,'city':'sehore','qualification':'MA'}
print(d1.popitem())
# ('qualification', 'MA')


print(d1)
# {'name': 'jatin', 'age': 24, 'city': 'sehore'}

# pop()
d1={'name':'jatin','age':24,'city':'sehore','qualification':'MA'}
print(d1.pop('age'))
# 24

print(d1)
# {'name': 'jatin', 'city': 'sehore', 'qualification': 'MA'}

# set default
d1={'name':'jatin','age':24,'city':'sehore','qualification':'MA'}
print(d1.setdefault('name','raj'))
# jatin                              can't change because name is already there with asigned value

print(d1)
# {'name': 'jatin', 'age': 24, 'city': 'sehore', 'qualification': 'MA'}             can't change data now

d1={'name':'jatin','age':24,'city':'sehore','qualification':'MA'}
print(d1.setdefault('new','raj'))
# raj

print(d1)
# {'name': 'jatin', 'age': 24, 'city': 'sehore', 'qualification': 'MA', 'new': 'raj'}

# update()
d1={'name':'jatin','age':24,'city':'sehore','qualification':'MA'}
d2={'cet':'get'}
d1.update(d2)
print(d1)
# {'name': 'jatin', 'age': 24, 'city': 'sehore', 'qualification': 'MA', 'cet': 'get'}


# 6 = set   ===========================================================================================

set1={'jatin',24,'raj',87,54,'abhi',52.1}

print(set1)
# {52.1, 54, 87, 24, 'jatin', 'abhi', 'raj'}          unordered

print(type(set1))
# <class 'set'>

# inbiult methods of set
# max()
set1={'jatin','raj','abhi'}
print(max(set1))
# raj

# min()
set1={'jatin','raj','abhi'}
print(min(set1))
# abhi

# type()
set1={'jatin',24,'raj',87,54,'abhi',52.1}
print(type(set1))
# <class 'set'>

# id()
set1={'jatin','raj','abhi'}
print(id(set1))
# 1642109076192

# len()
set1={'jatin','raj','abhi'}
print(len(set1))
# 3

# sum()
set1={5,1,4,7,8}
print(sum(set1))
# 25

# methods for set

# copy()
set1={5,1,4,7,8}
x=set1.copy()
print(x)
# {1, 4, 5, 7, 8}           unordered

# clear()
set1={5,1,4,7,8}
set1.clear()
print(set1)
# set()

# add()
set1={5,1,4,7,8}
set1.add(9)
print(set1)
# {1, 4, 5, 7, 8, 9}             unordered

# update()
set1={5,1,4,7,8}
l1={6,58,5}
set1.update(l1)
print(set1)
# {1, 4, 5, 6, 7, 8, 58}

# pop()
set1={5,1,4,7,8}
set1.pop()
print(set1)
# {4, 5, 7, 8}

# remove()              remove particular element of set
set1={5,1,4,7,8}
set1.remove(4)
print(set1)
# {1, 5, 7, 8}

set1.remove(4)
print(set1)
# error        because we remove 4 just up

# discard()        also remove particular element
set1={5,1,4,7,8}
set1.discard(4)
print(set1)
# {1, 5, 7, 8}

set1.discard(4)
print(set1)
# {1, 5, 7, 8}           it dosen't show error as remove does when not find that element

# special mathematical operstions for set

# union()
A={1,2,3,4,5,6}
B={3,6,7,8}
print(A.union(B))
# {1, 2, 3, 4, 5, 6, 7, 8}

print(A)
# {1, 2, 3, 4, 5, 6}

print(B)
# {8, 3, 6, 7}

# intersection()
A={1,2,3,4,5,6}
B={3,6,7,8}
print(A.intersection(B))
# {3,6}                 takes common element

print(A)
# {1, 2, 3, 4, 5, 6}

print(B)
# {8, 3, 6, 7}

# intersection_update()

A={1,2,3,4,5,6}
B={3,6,7,8}
print(A)
# {1, 2, 3, 4, 5, 6}

A.intersection_update(B)
print(A)
# {3,6}

# diffrence()

A={1,2,3,4,5,6}
B={3,6,7,8}
A.difference(B)
print(A)
# {1, 2, 3, 4, 5, 6}


# difference_update()
A.difference_update(B)
print(A)
# {1, 2, 4, 5}

# symmetric_difference()
A={1,2,3,4,5,6}
B={3,6,7,8}
A.symmetric_difference(B)
print(A)
# {1, 2, 3, 4, 5, 6}


# symmetric_difference_update()
B.symmetric_difference_update(A)
print(B)
# {1, 2, 4, 5, 7, 8}



# 7 = frozenset ===========================

# example 
s='jatin'
x=frozenset(s)
print(x)
# frozenset({'t', 'a', 'j', 'n', 'i'})

print(type(x))
# <class 'frozenset'>

l=[1,2,5,4,6]
x=frozenset(l)
print(x)
# frozenset({1, 2, 4, 5, 6})

print(type(x))
# <class 'frozenset'>


# mathematical operations for frozenset
# union
a={2,4,6,8}
b={1,3,5,7,6,8}
x=frozenset(a)
y=frozenset(b)
print(x.union(b))
# frozenset({1, 2, 3, 4, 5, 6, 7, 8})

# intersection
a={2,4,6,8}
b={1,3,5,7,6,8}
x=frozenset(a)
y=frozenset(b)
print(x.intersection(b))
# frozenset({8, 6})

# difference
a={2,4,6,8}
b={1,3,5,7,6,8}
x=frozenset(a)
y=frozenset(b)
print(x.difference(b))
# frozenset({2, 4})

# symmetric_difference
a={2,4,6,8}
b={1,3,5,7,6,8}
x=frozenset(a)
y=frozenset(b)
print(x.symmetric_difference(b))
# frozenset({1, 2, 3, 4, 5, 7})

# isdisjoint  = return boolean
a={2,4,6,8}
b={1,3,5,7,6,8}
x=frozenset(a)
y=frozenset(b)
print(x.isdisjoint(y))
# False
print(y.isdisjoint(x))
# False

# issubset     value of a present in b
a={2,4,6,8}
b={1,3,5,7,6,8}
x=frozenset(a)
y=frozenset(b)
print(x.issubset(y))
# False
print(y.issubset(x))
# False

# issuperset   
a={2,4,6,8}
b={1,3,5,7,6,8}
x=frozenset(a)
y=frozenset(b)
print(x.issuperset(y))
# False
print(y.issuperset(x))
# False



# condiational statement =============================================

# 1 = conditional statement
# a if
x=10
y=20

if x<y:
    print("not")

print("hello..........")

# not
# hello..........
# if condition is true then it provide ans

x=10
y=20

if x>y:
    print("not")

print("hello..........")
# hello..........
# if condition is false then it avoid statement and print next line if present




# b if-else

x=int(input("Enter Any Number"))
# takes input from user and that is integer

if x%2==0:
    print("Even Number")

else:
    print("Odd Number")




# wrong approach==============
# we don't use 'True' in if condition because it is hard coding
x=int(input("Enter Any Number"))

if True:
    print("Even Number")

else:
    print("Odd Number")
# it gives even number beacuse it is true so if u say odd number it gives answer 'even number'
# wrong approach==============



# question
x=int(input("Enter 1st Number"))
y=int(input("Enter 2nd Number"))


if x>y:
    print("x is greater")

else:
    print(f'{y} is greater')


# question
x=int(input("Enter your age"))


if x>=18:
    print("u can vote")

else:
    print("you can't vote")



# nested if

a=int(input("Enter 1st Number = "))
b=int(input("Enter 2nd Number = "))
c=int(input("Enter 3rd Number = "))

if (a>b and a>c):
    print(f'{a} is greater')

else:
    if (b>c and b>a):
        print(f'{b} is greater')

    else:
        print(f'{c} is greater')

# exception = first and second num is zero and third is -1 then gives -1 bigger
# avoid using nested if


# if elif

a=int(input("Enter 1st Number = "))
b=int(input("Enter 2nd Number = "))
c=int(input("Enter 3rd Number = "))

if (a>b and a>c):
    print(f'{a} is greater')

elif (b>c and b>a):
     print(f'{b} is greater')

elif (c>a and c>b):
     print(f'{c} is greater')

# not work for two same number



# complete for same number also
a=int(input("Enter 1st Number = "))
b=int(input("Enter 2nd Number = "))
c=int(input("Enter 3rd Number = "))


if (a==b and b==c ):
    print("a and  b and c are equal")


elif (a==b ):
    print("a and  b are equal")


elif (b==c ):
    print("b and  c are equal")

elif (c==a ):
    print("c and  a are equal")


elif (a>b and a>c):
    print(f'{a} is greater')

elif (b>c and b>a):
     print(f'{b} is greater')

elif (c>a and c>b):
     print(f'{c} is greater')

else:
    print("Please Enter Valid Input")



    # iterative statement

 # 1= while loop
    # print natural number
n=int(input("Enter Any Number"))
i=1
while i<=n:
    print(i)
    i=i+1
# ans print from 1 to 10

# 2's table in table format
n=int(input("Enter Any Number"))
i=1
while i<=n:
    x=2*i
    print(f'2*{i}={x}')
    i=i+1

# 10 even number
n=int(input("Enter Any Number"))
i=1
while i<=n:
    x=2*i 
    print(x)
    i=i+1

# print counting from 1 to 10 in horizontal line with coma seperate

n=int(input("Enter Any Number"))
i=1
while i<=n:
    if i<n:
        print(i,end=',')

    else:
        print(i)
    i=i+1

print("hello")
# ans 1,2,3,4,5,6,7,8,9,10
# ans hello


# digit count of a number with floor method = //
n=int(input("Enter Any Number"))
digit=0
while n>0:
    digit=digit+1
    n=n//10
print(digit)
# now if we print n then ans is 0


# sum of number
n=int(input("Enter Any Number"))
sum=0
while n>0:
    last_digit=n%10
    sum=sum+last_digit**2
    n=n//10
print(sum)
print(n)
# sum=
# n=0


# armstromg number
n=int(input("Enter Any Number"))
x=y=n
digit=0
while n>0:
    digit=digit+1
    n=n//10
sum=0
while y>0:
     last_digit=y%10
     sum=sum+last_digit**digit
     y=y//10
if x==sum:
    print(f'{x} is armstrong')

else:
    print(f'{x} is not a armstrong')


# pallindrom
n=int(input("Enter Any Number"))
x=n
rv_digit=0
while n>0:
    last_digit=n%10
    rv_digit=rv_digit*10+last_digit
    n=n//10
if x==rv_digit:
    print(f'{x} is pallindrom')
else:
    print(f'{x}is not')




# pallindrom with slice

n=input("Enter String")

if n==n[::-1]:
    print("pallindrom")

else:
    print("not")


# 2 for loop
# questions = 

n=input("Enter Your Name")

for i in n:
    print(i)


# add 4 char

n='abcd'
for i in n:
    x=ord(i)+4
    y=chr(x)
    print(y,end='')


# pallindrom
n=input("Enter string")
l=len(n)
x=''
for i in range(l-1,-1,-1):
    x=x+n[i]
if n==x:
    print ("Pallindrom")
   
else:
    print("not")