a = int(input("Enter Value of a :"))
b = int(input("Enter Value of b :"))
c = int(input("Enter Value of c :"))

print("1.equilateral triangle\n2.isosceles triangle\n3.right angled triangle\n4.Exit")
choice = int(input("choose from above :"))

match choice:
    case 1:
        if a==b==c:
            print("it is equilateral triangle")
        else :
            print("it is not equilateral triangle")

    case 2:
        if a==b or b==c or c==a:
            print("it is isosceles triangle")
        else :
            print("it is not isosceles triangle")

    case 3:
        if (c**2)==(a**2 + b**2) or (b**2)==(a**2 + c**2) or (a**2)==(c**2 + b**2):
            print("it is right angled triangle")
        else :
            print("it is not right angled triangle")

    case 4:
        print("Exit")
    
