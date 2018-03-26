n =1
c = int(input("masukan angka : "))
z = int(c / 2)

print("Right Triangle")
for r in range(z):
    for j in range( r + 1):
        print("*", end = "")
    print()
print("")
print("")
print("Isosceles Triangle")
for r in range(z):
    for j in range( r + 1):
        print("#", end = "")
    print()
for x in reversed(range(z+1)):
    for k in range(x - 1):
        print("#", end= "")
    print()
print("")
print("")
print("Equilateral Triangle")
for x in reversed(range(z)):
    for k in range(x + 1):
        print(" ", end= "")
    for j in reversed(range( z - (x+1))):
        print("&", end= "")
    for m in range(z-x):
        print("&", end= "")
    print()
print("")
print("")
print("diamond")
for x in reversed(range(z)):
    for k in range(x + 1):
        print(" ", end= "")
    for j in reversed(range( z - (x+1))):
        print("^", end= "")
    for m in range(z-x):
        print("^", end= "")
    print()
for x in range(z):
    for k in reversed(range(x + 1)):
        print(" ", end= "")
    for j in range( z -x):
        print("V", end= "")
    for m in reversed(range(z-(x+1))):
        print("V", end= "")
    print()


