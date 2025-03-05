# topics ======*********************************************************************===========================

# 1=keyward=35 ==========

# True , False , None , and , as ,assert , async , await , break , class , continue , def , del , elif , else , except , finally ,
#  for , from , global , if , import , in , is , lambda , nonlocal , not , or , pass , raise , return , try , while , with , yield 

# softkward=4

# 'match' , 'case' , 'type' , '_'

# special symbol=32

#  + , - , * , = ,  ** , / , //(floor) , % , << , >> , & , | , ^ , ~ , < > , <= , >= , == , != , <> , += , -= , *= , /= , //= , %= , **= , &= ,
#  |= , ^= , >>= , <<== ,

# 2=punctation = 32

# ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~


# 3=identifiers         ===============================================================================================

# 4=operators            =======================================================================================================

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

# 5=literals   [The value asigned to a constant variable is called literals]          =====================================================

# literals types===  [numeric, string, boolen, list, tuple, dict , (set,frozenset)]  set and frozenset are not used in web development
# and these types are called data types

# 5A=numeric ===
# a=integer== 2,4,5,7,etc
# b=float== 3.4,1.2,5.4,etc
# c=complex== x+yj             x is real number  and y is imaginary number

# 5B =string  ==    collection of characters     
# represented by==
# ''=single quote     ====     used for single line string   
#    ""=double quote   ====    used for single line string  (prefer single quote because it take less memory then double quote)
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


# 6 (                            ==============================================================

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

# dict
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



# 7 = indexing            =========================================================================================================

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

# 8 = slicing          ======================================================================================================

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



# 9 = data-types   ===================================================================================================================== 


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


# 10 = control statement         ===============================================================================

# python is a squential + conditional statement
# 
# 10a = conditional statement = if , if-else , if-elif , if-elif-else

# 10b =  looping / iterative statement  = while , for
# while   =  1 = initialization      2 = condition check   = (a) If True = execute block of code  (b) Increase/Decrease (c) If condition False = break/terminate loop
# syntax  =  initialization(i)  ,  while(condition check) , block of code  , i=i+1 / i=i-1

# for    =  
# syntax  =  for i in collection 
#          collections are = list , string , tuple , dict

# 10c =  transfer statement    = continue , break , pass

# break = exit from loop
# continue = skip current iteration
# pass = skip current block                                                                                                             



# 11 = pattern

# 12 = calculator

# 13 = LCM And HCF



# 14 = Function 


# function is a block of reusable code 
# syntax = 

# *=required    , o=optional


# *def *function-name(parameter):    (parameter is optional)
#     'doc-string'   = optional
#     body of function     = cant leave it empty
#     return               = optional

# var *function-name(argument)                =  call a function
# argument is optional

# relation between parameter and argument=
# 1 = positional argument
# 2 = key-word argument
# 3 = default argument
# 4 = variable length argument   or   (* args)
# (* args) =  use to pass tuple as a argument


# 15 = scope of varaible = 

# 1a = local variable   = access only in its block 
# 1b = global variable   = access throghout the code 
# imp = to make local variable into global variable = global (keyward)
# imp = to access global variable into local scope with the same name of declaration present =  globals()    (keyward)






















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


x= list(range(50,101))
print(x)




# imp =========

# eval()   = 10 = return int , 'jatin' = return str  , [10,20,30] = return list

x=eval(input("Enter any thing"))
print(x)
print(type(x))







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

# identifiers is a name that can be used to indentify the object. example = (variable,module,packages,libraray)
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
# True

print('a' not in str1)
# False

# identity operators

x=10
y=20
print(x is y)
# False      because both have diffrent memory address

x=10
y=10
print(x is y)
# True     bacause both have same memory address

x=[10]
y=[10]
print(x is y)
# False  beacuse of diffrent memory storage  

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


#   literals ==================================================================================

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
print(type(x))
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
# can't use list keyward in place of x or any other variable
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
# ans   {56, 12, 4, 23}      // order is always different
#  ans    <class 'set'>

# frozenset
x=frozenset({12,23,4,56,12})
print(x)  
print(type(x))
# frozenset({56, 12, 4, 23})     // order is always different
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

str1 = "python"
print(min(str1))
# ans h

str1 = "python"
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
# -1                      if not find then -1 is by default value

str1 = " I Love Python"
print(str1.index('z'))
# error


str1 = " I Love Python"
print(str1.split())
# ['I', 'Love', 'Python']        by default split through space if value not given

str1 = " I Love Python"
print(str1.split('o'))
# [' I L', 've Pyth', 'n']

str1 = " I Love Python"
print(str1.split('o',1))
# [' I L', 've Python']      if passess 1 then object return 2   ,   if passs 2 then object return 3    and so on   



