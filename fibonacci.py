def fib(n):
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib2(n, count=3, prevPrev=1, prev=1):
    if n < 3:
        return n
    if count > n:
        return prev
    return fib2(n, count + 1, prev, prevPrev + prev)
