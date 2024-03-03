
-----------------------------------------------------------------
## Python OOPS

-----------------------------------------------------------------
### Class 
  
A class is a blueprint for creating objects. It defines the properties and methods that all objects of that class will have. 

## self 
is a convention used within the methods of a class to refer to the instance of the class itself. It is the first parameter in the method definition,  
but when you call the method, you don't need to pass a value for self explicitly; Python takes care of that for you.


In object-oriented programming, the term "current instance" refers to an object that is currently being operated on or accessed by a method or function. Each object created from a class is considered an instance of that class. For example, if you have a class called Car, you can create multiple Car objects, each representing a different car.

When you call a method on an object, the method typically operates on the data of that object. The this keyword in C#, or the self keyword in Python, is a reference to the current instance of the class within a method.

You can use give any name in place of self, it will work as first passed variable is considered as this irrespective of name. 
So, while you can use any valid variable name in place of self, it's best to stick with the convention of using self to make your code more readable and maintainable.

### Constructors __init__

Always called when object is being created

This default constructor initializes the object with no arguments. It is called the __init__ method.

In Python, a class can have only one constructor, which is the __init__ method. However, you can achieve the effect of having multiple constructors by using default values for the parameters of the __init__ method.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.make} {self.model} starts its engine.")

    def stop_engine(self):
        print(f"The {self.make} {self.model} stops its engine.")

    def drive(self):
        print(f"The {self.make} {self.model} drives forward.")

my_car = Car("Toyota", "Camry", 2020)
print(my_car.make)  # Output: Toyota
print(my_car.year)  # Output: 2020

my_car.start_engine()  # Output: The Toyota Camry starts its engine.
my_car.drive()         # Output: The Toyota Camry drives forward.
my_car.stop_engine()   # Output: The Toyota Camry stops its engine.
```

-----------------------------------------------------------------
### Decorators 
  
Decorators in Python are a powerful tool used to modify or extend the behaviour of a callable (functions, methods, or classes) without modifying its source code. They are a way of wrapping a function or method with another function or method, which allows you to add functionality to the original function or method.

In Python, decorators are implemented using the @ symbol followed by the name of the decorator function or class. The decorator is placed above the function or method definition, like this:

```python
@decorator
def function():
    pass

#or

class MyClass:
    @decorator
    def method(self):
        pass

```

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
``` 

```python
## Decorators can also take arguments. For example:
def repeat(n):
    def decorator(func):
        def wrapper():
            for _ in range(n):
                func()
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()

# Hello!
# Hello!
# Hello!

``` 

```python
def my_decorator(*args, **kwargs):
    def decorator(func):
        def wrapper():
            print(f"Decorator arguments: {args}, {kwargs}")
            func()
        return wrapper
    return decorator

@my_decorator(1, 2, 3, a='hello', b='world')
def say_hello():
    print("Hello!")

say_hello()

# Output
# Decorator arguments: (1, 2, 3), {'a': 'hello', 'b': 'world'}
# Hello!

```	

-----------------------------------------------------------------
### Getters and Setters 
  
Getters and setters are methods used to access and modify the private attributes of a class in Python. They are used to provide controlled access to the attributes of an object. Getters are used to retrieve the value of an attribute, while setters are used to modify the value of an attribute.

In Python, you can create getters and setters using the @property decorator and the @attribute_name.setter decorator.

```python

class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        self._make = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

my_car = Car("Toyota", "Camry", 2020)
print(my_car.make)  # Output: Toyota

my_car.make = "Ford"
print(my_car.make)  # Output: Ford
```

In this example, the Car class has private attributes _make, _model, and _year. These attributes are accessed and modified using the make, model, and year properties, which are decorated with the @property decorator. The make, model, and year properties are getters, and the corresponding @attribute_name.setter decorators are used to define setters for these properties.


-----------------------------------------------------------------
### Inheritance
  
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (subclass) to inherit the behavior and attributes of another class (superclass).  
In Python, you can create a subclass by specifying the superclass in parentheses after the subclass name.

