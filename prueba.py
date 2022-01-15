Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 09:44:33) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 4<10
True
>>> "hola"=="adios"
False
>>> 5<=5
True
>>> 5<5
False
>>> "a"<"b"
True
>>> "casa"<"cosa"
True
>>> edad=20
>>> edad
20
>>> edad>18
True
>>> edad>"abc"
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    edad>"abc"
TypeError: '>' not supported between instances of 'int' and 'str'
>>> 
================================= RESTART: Shell ================================
>>> 100/5
20.0
>>> type(100/5)
<class 'float'>
>>> type(7/2)
<class 'float'>
>>> type(7//2)
<class 'int'>
>>> type(7%2)
<class 'int'>
>>> type("a")
<class 'str'>
>>> type("tiza"+".")
<class 'str'>
>>> type("hola"[1+1])
<class 'str'>
>>> type(len("hola"))
<class 'int'>
>>> type(int("145"))
<class 'int'>
>>> type(float("145"))
<class 'float'>
>>> type(float(145))
<class 'float'>
>>> type(str(32))
<class 'str'>
>>> type(1+2!=3)
<class 'bool'>
>>> type(177%2==0)
<class 'bool'>
>>> type(len("nube")<=20)
<class 'bool'>
>>> 
>>> 
================================= RESTART: Shell ================================
>>> n=167/10
>>> n
16.7
>>> n=167//10
>>> n
16
>>> n=167%10
>>> n
7
>>> letra="a"
>>> letra
'a'
>>> saludo="hola"+letra
>>> saludo
'holaa'
>>> C=saludo[0]
>>> C
'h'
>>> C=saludo[1+3]
>>> C
'a'
>>> L=len(saludo)
>>> L
5
>>> C=saludo[len(saludo)-1]
>>> C
'a'
>>> menor="a"<"b"
>>> menor
True
>>> D=1!=1
>>> D
False
>>> D="cinta">="canto"
>>> D
True
>>> c="z"+"a"+"paz"[0]
>>> c
'zap'
>>> x=c[0]=="z"
>>> x
True
>>> 
================================= RESTART: Shell ================================
>>> 11-(4%2+10)
1
>>> "30"+2
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    "30"+2
TypeError: can only concatenate str (not "int") to str
>>> "30"+"2"
'302'
>>> "hola"[len("hola")]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    "hola"[len("hola")]
IndexError: string index out of range
>>> len(124)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    len(124)
TypeError: object of type 'int' has no len()
>>> "hola" [len("fin")]
'a'
>>> "hola"[11-(4%2+10)]
'o'
>>> int("4")
4
>>> int(4)
4
>>> int("z")
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    int("z")
ValueError: invalid literal for int() with base 10: 'z'
>>> int("4.")
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    int("4.")
ValueError: invalid literal for int() with base 10: '4.'
>>> 4<"f"
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    4<"f"
TypeError: '<' not supported between instances of 'int' and 'str'
>>> "palabra"="rama"
SyntaxError: can't assign to literal
>>> "palabra"=="rama"
False
>>> 