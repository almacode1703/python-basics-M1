# take input
a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")

print("\nBefore swapping:")
print("a =", a, "b =", b, "c =", c)

# swap
a, b, c = b, c, a

print("\nAfter swapping:")
print("a =", a, "b =", b, "c =", c)
