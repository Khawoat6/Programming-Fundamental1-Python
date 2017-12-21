
' CODE PYTHON Application Programming (Wesley J.Chun) '



' PYTHON HOW TO PROGRAM '

Escape Sequence       Desciption
 \n                     newline
 \t                     horizontal
 \r                     carriage return
 \b                     backspace
 \a                     alert
 \\                     backslash
 \"                     double quote
 \'                     single quote

Python                Arithmetic
operation             operator
 +                      addition
 -                      subtraction
 *                      mutiplication
 **                     exponentiation
 /                      division
 //
 %                      modulus

Operator(s)           Operation(s)
 ()                     parenthese
 **                     exponentiation
 * / // %               multiplication
                        division
                        modulus
 + -                    addition
                        subtraction

Python keywords
 and    continue    else    for     import  not     raise
 assert def         except  from    in      or      return
 break  del         exec    global  is      pass    try
 class  elif        finally if      lambda  print   while


TERMINOLOGY
action/decision model of programming                function
action sysbol                                       goto elimination
algorithm                                           goto statement
and (logical AND) operator                          if selection structure
augmented addition assignment                       if/elif/else selection structure
augmented assignment statement                      if/else
break statement                                     increment argument of range function
continue statement                                  initialization phase
control structure                                   int function
end argument of range function                      nonfatal logic error
exception handling                                  not (logical NOT) operator
first refinement                                    or (logical OR) operator
float function                                      pass keyword
for repetition structure                            processing phase
int function                                        true divition
left-to-right evaluation                            type function
id function                                         string of characters
comment                                             precision
conversion specifier                                .py extension
data member                                         .pyw extension
debugging                                           raw_input function
acos function                                       fans function
asin function                                       factorial
atan function                                       fibonacci series
base case                                           floor function
ceil function                                       function body
cos function                                        function definition
def statement                                       function name
default argument                                    function parameter
dir function                                        global keyword
exp function                                        globals function
expression                                          hypot function
identifier                                          _name_
import keyword                                      package
iterative function                                  parameter list
local namespace                                     random module
local variable                                      randrange function
locals function                                     recursion
log function                                        recursive function
log10 function                                      return keyword
"_main_"                                            scope
main program                                        sin function
math module                                         sqrt function
module                                              tan function
append method of list                               bracket operator ([])
comma (,)                                           m-by-n sequence
dictionary                                          name(sequence)
element                                             out-of-range error message
emply curly braces {}                               packed
emply dictionary                                    packing a tuple
emply list                                          pass-by-object-reference
emply quotes                                        pass-by-value
emply parentheses ()                                pass-by-reference
emply square brackets []                            popitem method of dictionary
emply string                                        positin number
emply tuple                                         row
for structure                                       search
in keyword                                          slice a sequence
index                                               slicikng operator ([:])
index method of list                                sort
list                                                zeroth element




Operators                               Type
 ()                                      parenthese
 []                                      subscipt
 **                                      exponentiation
 * / // %                                multiplicative
 + -                                     additive
 < <= > >=                               relational
 == != <>                                equality
 and                                     logical AND
 or                                      logical OR
 not                                     lpgical NOT

Method
append(item)
count(element)
extend(newList)
index(element)
insert(index,item)
pop([index])
remove(element)
reverse()
sort([compare-function])
clear()
copy()
get(key[,returnValue])
has_key(key)
item()
keys()
popitem()
setdefault(key[,dummyValue])
update(newDictionary)
values()
iterkeys()
iteritems()
itervalues()


Number-Theoretic and Representation function
math.ceil(x)  ให้ค่าปัดขึ้นของ x
math.floor(x) ให้ค่าปัดลงของ x
math.factorial(x) หาแฟคตอเรียลของ x
math.exp(x)   ให้ค่า e ยกกำลัง x
math.log(x,base) ได้ลอการิทึมของ x ฐาน base
math.sqrt(x)  ให้ค่ารากที่สองของ x
math.pow(x,y) x ยกกำลัง y

