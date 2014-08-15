##Interview Key Words

* Big-O
Sorting. quicksort, mergesort and all their complexity

* Hashtable 仔细想想确实是, 好多面试都会面这个, 自己不如尝试implement一下
* Trees 除了tree的基础题(其实已经蛮多的了), 最好还能看看n-ary tree, trie-trees. Red/black tree, splay tree or AVL tree. BFS DFS in-order, post-order and pre-order
* Graphs 这个是我最薄弱的地方, 但是说实话, 真的会经常面试到, 这里一定要好好准备
There are three basic ways to represent a graph in memory (objects and pointers, matrix, and adjacency list). Also BFS and DFS in 伪代码. Dijkstra and A*(卧槽这两个实在是太fancy了).
还有一些有空时候看的东西. About NP-complete problems(NP完全), Traverling Salesman Problem(旅行推销员问题) and Knapsack Problem(背包问题)

* Math, 这个简单, 主要是离散数学, 稍微复习一下排列组合
* OS, 妈的这里实在是太蛋疼了, 实际真的都是经验之谈, 但是有好多傻逼的概念需要fresh-up
Locks, Mutexes, Semaphores, Monitors
Deadlock and lovelock and how to avoid them
What resources a processes needs, and a thread needs
Context switching
Scheduling -> multi-core (Look Doug Lea's Concurrent Programming in Java)

-----
##Hashtable
Using hash function is two steps:
* Map the key to an integer
* Map the integer to a bucket

两个特性:
* Not invertible 不可逆
* Unique deterministic 唯一性

MD5 and SHA1
简单的Hash Functions:
* Division method (Cormen) Choose a prime that isn't close to a power of 2. h(k) = k mod m. Works badly for many types of patterns in the input data.
* Knuth Variant on Division h(k) = k(k+3) mod m. Supposedly works much better than the raw division method.
* Multiplication Method (Cormen). Choose m to be a power of 2. Let A be some random-looking real number. Knuth suggests M = 0.5*(sqrt(5) - 1). Then do the following:
```
s = k * A
x = fractional part of s
h(k) = floor(m*x)
```

This seems to be the method that the theoreticians like.(可能永远都不需要知道)
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

##Python
* Lambda
* List/Dict Comprehension: [x**2 for x in range(10)]
* Immutable Types Can't Be Changed in Place. Remember that you can't change an immutable object (e.g., tuple, string) in place:
* Cyclic Datastructures Can Cause Loops
* Although fairly rare in practice, if a collection object contains a reference to itself, it's called a cyclic object. Python prints a [...] whenever it detects a cycle in the object, rather than getting stuck in an infinite loop:
```python
>>> L = ['grail']  # Append reference back to L
>>> L.append(L)    # Generates cycle in object
>>> L
['grail', [...]]
Assignment Creates References, Not Copies
This is a core Python concept, which can cause problems when its behavior isn't expected. In the following example, the list object assigned to the name L is referenced both from L and from inside of the list assigned to name M. Changing L in place changes what M references, too, because there are two references to the same object:
>>> L = [1, 2, 3]        # A shared list object
>>> M = ['X', L, 'Y']    # Embed a reference to L
>>> M
['X', [1, 2, 3], 'Y']

>>> L[1] = 0             # Changes M too
>>> M
['X', [1, 0, 3], 'Y']
This effect usually becomes important only in larger programs, and shared references are normally exactly what you want. If they're not, you can avoid sharing objects by copying them explicitly; for lists, you can make a top-level copy by using an empty-limits slice:
>>> L = [1, 2, 3]
>>> M = ['X', L[:], 'Y']   # Embed a copy of L

>>> L[1] = 0               # Change only L, not M
>>> L
[1, 0, 3]
>>> M
['X', [1, 2, 3], 'Y']
```

Slice limits default to 0 and the length of the sequence being sliced. If both are omitted, the slice extracts every item in the sequence, and so makes a top-level copy (a new, unshared object). For dictionaries, use the dict.copy() method.
Python的basic immutable types: Numbers, Strings, Tuples

##Old Stuff

###Garbage Collection
* Pros: programmers don’t have to worry about memory deallocation
* Cons: Often run more slowly because of the overhead needed for the system to determine when to deallocate and reclaim memory no longer need.

两种方法：
Reference counting(if no one is keeping a reference to the object, then the object is no longer needed.)
* Pros: simple and relatively fast
* Cons: doesn’t handle circular reference

Mark and sweep: two passes. 
1. Mark all the objects that can be accessed. 
2. Unmarked objects are deallocated.
System. gc() method may be used to call it explicitly.

Private Constructor
no one outside class can directly instantiate this class. (or provide a static public method). class cannot be inherited

Executed finally
1.virtual machine exits.
thread get killed.

###Final, Finally, Finalize

Final
variable(primitive):value cannot change
variable(reference): reference variable cannot point to any other object on the heap
method: method cannot be overridden
class: class cannot be subclassed.

Finally
used after try-catch block which will always be executed.

Finalize()
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
* Method: Class method Called with Foo DoIt() instead of f DoIt()
* Variable: Class variable Has only one copy and is accessed through the class name

###Abstract
* Class: Contains abstract methods Can not be instantiated
* Interface: All interfaces are implicitly abstract This modifier is optional
* Method: Method without a body Class must also be abstract

###Primitive Types:
byte short int long float double boolean char

###Three Principles
* Encapsulation is the mechanism that binds together code and data it manipulates and keeps both safe from outside interference and misuse. 
* Inheritance is the process by which one object acquires the properties of another object.
继承之后相当于child会copy所有parent内的函数，等于是重新抄写一遍。除非重写，否则一切都是原样。
* Polymorphism is the feature that allows one interface to be used for general class actions.

####Three kinds of Polymorphism:
* Overriding a method from inheritance.
* Implementing a abstract method
* Implementing a Java interface

###Class, Constructor, Casting
Class is a template for multiple objects with similar features and it is a blue print for objects. It defines a type of object according to the data the object can hold and the operations the object can perform.
Constructor is a special kind of method that determines how an object is initialized when created. 

Constructor and Method  Constructor will be automatically invoked when an object is created whereas method has to be called explicitly.

Casting is used to convert the value of one type to another.

* Method overloading: When a method in a class having the same method name with different arguments is said to be method overloading. 
* Method overriding: When a method in a class having the same method name with same arguments is said to be method overriding.

A package is a collection of classes and interfaces that provides a high-level layer of access protection and name space management.

//问题有点傻逼
####Difference between abstract class and interface?
All the methods declared inside an interface are abstract whereas abstract class must have at least one abstract method and others may be concrete or abstract.
In abstract class, key word abstract must be used for the methods whereas interface we need not use that keyword for the methods.
Abstract class must have subclasses whereas interface can’t have subclasses.

###Thread:
1. Implementing the java.lang.Runnable interface
	public interface Runnable{
		void run();
	}

	RunnableThreadExample instance =new RunnableThreadExample();
	Thread thread=new Thread(instance);
	thread.start();
2. Extending the java.lang.Thread class
	ThreadExample instance=new ThreadExample();
	instance.start();

Runnable interface 好在：
1. No multiple inheritance
2. Inheriting the full thread class would be excessive.

-----

###Lock
* Lock: at most one thread can hold the lock, and therefore only on thread can access the shared resource.
* Deadlock: When two threads are waiting each other and can’t precede the program is said to be deadlock.
Or: 
* Thread 1 waiting for lock2 which thread2 holds. Thread2 is waiting for lock1 which thread1 holds

* A Monitor is an object designed to be accessed from multiple threads. The member functions or methods of a monitor object will enforce mutual exclusion, so only one thread may be performing any action on the object at a given time. If one thread is currently executing a member function of the object then any other thread that tries to call a member function of that object will have to wait until the first has finished. Just a lock

* A Semaphore is a lower-level object. You might well use a semaphore to implement a monitor. A semaphore essentially is just a counter. When the counter is positive, if a thread tries to acquire the semaphore then it is allowed, and the counter is decremented. When a thread is done then it releases the semaphore, and increments the counter. A counter. One example Mutex, hold and wait

####Prevention:
1. Mutual Exclusion: Limited access to a resource. Free the limited quantity of resource.增大循环数量或者resource数量
2. Hold and wait: release the lock before request for another resource.
3. No preemption: force other process to release the lock.
4. Circular wait: 减少循环发生的可能性 reduce the occurrence to circular access for a resource.s

####Thread and Process
A process can be thought of as an instance of a program in execution Each process is an in- dependent entity to which system resources (CPU time, memory, etc ) are allocated and each process is executed in a separate address space One process cannot access the variables and data structures of another process If you wish to access another process’ resources, inter-process communications have to be used such as pipes, files, sockets etc

A thread uses the same stack space of a process A process can have multiple threads A key difference between processes and threads is that multiple threads share parts of their state Typically, one allows multiple threads to read and write the same memory (no processes can directly access the memory of another process) However, each thread still has its own registers and its own stack, but other threads can read and write the stack memory

A thread is a particular execution path of a process; when one thread modifies a process resource, the change is immediately visible to sibling threads

##Big vs Little Endian:
In big endian, the most significant byte is stored at the memory address location with the lowest address This is akin to left-to-right reading order Little endian is the reverse: the most significant byte is stored at the address with the highest address

Stack (Memory)
When a function calls another function which calls another function, this memory goes onto the stack An int (not a pointer to an int) that is created in a function is stored on the stack
Heap (Memory)
When you allocate data with new() or malloc(), this data gets stored on the heap

The JVM divided the memory into following sections.
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

When a method is called , a frame is created on the top of stack.
Once a method has completed execution , flow of control returns to the calling method and its corresponding stack frame is flushed.
Local variables are created in the stack
Instance variables are created in the heap & are part of the object they belong to.
Reference variables are created in the stack.

###Malloc
Memory allocated using malloc is persistent—i e , it will exist until either the programmer frees the memory or the program is terminated
void *malloc(size_t sz)
Malloc takes as input sz bytes of memory and, if it is successful, returns a void pointer which indicates that it is a pointer to an unknown data type
void free(void * p)
Free releases a block of memory previously allocated with malloc, calloc, or realloc

###External Sort
20GB file, one String per line, how to sort them.
Divide the file into x megabytes each, where x is the available memory that we have. Sort each chunk separately and save back to the file system. Once all sorted, we then merge the chunk, one by one. At the end, we will have a fully sorted file.


##Virtual Method/Function
Without "virtual" you get "early binding". Which implementation of the method is used gets decided at compile time based on the type of the pointer that you call through.

With "virtual" you get "late binding". Which implementation of the method is used gets decided at run time based on the type of the pointed-to object - what it was originally constructed as. This is not necessarily what you'd think based on the type of the pointer that points to that object.

```java
class Base
{
  public:
            void Method1 ()  {  std::cout << "Base::Method1" << std::endl;  }
    virtual void Method2 ()  {  std::cout << "Base::Method2" << std::endl;  }
};

class Derived : public Base
{
  public:
    void Method1 ()  {  std::cout << "Derived::Method1" << std::endl;  }
    void Method2 ()  {  std::cout << "Derived::Method2" << std::endl;  }
};

Base* obj = new Derived ();
  //  Note - constructed as Derived, but pointer stored as Base*

obj->Method1 ();  //  Prints "Base::Method1"
obj->Method2 ();  //  Prints "Derived::Method2"
```

###Abstract Tips
抽象类中不一定包含抽象方法，但是包含抽象方法的类一定要被声明为抽象类。抽象类本身不具备实际的功能，只能用于派生其子类。抽象类中可以包含构造方法，但是构造方法不能被声明为抽象。 

调用抽象类中的方法(抽象方法和非抽象方法)，如果方法是static的，直接 抽象类.方法  就可以了；如果是非static的则必须需要一个继承的非抽象类，然后用这个非抽象类的实例来调用方法。

1. 抽象类可以有实例变量，而接口不能拥有实例变量，接口中的变量都是静态（static）的常量（final）
2. 抽象类可以有非抽象方法，而接口只能有抽象方法。 接口中的所有方法都是抽象方法

Implement Heap:
```
PriorityQueue q = new PriorityQueue();   									 //min heap;
PriorityQueue p = new PriorityQueue(int size, Collections.reverseOrder())    //max heap;
```

###HashMap & Hashtable
* Hashtable is synchronized, whereas HashMap is not. This makes HashMap better for non-threaded applications, as unsynchronized Objects typically perform better than synchronized ones.
* Hashtable does not allow null keys or values. HashMap allows one null key and any number of null values.

Map(K,V) is an interface which Hashtable and HashMap implement it.
Priority Queue 可以选择ordered or unordered  反正insert 和extract一个是O(n)一个是O(1)
Heap  insert和extract都是O(logn)

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

Logical grouping of classes If a class is useful to only one other class, then it is logical to embed it in that class and keep the two together. Nesting such "helper classes" makes their package more streamlined.

Increased encapsulation Consider two top-level classes, A and B, where B needs access to members of A that would otherwise be declared private. By hiding class B within class A, A's members can be declared private and B can access them. In addition, B itself can be hidden from the outside world.
More readable, maintainable code Nesting small classes within top-level classes places the code closer to where it is used.

Static Nested Class
OuterClass.StaticNestedClass nestedObject = new OuterClass.StaticNestedClass();
As with class methods and variables, a static nested class is associated with its outer class. And like static class methods, a static nested class cannot refer directly to instance variables or methods defined in its enclosing class — it can use them only through an object reference.

Inner Class
An instance of InnerClass can exist only within an instance of OuterClass and has direct access to the methods and fields of its enclosing instance. The next figure illustrates this idea.
OuterClass.InnerClass innerObject = outerObject.new InnerClass();

Types of Nested Classes


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

##Transmission Control Protocol (TCP)

1. Transmission Control Protocol (TCP) is a connection oriented protocol, which means the devices should open a connection before transmitting data and should close the connection gracefully after transmitting the data.
2. Transmission Control Protocol (TCP) assure reliable delivery of data to the destination.
3. Transmission Control Protocol (TCP) protocol provides extensive error checking mechanisms such as flow control and acknowledgment of data.
4. Sequencing of data is a feature of Transmission Control Protocol (TCP).
5. Delivery of data is guaranteed if you are using Transmission Control Protocol (TCP).
6. Transmission Control Protocol (TCP) is comparatively slow because of these extensive error checking mechanisms
7. Multiplexing and Demultiplexing is possible in Transmission Control Protocol (TCP) using TCP port numbers.
8. Retransmission of lost packets is possible in Transmission Control Protocol (TCP).

##User Datagram Protocol (UDP)

1. User Datagram Protocol (UDP) is Datagram oriented protocol with no overhead for opening, maintaining, and closing a connection.
2. User Datagram Protocol (UDP) is efficient for broadcast/multicast transmission.
3. User Datagram protocol (UDP) has only the basic error checking mechanism using checksums.
4. There is no sequencing of data in User Datagram protocol (UDP) .
5. The delivery of data cannot be guaranteed in User Datagram protocol (UDP) .
6. User Datagram protocol (UDP) is faster, simpler and more efficient than TCP. However, User Datagram protocol (UDP) it is less robust then TCP
7. Multiplexing and Demultiplexing is possible in User Datagram Protcol (UDP) using UDP port numbers.

There is no retransmission of lost packets in User Datagram Protcol (UDP).

##Serialization
Java provides a mechanism, called object serialization where an object can be represented as a sequence of bytes that includes the object's data as well as information about the object's type and the types of data stored in the object.

After a serialized object has been written into a file, it can be read from the file and deserialized that is, the type information and bytes that represent the object and its data can be used to recreate the object in memory.

Comparable lets a class implement its own comparison:

it's in the same class (it is often an advantage)
there can be only one implementation (so you can't use that if you want two different cases)

By comparison, Comparator is an external comparison:

it is typically in a unique instance (either in the same class or in another place)
you name each implementation with the way you want to sort things
you can provide comparators for classes that you do not control
the implementation is usable even if the first object is nullInterview About Javascript

Javascript types: Number, String, Boolean, Function, Object, Null, and Undefined
In JavaScript, undefined means a variable has been declared but has not yet been assigned a value, such as:
var TestVar;
alert(TestVar); //shows undefined
alert(typeof TestVar); //shows undefined
null is an assignment value. It can be assigned to a variable as a representation of no value:
var TestVar = null;
alert(TestVar); //shows null
alert(typeof TestVar); //shows object
From the preceding examples, it is clear that undefined and null are two distinct types: undefined is a type itself (undefined) while null is an object.

###Javascript var question
If you're in the global scope then there's no difference.
If you're in a function then "var" will create a local variable, "no var" will look up the scope chain until it finds the variable or hits the global scope (at which point it will create it)
it doesn't declare global variable, it creates a global property.
http://stackoverflow.com/questions/1470488/what-is-the-function-of-the-var-keyword-in-ecmascript-262-3rd-edition-javascript

###JavaScript's this keyword:
JavaScript's this keyword normally refers to the object that owns the method, but it depends on how a function is called. Basically, it points to the currently in scope object that owns where you are in the code. When working within a Web page, this usually refers to the Window object. If you are in an object created with the new keyword, the this keyword refers to the object being created. When working with event handlers, JavaScript's this keyword will point to the object that generated the event.
Keep on mind this thing
```javascript
var elements = [...];
for (var i = 0, n = elements.length; i < n; i++) {
  var el = elements[i];
  el.addEventListener('click', function() {
    doAllOfMayasThingsQuickly(i, el);
  });
}
```
JavaScript is an object-based language based on prototypes, rather than being class-based.

In JavaScript, what is the difference between var x = 1 and x = 1? Answer in as much or as little detail as you feel comfortable.
Novice JS programmers might have a basic answer about locals vs globals. Intermediate JS guys should definitely have that answer, and should probably mention function-level scope. Anyone calling themselves an "advanced" JS programmer should be prepared to talk about locals, implied globals, the window object, function-scope, declaration hoisting, and scope chains. Furthermore, I'd love to hear about [[DontDelete]], hoisting precedence (parameters vs var vs function), and undefined.
Basic JS programmming
Scope of variable
What is Associative Array? How do we use it?

##OOPS JS
Difference between Classic Inheritance and Prototypical Inheritance

What is difference between private variable, public variable and static variable? How we achieve this in JS?
How to add/remove properties to object in run time?
How to achieve inheritance ?
How to extend built-in objects?
Why extending array is bad idea?

##DOM and JS
Difference between browser detection and feature detection
DOM Event Propagation
Event Delegation
Event bubbling V/s Event Capturing

##Misc
Graceful Degradation V/s Progressive Enhancement

What is the difference between “==” and “===”? 
“==” checks equality only,  “===” checks for equality as well as the type.

What are Javascript closures?When would you use them?
Two one sentence summaries:
* a closure is the local variables for a function – kept alive after the function has returned, or * a closure is a stack-frame which is not deallocated when the function returns.
A closure takes place when a function creates an environment that binds local variables to it in such a way that they are kept alive after the function has returned. A closure is a special kind of object that combines two things: a function, and any local variables that were in-scope at the time that the closure was created.
The following code returns a reference to a function:
function sayHello2(name) { var text = ‘Hello ‘ + name; // local variable var sayAlert = function() { alert(text); } return sayAlert; }
Closures reduce the need to pass state around the application. The inner function has access to the variables in the outer function so there is no need to store the information somewhere that the inner function can get it.
This is important when the inner function will be called after the outer function has exited. The most common example of this is when the inner function is being used to handle an event. In this case you get no control over the arguments that are passed to the function so using a closure to keep track of state can be very convenient.