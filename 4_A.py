print("Enter your choice:")
print("1.C TO F")
print("2.F TO C")
print("3.C TO K")
print("4.K TO C")
print("5.Print the list")
print("6.Exit the program")
list =[]

def CtoF(t):
    far = t*(9/5)+32.0
    tuple={t,far}
    print(tuple)
    list.append(tuple)
def FtoC(t):
    cel = (t-32.0)*5/9
    tuple={t,cel}
    print(tuple)
    list.append(tuple)
def CtoK(t):
    kel = t+273.15
    tuple={t,kel}
    print(tuple)
    list.append(tuple)
def KtoC(t):
    cel = t+273.15
    tuple={t,cel}
    print(tuple)
    list.append(tuple)

while True :
    num = int(input("Give your choice"))
    if num==1:
        temp = float(input("Give Temperature"))
        CtoF(temp)
        # list.append()
    elif num==2:
        temp = float(input("Give Temperature"))
        FtoC(temp)
    elif num==3:
        temp = float(input("Give Temperature"))
        CtoK(temp)
    elif num==4:
        temp = float(input("Give Temperature"))
        KtoC(temp)
    elif num==5:
        print(list)
    elif num==6:
        break
    else:
        print("Invalid choice \nProgram Ended")
        break
