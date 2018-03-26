n =1
c = int(input("masukan angka : "))
z = int(c / 2)

for q in range(z):
    for x in reversed(range(c)):
        if(0 == x%2):
            print("+ ",end="")
            print("+ ",end="")
        else:
            print("- ",end="")
            print("- ",end="")
    print()
    for x in reversed(range(c)):
        if(0 == x%2):
            print("+ ",end="")
            print("+ ",end="")
        else:
            print("- ",end="")
            print("- ",end="")
    print()
    for x in reversed(range(c)):
        if(0 == x%2):
            print("- ",end="")
            print("- ",end="")
        else:
            print("+ ",end="")
            print("+ ",end="")
    print()
    for x in reversed(range(c)):
        if(0 == x%2):
            print("- ",end="")
            print("- ",end="")
        else:
            print("+ ",end="")
            print("+ ",end="")
    print()