```python

# Base Class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")

#Derived Class 
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def drive(self):
        print("Car is driving.")


my_car = Car("Toyota", "Camry", 2020, 4)
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Camry
print(my_car.year)   # Output: 2020
print(my_car.doors)  # Output: 4
my_car.start_engine()  # Output: Engine started.
my_car.drive()         # Output: Car is driving.
my_car.stop_engine()   # Output: Engine stopped.
```

In this example, the Vehicle class is the superclass, and the Car class is the subclass. The Car class inherits the behavior and attributes of the Vehicle class using the super() function in the __init__ method.

-----------------------------------------------------------------
### Access Modifiers
  
It's important to note that Python does not have true access modifiers. The single underscore and double underscore naming conventions are just conventions, and it is still possible to access protected and private members using name mangling. Additionally, it is generally considered better practice to use public variables and methods whenever possible.


Public: By default, all class members in Python are public and can be accessed from outside the class.

Protected: In Python, you can use a single underscore (_) at the beginning of a variable or method name to indicate that it is protected. 
Protected members can be accessed from outside the class, but it is considered a convention that they should not be modified.
Can be accessed by Derived classes. 

Private: In Python, you can use a double underscore (__) at the beginning of a variable or method name to indicate that it is private. Private members cannot be accessed from outside the class.

```python
class MyClass:
    def __init__(self):
        # Public variable
        self.my_variable = 10  

        # Protected variable
        self._my_protected_variable = 20

        # Private variable
        self.__my_private_variable = 30

    # Public method
    def my_method(self):
        print("This is a public method.")

    # Protected method
    def _my_protected_method(self):
        print("This is a protected method.")

    # Private method
    def __my_private_method(self):
        print("This is a private method.")



############# Create an instance of MyClass
my_object = MyClass()

# Access and modify public variable
print(my_object.my_variable)  # Output: 10
my_object.my_variable = 40
print(my_object.my_variable)  # Output: 40

# Access and modify protected variable (not recommended)
print(my_object._my_protected_variable)  # Output: 20
my_object._my_protected_variable = 50
print(my_object._my_protected_variable)  # Output: 50

# Access and modify private variable (not recommended)
print(my_object._MyClass__my_private_variable)  # Output: 30
my_object._MyClass__my_private_variable = 60
print(my_object._MyClass__my_private_variable)  # Output: 60

# Call public method
my_object.my_method()  # Output: This is a public method.

# Call protected method (not recommended)
my_object._my_protected_method()  # Output: This is a protected method.

# Call private method (not recommended)
my_object._MyClass__my_private_method()  # Output: This is a private method.
```

-----------------------------------------------------------------
### Name mangling 
  

Name mangling is a technique used in Python to make private class members (variables and methods) less accessible from outside the class. It works by prefixing the name of the private member with two underscores (__). This causes the interpreter to rename the member in a way that makes it harder to access, but not impossible.

The purpose of name mangling is to discourage direct access to private members and to avoid name clashes with subclasses that may use the same name for their own private members.

```python
class MyClass:
    def __init__(self):
        self.__my_private_variable = 10  # Private variable

    def __my_private_method(self):
        print("This is a private method.")


#########################

my_object = MyClass()
# Private members can not be accessed directly 
print(my_object.__my_private_variable)  # Output: Will throw error 

# Access and modify private variable using name mangling
print(my_object._MyClass__my_private_variable)  # Output: 10
my_object._MyClass__my_private_variable = 20
print(my_object._MyClass__my_private_variable)  # Output: 20

# Call private method using name mangling
my_object._MyClass__my_private_method()  # Output: This is a private method.

```

In this example, __my_private_variable and __my_private_method are private members of the MyClass class. They are accessed and modified using name mangling, which involves prefixing the member name with _MyClass__.

It's important to note that name mangling is a convention, not a security feature. It is still possible to access private members using their mangled names, although this is generally not recommended. Name mangling is primarily intended to discourage direct access to private members and to avoid name clashes with subclasses.


