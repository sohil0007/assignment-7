s = input("Enter a string :")
s.strip()

match s:
    case s if ' ' in s:
        print("multiword string")

    case _:
        print("Single word stirng")    