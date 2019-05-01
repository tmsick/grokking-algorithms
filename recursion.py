def countdown(n):
    print(n)
    if n > 0:
        countdown(n - 1)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def factorial_detailed(n, tier=0):
    if n == 1:
        return 1
    tab = "  " * tier
    print(tab + "n: " + str(n))
    ans = n * factorial_detailed(n - 1, tier + 1)
    print(tab + "return")
    return ans


ans = factorial_detailed(9)
print(ans)
