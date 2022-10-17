num = int(input("Enter a number :"))

match num:
    
    case num if num%2==0:
        print("Saurabh Shukla")
    
    case num if num>=0 and num%2==1:
        print("Aditya Choudhary")
    
    case num if num<=0 and num%2==1:
        print("Prateek Jain")


