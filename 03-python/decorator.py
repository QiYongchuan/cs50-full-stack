# decorator is going to be a function that take a function as input and ruturn a modified version of that function as output

#In python ,a function is just a value like any other,you can pass it as as input to another function,
# you can get it as the output of another function
# and this is known as a functional programming paradigm.  
# functions are themselves values

def announce(f):
  def wrapper():
    print("About to run the function....")
    f()
    print("Done with the function")
  return wrapper

@announce
def hello():
  print("Hello,world!")
  
hello()

#在这里，装饰器起到的作用是为一个函数添加新的功能