-----------------------------------------------------------------
### __dir__() 
  
Will show all details of that class   
```python
print(obj.__dir__())
```

-----------------------------------------------------------------
### Static Methods in Python
  
Static methods in Python are functions within a class that are not bound to any specific instance of that class. They are independent of the class's state and do not have access to the class's attributes or methods. They are defined using the @staticmethod decorator.

Need not to pass self in static methods as it don't refer instance
```python

class MyClass:
    @staticmethod
    def my_static_method(x, y):
        return x + y

# You can call the static method without creating an instance of the class
result = MyClass.my_static_method(3, 5)
print(result)  # Output: 8
```

-----------------------------------------------------------------
### property()
  
In Python, you can use the property() function to create a property without a setter. A property without a setter is read-only. Here's an example:
```python
class MyClass:
    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    x = property(get_x, None) # no setter
```

you can declare a property without values by using the property decorator. This allows you to define custom getter, setter, and deleter methods for a property. 

```python
class MyClass:
    def __init__(self):
        self._my_property = None

    @property
    def my_property(self):
        return self._my_property

    @my_property.setter
    def my_property(self, value):
        self._my_property = value

    @my_property.deleter
    def my_property(self):
        del self._my_property

# Usage
obj = MyClass()
obj.my_property = "Hello, world!"
print(obj.my_property)  # Output: Hello, world!

```

-----------------------------------------------------------------
### Instance variables vs Class variables 
  
Instance Variables:

Instance variables are variables that belong to a specific instance of a class. They are defined inside a method and are prefixed with self..  
Each instance of the class has its own copy of instance variables, which means that changes made to one instance's instance variables do not affect other instances of the class.  
Instance variables are typically used to store data that is unique to each instance of the class.

```python
class MyClass:
    def __init__(self, x):
        self.x = x  # `x` is an instance variable

obj1 = MyClass(5)
obj2 = MyClass(10)

print(obj1.x)  # Output: 5
print(obj2.x)  # Output: 10
```

Class Variables:

Class variables are variables that are shared among all instances of a class. They are defined outside of any method and are prefixed with the class name.  
Changes made to class variables are reflected in all instances of the class.  
Class variables are typically used to store data that is shared among all instances of the class.  

```python
class MyClass:
    class_var = 0  # `class_var` is a class variable

    def __init__(self, x):
        self.x = x  # `x` is an instance variable

obj1 = MyClass(5)
obj2 = MyClass(10)

print(obj1.class_var)  # Output: 0
print(obj2.class_var)  # Output: 0

MyClass.class_var = 100

print(obj1.class_var)  # Output: 100
print(obj2.class_var)  # Output: 100
```

You can define instance variables without initializing them at the time of class declaration. This is particularly useful when you need to create an instance variable dynamically, based on certain conditions or user input.

```python

class MyClass:
    def __init__(self):
        pass

instance = MyClass()
instance.new_variable = "Hello World"

print(instance.new_variable)  # Output: Hello World

```

In this example, we define a class MyClass with an empty __init__ method (which means it does nothing). We then create an instance of MyClass and dynamically add a new instance variable new_variable to it. This variable is assigned the value "Hello World". When we print instance.new_variable, it prints the value of the new_variable instance variable, which is "Hello World".

So, yes, you can define instance variables in Python without initializing them at the time of class declaration. You can add them dynamically to instances of the class later on.


-----------------------------------------------------------------
### Class Methods
  
In Python, class methods are methods that are bound to the class, rather than the instance of the class. They are defined using the @classmethod decorator, and their first parameter is always the class itself, typically named cls.  

The @classmethod decorator in Python is used to create class methods. A class method is a method that is bound to the class rather than an instance of the class. This means that the method can be called on the class itself, rather than on an instance of the class.

To define a class method, you use the @classmethod decorator before the method definition. The first parameter of the method should be cls, which is a reference to the class itself. You can then use cls to access class-level variables and methods within the class method.

