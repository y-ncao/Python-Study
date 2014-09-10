###Closure in python
```python
def make_closure(a):
    def inner():
        print a
    return inner
    # Notice here returns the func but not runned func

# This is a closure
closure = make_closure('lala')
print closure.__closure__
closure()

print '-' * 10

def make_not_closure(a):
    def inner(a=a):
        print a
    return inner

not_closure = make_not_closure('lala')
print not_closure.__closure__
not_closure()

# In sublime, use cmd B to run
```

###Closure in Javascript

```javascript
function not_closure(){
    var say = "I'm not closure";
    function inner(){
        alert(say);
    }
    inner();
}

not_closure();



function closure(){
    var say = "I'm closure";
    function inner(){
        alert(say);
    }
    return inner; // Here returns the func not the runned func
}

var my_closure = closure();
my_closure();

```

####Definition
* Closures are functions that refer to independent (free) variables.
* A closure is a special kind of object that combines two things: a function, and the environment in which that function was created.
* The environment consists of any local variables that were in-scope at the time that the closure was created.

* Normally, the local variables within a function only exist for the duration of that function's execution.
* Once makeFunc() has finished executing, it is reasonable to expect that the name variable will no longer be accessible.

####Python的closure和javascript的closure是一样的

```python
1 def increase(x):
2    x += 1
3    def inner():
4        print x
5    return inner

>>> a = increase(5)
>>> a()
6
>>> a()
6
```

这段代码有几个地方值得注意的地方
1. line 2的 increase只能发生在outer function. 如果插在3 4 行之间, 会出现UnboundLocalError: local variable 'x' referenced before assignment  
   分析原因是因为如果只是print x的话是没有赋值的, 所以会搜索上一层的namespace, 因为产生了closure, 所以在inner会搜到  
   但是如果存在赋值的话, 就会找当前的namespace. 这里有个小插曲, code is 
```python
def increase(x):
    def inner():
        x.append(5)
        print x
    return inner
```

2. 正确的方式去证明python的closure是
```pytyhon
>>> def increase(x):
...     def inner():
...         x.append(5)
...         print x
...     return inner
>>> a = increase([3])
>>> a()
[3, 5]
>>> a()
[3, 5, 5]
>>> a()
[3, 5, 5, 5]
```

但是

```python
>>> def increase(x):
...     x.append(5)
...     def inner():
...         print x
...     return inner
...
>>> a = increase([3])
>>> a()
[3, 5]
>>> a()
[3, 5]
```

因为后者不能算是closure, 它对data的modify位于outer func

Same in javascript
```javascript
function increase(x){
    x ++;
    return function(){
         alert(x);
    }
}
a = increase(5);

a();  // 6
a();  // 6

```

但是
```javascript
function increase(x){
    return function(){
         x ++;
         alert(x);
    }
}
a = increase(5);

a();  // 6
a();  // 7

```



