SideA = int(input("Enter the length of side 1: "))
SideB = int(input("Enter the length of side 2: "))
SideC = int(input("Enter the length of side 3: "))

SquareA = SideA ** 2
SquareB = SideB ** 2
SquareC = SideC ** 2

if SquareA == (SquareB + SquareC) or SquareB == (SquareA + SquareC) or SquareC == (SquareB + SquareA):
    print("This is a Right Triangle")
else:
    print("This is NOT a right triangle")