# output of join is = single output
la=['shir','jatin','parmar']

print(','.join(la))
# shir,jatin,parmar          ',' is the point from where u want to join

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



# conditional statement =============================================

# 1 = conditional statement
# a if
x=10
y=20

if x<y:
    print("smaller")

print("hello..........")

# smaller
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
# ans print from 1 to n

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
print(n)
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


    # transfer statement    

# questions ==== 

# break = exit from loop=======

n=int(input("Enter Any Number"))
i=1
while i<=n:
    if i==6:
        break
    print(i)
    i=i+1

# continue = skip current iteration

n=int(input("Enter Any Number"))
i=1
while i<=n:
    if i==6:
        i=i+1
        continue
    print(i)
    i=i+1
# skip 6 from loop


# infinitie loop
n=int(input("Enter Any Number"))
i=1
while i<=n:
    if i==6:
        print(i)
        continue
    print(i)
    i=i+1
# print 6 for infinte


# pass = skip current block
n=int(input("Enter Any Number"))
i=1
while i<=n:
    if i==6:
        i=i+1
        pass     
    print(i)
    i=i+1
# print 1 to n number except 6
	



# patterns ==================================================================================

# n is the number of row

# right angle triangle

n=int(input("Enter row"))
i=1
while i<=n:
    print(i*'*')
    i=i+1
# ans
# *
# **
# ***
# ****
# *****


# inverted left 
n=int(input("Enter row"))
while n>=1:
    print('*'*n)
    n=n-1

    #  0r

n=int(input("Enter row"))
i=n
while i>=1:
    print('*'*i)
    i=i-1

# ans
# *****
# ****
# ***
# **
# *


# left angle triangle

n=int(input("Enter row"))
i=1
while i<=n:
    print(' '*(n-i)+'*'*i)
    i=i+1

# ans

#     *
#    **
#   ***
#  ****
# *****

# inverted right
n=int(input("Enter row"))
i=0
while i<n:
    print(' '*i+'*'*(n-i))
    i=i+1

# ans
# *****
#  ****
#   ***
#    **
#     *

# pyramid
# u can give space before or after (*) that doesn't matter  = ' *' = '* '
n=int(input("Enter row"))
i=1
while i<=n:
    print(' '*(n-i)+' *'*i)
    i=i+1
# ans
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *

# inverted pyramid
# u can give space before or after (*) that doesn't matter  = ' *' = '* '
n=int(input("Enter row"))
i=0
while i<n:
    print(' '*i+'* '*(n-i))
    i=i+1

# ans
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 




# design  1 =
# *
# **
# ***
# ****
# *****
# ******
# *****
# ****
# ***
# **
# *

n=int(input("Enter row"))
i=1
while i<=n:
    print(i*'*')
    i=i+1

while i>=1:
    print('*'*i)
    i=i-1


#  design 2 =====
#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *

n=int(input("Enter row = "))
i=1
while i<=n:
    print(' '*(n-i)+'*'*i)
    i=i+1

i=1
while i<n:
    print(' '*i+'*'*(n-i))
    i=i+1

# design 3 
# *
# **
# ***
# ****
# *****
#  ****
#   ***
#    **
#     *

n=int(input("Enter row = "))
i=1
while i<=n:
    print(i*'*')
    i=i+1
i=1
while i<=n:
    print(' '*i+'*'*(n-i))
    i=i+1

# design 4 
#     *
#    **
#   ***
#  ****
# *****
# *****
# ****
# ***
# **
# *

n=int(input("Enter row = "))
i=1
while i<=n:
    print(' '*(n-i)+'*'*i)
    i=i+1

i=n
while i>=1:
    print('*'*i)
    i=i-1

# design 5
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
n=int(input("Enter row = "))
i=1
while i<=n:
    print(' '*(n-i)+' *'*i)
    i=i+1
i=1
while i<n:
    print(' '*i+' *'*(n-i))
    i=i+1




# calculator =======================================================

while True:
    print("1 for add \n 2 for sub \n 3 for multiply \n 4 for division \n 5 for OFF")
    n=int(input("Enter Your Choice"))
    if n==1:
        x=int(input("Enter First Number"))
        y=int(input("Enter Second Number"))
        z=x+y
        print(f'addition of {x} and {y} is {z}')

    elif n==2:
         x=int(input("Enter First Number"))
         y=int(input("Enter Second Number"))
         z=x-y
         print(f'sub of {x} and {y} is {z}')

    
    elif n==3:
         x=int(input("Enter First Number"))
         y=int(input("Enter Second Number"))
         z=x*y
         print(f'multiply of {x} and {y} is {z}')

    
    elif n==4:
         x=int(input("Enter First Number"))
         y=int(input("Enter Second Number"))
         z=x-y
         print(f'div of {x} and {y} is {z}')

    elif n==5:
        break

    else:
        print("Enter Valid Number")


    
                
                                # or modified version of claculator



