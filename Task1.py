def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)

x = int(input("enter a number :"))

result = factorial(x)
print("Factorial of",x,"is:",result)