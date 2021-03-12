def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibRange(n1, n2):
    total = 0
    for i in range(n1, n2):
        ans = fibonacci(i)
        if ans % 2 == 0:
            total += ans
    return total


fibRange(1, 33)