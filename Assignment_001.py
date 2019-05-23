def calculator():
    print('WElcome to my Calculator')
    while True:
        try:
            num1 = int(input("Enter 1st NO# : \t "))
            num2 = int(input("Enter 2nd NO# : \t "))
        except:
            print("Please enter Number not Charecters ")
        try:
            oprt = input("Please Enter Operation e.g --> ( +,-,*,/,% ) \n ")
            if oprt =='+':
                print("Resule is -->  "+str(num1+num2))
                break
            if oprt =='-':
                print("Resule is -->  "+str(num1-num2))
                break
            if oprt =='/':
                print("Resule is -->  "+str(num1/num2))
                break
            if oprt =='*':
                print("Resule is -->  "+str(num1*num2))
                break
            if oprt =='%':
                print("Resule is -->  "+str(num1%num2))
                break
        except:
            if oprt != '+' or oprt != '*' or oprt != '/' or oprt != '-' or oprt != '%':
                print("\nPleAse enter correct operation ")

def grade_marks():
    print('WElcome to Grade MArks')

    try:
        obtain_marks = int(input("Enter Your Obtain Marks \n"))
        total_marks = int(input("Enter Total Marks \n"))

        percentage = obtain_marks*100/total_marks
        print("\npercentage --> "+str(percentage)+"%")

        if percentage < 50 and percentage > 0 :
            print("Fail")
        if percentage < 70 and percentage > 50:
            print("C Grade Pass ")
        if percentage < 80 and percentage > 70:
            print("B Grade Pass")
        if percentage < 100 and percentage > 80:
            print("B Grade Pass")

    except:
        print("Please enter Number not Charecters ")



print("ASSIGNMENT NO# 1")
while True:

    op = input("\n1: Run Calculator Program \n2: Run Grade Marks Program \n\t")
    if op == '1':
        calculator()
        break
    if op == '2':
        grade_marks()
        break
    if op != '1' or op != '2':
        print('wrong input !!!\nplease select 1 or 2 ')