#Interview Key Words
* Big-O
* Sorting. quicksort, mergesort and all their complexity.
* Hashtable 仔细想想确实是, 好多面试都会面这个, 自己不如尝试implement一下.
* b Trees 除了tree的基础题(其实已经蛮多的了), 最好还能看看n-ary tree, trie-trees. Red/black tree, splay tree or AVL tree. BFS DFS in-order, post-order and pre-order.
* Graphs 这个是我最薄弱的地方, 但是说实话, 真的会经常面试到, 这里一定要好好准备.  

  There are three basic ways to represent a graph in memory (objects and pointers, matrix, and adjacency list). Also BFS and DFS in 伪代码. Dijkstra and A(卧槽这两个实在是太fancy了).

  还有一些有空时候看的东西. About NP-complete problems(NP完全), Traverling Salesman Problem(旅行推销员问题) and Knapsack Problem(背包问题)

* Math, 这个简单, 主要是离散数学, 稍微复习一下排列组合.
* OS, 妈的这里实在是太蛋疼了, 实际真的都是经验之谈, 但是有好多傻逼的概念需要fresh-up
  * Locks, Mutexes, Semaphores, Monitors
  * Deadlock and lovelock and how to avoid them
  * What resources a processes needs, and a thread needs
  * Context switching
  * Scheduling -> multi-core (Look Doug Lea's Concurrent Programming in Java)

#[Python](https://docs.python.org/2/faq/programming.html#what-is-a-class)

##Important Concepts

###[Data Models](https://docs.python.org/2/reference/datamodel.html#attribute-access)
###[Descriptor](https://docs.python.org/2/howto/descriptor.html)
[Another paper](http://www.cafepy.com/article/python_attributes_and_methods/python_attributes_and_methods.html)
[PPT](http://www.aleax.it/Python/osc05_bla_dp.pdf)

####Definition
If any of ```__get__(), __set__(), and __delete__()``` these methods are defined for an object, it is said to be a descriptor.

####Descriptor Protocol
```python
descr.__get__(self, obj, type=None) --> value
descr.__set__(self, obj, value) --> None
descr.__delete__(self, obj) --> None
```

####Invoking
* For objects, the machinery is in ```object.__getattribute__()``` which transforms ```b.x``` into ```type(b).__dict__['x'].__get__(b, type(b))```.
* For classes, the machinery is in ```type.__getattribute__()``` which transforms ```B.x``` into ```B.__dict__['x'].__get__(None, B)```.

* descriptors are invoked by the ```__getattribute__()``` method
* overriding ```__getattribute__()``` prevents automatic descriptor calls
* ```__getattribute__()``` is only available with new style classes and objects (感觉就这句话说的不是天书)
* ```object.__getattribute__()``` and ```type.__getattribute__()``` make different calls to ```__get__()```.
* data descriptors always override instance dictionaries.
* non-data descriptors may be overridden by instance dictionaries.

####[Use Case](https://docs.python.org/2/howto/descriptor.html#descriptor-example)
感觉看了这里才稍微有点点知道这东西是干吗用的

####[Property](https://docs.python.org/2/howto/descriptor.html#properties)
property(fget=None, fset=None, fdel=None, doc=None) -> property attribute
我觉得[这个](https://docs.python.org/3.3/library/functions.html#property)才讲的比较清楚
```
x = property(getx, setx, delx, "I'm the 'x' property.")
```
If then c is an instance of C, c.x will invoke the getter, c.x = value will invoke the setter and del c.x the deleter.

####Bound vs Unbound
* 从instance访问, 返回bound method
* 从Class访问, 返回unbound method

感觉Unbound method主要就是没有绑定instance的method. 一般来说是不能运行的, 但是如果用了decorator @staticmethod, 就可以tell metaclass type not to create a bound method.

####[Static Methods and Class Methods](https://docs.python.org/2/howto/descriptor.html#static-methods-and-class-methods)
* Static Methods: return the underlying function without changes. Good candidates for static methods are methods that do not reference the self variable.
* Class Methods: function only needs to have a class reference and does not care about any underlying data.

###Decorator
Decorators allow you to inject or modify code in functions or classes". In other words decorators allow you to wrap a function or class method call and execute some code before or after the execution of the original code. And also you can nest them e.g. to use more than one decorator for a specific function. Usage examples include – logging the calls to specific method, checking for permission(s), checking and/or modifying the arguments passed to the method etc.

A implement of decorator is classmethod() and staticmethod()

```
@f1(arg)
@f2
class Foo: pass
```
is equivalent to
```
class Foo: pass
Foo = f1(arg)(f2(Foo))
```

######The decorator is solving problems by avoid doing closure way

###[Closure](./Concept_Implement/Closures.md) and nonlocal (说到closure就应该想到nonlocal)
* ```locals()```

Update and return a dictionary representing the current local symbol table. Free variables are returned by locals() when it is called in function blocks, but not in class blocks.
太长了的[解释](https://gist.github.com/DmitrySoshnikov/700292), 但是挺好.

* 另外一个[解释](http://stackoverflow.com/questions/4020419/closures-in-python)

###dir
* dir(x) is used to find out which names does module x defines. Including variables, modules, functions, etc.
* Without arguments, dir() lists the names you have defined currently.
```
>>>import __builtin__
>>>dir(__builtin__)
```
And you will get a lot

###[Classmethod vs Staticmethod](http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner)
First of all, both of ```@classmethod and @staticmethod``` are decorators.
* ```@classmethod``` means: when this method is called, we pass the class as the first argument instead of the instance of that class (as we normally do with methods). This means you can use the class and its properties inside that method rather than a particular instance.
  Parse something into the method an return an object. Like ```Date.from_string('11-09-2012')``` where ```def from_string(cls, date_as_string):``` pass the cls(in the place where self should go) in.

* ```@staticmethod``` means: when this method is called, we don't pass an instance of the class to it (as we normally do with methods). This means you can put a function inside a class but you can't access the instance of that class (this is useful when your method does not use the instance).
  Nothing more than a function defined inside a class. Think example of ```Date.is_date_valid()``` and ```Math``` functions.

###[Magic Methods](http://www.rafekettler.com/magicmethods.html)
* Can use dir() to check what methods does an object own.
* ```__getitem__()``` 用于像list get index, dict get key的方法.
* ```__getattribute__()``` 用于调用一个dir()之后可以看到的method.
* ```__dict___()``` 用于得到object的内部变量?
* ```dir()``` 用于得到object的method(attribute)

###[New Class vs Old Class](http://stackoverflow.com/questions/54867/old-style-and-new-style-classes-in-python)
* If x is an instance of an old-style class, then ```x.__class__``` designates the class of x, but type(x) is always <type 'instance'>.
* If x is an instance of a new-style class, then type(x) is the same as ```x.__class__```.
* For compatibility reasons, classes are still old-style by default.
* Python 3 only has new-style classes.

###[Metaclass](http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python)
* Metaclasses are the 'stuff' that creates classes.
* type is the built-in metaclass Python uses, but of course, you can create your own metaclass. ```MyClass = type('MyClass', (), {})```
```python
type(name of the class,
     tuple of the parent class (for inheritance, can be empty),
     dictionary containing attributes names and values)
```
```python
>>> class MyShinyClass(object):
...       pass
```
can be created manually this way:
```python
>>> MyShinyClass = type('MyShinyClass', (), {}) # returns a class object
>>> print(MyShinyClass)
<class '__main__.MyShinyClass'>
>>> print(MyShinyClass()) # create an instance with the class
<__main__.MyShinyClass object at 0x8997cec>
```

#####Usage
* intercept a class creation
* modify the class
* return the modified class

#####Why metaclass over function?
* The intention is clear. When you read UpperAttrMetaclass(type), you know what's going to follow
* You can use OOP. Metaclass can inherit from metaclass, override parent methods. Metaclasses can even use metaclasses.
* You can structure your code better. You never use metaclasses for something as trivial as the above example. It's usually for something complicated. Having the ability to make several methods and group them in one class is very useful to make the code easier to read.
* You can hook on ```__new__```, ```__init__``` and ```__call__```. Which will allow you to do different stuff. Even if usually you can do it all in ```__new__```, some people are just more comfortable using __init__.
* These are called metaclasses, damn it! It must mean something!

#####Use Case
The main use case for a metaclass is creating an API. A typical example of this is the Django ORM.

classes are themselves instances. Of metaclasses.

###[Abstract Class](http://pymotw.com/2/abc/)

Abstract base classes are a form of interface checking more strict than individual hasattr() checks for particular methods.

#####Why?
Define a set of subclasses, so for large project, you won't forget to miss one of the method.

#####Work

```python
import abc

class PluginBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source and return an object."""
        return

    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output."""
        return
```

#####Two ways to make this work:
* [Registering a Concrete Class](http://pymotw.com/2/abc/#registering-a-concrete-class) ```PluginBase.register(RegisteredImplementation)```
* [Implementation Through Subclassing](http://pymotw.com/2/abc/#implementation-through-subclassing) ```class SubclassImplementation(PluginBase):```

###Some Words
* [Duck-Typing](https://docs.python.org/2/glossary.html#term-duck-typing)

-----

###[Yield](http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python)
* Similar to return, but it returns a generator.
* When you call the function, the code you have written in the function body does not run. It's because they do not store all the values in memory, they generate the values on the fly.

###Itertool
```python
import itertools
horses = [1,2,3,4]
races = itertools.permutations(horses)
print list(races)
```

###[Iterables, Iterators, Generators, Itertool](http://blog.chinaunix.net/uid-15174104-id-4172583.html)

####Generator
* Generator is generated by functions using __yield__ or using generator expression
* It can be used only once. First time you call generator_a, it can return you everything in it. But second time it will only return you empty list
* Way to generate/call it:
```
gx = (x ** 2 for x in xrange(10))
print list(gx)
# Or
gx.next()
```
* Like the discussion above on yield, the generator isn't "generated" until it is called by next().
* So if we need to iterate again the whole generator, we need to re-gen the generator.
* Stops when raising StopIteration
* Generator doesn't support indexing or slicing. Also can't add anything.

#####[Generator Expression](http://legacy.python.org/dev/peps/pep-0289/)
Compare to list comprehension

1. Generator doesn't support indexing or slicing. Also can't add anything.
2. [But save memory](http://stackoverflow.com/a/47792)

#####Conclusion
1. 必须包含yield语句的函数。
2. 在调用时不会运行。
3. 调用生成器时生成的生成器对象只能被使用一次（遍历）。
4. 返回迭代器，但是不用关心迭代协议。

#####Why use Generator
If you have infinite loops, or it may make inefficient use of memory when you have a really long list.

####Iterable
* This is a type of objects. 这类对象能够每次返回它的一个element, 换句话说就是任何可以iterate的对象. 具体一点就是, 任何定义了```__iter__() or getitem()```的对象.
* 例如 list, str, tuple, dict, file, xrange等等
* iter(iterable) -> iterator object
* 核心是implement iterable protocol
  1. Built-in lists, dictionaries, tuples, sets, files.
  2. User defined classes that implement ```__iter__()```.
  3. Generators.

####Sequence定义
1. Iterable
2. Supports efficient element access using integer indices via the ```__getitem__()``` special method and defines a ```__len__()``` method that returns the length of the sequence.
   也就是必须要支持下标搜索, 所以dict是一个iterable, 但是不是sequence.

####Iterator
* 通过调用```__iter__(object)```来得到iterator
* 通过调用next()来获取下一个element

Iterator Protocol就是implement以上两个method.

####关系
* 所有的定义了```__iter__() or getitem()```函数的object称作Iterable
* Iterable分为两类
  * Sequence类 (list, tuple, str, ...)
  * Non-sequence类 (dict, set)
* 以上二者的区别在于
  * sequence object can access from index
  * non-sequence object can't

#####[Generator vs Iterator](http://stackoverflow.com/questions/2776829/difference-between-python-generators-vs-iterators)
All Generators must be Iterator, but no vise versa.

####[For循环过程](http://stackoverflow.com/a/237028)
```python
for x in mylist:
    ...loop body...
```
1. Gets an iterator for mylist:
   Call iter(mylist) -> this returns an object with a next() method (or ```__next__()``` in Python 3).
2. Uses the iterator to loop over items:
   Keep calling the next() method on the iterator returned from step 1. The return value from next() is assigned to x and the loop body is executed. If an exception StopIteration is raised from within next(), it means there are no more values in the iterator and the loop is exited.

-----

##Interview
###```__new__() and __init__()```
```__new__``` is static class method, while ```__init__``` is instance method.  ```__new__``` has to create the instance first, so ```__init__``` can initialize it. Note that ```__init__``` takes self as parameter. Until you create instance there is no self.

###isinstance(inst, class)
Use this function to check if an object is an instance of a given class or of a subclass of it.

### [With Statement](http://effbot.org/zone/python-with-statement.htm)
In a few words the with statement allows you to executed code before and/or after a specific set of operations. For example if you open a file for reading and parsing no matter what happens during the parsing you want to be sure that at the end the file is closed. This is normally achieved using the try… finally construction but the with statement simplifies it usin the so called “context management protocol”. To use it with your own objects you just have to define ```__enter__``` and ```__exit__``` methods. Some standard objects like the file object automatically support this protocol. For more information you may check Understanding Python’s “with” statement.


###[Underscore and Double Underscore](http://stackoverflow.com/questions/1301346/the-meaning-of-a-single-and-a-double-underscore-before-an-object-name-in-python)
* Names, in a class, with a leading underscore are simply to indicate to other programmers that the attribute or method is intended to be private. However, nothing special is done with the name itself.
* ```_single_leading_underscore```: weak "internal use" indicator. E.g. from M import * does not import objects whose name starts with an underscore.
* ```__foo__```: this is just a convention, a way for the Python system to use names that won't conflict with user names.
* ```_foo```: this is just a convention, a way for the programmer to indicate that the variable is private (whatever that means in Python).
* ```__foo```: this has real meaning: the interpreter replaces this name with ```_classname__foo``` as a way to ensure that the name will not overlap with a similar name in another class.  
  __(at least two leading underscores, at most one trailing underscore)__

Private class/method/var are same since everything is object in python.

###PEP8
PEP 8 is a coding convention(a set of recommendations) how to write your Python code in order to make it more readable and useful for those after you.

###Python 2.x to 3.x
* All strings are now Unicode
* Print is now function not a statement.
* There is no range, it has been replaced by xrange which is removed.
* All classes are new style and the division of integers now returns float.

###xrange and range
* range creates a list, so if you do range(1, 10000000) it creates a list in memory with 10000000 elements.
* xrange is a sequence object is a that evaluates lazily.

###Pickling and unpickling
pickle module accepts any python object converts it into a string representation & dumps it into a file(by using dump() function) which can be used later, process is called pickling. Whereas unpickling is process of retrieving original python object from the stored string representation for use.

###```__repr__```vs ```__str__```
machine-headable vs human-readable

###Explain how python is interpreted.
Python program runs directly from the source code. Each type Python programs are executed code is required. Python converts source code written by the programmer into intermediate language which is again translated it into the native language / machine language that is executed. So Python is an Interpreted language.

###How is memory managed in python?
* Memory management in Python involves a private heap containing all Python objects and data structures. Interpreter takes care of Python heap and that the programmer has no access to it.
* The allocation of heap space for Python objects is done by Python memory manager. The core API of Python provides some tools for the programmer to code reliable and more robust program.
* Python also has a build-in garbage collector which recycles all the unused memory. When an object is no longer referenced by the program, the heap space it occupies can be freed. The garbage collector determines objects which are no longer referenced by the program frees the occupied memory and make it available to the heap space.
* The gc module defines functions to enable /disable garbage collector:
  gc.enable() -Enables automatic garbage collection.
  gc.disable() - Disables automatic garbage collection.

###[What is delegation?](https://docs.python.org/2/faq/programming.html#what-is-delegation)
Delegation is an object oriented technique (also called a design pattern). Let’s say you have an object x and want to change the behaviour of just one of its methods. You can create a new class that provides a new implementation of the method you’re interested in changing and delegates all other methods to the corresponding method of x.

Need to see the example from the above link.

###Write a sample program to print the complete contents of a file, with a way to catch a missing file.
```python
try:
    with open('filename','r') as file:
    print file.read()
except IOError:
    print 'no such file exists'
```

###Write a sample program to print the length of each line in a particular file, not counting whitespace at the ends.
```python
with open('filename.txt', 'r') as file:
    print len(file.readline().rstrip())
```

###Remove Duplicates
```python
list(set(dup_list))
```

###Random
* random() - generate(0,1)

###Python vs Other Languages
1. Python is script language, Java C++ compiling language.
2. Simpler

###Python数字精度问题
Flexible精度, you can test it by doing
```
import sys
sys.getsizeof(x)
```
where x is the number.
You can get 24 or 36.
```
print sys.maxint
```
Also

```
>>> print type(1<<62)
<type 'int'>
>>> print type(1<<63)
<type 'long'>
```
[But note this depends on the system is 32bit or 64bit](http://stackoverflow.com/a/2104962/1939805)

-----

##My Search
###Lambda
* ```sorted(student_tuples, key=lambda student: student[2])```

###List/Dict Comprehension:
* ```[x**2 for x in range(10)]```
* ```{str(x): x+1 for x in range(10)}```

###Python Pros and Cons

#####Pros
* Cleaner Syntax
* No brackets, use indentation, which I'm comfortable with
* Easier to test, no need to compile. Type python in terminal you can start testing.

#####Cons
* Lack of true multiprocessor support
* Slow - Performance not good
* Lacks any sort of data protection, use __ instead
* All strings are not unicode by default (Fixed in Python3)

###[Python's Thread](http://pymotw.com/2/threading/)
```python
# An very basic example
import threading

def worker(num):
    """thread worker function"""
    print 'Worker: %s' % num
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
```

#####Current Thread
```python
threading.currentThread().getName()
```

#####Daemon vs. Non-Daemon Threads
意思就是daeomon thread will run wihtout blocking main program from exiting
如果不设的话主程序会等待所有thread运行完毕

#####Subclass 应该用
```python
class MyThread(threading.Thread):
    def run(self):
      logging.debug('running')
      return
```
重写```run()```函数

#####Signaling Between Threads 用```threading.Event()```在thread之间传递信号

#####[Lock](http://pymotw.com/2/threading/#controlling-access-to-resources)
Python’s built-in data structures (lists, dictionaries, etc.) are thread-safe as a side-effect of having atomic byte-codes for manipulating them (the GIL is not released in the middle of an update). Other data structures implemented in Python, or simpler types like integers and floats, don’t have that protection. To guard against simultaneous access to an object, use a Lock object.
```python
lock = threading.Lock()
lock.acquire()
lock.release()
```
注意如果是普通的lock.acquire()就会一直等着lock release，程序就sb了
但是可以用
```python
lock.acquire(0)
# or
lock = threading.RLock()
```
这样只会try一下，如果锁死就干别的去了

#####[Semaphore](http://pymotw.com/2/threading/#limiting-concurrent-access-to-resources)
Allow more than one worker access to a resource at a time(其实就是一个带counter的lock)
```python
threading.Semaphore(2)
```

#####[GIL](http://stackoverflow.com/questions/34020/are-python-threads-buggy) Global Interpreter Lock
Cpython use OS threads. Only one thread at a time is allowed to run Python code.
* Use multiple python interpreters concurrently,
* Use different implementation of Python that does not use a GIL, like Jython and IronPython.

###[Class Attributes](http://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide#.)

###Override and Overload
* Overloading(same func name, but different parameters) - Can use default value like ```def func(self, abc = None)```
  __Python does NOT support overloading__
* Override - 就是正常的override, 自己去试以下

###Import
1. import SomeModule
  可以用import SomeModule.SomeName 调用时用 SomeModule.SomeName()
2. from SomeModule import SomeName
  可以直接用 SomeName()
3. from SomeModule import *
  可能mess up with your namespaces

###Self
Used by method or anything inside a class to access method or varibles inside
To use a reference of itself

###Namespace
* [A](http://stackoverflow.com/questions/3913217/what-are-python-namespaces-all-about)
* [B](http://bytebaker.com/2008/07/30/python-namespaces/)

###[args, kargs](http://stackoverflow.com/questions/3394835/args-and-kwargs)

* All the keyword arguments passed must match one of the arguments accepted by the function, and their order is not important. This also includes non-optional arguments.
* No argument may receive a value more than once.
```python
def foo(kind, *args, **kwargs):
    for value in args:
        print value
    for key, value in kwargs:
        print key, value
```

###[Pass by Assignment](http://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference)
1. If passing a mutable object, the method got an reference of the object and you can change it. But if you rebind the reference, outer scope wouldn't know
2. Immutable object is changed by rebind, so outer scope wouldn't know.

-----

Assignment Creates References, Not Copies

This is a core Python concept, which can cause problems when its behavior isn't expected. In the following example, the list object assigned to the name L is referenced both from L and from inside of the list assigned to name M. Changing L in place changes what M references, too, because there are two references to the same object:

```python
>>> L = [1, 2, 3]        # A shared list object
>>> M = ['X', L, 'Y']    # Embed a reference to L
>>> M
['X', [1, 2, 3], 'Y']

>>> L[1] = 0             # Changes M too
>>> M
['X', [1, 0, 3], 'Y']
```

This effect usually becomes important only in larger programs, and shared references are normally exactly what you want. If they're not, you can avoid sharing objects by copying them explicitly; for lists, you can make a top-level copy by using an empty-limits slice:

```python
>>> L = [1, 2, 3]
>>> M = ['X', L[:], 'Y']   # Embed a copy of L

>>> L[1] = 0               # Change only L, not M
>>> L
[1, 0, 3]
>>> M
['X', [1, 2, 3], 'Y']
```

Slice limits default to 0 and the length of the sequence being sliced. If both are omitted, the slice extracts every item in the sequence, and so makes a top-level copy (a new, unshared object). For dictionaries, use the dict.copy() method.

###Basic Immutable types
Numbers, Strings, Tuples

Immutable Types Can't Be Changed in Place. Remember that you can't change an immutable object.

###Exception and Error

####Common Errors
* ZeroDivisionError
* NameError
* TypeError
* RuntimeError

######[Why are Python exceptions named “Error”?](http://stackoverflow.com/questions/2903827/why-are-python-exceptions-named-error)
因为名字命名要有意义...

```python
try:
    int('100+5')
except ValueError:
    print "Oh I can't"


class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "WRONG %d" % self.value
# 基本就是重写这两个函数
```

###Special Data Structures
* DefaultDict
  ```python
  from collections import defaultdict
  # Use case 1. Similar to setdefault(key, [])
  d = defaultdict(list)
  for k, v in s:
     d[k].append(v)

  # Use case 2
  d = defaultdict(int)
  for k in s:
     d[k] += 1
  ```

* [OrderedDict](./Leetcode/LRU_Cache.py)
  ```python
  from collections import OrderedDict
  # Like LRU Cache
  self.cache = collections.OrderedDict()
  self.cache.popitem(last=False)
  ```

* Set

  Use {1,2,3} to create.

  Another way is:
  ```python
  from sets import Set
  engineers = Set(['John', 'Jane', 'Jack', 'Janice'])
  s.add(x)     # add element x to set s
  s.remove(x)  # remove x from set s; raises KeyError if not present
  s.discard(x) # removes x from set s if present
  s.pop()      # remove and return an arbitrary element from s; raises KeyError if empty
  ```

* Deque
  ######Deque
   * Deque manages its elements with a dynamic array, provides random access, and has almost the same interface as a vector.
   * Deque provides Fast insertions and deletions at both the end and the beginning. Inserting and deleting elements in the middle is relatively slow because all elements up to either of both ends may be moved to make room or to fill a gap.
   * Any insertion or deletion of elements other than at the beginning or end invalidates all pointers, references, and iterators that refer to elements of the deque.

  ######List
   * List manages its elements as a doubly linked list and does not provide random access.
   * In List, inserting and removing elements is fast at each position, and not only at one or both ends.
   * List: Inserting and deleting elements does not invalidate pointers, references, and iterators to other elements.
  Deque is better for insert/delete at begining and ending of the sequence
  ```python
  from collections import deque
  d.append('j')
  d.appendleft('f') # This is what queue should use
  d.pop()           # This is what queue should use
  d.popleft()
  ```

* [Priority Queue](http://pymotw.com/2/heapq/)
  * [Complexity](http://bigocheatsheet.com)
    * heapify O(n)
    * findMax O(1)
    * extractMax O(log(n))
    * insert O(log(n))
    * delete O(log(n))
    * merge O(m+n)
  * heap的存放方式是由上至下由左至右
  * ```import heapq```
  * ```heappush(heap, (value, key))```这里的(value, key)可以只是一个value
  ```python
  pq = []
  heapq.heappush(pq, 1)
  heapq.heappush(pq, -5)
  heapq.heappush(pq, 2)
  # Will have pq = [-5, 1, 2]
  ```
  * ```heapq.heappop(heap)```这个函数本身用途不大, 如果heap是乱的pop的信息也是乱的, 因为他只是个popleft()
  ```python
  heapq.heappop(pq)
  # will get -5
  ```
  * ```heapq.heapify(heap)```可以用来sort heap, 其实就是一个sort
  * ```heapq.heapreplace(heap, value)```可以用来在保持heap same size的同时, 插入一个新数, 这样会有旧数被丢掉.
  * ```nlargest(n, data)``` and ```nsmallest(n, data)```

###Special function
* ```str.isalnum()``` is alphanumeric
* ```str.isalpha()``` is alphabetic
* ```str.isdigit()``` is digits
* ```str.strip()``` 没什么好讲的了
* ```str.split(sep, maxsplit)``` separate by sep. 发现的位置全会被replace by '', 但不会重复  
  ```
  >>>a = 'abssdfcds'
  >>>a.split('s')
  ['ab', '', 'dfcd', '']
  ```

* ```int()``` 如果有空格的话会直接无视，可以正确转化，不能有小数点

-----
##Just Interesting

###["Sticky" Method](http://effbot.org/zone/default-values.htm)
Problem:
```
>>> def function(data=[]):
...     data.append(1)
...     return data
...
>>> function()
[1]
>>> function()
[1, 1]
>>> function()
[1, 1, 1]
```

So when def is called, it creates a function object, and it also evaluates the default values. It will always be the same object when you call function, unless you def a new one.

###Cyclic Datastructures
Cyclic Datastructures Can Cause Loops

Although fairly rare in practice, if a collection object contains a reference to itself, it's called a cyclic object. Python prints a [...] whenever it detects a cycle in the object, rather than getting stuck in an infinite loop:

```python
>>> L = ['grail']  # Append reference back to L
>>> L.append(L)    # Generates cycle in object
>>> L
['grail', [...]]
```

###Reference
[Reference](http://pyzh.readthedocs.org/en/latest/index.html)

-----

#[Hashtable](./Concept_Implement/HashTable.py)
###Using hash function is two steps
1. Map the key to an integer
2. Map the integer to a bucket

###Hash的两个特性:
* Not invertible 不可逆
* Unique deterministic 唯一性

常见的Hash方法是MD5 and SHA1

###简单的Hash Functions:

* __Division method (Cormen)__ Choose a prime that isn't close to a power of 2. h(k) = k mod m. Works badly for many types of patterns in the input data.
* __Knuth Variant__ on Division h(k) = k(k+3) mod m. Supposedly works much better than the raw division method.
* Multiplication Method (Cormen).
  1. Choose m to be a power of 2.
  2. Let A be some random-looking real number. Knuth suggests M = 0.5*(sqrt(5) - 1).
  3. Then do the following:

  ```python
  s = k * A
  x = fractional part of s
  h(k) = floor(m*x)
  ```

This seems to be the method that the theoreticians like.(可能永远都不需要知道)

###Collision
* Open Hashing (支持元素删除)
* Closed Hashing (不支持元素删除)

最重要的一点是Mod by something

```python
class KeyValue:
    def __init__(self,key,value):
        self.key=key
        self.value=value
    def __str__(self):
        return self.key+":"+str(self.value)
class HashTable:
    SIZE=10
    def __init__(self):
        i=0
        self.list=[]
        while i<self.SIZE:
            self.list.append([])
            i=i+1

    def getValue(self,key):
        h = self.hash (key)
        bucket = self.list[h]
        for kv in bucket:
            if kv.key==key:
                return kv.value
    def setValue(self,key,value):
        h = self.hash(key)
        # should search first so we don't put key in twice, but for now ignore
        self.list[h].append(KeyValue(key,value))
    def hash(self,key):
        i=0
        total=0
        while i<len(key):
            total = total+ord(key[i])
            i=i+1
        return total % self.SIZE

htable= HashTable()
htable.setValue("wolber","359-4787")
htable.setValue("reblow","akfj-askf")
print htable.getValue("wolber")
print htable.getValue("reblow")
```

------
#System Design
####By Tiny URL
1. Constrains and Use Cases
   1. Use Cases - What do we use the system for?
      1. Shortening: take a url => return a much shorter url
      2. Redirection: take a short ulr => redirect to the original url
      3. ~~Custom url~~
      4. ~~Analytics~~
      5. ~~Automatic link expiration~~~
      6. ~~Manual link removal~~
      7. ~~UI vs API~~
      8. Highly available
   2. Constrains:
      1. Basic knowledge:
         * 1.3 Billion Facebook active users
         * 650 Million Twitter
         * New Tweets per day 500 Million
      2. 这道题的数据
         1. All shortened URLs per Month: 1.5BN
         2. Sites below the top3: 300M per month
         3. We: 100M per month
         4. 1BN request per month
         5. request by second   400+per second(40 shorten 360 redirects)
         6. Total url 5 years * 12 * 100M: 6Billion url in 5 years
         7. 每个url长度 500bytes: __1 char = 1 byte__ 这个太重要了(ASCII是128=2**7个, 1byte就够了, 但是UTF-8是1~4bytes一个字符)
         8. __url是case sensitive的__
         9. 6 bytes per hash
         10. 注意, 10^3 K->kb, 10^6 M->MB, 10^9 B->GB, 10^12 ->TB
         11. New data written per second 40*(500+6)bytes = 20kb
         12. Data read per second: 360 * 506 bytes = 180k
      3. 重要的几个点
         1. Storage
         2. Data written & Data Read

2. Abstract Design - Finally simple the problem to per second
   1. Application service layer(serves the requests)
      * Shortening Service
      * Redirection Service
   2. Data storage layer(keep track of the hash =>url mapping)
      * Act like a big hash table: stores new mappings and retrieves a value given a key
   3. ```hashed_url = convert_to_base_62(md5(original_url + random_salt))[:6]```
      * Base 62 是一种short ulr的encoding, encode之后只有62种字符0-9 a-z A-Z
3. Understanding Bottlenecks
   * Traffic - not going to be very hard
   * Lots of data - more interesting
4. Scaling Abstract Design
   1. Application Service Layer
      * Start with one machine
      * Measure how far it take us(load tests)
      * Add a load balancer + a cluster of machines over time
        1. to deal with spiky traffice
        2. Also avoid single failure and increase the availability
   2. Data Storage Layer
      1. What's data?
         * Billions of objects
         * Each object is fairly small(<1k)
         * There are no relationship between the objects
         * Reads are 9x more frequent thant writes(360 reads, 40 writes per second)
         * 3TBs of urls, 36GB of hashes
      2. NoSQL vs Relation SQL
         * MySQL:
           * Widely used
           * Mature technology
           * Clear Scaling Paradimgs(sharding, master/slave replication, master/master replication)
           * Used by Facebook, Twitter, Google etc
           * Index lookups are very fast
         * Mappings
           * hash: varchar(6)
           * original_url: varchar(512)
      3. Create a unique index on the hash(36GB+). We want to hold it in memory to speed up lookups.
         1. Vertical Scaling of the MySQL machine (memory is cheap) (vertical for a while)
         2. Partition the data: 5 partitions, 600GB of data, 8GB of indexes (Eventually partiion)
            * We can add more shards in the future. Easier for backup and replicate
            * Default idea of this is: get the first char from the ```hash % num_of_partition```
      4. Master/Slave replication(reading from the slave replicas, writes to the master)(如果有一天read/write不balance了的话) Master/Master

------
总结:
1. 从base开始, 最后变得复杂, 可以一开始vertical, 后面horizontal
2. 核心是从连个方向走
   * Traffic
     1. More server(应该是这里体现consistent hashing, map reduce可能也是这里)
     2. Load balancer()
   * Data
     1. NoSQL vs Relation SQL
     2. 如果小的话就store in memory, 大的话就得考虑sharding(easier for replicate and backup)
     3. 如果读写不均匀的话就分开读写, master/slave replication(reading from slaves and write to master)

------

####From [Harvard Class](https://www.youtube.com/watch?v=-W9F__D3oY4)
1. 形式: Multi-tier architecture
   ![Multi-tier architecture](http://d0.awsstatic.com/architecture-diagrams/customers/arch-anganguera.png)
2. 重要的几个东东西
   * DNS - 可以通过DNS来进行geo based load balancing, ```nslookup google```
   * Firewall - 只允许来自80 443 22 VPN端口的访问. 过了下面那层LB，把443转换成80就行了
     * [Principle of Least Privilege](http://en.wikipedia.org/wiki/Principle_of_least_privilege)
   * Load Balancer
     * 分为软的和硬的  
       Software - Elastic Load Balancing, HAProxy(TCP/HTTP), Linux Virtual Server  
       Hardware - Barracuda, Cisco, Citrix, F5
     * 方法
       * Round robin
       * Weighted round robin
       * Least connections
       * Least response time
       * Layer 7 load balancers can further distribute requests based on application specific data such as HTTP headers, cookies, or data within the application message itself, such as the value of a specific parameter.
     * Heart Beat health check
       * Active/Active - 意味着run full capacity, 如果一个跪了，整体的load balancing速度会降低
       * [Active/passive](http://www.loadbalancerblog.com/blog/2013/01/understanding-active-passive-activeactive-load-balancing)
     * ip-hash 根据ip造server
   * Web Server
     * 可以partition，按照某种方法处理request(例如名字)
   * 在Web Server和Storage之间还可能要有一层Load Balancer
   * Switch - 每个server在联入网的时候都是有两个switch，需要调节好防止packet在中间形成loop
   * Storage
     * NoSQL vs Relational SQL
     * Raid0, Raid1, Raid5, Raid6, Raid10
     * Master/Slave Mode (重点是replica)
       * 一个Master多个Slave, 内容一样，如果Master跪了可以promote一个Slave
       * 分开读写，Master写，Slave读，实时同步(好像有点点SPF)
     * Master/Master Mode
       * 两个Master多个Slave, 就不会跪了

------

###NoSQL vs Relational SQL
* NoSQL
  * MongoDB(Document)
  * Google Big Table (Column)
  * Cassandra (Column)
  * HBase (Column)
  * Amazon DynamoDB(Key-Value Eventually Consistent)
  * Redis(Key-Value RAM)
  * MemcacheDB(Key-Value RAM)
* Eventually Consistent
* Pros:
  * Scalable
  * Flexible
  * It’s Administrator-Friendly
  * It’s Cost-Effective and Open-Source
  * The Cloud’s the Limit
* Cons:
  * A General Lack of Maturity
  * Performance and Scaling > Consistency - Performance and Scaling is good, lack of Consistency

###[Sharding](http://docs.mongodb.org/manual/core/sharding-introduction/)
* Storing data across multiple machines
* Purpose - horizontal scaling
* Advantages
  * Sharding reduces the number of operations each shard handles
  * Sharding reduces the amount of data that each server needs to store.
* 三个重要的structure
  * __Shards__ store the data
  * __Query Routers__ interface with client applications and direct operations to the appropriate shard or shards
  * __Config servers__ store the cluster’s metadata.
* Data Partitioning
  * Range Based Sharding
  * Hash Based Sharding
* Splitting
* Balancing

###[MapReduce](http://michaelnielsen.org/blog/write-your-first-mapreduce-program-in-20-minutes/)
拿这个link的word count作为栗子
* Map is a step to convert each chapter to a dict  
  * 实际栗子里是把combine这步放到这里，把多个chapter组成一个intermediate list
  * 所以，输入是chapter，输出是list of words with count 1, a lot duplidates
* Reduce is a step to combine each list and reduce the duplicate data
  输入是个list，通过使用itertool.groupby()和dict来实现去重，把intermediate信息输入进去，最后得到一个新的reduced list
* Steps
  1. Partitioning data
  2. Apply function to the pieces in parallel without communication to each other between the analyzers
  3. Apply another function to combine the results

###[Consistent Hashing](http://blog.csdn.net/sparkliang/article/details/5279393)
* Naive way to do: hash(k) % n
* four important keys
  * Balancing
  * Monotonicity
  * Spread
  * Load
* 解决的问题：N个server， 需要增加或者减少一台，但是又不想re-hash
* Steps:
  1. 环形hash空间
  2. 把数据对象Objecthash到环形空间
  3. 把Server hash到环形空间
  4. Map Object to Server：顺时针顺着object的key走遇到的第一个Server负责该object
  5. 分析
     * 移除Server
       Server B被移除后，只需要从B出发逆时针找第一个Server，在此之间的所有object都要re-map到Server B的下一个Server
     * 添加Server
       同样是从新的server逆时针出发到上一个server之间object归他管了
* 通过virtual node来提高balance
* 正常hash就直接hash ip就行了 hash('192.168.1.1')， 如果是hash virtual node可以 hash('192.168.1.1#1')

------

#Javascript

###Javascript types
Number, String, Boolean, Function, Object, Null, and Undefined

In JavaScript, __undefined__ means a variable has been declared but has not yet been assigned a value, such as:

```javascript
var TestVar;
alert(TestVar); //shows undefined
alert(typeof TestVar); //shows undefined
```

null is an assignment value. It can be assigned to a variable as a representation of no value:

```javascript
var TestVar = null;
alert(TestVar); //shows null
alert(typeof TestVar); //shows object
```

From the preceding examples, it is clear that undefined and null are two distinct types: undefined is a type itself (undefined) while null is an object.

###[Var](http://stackoverflow.com/questions/1470488/what-is-the-function-of-the-var-keyword-in-ecmascript-262-3rd-edition-javascript)
If you're in the __global__ scope then there's no difference.

If you're in a function then "var" will create a local variable, "no var" will look up the scope chain until it finds the variable or hits the global scope (at which point it will create it):

```javascript
// These are both globals
var foo = 1;
bar = 2;

function()
{
    var foo = 1; // Local
    bar = 2;     // Global

    // Execute an anonymous function
    (function()
    {
        var wibble = 1; // Local
        foo = 2; // Inherits from scope above (creating a closure)
        moo = 3; // Global
    }())
}
```
If you're not doing an assignment then you need to use var:

```javascript
var x; // Declare x
```


###[this](http://stackoverflow.com/questions/133973/how-does-this-keyword-work-within-a-javascript-object-literal)
Javascript's this keyword normally refers to the object that owns the method, but it depends on how a function is called. Basically, it points to the currently in scope object that owns where you are in the code. When working within a Web page, this usually refers to the Window object. If you are in an object created with the new keyword, the this keyword refers to the object being created. When working with event handlers, JavaScript's this keyword will point to the object that generated the event.

###Keep on mind this thing.
```javascript
var elements = [...];
for (var i = 0, n = elements.length; i < n; i++) {
  var el = elements[i];
  el.addEventListener('click', function() {
    doAllOfMayasThingsQuickly(i, el);
  });
}
```

###JavaScript is an object-based language based on prototypes, rather than being class-based.

-----

###In JavaScript, what is the difference between var x = 1 and x = 1? Answer in as much or as little detail as you feel comfortable.
Novice JS programmers might have a basic answer about locals vs globals. Intermediate JS guys should definitely have that answer, and should probably mention function-level scope. Anyone calling themselves an "advanced" JS programmer should be prepared to talk about locals, implied globals, the window object, function-scope, declaration hoisting, and scope chains. Furthermore, I'd love to hear about [[DontDelete]], hoisting precedence (parameters vs var vs function), and undefined.

###Basic JS programmming
Scope of variable
What is Associative Array? How do we use it?

###OOPS JS
Difference between Classic Inheritance and Prototypical Inheritance

What is difference between private variable, public variable and static variable? How we achieve this in JS?
How to add/remove properties to object in run time?
How to achieve inheritance ?
How to extend built-in objects?
Why extending array is bad idea?

###DOM and JS
Difference between browser detection and feature detection
DOM Event Propagation
Event Delegation
Event bubbling V/s Event Capturing

###Misc
Graceful Degradation V/s Progressive Enhancement

###What is the difference between “==” and “===”?
* __==__ checks equality only
* __===__ checks for equality as well as the type

###What are Javascript closures? When would you use them?
Two one sentence summaries:

* a closure is the local variables for a function – kept alive after the function has returned, or * a closure is a stack-frame which is not deallocated when the function returns.

A closure takes place when a function creates an environment that binds local variables to it in such a way that they are kept alive after the function has returned. A closure is a special kind of object that combines two things: a function, and any local variables that were in-scope at the time that the closure was created.

The following code returns a reference to a function:

```javascript
function sayHello2(name) { var text = ‘Hello ‘ + name; // local variable var sayAlert = function() { alert(text); } return sayAlert; }
```
Closures reduce the need to pass state around the application. The inner function has access to the variables in the outer function so there is no need to store the information somewhere that the inner function can get it.

This is important when the inner function will be called after the outer function has exited. The most common example of this is when the inner function is being used to handle an event. In this case you get no control over the arguments that are passed to the function so using a closure to keep track of state can be very convenient.

###[Closure](http://en.wikipedia.org/wiki/Closure%5F%28computer%5Fscience%29)

#Linux
* grep
* awk
* xargs
* wc
* ps -A
* top

###[Compiled Language vs Scripting Language](http://eimg.wordpress.com/2007/12/31/compiled-languages-vs-scripting-languages/)
* Compiled Lanuage - Computers do not actually understand the code we write. We need to translate our human-readable code to machine-readable code. (Java, C, C++)
* Scripting Languages - Languages that not require compilation are called scripting languages. (Perl, PHP, Python and Ruby)

#SQL
###ORM
Object-relational mapping
Like SQLAlchemy

#OS Knowledge

###[REST vs SOAP](http://stackoverflow.com/questions/19884295/soap-vs-rest-differences)
* SOAP and REST can't be compared directly, since the first is a protocol (or at least tries to be) and the second is an architectural style.
* SOAP client works like a desktop application
  * Everything is expected to break if either side changes anything
* [REST client works like a browser](http://en.wikipedia.org/wiki/Representational_state_transfer)
  * Base URI
  * An Internet media type for the data (JSON)
  * standard HTTP methods
  * [hypertext links to reference state](http://en.wikipedia.org/wiki/HATEOAS)
  * hypertext links to reference related resources
  * 还有一个没提的我觉得是cacheable
* Diff
  * You can cache REST but not SOAP
  * SOAP can only do xml but REST supports many data formats
  * stateless vs statuses

###[Encoding](http://kunststube.net/encoding/)
#####Unicode, Ascii, UTF-8
* 1 byte = 8 bit
* Ascii has 128 characters
* ```2**8 = 256```
* UTF-16 and UTF-8 are variable-length encodings. If a character can be represented using a single byte (because its code point is a very small number), UTF-8 will encode it with a single byte. If it requires two bytes, it will use two bytes and so on.
* UTF-8 is an encoding - Unicode is a character set
* UTF-8 and Unicode cannot be compared. UTF-8 is an encoding used to translate binary data into numbers. Unicode is a character set used to translate numbers into characters.
* [How big is Unicdoe](http://en.wikipedia.org/wiki/Unicode) 113,021
* In Python 3, all strings are sequences of Unicode characters. There is a bytes type that holds raw bytes.
* In Python 2, a string may be of type str or of type unicode. You can tell which using code something like this:  
```python
def whatisthis(s):
  if isinstance(s, str):
      print "ordinary string"
  elif isinstance(s, unicode):
      print "unicode string"
  else:
      print "not a string"
```

#####hex and integer
* hex是十六进制表示方法  
  ```
  >>> hex(10)
  '0xa'
  ```
* python会自动转换0x 十六进制的数字为integer
  ```
  >>> a = 0xa
  >>> type(a)
  <type 'int'>
  ```
* ord('d') 会显示这个字符的ascii数字， chr(int) 会转换int变成字符，注意这个int不能超过255
* 于是有了chr(10) == chr(0xa)
* ```'\xhh'```表示的是一个string(其实是一个char)， hh是两位十六进制，比如  
  ```
  >>> '\x29'
  ')'
  ```
* ascii从0~8显示的都是'\x0i' where i in 0~8, 127过后也都是'\xhh'形式的，显示不出来字符本身。
* 于是很逗的现象就是，有些东西只是把十进制转化成十六进制罢了。
  ```
  >>> chr(127)
  '\x7f'
  >>> ord('\x7f')
  127
  ```

###[Big O](http://bigocheatsheet.com/)
* Time Complexity - The amount of time needed to finish the task
* Space Complexity - The amount of memory needed to store values/variables

###Lock
__Lock__: at most one thread can hold the lock, and therefore only on thread can access the shared resource.

__Deadlock__:

* When two threads are waiting each other and can’t precede the program is said to be deadlock.

Or:

* Thread 1 waiting for lock2 which thread2 holds. Thread2 is waiting for lock1 which thread1 holds

###Monitor & Semaphore

A __Monitor__ is an object designed to be accessed from multiple threads. The member functions or methods of a monitor object will enforce mutual exclusion, so only one thread may be performing any action on the object at a given time. If one thread is currently executing a member function of the object then any other thread that tries to call a member function of that object will have to wait until the first has finished. Just a lock

A __Semaphore__ is a lower-level object. You might well use a semaphore to implement a monitor. A semaphore essentially is just a counter. When the counter is positive, if a thread tries to acquire the semaphore then it is allowed, and the counter is decremented. When a thread is done then it releases the semaphore, and increments the counter. __A counter. One example Mutex, hold and wait__.

###Prevention:
1. Mutual Exclusion: Limited access to a resource. Free the limited quantity of resource.增大循环数量或者resource数量
2. Hold and wait: release the lock before request for another resource.
3. No preemption: force other process to release the lock.
4. Circular wait: 减少循环发生的可能性 reduce the occurrence to circular access for a resource.s

###Thread and Process
A __process__ can be thought of as an instance of a program in execution Each process is an in- dependent entity to which system resources (CPU time, memory, etc ) are allocated and each process is executed in a separate address space One process cannot access the variables and data structures of another process If you wish to access another process’ resources, inter-process communications have to be used such as pipes, files, sockets etc

A __thread__ uses the same stack space of a process A process can have multiple threads A key difference between processes and threads is that multiple threads share parts of their state Typically, one allows multiple threads to read and write the same memory (no processes can directly access the memory of another process) However, each thread still has its own registers and its own stack, but other threads can read and write the stack memory

A thread is a particular execution path of a process; when one thread modifies a process resource, the change is immediately visible to sibling threads

###Big vs Little Endian:
In __big endian__, the most significant byte is stored at the memory address location with the lowest address This is akin to left-to-right reading order Little endian is the reverse: the most significant byte is stored at the address with the highest address

###[Memory](http://stackoverflow.com/questions/79923/what-and-where-are-the-stack-and-heap)
* Cpython only involves a private heap containing all python objects.
* Cpython use reference counting for garbage collection.

But Basically,
* Process is on Heap memory.
* Thread is on Stack memory.
* Stack is faster while heap is slower
* stackoverflow for stack while heap is for memory leak


#####Compare
| Stack | Heap |
| --- | --- |
| Stored in computer RAM just like the heap. | Stored in computer RAM just like the stack. |
| Variables created on the stack will go out of scope and automatically deallocate. | Variables on the heap must be destroyed manually and never fall out of scope. The data is freed with delete, delete[] or free |
| Much faster to allocate in comparison to variables on the heap. | Slower to allocate in comparison to variables on the stack. |
| Implemented with an actual stack data structure. | Used on demand to allocate a block of data for use by the program. |
| Stores local data, return addresses, used for parameter passing | Can have fragmentation when there are a lot of allocations and deallocations |
| Can have a stack overflow when too much of the stack is used. (mostly from infinite (or too much) recursion, very large allocations) | In C++ data created on the heap will be pointed to by pointers and allocated with new or malloc |
| Data created on the stack can be used without pointers. | Can have allocation failures if too big of a buffer is requested to be allocated. |
| You would use the stack if you know exactly how much data you need to allocate before compile time and it is not too big. | You would use the heap if you don't know exactly how much data you will need at runtime or if you need to allocate a lot of data.|
| Usually has a maximum size already determined when your program starts | Responsible for memory leaks |

#####[Memory Leak](http://en.wikipedia.org/wiki/Memory_leak)
A memory leak may happen when an object is stored in memory but cannot be accessed by the running code.

#####Stack (Memory)
When a function calls another function which calls another function, this memory goes onto the stack An int (not a pointer to an int) that is created in a function is stored on the stack
#####Heap (Memory)
When you allocate data with new() or malloc(), this data gets stored on the heap

The JVM divided the memory into following sections:

* Heap
* Stack
* Code
* Static

This division of memory is required for its effective management.

* The code section contains your bytecode.
* The Stack section of memory contains methods, local variables and reference variables.
* The Heap section contains Objects (may also contain reference variables).
* The Static section contains Static data/methods.

Of all of the above 4 sections, you need to understand the allocation of memory in Stack & Heap the most, since it will affect your programming efforts

* When a method is called , a frame is created on the top of stack.
* Once a method has completed execution , flow of control returns to the calling method and its corresponding stack frame is flushed.
* Local variables are created in the stack
* Instance variables are created in the heap & are part of the object they belong to.
* Reference variables are created in the stack.

###External Sort
20GB file, one String per line, how to sort them.
Divide the file into x megabytes each, where x is the available memory that we have. Sort each chunk separately and save back to the file system. Once all sorted, we then merge the chunk, one by one. At the end, we will have a fully sorted file.

###what happens when you type in a URL in browser
1. browser checks cache; if requested object is in cache and is fresh, skip to #9
2. browser asks OS for server's IP address
3. OS makes a DNS lookup and replies the IP address to the browser(host/dig)
4. browser opens a TCP connection to server (this step is much more complex with HTTPS)
5. browser sends the HTTP request through TCP connection
6. browser receives HTTP response and may close the TCP connection, or reuse it for another request
7. browser checks if the response is a redirect (3xx result status codes), authorization request (401), error (4xx and 5xx), etc.; these are handled differently from normal responses (2xx)
8. if cacheable, response is stored in cache
9. browser decodes response (e.g. if it's gzipped)
10. browser determines what to do with response (e.g. is it a HTML page, is it an image, is it a sound clip?)
11. browser renders response, or offers a download dialog for unrecognized types

###Transmission Control Protocol (TCP)
1. Transmission Control Protocol (TCP) is a connection oriented protocol, which means the devices should open a connection before transmitting data and should close the connection gracefully after transmitting the data.
2. Transmission Control Protocol (TCP) assure reliable delivery of data to the destination.
3. Transmission Control Protocol (TCP) protocol provides extensive error checking mechanisms such as flow control and acknowledgment of data.
4. Sequencing of data is a feature of Transmission Control Protocol (TCP).
5. Delivery of data is guaranteed if you are using Transmission Control Protocol (TCP).
6. Transmission Control Protocol (TCP) is comparatively slow because of these extensive error checking mechanisms
7. Multiplexing and Demultiplexing is possible in Transmission Control Protocol (TCP) using TCP port numbers.
8. Retransmission of lost packets is possible in Transmission Control Protocol (TCP).

###User Datagram Protocol (UDP)

1. User Datagram Protocol (UDP) is Datagram oriented protocol with no overhead for opening, maintaining, and closing a connection.
2. User Datagram Protocol (UDP) is efficient for broadcast/multicast transmission.
3. User Datagram protocol (UDP) has only the basic error checking mechanism using checksums.
4. There is no sequencing of data in User Datagram protocol (UDP) .
5. The delivery of data cannot be guaranteed in User Datagram protocol (UDP) .
6. User Datagram protocol (UDP) is faster, simpler and more efficient than TCP. However, User Datagram protocol (UDP) it is less robust then TCP
7. Multiplexing and Demultiplexing is possible in User Datagram Protcol (UDP) using UDP port numbers.

There is no retransmission of lost packets in User Datagram Protcol (UDP).

###Serialization
Java provides a mechanism, called object serialization where an object can be represented as a sequence of bytes that includes the object's data as well as information about the object's type and the types of data stored in the object.

After a serialized object has been written into a file, it can be read from the file and deserialized that is, the type information and bytes that represent the object and its data can be used to recreate the object in memory.

#Java & C

###Garbage Collection
* Pros: programmers don’t have to worry about memory deallocation
* Cons: Often run more slowly because of the overhead needed for the system to determine when to deallocate and reclaim memory no longer need.

__两种方法__:

* Reference counting(if no one is keeping a reference to the object, then the object is no longer needed.)
  * Pros: simple and relatively fast
  * Cons: doesn’t handle circular reference

* Mark and sweep: two passes.
  1. Mark all the objects that can be accessed.
  2. Unmarked objects are deallocated.

System.gc() method may be used to call it explicitly.

###Private Constructor
no one outside class can directly instantiate this class. (or provide a static public method). class cannot be inherited

###Executed finally
1. Virtual machine exits.
2. Thread get killed.

###Final, Finally, Finalize

####Final
__variable(primitive)__:value cannot change

__variable(reference)__: reference variable cannot point to any other object on the heap

__method__: method cannot be overridden

__class__: class cannot be subclassed.

####Finally
used after try-catch block which will always be executed.

####Finalize()
callled by the garbage collector when it determinesthat no more references exist.

###C++ vs Java
A very common question in an interview is “describe the differences between C++ and Java ” If you aren’t comfortable with any of these concepts, we recommend reading up on them

1. Java runs in a virtual machine
2. C++ natively supports unsigned arithmetic
3. In Java, parameters are always passed by value (or, with objects, their references are passed by value) In C++, parameters can be passed by value, pointer, or by reference
4. Java has built-in garbage collection
5. C++ allows operator overloading
6. C++ allows multiple inheritance of classes

###Static
* __Method__: Class method Called with Foo DoIt() instead of f DoIt()
* __Variable__: Class variable Has only one copy and is accessed through the class name

###Abstract
* __Class__: Contains abstract methods Can not be instantiated
* __Interface__: All interfaces are implicitly abstract This modifier is optional
* __Method_: Method without a body Class must also be abstract

###Primitive Types:
byte, short, int, long, float, double, boolean, char

###Three Principles
* Encapsulation is the mechanism that binds together code and data it manipulates and keeps both safe from outside interference and misuse. 
* Inheritance is the process by which one object acquires the properties of another object.
继承之后相当于child会copy所有parent内的函数，等于是重新抄写一遍。除非重写，否则一切都是原样。
* Polymorphism is the feature that allows one interface to be used for general class actions.

###Three kinds of Polymorphism:
* Overriding a method from inheritance.
* Implementing a abstract method
* Implementing a Java interface

###Class, Constructor, Casting
__Class__ is a template for multiple objects with similar features and it is a blue print for objects. It defines a type of object according to the data the object can hold and the operations the object can perform.

__Constructor__ is a special kind of method that determines how an object is initialized when created. 

__Constructor and Method__ Constructor will be automatically invoked when an object is created whereas method has to be called explicitly.

__Casting__ is used to convert the value of one type to another.

##Missing Package Access Here

* Method overloading: When a method in a class having the same method name with different arguments is said to be method overloading. 
* Method overriding: When a method in a class having the same method name with same arguments is said to be method overriding.

A package is a collection of classes and interfaces that provides a high-level layer of access protection and name space management.

###Difference between abstract class and interface?(略傻逼)
1. All the methods declared inside an interface are abstract whereas abstract class must have at least one abstract method and others may be concrete or abstract.
2. In abstract class, key word abstract must be used for the methods whereas interface we need not use that keyword for the methods.
3. Abstract class must have subclasses whereas interface can’t have subclasses.

###Thread:
1. __Implementing the java.lang.Runnable interface__

  ```java
  public interface Runnable{
      void run();
  }

  RunnableThreadExample instance = new RunnableThreadExample();
  Thread thread = new Thread(instance);
  thread.start();
  ```

2. __Extending the java.lang.Thread class__

  ```java
  ThreadExample instance = new ThreadExample();
  instance.start();
  ```

Runnable interface 好在：
1. No multiple inheritance
2. Inheriting the full thread class would be excessive.

###Abstract Tips
抽象类中不一定包含抽象方法，但是包含抽象方法的类一定要被声明为抽象类。抽象类本身不具备实际的功能，只能用于派生其子类。抽象类中可以包含构造方法，但是构造方法不能被声明为抽象。

调用抽象类中的方法(抽象方法和非抽象方法)，如果方法是static的，直接 抽象类.方法  就可以了；如果是非static的则必须需要一个继承的非抽象类，然后用这个非抽象类的实例来调用方法。

1. 抽象类可以有实例变量，而接口不能拥有实例变量，接口中的变量都是静态（static）的常量（final）
2. 抽象类可以有非抽象方法，而接口只能有抽象方法。 接口中的所有方法都是抽象方法

###Malloc
Memory allocated using malloc is persistent—i e , it will exist until either the programmer frees the memory or the program is terminated
void *malloc(size_t sz)
Malloc takes as input sz bytes of memory and, if it is successful, returns a void pointer which indicates that it is a pointer to an unknown data type
void free(void * p)
Free releases a block of memory previously allocated with malloc, calloc, or realloc

###HashMap & Hashtable
* Hashtable is synchronized, whereas HashMap is not. This makes HashMap better for non-threaded applications, as unsynchronized Objects typically perform better than synchronized ones.
* Hashtable does not allow null keys or values. HashMap allows one null key and any number of null values.

Map(K,V) is an interface which Hashtable and HashMap implement it.
Priority Queue 可以选择ordered or unordered  反正insert 和extract一个是O(n)一个是O(1)
Heap  insert和extract都是O(logn)

```java
Nested Class
class OuterClass {
    ...
    static class StaticNestedClass {
        ...
    }
    class InnerClass {
        ...
    }
}
```

###Logical grouping of classes
If a class is useful to only one other class, then it is logical to embed it in that class and keep the two together. Nesting such "helper classes" makes their package more streamlined.

###Increased encapsulation
Consider two top-level classes, A and B, where B needs access to members of A that would otherwise be declared private. By hiding class B within class A, A's members can be declared private and B can access them. In addition, B itself can be hidden from the outside world.
More readable, maintainable code Nesting small classes within top-level classes places the code closer to where it is used.

###Static Nested Class
OuterClass.StaticNestedClass nestedObject = new OuterClass.StaticNestedClass();
As with class methods and variables, a static nested class is associated with its outer class. And like static class methods, a static nested class cannot refer directly to instance variables or methods defined in its enclosing class — it can use them only through an object reference.

###Inner Class
An instance of InnerClass can exist only within an instance of OuterClass and has direct access to the methods and fields of its enclosing instance. The next figure illustrates this idea.
OuterClass.InnerClass innerObject = outerObject.new InnerClass();

###Java: Difference between implementing Comparable and Comparator?

####Comparable

A __comparable__ object is capable of comparing itself with another object. The class itself must implements the java.lang.Comparable interface in order to be able to compare its instances.

####Comparator

A __comparator__ object is capable of comparing two different objects. The class is not comparing its instances, but some other class’s instances. This comparator class must implement the java.util.Comparator interface.

-----
Comparable lets a class implement its own comparison:

* It's in __the same class__ (it is often an advantage)
* There can be __only one implementation__ (so you can't use that if you want two different cases)

By comparison, Comparator is an external comparison:

* It is typically in a unique instance (either in the same class or in another place)
* You __name each implementation__ with the way you want to sort things
* You can provide comparators for __classes that you do not control__
* The implementation is __usable even if the first object is null__

-----

###NodeJS
Node.js uses an event-driven, non-blocking I/O model that makes it lightweight and efficient, perfect for data-intensive real-time applications that run across distributed devices.

[Reference](http://www.ibm.com/developerworks/cn/opensource/os-nodejs/)
