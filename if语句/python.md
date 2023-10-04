### python

==字符串==

``` python 
name="ada lovelace"
print(name.title())#将每个单词的首字母大写
print(name.upper())#全大写
print(name.lower())#全小写
```

方法是python可对数据执行的操作，name后面的（.）是让变量name执行方法title（）指定的操作。每个方法后面都跟着圆括号，这是因为方法通常需要额外的信息来完成其工作。这种信息死在圆括号内提供的，title（）不需要额外的信息，因此是空的。

``` python
在字符串中使用变量
first_name="ada"
last_name="lovelace"
full_name=f"{first_name}{last_name}"
print(full_name)

```

要在字符串中插入变量的值，可在前引号前加上字母f，再将要插入的变量放在花括号内。这样，当python显示字符串时，将把每个变量都替换成其值。
这种字符串名为f字符串。

==使用制表符或换行符来添加空白==

``` python
print("python")
print("\tpython")#添加制表符
print("langguages:\nc\nc++\njava\npython")#换行
print("langguages:\n\tc\n\tc++\n\tjava\n\tpython")#换到下一行，并加一个制表符。
```

``` py
>>> favorite_language='python '
>>> favorite_language
'python ' 		#询问这个变量的值，可看到末尾的空格
>>> favorite_language.rstrip()
'python'		#多余的空格被删除
>>> favorite_language
'python '		#空格还在
>>> favorite_language=favorite_language.rstrip()	#将删除结果关联到变量
>>> favorite_language
'python'

>>>favorite_language=' python '
>>>favorite_language.rstrip()
' python'		#删右边的
>>>favorite_language.lstrip()
'python '		#删左边的
>>>favorite_language.strip()
'python'		#删两边
```

==数==

python将所有带小数点的数称为浮点数

书写很大的数时可以用下划线将其中的数字分组，更易读，打印时不会打印下划线

两个数相除的时候就算可以除

``` python
>>>name=14_0000_00000_000
>>>print(name)
 1400000000000
```

同时给多个变量赋值

``` python
x,y,z=0,0,0
print(x,y,z)

```

``` python	
10 ** 2//100
2 ** 4//16
**代表乘方
```



常量类似于变量，其值在程序的生命周期保持不变，python没有内置的常量类型，但python程序员会使用全大写来指出应将某个变量视为常量，其值应始终不变。

``` python
MAX_CONNECTIONS=5000
```

==列表==

``` python 
bicycles= ['tiek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())#可以用字符串方法
print(bicycles[-1])#倒数第一个元素
```

修改列表元素

``` py
motorcycles.append('ducati')#添加在末尾
motorcycles.insert(0,'ducati')#insert可以在任何位置插入元素，需指定新元素的索引
del motorcycles[0]#删除列表的元素
popped_motorcycles=motorcycles.pop()#pop方法删除列表末尾的元素，并让你接着使用它
popped_motorcycles=motorcycles.pop(1)#pop方法也可以弹出列表中任意位置的元素，只需在括号中加上索引

```

根据值删除元素

``` python
motorcycles.remove('suzuki')
```

用remove()删除元素时，也可接着使用它的值，下面删除‘dacati’并打印删除原因

``` python
motorcycles=['haoda','yamaha','suzuki','dacati']
too_expensive='dacati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
```

使用方法sort（）对列表永久排序

``` python
cars=['bmw','audi','toyota','subaru']
cars.sort()#按字母顺序排序
print(cars)
//['audi', 'bmw', 'subaru', 'toyota']
cars.sort(reverse=True)#按字母顺序相反排序
//['toyota', 'subaru', 'bmw', 'audi']
```

使用函数sorted()对列表临时排序

``` python
sorted(cars)
以特定的顺序呈现它们，同时不影响原始顺序
```

倒着打印列表

``` python
cars.reverse()
print(cars)
反转列表
```

确定列表的长度

``` python
len(cars)
num=len(cars)#4
```

for循环

``` python
motorcycles=['haoda','yamaha','suzuki','dacati']
for person in motorcycles:
    print(person)
    执行更多操作
    print(f"{person.title()}, that was a great trick")
 //Haoda, that was a great trick
Yamaha, that was a great trick
Suzuki, that was a great trick
Dacati, that was a great trick   
```

在for循环后面没有缩进的代码只执行一次

==创建数值列表==

使用函数range()