while True:
    print("1 for add \n 2 for sub \n 3 for multiply \n 4 for division \n 5 for OFF")
    n=int(input("Enter Your Choice = "))
    p=(1,2,3,4,5)
    if n in p:
        x=int(input("Enter First Number"))
        y=int(input("Enter Second Number"))

        if n==1:
            z=x+y
            print(f'addition of {x} and {y} is {z}')

        elif n==2:
            z=x-y
            print(f'sub of {x} and {y} is {z}')

        elif n==3:
             z=x*y
             print(f'multiply of {x} and {y} is {z}')

        elif n==4:
             z=x-y
             print(f'div of {x} and {y} is {z}')

        elif n==5:
             break

        else:
             print("Enter Valid Number")



#  LCM 
x=int(input("Enter First Number = "))
y=int(input("Enter Second Number = "))
maxN=max(x,y)

while True:
    if maxN%x==0 and maxN%y==0:
        break
    maxN=maxN+1
print(f'LCM of {x} and {y} is = {maxN}')

# HCF
x=int(input("Enter First Number = "))
y=int(input("Enter Second Number = "))
minN=min(x,y)

while True:
    if x%minN==0 and y%minN==0:
        break
    minN=minN-1
print(f'HCF of {x} and {y} is = {minN}')




# Function

#  1 = postional argument = if we pass 2 parameter then we have to give 2 arguments also 
def sum(x,y):
    return x+y
z= sum (2,4)
print(z)
# ans 6



def sum(x,y):
    return x+y
z= sum (2)
print(z)
error = missing one argument


# 2 = keyward argument

def sum(x,y):
    return x+y
z= sum (y=5,x=5)
print(z)
ans 10 

#     or 
# we can ask at run time also

def sum(x,y):
    print("value of x = ",x)
    print("value of y = ",y)
    return x+y
p=int(input("Enter value 1 = "))
q=int(input("Enter value 2 = "))

z= sum (y=p,x=q)
print(z)

# ans
# Enter value 1 = 4
# Enter value 2 = 4
# value of x =  4
# value of y =  4
# 8


# use of doc string
def sum(x,y):
    'Use for sum'
    print("value of x = ",x)
    print("value of y = ",y)
    return x+y
p=int(input("Enter value 1 = "))
q=int(input("Enter value 2 = "))

z= sum (y=p,x=q)
print(z)
print(sum.__doc__)

#  ans = Use for sum

# print(dir(sum))  === use to see magic method for sum function
# methods =
# ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__type_params__']



# 3 = default argument =  we can asign values in parameter if didn't want to pass as an argument

def added (x=0,y=0,z=0):
    p=x+y+z
    return p
x=added()
print(x)


# or 

def added (x=0,y=0,z=0):
    print('x=',x)
    print('y=',y)
    print('z=',z)
    return x+y+z
x=added(5)
print(x)
# x= 5
# y= 0
# z= 0
# 5

#   or 
def added (x=0,y=0,z=0):
    print('x=',x)
    print('y=',y)
    print('z=',z)
    return x+y+z
x=added(5,6,7)
print(x)
# x= 5
# y= 6
# z= 7
# 18


# 4 = variable length argument
# we can't pass integer with *
# gives tuple


def add(*n):
    print(n)
    print(type(n))
    sum=0
    for i in n:
        sum=sum+i
    return sum
   

x=add(1,2,3,4,5,6)
print(x)

# (1, 2, 3, 4, 5, 6)
# <class 'tuple'>
# 21

# value taken at run time
def add(*n):
    print(n)
    print(type(n))
    sum=0
    for i in n:
        for x in i:
            sum=sum+x
    return sum

p=eval(input("Enter Any Tuple = "))
x=add(p)
print(x)
# ans
# ((1, 2, 3, 4, 5),)
# <class 'tuple'>
# 15

#              to remove nested loop we use * where we call function and provide answer in single tuple (1,2,3)

def add(*n):
    print(n)
    print(type(n))
    sum=0
    for i in n:
        sum=sum+i
    return sum

x=eval(input("Enter Tuple="))
res=add(*x)
print(res)
# ans 
# (1, 2, 3, 4, 5)
# <class 'tuple'>
# 15



# 4 default key-ward argument===  **kwarge
# gives dict

def showdetail(**n):
    print(n)
    print(type(n))