```python

class MyClass:
    class_variable = "Hello, world!"

    @classmethod
    def class_method(cls):
        print(cls.class_variable)

MyClass.class_method()  # Output: Hello, world!

```

Class methods are often used as alternative constructors, providing different ways to create instances of a class. This is useful when you want to create an instance of a class using parameters that are different from those used by the primary constructor.

```python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2024
        age = current_year - birth_year
        return cls(name, age)

    @classmethod
    def from_birth_year_and_age(cls, name, birth_year, age):
        return cls(name, age)

# Using the primary constructor
person1 = Person("Alice", 25)

# Using the class method as an alternative constructor
person2 = Person.from_birth_year("Bob", 1990)

# Using the other class method as an alternative constructor
person3 = Person.from_birth_year_and_age("Charlie", 1985, 39)

print(person1.name, person1.age)  # Output: Alice 25
print(person2.name, person2.age)  # Output: Bob 34
print(person3.name, person3.age)  # Output: Charlie 39
```

In each case, the __init__ method is called to initialize the instance attributes name and age. The only difference between using the primary constructor and the class methods is that the class methods allow you to create instances using different sets of parameters.

-----------------------------------------------------------------
### Get Details -->> dir, __dict__ and help method
  
dir() function:
The dir() function returns a list of valid attributes and methods of an object. It can be used with any object, including modules, classes, and instances. When called without arguments, it returns a list of names in the current local scope.

```python

import math

print(dir(math))  # Output: ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

class MyClass:
    def __init__(self):
        self.attribute1 = 'value1'
        self.attribute2 = 'value2'

my_instance = MyClass()

print(dir(my_instance))  # Output: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute1', 'attribute2']

```

__dict__ attribute:
The __dict__ attribute is a dictionary that contains all the attributes and their values of an object. It can be useful for inspecting the attributes of an object at runtime.

```python

class MyClass:
    def __init__(self):
        self.attribute1 = 'value1'
        self.attribute2 = 'value2'

my_instance = MyClass()

print(my_instance.__dict__)  # Output: {'attribute1': 'value1', 'attribute2': 'value2'}

```

help() function:
The help() function is used to get information about an object, module, function, or class. When called with an object or module as an argument, it prints a help message with information about the object's methods and attributes. When called without arguments, it starts an interactive help session.

```python
import math

help(math)  # This will print help information about the math module

help(math.sqrt)  # This will print help information about the sqrt function in the math module

```

Note that you don't always have to use super, especially if you're not dealing with multiple inheritance or if you're not overriding methods.

-----------------------------------------------------------------
### Super
  
"super" is a built-in function that allows you to access methods and properties of a base or superclass from a derived or subclass. It's often used in the context of inheritance, where a class inherits from another class, and the derived class wants to call a method from the base class.

```python
class BaseClass:
    def __init__(self, x):
        self.x = x

    def display(self):
        print("BaseClass:", self.x)

class DerivedClass(BaseClass):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def display(self):
        super().display()
        print("DerivedClass:", self.y)

obj = DerivedClass(10, 20)
obj.display()

# Output:
# BaseClass: 10
# DerivedClass: 20

```
Note that you don't always have to use super, especially if you're not dealing with multiple inheritance or if you're not overriding methods.

-----------------------------------------------------------------
### Magic/Dunder Methods in Python 
 
Magic (or dunder) methods in Python are special methods that are surrounded by double underscores ("__") at the beginning and end of their names. They are called "magic" or "dunder" because they have special behavior or significance in Python. These methods are used to implement specific functionality and are called automatically by Python in certain situations.

Here are some common magic methods and their uses:

1. `__init__(self, ...):` This is the constructor method, which is called when an instance of the class is created. It is used to initialize the object's attributes.

2. `__repr__(self):` This method is called when the `repr()` function is used or when the object is printed. It should return a string that represents the object in a way that can be used to recreate the object.

3. `__str__(self):` This method is called when the `str()` function is used or when the object is converted to a string using the `print()` function. It should return a human-readable string representation of the object.

4. `__len__(self):` This method is called when the `len()` function is used to get the length of the object.

