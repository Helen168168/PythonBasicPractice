#Fibonacci数列-斐波那契数列 每个数是前两个数的和
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        print(a, end=' ')
fibonacci(10)