showdetail(name='jatin',age=24,city='Sehore')
# 
# {'name': 'jatin', 'age': 24, 'city': 'Sehore'}
# <class 'dict'>

# looping in dict for every details
def showdetail(**n):
    print(n)
    print(type(n))
    for k,v in n.items():
        print(f'My {k} is {v}')

showdetail(name='jatin',age=24,city='Sehore')
# ans 
# {'name': 'jatin', 'age': 24, 'city': 'Sehore'}
# <class 'dict'>
# My name is jatin
# My age is 24
# My city is Sehore


# used double star ** at parameter and at argument

def showdetail(**n):
    print(n)
    print(type(n))
    for k,v in n.items():
        print(f'My {k} is {v}')

x=eval(input("Enter Key Value = "))
showdetail(**x)

# 
# Enter Key Value = {'name':'jatin','age':24}
# {'name': 'jatin', 'age': 24}
# <class 'dict'>
# My name is jatin
# My age is 24


# print with methods
def showdetail(**n):
    l=[]
    for v in n.value():
        l.append(v)
    return l

    
x=eval(input("Enter Key Value = "))
res=showdetail(**x)
print(res)
# provide only values    == 



#  scope of variable


x=10
def new():
    y=20
    print(y)
    print(x)
new()
print(x)
print(y)
# ans 
# 20
# 10
# 10
# error


# declare y as global to access throughout the code 

x=10
def new():
    global y
    y=20
    print(y)
    print(x)
new()
print(x)
print(y)
# ans 
# 20
# 10
# 10
# 20


# make the local value global and access throgout the code
x=10
def new():
    global x
    print(x)
    x=20
    print(x)
new()
print(x)
# ans 
# 10
# 20
# 20


# access global variable in local scope = using globals method
x=10
def new():
    x=20
    print("Enter global variable = ",globals()['x'])
    print("Enter local variable = ",x)

new()
print(x)
# ans
# Enter global variable =  10
# Enter local variable =  20
# 10



# y as global with global x in local scope  

x=10
def new():
    global y
    x=20
    y=30
    print("Enter global variable = ",globals()['x'])
    print("Enter local variable = ",x)
    print("Enter local variable = ",y)


new()
print(x)
print(y)
# ans
# Enter global variable =  10
# Enter local variable =  20
# Enter local variable =  30
# 10
# 30





























# Q - 1 Harshad Number

n=int(input("Enter Any Number"))
x=n
sum=0
while n>0:
    ld=n%10
    sum=sum+ld
    n=n//10

if x%sum==0:
    print("Harshad Number")

else:
    print("Not A Harshad")


# Q - 5  Spy Number

n=int(input("Enter Any Number"))
prod=1
sum=0
while n>0:
    ld=n%10
    sum=sum+ld
    prod=prod*ld
    n=n//10

if prod==sum:
    print("Spy Number")

else:
    print("Not A Spy")


# vowel and consonent count

str1=input("Enter Any String = ")
vowel="aeiouAEIOU"
countvowel=0
countconsonent=0

for x in str1:
    if x in vowel:
        countvowel=countvowel+1

    else:
        countconsonent=countconsonent+1

print("vowel = ", countvowel, "consonents =",countconsonent)




# question = small capital letter and num count
str2=input("Enter = ")
capital=0
small=0
num=0

for x in str2:
    if x>=chr(65) and x<=chr(90):
        capital=capital+1

    elif x>=chr(97) and x<=chr(122):
        small=small+1

    elif int(x)>=0 and int(x)<=9:
        num=num+1
print("num = ",num , "small = ",small , "capital = ",capital)
    
















































#  Advance Python

# Topics



# 1 = Higher Order Function
# 1a = map()
# number of input is always equal to number of output
# we can use them directly

# 1b = filter()
# number of input is >= number of output
# we can use them directly


# 1c = reduce 
# datatype not neccesary to find in print

# number of output is always = 1
# method to use reduce

# 1 = have to import functools        (a module)
# syntax = functools.reduce(func_name,collection)

# 2 = from functools import reduce
# syntax  = reduce(func_name,collection)


# 2 = lambda function   = 
# a function that does not have a name   /   anonymos function
# function define with lambda keyword instead of def keyword
# it takes n number of arguments and execute only single line of expression
# syntax   lambda argument:expression
# we can only use list comprehension []
# we can't use while loop with lambda beacuse it support one line expression and while loop need two line of expression like 1 is condition and 2nd is increament

# 3 =  Generators  = 
#   generator is a special type of function that can be use to generate iterate object.
# instead of return keyward we now use 'yield' keyward.


# 4 =  Decorators  = 
# special type of higher order function that can take function as an arugumeht and it also return a function (where we change the behaviour)
# change the internal working without changing it's code




