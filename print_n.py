def display(n):
    if n == 1:
        print(1)
        return
    display(n-1)
    print(n)


def display_opp(n):
    if n == 1:
        print(1)
        return
    print(n)  
    display_opp(n-1)
  

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(3))