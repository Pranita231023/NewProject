def hello():
    n = input("Name: ")
    print("Hello", n)

def calc():
    a = float(input("A: "))
    b = float(input("B: "))
    print(a+b, a-b, a*b, a/b)

def count():
    s = input("String: ")
    print("Words:", len(s.split()))
    print("Chars:", len(s))

def area():
    sh = input("r/t/c: ")
    if sh=="r":
        l=float(input()); b=float(input())
        print(l*b)
    elif sh=="t":
        b=float(input()); h=float(input())
        print(0.5*b*h)
    elif sh=="c":
        r=float(input())
        print(3.14*r*r)

while True:
    print("1) Hello")
    print("2) Calc")
    print("3) Count")
    print("4) Area")
    print("5) Exit")

    ch = input("Choice: ")

    if ch=="1": hello()
    elif ch=="2": calc()
    elif ch=="3": count()
    elif ch=="4": area()
    else: break
