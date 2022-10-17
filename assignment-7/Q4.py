Age = int(input("Enter your age in year :"))

match Age:
    case Age if 0<=Age<10 :
        print("you are kid")
    
    case Age if 10<=Age<20 :
        print ("you are teen")
    
    case Age if 20<=Age<40 :
        print ("you are young")
    
    case Age if 40<=Age<60 :
        print ("you are Experienced")
    
    case Age if Age>=60 :
        print ("you are Senior Citizen")
    
    case _:
        print ("invalid age")    