# 5 = module = 
# a .py extension file that contains variable,functions,class , methods .


# 6 = elliyasing =
# to use small name instead of big original name . it represent by = as keyward
# example = 
# import calculator as c
# print(c.variable)
# now we can use calculator as c in anywhere of the code and after that we can't use calculator word below elliyasing

# two types = 
# over module and over function




#  7  = oops = 
# to add real world entities to programming world

# properties of oops = 
abstraction = data-protection
encapsulation = data-protection
inheritence = reusability
polymorphism = reusability



# 7a = class = it is a dummy modele of design and it has no physical existance,it dosen't take memory until it is called;(blueprint of an object)
#       it holds properties and action/behavior of object
#       properties = variables     =  (static/class variable , instance variable , local variable)
#       action/behavior = methods  =  (constructor(special type of method) , instance method , static method , class method )
# instance = first parameter should be self

# syntax = class ClassName and Classname should be in camelcase and first letter must be capital.
# '''doc string'''  =  must written in triple quote.

# syntax = 
# class ClassName:
#     '''doc string'''
#     variables
#     methods
# obj=ClassName
# print(obj.variables)
# print(obj.method())




# 7b = object = pyhsical existance of a class  or   instance of a class.

# 7c = constructor = constructor is a special type of method that called automatically when object created.

# 7d = self = self is a refrence variable that holds address of current object of current class.

#  7e = variable = 

#  7e = 1  =  instance variable  =   a variable which is initialize with self and change its value when the value of object changes
# where we can declare instance variable = inside class   example = (self.<variable name>),  outside class   example = (object.<variable name?)
# where we can access instance variable   = inside class with the help of self  , outside class with the help of object


# 7e = 2 = static variable  =  value dosn't change when value of object change
# declare = 
# inside class = 
# outside class = 

# calling = 
# inside class = 
# outside class = 

# 7e = 3 = local variable = a variable declare inside any method then we can call it in only it's block of code 

# 7f = methods = 
# instance method = directly related to its object
# class method = @classmethod = use to modify the variable  and instead of self we now use cls.  =
# related with class not with object . 

# static method = @staticmethod = use to modify the variable  and instead of self we now use cls. = 






#  = file handeling












































# collection always need to have data type
1 = Higher Order Function

#   1a = map() = number pf input = number of output
#       syntax = map(function_name , collection)                          // collection=iterables, string , list , tuple , set , dict
# collection always need to have data type
#     another syntax = map(function_name , iterable1,iterable2)

# we can send multiple collecttions only in map method             //  imp

# 1a map()

# question 
# square of every element
def sqau(x):
    return x**2
    
l1=eval(input("Enter Any Numeric Collection = "))

res=map(sqau,l1)
print(res)
print(list(res))



# question = add +1 in odd number   ,  add +2 in even number
def add(x):
    if (x%2==0):
        return x+2

    else:
        return x+1

n=eval(input("Enter Series"))
res=map(add,n)
print(list(res))

# question 
# power is taken from second list
def powerr(x,y):
    return x**y

x=eval(input("Enter First string = "))
y=eval(input("Enter Second string = "))

res=map(powerr,x,y)
print(list(res))


# question  take 3 list and add them
def sum(x,y,z):
    return x+y+z

l1=[2,3,4]
l2=[3,4,5]
l3=[4,5,6]

res=map(sum,l1,l2,l3)
print(list(res))

# question print ['odd','even','odd','even']
def even(x):
    if x%2==0:
        return 'even'

    else :
        return 'odd'

li=[1,2,3,4,5,6,7,8,9,10]
res=map(even,li)
print(list(res))





# 1b = filter()
# number of input is >= number of output

# question  = even number
def even(x):
    if x%2==0:
        return x

li=[1,2,3,4,5,6,7,8,9,10]
res=filter(even,li)
print(list(res))

# question = odd number
if x%2!=0

# question = positive
if x>=0

# question  = negative 
if x<0


# question = find name with less character then 3
def finds(x):
    if len(x)<=3:
        return x

li=['jatin','raj','jai','amit']
res=filter(finds,li)
print(list(res))

#      run time input
def finds(x):
    if len(x)<=3:
        return x

li=eval(input("Enter Your Name = "))
res=filter(finds,li)
print(list(res))


# 1c = reduce 
# number of output = 1

# question = maximum number
# have to give 2 parameters to compare with second one




import functools

l1=[2,4,6,10,15,3]

def mymax(x,y):
    if x>y:
        return x

    else :
        return y

res=functools.reduce(mymax,l1)
print(res)


# question = minimum number

import functools

l1=[2,4,6,10,15,3]

def mymin(x,y):
    if x<y:
        return x

    else :
        return y