Constant (ค่าคงที่ต่างๆ)
math.pi คือค่า π  มีค่าเท่ากับ 3.14
math.e  คือค่า e natural log มีค่าเท่ากับ 2.71

import math
math.exp(x)                     e**x
math.log(x,base)                log base x
math.sqrt(x)                    รูด 2
math.sin(x)                     x in radians
math.cos(x)                     x in radians
math.degree(x)                  x in radians
math.radians(x)                 x in degrees
math.pi                         พาย = 3.141592...
math.e                          e = 2.718281

New File		Ctal+N
Open		Ctal+O
Save		Ctal+S
Save As...	Ctal+Shift+S
Print Window	Ctal+P
Close		Ctal+F4
Exit		Ctal+Q
Undo		Ctal+Z
Redo		Ctal+Shift+Z
Cut		Ctal+X
Copy		Ctal+C
Paste		Ctal+V
Select All		Ctal+A
Restart Shell	Ctal+F6
Run		F5


#Error

Exception
SystemExit
ArithmeticError
FloatingPointError
OverflowError
ZeroDivisionError
AssertionError
AttributeError
EnvironmentError
IOError
OSError
EOFError
ImportError
LookupError
IndexError
KeyError
MemoryError
NameError
RuntimeError
SyntaxError
TabError
IndentationError
SystemError
TypeError
ValueError
UnicodeError

#เลขฐานสอง   เลขฐาน 16   เลขฐาน 10 
0000            0           0      
0001            1           1    
0010            2           2
0011            3           3
0100            4           4
0101            5           5
0110            6           6
0111            7           7
1000            8           8
1001            9           9
1010            A           10
1011            B           11
1100            C           12
1101            D           13
1110            E           14
1111            F           15















#Function Built-in : เป็นฟังก์ชันที่สามารถเรียกใช้ได้เลย โดยไม่ต้องประกาศด้วยประโยค import
ads(x)                              #ทำหน้าที่คำนวณหาค่า absolute ของตัวแปล x
apply(function,arge[,keywords])     #ใช้สำหรับอาร์กิเมนต์ที่เป็นชนิดข้อมูลชนิดทูเปิล
buffer(object[,offset[size]])       #ใช้สำหรับสร้างบัพเฟอร์หรือที่พักข้อมูงชั่วคราว
callable(object)                    #ใช้ตรวจสอบว่าออปเจกต์นั้นๆสามารถเรียกใช้งานได้หรือไม่
chr(i)                              #ทำหน้าที่เเสดงรหัสแอสกี้ให้ปรากฎบนจอภาพ
coerce(x,y)                         #ใช้สำหรับแปลงตัวเลขสองจำนวนให้เป็นชนิดข้อมูลทูเปิล
compile(string,filename,kind)       #ทำหน้าทีี่คอมไพล์สตริงที่เป็นซอร์ซโค้ดหรือคำสั่งไพธอน
complex(real[,imag])                #ทำหน้าที่แปลงเลขให้อยู่ในฟอร์มเลขจำนวนเชิงซ้อน
delattr(object, name)               #ใช้สำหรับลบ attribute ของ object ใช้กับฟังก์ชัน setattr()
dir([object])                       #ทำหน้าที่ตรวจสอบว่าปัจจุบันนั้นตัวแปรและออปเจกต์ใดบ้างที่กำลังถูกโหลดใช้งานในหน่วยความจำ
divmod(a,b)                         #ทำหน้าที่คืนค่าการหารและการหารเอาเศษ
eval(expreesion[,globals[,locals]]) #ใช้สำหรับประมวลผลคพสั่งที่อยู่ในรูปแบบสตริงหรือข้อมูลในรูป byte code ที่ผ่านขั้ตอนการคอมไพล์มาแล้ว
execfile(file[,globals[,locals]])   #ทำหน้าที่คล้ายกับคำสั่ง exec แต่เป็นการกระทำกับไฟล์

