5. `__getitem__(self, key):` This method is called when an item is accessed using square brackets (`[]`). It should return the value associated with the given key.

6. `__setitem__(self, key, value):` This method is called when an item is assigned to a key using square brackets (`[]`). It should set the value associated with the given key to the given value.

7. `__delitem__(self, key):` This method is called when an item is deleted using the `del` keyword. It should delete the item associated with the given key.

8. `__iter__(self):` This method is called when the object is used in a `for` loop. It should return an iterator object that can be used to iterate over the object's elements.

9. `__next__(self):` This method is called when the `next()` function is used to get the next element in the iteration. It should return the next element in the iteration or raise a `StopIteration` exception if there are no more elements.

10. `__contains__(self, item):` This method is called when the `in` keyword is used to check if an item is in the object. It should return `True` if the item is in the object, and `False` otherwise.

These are just a few of the many magic methods in Python. They allow you to define custom behavior for your objects and make your code more expressive and readable.


-----------------------------------------------------------------
### Method Overriding in Python
  
Method overriding in Python refers to the process of redefining a method in the subclass that is already defined in the superclass. This allows the subclass to provide a specific implementation of the method that is different from the implementation in the superclass.

When a method is overridden in a subclass, the method in the subclass takes precedence over the method in the superclass. This means that when an object of the subclass is created and the overridden method is called, the implementation of the method in the subclass is executed instead of the implementation in the superclass.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Create an object of the Dog class
dog = Dog()

# Call the speak method of the Dog class
dog.speak()  # Output: Dog barks
```

-----------------------------------------------------------------
### Method Overloading in Python
  
In Python, however, you cannot directly overload methods in the same way. If you define two methods with the same name in a class, the second definition will simply overwrite the first one. This is because Python uses dynamic typing and duck typing rather than static typing.

However, you can achieve similar functionality in Python using default arguments or variable-length arguments. Here's an example of how you might simulate method overloading in Python:

```python

class MyClass:
    def my_method(self, x, y=None):
        if y is None:
            # Do something with x
            print(f"x: {x}")
        else:
            # Do something with x and y
            print(f"x: {x}, y: {y}")

obj = MyClass()

# Call my_method with one argument
obj.my_method(10)  # Output: x: 10

# Call my_method with two arguments
obj.my_method(10, 20)  # Output: x: 10, y: 20
```

-----------------------------------------------------------------
### Operator Overloading in Python
  
Operator overloading in Python refers to the ability to define custom behavior for built-in operators, such as addition (+), subtraction (-), multiplication (*), and so on. This allows you to use operators with custom objects and define what happens when those operators are applied to instances of your class.

```python

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Create two Vector objects
v1 = Vector(1, 2)
v2 = Vector(3, 4)

# Add the two Vector objects
result = v1 + v2
print(result)  # Output: Vector(4, 6)
```

In this example, the Vector class defines a custom \__add__ method that takes another Vector object as an argument and returns a new Vector object with the sum of their x and y components. When we add two Vector objects together using the + operator, Python calls the __add__ method of the first object and passes the second object as an argument.

Here are some other common operators that can be overloaded in Python:

## Commonly Overloaded Operators in Python

Operator overloading in Python allows you to define custom behavior for built-in operators. Below are some common operators that can be overloaded in Python along with their respective meanings:

- `__sub__`: Subtraction (`-`)
- `__mul__`: Multiplication (`*`)
- `__truediv__`: True division (`/`)
- `__floordiv__`: Floor division (`//`)
- `__mod__`: Modulo (`%`)
- `__pow__`: Exponentiation (`**`)
- `__lt__`: Less than (`<`)
- `__le__`: Less than or equal to (`<=`)
- `__eq__`: Equal to (`==`)
- `__ne__`: Not equal to (`!=`)
- `__gt__`: Greater than (`>`)
- `__ge__`: Greater than or equal to (`>=`)

