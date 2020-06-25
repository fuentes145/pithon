def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

p = list(str(factorial(100)))
a = list(map (lambda x: int(x), p))
print(a)
c = 0
for i in a:
    c += i
print(c)