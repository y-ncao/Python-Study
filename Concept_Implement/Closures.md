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