``` python
for value in range(1,5):
    print(value)//1,2,3,4
 range()只打印1~4，函数range()让python从指定的第一个值开始数，并到第二个值停止。所有不会输出这个值（这里指5）
要打印1~5
range(1,6)
```

使用range()创建数字列表

``` python
numbers = list(range(1,6))
print(numbers)
使用函数range时还可指定步长，可给这个函数三个参数，
打印1~10的偶数
even_number=list(range(2,11,2))
print(even_number)
乘方运算
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)
更简洁
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)
```

对数字列表执行简单的统计计算

```  python
>>> digits= [1,3,5,2,6,7,9,8,0]
>>> min(digits)
0
>>> max(digits)
9
>>> sum(digits)
41
>>>
```

列表解析

``` python
squares=[value**2 for value in range(1,11)]
print(squares)
要使用这种语法，首先指定一个描述性的列表名，如 squares。然后，指定一个左方括号，并定义一个表达式，用于生成要存储到列表中的值。在这个示例中，表达式为value**2，它计平方值。接下来，编写一个for循环，用于给表达式提供值，再加上右方括号。在这个示例中for循环为 for value in range(1,11)，它将值1-10提供给表达式value**2。请注意，这里for语句末尾没有冒号。
```

==使用列表的一部分==

切片：处理列表的部分元素，python称之为切片

要创建切片，可指定要使用的第一个元素和最后一个元素的索引。要输出列表前三个元素，需指定索引0和3

``` python
players=['charles','martina','michael','florence','eli']
print(players[0:3])//前三个元素
print(players[1:4])//从第二个元素开始到第四个
print(players[:4])//从零开始
print(players[2:])//从第三个到末尾
print(players[-3:])//倒数三个


```

复制列表

``` python
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]//复制列表
区别两个列表
my_foods.append('ice cream')
friend_foods.append('cannoli')
print(my_foods)
print(friend_foods)

```

==元组==

python将不能修改的值称为不可变的，而不可变列表被称为元组

``` python
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
严格的说，元组是由逗号标识的，圆括号只是让元组看起来更整洁·更清晰。要定义一个只包含一个元素的元组，必须在这个元素后面加上逗号：
my_t=(3,)

```

修改元组变量

不能修改元组的元素，但可以给从存储元组的变量赋值。因此，如果要修改前面的元组，可从新定义整个元组

``` python
dimensions = (200,50)
for dimenison in dimensions:
    print(dimenison)
dimensions = (400,100)
for dimenison in dimensions:
    print(dimenison)
```

==if语句==

``` python
cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

```

条件测试

``` python
car = 'audi'
car == 'Audi'
false

car = 'Audi'
car.lower() == 'audi'
True


```

检查多个条件

``` python
1.使用and检查多个条件
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 and age_1 >= 21
False
>>> age_1 = 22
>>> age_0 >= 21 and age_1 >= 21
True
为改善可读性
(age_0 >= 21) and (age_1 >= 21)

2.使用or检查多个条件
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 or age_1 >= 21
True
>>> age_0 = 18
>>> age_0 >= 21 or age_1 >= 21
False
```

检查特定值是否包含在列表中

``` python
判断特定值是否包含，可使用关键字in
>>> requested_toppings = ['mushrooms','onions','pineapple']
>>> 'mushrooms' in requested_toppings
True
>>> 'ion' in requested_toppings
False
```

检查特定值是否不包含在列表中

```  python
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
marie不在列表banned_users中，因此他将看到一条邀请他发表评论的消息    
```

布尔表达式

``` python
gaem_active = True
can_edit = False
```

if-else语句

``` python
age = 19
if age >=18:
    print("you are old enough to vote!")
else:
    print("sorry, you are too youung to vote")

```

if-elif-else语句

``` python
age=12
if age <=4:
    print("you free")
elif age <18:      //elif代码其实是另一个if测试
    print("you need pay 25")
else:
    print("you need pay 40")
```

使用if语句处理列表

``` python
requested_toppings = ['mushrooms','green peppers','exxtra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers': //如果没有青椒
        print("sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")
```

确定列表不是空的

在if语句中将列表名用作条件表达式时，python将在列表至少包含一个元素时，返回Ture,并在列表为空的时候返回Flase.如果requested_toppings不为空，就运行前一个示例相同的for循环

``` python
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print(f"Adding {requested_topping}.")
else:
    print("Are you sure you want a plain pizza?")
```

使用多个列表

``` python

available_toppings = ['mushrooms','olices','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")
```















































