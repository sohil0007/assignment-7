s1 = input("Enter your favourite colour :")
l1 = ["yellow","blue","orange","white","black","red"]

for colour in l1:
    if colour in s1:
        c=colour
        break

else:
    c="other"    

match c:
    case "yellow":
        print("Monday")
    case "blue":
        print("Tuesday")
    case "orange":
        print("wednesday")
    case "white":
        print("thursday")
    case "black":
        print("friday")
    case "red":
        print("saturday")
    case "other":
        print("Sunday")
            