These are just a few examples of operators that can be overloaded in Python. You can also define custom behavior for other operators, such as bitwise operators (`&`, `|`, `^`, `<<`, `>>`), comparison operators (`in`, `not in`, `is`, `is not`), and others.

Operator overloading can make your code more expressive and readable by allowing you to use built-in operators with custom objects in a natural way. However, it's important to use operator overloading judiciously and only when it makes sense in the context of your code.


-----------------------------------------------------------------
### Multiple Inheritance 
  
Multiple inheritance in Python is the feature that allows a class to inherit attributes and methods from more than one parent class. This means that a child class can inherit from multiple parent classes, which can be useful for code reuse and organizing code in a more modular way.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

########### Multiple inheritance

class Pet(Dog, Cat):
    pass

my_pet = Pet("Fido")
print(my_pet.speak()) # Output: "Woof!"
```

-----------------------------------------------------------------
### Multilevel Inheritance
  
sequence of exe of constructor for 3 level of inheritance  
 
In Python, when you create an instance of a class, the constructor method `__init__()` is automatically invoked. This applies to all classes in the inheritance chain.

Let's consider a three-level inheritance hierarchy with classes A, B, and C, where C inherits from B, and B inherits from A. Each class has its own `__init__()` method.

1. When you create an instance of class C, Python first looks for `__init__()` in C. If it's not found, it looks in B, and then in A. This is known as the method resolution order (MRO).
2. If Python finds the `__init__()` method in C, it executes it and stops searching.
3. If `__init__()` isn't found in C, but is found in B, it executes the `__init__()` method of B and stops searching.
4. If `__init__()` isn't found in C or B, but is found in A, it executes the `__init__()` method of A and stops searching.

```python
class A:
    def __init__(self):
        print("A's constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("B's constructor")

class C(B):
    def __init__(self):
        super().__init__()
        print("C's constructor")

c = C()

# Output
# A's constructor
# B's constructor
# C's constructor

```

In this example, C inherits from B, and B inherits from A. When you create an instance c of C, Python first looks for __init__() in C, but it's not found. It then looks in B, where it's found, and executes B's __init__() method. The super().__init__() call in B calls A's __init__() method. Finally, C's __init__() method is executed, and the output is:


-----------------------------------------------------------------
### Constructor -- called in multiple inheritance
  
In multiple inheritance in Python, the constructor (__init__ method) of each class in the inheritance chain is called according to the method resolution order (MRO). The MRO is determined at runtime and follows a specific algorithm (C3 linearization) that ensures the classes are searched in a consistent order.

```python

class A:
    def __init__(self):
        print("A's constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("B's constructor")

class C(A):
    def __init__(self):
        super().__init__()
        print("C's constructor")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D's constructor")

d = D()

# Output
# A's constructor
# B's constructor
# D's constructor

```

In this example, `D` inherits from both `B` and `C`, which in turn inherit from `A`. When you create an instance `d` of `D`, Python follows these steps:

1. It looks for `__init__()` in `D`, but it's not found.
2. It then looks in `B`, where it's found. The `super().__init__()` call in `B` calls `A`'s `__init__()` method.
3. After the constructor of `A` is executed, the constructor of `B` is executed.
4. Finally, the constructor of `D` is executed.



-----------------------------------------------------------------
### Hybrid Inheritance 
  
Hybrid Inheritance refers to the combination of two or more types of inheritance within a single class or inheritance hierarchy. This means that a class can inherit from more than one parent class or have multiple parent classes, each of which could use different types of inheritance like single, multiple, or multilevel inheritance. In Python, this is achieved by defining a class that inherits from more than one class.

```python

class A:
    def methodA(self):
        print("Method A")

class B(A):
    def methodB(self):
        print("Method B")

class C:
    def methodC(self):
        print("Method C")

class D(B, C):
    def methodD(self):
        print("Method D")

obj = D()
obj.methodA() # Output: Method A
obj.methodB() # Output: Method B
obj.methodC() # Output: Method C
obj.methodD() # Output: Method D
```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
### 
  
  
```python



```

-----------------------------------------------------------------