res=functools.reduce(mymin,l1)
print(res)


# question = sum

import functools

l1=[2,4,6,10,15,3]

def sum(x,y):
    return x+y

    
res=functools.reduce(sum,l1)
print(res)

# question = lenth of name = biggest

import functools

l1=['jatin','raj','abhishek','ajay','vikas']

def sum(x,y):
    if len(x)>len(y):
        return x

    else:
        return y
    
res=functools.reduce(sum,l1)
print(res)





2 = lambda function

# question  = add
add=lambda x,y:x+y
p=int(input("Enter 1st Number = "))
q=int(input("Enter 2nd Number = "))
print(add(p,q))

# or we can print it with expression also

add=lambda x,y:print(x+y)
p=int(input("Enter 1st Number = "))
q=int(input("Enter 2nd Number = "))
add(p,q)


# question = we can use if else 
n=int(input("Enter Number = "))
checkN=lambda x:'even number' if x%2==0 else 'odd number'
print(checkN(n))



# question = nested if         ('positive' if x>=0) if's portion      else portion ('nagetive' if x<0 else 'zero')    
n=int(input("Enter Number = "))
checkN=lambda x:'positive' if x>=0 else 'nagetive' if x<0 else 'zero'
print(checkN(n))


# question with for loop
x= lambda p :[i for i in range(p)]
p=int(input("Enter Number = "))
print(x(p))


# question nested for loop =  p for the collection and q for the repeated time
x=lambda p,q:[[r for r in range(p)]for i in range(q)]
p=int(input("Enter Number of Collection required = "))
q=int(input("Enter Number of times to repeat collection = "))
print(x(p,q))
# let p = 4
# let q = 5
# ans = [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]


# question = lambda with map
l1=[1,2,3,4,5,6,7,8]
res=list(map(lambda x:x**2 , l1))
print(res)
# ans = [1, 4, 9, 16, 25, 36, 49, 64]


# question = lambda with map at run time

n=eval(input("Enter Series"))
res=list(map(lambda x:x**2 , n))
print(res)
# Enter Series[2,3,4,5]
# [4, 9, 16, 25]


# adding to list with lambda
l1=[2,3,4,5,6]
l2=[3,4,5,6,7]
res=list(map(lambda x,y:x+y , l1,l2))
print(res)
# ans = [5, 7, 9, 11, 13]

# all letter in capital 
str1=['jatin','raj','jai']
res=list(map(lambda x: x.upper(),str1))
print(res)


# filter with lambda 
# question even 
l1=[2,3,4,5,6]
res=list(filter(lambda x:x%2==0 , l1))
print(res)


# lambda with reduce
import functools

l1=[1,2,3,4,5]
res=functools.reduce(lambda x,y : x+y , l1)
print(res)



# question = 

n=int(input("Enter Number = "))
res=[[j for j in range(1,n)] for i in range(n)]
print(res)
# Enter Number = 5
# [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

# question = 
for i in range(0,5):
    print("Hi")
# Hi
# Hi
# Hi
# Hi
# Hi

# question = with _ underscore
for _ in range(0,5):
    print("Hi")
# Hi
# Hi
# Hi
# Hi
# Hi


# 3 = generator

def new():
    yield 10

x=new()
# print(x.__next__())
# or
print(next(x))

