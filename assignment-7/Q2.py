num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
choice = int(input("Choose from above :"))

match choice:
    case 1 :
        print("Addition is:",num1+num2)
        
    case 2 :
        print("Subtraction is:",num1-num2)
        
    case 3 :
        print("Multiplication is:",num1*num2)
        
    case 4 :
        print("Division is:",num1/num2)

    case _:
        print("invalid choice")
