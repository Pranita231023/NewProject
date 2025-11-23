import time

# a) Print name n times (for + while)
name = input("Enter name: ")
n = int(input("Enter count: "))

print("\nUsing for loop:")
for i in range(n):
    print(name)

print("\nUsing while loop:")
i = 0
while i < n:
    print(name)
    i += 1

# b) Divide by zero exception
print("\nDivision Example:")
try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    print("Result =", a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# c) Print current time 10 times, 10 sec interval
print("\nCurrent Time (10 times):")
for x in range(10):
    print(time.ctime())
    time.sleep(10)

# d) Read file line-by-line and print word count
print("\nFile Word Count:")
file = input("Enter filename: ")
with open(file) as f:
    for line in f:
        print("Words:", len(line.split()))
