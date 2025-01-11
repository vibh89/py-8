''' Py Intro
- Von Guido Rossum -----> 1989
- official version -1991 ...21th feb 1991 
- The Complete Monty's Python Circus ---->
- C ,C++ , Perl ,Ruby (Proc Or Lang + Scripting Lang) 

Properties of Python :
1) Simple to use 
2) Freeware and open source
3) High level programming language
4) Interpreted ----->Interpreter---> PVM
5) Platform Independant
6) Poratbility
7) Dynamically Typed  ----> *******
8) Both Procedure oriented and Object Oriented
9) Extensible -----> other program ---> python file
10) Embedded
11) Rich in libraries



Where to use:
1) Desktop applications
2) Games 
3) Web Developement
4) Data Science and machine learning app
6) 

Disadv
1) Mobile applications


'''
# x = 100
# y = 0.05
# print(type(x))
# print(type(y))

# Comments in python ###########3
# print("Hello world !")  # This line prints the messsage

'''
1) single line comment  ----> #
2) Multiple line comment  ----->""" comment""" 
'''

### Escape Sequence ##########

'''
Illegal character s put up 
\" ----> "
\' -----> '
\\ -----> \
\t ------> tab space


'''

# print("Dpark\ts Soultions")


'''
Create a mountain pattern for the following:
1) ////\\\\/\\\/\
2) \/\/\///\\\
'''


######################## ################################
######## Identifiers ################
# identifiers == name


# Rules for Identifiers

'''

1) name always starts with alphabets only
2) _ Allowed -----> start ,middle,end
3) No special character is allowed ---
4) _ -----> Protected variable
5) __ ----> private variable /strictly protected variable
6) __start__ -----> special variable /magic methods /Dunder methods
7) case sensitive
8) no limits for value of identifier
9) name ---->always meaningful
'''

# 3x = "dpark solutions"
# print(3x)


# x = 1000

# X = 100

# print(id(x))   ## gives address of the variable in memory
# print(id(X))


# x = 1000

# print(x)


# x = 50

# print(x)


# x = 10

# print("now x = ",x)


# Multi words names
'''
1) camel case ---->myVariablename
2) Pascal Case ----->MyVariableName
3) sneak case ----->my_variable_name



# '''
# my_variable = 100
# print(my_variable)


# x = "apple"
# y ="banana"
# z = "mango"

# x, y, z = "apple", "banana", "mango"  # multivalue assignement

# print(x, y, z)

# a = "buldhana"
# b = "buldhana"
# c = "buldhana"

# a = b = c = "buldhana"
# print(a,b,c)


############# Keywords ##################

# import keyword as kw
# print(kw.kwlist)

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
    'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


############ Data types ##########################
'''
1) Numeric
    -- int
    -- float
    --complex
2) Sequence
    -- string
    -- list
    -- tuple
    -- set
    --frozenset
    -- bytes
    -- bytesarray
    --range
3) Boolean
    -- True
    -- False
4) None
    -- none

5) mapping
    --dictionary

'''


##### Numeric ###################
# print(),id(),type()
# x = 10
# print(x)
# print(type(x))
# y = 1000000000
# print(type(y))

# z = 0.0000000000000005
# print(type(z))

# v = 2 + 3j
# print(type(v))

# print(v.real)
# print(v.imag)


# x = 5   #int ----decimal
# print(bin(x)) #0b101 -----> b binary
# f = bin(x)


# print(type(f))

# print(oct(x))  #0o5  ----> o  octal

# print(hex(x)) #0x5  ----> x hexadecimal


# c = 2 + 3j

# print(type(c))

# y = int(c)
# print(y)


# d = 1.421
# y = int(d)
# print(y)


# d = 5
# print(complex(d))


# e = 0.46
# print(complex(e))


########################### String #############################
'''
- group of characters ----alphabets, numbers, special char
- insertion order is maintained
- immutable in nature  ----CRUD operation (create,read, update and delete)
- homogenous + heterogenous
- not growable in nature
- indexing 



'''
# s = """dpark solutions"""
# print(s)
# print(type(s))

# d = "yash"

# print(len(d))  # length of str

# fetching of characters from string w.t.h.of(indexing)
# print(d[0])
# print(d[1])
# print(d[2])
# print(d[3])
# print(d[4])

############# Slicing ###############

# d = "yash"
d = "I am a good boy."

# print(d[0:2])
# print(d[0:3])
# print(d[0:4])
# print(d[0:5])

# print(len(d))

# print(d[:])  # 0 to len(str)

# print(d[0:len(d)])
# print(d[3:10])
# print(d[2:5])   #positive slicing
# print(d[0:100])

# print(d[5:2])

d = "I am a good boy."

# print(d[-1])
# print(d[-2])
# print(d[-3])
# print(d[-4])

# print(d[-17])

# print(d[-5:-3])
# print(d[-16:])

# Advanced slicing /Extended slicing

d = "I am a good boy."


# print(d[0:16:2])   # stepping index


# print(d[-1:-17:-1])   # stepping index
# print(d[-1:-17:-3])   # stepping index


#############################################
# print, id,type,len, dir


# s1 = ""
# print(type(s1))
# print(dir(s1))  # gives you list of variables and functions

##################### List ####################
'''
-- index based operation
-- mutable ---CRUD operation
-- homogenous + Heterogenous
-- insertion order is maintained
-- duplicates are allowed
--denoted by square brackets --[]
-- growable in nature
'''


l = [1,2,3,4,"a",0.5,1,1,1,1,1]
# print(len(l))
# print(type(l))
print(l[0])  # fetching of elements from list
print(l[1])