# question
def even(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i=i+1
res=even(10)
print(res)
print(list(res))
# ans 
# <generator object even at 0x000002392CE46740>
# [0, 2, 4, 6, 8, 10]


# question
def even(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i=i+1
res=even(10)
x=next(res)
y=next(res)
z=next(res)
print(x,y,z)
# ans = 0 ,2 , 4


# 4 = decorator without @
# normsl calling

def outerfun(fun1):
    def innerfun():
        print("Before Modification")
        fun1()
        print("After Modification")
    return innerfun

def fun():
    print("This is from main Function")

res=outerfun(fun)
res()
# ans 
# Before Modification
# This is from main Function
# After Modification



# decorator is used with @
# easy calling

def outerfun(fun1):
    def innerfun():
        print("Before Modification")
        fun1()
        print("After Modification")
    return innerfun

@outerfun
def fun():
    print("This is from main Function")

fun()
# ans 
# Before Modification
# This is from main Function
# After Modification


# question

def outerfun(fun1):
    def innerfun(r,s,t):
        r=r+10
        s=s+10
        t=t+10
        a=fun1(r,s,t)
        print(a)
       
    return innerfun


def fun(x,y,z):
    return x+y+z

res=outerfun(fun)
x=int(input("Enter 1st Number = "))
y=int(input("Enter 2nd Number = "))
z=int(input("Enter 3rd Number = "))
res(x,y,z)
fun(x,y,z)

# ans  =  90






# 7 = oops

# to hit doc string

class Student:
    '''student details'''
    name='jatin parmar'
    city='sehore'

# print(dir(Student))   it gives all magic method
print(Student.__doc__)

# ans = student details 

class Student:
    '''student details'''
    name='jatin parmar'
    city='sehore'

print(dir(Student))

# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'city', 'name']


# question

class Student:
    '''student details'''
    name='jatin parmar'
    city='sehore'


print(Student)
obj=Student
print(obj)

# ans    =  these are object of python 

# <class '__main__.Student'>
# <class '__main__.Student'>


# call with  constructor
# object of class 

class Student:
    '''student details'''
    name='jatin parmar'
    city='sehore'


x=Student()   //  parentheises is neccesary to call the object of class
print(x)

# ans = 
# <__main__.student object at 0x000002BCFD3E6F90>



# constructor calling

# __init__     =  in build  constructor 

class Student:
    '''student details'''
    def __init__(self):
        print("constructor called")

# obj=Student  =  not give any thing
obj=Student()

# constructor called




# same address as self

class Student:
    '''student details'''
    def __init__(self):
        print("constructor called")
        print("self :",id(self))

# obj=Student
obj=Student()
print(id(obj))

# 
constructor called
self : 2565191069584
2565191069584



# self has already been declared in obj =
class Student:
    '''student details'''
    def __init__(self,name,roll,marks):
        self.x=name
        self.y=roll
        self.z=marks
       

obj=Student("jatin",24,95)
print(obj.x)
print(obj.y)
print(obj.z)

# ans =
jatin
24
95


# multiple constructor  //  python does not support overloadind

# it gives result of the last one 

class Student:
    '''student details'''
    def __init__(self,name,roll,marks):
        self.x=name
        self.y=roll
        self.z=marks

    def __init__(self):
        print("constructor called")
       

obj=Student()

obj.__init__()  // we can call constructor 

# constructor called


# variables = 
# 1 = instance variable = 


class Student:
    '''student details'''
    def __init__(self,name,roll,marks):
        self.x=name               //  instance varaible declare inside constructor
        self.y=roll               //  instance varaible declare inside constructor
        self.z=marks              //  instance varaible declare inside constructor

    def add_new(self,city):
        self.p=city                   //  instance varaible declare inside instance method

    def show(self):
        print(self.x,self.y,self.z,self.p,self.school_name)       //  instance varaible call inside instance method
    
       

obj=Student('jatin',21,80)                  //  instance varaible declare outside of class
obj.add_new('sehore')
obj.school_name='SHSS'
obj.show()
print(obj.x,obj.y,obj.z,obj.p,obj.school_name)



# 2 = static variable = a variable that doesn't change when object change = 


class Student:
    '''School Details'''
    school="ASSF"            // declaration of static method

    def __init__(self,name,roll):
        self.a=name
        self.b=roll
        Student.scode=123                 // declaration of static method
    
    def new(self):
        Student.city="Sehore"                 // declaration of static method
        

    def show(self):
        print(Student.school,Student.scode,Student.city,Student.subject)

Student.subject="PCM"                                    // declaration outside class
obj=Student("Jatin",101)
obj.new()
obj.show()


 # 3 = local variable =
 class Student:
    '''School Details'''
    school="ASSF"

    def __init__(self,name,roll):
        self.a=name
        self.b=roll
        Student.scode=123
    
    def new(self):
        Student.city="Sehore"
        

    def show(self):
        print(Student.school,Student.scode,Student.city,Student.subject)

Student.subject="PCM"
obj=Student("Jatin",101)
obj.new()
obj.show()
print(school)
       
# ans == error in print(school)




# all three variable used here 

class Mobile:
    '''mobile name'''
    another="oppo"     // static
    def __init__(self,name,comp):
        self.a=name        // instance                  
        self.s=comp        // instance           
        print(Mobile.another)

    def addnew(self):
        x=2                // local
        print("value of x",x)

    def show(self):
        print(self.a,self.s,Mobile.another)

obj=Mobile("apple","vivo")

obj.addnew()
obj.show()

# ans =
oppo
value of x 2
apple vivo oppo



# methods=

# instance with class method = 


class Book:
    price=100
    totalpages=500
    def __init__(self,title,author):
        self.t=title
        self.a=author

    @classmethod
    def update(cls,newprice,newpagecount):
        cls.price=newprice
        cls.totalpages=newpagecount
    
    @classmethod
    def addnew(cls,author):
        cls.author2=author

    def show(self):
        print(self.t,self.a,Book.price,Book.totalpages)


obj=Book("python","jatin")
Book.update(110,550)
obj.show()

# ans =  python jatin 110 550


# static method = 

class Book:
    price=100
    totalpages=500
    def __init__(self,title,author):
        self.t=title
        self.a=author

    @classmethod
    def update(cls,newprice,newpagecount):
        cls.price=newprice
        cls.totalpages=newpagecount
    
    @classmethod
    def addnew(cls,author):
        cls.author2=author

    def show(self):
        print(self.t,self.a,Book.price,Book.totalpages)

    @staticmethod
    def Welcome():
        print("Welcome to My Website ")

    @staticmethod
    def Thanks():
        print("Visit Again")


obj=Book("python","jatin")
Book.update(110,550)
Book.Welcome()
obj.show()
Book.Thanks()
# obj.Thanks                               //  work with that also = 

# ans =
# Welcome to My Website 
# python jatin 110 550
# Visit Again


# oops properties = =======================================================================================================================

# 1 = abstraction = hiding internal process 
# abstract class is a class where atleast 1 abstract method is present 
# abc = abstract base class

from abc import ABC , abstractmethod

class Bankapp(ABC):
    def login(self):
        print("User Login ")

    def logout(self):
        print("User logout ")

    def userdata(self):
        print("User database")
    
    @abstractmethod
    def database(self):
        pass
    

class Webpage(Bankapp):
    def new(self):
        print("database accepted")

obj=Webpage()    // error
obj.database()
obj.login()
obj.logout()
obj.userdata()
# show error because we can't create obj without @abstractmethod in Webpage = 'database'

# completed with abstract method=
from abc import ABC , abstractmethod

class Bankapp(ABC):
    def login(self):
        print("User Login ")

    def logout(self):
        print("User logout ")

    def userdata(self):
        print("User database")
    
    @abstractmethod
    def database(self):
        pass
    

class Webpage(Bankapp):
    def database(self):
        print("database accepted")

obj=Webpage()
obj.database()
obj.login()
obj.logout()
obj.userdata()


# ans 
# database accepted
# User Login 
# User logout 
# User database

# 2 = Encapsulation =   wrapping up of data in single unit
# any example of class


# 3 = Inheritance = inderitence of parent's data by child
# advantages = code reusability, time saving , reduce redundency(repeatation of code ) = 

class A:
    x=10
    y=20

    def home(self):
        print("Home = ")

    def car(self):
        print("Car = ")

class B(A):
    def new(self):
        print("New Home")
  

obj=B()
obj.home()
obj.car()
obj.new()
print(A.x)
print(B.x)

# ans = 
# Home = 
# Car = 
# New Home
# 10
# 20


# Types of Inheritance = 
# 1 = single level inheritance = parent to child 

# 2 = multiple inheritance = 
# multiple parent to one child

# 3 = multilevel inheritance = 
# grand parent to parent and parent to child 

# 4 = herarichal inheritance = 
# parent to multiple child

# 5 = hybrid inheritance =  use of 2 types of inheritance
# multiple parent to child and from child to multiple grand child







# python does not support method overloading 
#  same name of method in one class 





# method over-riding = 

# 2 different class with in heritance
class Parent:
    z=12
    def home(self):
        print("Parent's property")

class Child(Parent):
    y=122
    def home(self):
        print("Carrr")

obj=Child()
obj.home()

# ans = Carrr


# super method to call super class or parent class=

class Parent:
    z=12
    def home(self):
        print("Parent's property")

class Child(Parent):
    y=122
    def home(self):
        super().home()
        print("Carrr")

obj=Child()
obj.home()

# ans =
# Parent's property
# Carrr





# Example of types of inheritance 
 
#  1 = single level inheritance = 

class Parent:
    z=12
    def home(self):
        print("Parent's property")

class Child(Parent):
    y=122
    def car(self):
        print("Carrr")

obj=Child()
print(Child.z)
obj.home()
obj.car()

# ans =
# 12
# Parent's property
# Carrr


# 2 = multiple inheritance = 

# mro method = method resolution operator =  check the parent in child parameter from left and search in there if that data is present in or not

class Parent1:
    z=12
    def home(self):
        print("Parent's 1  property")

class Parent2:
    y=122
    def home(self):
        print("Parent's 2  property")

class Child(Parent1,Parent2):
    def car(self):
        print("Child's car")

obj=Child()
obj.home()

# ans = Parent's 1  property

#        or  ==========

class Parent1:
    z=12
    def home(self):
        print("Parent's 1  property")

class Parent2:
    y=122
    def home(self):
        print("Parent's 2  property")

class Child(Parent2,Parent1):
    def car(self):
        print("Child's car")

obj=Child()
obj.home()

# ans = Parent's 2  property


