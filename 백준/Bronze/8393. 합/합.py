def factorial_iterative(n):
    result=0
    for i in range(1, n+1):
        result+=i
    return result

n = int(input())
print(factorial_iterative(n))