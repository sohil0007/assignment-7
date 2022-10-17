y = int(input("Enter year number :"))

match y:
    case y if y%4==0 and y%100!=0:
        print("non century leap year")
    case y if y%400==0:
        print("century leap year")
    case y if y%4!=0 and y%100!=0:
        print("non century non leap year")
    case y if y%400==0 or y%100==0:
        print("century non leap year")     
    
    case _:
        print("non leap year") 
