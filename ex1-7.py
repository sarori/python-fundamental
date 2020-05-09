def plus(a, b):
    return a + b

result = plus(b = 30, a = 1)
print(result)

def say_hello(name, age):
    return f"hello {name} you are {age} years old"

#return "Hello " + name + " you are " + age + " years old" => 이것도 가능하다.
hello = say_hello("nico", "12")
print(hello)