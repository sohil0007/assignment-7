num = int(input("Enter a Number :"))

match num:
    case num if num>0:
        print("positive")
    case num if num<0:
        print("negative")
    case num if num==0:
        print("zero")
    case _:
        print("invalid enter number")
