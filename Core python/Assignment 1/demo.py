print("Hello Adinath!")
print("Welcome to Python")

###Datatypes
##1. Numeric
#int
i=12
print(type(i))

#float
num=1.23
print(type(num))

#complex
num= 3+ 2j
print(type(num))


##Text
#String('str')
a='python'
print(type(a))

##Sequence
#list
li=[1,2,3,4]
print(type(li))

#tuple
tu=(10,20,40,35,60)
print(type(tu))

#range
r=range(1,10)
print(type(r))

##mapping
#dictionary
dict={1:'python', 2:'Java', 3:'C++'}
print(type(dict))

##set_type
#set
s1={10,100,1000,10000}
print(type(s1))

#frozonset
f1=frozenset({10,20,30,40})
print(type(f1))

##Boolean
#true
va1=True
print(type(va1))

#false
val2=False
print(type(val2))

##None_type
val=None
print(type(val))

##Binary_datatypes
#bytes
data=b'hello'
print(type(data))

#bytearray
data=bytearray(b'hello')
print(type(data))

#memory_view
data=b'python'
view=memoryview(data)
print(type(view))